#!/usr/bin/env python3
"""
scripts/maintenance/satellite_linker.py

Zarządzanie szablonami "satelitarnymi" — niezmapowanymi dokumentami, które
logicznie należą obok konkretnego zatwierdzonego dokumentu IT.

Koncepcja:
  Zamiast przypisywać niezamapowany szablon bezpośrednio do standardu,
  oznaczamy go jako "satelitę" istniejącego, zatwierdzonego dokumentu.
  Satelita dziedziczy kontekst standardów rodzica, ale nie jest jego kopią.

Użycie:
  python3 satellite_linker.py --suggest [--top N] [--min-score 0.3]
  python3 satellite_linker.py --link <satellite_path> <parent_path> [--note "..."]
  python3 satellite_linker.py --list [--parent <parent_path>]
  python3 satellite_linker.py --unlink <satellite_path> <parent_path>
  python3 satellite_linker.py --report

Schema w DB:
  doc_satellites(id, satellite_path, parent_path, linked_by, linked_at, note)
"""

import argparse
import sqlite3
from pathlib import Path
from typing import List, Optional

# ---------------------------------------------------------------------------
# Konfiguracja
# ---------------------------------------------------------------------------

_DB_DEFAULT = Path(__file__).resolve().parents[2] / "reports" / "it_doc_matrix.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS doc_satellites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    satellite_path TEXT NOT NULL,
    parent_path TEXT NOT NULL,
    linked_by TEXT DEFAULT 'manual',
    linked_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    note TEXT,
    UNIQUE(satellite_path, parent_path)
);
"""


# ---------------------------------------------------------------------------
# Pomocnicze
# ---------------------------------------------------------------------------

def _words(text: str) -> set:
    """Zwraca zbiór słów z tekstu (lowercase, min 3 znaki)."""
    import re
    tokens = re.findall(r"[a-ząćęłńóśźżA-ZĄĆĘŁŃÓŚŹŻ]+", text.lower())
    return {t for t in tokens if len(t) >= 3}


def similarity_score(title_a: str, title_b: str) -> float:
    """Jaccard similarity między zbiorami słów dwóch tytułów."""
    a, b = _words(title_a), _words(title_b)
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def ensure_table(conn: sqlite3.Connection) -> None:
    """Tworzy tabelę doc_satellites jeśli nie istnieje."""
    conn.executescript(CREATE_TABLE_SQL)
    conn.commit()


# ---------------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------------

def get_unmapped_docs(conn: sqlite3.Connection) -> List[dict]:
    """Zwraca dokumenty bez żadnego mapowania standardu."""
    rows = conn.execute("""
        SELECT d.path, d.title
        FROM docs d
        WHERE NOT EXISTS (
            SELECT 1 FROM doc_standard_mapping m WHERE m.doc_path = d.path
        )
        AND NOT EXISTS (
            SELECT 1 FROM doc_satellites s WHERE s.satellite_path = d.path
        )
        ORDER BY d.path
    """).fetchall()
    return [{"path": r["path"], "title": r["title"] or ""} for r in rows]


def get_approved_docs(conn: sqlite3.Connection) -> List[dict]:
    """Zwraca dokumenty z zatwierdzonymi mapowaniami (keyword_match lub manual)."""
    rows = conn.execute("""
        SELECT DISTINCT d.path, d.title, GROUP_CONCAT(m.standard_code, ', ') AS standards
        FROM docs d
        JOIN doc_standard_mapping m ON m.doc_path = d.path
        WHERE m.match_reason IN ('keyword_match', 'manual', 'section_match', 'title_match')
        GROUP BY d.path
        ORDER BY d.path
    """).fetchall()
    return [{"path": r["path"], "title": r["title"] or "", "standards": r["standards"] or ""} for r in rows]


def suggest_satellites(
    conn: sqlite3.Connection,
    top: int = 20,
    min_score: float = 0.25,
) -> List[dict]:
    """
    Dla każdego niezmapowanego dokumentu szuka najbardziej podobnego
    zatwierdzonego dokumentu (Jaccard similarity tytułów).
    Zwraca listę (satellite, parent, score) posortowaną malejąco.
    """
    unmapped = get_unmapped_docs(conn)
    approved = get_approved_docs(conn)

    if not unmapped or not approved:
        return []

    results = []
    for sat in unmapped:
        best_score = 0.0
        best_parent = None
        for par in approved:
            score = similarity_score(sat["title"], par["title"])
            if score > best_score:
                best_score = score
                best_parent = par
        if best_score >= min_score and best_parent:
            results.append({
                "satellite_path": sat["path"],
                "satellite_title": sat["title"],
                "parent_path": best_parent["path"],
                "parent_title": best_parent["title"],
                "parent_standards": best_parent["standards"],
                "score": best_score,
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top]


def link_satellite(
    conn: sqlite3.Connection,
    satellite_path: str,
    parent_path: str,
    linked_by: str = "manual",
    note: Optional[str] = None,
) -> bool:
    """
    Tworzy powiązanie satelita→rodzic.
    Zwraca True jeśli wstawiono, False jeśli już istnieje.
    """
    ensure_table(conn)
    try:
        conn.execute(
            """
            INSERT INTO doc_satellites (satellite_path, parent_path, linked_by, note)
            VALUES (?, ?, ?, ?)
            """,
            (satellite_path, parent_path, linked_by, note),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def unlink_satellite(
    conn: sqlite3.Connection,
    satellite_path: str,
    parent_path: str,
) -> bool:
    """Usuwa powiązanie satelita→rodzic. Zwraca True jeśli usunięto."""
    cur = conn.execute(
        "DELETE FROM doc_satellites WHERE satellite_path=? AND parent_path=?",
        (satellite_path, parent_path),
    )
    conn.commit()
    return cur.rowcount > 0


def list_satellites(
    conn: sqlite3.Connection,
    parent_path: Optional[str] = None,
) -> List[dict]:
    """Zwraca listę powiązań satelitarnych (opcjonalnie filtruje po rodzicu)."""
    ensure_table(conn)
    if parent_path:
        rows = conn.execute(
            """
            SELECT s.satellite_path, s.parent_path, s.linked_by, s.linked_at, s.note,
                   d.title AS satellite_title, p.title AS parent_title
            FROM doc_satellites s
            LEFT JOIN docs d ON d.path = s.satellite_path
            LEFT JOIN docs p ON p.path = s.parent_path
            WHERE s.parent_path = ?
            ORDER BY s.satellite_path
            """,
            (parent_path,),
        ).fetchall()
    else:
        rows = conn.execute(
            """
            SELECT s.satellite_path, s.parent_path, s.linked_by, s.linked_at, s.note,
                   d.title AS satellite_title, p.title AS parent_title
            FROM doc_satellites s
            LEFT JOIN docs d ON d.path = s.satellite_path
            LEFT JOIN docs p ON p.path = s.parent_path
            ORDER BY s.parent_path, s.satellite_path
            """,
        ).fetchall()
    return [dict(r) for r in rows]


def satellite_report(conn: sqlite3.Connection) -> str:
    """Generuje raport Markdown o satelitach."""
    ensure_table(conn)
    links = list_satellites(conn)
    unmapped_count = len(get_unmapped_docs(conn))
    total_satellites = len(links)

    lines = [
        "# Raport Satelitów Dokumentacyjnych\n",
        f"**Satelity zarejestrowane:** {total_satellites}",
        f"**Dokumenty nadal bez przypisania:** {unmapped_count}\n",
    ]

    if not links:
        lines.append("*Brak zarejestrowanych satelitów.*\n")
        return "\n".join(lines)

    # Grupuj po rodzicu
    by_parent: dict = {}
    for lnk in links:
        parent = lnk["parent_path"]
        by_parent.setdefault(parent, []).append(lnk)

    lines.append("## Satelity według dokumentu nadrzędnego\n")
    for parent_path, children in sorted(by_parent.items()):
        parent_title = children[0]["parent_title"] or parent_path
        lines.append(f"### `{parent_path}` — {parent_title}")
        for ch in children:
            sat_title = ch["satellite_title"] or ch["satellite_path"]
            note_str = f" *(nota: {ch['note']})*" if ch["note"] else ""
            lines.append(f"- `{ch['satellite_path']}` — {sat_title}{note_str}")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Zarządzanie szablonami satelitarnymi w bibliotece IT.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--db", default=str(_DB_DEFAULT), help="Ścieżka do pliku DB")
    sub = p.add_subparsers(dest="cmd")

    # --suggest
    s = sub.add_parser("--suggest", help="Pokaż kandydatów na satelity (bez zapisu)")
    s.add_argument("--top", type=int, default=20, help="Ile par pokazać")
    s.add_argument("--min-score", type=float, default=0.25, help="Minimalny score")

    # --link
    lk = sub.add_parser("--link", help="Zarejestruj satelitę")
    lk.add_argument("satellite_path", help="Ścieżka satelity (np. core/doc.md)")
    lk.add_argument("parent_path", help="Ścieżka dokumentu nadrzędnego")
    lk.add_argument("--note", default=None, help="Opcjonalna nota")

    # --unlink
    ul = sub.add_parser("--unlink", help="Usuń powiązanie satelita→rodzic")
    ul.add_argument("satellite_path")
    ul.add_argument("parent_path")

    # --list
    ls = sub.add_parser("--list", help="Wypisz zarejestrowane satelity")
    ls.add_argument("--parent", default=None, help="Filtruj po ścieżce rodzica")

    # --report
    sub.add_parser("--report", help="Generuj raport Markdown")

    # Obsługa starych flag-style (--suggest bez subcommand)
    p.add_argument("--suggest", action="store_true", help=argparse.SUPPRESS)
    p.add_argument("--top", type=int, default=20)
    p.add_argument("--min-score", type=float, default=0.25)
    p.add_argument("--link", nargs=2, metavar=("SATELLITE", "PARENT"), help="--link satellite_path parent_path")
    p.add_argument("--note", default=None)
    p.add_argument("--unlink", nargs=2, metavar=("SATELLITE", "PARENT"))
    p.add_argument("--list", action="store_true")
    p.add_argument("--parent", default=None)
    p.add_argument("--report", action="store_true")

    return p


def _get_conn(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    ensure_table(conn)
    return conn


def main() -> None:
    p = build_parser()
    args = p.parse_args()
    conn = _get_conn(args.db)

    if args.suggest:
        suggestions = suggest_satellites(conn, top=args.top, min_score=args.min_score)
        if not suggestions:
            print("Brak sugestii dla podanego progu.")
            return
        print(f"\n{'Satelita':<45} {'Rodzic':<45} {'Score':>6}  Standardy")
        print("-" * 120)
        for s in suggestions:
            print(
                f"{s['satellite_path']:<45} {s['parent_path']:<45} {s['score']:>6.2f}  {s['parent_standards']}"
            )
        print(f"\nŁącznie: {len(suggestions)} sugestii (min-score={args.min_score})")

    elif args.link:
        sat, par = args.link
        ok = link_satellite(conn, sat, par, linked_by="manual", note=args.note)
        if ok:
            print(f"✅ Zarejestrowano: {sat} → {par}")
        else:
            print(f"⚠️  Powiązanie już istnieje: {sat} → {par}")

    elif args.unlink:
        sat, par = args.unlink
        ok = unlink_satellite(conn, sat, par)
        if ok:
            print(f"🗑️  Usunięto powiązanie: {sat} → {par}")
        else:
            print(f"⚠️  Powiązanie nie istnieje: {sat} → {par}")

    elif args.list:
        links = list_satellites(conn, parent_path=args.parent)
        if not links:
            print("Brak zarejestrowanych satelitów.")
            return
        for lnk in links:
            note_str = f"  [{lnk['note']}]" if lnk["note"] else ""
            print(f"{lnk['satellite_path']}  →  {lnk['parent_path']}{note_str}")

    elif args.report:
        print(satellite_report(conn))

    else:
        p.print_help()


if __name__ == "__main__":
    main()
