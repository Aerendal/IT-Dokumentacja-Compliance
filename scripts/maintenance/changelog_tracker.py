#!/usr/bin/env python3
"""
scripts/maintenance/changelog_tracker.py

Śledzenie i przeglądanie historii zmian w szablonach IT Dokumentacja.

Tabela template_changelog jest automatycznie uzupełniana przez:
  - bulk_section_patcher.py
  - regulation_updater.py
  - inject_aspirational_sections.py

Użycie:
  python3 scripts/maintenance/changelog_tracker.py list
  python3 scripts/maintenance/changelog_tracker.py list --template "core/security_policy.md"
  python3 scripts/maintenance/changelog_tracker.py list --since 2026-03-01
  python3 scripts/maintenance/changelog_tracker.py list --type bulk_patch
  python3 scripts/maintenance/changelog_tracker.py stats
  python3 scripts/maintenance/changelog_tracker.py export --save reports/changelog_export.json
"""

import argparse
import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "reports" / "it_doc_matrix.db"


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def ensure_table(conn: sqlite3.Connection):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS template_changelog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            template_path TEXT NOT NULL,
            changed_at TEXT NOT NULL,
            change_type TEXT NOT NULL,
            change_reason TEXT,
            diff_summary TEXT,
            patch_args TEXT
        )
    """)
    conn.commit()


def cmd_list(conn: sqlite3.Connection, args):
    ensure_table(conn)
    cur = conn.cursor()

    query = "SELECT id, template_path, changed_at, change_type, change_reason, diff_summary FROM template_changelog WHERE 1=1"
    params = []

    if args.template:
        query += " AND template_path LIKE ?"
        params.append(f"%{args.template}%")
    if args.since:
        query += " AND changed_at >= ?"
        params.append(args.since)
    if args.type:
        query += " AND change_type = ?"
        params.append(args.type)

    query += " ORDER BY changed_at DESC"
    if args.limit:
        query += f" LIMIT {args.limit}"

    cur.execute(query, params)
    rows = cur.fetchall()

    if not rows:
        print("Brak wpisów w changelog spełniających kryteria.")
        return

    if args.output == "json":
        data = [dict(r) for r in rows]
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    print(f"\n{'ID':>6}  {'Data':>24}  {'Typ':>20}  {'Szablon'}")
    print("-" * 100)
    for r in rows:
        print(
            f"{r['id']:>6}  {r['changed_at'][:19]:>19}  {r['change_type']:>20}  {r['template_path']}"
        )
        if r["change_reason"]:
            print(f"{'':>6}  Powód: {r['change_reason']}")
        if r["diff_summary"]:
            print(f"{'':>6}  Zmiana: {r['diff_summary']}")
    print(f"\nŁącznie: {len(rows)} wpisów")


def cmd_stats(conn: sqlite3.Connection, args):
    ensure_table(conn)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM template_changelog")
    total = cur.fetchone()[0]

    cur.execute("""
        SELECT change_type, COUNT(*) as cnt
        FROM template_changelog GROUP BY change_type ORDER BY cnt DESC
    """)
    by_type = cur.fetchall()

    cur.execute("""
        SELECT date(changed_at) as day, COUNT(*) as cnt
        FROM template_changelog GROUP BY day ORDER BY day DESC LIMIT 10
    """)
    by_day = cur.fetchall()

    cur.execute("""
        SELECT template_path, COUNT(*) as cnt
        FROM template_changelog GROUP BY template_path ORDER BY cnt DESC LIMIT 10
    """)
    most_changed = cur.fetchall()

    print("\n=== Statystyki changelog ===")
    print(f"Łącznie wpisów: {total}")

    print("\nPo typie zmiany:")
    for r in by_type:
        print(f"  {r['cnt']:6d}  {r['change_type']}")

    print("\nPo dniu (ostatnie 10):")
    for r in by_day:
        print(f"  {r['day']}  {r['cnt']:5d} zmian")

    print("\nNajczęściej zmieniane szablony (top 10):")
    for r in most_changed:
        print(f"  {r['cnt']:4d}x  {r['template_path']}")


def cmd_export(conn: sqlite3.Connection, args):
    ensure_table(conn)
    cur = conn.cursor()
    cur.execute("SELECT * FROM template_changelog ORDER BY changed_at DESC")
    rows = [dict(r) for r in cur.fetchall()]

    if args.save:
        path = Path(args.save)
        path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Eksportowano {len(rows)} wpisów do {path}")
    else:
        print(json.dumps(rows, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Historia zmian szablonów IT Dokumentacja")
    sub = parser.add_subparsers(dest="command")

    # list
    p_list = sub.add_parser("list", help="Wyświetl historię zmian")
    p_list.add_argument("--template", metavar="PATH", help="Filtruj po ścieżce szablonu")
    p_list.add_argument("--since", metavar="DATE", help="Filtruj od daty (YYYY-MM-DD)")
    p_list.add_argument("--type", metavar="TYPE", help="Filtruj po typie zmiany")
    p_list.add_argument("--limit", type=int, default=50, help="Maks. liczba wyników")
    p_list.add_argument("--output", choices=["table", "json"], default="table")

    # stats
    sub.add_parser("stats", help="Statystyki changelog")

    # export
    p_exp = sub.add_parser("export", help="Eksportuj cały changelog")
    p_exp.add_argument("--save", metavar="FILE", help="Plik docelowy (.json)")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 0

    conn = connect()
    if args.command == "list":
        cmd_list(conn, args)
    elif args.command == "stats":
        cmd_stats(conn, args)
    elif args.command == "export":
        cmd_export(conn, args)
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
