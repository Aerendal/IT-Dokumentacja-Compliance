#!/usr/bin/env python3
"""
build_standards_catalog.py — Buduje katalog wymaganych dokumentów dla 44 standardów.

Dla każdego standardu definiuje listę typów dokumentów które standard
wymaga (is_required=True) lub zaleca (is_required=False).
Źródła: oficjalne specyfikacje, iso.org scope, Wikipedia, publiczne TOC.

Wynik: tabela standards_catalog w DB.
Dane katalogu: config/standards_catalog.yaml
"""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

import yaml

DB_DEFAULT = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"
_CATALOG_YAML = Path(__file__).parent.parent / "config" / "standards_catalog.yaml"


def _load_catalog_data() -> dict[str, list[dict]]:
    """Wczytuje katalog standardów z config/standards_catalog.yaml."""
    return yaml.safe_load(_CATALOG_YAML.read_text(encoding="utf-8"))


CATALOG: dict[str, list[dict]] = _load_catalog_data()


# ---------------------------------------------------------------------------


def create_table(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS standards_catalog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            standard_code TEXT NOT NULL,
            doc_type_id   TEXT NOT NULL UNIQUE,
            doc_title     TEXT NOT NULL,
            is_required   INTEGER NOT NULL DEFAULT 1,
            category      TEXT,
            source_url    TEXT,
            notes         TEXT,
            created_at    TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (standard_code) REFERENCES standards(standard_code)
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_sc_standard ON standards_catalog(standard_code)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_sc_category ON standards_catalog(category)")
    conn.commit()


def count_existing(conn: sqlite3.Connection) -> int:
    return conn.execute("SELECT COUNT(*) FROM standards_catalog").fetchone()[0]


def load_catalog(conn: sqlite3.Connection, replace: bool = False) -> dict[str, int]:
    if replace:
        conn.execute("DELETE FROM standards_catalog")
        conn.commit()

    stats: dict[str, int] = {}
    for standard_code, entries in CATALOG.items():
        inserted = 0
        for entry in entries:
            try:
                conn.execute(
                    """INSERT OR IGNORE INTO standards_catalog
                       (standard_code, doc_type_id, doc_title, is_required, category, source_url, notes)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (
                        standard_code,
                        entry["doc_type_id"],
                        entry["title"],
                        int(entry["required"]),
                        entry.get("category"),
                        entry.get("url") or None,
                        entry.get("notes") or None,
                    ),
                )
                inserted += 1
            except sqlite3.IntegrityError as e:
                print(f"  SKIP {entry['doc_type_id']}: {e}")
        stats[standard_code] = inserted
    conn.commit()
    return stats


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", default=DB_DEFAULT, help="Path to SQLite DB")
    ap.add_argument("--replace", action="store_true", help="Delete and re-insert all rows")
    ap.add_argument("--stats", action="store_true", help="Print stats only, don't insert")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    create_table(conn)

    if args.stats:
        n = count_existing(conn)
        print(f"Catalog entries in DB: {n}")
        rows = conn.execute(
            "SELECT standard_code, COUNT(*) FROM standards_catalog GROUP BY standard_code ORDER BY standard_code"
        ).fetchall()
        for code, cnt in rows:
            print(f"  {code}: {cnt}")
        conn.close()
        return

    stats = load_catalog(conn, replace=args.replace)
    print("=== Standards Catalog loaded ===")
    total = 0
    for code, n in sorted(stats.items()):
        print(f"  {code:40s} +{n}")
        total += n
    print(f"\nTotal inserted: {total} catalog entries across {len(stats)} standards")

    # Summary: which standards from DB have no catalog entries yet?
    missing = conn.execute("""
        SELECT s.standard_code FROM standards s
        WHERE NOT EXISTS (SELECT 1 FROM standards_catalog c WHERE c.standard_code = s.standard_code)
        ORDER BY s.standard_code
    """).fetchall()
    if missing:
        print(f"\nWARN: Standards with no catalog entries: {[r[0] for r in missing]}")
    else:
        print(f"\nAll {len(CATALOG)} standards covered.")
    conn.close()


if __name__ == "__main__":
    main()
