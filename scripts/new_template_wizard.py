#!/usr/bin/env python3
"""Faza 6: Wizard tworzenia nowego szablonu dokumentacji IT.

Uruchomienie interaktywne:
    cd dokumentacja
    python3 scripts/new_template_wizard.py

Uruchomienie nieinteraktywne (CLI):
    python3 scripts/new_template_wizard.py \\
        --title "Zarządzanie Incydentami" \\
        --type "Procedura" \\
        --standard "ISO/IEC 27001" \\
        --regulation "RODO" \\
        --goal "Definiuje proces obsługi incydentów bezpieczeństwa" \\
        --dry-run

Wizard:
  1. Pyta o tytul, branze (ISIC), faze SDLC, powiazane dokumenty, standardy.
  2. Generuje plik .md w generated_templates/core/ lub satellite/.
  3. Wstawia rekord do docs i doc_section_guidance w it_doc_matrix.db.
  4. Uruchamia pipeline (opcjonalnie).
"""

import sys
import re
import json
import sqlite3
import hashlib
import argparse
import unicodedata
from pathlib import Path
from datetime import date

# ── Sciezki ──────────────────────────────────────────────────────────────────
SCRIPT_DIR   = Path(__file__).parent
DOC_DIR      = SCRIPT_DIR.parent
DB_PATH      = DOC_DIR / "reports" / "it_doc_matrix.db"
CORE_DIR     = DOC_DIR / "generated_templates" / "core"
SAT_DIR      = DOC_DIR / "generated_templates" / "satellite"

# ── Stale ─────────────────────────────────────────────────────────────────────
PHASES = [
    "Faza 1: Koncepcja i Wizja",
    "Faza 2: Analiza Wymagań",
    "Faza 3: Projekt / Design",
    "Faza 4: Planowanie",
    "Faza 5: Implementacja",
    "Faza 6: Testowanie / QA",
    "Faza 7: Bezpieczeństwo / Compliance",
    "Faza 8: Wdrożenie / Deployment",
    "Faza 9: Operacje / Maintenance",
    "Faza 10: Incident Management",
    "Faza 11: Monitoring / Observability",
    "Faza 12: Dokumentacja referencyjna",
    "Faza 13: Szkolenie / Onboarding",
    "Faza 14: Komunikacja stakeholders",
    "Faza 15: Knowledge Management",
    "Faza 16: Postmortem / Retrospektywa",
    "Faza 17: Budżetowanie / Cost Management",
    "Faza 18: Vendor Management",
    "Faza 19: Governance / Compliance",
    "Faza 20: Decommission / Sunset",
    "Faza 21: DR / BCP",
    "Faza 22: Change Management",
    "Faza 23: Capacity Planning",
]

STANDARD_GUIDANCE: dict[str, str] = {
    "ISO/IEC 27001":  "System Zarządzania Bezpieczeństwem Informacji",
    "ISO/IEC 27002":  "Katalog kontrolek bezpieczeństwa",
    "ISO/IEC 27005":  "Zarządzanie ryzykiem bezpieczeństwa",
    "ISO 22301":      "Ciągłość działania (BCMS)",
    "ISO 20000-1":    "Zarządzanie usługami IT (ITSM)",
    "ISO 9001":       "System Zarządzania Jakością",
    "ISO/IEC 12207":  "Procesy cyklu życia oprogramowania",
    "IEEE 829":       "Dokumentacja testów",
    "IEEE 830":       "Specyfikacja wymagań oprogramowania",
    "IEEE 1016":      "Dokumentacja projektu oprogramowania",
    "IEEE 42010":     "Architektura systemów i oprogramowania",
    "ITIL 4":         "Zarządzanie usługami IT",
    "TOGAF ADM":      "Architektura korporacyjna",
    "PMBOK 7":        "Zarządzanie projektami",
    "PRINCE2 7":      "Metodologia projektów",
    "COBIT 2019":     "Ład IT i zarządzanie",
    "DORA":           "Cyfrowa odporność operacyjna (finanse)",
    "NIS2":           "Bezpieczeństwo sieci i systemów informacyjnych",
    "NIST CSF":       "Framework cyberbezpieczeństwa NIST",
    "OWASP ASVS":     "Weryfikacja bezpieczeństwa aplikacji",
    "CIS Controls v8":"Kontrole bezpieczeństwa CIS",
    "PCI DSS":        "Bezpieczeństwo danych kart płatniczych",
    "SAFe 6.0":       "Scaled Agile Framework",
    "SCRUM Guide":    "Framework Scrum",
}

REGULATION_GUIDANCE: dict[str, str] = {
    "KSC-PL":           "Ustawa o krajowym systemie cyberbezpieczeństwa",
    "UODO-PL":          "Ustawa o ochronie danych osobowych / RODO-PL",
    "PZP-PL":           "Prawo zamówień publicznych",
    "UŚUDE-PL":         "Ustawa o świadczeniu usług drogą elektroniczną",
    "PN-ISO/IEC-27001":  "Polska Norma — ISO/IEC 27001",
    "CERT-PL-WYTYCZNE":  "Wytyczne CERT Polska",
    "KNF-REKOM-IT":      "Rekomendacje KNF dla sektora finansowego",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(title: str) -> str:
    """Generuje slug nazwy pliku: lowercase, ASCII, podkreslniki."""
    s = unicodedata.normalize("NFKD", title)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
    return s[:80]


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    val = input(f"{prompt}{suffix}: ").strip()
    return val or default


def choose(prompt: str, options: list[str], multi: bool = False) -> list[str]:
    """Interaktywny wybor z listy. Zwraca liste wybranych."""
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"  {i:>2}. {opt}")
    if multi:
        raw = input("  Numery (np. 1,3,7) lub Enter=pomiń: ").strip()
    else:
        raw = input("  Numer lub Enter=pomiń: ").strip()
    if not raw:
        return []
    nums = [int(x.strip()) for x in raw.split(",") if x.strip().isdigit()]
    return [options[n - 1] for n in nums if 1 <= n <= len(options)]


# ── Generowanie pliku .md ─────────────────────────────────────────────────────

def render_template(
    title: str,
    phases: list[str],
    linked_docs: list[str],
    standards: list[str],
    regulations: list[str],
    guidance_cel: str,
) -> str:
    today = date.today().isoformat()

    stds_block = ""
    if standards:
        lines = [f"- **{s}** — {STANDARD_GUIDANCE.get(s, '')}" for s in standards]
        stds_block = "\n### Standardy międzynarodowe\n" + "\n".join(lines)
    regs_block = ""
    if regulations:
        lines = [f"- **{r}** — {REGULATION_GUIDANCE.get(r, '')}" for r in regulations]
        regs_block = "\n### Polskie normy i regulacje\n" + "\n".join(lines)
    standards_section = ""
    if stds_block or regs_block:
        standards_section = (
            "\n## Mające zastosowanie standardy i normy\n"
            + stds_block + regs_block
            + "\n\n> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij.\n"
        )

    links_block = "\n".join(f"- {d}" for d in linked_docs) if linked_docs else "- (brak wskazanych)"

    phases_block = ""
    for ph in phases:
        phases_block += f"\n### {ph}\n- [ ] Opisz działania w tej fazie.\n"

    return f"""---
title: {title}
status: needs_content
aligned: false
aligned_rev: 0
aligned_at: {today}
aligned_by: wizard
---

# {title}

## Metadane
- Właściciel: [Wypełnij]
- Wersja: v0.1
- Data aktualizacji: {today}
- Status: draft

## Cel dokumentu
{guidance_cel or 'Opisz cel i rolę tego dokumentu w procesie.'}

## Zakres i granice
- Obejmuje: (do uzupełnienia)
- Poza zakresem: (do uzupełnienia)

## Wejścia i wyjścia
- Wejścia: (do uzupełnienia)
- Wyjścia: (do uzupełnienia)

## Powiązania (meta)
- Key Documents: (do uzupełnienia)
- Document Dependencies: (do uzupełnienia)

## Zależności dokumentu
(Opisz, od których dokumentów zależy ten szablon i które dokumenty zależą od niego.)

## Fazy cyklu życia
{phases_block}
## Struktura sekcji (szkielet)
(Opisz strukturę wewnętrzną dokumentu — jakie sekcje musi zawierać wypełniona wersja.)

## Wymagane rozwinięcia
(Co musi być doprecyzowane zanim dokument będzie kompletny.)

## Wymagane streszczenia
(Co powinno znaleźć się w streszczeniu wykonawczym dokumentu.)

## Guidance (skrót)
(Krótkie wskazówki dla autora: na co zwrócić uwagę podczas wypełniania.)

## Szybkie powiązania
{links_block}
{standards_section}
## Jak używać dokumentu
1. Uzupełnij sekcje metadane i cel dokumentu.
2. Wypełnij fazy cyklu życia odpowiednie dla kontekstu projektu.
3. Zweryfikuj powiązania z innymi dokumentami biblioteki.

## Checklisty Definition of Ready (DoR)
- [ ] Właściciel dokumentu zidentyfikowany.
- [ ] Zakres i cel dokumentu zatwierdzone przez interesariuszy.

## Checklisty Definition of Done (DoD)
- [ ] Wszystkie sekcje wypełnione zgodnie z guidance.
- [ ] Powiązania z innymi dokumentami zweryfikowane.
- [ ] Dokument zatwierdzony przez właściciela.
"""


# ── Wstawianie do DB ──────────────────────────────────────────────────────────

def ulid_simple(title: str) -> str:
    """Pseudo-ULID na podstawie hash tytulu (dla nowych dokumentow)."""
    h = hashlib.sha256(title.encode()).hexdigest()[:20].upper()
    return h


def insert_to_db(
    conn: sqlite3.Connection,
    title: str,
    path: str,
    standards: list[str],
    regulations: list[str],
) -> None:
    cur = conn.cursor()
    doc_uid = ulid_simple(title)

    # docs
    title_norm = re.sub(r"\s+", " ", title.lower().strip())
    cur.execute(
        "INSERT OR IGNORE INTO docs (doc_uid, title, title_norm, path, origin) VALUES (?,?,?,?,?)",
        (doc_uid, title, title_norm, path, "wizard"),
    )

    # doc_standard_mapping
    for s in standards:
        cur.execute(
            "INSERT OR IGNORE INTO doc_standard_mapping (doc_path, standard_code, match_reason) VALUES (?,?,?)",
            (path, s, "wizard"),
        )

    # doc_regulation_mapping
    for r in regulations:
        cur.execute(
            "INSERT OR IGNORE INTO doc_regulation_mapping (doc_path, regulation_code, match_reason) VALUES (?,?,?)",
            (path, r, "wizard"),
        )

    # Podstawowe guidance rows
    base_sections = [
        ("Cel dokumentu", "Krótko opisz cel i rolę dokumentu w procesie."),
        ("Zakres i granice", "Zdefiniuj zakres tematyczny i organizacyjny."),
        ("Wejścia i wyjścia", "Wymień kluczowe wejścia (dane/dokumenty potrzebne) i wyjścia (rezultaty)."),
        ("Zależności dokumentu", "Wskaż dokumenty zależne i nadrzędne."),
    ]
    stds_json = json.dumps(standards, ensure_ascii=False) if standards else None
    regs_json = json.dumps(regulations, ensure_ascii=False) if regulations else None
    for sec, guide in base_sections:
        cur.execute(
            """INSERT OR IGNORE INTO doc_section_guidance
               (doc_title, section_title, guidance, standards_refs, regulations_refs)
               VALUES (?,?,?,?,?)""",
            (title, sec, guide, stds_json, regs_json),
        )

    conn.commit()
    print(f"  DB: dodano docs+guidance dla '{title}' (uid={doc_uid})")


# ── CLI args ──────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Wizard tworzenia nowego szablonu dokumentacji IT"
    )
    parser.add_argument("--title", help="Tytuł dokumentu")
    parser.add_argument(
        "--type", dest="type",
        help="Typ dokumentu (np. Procedura, Polityka, Instrukcja)"
    )
    parser.add_argument(
        "--standard", action="append",
        help="Kod standardu (można powtarzać, np. --standard 'ISO/IEC 27001')"
    )
    parser.add_argument(
        "--regulation", action="append",
        help="Kod regulacji (można powtarzać, np. --regulation 'RODO')"
    )
    parser.add_argument("--goal", help="Krótki opis celu dokumentu")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Renderuj szablon i wyświetl na stdout bez zapisywania pliku ani wpisu do DB"
    )
    parser.add_argument(
        "--no-pipeline", action="store_true",
        help="Pomiń uruchomienie pipeline_run na końcu"
    )
    parser.add_argument(
        "--db", type=Path, default=None,
        help="Ścieżka do bazy danych legacy-runtime (domyślnie: reports/it_doc_matrix.db)"
    )
    parser.add_argument(
        "--templates-root", type=Path, default=None,
        help="Katalog główny szablonów (domyślnie: generated_templates/)"
    )
    parser.add_argument(
        "--core-dir", type=Path, default=None,
        help="Katalog szablonów core (domyślnie: generated_templates/core/)"
    )
    parser.add_argument(
        "--sat-dir", type=Path, default=None,
        help="Katalog szablonów satellite (domyślnie: generated_templates/satellite/)"
    )
    return parser.parse_args()


# ── Interactive inputs ────────────────────────────────────────────────────────

def get_interactive_inputs() -> dict:
    """Zbiera dane od użytkownika interaktywnie. Zwraca słownik wejść."""
    print("=" * 60)
    print("  WIZARD NOWEGO SZABLONU DOKUMENTACJI IT")
    print("=" * 60)
    print("Ctrl+C aby przerwac.\n")

    title = ask("Tytuł dokumentu (PL)")
    if not title:
        print("Tytul jest wymagany."); sys.exit(1)

    goal = ask("Krotki opis celu dokumentu (opcjonalny)")

    kind = ask("Typ szablonu (core/satellite)", default="core")

    sel_phases = choose(
        "Wybierz fazy cyklu zycia (Enter=wszystkie 23):",
        PHASES,
        multi=True,
    )
    if not sel_phases:
        sel_phases = PHASES

    raw_links = ask("Powiazane dokumenty (tytuły po przecinku, opcjonalnie)")
    linked_docs = [d.strip() for d in raw_links.split(",") if d.strip()] if raw_links else []

    std_list = list(STANDARD_GUIDANCE.keys())
    standards = choose("Standardy miedzynarodowe (opcjonalnie):", std_list, multi=True)

    reg_list = list(REGULATION_GUIDANCE.keys())
    regulations = choose("Polskie regulacje/normy (opcjonalnie):", reg_list, multi=True)

    return {
        "title": title,
        "doc_type": kind.strip().lower(),
        "standards": standards,
        "regulations": regulations,
        "goal": goal,
        "phases": sel_phases,
        "linked_docs": linked_docs,
    }


# ── Core run logic ────────────────────────────────────────────────────────────

def run(
    title: str,
    doc_type: str,
    standards: list,
    regulations: list,
    goal: str,
    dry_run: bool = False,
    no_pipeline: bool = False,
    phases: list | None = None,
    linked_docs: list | None = None,
) -> dict:
    """Renderuje szablon i opcjonalnie zapisuje plik oraz wstawia do DB.

    Zwraca dict: {status: 'ok'/'dry_run', path: str, content: str}
    """
    if phases is None:
        phases = PHASES
    if linked_docs is None:
        linked_docs = []

    target_dir = SAT_DIR if doc_type and doc_type.strip().lower() == "satellite" else CORE_DIR
    out_path = target_dir / f"{slugify(title)}.md"

    content = render_template(title, phases, linked_docs, standards, regulations, goal)

    if dry_run:
        print(content)
        print(f"DRY RUN: Nie zapisano pliku. Ścieżka byłaby: {out_path}")
        return {"status": "dry_run", "path": str(out_path), "content": content}

    # Overwrite check in interactive (tty) sessions
    if out_path.exists() and sys.stdin.isatty():
        overwrite = ask(f"Plik {out_path.name} juz istnieje. Nadpisac? (tak/nie)", default="nie")
        if overwrite.lower() not in ("tak", "t", "yes", "y"):
            print("Anulowano."); sys.exit(0)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")
    rel_path = out_path.relative_to(DOC_DIR / "generated_templates")
    print(f"\n  Plik: generated_templates/{rel_path}")

    db_rel = str(rel_path).replace("\\", "/")
    conn = sqlite3.connect(str(DB_PATH))
    try:
        from itdoc.schema_profile import assert_schema_profile
        assert_schema_profile(conn, "legacy-runtime")
    except RuntimeError as exc:
        conn.close()
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
    insert_to_db(conn, title, db_rel, standards, regulations)
    conn.close()

    if not no_pipeline:
        import subprocess
        pipe_result = subprocess.run(
            ["python3", "scripts/pipeline_run.py"],
            cwd=str(DOC_DIR),
            capture_output=True, text=True,
        )
        print(pipe_result.stdout[-500:] if pipe_result.stdout else "")
        if pipe_result.returncode != 0:
            print("OSTRZEZENIE: pipeline zakonczyl sie bledem.")
        else:
            print("Pipeline: PASS")

    print("\nGotowe! Nowy szablon jest gotowy do edycji.")
    print(f"Sciezka: {out_path}")

    return {"status": "ok", "path": str(out_path), "content": content}


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    args = parse_args()

    if args.title:
        inputs: dict = {
            "title": args.title,
            "doc_type": args.type or "core",
            "standards": args.standard or [],
            "regulations": args.regulation or [],
            "goal": args.goal or "",
        }
    else:
        inputs = get_interactive_inputs()

    run(**inputs, dry_run=args.dry_run, no_pipeline=args.no_pipeline)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrzerwano.")
