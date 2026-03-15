"""scripts.nlp.doc_auditor — Główny orchestrator audytu dokumentacji.

Łączy GapDetector, DuplicateDetector i RelationMapper w jednym przebiegu.
Zapisuje wyniki do SQLite (tabele z ddl_audit.sql).
Obsługuje CLI (argparse) i programatyczne wywołanie.

Użycie CLI:
    python3 scripts/nlp/doc_auditor.py scan --dir docs/ [--db reports/it_doc_matrix.db]
    python3 scripts/nlp/doc_auditor.py report --run-id <RUN_ID>
    python3 scripts/nlp/doc_auditor.py list-runs

Użycie w kodzie:
    auditor = DocAuditor(db_path="reports/it_doc_matrix.db")
    run_id = auditor.scan(scan_dir=Path("docs/"))
    report = auditor.report(run_id)
    print(report)
"""

from __future__ import annotations

import argparse
import json
import logging
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

from scripts.nlp.gap_detector import GapDetector, GapFinding
from scripts.nlp.duplicate_detector import DuplicateDetector, DuplicateRecord
from scripts.nlp.relation_mapper import RelationMapper, RelationRecord
from scripts.nlp.text_utils import extract_headings, tokenize

_log = logging.getLogger(__name__)

_SCRIPT_DIR = Path(__file__).parent
_DDL_PATH = _SCRIPT_DIR / "ddl_audit.sql"

# Rozszerzenia plików skanowanych jako dokumentacja
_DOC_EXTENSIONS: frozenset[str] = frozenset({".md", ".markdown", ".rst", ".txt"})

# Domyślne katalogi do pominięcia
_SKIP_DIRS: frozenset[str] = frozenset({
    ".git", "__pycache__", ".pytest_cache", "node_modules",
    ".venv", "venv", "env", ".tox",
})


# ---------------------------------------------------------------------------
# DocAuditor
# ---------------------------------------------------------------------------

class DocAuditor:
    """Orchestrator audytu dokumentacji projektowej.

    Args:
        db_path: Ścieżka do pliku SQLite (domyślnie: obok ddl_audit.sql).
        verbose: Czy logować szczegóły na stdout.
    """

    def __init__(
        self,
        db_path: Path | str | None = None,
        verbose: bool = False,
    ) -> None:
        if db_path is None:
            db_path = _SCRIPT_DIR.parent.parent / "reports" / "it_doc_audit.db"
        self._db_path = Path(db_path)
        self._verbose = verbose
        self._gap_detector = GapDetector()
        self._relation_mapper = RelationMapper()
        self._ensure_schema()

    # -------------------------------------------------------------------
    # Publiczne API
    # -------------------------------------------------------------------

    def scan(
        self,
        scan_dir: Path | str,
        *,
        extensions: frozenset[str] = _DOC_EXTENSIONS,
        skip_dirs: frozenset[str] = _SKIP_DIRS,
        config: dict | None = None,
    ) -> str:
        """Skanuj katalog i zapisz wyniki do DB.

        Args:
            scan_dir: Katalog z dokumentami.
            extensions: Rozszerzenia plików do skanowania.
            skip_dirs: Nazwy katalogów do pominięcia.
            config: Opcjonalne parametry audytu (zapisywane w run).

        Returns:
            run_id — identyfikator przebiegu audytu.
        """
        scan_dir = Path(scan_dir).resolve()
        if not scan_dir.exists():
            raise FileNotFoundError(f"Katalog nie istnieje: {scan_dir}")

        run_id = self._new_run_id()
        started_at = self._now()

        # Zarejestruj przebieg
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO doc_audit_runs "
                "(run_id, scanned_dir, started_at, status, config) "
                "VALUES (?, ?, ?, 'running', ?)",
                (run_id, str(scan_dir), started_at, json.dumps(config or {})),
            )

        if self._verbose:
            print(f"[DocAuditor] Scan run={run_id} dir={scan_dir}")

        # Zbierz dokumenty
        docs: dict[str, str] = {}
        for doc_path in self._iter_docs(scan_dir, extensions, skip_dirs):
            try:
                text = doc_path.read_text(encoding="utf-8", errors="replace")
                rel_path = str(doc_path.relative_to(scan_dir))
                docs[rel_path] = text
            except OSError as e:
                _log.warning("Nie można odczytać %s: %s", doc_path, e)

        if self._verbose:
            print(f"[DocAuditor] Znaleziono {len(docs)} dokumentów")

        # Uruchom detektory
        gap_findings = self._run_gap_detection(run_id, docs)
        dup_records = self._run_duplicate_detection(run_id, docs)
        rel_records = self._run_relation_mapping(run_id, docs)

        # Aktualizuj run
        with self._connect() as conn:
            conn.execute(
                "UPDATE doc_audit_runs "
                "SET doc_count=?, finished_at=?, status='done' "
                "WHERE run_id=?",
                (len(docs), self._now(), run_id),
            )

        if self._verbose:
            print(
                f"[DocAuditor] Gotowe: "
                f"{len(gap_findings)} braków, "
                f"{len(dup_records)} duplikatów, "
                f"{len(rel_records)} relacji"
            )

        return run_id

    def report(self, run_id: str) -> str:
        """Wygeneruj tekstowy raport dla danego przebiegu."""
        with self._connect() as conn:
            run = conn.execute(
                "SELECT * FROM doc_audit_runs WHERE run_id=?", (run_id,)
            ).fetchone()
            if not run:
                return f"Run {run_id!r} nie znaleziony."

            completeness = conn.execute(
                "SELECT doc_path, completeness_score, gap_error_count, "
                "gap_warning_count, doc_type "
                "FROM doc_completeness WHERE run_id=? "
                "ORDER BY completeness_score ASC",
                (run_id,),
            ).fetchall()

            findings = conn.execute(
                "SELECT doc_path, severity, gap_type, section, description "
                "FROM doc_audit_findings WHERE run_id=? "
                "ORDER BY doc_path, severity",
                (run_id,),
            ).fetchall()

            duplicates = conn.execute(
                "SELECT doc_a, doc_b, similarity, duplicate_type, description "
                "FROM doc_duplicates WHERE run_id=? "
                "ORDER BY similarity DESC",
                (run_id,),
            ).fetchall()

            relations = conn.execute(
                "SELECT source_doc, target_doc, relation_type, link_text, confidence "
                "FROM doc_relations WHERE run_id=? "
                "ORDER BY relation_type, confidence DESC",
                (run_id,),
            ).fetchall()

            isolated = conn.execute(
                "SELECT c.doc_path FROM doc_completeness c "
                "WHERE c.run_id=? "
                "AND c.doc_path NOT IN ("
                "  SELECT source_doc FROM doc_relations WHERE run_id=?"
                "  UNION"
                "  SELECT target_doc FROM doc_relations WHERE run_id=?"
                ")",
                (run_id, run_id, run_id),
            ).fetchall()

        lines: list[str] = []
        lines.append("=" * 72)
        lines.append(f"RAPORT AUDYTU DOKUMENTACJI  run_id={run_id}")
        lines.append(
            f"Katalog: {run['scanned_dir']}  "
            f"Dokumentów: {run['doc_count']}  "
            f"Status: {run['status']}"
        )
        lines.append("=" * 72)

        # --- Kompletność ---
        lines.append("\n## KOMPLETNOŚĆ DOKUMENTÓW\n")
        for row in completeness:
            score = row["completeness_score"]
            bar = _score_bar(score)
            lines.append(
                f"  [{bar}] {score:.2f}  "
                f"E:{row['gap_error_count']} W:{row['gap_warning_count']}  "
                f"{row['doc_path']}"
            )

        # --- Braki ---
        errors = [f for f in findings if f["severity"] == "ERROR"]
        warnings = [f for f in findings if f["severity"] == "WARNING"]
        lines.append(f"\n## BRAKI ({len(errors)} ERROR, {len(warnings)} WARNING)\n")
        current_doc = None
        for f in findings:
            if f["doc_path"] != current_doc:
                current_doc = f["doc_path"]
                lines.append(f"\n  [{current_doc}]")
            icon = "✗" if f["severity"] == "ERROR" else "⚠"
            lines.append(f"    {icon} [{f['gap_type']}] {f['description']}")

        # --- Duplikaty ---
        lines.append(f"\n## DUPLIKATY / TREŚCI POKREWNE ({len(duplicates)})\n")
        for d in duplicates:
            type_icon = {"exact": "⊕", "extending": "≈", "thematic": "~", "partial": "◐"}.get(
                d["duplicate_type"], "?"
            )
            lines.append(
                f"  {type_icon} [{d['duplicate_type']:10}] sim={d['similarity']:.2f}  "
                f"{d['doc_a']} ↔ {d['doc_b']}"
            )
            if d["description"]:
                lines.append(f"      {d['description']}")

        # --- Relacje ---
        lines.append(f"\n## RELACJE MIĘDZY DOKUMENTAMI ({len(relations)})\n")
        last_type = None
        for r in relations:
            if r["relation_type"] != last_type:
                last_type = r["relation_type"]
                lines.append(f"\n  [{last_type.upper()}]")
            lines.append(
                f"    conf={r['confidence']:.2f}  "
                f"{r['source_doc']} → {r['target_doc']}"
                + (f"  [{r['link_text'][:50]}]" if r["link_text"] else "")
            )

        # --- Izolowane ---
        if isolated:
            lines.append(f"\n## DOKUMENTY BEZ RELACJI ({len(isolated)})\n")
            for row in isolated:
                lines.append(f"  ⊘ {row['doc_path']}")

        lines.append("\n" + "=" * 72)
        return "\n".join(lines)

    def list_runs(self) -> list[dict]:
        """Zwróć listę wszystkich przebiegów audytu."""
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT run_id, scanned_dir, doc_count, started_at, status "
                "FROM doc_audit_runs ORDER BY started_at DESC"
            ).fetchall()
        return [dict(r) for r in rows]

    # -------------------------------------------------------------------
    # Prywatne — detektory
    # -------------------------------------------------------------------

    def _run_gap_detection(
        self, run_id: str, docs: dict[str, str]
    ) -> list[GapFinding]:
        """Uruchom GapDetector dla wszystkich dokumentów."""
        all_findings: list[GapFinding] = []
        now = self._now()

        with self._connect() as conn:
            for doc_id, text in docs.items():
                findings = self._gap_detector.analyse(doc_id, text)
                all_findings.extend(findings)

                headings = extract_headings(text)
                token_count = len(tokenize(text, remove_stopwords=False))
                score = self._gap_detector.completeness_score(findings)

                errors = sum(1 for f in findings if f.severity == "ERROR")
                warnings = sum(1 for f in findings if f.severity == "WARNING")
                infos = sum(1 for f in findings if f.severity == "INFO")

                # Wykryj typ dokumentu (reuse logic)
                from scripts.nlp.gap_detector import _detect_doc_type
                doc_type = _detect_doc_type(doc_id, text)

                conn.execute(
                    "INSERT OR REPLACE INTO doc_completeness "
                    "(run_id, doc_path, doc_type, heading_count, token_count, "
                    "completeness_score, gap_error_count, gap_warning_count, "
                    "gap_info_count, analysed_at) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (run_id, doc_id, doc_type, len(headings), token_count,
                     score, errors, warnings, infos, now),
                )

                for f in findings:
                    conn.execute(
                        "INSERT INTO doc_audit_findings "
                        "(run_id, doc_path, gap_type, severity, section, "
                        "description, weight, analysed_at) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (run_id, doc_id, f.gap_type, f.severity, f.section,
                         f.description, f.weight, now),
                    )

        return all_findings

    def _run_duplicate_detection(
        self, run_id: str, docs: dict[str, str]
    ) -> list[DuplicateRecord]:
        """Uruchom DuplicateDetector."""
        if len(docs) < 2:
            return []

        detector = DuplicateDetector()
        for doc_id, text in docs.items():
            detector.add(doc_id, text)

        records = detector.analyse()
        now = self._now()

        with self._connect() as conn:
            for r in records:
                conn.execute(
                    "INSERT OR IGNORE INTO doc_duplicates "
                    "(run_id, doc_a, doc_b, similarity, method, duplicate_type, "
                    "description, analysed_at) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (run_id, r.doc_a, r.doc_b, r.similarity, r.method,
                     r.duplicate_type, r.description, now),
                )

        return records

    def _run_relation_mapping(
        self, run_id: str, docs: dict[str, str]
    ) -> list[RelationRecord]:
        """Uruchom RelationMapper."""
        records = self._relation_mapper.analyse(docs)
        now = self._now()

        with self._connect() as conn:
            for r in records:
                conn.execute(
                    "INSERT INTO doc_relations "
                    "(run_id, source_doc, target_doc, relation_type, "
                    "link_text, confidence, analysed_at) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (run_id, r.source_doc, r.target_doc, r.relation_type,
                     r.link_text, r.confidence, now),
                )

        return records

    # -------------------------------------------------------------------
    # Prywatne — infrastruktura
    # -------------------------------------------------------------------

    def _ensure_schema(self) -> None:
        """Stwórz tabele jeśli nie istnieją."""
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        ddl = _DDL_PATH.read_text(encoding="utf-8")
        with self._connect() as conn:
            conn.executescript(ddl)

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self._db_path), timeout=30)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA foreign_keys=ON")
        return conn

    @staticmethod
    def _now() -> str:
        return datetime.now(timezone.utc).isoformat()

    @staticmethod
    def _new_run_id() -> str:
        return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + "-" + uuid.uuid4().hex[:6]

    @staticmethod
    def _iter_docs(
        root: Path,
        extensions: frozenset[str],
        skip_dirs: frozenset[str],
    ) -> Iterator[Path]:
        """Iteruj po plikach dokumentacji w drzewie katalogów."""
        for path in root.rglob("*"):
            if any(part in skip_dirs for part in path.parts):
                continue
            if path.is_file() and path.suffix.lower() in extensions:
                yield path


# ---------------------------------------------------------------------------
# Helpers — raport
# ---------------------------------------------------------------------------

def _score_bar(score: float, width: int = 10) -> str:
    """Tekstowy pasek postępu dla wyników kompletności."""
    filled = round(score * width)
    return "█" * filled + "░" * (width - filled)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cmd_scan(args: argparse.Namespace) -> int:
    auditor = DocAuditor(db_path=args.db, verbose=True)
    try:
        run_id = auditor.scan(
            scan_dir=Path(args.dir),
            config={"cli": True, "extensions": list(_DOC_EXTENSIONS)},
        )
        print(f"\nRun ID: {run_id}")
        if args.report:
            print(auditor.report(run_id))
        return 0
    except FileNotFoundError as e:
        print(f"Błąd: {e}", file=sys.stderr)
        return 1


def _cmd_report(args: argparse.Namespace) -> int:
    auditor = DocAuditor(db_path=args.db)
    run_id = args.run_id
    if not run_id:
        # Użyj ostatniego przebiegu
        runs = auditor.list_runs()
        if not runs:
            print("Brak przebiegów w DB.", file=sys.stderr)
            return 1
        run_id = runs[0]["run_id"]
        print(f"(używam ostatniego przebiegu: {run_id})")
    print(auditor.report(run_id))
    return 0


def _cmd_list_runs(args: argparse.Namespace) -> int:
    auditor = DocAuditor(db_path=args.db)
    runs = auditor.list_runs()
    if not runs:
        print("Brak przebiegów.")
        return 0
    print(f"{'RUN ID':30} {'DOC_COUNT':>9}  {'STATUS':8}  {'STARTED_AT':30}  DIR")
    print("-" * 100)
    for r in runs:
        print(
            f"{r['run_id']:30} {r['doc_count']:>9}  {r['status']:8}  "
            f"{r['started_at']:30}  {r['scanned_dir']}"
        )
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Zbuduj parser CLI."""
    parser = argparse.ArgumentParser(
        prog="doc_auditor",
        description="Audyt dokumentacji projektowej — braki, duplikaty, relacje.",
    )
    parser.add_argument(
        "--db",
        default=str(Path(__file__).parent.parent.parent / "reports" / "it_doc_audit.db"),
        metavar="PATH",
        help="Ścieżka do pliku SQLite (domyślnie: reports/it_doc_audit.db)",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    # scan
    p_scan = sub.add_parser("scan", help="Skanuj katalog z dokumentami")
    p_scan.add_argument("--dir", required=True, metavar="DIR",
                         help="Katalog z plikami dokumentacji")
    p_scan.add_argument("--report", action="store_true",
                         help="Wyświetl raport po skanowaniu")
    p_scan.set_defaults(func=_cmd_scan)

    # report
    p_report = sub.add_parser("report", help="Pokaż raport dla przebiegu")
    p_report.add_argument("--run-id", default=None, dest="run_id",
                           help="ID przebiegu (domyślnie: ostatni)")
    p_report.set_defaults(func=_cmd_report)

    # list-runs
    p_list = sub.add_parser("list-runs", help="Listuj wszystkie przebiegi")
    p_list.set_defaults(func=_cmd_list_runs)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.WARNING)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
