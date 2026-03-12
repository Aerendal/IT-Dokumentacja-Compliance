#!/usr/bin/env python3
"""Krok 2: Re-indeks tabeli sections.

Parsuje wszystkie pliki .md w generated_templates/ i dostawia brakujace wiersze
do tabeli sections. Nie usuwa istniejacych — INSERT OR IGNORE zachowuje dane.

Generuje section_uid jako SHA256 (doc_uid + heading_text + ordinal) truncowany do 26 znaków.
Uzywa tej samej logiki anchor co oryginalne seedy (lowercase + strip non-ASCII + spaces→dash).
"""

import hashlib
import re
import sqlite3
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DOC_DIR = SCRIPT_DIR.parent
DB_PATH = DOC_DIR / "reports" / "it_doc_matrix.db"
TPL_DIR = DOC_DIR / "generated_templates"


def to_anchor(heading: str) -> str:
    """Identyczna logika jak oryginalne generowanie anchorow w sections."""
    s = heading.lower().strip()
    # Faza headings maja specjalny format: 'Faza N: ...' -> 'phase-0N'
    m = re.match(r"^faza\s+(\d+)\s*:", s)
    if m:
        n = int(m.group(1))
        return f"phase-{n:02d}"
    # Standardowy: strip non-ASCII, remove non-alnum/space/dash, spaces->dash
    s = s.encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def make_section_uid(doc_uid: str, heading_text: str, ordinal: int) -> str:
    """Pseudo-UID deterministyczny z doc_uid + heading + ordinal."""
    raw = f"{doc_uid}|{heading_text}|{ordinal}"
    return hashlib.sha256(raw.encode()).hexdigest()[:26].upper()


def parse_headings(md_path: Path, doc_title: str) -> list[tuple]:
    """Zwraca liste (heading_text, heading_norm, heading_level, heading_path, anchor)."""
    headings = []
    try:
        content = md_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return headings

    # Szukaj pierwszego naglowka h1 w pliku jako tytul dokumentu dla sciezki
    for line in content.splitlines():
        m = re.match(r"^#{1}\s+(.+)", line)
        if m:
            m.group(1).strip()
            break

    parent_h2 = doc_title
    for line in content.splitlines():
        m = re.match(r"^(#{2,3})\s+(.+)", line)
        if m:
            level = len(m.group(1))  # 2 for ##, 3 for ###
            heading_text = m.group(2).strip()
            heading_norm = heading_text.lower().strip()
            anchor = to_anchor(heading_text)
            if not anchor:
                continue
            if level == 2:
                parent_h2 = heading_text
                heading_path = f"{doc_title} > {heading_text}"
            else:
                heading_path = f"{doc_title} > {parent_h2} > {heading_text}"
            headings.append((heading_text, heading_norm, level, heading_path, anchor))
    return headings


def main():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    cur = conn.cursor()

    # Zbuduj mape path -> doc_uid z docs
    cur.execute("SELECT doc_uid, path FROM docs")
    path_to_uid: dict[str, str] = {r[1]: r[0] for r in cur.fetchall()}
    print(f"Dokumenty w docs: {len(path_to_uid)}")

    # Pobierz istniejace sekcje (doc_uid, anchor) dla szybkiego sprawdzenia duplikatow
    cur.execute("SELECT doc_uid, anchor FROM sections")
    existing: set[tuple[str, str]] = set(cur.fetchall())
    print(f"Istniejace sekcje w sections: {len(existing)}")

    # Pobierz tytuly dokumentow do sciezek
    cur.execute("SELECT doc_uid, title FROM docs")
    uid_to_title: dict[str, str] = {r[0]: r[1] for r in cur.fetchall()}
    md_files = list(TPL_DIR.rglob("*.md"))
    print(f"Pliki .md do przeskanowania: {len(md_files)}")

    new_rows: list[tuple] = []  # (section_uid, doc_uid, heading_text, anchor, ordinal)
    skipped_no_doc = 0

    for md_path in md_files:
        # Ustal relatywna sciezke wzgledem generated_templates/
        try:
            rel = md_path.relative_to(TPL_DIR)
        except ValueError:
            continue

        # Szukaj doc_uid po sciezce
        rel_str = str(rel).replace("\\", "/")
        doc_uid = path_to_uid.get(rel_str)
        if doc_uid is None:
            skipped_no_doc += 1
            continue
        doc_title = uid_to_title.get(doc_uid, rel_str)

        headings = parse_headings(md_path, doc_title)
        for ordinal, (heading_text, heading_norm, level, heading_path, anchor) in enumerate(
            headings, start=1
        ):
            if (doc_uid, anchor) in existing:
                continue
            section_uid = make_section_uid(doc_uid, heading_text, ordinal)
            new_rows.append(
                (
                    section_uid,
                    doc_uid,
                    heading_text,
                    heading_norm,
                    level,
                    heading_path,
                    anchor,
                    ordinal,
                )
            )

    print(f"Pliki bez doc_uid: {skipped_no_doc}")
    print(f"Nowe sekcje do wstawienia: {len(new_rows)}")

    if new_rows:
        print("Wstawianie...")
        cur.executemany(
            """INSERT OR IGNORE INTO sections
               (section_uid, doc_uid, heading_text, heading_norm, heading_level, heading_path, anchor, ordinal)
               VALUES (?,?,?,?,?,?,?,?)""",
            new_rows,
        )
        conn.commit()
        cur.execute("SELECT COUNT(*) FROM sections")
        total = cur.fetchone()[0]
        print(f"sections razem po reindeksie: {total}")

        # Pokaz jakie nowe anchory pojawiły sie
        cur.execute(
            "SELECT anchor, COUNT(*) c FROM sections GROUP BY anchor ORDER BY c DESC LIMIT 20"
        )
        print("\nTop anchory po reindeksie:")
        for r in cur.fetchall():
            print(f"  {r[1]:>6}  {r[0]}")
    else:
        print("Brak nowych sekcji do dodania.")

    # Sprawdz kluczowe anchory
    print("\nKluczowe anchory:")
    for anchor in [
        "standardy-i-compliance",
        "raci-i-role",
        "zalenoci-dokumentu",
        "powizania-meta",
        "mace-zastosowanie-standardy-i-normy",
        "majace-zastosowanie-standardy-i-normy",
    ]:
        cur.execute("SELECT COUNT(*) FROM sections WHERE anchor=?", (anchor,))
        print(f"  {anchor}: {cur.fetchone()[0]}")

    conn.close()
    print("\nGotowe.")


if __name__ == "__main__":
    main()
