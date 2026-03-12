#!/usr/bin/env python3
"""
scripts/fill_guidance_from_similar.py

Faza 11: Wypelnienie guidance w malych szablonach przez klonowanie z podobnych duzych.

Dla kazdego szablonu z generycznymi placeholderami (tekst w nawiasach [...]):
1. Znajdz najlepiej pasujacy duzy szablon po wspolnych slowach kluczowych tytulu
2. Skopiuj z niego tresc brakujacych sekcji
3. Zaktualizuj aligned_rev

Nie zmienia sekcji ktore juz maja specyficzna tresc (nie sa samo-placeholderami).
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

TEMPLATES_DIR = Path(__file__).parent.parent / "generated_templates" / "core"

# Sekcje ktore chcemy wypelnic guidance (nie te z realnym wypeinieniem przez uzytkownika)
TARGET_SECTIONS = {
    "## Zakres i granice",
    "## Użytkownicy i interesariusze",
    "## Wejścia i wyjścia",
    "## Założenia",
    "## Otwarte pytania",
    "## Powiązania (meta)",
    "## Zależności dokumentu",
    "## Fazy cyklu życia",
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
    "## Cel dokumentu",
    "## Fazy cyklu życia",
    "## Struktura sekcji (szkielet)",
    "## Jak używać dokumentu",
}

PLACEHOLDER_RE = re.compile(
    r'^\s*-\s*\[.+?\]|^\s*\[.+?\]|Uzupelnij zgodnie|Opisz co wchodzi',
    re.MULTILINE
)


def is_placeholder_body(body: str) -> bool:
    """Returns True if the section body is mostly generic placeholders."""
    stripped = body.strip()
    if not stripped:
        return True
    lines = [l.strip() for l in stripped.splitlines() if l.strip()]
    if not lines:
        return True
    placeholder_lines = sum(1 for l in lines if re.match(r'^\[.+\]$|^-\s*\[.+\]$', l))
    # Also check for the generic guidance text we inserted
    generic_markers = [
        "Uzupełnij zgodnie z kontekstem",
        "Opisz co wchodzi w zakres",
        "Dla każdej fazy określ",
        "[akcja i odpowiedzialny]",
        "Faza 1 \u2013 Koncepcja i Wizja: [",
        "[Rola / interesariusz]",
        "[Wej\u015bcia:",
        "Wej\u015bcia: [dokumenty",
        "Konsumuje: [dokumenty wej\u015bciowe",
        "Dostarcza do: [dokumenty wyj\u015bciowe",
        "[Za\u0142o\u017cenie 1",
        "[Pytanie 1",
        "Wymaga odniesienia do: [",
        "Konsumuje: [dokumenty",
        "[Termin 1]",
        "[Przyk\u0142ad 1",
        "[Ryzyko 1",
        "[Decyzja 1",
        "[Dokument A]",
        "[Dokument X",
        "[Poj\u0119cie 1]",
        "[Standard 1",
        "[Sekcja A]",
        "[Wej\u015bcie]",
        "[Artefakt 1",
        "[Decyzja]",
        "[Kto zatwierdza]",
        "[Metryka 1",
        "[Kryterium 1",
    ]
    for marker in generic_markers:
        if marker in stripped:
            return True
    if len(lines) > 0 and placeholder_lines / len(lines) > 0.5:
        return True
    return False


def extract_title_from_file(text: str, filename: str) -> str:
    """Extract document title from H1 heading or filename."""
    m = re.search(r'^# (.+)$', text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return filename.replace("_", " ").replace(".md", "")


def title_keywords(title: str) -> set:
    """Extract meaningful keywords from title."""
    stop = {"and", "or", "the", "a", "an", "of", "in", "for", "to", "with",
            "plan", "document", "dokumentu", "i", "w", "z", "do", "na", "dla",
            "oraz", "lub", "jak", "jest", "nie", "co", "sie"}
    words = re.findall(r'[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+', title.lower())
    return {w for w in words if len(w) > 2 and w not in stop}


def parse_sections(text: str) -> dict:
    """Parse H2 sections from markdown text."""
    parts = re.split(r'^(## .+)$', text, flags=re.MULTILINE)
    sections = {}
    for i in range(1, len(parts) - 1, 2):
        heading = parts[i].rstrip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        if heading not in sections:
            sections[heading] = body
    return sections


def build_large_template_index() -> list[tuple[set, dict, str]]:
    """
    Build index of large templates: [(keywords, sections, filename), ...]
    Only load files > 8KB (truly large, well-developed templates).
    """
    index = []
    for f in TEMPLATES_DIR.glob("*.md"):
        if f.stat().st_size < 8000:
            continue
        try:
            text = f.read_text(encoding="utf-8")
            title = extract_title_from_file(text, f.name)
            kw = title_keywords(title)
            sections = parse_sections(text)
            # Only include templates with rich section content
            rich_sections = {k: v for k, v in sections.items()
                             if k in TARGET_SECTIONS and not is_placeholder_body(v)}
            if len(rich_sections) >= 5:
                index.append((kw, rich_sections, f.name))
        except Exception:
            pass
    return index


def find_best_match(target_kw: set, index: list, exclude_name: str | None = None) -> dict | None:
    """Find the large template with highest keyword overlap (excluding self)."""
    best_score = 0
    best_sections = None
    for kw, sections, fname in index:
        if fname == exclude_name:
            continue  # never match self
        if not kw or not target_kw:
            continue
        score = len(target_kw & kw) / max(len(target_kw | kw), 1)
        if score > best_score:
            best_score = score
            best_sections = sections
    if best_score >= 0.01:
        return best_sections
    return None


def rebuild_file_with_new_sections(text: str, updated_sections: dict) -> str:
    """Replace section bodies in text with updated ones."""
    result = text
    for heading, new_body in updated_sections.items():
        # Find and replace just this section's body
        pattern = re.compile(
            r'(^' + re.escape(heading) + r'\n)(.*?)(?=^## |\Z)',
            re.MULTILINE | re.DOTALL
        )
        replacement = r'\g<1>' + new_body.lstrip("\n")
        result = pattern.sub(replacement, result)
    return result


def bump_rev(text: str) -> str:
    def inc(m):
        return f"aligned_rev: {int(m.group(1)) + 1}"
    return re.sub(r'aligned_rev:\s*(\d+)', inc, text)


def main():
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv

    print("Faza 11 — Budowanie indeksu duzych szablonow...")
    index = build_large_template_index()
    print(f"  Zaladowano {len(index)} duzych szablonow jako wzorce.")

    # Find files that still have placeholder sections
    candidates = []
    for f in sorted(TEMPLATES_DIR.glob("*.md")):
        try:
            text = f.read_text(encoding="utf-8")
            sections = parse_sections(text)
            needs_fill = {k for k, v in sections.items()
                          if k in TARGET_SECTIONS and is_placeholder_body(v)}
            if needs_fill:
                candidates.append((f, text, sections, needs_fill))
        except Exception:
            pass

    print(f"  {len(candidates)} szablonow z placeholderami do wypelnienia.")

    if dry_run:
        for f, text, sections, needs_fill in candidates[:10]:
            title = extract_title_from_file(text, f.name)
            kw = title_keywords(title)
            match = find_best_match(kw, index)
            matched_name = "BRAK"
            for kw2, secs, fname in index:
                if secs is match:
                    matched_name = fname
                    break
            print(f"  {f.name} -> {matched_name} ({len(needs_fill)} sekcji)")
        return

    modified = 0
    no_match = 0

    for f, text, sections, needs_fill in candidates:
        title = extract_title_from_file(text, f.name)
        target_kw = title_keywords(title)
        donor = find_best_match(target_kw, index, exclude_name=f.name)

        updates = {}
        if donor:
            for sec in needs_fill:
                if sec in donor and not is_placeholder_body(donor[sec]):
                    updates[sec] = "\n" + donor[sec].strip() + "\n"
        else:
            no_match += 1
            continue  # keep generic placeholder if no match

        if not updates:
            no_match += 1
            continue

        new_text = rebuild_file_with_new_sections(text, updates)
        new_text = bump_rev(new_text)

        if verbose:
            print(f"  {f.name}: {len(updates)} sekcji z donor")

        f.write_text(new_text, encoding="utf-8")
        modified += 1

        if modified % 100 == 0:
            print(f"  ...{modified} plikow zaktualizowanych...")

    print(f"\nGotowe: {modified} plikow zaktualizowanych, {no_match} bez dopasowania.")


if __name__ == "__main__":
    main()
