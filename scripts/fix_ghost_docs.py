"""scripts/fix_ghost_docs.py — naprawia ghost docs (docs z path=NULL).

Uruchamiać z katalogu dokumentacja/:
    python3 scripts/fix_ghost_docs.py [--dry-run]

Strategia dopasowania (malejący priorytet):
  1. Transliteracja PL→ASCII + strip znaków specjalnych → dokładny slug match
  2. Substring match (slug pliku zawiera poszukiwany slug lub odwrotnie)
  Nieodpasowane → path = 'ORPHAN' (nie NULL, by testy mogły je filtrować)
"""

import argparse
import re
import sqlite3
import unicodedata
from pathlib import Path

DB_PATH = Path("reports/it_doc_matrix.db")
CORE_DIR = Path("generated_templates/core")

PL_TRANS = str.maketrans(
    "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ",
    "acelnoszZACELNOSZZ",
)
# pełna mapa: lowercase + uppercase (oba kierunki)
PL_TRANS = str.maketrans(
    "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ",
    "acelnoszzACELNOSZZ",
)


def to_slug(text: str) -> str:
    """Konwertuj tytuł → slug (transliteracja PL, lowercase, snake_case)."""
    # 1. transliteracja polskich liter
    s = text.translate(PL_TRANS)
    # 2. normalizacja Unicode (reszta znaków diakrytycznych)
    s = unicodedata.normalize("NFKD", s)
    s = s.encode("ascii", "ignore").decode("ascii")
    # 3. lowercase
    s = s.lower()
    # 4. zastąp znaki niealfanumeryczne spacją
    s = re.sub(r"[^a-z0-9]+", " ", s)
    # 5. spacje → podkreślnik
    s = re.sub(r"\s+", "_", s.strip())
    s = s.strip("_")
    return s


def build_slug_map(core_dir: Path) -> dict[str, Path]:
    """Buduje mapę: slug_pliku → Path dla wszystkich .md w core/."""
    result = {}
    for f in core_dir.glob("*.md"):
        slug = to_slug(f.stem)
        result[slug] = f
    return result


def find_path(title: str, slug_map: dict[str, Path]) -> Path | None:
    """Zwraca dopasowaną ścieżkę lub None."""
    slug = to_slug(title)
    if not slug:
        return None

    # 1. dokładny match
    if slug in slug_map:
        return slug_map[slug]

    # 2. substring match: poszukiwany slug jest częścią slug pliku
    candidates = [v for k, v in slug_map.items() if slug in k]
    if len(candidates) == 1:
        return candidates[0]

    # 3. slug pliku jest częścią poszukiwanego (krótszy klucz)
    candidates = [v for k, v in slug_map.items() if k in slug and len(k) >= 8]
    if len(candidates) == 1:
        return candidates[0]

    return None


def main():
    parser = argparse.ArgumentParser(description="Napraw ghost docs (path=NULL) w DB")
    parser.add_argument("--dry-run", action="store_true", help="Tylko raport, brak zmian w DB")
    parser.add_argument("--db", default=str(DB_PATH), help="Ścieżka do DB")
    args = parser.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        print(f"BŁĄD: DB nie istnieje: {db_path}")
        return 1

    if not CORE_DIR.exists():
        print(f"BŁĄD: katalog core/ nie istnieje: {CORE_DIR}")
        return 1

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    ghost = conn.execute(
        "SELECT doc_uid, title, title_norm FROM docs WHERE path IS NULL"
    ).fetchall()

    print(f"Ghost docs (path=NULL): {len(ghost)}")
    if not ghost:
        print("Brak ghost docs — nic do naprawy.")
        conn.close()
        return 0

    slug_map = build_slug_map(CORE_DIR)
    print(f"Pliki w core/: {len(slug_map)}")
    print()

    matched = []
    orphans = []

    for g in ghost:
        path = find_path(g["title"], slug_map)
        if path:
            rel = f"core/{path.name}"
            matched.append((g["doc_uid"], g["title"], rel))
        else:
            orphans.append((g["doc_uid"], g["title"]))

    print(f"Dopasowanych: {len(matched)}/{len(ghost)}")
    print(f"Prawdziwych orphanów: {len(orphans)}/{len(ghost)}")
    print()

    if matched:
        print("=== DOPASOWANE (będą zaktualizowane) ===")
        for uid, title, rel in matched:
            print(f"  {uid}  '{title}'  →  {rel}")

    if orphans:
        print("\n=== ORPHANY (path='ORPHAN') ===")
        for uid, title in orphans:
            print(f"  {uid}  '{title}'")

    if args.dry_run:
        print("\n[dry-run] Brak zmian w DB.")
        conn.close()
        return 0

    # Zastosuj zmiany
    updated = 0
    for uid, title, rel in matched:
        conn.execute("UPDATE docs SET path = ? WHERE doc_uid = ?", (rel, uid))
        updated += 1

    for uid, title in orphans:
        conn.execute("UPDATE docs SET path = 'ORPHAN' WHERE doc_uid = ?", (uid,))
        updated += 1

    conn.commit()
    conn.close()

    print(f"\n✓ Zaktualizowano {updated} wierszy w docs")
    return 0


if __name__ == "__main__":
    exit(main())
