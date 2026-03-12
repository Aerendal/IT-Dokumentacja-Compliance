#!/usr/bin/env python3
"""
scripts/enrich_small_templates.py

Faza 10: Uzupełnienie małych szablonów (<3KB) o brakujące sekcje.

Małe szablony mają tylko 6-8 sekcji. Wszystkie duże szablony (~6600 plików)
mają ~20+ sekcji z pełnym guidance. Ten skrypt wstrzykuje brakujące sekcje
do 914 małych szablonów tak by każdy miał tę samą strukturę co duże.

Podejście:
- Zachowuje frontmatter i istniejące sekcje bez zmian
- Wstrzykuje brakujące sekcje w kanonicznym porządku
- Aktualizuje frontmatter: status=needs_content (bez zmian), aligned_rev++
"""

import re
import sys
from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent.parent / "generated_templates" / "core"
MAX_SIZE_BYTES = 9000  # pliki ponizej 9KB uznajemy za "male"

# Kanoniczny porządek wszystkich sekcji (na podstawie analizy 6600 duzych szablonow)
CANONICAL_ORDER = [
    "## Metadane",
    "## Cel dokumentu",
    "## Zakres i granice",
    "## Użytkownicy i interesariusze",
    "## Wejścia i wyjścia",
    "## Założenia",
    "## Otwarte pytania",
    "## Powiązania (meta)",
    "## Zależności dokumentu",
    "## Fazy cyklu życia",
    "## Struktura sekcji (szkielet)",
    "## Szybkie powiązania",
    "## Mające zastosowanie standardy i normy",
    "## Standardy i compliance",
    "## RACI i role",
    "## Jak używać dokumentu",
    "## Checklisty jakości",
    "## Definicje robocze",
    "## Przykłady użycia",
    "## Ryzyka i ograniczenia",
    "## Decyzje i uzasadnienia",
    "## Powiązania z innymi dokumentami",
    "## Powiązania z sekcjami innych dokumentów",
    "## Słownik pojęć w dokumencie",
    "## Wymagane odwołania do standardów",
    "## Mapa relacji sekcja→sekcja",
    "## Mapa relacji dokument→dokument",
    "## Ścieżki informacji",
    "## Weryfikacja spójności",
    "## Lista kontrolna spójności relacji",
    "## Artefakty powiązane",
    "## Ścieżka decyzji",
    "## Ścieżka akceptacji",
    "## Metryki jakości",
    "## Kryteria ukończenia",
]

# Domyślna treść guidance dla każdej sekcji (jezyk PL, zgodnie z filozofia projektu)
SECTION_GUIDANCE = {
    "## Zakres i granice": """\
Opisz co wchodzi w zakres tego dokumentu, a co jest poza nim.
Przykład: „Obejmuje: [lista obszarów]. Nie obejmuje: [lista wyłączeń]."
Podaj granice odpowiedzialności, systemy/procesy których dokument dotyczy oraz te, które są z niego wyłączone.""",
    "## Użytkownicy i interesariusze": """\
- [Rola / interesariusz] — [potrzeby i odpowiedzialności]
- [Rola / interesariusz] — [potrzeby i odpowiedzialności]""",
    "## Wejścia i wyjścia": """\
- Wejścia: [dokumenty, dane, decyzje potrzebne przed rozpoczęciem pracy z tym dokumentem]
- Wyjścia: [dokumenty, decyzje, artefakty produkowane na podstawie tego dokumentu]""",
    "## Założenia": """\
- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]""",
    "## Otwarte pytania": """\
- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]""",
    "## Powiązania (meta)": """\
- Wymaga odniesienia do: [dokument lub sekcja źródłowa]
- Wymaga odniesienia do: [dokument lub sekcja źródłowa]
- Dostarcza do: [dokument lub sekcja docelowa]""",
    "## Zależności dokumentu": """\
- Konsumuje: [dokumenty wejściowe — co musi istnieć zanim ten dokument powstanie]
- Dostarcza do: [dokumenty wyjściowe — co korzysta z tego dokumentu]""",
    "## Fazy cyklu życia": """\
Dla każdej fazy określ, czy dokument w tej fazie: powstaje, jest aktualizowany, przeglądany czy archiwizowany.
- Faza 1 – Koncepcja i Wizja: [akcja i odpowiedzialny]
- Faza 2 – Analiza Wymagań: [akcja i odpowiedzialny]
- Faza 3 – Projekt / Design: [akcja i odpowiedzialny]
- Faza 4 – Planowanie: [akcja i odpowiedzialny]
- Faza 5 – Implementacja: [akcja i odpowiedzialny]
- Faza 6 – Testowanie / QA: [akcja i odpowiedzialny]
- Faza 7 – Bezpieczeństwo / Compliance: [akcja i odpowiedzialny]
- Faza 8 – Wdrożenie / Deployment: [akcja i odpowiedzialny]
- Faza 9 – Operacje / Maintenance: [akcja i odpowiedzialny]""",
    "## Definicje robocze": """\
- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]""",
    "## Przykłady użycia": """\
- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]""",
    "## Ryzyka i ograniczenia": """\
- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]""",
    "## Decyzje i uzasadnienia": """\
- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]""",
    "## Powiązania z innymi dokumentami": """\
- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]""",
    "## Powiązania z sekcjami innych dokumentów": """\
- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]""",
    "## Słownik pojęć w dokumencie": """\
- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]""",
    "## Wymagane odwołania do standardów": """\
- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]""",
    "## Mapa relacji sekcja→sekcja": """\
- [Sekcja A] -> [Sekcja B] : [typ relacji: rozszerza/streszcza/wymaga/wyklucza]
- [Sekcja C] -> [Sekcja D] : [typ relacji]""",
    "## Mapa relacji dokument→dokument": """\
- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]""",
    "## Ścieżki informacji": """\
- [Wejście] -> [Sekcja źródłowa] -> [Sekcja rozwinięcia] -> [Wyjście]
- [Wejście] -> [Sekcja źródłowa] -> [Sekcja streszczenia] -> [Wyjście]""",
    "## Weryfikacja spójności": """\
- [ ] Czy wszystkie ścieżki informacji są zamknięte (każde wejście ma wyjście)?
- [ ] Czy istnieją pętle lub sprzeczne relacje między sekcjami?
- [ ] Czy sekcje kluczowe mają wskazane źródła i odbiorców?
- [ ] Czy terminologia jest spójna z sekcją "Słownik pojęć"?""",
    "## Lista kontrolna spójności relacji": """\
- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?""",
    "## Artefakty powiązane": """\
- [Artefakt 1, np. diagram architektury] — [opis i relacja do tego dokumentu]
- [Artefakt 2, np. schemat bazy danych] — [opis i relacja do tego dokumentu]""",
    "## Ścieżka decyzji": """\
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]""",
    "## Ścieżka akceptacji": """\
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]""",
    "## Metryki jakości": """\
- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]""",
    "## Kryteria ukończenia": """\
- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]""",
}


def parse_file(text: str) -> tuple[str, dict[str, str], list[str]]:
    """
    Returns (frontmatter, sections_dict, section_order).
    frontmatter: raw YAML block including --- delimiters
    sections_dict: heading -> body (including trailing newlines)
    section_order: list of headings in original order
    """
    # Extract frontmatter
    fm = ""
    body_start = 0
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[: end + 4]
            body_start = end + 4

    body = text[body_start:]

    # Split into sections
    parts = re.split(r"^(#{1,3} .+)$", body, flags=re.MULTILINE)
    sections = {}
    order = []

    # Parts: [pre_content, heading1, body1, heading2, body2, ...]
    pre = parts[0] if parts else ""
    for i in range(1, len(parts) - 1, 2):
        heading = parts[i].rstrip()
        body_part = parts[i + 1] if i + 1 < len(parts) else ""
        # Only process ## headings (H2) as section dividers
        if heading.startswith("## "):
            if heading not in sections:
                sections[heading] = body_part
                order.append(heading)
        else:
            # H1 or H3 — treat as part of previous section's body or pre
            if order:
                sections[order[-1]] += heading + (parts[i + 1] if i + 1 < len(parts) else "")
            else:
                pre += heading + (parts[i + 1] if i + 1 < len(parts) else "")

    return fm, pre, sections, order


def rebuild_file(fm: str, pre: str, sections: dict, order: list) -> str:
    """Rebuild file from parts."""
    out = fm
    if pre.strip():
        out += "\n" + pre.lstrip("\n")

    for heading in order:
        out += "\n" + heading + "\n"
        body = sections.get(heading, "")
        if body and not body.startswith("\n"):
            body = "\n" + body
        if body and not body.endswith("\n"):
            body += "\n"
        out += body

    return out


def enrich_file(path: Path) -> bool:
    """Add missing sections to a small template. Returns True if modified."""
    text = path.read_text(encoding="utf-8")
    fm, pre, sections, order = parse_file(text)

    # Find which canonical sections are missing
    missing = [s for s in CANONICAL_ORDER if s not in sections]
    if not missing:
        return False

    # Build new order: canonical order for known sections + unknown extras at end
    unknown_extras = [s for s in order if s not in CANONICAL_ORDER]

    new_order = []
    for s in CANONICAL_ORDER:
        if s in sections or s in missing:
            new_order.append(s)
    new_order.extend(unknown_extras)

    # Add missing sections with guidance content
    for s in missing:
        guidance = SECTION_GUIDANCE.get(s, "- [Uzupełnij zgodnie z kontekstem dokumentu]")
        sections[s] = "\n" + guidance + "\n"

    # Bump aligned_rev in frontmatter
    def bump_rev(fm_text: str) -> str:
        def inc(m):
            return f"aligned_rev: {int(m.group(1)) + 1}"

        return re.sub(r"aligned_rev:\s*(\d+)", inc, fm_text)

    new_fm = bump_rev(fm)

    new_text = rebuild_file(new_fm, pre, sections, new_order)
    path.write_text(new_text, encoding="utf-8")
    return True


def main():
    dry_run = "--dry-run" in sys.argv

    # Find small files
    small_files = [f for f in TEMPLATES_DIR.glob("*.md") if f.stat().st_size < MAX_SIZE_BYTES]
    small_files.sort()

    print(
        f"Faza 10 — Uzupelnianie malych szablonow ({len(small_files)} plikow <{MAX_SIZE_BYTES // 1024}KB)"
    )
    if dry_run:
        print("  [DRY RUN — brak zapisu]")

    modified = 0
    skipped = 0
    for f in small_files:
        if dry_run:
            text = f.read_text(encoding="utf-8")
            fm, pre, sections, order = parse_file(text)
            missing = [s for s in CANONICAL_ORDER if s not in sections]
            if missing:
                print(f"  {f.name}: brakuje {len(missing)} sekcji: {missing[:3]}...")
                modified += 1
            else:
                skipped += 1
        else:
            try:
                if enrich_file(f):
                    modified += 1
                else:
                    skipped += 1
            except Exception as e:
                print(f"  BLAD {f.name}: {e}")

        if not dry_run and modified % 100 == 0 and modified > 0:
            print(f"  ...{modified} plikow zaktualizowanych...")

    print(f"\nGotowe: {modified} zmodyfikowanych, {skipped} juz kompletnych.")


if __name__ == "__main__":
    main()
