#!/usr/bin/env python3
"""
scripts/seed_document_types.py

Faza 9B: Zasilenie tabeli document_types.
Typy dokumentów IT z polskimi nazwami, opisami, typowym właścicielem i formatem.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"

DOCUMENT_TYPES = [
    # (type_code, name_pl, name_en, description, typical_owner, typical_format, template_available)
    (
        "POLICY",
        "Polityka",
        "Policy",
        "Dokument strategiczny definiujący zasady i reguły postępowania w organizacji",
        "CISO / CTO / MGR",
        "Markdown / PDF",
        1,
    ),
    (
        "STANDARD",
        "Standard",
        "Standard",
        "Specyfikacja techniczna lub procesowa obowiązująca w organizacji",
        "ARCH / SEC",
        "Markdown / PDF",
        1,
    ),
    (
        "PROCEDURE",
        "Procedura",
        "Procedure",
        "Krok po kroku opis wykonywania czynności operacyjnych",
        "OPS / DEVOPS",
        "Markdown",
        1,
    ),
    (
        "RUNBOOK",
        "Runbook operacyjny",
        "Runbook",
        "Zestaw kroków do wykonania w odpowiedzi na zdarzenie lub rutynową operację",
        "SRE / OPS",
        "Markdown",
        1,
    ),
    (
        "PLAYBOOK",
        "Playbook",
        "Playbook",
        "Zestaw scenariuszy i odpowiedzi na konkretne typy incydentów lub sytuacji",
        "SRE / SEC",
        "Markdown",
        1,
    ),
    (
        "CHECKLIST",
        "Checklista",
        "Checklist",
        "Lista kontrolna do weryfikacji spełnienia wymagań lub kroków procesu",
        "QA / OPS",
        "Markdown",
        1,
    ),
    (
        "SPEC",
        "Specyfikacja",
        "Specification",
        "Szczegółowy opis wymagań funkcjonalnych lub technicznych",
        "BA / DEV",
        "Markdown",
        1,
    ),
    (
        "ADR",
        "Decyzja architektoniczna",
        "Architecture Decision Record",
        "Dokumentacja decyzji architektonicznej z kontekstem, opcjami i uzasadnieniem",
        "ARCH / SA",
        "Markdown",
        1,
    ),
    (
        "DESIGN",
        "Dokument projektowy",
        "Design Document",
        "Projekt techniczny komponentu lub systemu",
        "ARCH / DEV",
        "Markdown / Diagram",
        1,
    ),
    (
        "REPORT",
        "Raport",
        "Report",
        "Dokument analityczny lub statusowy prezentujący wyniki lub postęp",
        "PM / BA / MGR",
        "Markdown / PDF",
        1,
    ),
    (
        "PLAN",
        "Plan",
        "Plan",
        "Dokument planistyczny określający cele, harmonogram i zasoby",
        "PM / PO",
        "Markdown",
        1,
    ),
    (
        "GUIDE",
        "Przewodnik",
        "Guide",
        "Dokument instruktażowy opisujący jak korzystać z systemu lub procesu",
        "DEVOPS / TRAIN",
        "Markdown",
        1,
    ),
    (
        "MATRIX",
        "Matryca",
        "Matrix",
        "Tabelaryczne zestawienie relacji (np. RACI, traceability, zależności)",
        "PM / BA",
        "Markdown / Tabela",
        1,
    ),
    (
        "REGISTER",
        "Rejestr",
        "Register",
        "Ewidencja elementów (ryzyk, decyzji, zmian, incydentów)",
        "PM / RISK / MGR",
        "Markdown / Tabela",
        1,
    ),
    (
        "CONTRACT",
        "Umowa / SLA",
        "Contract / SLA",
        "Formalne porozumienie z dostawcą lub klientem wewnętrznym",
        "LEGAL / VENDOR",
        "PDF",
        0,
    ),
    (
        "ASSESSMENT",
        "Ocena / Assessment",
        "Assessment",
        "Dokument oceny stanu, ryzyk lub zgodności z wymaganiami",
        "SEC / AUDIT / RISK",
        "Markdown / PDF",
        1,
    ),
    (
        "POSTMORTEM",
        "Postmortem",
        "Postmortem",
        "Analiza incydentu lub awarii po jego zakończeniu",
        "SRE / DEV",
        "Markdown",
        1,
    ),
    (
        "RFC",
        "Wniosek o zmianę",
        "Request for Change",
        "Formalny wniosek o wprowadzenie zmiany w systemie lub procesie",
        "CHANGE / MGR",
        "Markdown / Form",
        1,
    ),
    (
        "ONBOARDING",
        "Dokumentacja wdrożeniowa",
        "Onboarding Documentation",
        "Materiały dla nowych członków zespołu lub użytkowników systemu",
        "TRAIN / MGR",
        "Markdown",
        1,
    ),
    (
        "ARCHITECTURE",
        "Dokument architektoniczny",
        "Architecture Document",
        "Opis architektury systemu: komponenty, interfejsy, integracje",
        "ARCH / EA",
        "Markdown / Diagram",
        1,
    ),
]


def main():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # Check available columns
    cur.execute("PRAGMA table_info(document_types)")
    cols = {r[1] for r in cur.fetchall()}

    inserted = 0
    for dt in DOCUMENT_TYPES:
        type_code, name_pl, name_en, desc, owner, fmt, tmpl = dt
        try:
            if "type_code" in cols and "name_pl" in cols and "name_en" in cols:
                cur.execute(
                    """
                    INSERT OR IGNORE INTO document_types
                      (type_code, name_pl, name_en, type_description, typical_owner, typical_format, template_available)
                    VALUES (?,?,?,?,?,?,?)
                """,
                    (type_code, name_pl, name_en, desc, owner, fmt, tmpl),
                )
            elif "type_code" in cols and "name_pl" in cols:
                insert_cols = ["type_code", "name_pl", "template_available"]
                insert_vals = [type_code, name_pl, tmpl]
                for col, val in [
                    ("type_name", name_pl),
                    ("type_description", desc),
                    ("typical_owner", owner),
                    ("typical_format", fmt),
                    ("name", name_pl),
                    ("description", desc),
                ]:
                    if col in cols and col not in insert_cols:
                        insert_cols.append(col)
                        insert_vals.append(val)
                ph = ",".join("?" * len(insert_vals))
                cur.execute(
                    f"INSERT OR IGNORE INTO document_types ({','.join(insert_cols)}) VALUES ({ph})",
                    insert_vals,
                )
            elif "code" in cols:
                cur.execute(
                    """
                    INSERT OR IGNORE INTO document_types (code, name, description)
                    VALUES (?,?,?)
                """,
                    (type_code, name_pl, desc),
                )
            if cur.rowcount:
                inserted += 1
        except Exception as e:
            print(f"  Błąd {type_code}: {e}")

    conn.commit()
    conn.close()
    print(f"Faza 9B — document_types: wstawiono {inserted} wierszy.")


if __name__ == "__main__":
    main()
