#!/usr/bin/env python3
"""
map_standards_to_docs.py — Mapuje dokumenty IT na standardy według słów kluczowych.
Dane reguł: config/standard_rules.yaml
"""

from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path

import yaml

DB_DEFAULT = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"

_RULES_YAML = Path(__file__).parent.parent / "config" / "standard_rules.yaml"


def _load_rules() -> list[tuple[list[str], list[str]]]:
    """Wczytuje reguły mapowania z config/standard_rules.yaml."""
    data = yaml.safe_load(_RULES_YAML.read_text(encoding="utf-8"))
    return [(r["keywords"], r["standards"]) for r in data["rules"]]


STANDARD_RULES: list[tuple[list[str], list[str]]] = _load_rules()

# ---------------------------------------------------------------------------

def create_mapping_tables(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS doc_standard_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_path TEXT NOT NULL,
            standard_code TEXT NOT NULL,
            match_reason TEXT,
            UNIQUE(doc_path, standard_code)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS doc_regulation_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_path TEXT NOT NULL,
            regulation_code TEXT NOT NULL,
            match_reason TEXT,
            UNIQUE(doc_path, regulation_code)
        )
    """)
    conn.commit()


def match_rules(path: str, title: str, rules: list) -> list[str]:
    """Zwraca liste dopasowanych kodow dla danej sciezki/tytulu."""
    combined = (path + " " + title).lower()
    matched = set()
    for keywords, codes in rules:
        for kw in keywords:
            if kw.lower() in combined:
                matched.update(codes)
                break
    return sorted(matched)


def build_mappings(conn: sqlite3.Connection, dry_run: bool = False):
    cur = conn.cursor()

    # Pobierz wszystkie dokumenty
    cur.execute("SELECT doc_uid, path, title FROM docs")
    docs = cur.fetchall()
    print(f"  Dokumentow do przetworzenia: {len(docs)}")

    std_inserts = []
    reg_inserts = []
    std_total = 0
    reg_total = 0

    for _doc_uid, path, title in docs:
        path = path or ""
        title = title or ""

        std_codes = match_rules(path, title, STANDARD_RULES)
        for code in std_codes:
            std_inserts.append((path, code, "keyword_match"))
            std_total += 1

        reg_codes = match_rules(path, title, REGULATION_RULES)
        for code in reg_codes:
            reg_inserts.append((path, code, "keyword_match"))
            reg_total += 1

    print(f"  doc_standard_mapping: {std_total} wpisow dla {len(docs)} dokumentow")
    print(f"  doc_regulation_mapping: {reg_total} wpisow dla {len(docs)} dokumentow")

    if not dry_run:
        cur.execute("DELETE FROM doc_standard_mapping")
        cur.execute("DELETE FROM doc_regulation_mapping")
        cur.executemany(
            "INSERT OR IGNORE INTO doc_standard_mapping (doc_path, standard_code, match_reason) VALUES (?,?,?)",
            std_inserts,
        )
        cur.executemany(
            "INSERT OR IGNORE INTO doc_regulation_mapping (doc_path, regulation_code, match_reason) VALUES (?,?,?)",
            reg_inserts,
        )
        conn.commit()
        print("  Zapisano do DB.")


def inject_standards_section(dry_run: bool = False, limit: int = 0):
    """
    Wstrzykuje sekcje 'Majace zastosowanie standardy i normy' do plikow .md.
    Pomija pliki, ktore juz maja te sekcje.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Pobierz mapowanie path -> standardy + regulacje
    cur.execute("""
        SELECT m.doc_path,
               GROUP_CONCAT(DISTINCT s.standard_code) AS stds,
               GROUP_CONCAT(DISTINCT s.standard_name) AS std_names
        FROM doc_standard_mapping m
        JOIN standards s ON m.standard_code = s.standard_code
        GROUP BY m.doc_path
    """)
    std_map = {
        r[0]: list(zip(r[1].split(","), r[2].split(","))) if r[1] else [] for r in cur.fetchall()
    }

    cur.execute("""
        SELECT m.doc_path,
               GROUP_CONCAT(DISTINCT r.regulation_code) AS regs,
               GROUP_CONCAT(DISTINCT r.regulation_name) AS reg_names
        FROM doc_regulation_mapping m
        JOIN compliance_regulations r ON m.regulation_code = r.regulation_code
        GROUP BY m.doc_path
    """)
    reg_map = {
        r[0]: list(zip(r[1].split(","), r[2].split(","))) if r[1] else [] for r in cur.fetchall()
    }
    conn.close()

    SECTION_HEADER = "## Mające zastosowanie standardy i normy"
    INJECT_BEFORE = "## Jak używać dokumentu"  # wstrzyknij przed ta sekcja

    modified = 0
    skipped = 0
    processed = 0

    for md_file in sorted(TEMPLATES_ROOT.rglob("*.md")):
        if limit and processed >= limit:
            break

        rel_path = md_file.relative_to(TEMPLATES_ROOT).as_posix()
        stds = std_map.get(rel_path, [])
        regs = reg_map.get(rel_path, [])

        if not stds and not regs:
            skipped += 1
            continue

        content = md_file.read_text(encoding="utf-8")
        if SECTION_HEADER in content:
            skipped += 1
            continue

        # Buduj sekcje
        lines = [SECTION_HEADER, ""]
        if stds:
            lines.append("### Standardy międzynarodowe")
            for code, name in stds:
                lines.append(f"- **{code}** — {name}")
            lines.append("")
        if regs:
            lines.append("### Polskie normy i regulacje")
            for code, name in regs:
                lines.append(f"- **{code}** — {name}")
            lines.append("")
        lines.append(
            "> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe "
            "normy/regulacje specyficzne dla kontekstu projektu."
        )
        lines.append("")
        section_text = "\n".join(lines)

        # Wstrzyknij przed "## Jak używać dokumentu" lub na koniec
        if INJECT_BEFORE in content:
            new_content = content.replace(INJECT_BEFORE, section_text + INJECT_BEFORE, 1)
        else:
            new_content = content.rstrip() + "\n\n" + section_text

        processed += 1
        if not dry_run:
            md_file.write_text(new_content, encoding="utf-8")
        modified += 1

    print(
        f"  Zmodyfikowano: {modified} plikow | Pominieto (brak mapowania lub juz ma sekcje): {skipped}"
    )
    if dry_run:
        print("  DRY-RUN — pliki nie zostaly zapisane.")


def main():
    dry_run = "--dry-run" in sys.argv
    limit = 0
    for arg in sys.argv:
        if arg.startswith("--limit="):
            limit = int(arg.split("=")[1])

    if dry_run:
        print("=== TRYB DRY-RUN ===")

    conn = sqlite3.connect(DB_PATH)
    create_mapping_tables(conn)
    build_mappings(conn, dry_run=dry_run)
    conn.close()

    print("\nWstrzykiwanie sekcji standardow do szablonow .md...")
    inject_standards_section(dry_run=dry_run, limit=limit)
    print("Gotowe.")


if __name__ == "__main__":
    main()
