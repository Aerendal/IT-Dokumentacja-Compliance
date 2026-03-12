#!/usr/bin/env python3
"""
audit_templates.py

Audytor integralnosci biblioteki szablonow.
Porownuje pliki fizyczne na dysku z rekordami w bazie SQLite (docs, gap_analysis).
Wykrywa sieroty (dysk bez DB), duchy (DB bez dysku), duplikaty tresci i dokumenty
bez mapowania do standardow.

Uzycie:
    python3 audit_templates.py --report
    python3 audit_templates.py --report --json
    python3 audit_templates.py --fix --dry-run
    python3 audit_templates.py --fix
"""

import argparse
import hashlib
import json
import logging
import sqlite3
import sys
import os
from datetime import datetime
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Any, Set

_log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Stale
# ---------------------------------------------------------------------------

VERSION = "1.0.0"

PROJECT_ROOT = Path(__file__).parent.parent.parent
DEFAULT_DB = PROJECT_ROOT / "reports" / "it_doc_matrix.db"
DEFAULT_TEMPLATES_DIR = PROJECT_ROOT / "generated_templates" / "core"

ANSI_RESET  = "\033[0m"
ANSI_RED    = "\033[91m"
ANSI_GREEN  = "\033[92m"
ANSI_YELLOW = "\033[93m"
ANSI_BOLD   = "\033[1m"
ANSI_DIM    = "\033[2m"

EXIT_OK    = 0
EXIT_WARN  = 2
EXIT_ERROR = 1


# ---------------------------------------------------------------------------
# Narzedzia pomocnicze
# ---------------------------------------------------------------------------

def colored(text: str, color: str) -> str:
    if not sys.stdout.isatty():
        return text
    return f"{color}{text}{ANSI_RESET}"


def log_info(msg: str) -> None:
    print(f"[INFO] {msg}")


def log_ok(msg: str) -> None:
    print(colored(f"[OK]   {msg}", ANSI_GREEN))


def log_warn(msg: str) -> None:
    print(colored(f"[WARN] {msg}", ANSI_YELLOW))


def log_err(msg: str) -> None:
    print(colored(f"[BLAD] {msg}", ANSI_RED), file=sys.stderr)


# ---------------------------------------------------------------------------
# Funkcje top-level (exportowane do testow)
# ---------------------------------------------------------------------------

def normalize_path(path: str) -> str:
    """Normalizuje sciezke: backslash -> forward slash, lowercase."""
    return path.replace("\\", "/").strip().lower()


def compute_hash(content: bytes) -> str:
    """Oblicza SHA256 hex digest dla podanych bytow."""
    return hashlib.sha256(content).hexdigest()


def find_ghosts(conn: sqlite3.Connection, templates_dir: Path) -> List[str]:
    """
    Zwraca liste sciezek ktore sa w bazie (docs.path i gap_analysis.matched_doc_path)
    ale nie istnieja jako pliki na dysku w templates_dir.
    Sciezki w formacie np. 'core/nazwa.md'.
    """
    db_paths: Set[str] = set()

    # docs.path
    try:
        cur = conn.execute("SELECT path FROM docs WHERE path IS NOT NULL AND path != 'ORPHAN'")
        for row in cur.fetchall():
            if row[0]:
                db_paths.add(normalize_path(row[0]))
    except sqlite3.Error as exc:
        _log.debug("docs.path table unavailable (DB may lack table): %s", exc)

    # gap_analysis.matched_doc_path
    try:
        cur = conn.execute(
            "SELECT matched_doc_path FROM gap_analysis WHERE matched_doc_path IS NOT NULL"
        )
        for row in cur.fetchall():
            if row[0]:
                db_paths.add(normalize_path(row[0]))
    except sqlite3.Error as exc:
        _log.debug("gap_analysis table unavailable: %s", exc)

    ghosts = []
    templates_base = templates_dir.parent  # generated_templates/

    for db_path in sorted(db_paths):
        full_path = templates_base / db_path
        if not full_path.exists():
            ghosts.append(db_path)

    return ghosts


def find_orphans(conn: sqlite3.Connection, templates_dir: Path) -> List[str]:
    """
    Zwraca liste sciezek plikow ktore istnieja na dysku w templates_dir
    ale nie maja wpisu w docs.path.
    Sciezki w formacie np. 'core/nazwa.md'.
    """
    # Pobierz sciezki z DB
    db_paths: Set[str] = set()
    try:
        cur = conn.execute("SELECT path FROM docs WHERE path IS NOT NULL AND path != 'ORPHAN'")
        for row in cur.fetchall():
            if row[0]:
                db_paths.add(normalize_path(row[0]))
    except sqlite3.Error as exc:
        _log.debug("docs.path table unavailable in find_orphans: %s", exc)
    templates_base = templates_dir.parent  # generated_templates/

    orphans = []
    for md_file in sorted(templates_dir.rglob("*.md")):
        rel = normalize_path(str(md_file.relative_to(templates_base)))
        if rel not in db_paths:
            orphans.append(rel)

    return orphans


def find_duplicates(templates_dir: Path) -> Dict[str, List[str]]:
    """
    Wykrywa pliki o identycznej tresci (SHA256).
    Zwraca slownik: sha256_hex -> [sciezki_relatywne].
    Uwzglednia tylko grupy z >= 2 plikami.
    """
    templates_base = templates_dir.parent
    hash_map: Dict[str, List[str]] = defaultdict(list)

    for md_file in sorted(templates_dir.rglob("*.md")):
        try:
            content = md_file.read_bytes()
            h = compute_hash(content)
            rel = normalize_path(str(md_file.relative_to(templates_base)))
            hash_map[h].append(rel)
        except OSError as exc:
            _log.debug("Cannot read %s for duplicate detection: %s", md_file, exc)

    return {h: paths for h, paths in hash_map.items() if len(paths) > 1}


def find_unmapped(conn: sqlite3.Connection) -> List[str]:
    """
    Zwraca liste docs.path ktore nie maja zadnego wpisu w doc_standard_mapping.
    Pomija rekordy ORPHAN i NULL.
    """
    try:
        cur = conn.execute("""
            SELECT d.path
            FROM docs d
            WHERE d.path IS NOT NULL
              AND d.path != 'ORPHAN'
              AND NOT EXISTS (
                  SELECT 1 FROM doc_standard_mapping m
                  WHERE m.doc_path = d.path
              )
            ORDER BY d.path
        """)
        return [row[0] for row in cur.fetchall()]
    except sqlite3.Error as exc:
        log_warn(f"Nie mozna sprawdzic doc_standard_mapping: {exc}")
        return []


# ---------------------------------------------------------------------------
# Baza danych — inicjalizacja
# ---------------------------------------------------------------------------

def open_db(db_path: str) -> sqlite3.Connection:
    if not os.path.exists(db_path):
        log_err(f"Brak bazy danych: {db_path}")
        sys.exit(EXIT_ERROR)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    _ensure_audit_log_table(conn)
    return conn


def _ensure_audit_log_table(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS audit_integrity_log (
            id             INTEGER PRIMARY KEY,
            run_at         TEXT NOT NULL DEFAULT (datetime('now')),
            orphan_count   INTEGER,
            ghost_count    INTEGER,
            duplicate_count INTEGER,
            unmapped_count INTEGER,
            report_json    TEXT
        )
    """)
    conn.commit()


def save_audit_run(
    conn: sqlite3.Connection,
    orphan_count: int,
    ghost_count: int,
    duplicate_count: int,
    unmapped_count: int,
    report: Dict[str, Any],
) -> None:
    conn.execute("""
        INSERT INTO audit_integrity_log
            (run_at, orphan_count, ghost_count, duplicate_count, unmapped_count, report_json)
        VALUES (datetime('now'), ?, ?, ?, ?, ?)
    """, (
        orphan_count, ghost_count, duplicate_count, unmapped_count,
        json.dumps(report, ensure_ascii=False),
    ))
    conn.commit()


# ---------------------------------------------------------------------------
# Archiwizacja duchow
# ---------------------------------------------------------------------------

def archive_ghosts(
    conn: sqlite3.Connection,
    ghosts: List[str],
    templates_dir: Path,
    dry_run: bool,
) -> int:
    """
    Archiwizuje duchy: przenosi rekordy gap_analysis (matched_doc_path) do
    tabeli gap_analysis_archive (tworzonej jesli nie istnieje).
    Nie usuwa rekordow z docs.
    Zwraca liczbe zarchiwizowanych.
    """
    if dry_run:
        for g in ghosts:
            log_info(f"[DRY-RUN] archiwizacja ducha: {g}")
        return len(ghosts)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS gap_analysis_archive (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            archived_at   TEXT NOT NULL,
            original_id   INTEGER,
            matched_doc_path TEXT,
            standard_code TEXT,
            confidence    TEXT
        )
    """)
    conn.commit()

    archived = 0
    for ghost_path in ghosts:
        rows = conn.execute(
            "SELECT id, standard_code, confidence FROM gap_analysis WHERE matched_doc_path = ?",
            (ghost_path,),
        ).fetchall()
        for row in rows:
            conn.execute("""
                INSERT INTO gap_analysis_archive
                    (archived_at, original_id, matched_doc_path, standard_code, confidence)
                VALUES (datetime('now'), ?, ?, ?, ?)
            """, (row[0], ghost_path, row["standard_code"], row["confidence"]))
            archived += 1
    conn.commit()
    return archived


# ---------------------------------------------------------------------------
# Raport
# ---------------------------------------------------------------------------

def build_report(
    orphans: List[str],
    ghosts: List[str],
    duplicates: Dict[str, List[str]],
    unmapped: List[str],
) -> Dict[str, Any]:
    return {
        "generated_at": datetime.now().isoformat(),
        "orphan_count": len(orphans),
        "ghost_count": len(ghosts),
        "duplicate_count": len(duplicates),
        "unmapped_count": len(unmapped),
        "orphans": orphans,
        "ghosts": ghosts,
        "duplicates": duplicates,
        "unmapped": unmapped,
    }


def print_report(report: Dict[str, Any]) -> None:
    print(colored("=" * 62, ANSI_BOLD))
    print(colored("  RAPORT INTEGRALNOSCI BIBLIOTEKI SZABLONOW", ANSI_BOLD))
    print(colored("=" * 62, ANSI_BOLD))
    print(f"  Wygenerowano:    {report['generated_at'][:19]}")
    print(f"  Sieroty (orphans):    "
          f"{colored(str(report['orphan_count']), ANSI_YELLOW if report['orphan_count'] else ANSI_GREEN)}")
    print(f"  Duchy (ghosts):       "
          f"{colored(str(report['ghost_count']), ANSI_RED if report['ghost_count'] else ANSI_GREEN)}")
    print(f"  Duplikaty tresci:     "
          f"{colored(str(report['duplicate_count']), ANSI_YELLOW if report['duplicate_count'] else ANSI_GREEN)}")
    print(f"  Bez mapowania std.:   "
          f"{colored(str(report['unmapped_count']), ANSI_YELLOW if report['unmapped_count'] else ANSI_GREEN)}")
    print(colored("-" * 62, ANSI_DIM))

    if report["orphans"]:
        print(colored(f"\nSieroty ({report['orphan_count']}) — pliki na dysku bez wpisu w docs:", ANSI_BOLD))
        for p in report["orphans"][:20]:
            print(f"  {colored('-', ANSI_YELLOW)} {p}")
        if report["orphan_count"] > 20:
            print(colored(f"  ... ({report['orphan_count'] - 20} wiecej)", ANSI_DIM))

    if report["ghosts"]:
        print(colored(f"\nDuchy ({report['ghost_count']}) — wpisy w DB bez pliku na dysku:", ANSI_BOLD))
        for p in report["ghosts"][:20]:
            print(f"  {colored('-', ANSI_RED)} {p}")
        if report["ghost_count"] > 20:
            print(colored(f"  ... ({report['ghost_count'] - 20} wiecej)", ANSI_DIM))

    if report["duplicates"]:
        print(colored(f"\nDuplikaty tresci ({report['duplicate_count']} grup):", ANSI_BOLD))
        for h, paths in list(report["duplicates"].items())[:5]:
            print(f"  hash {h[:12]}: {', '.join(paths)}")

    if report["unmapped"]:
        print(colored(f"\nBez mapowania standardow ({report['unmapped_count']}):", ANSI_BOLD))
        for p in report["unmapped"][:20]:
            print(f"  {colored('-', ANSI_YELLOW)} {p}")
        if report["unmapped_count"] > 20:
            print(colored(f"  ... ({report['unmapped_count'] - 20} wiecej)", ANSI_DIM))

    if not any([report["orphans"], report["ghosts"], report["duplicates"], report["unmapped"]]):
        log_ok("Wszystko OK — brak problemow integralnosci.")

    print(colored("=" * 62, ANSI_BOLD))


# ---------------------------------------------------------------------------
# Glowna logika
# ---------------------------------------------------------------------------

def run_audit(
    db_path: str,
    templates_dir: Path,
    *,
    report: bool = True,
    as_json: bool = False,
    fix: bool = False,
    dry_run: bool = False,
) -> int:
    conn = open_db(db_path)

    orphans = find_orphans(conn, templates_dir)
    ghosts = find_ghosts(conn, templates_dir)
    duplicates = find_duplicates(templates_dir)
    unmapped = find_unmapped(conn)

    rep = build_report(orphans, ghosts, duplicates, unmapped)

    if report:
        if as_json:
            print(json.dumps(rep, ensure_ascii=False, indent=2))
        else:
            print_report(rep)

    if fix:
        archived = archive_ghosts(conn, ghosts, templates_dir, dry_run=dry_run)
        if archived:
            log_ok(f"{'[DRY-RUN] ' if dry_run else ''}Zarchiwizowano duchow: {archived}")
        else:
            log_info("Brak duchow do archiwizacji.")

    # Zapisz run do audit_integrity_log
    if not dry_run:
        save_audit_run(
            conn,
            orphan_count=len(orphans),
            ghost_count=len(ghosts),
            duplicate_count=len(duplicates),
            unmapped_count=len(unmapped),
            report=rep,
        )

    conn.close()

    if ghosts or orphans:
        return EXIT_WARN
    return EXIT_OK


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Audyt integralnosci biblioteki szablonow vs baza SQLite.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--db",
        default=str(DEFAULT_DB),
        help="Sciezka do bazy SQLite",
    )
    parser.add_argument(
        "--templates-dir",
        default=str(DEFAULT_TEMPLATES_DIR),
        help="Katalog z szablonami (generated_templates/core)",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Wypisz raport na stdout",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Format raportu: JSON (wymaga --report)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Napraw: archiwizuj duchy z gap_analysis",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Pokaz co zostaloby zrobione bez zapisu (uzyj z --fix)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # Domyslnie pokaz raport jesli nie podano zadnej akcji
    show_report = args.report or not args.fix

    exit_code = run_audit(
        db_path=args.db,
        templates_dir=Path(args.templates_dir),
        report=show_report,
        as_json=args.as_json,
        fix=args.fix,
        dry_run=args.dry_run,
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
