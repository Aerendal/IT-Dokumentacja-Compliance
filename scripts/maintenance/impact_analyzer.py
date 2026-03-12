#!/usr/bin/env python3
"""
scripts/maintenance/impact_analyzer.py

Analiza wpływu zmian: dla podanego standardu, regulacji, sekcji lub dokumentu
pokazuje które szablony zostaną dotknięte zmianą.

Użycie:
  python3 scripts/maintenance/impact_analyzer.py --standard ISO/IEC 27001
  python3 scripts/maintenance/impact_analyzer.py --regulation KSC-PL
  python3 scripts/maintenance/impact_analyzer.py --section "Standardy i compliance"
  python3 scripts/maintenance/impact_analyzer.py --doc "Polityka bezpieczeństwa"
  python3 scripts/maintenance/impact_analyzer.py --standard ISO/IEC 27001 --output json

Wyniki: tabela w terminalu + opcjonalny zapis do reports/impact_<target>.json
"""

import argparse
import json
import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "reports" / "it_doc_matrix.db"
REPORTS_DIR = BASE_DIR / "reports"


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def analyze_standard(conn: sqlite3.Connection, code: str) -> dict:
    cur = conn.cursor()
    # Exact and partial match
    cur.execute(
        """
        SELECT standard_code, standard_name FROM standards
        WHERE standard_code LIKE ? OR standard_name LIKE ?
    """,
        (f"%{code}%", f"%{code}%"),
    )
    matched = cur.fetchall()
    if not matched:
        return {"error": f"Standard '{code}' nie znaleziony w tabeli standards"}

    results = []
    for std in matched:
        sc = std["standard_code"]
        cur.execute(
            """
            SELECT m.doc_path, m.match_reason, d.title
            FROM doc_standard_mapping m
            LEFT JOIN docs d ON d.path = m.doc_path
            WHERE m.standard_code = ?
            ORDER BY m.doc_path
        """,
            (sc,),
        )
        docs = cur.fetchall()
        results.append(
            {
                "standard_code": sc,
                "standard_name": std["standard_name"],
                "affected_templates": [
                    {"path": r["doc_path"], "title": r["title"], "reason": r["match_reason"]}
                    for r in docs
                ],
                "count": len(docs),
            }
        )

    return {
        "query_type": "standard",
        "query": code,
        "matched_standards": results,
        "total_affected": sum(r["count"] for r in results),
    }


def analyze_regulation(conn: sqlite3.Connection, code: str) -> dict:
    cur = conn.cursor()
    cur.execute(
        """
        SELECT regulation_code, regulation_name FROM compliance_regulations
        WHERE regulation_code LIKE ? OR regulation_name LIKE ?
    """,
        (f"%{code}%", f"%{code}%"),
    )
    matched = cur.fetchall()
    if not matched:
        return {"error": f"Regulacja '{code}' nie znaleziona w tabeli compliance_regulations"}

    results = []
    for reg in matched:
        rc = reg["regulation_code"]
        cur.execute(
            """
            SELECT m.doc_path, m.match_reason, d.title
            FROM doc_regulation_mapping m
            LEFT JOIN docs d ON d.path = m.doc_path
            WHERE m.regulation_code = ?
            ORDER BY m.doc_path
        """,
            (rc,),
        )
        docs = cur.fetchall()
        results.append(
            {
                "regulation_code": rc,
                "regulation_name": reg["regulation_name"],
                "affected_templates": [
                    {"path": r["doc_path"], "title": r["title"], "reason": r["match_reason"]}
                    for r in docs
                ],
                "count": len(docs),
            }
        )

    return {
        "query_type": "regulation",
        "query": code,
        "matched_regulations": results,
        "total_affected": sum(r["count"] for r in results),
    }


def analyze_section(conn: sqlite3.Connection, section_name: str) -> dict:
    cur = conn.cursor()
    # Find all docs that have this section heading
    cur.execute(
        """
        SELECT s.doc_uid, s.heading_text, s.anchor, d.title, d.path
        FROM sections s
        JOIN docs d ON s.doc_uid = d.doc_uid
        WHERE s.heading_text LIKE ?
        ORDER BY d.path
    """,
        (f"%{section_name}%",),
    )
    rows = cur.fetchall()

    # Also find content_links that reference this section
    cur.execute(
        """
        SELECT COUNT(*) FROM content_links
        WHERE to_ref LIKE ?
    """,
        (f"%::section::{section_name}%",),
    )
    link_count = cur.fetchone()[0]

    return {
        "query_type": "section",
        "query": section_name,
        "templates_with_section": [
            {
                "path": r["path"],
                "title": r["title"],
                "heading": r["heading_text"],
                "anchor": r["anchor"],
            }
            for r in rows
        ],
        "templates_count": len(rows),
        "content_links_referencing": link_count,
        "note": f"{len(rows)} szablonów posiada tę sekcję; {link_count} content_links do niej prowadzi",
    }


def analyze_doc(conn: sqlite3.Connection, doc_title: str) -> dict:
    cur = conn.cursor()
    cur.execute(
        """
        SELECT doc_uid, title, path FROM docs
        WHERE title LIKE ? OR path LIKE ?
        ORDER BY title
        LIMIT 20
    """,
        (f"%{doc_title}%", f"%{doc_title}%"),
    )
    docs = cur.fetchall()
    if not docs:
        return {"error": f"Dokument '{doc_title}' nie znaleziony"}

    results = []
    for doc in docs:
        uid = doc["doc_uid"]
        # Incoming links (who links TO this doc?)
        cur.execute(
            """
            SELECT COUNT(*) FROM content_links
            WHERE to_ref LIKE ?
        """,
            (f"document::{doc['title']}::%",),
        )
        incoming = cur.fetchone()[0]

        # Outgoing links (what does this doc link TO?)
        cur.execute(
            """
            SELECT COUNT(*) FROM content_links
            WHERE context_doc_uid = ?
        """,
            (uid,),
        )
        outgoing = cur.fetchone()[0]

        # Standards applied
        cur.execute(
            """
            SELECT standard_code FROM doc_standard_mapping WHERE doc_path = ?
        """,
            (doc["path"],),
        )
        standards = [r[0] for r in cur.fetchall()]

        # Regulations applied
        cur.execute(
            """
            SELECT regulation_code FROM doc_regulation_mapping WHERE doc_path = ?
        """,
            (doc["path"],),
        )
        regs = [r[0] for r in cur.fetchall()]

        # Sections in this doc
        cur.execute(
            """
            SELECT heading_text, anchor FROM sections WHERE doc_uid = ? ORDER BY ordinal
        """,
            (uid,),
        )
        sections = [{"heading": r["heading_text"], "anchor": r["anchor"]} for r in cur.fetchall()]

        results.append(
            {
                "title": doc["title"],
                "path": doc["path"],
                "incoming_links": incoming,
                "outgoing_links": outgoing,
                "standards": standards,
                "regulations": regs,
                "sections": sections,
            }
        )

    return {
        "query_type": "document",
        "query": doc_title,
        "matched_docs": results,
        "count": len(results),
    }


def print_table(result: dict):
    qt = result.get("query_type", "")
    q = result.get("query", "")
    print(f"\n=== Analiza wpływu: {qt.upper()} '{q}' ===\n")

    if "error" in result:
        print(f"BŁĄD: {result['error']}")
        return

    if qt == "standard":
        for std in result.get("matched_standards", []):
            print(f"Standard: {std['standard_code']} — {std['standard_name']}")
            print(f"  Dotknięte szablony: {std['count']}")
            for t in std["affected_templates"][:20]:
                print(f"    [{t['reason']:20s}] {t['path']}")
            if std["count"] > 20:
                print(f"    ... i {std['count'] - 20} więcej")
        print(f"\nŁącznie: {result['total_affected']} szablonów")

    elif qt == "regulation":
        for reg in result.get("matched_regulations", []):
            print(f"Regulacja: {reg['regulation_code']} — {reg['regulation_name']}")
            print(f"  Dotknięte szablony: {reg['count']}")
            for t in reg["affected_templates"][:20]:
                print(f"    [{t['reason']:20s}] {t['path']}")
            if reg["count"] > 20:
                print(f"    ... i {reg['count'] - 20} więcej")
        print(f"\nŁącznie: {result['total_affected']} szablonów")

    elif qt == "section":
        print(f"Sekcja: '{q}'")
        print(f"  Szablony z tą sekcją: {result['templates_count']}")
        print(f"  Content_links do niej: {result['content_links_referencing']}")
        for t in result["templates_with_section"][:20]:
            print(f"    [{t['anchor']:40s}] {t['path']}")
        if result["templates_count"] > 20:
            print(f"    ... i {result['templates_count'] - 20} więcej")

    elif qt == "document":
        for doc in result["matched_docs"]:
            print(f"Dokument: {doc['title']}")
            print(f"  Ścieżka:           {doc['path']}")
            print(f"  Linki przychodzące: {doc['incoming_links']}")
            print(f"  Linki wychodzące:   {doc['outgoing_links']}")
            print(f"  Standardy:          {', '.join(doc['standards']) or '(brak)'}")
            print(f"  Regulacje:          {', '.join(doc['regulations']) or '(brak)'}")
            print(f"  Sekcje ({len(doc['sections'])}):      ", end="")
            print(", ".join(s["heading"] for s in doc["sections"][:8]))
            if len(doc["sections"]) > 8:
                print(f"    ... i {len(doc['sections']) - 8} więcej sekcji")
            print()


def main():
    parser = argparse.ArgumentParser(description="Analiza wpływu zmian na szablony IT Dokumentacja")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--standard", metavar="CODE", help="Kod lub nazwa standardu (np. 'ISO/IEC 27001')"
    )
    group.add_argument(
        "--regulation", metavar="CODE", help="Kod lub nazwa regulacji (np. 'KSC-PL')"
    )
    group.add_argument(
        "--section", metavar="NAME", help="Nazwa sekcji (np. 'Standardy i compliance')"
    )
    group.add_argument("--doc", metavar="TITLE", help="Tytuł lub fragment ścieżki dokumentu")
    parser.add_argument(
        "--output",
        choices=["table", "json"],
        default="table",
        help="Format wyjścia: table (domyślnie) lub json",
    )
    parser.add_argument("--save", metavar="FILE", help="Zapisz wynik JSON do pliku")
    args = parser.parse_args()

    conn = connect()
    if args.standard:
        result = analyze_standard(conn, args.standard)
    elif args.regulation:
        result = analyze_regulation(conn, args.regulation)
    elif args.section:
        result = analyze_section(conn, args.section)
    else:
        result = analyze_doc(conn, args.doc)
    conn.close()

    if args.output == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_table(result)

    if args.save:
        save_path = Path(args.save)
        save_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nZapisano do: {save_path}")

    return 0 if "error" not in result else 1


if __name__ == "__main__":
    sys.exit(main())
