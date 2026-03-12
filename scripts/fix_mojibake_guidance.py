#!/usr/bin/env python3
"""
fix_mojibake_guidance.py
Naprawia kodowanie (mojibake cp1252->utf-8) w kolumnie doc_title tabeli doc_section_guidance.
Podobny problem może dotyczyć innych kolumn tekstowych — sprawdza też section_title i guidance.
"""

import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"

# Whitelist of allowed table/column/pk identifiers to prevent SQL injection
# if this function is ever called with dynamic arguments.
_ALLOWED_TABLES = frozenset(
    {"doc_section_guidance", "documents_final", "documents_expected", "link_type_guidance"}
)
_ALLOWED_COLUMNS = frozenset({"doc_title", "section_title", "guidance", "title", "link_type"})
_ALLOWED_PKS = frozenset({"id"})


def _validate_identifier(value: str, allowed: frozenset, kind: str) -> None:
    if value not in allowed:
        raise ValueError(f"Niedozwolony identyfikator {kind}: {value!r} (dozwolone: {allowed})")


def try_fix(value: str) -> tuple[str, bool]:
    """Próbuje naprawić mojibake (cp1252 błędnie zdekodowane jako unicode)."""
    try:
        fixed = value.encode("cp1252").decode("utf-8")
        return fixed, fixed != value
    except (UnicodeEncodeError, UnicodeDecodeError):
        return value, False


def fix_column(
    conn: sqlite3.Connection, table: str, column: str, pk: str = "id", dry_run: bool = False
):
    cur = conn.cursor()
    cur.execute(f"SELECT {pk}, {column} FROM {table}")  # nosec B608 -- identifiers come from hardcoded call sites in main(); validated by _validate_identifier before main() calls this
    rows = cur.fetchall()
    fixed_count = 0
    updates = []
    for row_id, value in rows:
        if value is None:
            continue
        fixed, changed = try_fix(value)
        if changed:
            updates.append((fixed, row_id))
            fixed_count += 1
    print(f"  [{table}.{column}] Znaleziono do naprawy: {fixed_count} / {len(rows)}")
    if not dry_run and updates:
        cur.executemany(f"UPDATE {table} SET {column} = ? WHERE {pk} = ?", updates)  # nosec B608 -- identifiers validated
        conn.commit()
        print(f"  [{table}.{column}] Naprawiono: {fixed_count} wierszy.")
    elif dry_run:
        print(f"  [{table}.{column}] DRY-RUN — bez zmian w DB.")
    return fixed_count


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("=== TRYB DRY-RUN (brak zmian w DB) ===")

    conn = sqlite3.connect(DB_PATH)

    total = 0
    # Validate all identifiers before use (defense-in-depth for future callers)
    calls = [
        ("doc_section_guidance", "doc_title", "id"),
        ("doc_section_guidance", "section_title", "id"),
        ("doc_section_guidance", "guidance", "id"),
        ("documents_final", "title", "id"),
        ("documents_expected", "title", "id"),
        ("link_type_guidance", "link_type", "id"),
        ("link_type_guidance", "guidance", "id"),
    ]
    for tbl, col, pk in calls:
        _validate_identifier(tbl, _ALLOWED_TABLES, "table")
        _validate_identifier(col, _ALLOWED_COLUMNS, "column")
        _validate_identifier(pk, _ALLOWED_PKS, "pk")
        total += fix_column(conn, tbl, col, pk=pk, dry_run=dry_run)

    conn.close()
    print(f"\nLacznie naprawionych: {total} wartosci.")
    if dry_run:
        print("Uruchom bez --dry-run aby zastosowac zmiany.")


if __name__ == "__main__":
    main()
