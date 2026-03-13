#!/usr/bin/env python3
"""
gap_analysis.py — Porównuje standards_catalog z szablonami w dokumentacja/generated_templates/core/

Wynik: tabela gap_analysis w DB z polami:
  standard_code, doc_type_id, doc_title, status (present/missing), matched_doc_path, confidence

Dodatkowo: tabela extra_docs — szablony bez żadnego mapowania w doc_standard_mapping.

Matching heurystyki (w kolejności pewności):
  1. Dokładny title match (slug normalize)
  2. Fuzzy n-gram overlap > 0.6
  3. Keyword overlap (znaczące słowa)
"""

from __future__ import annotations

import argparse
import re
import sqlite3
import unicodedata
from pathlib import Path

DB_DEFAULT = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"


# ---------------------------------------------------------------------------
# Text utils
# ---------------------------------------------------------------------------


def slugify(text: str) -> str:
    """Normalizuj tytuł do slug lowercase ascii."""
    text = text.lower()
    # transliteracja PL (explicit mapping dla znaków których NFKD nie obsługuje)
    pl = str.maketrans(
        {
            "ą": "a",
            "ć": "c",
            "ę": "e",
            "ł": "l",
            "ń": "n",
            "ó": "o",
            "ś": "s",
            "ź": "z",
            "ż": "z",
        }
    )
    text = text.translate(pl)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9]+", " ", text).strip()
    return text


def tokens(text: str) -> set[str]:
    """Zwróć set tokenów (słów >=3 znaki, bez stopwords)."""
    STOP = {
        "the",
        "and",
        "for",
        "with",
        "this",
        "that",
        "from",
        "are",
        "its",
        "per",
        "plan",
        "plans",
        "doc",
        "docs",
        "document",
        "dokumentacja",
        "dokumentu",
        "system",
        "systems",
        "management",
        "zarządzanie",
        "zarządzania",
        "opis",
        "specyfikacja",
        "procedura",
        "polityka",
        "raport",
        "rejestr",
    }
    words = re.findall(r"[a-z]{3,}", slugify(text))
    return {w for w in words if w not in STOP}


def ngram_score(title_a: str, title_b: str, n: int = 2) -> float:
    """Jaccard similarity na n-gramach słownych."""

    def ngrams(t: str) -> set[tuple]:
        ws = slugify(t).split()
        return set(zip(*[ws[i:] for i in range(n)])) if len(ws) >= n else set()

    a, b = ngrams(title_a), ngrams(title_b)
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def keyword_score(title_a: str, title_b: str) -> float:
    """Jaccard na tokenach (bez stopwords)."""
    a, b = tokens(title_a), tokens(title_b)
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


CONFIDENCE_EXACT = "exact"
CONFIDENCE_HIGH = "high"  # bigram >= 0.5
CONFIDENCE_MEDIUM = "medium"  # keyword >= 0.4
CONFIDENCE_LOW = "low"  # keyword >= 0.25
CONFIDENCE_MISS = "missing"

THRESHOLD_HIGH = 0.50
THRESHOLD_MEDIUM = 0.40
THRESHOLD_LOW = 0.25


def match_catalog_entry(
    doc_title: str,
    all_docs: list[tuple[str, str]],  # (path, title)
    standard_code: str | None = None,
    mapped_docs: set[str] | None = None,  # paths already mapped to this standard
) -> tuple[str, str, str] | None:
    """
    Dopasuj wpis katalogu do szablonu w DB.
    Zwraca (doc_path, matched_title, confidence) lub None.

    Ulepszony algorytm:
    1. Exact title match (slug)
    2. Sygnał z doc_standard_mapping: jeśli doc jest już zmapowany do tego standardu
       i ma wysokie podobieństwo tytułu → preferuj go
    3. Bigram Jaccard ≥ 0.50
    4. Keyword overlap ≥ 0.40 / ≥ 0.25
    """
    slug_a = slugify(doc_title)

    best_path = None
    best_title = None
    best_conf = CONFIDENCE_MISS
    best_score = 0.0

    mapped_docs = mapped_docs or set()

    for doc_path, doc_db_title in all_docs:
        slug_b = slugify(doc_db_title)

        # 1. Exact slug match
        if slug_a == slug_b:
            return (doc_path, doc_db_title, CONFIDENCE_EXACT)

        # 2. Sygnał z doc_standard_mapping: doc już zmapowany do tego standardu
        #    → zmniejszony próg dla high confidence
        in_mapping = doc_path in mapped_docs
        mapping_boost = 0.15 if in_mapping else 0.0

        # 3. Bigram Jaccard
        bi = ngram_score(doc_title, doc_db_title, n=2)
        effective_bi = bi + mapping_boost
        if effective_bi >= THRESHOLD_HIGH and bi > best_score:
            best_score = bi
            best_path = doc_path
            best_title = doc_db_title
            best_conf = CONFIDENCE_HIGH if bi >= THRESHOLD_HIGH else CONFIDENCE_MEDIUM
            continue

        # 4. Keyword overlap
        kw = keyword_score(doc_title, doc_db_title)
        effective_kw = kw + mapping_boost
        if effective_kw >= THRESHOLD_MEDIUM and best_conf not in (
            CONFIDENCE_EXACT,
            CONFIDENCE_HIGH,
        ):
            if kw > best_score:
                best_score = kw
                best_path = doc_path
                best_title = doc_db_title
                # Upgrade medium→high when mapping confirms standard
                best_conf = (
                    CONFIDENCE_HIGH if (in_mapping and kw >= THRESHOLD_LOW) else CONFIDENCE_MEDIUM
                )
        elif effective_kw >= THRESHOLD_LOW and best_conf not in (
            CONFIDENCE_EXACT,
            CONFIDENCE_HIGH,
            CONFIDENCE_MEDIUM,
        ):
            if kw > best_score:
                best_score = kw
                best_path = doc_path
                best_title = doc_db_title
                best_conf = CONFIDENCE_LOW

    if best_path:
        return (best_path, best_title, best_conf)
    return None


# ---------------------------------------------------------------------------


def create_tables(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS gap_analysis (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            standard_code    TEXT NOT NULL,
            doc_type_id      TEXT NOT NULL,
            doc_title        TEXT NOT NULL,
            catalog_category TEXT,
            is_required      INTEGER,
            status           TEXT NOT NULL,   -- present/missing
            matched_doc_path TEXT,
            matched_doc_title TEXT,
            confidence       TEXT,
            created_at       TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_ga_standard ON gap_analysis(standard_code)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_ga_status   ON gap_analysis(status)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_ga_conf     ON gap_analysis(confidence)")
    conn.commit()


def run_gap_analysis(conn: sqlite3.Connection, verbose: bool = False) -> None:
    # Wyczyść poprzedni wynik
    conn.execute("DELETE FROM gap_analysis")
    conn.commit()

    # Pobierz wszystkie szablony (w tym nowe 9)
    all_docs: list[tuple[str, str]] = conn.execute(
        "SELECT path, title FROM docs WHERE path != 'ORPHAN' ORDER BY title"
    ).fetchall()
    print(f"Loaded {len(all_docs)} templates from DB")

    # Pobierz katalog
    catalog = conn.execute(
        "SELECT standard_code, doc_type_id, doc_title, category, is_required FROM standards_catalog ORDER BY standard_code, doc_type_id"
    ).fetchall()
    print(f"Loaded {len(catalog)} catalog entries for gap analysis\n")

    # Pobierz mapowania standard → doc_path (sygnał dla algorytmu)
    mapping_index: dict[str, set[str]] = {}  # standard_code → set of doc_paths
    for std_code, doc_path in conn.execute(
        "SELECT DISTINCT standard_code, doc_path FROM doc_standard_mapping WHERE doc_path IS NOT NULL AND doc_path != ''"
    ).fetchall():
        mapping_index.setdefault(std_code, set()).add(doc_path)

    stats = {"present": 0, "missing": 0, "by_conf": {}}

    for standard_code, doc_type_id, doc_title, category, is_required in catalog:
        mapped_for_standard = mapping_index.get(standard_code, set())
        result = match_catalog_entry(doc_title, all_docs, standard_code, mapped_for_standard)

        if result:
            doc_path, matched_title, confidence = result
            status = "present"
            stats["present"] += 1
            stats["by_conf"][confidence] = stats["by_conf"].get(confidence, 0) + 1
            if verbose:
                mark = "✅" if confidence in (CONFIDENCE_EXACT, CONFIDENCE_HIGH) else "~"
                print(
                    f"  {mark} [{standard_code}] {doc_title[:50]} → {matched_title[:50]} ({confidence})"
                )
        else:
            doc_path = None
            matched_title = None
            confidence = CONFIDENCE_MISS
            status = "missing"
            stats["missing"] += 1
            if verbose:
                print(f"  ❌ [{standard_code}] {doc_title}")

        conn.execute(
            """INSERT INTO gap_analysis
               (standard_code, doc_type_id, doc_title, catalog_category, is_required, status, matched_doc_path, matched_doc_title, confidence)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                standard_code,
                doc_type_id,
                doc_title,
                category,
                is_required,
                status,
                doc_path,
                matched_title,
                confidence,
            ),
        )

    conn.commit()

    print("\n=== Gap Analysis Results ===")
    print(f"Present (matched):  {stats['present']:4d}")
    print(f"Missing (no match): {stats['missing']:4d}")
    print("\nConfidence breakdown (present only):")
    for conf in [CONFIDENCE_EXACT, CONFIDENCE_HIGH, CONFIDENCE_MEDIUM, CONFIDENCE_LOW]:
        n = stats["by_conf"].get(conf, 0)
        print(f"  {conf:8s}: {n}")


def print_missing_report(conn: sqlite3.Connection) -> None:
    """Drukuj brakujące szablony per standard."""
    print("\n=== MISSING templates per standard ===")
    rows = conn.execute("""
        SELECT standard_code, doc_title, is_required
        FROM gap_analysis WHERE status = 'missing'
        ORDER BY standard_code, is_required DESC, doc_title
    """).fetchall()

    current = None
    for code, title, req in rows:
        if code != current:
            print(f"\n[{code}]")
            current = code
        mark = "REQ" if req else "REC"
        print(f"  [{mark}] {title}")

    # Extra docs (w DB, bez mapowania w doc_standard_mapping)
    print("\n=== EXTRA templates (not mapped to any standard in doc_standard_mapping) ===")
    extra = conn.execute("""
        SELECT d.title, d.path FROM docs d
        WHERE d.path != 'ORPHAN'
        AND NOT EXISTS (SELECT 1 FROM doc_standard_mapping m WHERE m.doc_path = d.path)
        ORDER BY d.title
    """).fetchall()
    print(f"  Count: {len(extra)}")
    for title, _path in extra:
        print(f"  {title}")


def print_standard_summary(conn: sqlite3.Connection) -> None:
    """Tabela per standard: ile present/missing/low confidence."""
    print("\n=== SUMMARY per standard ===")
    print(f"{'Standard':<45} {'Present':>8} {'Missing':>8} {'Low/Med':>8}")
    print("-" * 73)
    rows = conn.execute("""
        SELECT
            g.standard_code,
            SUM(CASE WHEN g.status='present' THEN 1 ELSE 0 END) AS present,
            SUM(CASE WHEN g.status='missing' THEN 1 ELSE 0 END) AS missing,
            SUM(CASE WHEN g.confidence IN ('low','medium') THEN 1 ELSE 0 END) AS low_med
        FROM gap_analysis g
        GROUP BY g.standard_code
        ORDER BY g.standard_code
    """).fetchall()
    for code, present, missing, low_med in rows:
        flag = " ⚠" if missing > 0 else ""
        print(f"  {code:<43} {present:>8} {missing:>8} {low_med:>8}{flag}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--db",
        default=DB_DEFAULT,
        help="Ścieżka do pliku .db (domyślnie: reports/it_doc_matrix.db)",
    )
    ap.add_argument("--verbose", "-v", action="store_true", help="Print each match/miss")
    ap.add_argument("--report", action="store_true", help="Print missing + extra report")
    ap.add_argument("--summary", action="store_true", help="Print per-standard summary table")
    ap.add_argument("--all", action="store_true", help="Run + print all reports")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    create_tables(conn)
    run_gap_analysis(conn, verbose=args.verbose)

    if args.report or args.all:
        print_missing_report(conn)
    if args.summary or args.all:
        print_standard_summary(conn)

    conn.close()
    print("✓ Analiza luk zakończona.")


if __name__ == "__main__":
    main()
