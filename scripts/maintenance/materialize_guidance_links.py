#!/usr/bin/env python3
"""
materialize_guidance_links.py

Materializuje relacje many-to-many między guidance a standardami / regulacjami
poprzez rozwinięcie kolumn JSON standards_refs i regulations_refs z tabeli
doc_section_guidance do osobnych tabel linkujących.

Użycie:
    python3 materialize_guidance_links.py --apply --stats
    python3 materialize_guidance_links.py --dry-run
    python3 materialize_guidance_links.py --apply --standards-only
"""

import argparse
import json
import sqlite3
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Stałe
# ---------------------------------------------------------------------------

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_DB_PATH = _REPO_ROOT / "reports" / "it_doc_matrix.db"
_CHUNK_SIZE = 5000

DDL = """
CREATE TABLE IF NOT EXISTS guidance_standard_links (
    guidance_id   INTEGER NOT NULL,
    standard_code TEXT    NOT NULL,
    PRIMARY KEY (guidance_id, standard_code),
    FOREIGN KEY (guidance_id) REFERENCES doc_section_guidance(id)
);

CREATE TABLE IF NOT EXISTS guidance_regulation_links (
    guidance_id     INTEGER NOT NULL,
    regulation_code TEXT    NOT NULL,
    PRIMARY KEY (guidance_id, regulation_code),
    FOREIGN KEY (guidance_id) REFERENCES doc_regulation_mapping(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_gsl_standard  ON guidance_standard_links(standard_code);
CREATE INDEX IF NOT EXISTS idx_grl_regulation ON guidance_regulation_links(regulation_code);
"""


# ---------------------------------------------------------------------------
# Pomocnicze
# ---------------------------------------------------------------------------

def _parse_json_list(raw: str | None, row_id: int, field: str, json_errors: list) -> list[str]:
    """Parsuje kolumnę JSON → lista stringów. Zwraca [] przy NULL / pustej liście."""
    if raw is None:
        return []
    try:
        parsed = json.loads(raw)
        if not isinstance(parsed, list):
            json_errors.append((row_id, field, "not a list"))
            return []
        return [str(x) for x in parsed if x]
    except json.JSONDecodeError as exc:
        json_errors.append((row_id, field, str(exc)))
        return []


def _ensure_schema(conn: sqlite3.Connection) -> None:
    """Tworzy tabele i indeksy jeśli nie istnieją."""
    for stmt in DDL.strip().split(";"):
        stmt = stmt.strip()
        if stmt:
            conn.execute(stmt)
    conn.commit()


def _load_known_standards(conn: sqlite3.Connection) -> set[str] | None:
    """Wczytuje znane kody standardów z tabeli standards (jeśli istnieje)."""
    try:
        cur = conn.execute("SELECT code FROM standards")
        return {row[0] for row in cur.fetchall()}
    except sqlite3.OperationalError:
        return None


# ---------------------------------------------------------------------------
# Główna logika
# ---------------------------------------------------------------------------

def materialize(
    conn: sqlite3.Connection,
    *,
    dry_run: bool = False,
    standards_only: bool = False,
    stats: bool = False,
) -> dict:
    """
    Przetwarza doc_section_guidance i wstawia wiersze do tabel linkujących.

    Zwraca słownik z kluczami:
      std_inserted, reg_inserted, json_errors (lista krotek)
    """
    _ensure_schema(conn)
    known_standards = _load_known_standards(conn)

    json_errors: list[tuple] = []
    std_inserted = 0
    reg_inserted = 0
    unknown_standards_warned: set[str] = set()

    if not dry_run:
        conn.execute("DELETE FROM guidance_standard_links")
        if not standards_only:
            conn.execute("DELETE FROM guidance_regulation_links")
        conn.commit()

    print("Materializing guidance links...")

    # Iteracja po blokach
    offset = 0
    while True:
        rows = conn.execute(
            "SELECT id, standards_refs, regulations_refs FROM doc_section_guidance "
            "LIMIT ? OFFSET ?",
            (_CHUNK_SIZE, offset),
        ).fetchall()

        if not rows:
            break

        std_batch: list[tuple] = []
        reg_batch: list[tuple] = []

        for row_id, standards_raw, regulations_raw in rows:
            std_codes = _parse_json_list(standards_raw, row_id, "standards_refs", json_errors)
            for code in std_codes:
                if known_standards is not None and code not in known_standards:
                    if code not in unknown_standards_warned:
                        print(f"  WARN: unknown standard_code={code!r}", file=sys.stderr)
                        unknown_standards_warned.add(code)
                std_batch.append((row_id, code))
                std_inserted += 1

            if not standards_only:
                reg_codes = _parse_json_list(regulations_raw, row_id, "regulations_refs", json_errors)
                for code in reg_codes:
                    reg_batch.append((row_id, code))
                    reg_inserted += 1

        if not dry_run:
            conn.executemany(
                "INSERT OR IGNORE INTO guidance_standard_links (guidance_id, standard_code) VALUES (?, ?)",
                std_batch,
            )
            if not standards_only:
                conn.executemany(
                    "INSERT OR IGNORE INTO guidance_regulation_links (guidance_id, regulation_code) VALUES (?, ?)",
                    reg_batch,
                )
            conn.commit()

        end = offset + len(rows)
        print(f"Processing rows {offset}-{end}... ({end} done)")
        offset += _CHUNK_SIZE

    print("Done.")

    if stats and not dry_run:
        std_count = conn.execute("SELECT COUNT(*) FROM guidance_standard_links").fetchone()[0]
        reg_count = 0 if standards_only else conn.execute(
            "SELECT COUNT(*) FROM guidance_regulation_links"
        ).fetchone()[0]
        print(f"guidance_standard_links:  {std_count:,} rows")
        if not standards_only:
            print(f"guidance_regulation_links: {reg_count:,} rows")
    elif dry_run:
        print(f"[dry-run] Would insert {std_inserted:,} standard links")
        if not standards_only:
            print(f"[dry-run] Would insert {reg_inserted:,} regulation links")

    if json_errors:
        print(f"JSON errors: {len(json_errors)}")
    else:
        print("JSON errors: 0")

    return {
        "std_inserted": std_inserted,
        "reg_inserted": reg_inserted,
        "json_errors": json_errors,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Materializuje linki guidance → standards / regulations.",
    )
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Policz wiersze bez zapisu do DB")
    mode.add_argument("--apply", action="store_true", help="Zapisz do DB (domyślne)")
    p.add_argument("--standards-only", action="store_true", help="Tylko standards_refs, pomiń regulations")
    p.add_argument("--stats", action="store_true", help="Wydrukuj końcowe liczniki z tabel")
    p.add_argument("--db", default=str(_DB_PATH), help="Ścieżka do bazy SQLite")
    return p


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    db_path = Path(args.db)
    if not db_path.exists():
        print(f"ERROR: DB not found: {db_path}", file=sys.stderr)
        return 1

    conn = sqlite3.connect(str(db_path))
    try:
        materialize(
            conn,
            dry_run=args.dry_run,
            standards_only=args.standards_only,
            stats=args.stats,
        )
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
