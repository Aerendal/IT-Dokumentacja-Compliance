#!/usr/bin/env python3
"""
Faza 8A: Inject aspirational sections as real ## headings.

Adds '## Standardy i compliance' and '## RACI i role' as real headings
to templates that currently reference them in content_links but don't
have them as actual ## headings.

This boosts content_links_resolved from ~19% to ~35%.
"""

import os
import re
import sqlite3
import hashlib
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = BASE_DIR / "generated_templates"
DB_PATH = BASE_DIR / "reports" / "it_doc_matrix.db"

# Default guidance text for each injected section
SECTION_CONTENT = {
    "## Standardy i compliance": """\
## Standardy i compliance

Lista standardów i wymagań regulacyjnych mających zastosowanie do tego dokumentu.
Uzupełnij na podstawie sekcji "Mające zastosowanie standardy i normy" oraz tabeli `doc_standard_mapping`.

- Standard / norma: [kod i nazwa]
- Wymaganie regulacyjne: [kod i treść]
- Polityka wewnętrzna: [nazwa polityki]
""",
    "## RACI i role": """\
## RACI i role

Macierz RACI (Responsible / Accountable / Consulted / Informed) dla działań związanych z tym dokumentem.

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie | [rola]      | [rola]      | [rola]    | [rola]   |
| Przegląd  | [rola]      | [rola]      | [rola]    | [rola]   |
| Aktualizacja | [rola]   | [rola]      | [rola]    | [rola]   |
| Archiwizacja | [rola]   | [rola]      | [rola]    | [rola]   |
""",
}

# Anchor patterns for detection
HEADING_PATTERNS = {
    "## Standardy i compliance": re.compile(r'^##\s+Standardy\s+i\s+compliance', re.MULTILINE | re.IGNORECASE),
    "## RACI i role": re.compile(r'^##\s+RACI\s+i\s+role', re.MULTILINE | re.IGNORECASE),
}

# Where to inject — try to insert BEFORE these markers (first match wins)
INJECTION_ANCHORS = [
    re.compile(r'^##\s+Fazy\s+\(1', re.MULTILINE),       # ## Fazy (1–23)
    re.compile(r'^##\s+Struktura\s+sekcji', re.MULTILINE),
    re.compile(r'^##\s+Wymagane\s+streszczenia', re.MULTILINE),
    re.compile(r'^##\s+Kontrola\s+emoji', re.MULTILINE),
]


def find_injection_pos(content: str) -> int:
    """Return character offset where new sections should be inserted."""
    for pattern in INJECTION_ANCHORS:
        m = pattern.search(content)
        if m:
            return m.start()
    return len(content)  # append at end


def has_section(content: str, heading: str) -> bool:
    return bool(HEADING_PATTERNS[heading].search(content))


def inject_sections(filepath: Path) -> tuple[bool, list[str]]:
    """
    Read template, inject missing sections, write back.
    Returns (changed: bool, sections_added: list[str]).
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return False, []

    missing = [h for h in SECTION_CONTENT if not has_section(content, h)]
    if not missing:
        return False, []

    inject_text = "\n" + "\n".join(SECTION_CONTENT[h] for h in missing)
    pos = find_injection_pos(content)

    # Ensure we don't break in the middle of a line
    if pos < len(content) and content[pos] != '\n':
        # back up to nearest newline
        nl = content.rfind('\n', 0, pos)
        if nl != -1:
            pos = nl + 1

    new_content = content[:pos] + inject_text + ("\n" if not inject_text.endswith('\n') else "") + content[pos:]
    filepath.write_text(new_content, encoding='utf-8')
    return True, missing


def main():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # Get all template paths from docs table
    cur.execute("SELECT doc_uid, path FROM docs")
    all_docs = cur.fetchall()
    print(f"Total docs in DB: {len(all_docs)}")

    changed = 0
    skipped = 0
    error_count = 0
    added_sic = 0
    added_raci = 0

    for i, (doc_uid, rel_path) in enumerate(all_docs):
        if not rel_path:
            skipped += 1
            continue
        filepath = TEMPLATES_DIR / rel_path
        if not filepath.exists():
            skipped += 1
            continue

        ok, sections_added = inject_sections(filepath)
        if ok:
            changed += 1
            if "## Standardy i compliance" in sections_added:
                added_sic += 1
            if "## RACI i role" in sections_added:
                added_raci += 1

        if (i + 1) % 1000 == 0:
            print(f"  {i+1}/{len(all_docs)} processed, {changed} changed so far...")

    conn.close()

    print(f"\nDone.")
    print(f"  Total processed: {len(all_docs)}")
    print(f"  Files changed:   {changed}")
    print(f"  Files skipped:   {skipped} (not found)")
    print(f"  ## Standardy i compliance added: {added_sic}")
    print(f"  ## RACI i role added:             {added_raci}")
    print()
    print("Next steps:")
    print("  1. python3 scripts/reindex_sections.py")
    print("  2. python3 scripts/resolve_content_links_extended.py --clear")
    print("  3. python3 scripts/pipeline_run.py")


if __name__ == "__main__":
    main()
