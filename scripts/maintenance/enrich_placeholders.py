#!/usr/bin/env python3
"""
enrich_placeholders.py — wypełnia szablony-placeholdery
treścią opisującą: cel, co zawierają, dlaczego i mechanizmy wpływu.
Dane archetypów: config/doc_archetypes.yaml
"""

import argparse
import re
import sqlite3
import sys
from pathlib import Path

import yaml

DB_PATH = Path(__file__).parent.parent.parent / "reports/it_doc_matrix.db"
TDIR = Path(__file__).parent.parent.parent / "generated_templates"
PLACEHOLDER = "opisuje cel dokumentu, decyzje do podjęcia"

_ARCHETYPES_YAML = Path(__file__).parent.parent.parent / "config" / "doc_archetypes.yaml"


def _load_archetypes() -> list:
    """Wczytuje archetypy z config/doc_archetypes.yaml jako listę krotek (keywords, ...).

    Zwraca listę w formacie kompatybilnym z oryginalnym ARCHETYPES:
    każdy element to (keywords: list, purpose, inputs, outputs, impacts, dependencies, relationships).
    """
    data = yaml.safe_load(_ARCHETYPES_YAML.read_text(encoding="utf-8"))
    return [
        (
            arch["keywords"],
            arch["purpose"],
            arch["inputs"],
            arch["outputs"],
            arch["impacts"],
            arch["dependencies"],
            arch["relationships"],
        )
        for arch in data["archetypes"]
    ]


ARCHETYPES: list = _load_archetypes()

# ---------------------------------------------------------------------------

def find_archetype(title: str, content: str):
    tl = title.lower()
    cl = content.lower()
    # Dla placeholderow: najpierw samo dopasowanie tytulu
    for row in ARCHETYPES[:-1]:
        kws = row[0]
        if any(k in tl for k in kws):
            return row[1:]
    # Jezeli tytul nie pasuje, sprawdz tez tresc (nie-generyczna)
    if PLACEHOLDER not in content:
        for row in ARCHETYPES[:-1]:
            kws = row[0]
            if any(k in cl for k in kws):
                return row[1:]
    return ARCHETYPES[-1][1:]


def enrich_content(title: str, content: str, standard: str, parent_title: str = "") -> str:
    cel, wej, wyj, wplyw, zalezny, sekcje = find_archetype(title, content)

    std_blok = f"\nTen szablon jest zgodny ze standardem **{standard}**." if standard else ""
    parent_note = (
        f'\n\n> Dokument satelitarny do: "{parent_title}" - rozszerza lub uszczegolawia jego tresc.'
        if parent_title
        else ""
    )

    new_cel = f"{title} — szablon dokumentu IT.\n\n{cel}{std_blok}{parent_note}"

    new_wej_wyj = (
        f"- **Wejścia** (co musi być dostępne przed wypełnieniem): {wej}\n"
        f"- **Wyjścia** (co dokument wytwarza jako rezultat): {wyj}"
    )

    new_zal = (
        f"- **Wpływa na** (downstream — co zależy od tego dokumentu): {wplyw}\n"
        f"- **Zależy od** (upstream — co musi istnieć przed tym dokumentem): {zalezny}"
    )

    new_sekcje = f"- {sekcje}"

    # Zamień placeholder w Cel dokumentu
    content = re.sub(
        r"(## Cel dokumentu\s*\n\n?)([^\n].*?" + re.escape(PLACEHOLDER) + r".*?\n)",
        r"\g<1>" + new_cel + "\n",
        content,
        flags=re.DOTALL,
    )

    # Zamień Wejścia i wyjścia
    content = re.sub(
        r"(## Wejścia i wyjścia\s*\n\n?)(- Wejścia:.*?\n- Wyjścia:.*?\n)",
        r"\g<1>" + new_wej_wyj + "\n",
        content,
        flags=re.DOTALL,
    )

    # Zamień Zależności dokumentu
    content = re.sub(
        r"(## Zależności dokumentu\s*\n\n?)(- Upstream:.*?\n- Downstream:.*?\n- Zewnętrzne:.*?\n)",
        r"\g<1>" + new_zal + "\n",
        content,
        flags=re.DOTALL,
    )

    # Zamień Powiązania sekcja↔sekcja
    content = re.sub(
        r"(## Powiązania sekcja↔sekcja\s*\n\n?)(- Wymagania →.*?\n- Ryzyka.*?\n\n)",
        r"\g<1>" + new_sekcje + "\n\n",
        content,
        flags=re.DOTALL,
    )

    return content


def main():
    parser = argparse.ArgumentParser(
        description="Wzbogacaj placeholder szablony o semantyczne opisy"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Pokaż co zostałoby zmienione (bez zapisu)"
    )
    parser.add_argument(
        "--limit", type=int, default=0, help="Przetwórz max N dokumentów (0=wszystkie)"
    )
    parser.add_argument("--path-filter", default="", help="Filtruj ścieżki zawierające podciąg")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT d.path, d.title,
               m.standard_code,
               s.parent_path,
               pd.title as parent_title
        FROM docs d
        LEFT JOIN doc_standard_mapping m ON d.path = m.doc_path
        LEFT JOIN doc_satellites s ON d.path = s.satellite_path
        LEFT JOIN docs pd ON pd.path = s.parent_path
        WHERE m.standard_code IS NOT NULL OR s.parent_path IS NOT NULL
        GROUP BY d.path
        ORDER BY d.path
    """).fetchall()

    processed = enriched = errors = 0

    for row in rows:
        if args.path_filter and args.path_filter not in row["path"]:
            continue

        fpath = TDIR / row["path"]
        if not fpath.exists():
            continue

        try:
            content = fpath.read_text(encoding="utf-8", errors="replace")
        except Exception:
            errors += 1
            continue

        if PLACEHOLDER not in content:
            processed += 1
            continue

        new_content = enrich_content(
            row["title"] or "", content, row["standard_code"] or "", row["parent_title"] or ""
        )

        if new_content == content:
            processed += 1
            continue

        if args.dry_run:
            print(f"  [DRY] {row['path']}")
        else:
            try:
                fpath.write_text(new_content, encoding="utf-8")
                enriched += 1
            except Exception as e:
                print(f"  [ERR] {row['path']}: {e}", file=sys.stderr)
                errors += 1

        processed += 1
        if args.limit and enriched >= args.limit:
            break

    conn.close()
    print(f"\nPrzetworzone: {processed}  |  Wzbogacone: {enriched}  |  Błędy: {errors}")


if __name__ == "__main__":
    main()
