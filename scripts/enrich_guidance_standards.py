#!/usr/bin/env python3
"""Faza 5: Wzbogacenie doc_section_guidance o referencje do standardow i regulacji.

Logika:
  1. Dla kazdego rekordu guidance pobierz standardy przypisane do danego dokumentu
     (z doc_standard_mapping/doc_regulation_mapping via docs.title).
  2. Dodaj standardy specyficzne dla tytulu sekcji (np. testowanie -> IEEE 829).
  3. Zapisz do standards_refs / regulations_refs jako JSON-liste kodow.
"""

import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"

# Sekcja -> dodatkowe standardy miedzynarodowe (kody z tabeli standards)
SECTION_STANDARDS: dict[str, list[str]] = {
    "faza 1: koncepcja i wizja":      ["ISO 20000-1", "PMBOK 7", "PRINCE2 7", "TOGAF ADM"],
    "faza 2: analiza wymagan":        ["IEEE 830", "ISO/IEC 12207", "PMBOK 7"],
    "faza 3: projekt / design":       ["IEEE 1016", "IEEE 42010", "TOGAF ADM"],
    "faza 4: planowanie":             ["PMBOK 7", "PRINCE2 7", "SAFe 6.0", "ISO 20000-1"],
    "faza 5: implementacja":          ["ISO/IEC 12207", "SAFe 6.0", "SCRUM Guide"],
    "faza 6: testowanie / qa":        ["IEEE 829", "ISO/IEC 12207", "OWASP ASVS"],
    "faza 7: bezpieczenstwo / compliance": [
        "ISO/IEC 27001", "ISO/IEC 27002", "NIS2", "DORA", "CIS Controls v8", "OWASP ASVS"
    ],
    "faza 8: wdrozenie / deployment": ["ISO 20000-1", "ITIL 4", "ISO/IEC 27001"],
    "faza 9: operacje / maintenance": ["ITIL 4", "ISO 20000-1", "ISO/IEC 27001"],
    "faza 10: incident management":   ["ITIL 4", "ISO 20000-1", "NIST CSF", "ISO 22301"],
    "faza 11: monitoring / observability": ["ITIL 4", "ISO 20000-1", "NIST SP 800-53"],
    "faza 12: dokumentacja referencyjna": ["ISO/IEC 12207", "IEEE 1016", "ISO 20000-1"],
    "faza 13: szkolenie / onboarding": ["ISO 20000-1", "ITIL 4"],
    "faza 14: komunikacja stakeholders": ["PMBOK 7", "PRINCE2 7"],
    "faza 15: knowledge management":  ["ITIL 4", "ISO 20000-1"],
    "faza 16: postmortem / retrospektywa": ["ITIL 4", "SCRUM Guide", "PMBOK 7"],
    "faza 17: budzetowanie / cost management": ["COBIT 2019", "PMBOK 7", "ISO/IEC 38500"],
    "faza 18: vendor management":     ["ISO 20000-1", "ISO/IEC 38500", "COBIT 2019"],
    "faza 19: governance / compliance": ["COBIT 2019", "ISO/IEC 38500", "ISO/IEC 27001", "ITIL 4"],
    "faza 20: decommission / sunset": ["ISO 20000-1", "ISO/IEC 27001", "COBIT 2019"],
    "faza 21: dr / bcp":              ["ISO 22301", "NIST CSF", "ITIL 4", "ISO/IEC 27001"],
    "faza 22: change management":     ["ITIL 4", "ISO 20000-1", "COBIT 2019"],
    "faza 23: capacity planning":     ["ITIL 4", "ISO 20000-1", "COBIT 2019"],
    "raci i role":                    ["COBIT 2019", "ITIL 4", "PMBOK 7"],
    "standardy i compliance":         ["ISO/IEC 27001", "ISO 9001", "COBIT 2019", "ITIL 4"],
}

# Sekcja -> dodatkowe regulacje PL (kody z tabeli compliance_regulations)
SECTION_REGULATIONS: dict[str, list[str]] = {
    "faza 7: bezpieczenstwo / compliance": ["KSC-PL", "UODO-PL", "CERT-PL-WYTYCZNE"],
    "faza 19: governance / compliance":    ["KSC-PL", "UODO-PL", "PZP-PL"],
    "standardy i compliance":             ["KSC-PL", "UODO-PL"],
    "raci i role":                        ["UODO-PL"],
    "faza 21: dr / bcp":                  ["KSC-PL", "UŚUDE-PL"],
}


def normalize(s: str) -> str:
    s = s.lower().strip()
    # Strip diacritics for comparison
    replacements = [
        ("ą","a"),("ć","c"),("ę","e"),("ł","l"),("ń","n"),
        ("ó","o"),("ś","s"),("ź","z"),("ż","z"),
    ]
    for a, b in replacements:
        s = s.replace(a, b)
    return s


def main():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Pobierz valide kody standardow i regulacji z DB
    cur.execute("SELECT standard_code FROM standards")
    valid_standards = {r["standard_code"] for r in cur.fetchall()}
    cur.execute("SELECT regulation_code FROM compliance_regulations")
    valid_regs = {r["regulation_code"] for r in cur.fetchall()}

    print(f"Standardy w DB: {len(valid_standards)}, Regulacje: {len(valid_regs)}")

    # Zbudo słownik doc_title -> [standard_codes] z doc_standard_mapping
    # doc_standard_mapping: doc_path, standard_code (nie wymaga JOINa na standards)
    cur.execute("""
        SELECT d.title, m.standard_code
        FROM doc_standard_mapping m
        JOIN docs d ON d.path = m.doc_path
    """)
    doc_to_standards: dict[str, list[str]] = {}
    for row in cur.fetchall():
        doc_to_standards.setdefault(row["title"], []).append(row["standard_code"])

    # Zbudo słownik doc_title -> [regulation_codes]
    cur.execute("""
        SELECT d.title, m.regulation_code
        FROM doc_regulation_mapping m
        JOIN docs d ON d.path = m.doc_path
    """)
    doc_to_regs: dict[str, list[str]] = {}
    for row in cur.fetchall():
        doc_to_regs.setdefault(row["title"], []).append(row["regulation_code"])

    print(f"Dokumenty z mapowaniem standardów: {len(doc_to_standards)}")
    print(f"Dokumenty z mapowaniem regulacji: {len(doc_to_regs)}")

    # Pobierz wszystkie guidance rows
    cur.execute("SELECT id, doc_title, section_title FROM doc_section_guidance")
    rows = cur.fetchall()
    print(f"Wierszy guidance do wzbogacenia: {len(rows)}")

    updates = []
    for row in rows:
        doc_title = row["doc_title"]
        sec_title = row["section_title"]
        sec_norm = normalize(sec_title)

        # Standardy: doc-level + section-level
        stds = list(doc_to_standards.get(doc_title, []))
        extra_stds = SECTION_STANDARDS.get(sec_norm, [])
        stds = list(dict.fromkeys(stds + extra_stds))  # unique, ordered
        stds = [s for s in stds if s in valid_standards]

        # Regulacje: doc-level + section-level
        regs = list(doc_to_regs.get(doc_title, []))
        extra_regs = SECTION_REGULATIONS.get(sec_norm, [])
        regs = list(dict.fromkeys(regs + extra_regs))
        regs = [r for r in regs if r in valid_regs]

        stds_json = json.dumps(stds, ensure_ascii=False) if stds else None
        regs_json = json.dumps(regs, ensure_ascii=False) if regs else None

        updates.append((stds_json, regs_json, row["id"]))

    print("Zapisuję...")
    cur.executemany(
        "UPDATE doc_section_guidance SET standards_refs=?, regulations_refs=? WHERE id=?",
        updates
    )
    conn.commit()

    # Statystyki
    cur.execute("SELECT COUNT(*) FROM doc_section_guidance WHERE standards_refs IS NOT NULL")
    n_stds = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM doc_section_guidance WHERE regulations_refs IS NOT NULL")
    n_regs = cur.fetchone()[0]
    print(f"\nWiersze z standards_refs:    {n_stds:>7} / {len(rows)}")
    print(f"Wiersze z regulations_refs: {n_regs:>7} / {len(rows)}")

    # Sample
    cur.execute("""
        SELECT doc_title, section_title, standards_refs, regulations_refs
        FROM doc_section_guidance
        WHERE standards_refs IS NOT NULL LIMIT 5
    """)
    print("\nPróbka:")
    for r in cur.fetchall():
        print(f"  [{r['doc_title'][:40]}] {r['section_title'][:30]}")
        print(f"    std:  {r['standards_refs']}")
        print(f"    regs: {r['regulations_refs']}")

    conn.close()
    print("\nGotowe.")


if __name__ == "__main__":
    main()
