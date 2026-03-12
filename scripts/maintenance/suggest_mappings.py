#!/usr/bin/env python3
"""
scripts/maintenance/suggest_mappings.py

Automatyczne sugestie mapowań dla 3189 szablonów bez przypisanego standardu.

Algorytm:
  1. Dla każdego standardu buduje "profil słów" z tytułów już zmapowanych szablonów
  2. Dla każdego niezmapowanego szablonu oblicza Jaccard overlap z profilem każdego standardu
  3. Wybiera najlepiej pasujący standard (max overlap) jako sugestię
  4. Filtruje po progu pewności (--min-confidence)

Użycie:
  python3 suggest_mappings.py --analyze               # sugestie bez zapisu
  python3 suggest_mappings.py --analyze --top 20      # pokaż 20 najlepszych
  python3 suggest_mappings.py --auto-approve --min-confidence 0.40
  python3 suggest_mappings.py --report > suggestions.md
  python3 suggest_mappings.py --dry-run --min-confidence 0.35

match_reason wstawiany do DB: 'candidate_match'
"""

import argparse
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "reports" / "it_doc_matrix.db"

# Słowa stop dla języka polskiego i angielskiego
STOP_WORDS = {
    "i",
    "w",
    "z",
    "do",
    "na",
    "nie",
    "się",
    "to",
    "jest",
    "dla",
    "oraz",
    "lub",
    "przy",
    "po",
    "jak",
    "co",
    "by",
    "ale",
    "ze",
    "the",
    "a",
    "an",
    "and",
    "or",
    "of",
    "in",
    "for",
    "is",
    "with",
    "on",
    "at",
    "be",
    "as",
    "from",
    "that",
    "this",
    "it",
    "are",
    "was",
    "will",
    "can",
    "has",
    "have",
}

# Minimalna długość słowa do uwzględnienia w profilu
MIN_WORD_LEN = 3


def connect(db_path: Path = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def tokenize(text: str) -> set:
    """Tokenizuje tekst do zbioru słów kluczowych (lowercase, bez stop-words)."""
    if not text:
        return set()
    words = re.findall(r"[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+", text.lower())
    return {w for w in words if len(w) >= MIN_WORD_LEN and w not in STOP_WORDS}


def jaccard(set_a: set, set_b: set) -> float:
    """Współczynnik Jaccarda: |A∩B| / |A∪B|."""
    if not set_a or not set_b:
        return 0.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union > 0 else 0.0


def overlap_coefficient(doc_words: set, standard_words: set) -> float:
    """Overlap coefficient: |A∩B| / min(|A|,|B|) — lepszy gdy profile są różnej wielkości."""
    if not doc_words or not standard_words:
        return 0.0
    intersection = len(doc_words & standard_words)
    denom = min(len(doc_words), len(standard_words))
    return intersection / denom if denom > 0 else 0.0


def build_standard_profiles(conn: sqlite3.Connection) -> dict:
    """
    Buduje słownikowy profil słów dla każdego standardu na podstawie
    tytułów zmapowanych szablonów.
    Zwraca: {standard_code: frozenset(słów)}
    """
    cur = conn.cursor()
    cur.execute("""
        SELECT m.standard_code, d.title_norm, d.path
        FROM doc_standard_mapping m
        JOIN docs d ON d.path = m.doc_path
        WHERE d.title_norm IS NOT NULL
    """)
    profiles: dict = defaultdict(set)
    for row in cur.fetchall():
        words = tokenize(row["title_norm"])
        # Dokładamy też słowa z ścieżki pliku (bez rozszerzenia)
        path_stem = Path(row["path"]).stem if row["path"] else ""
        words |= tokenize(path_stem.replace("_", " "))
        profiles[row["standard_code"]] |= words

    return {code: frozenset(words) for code, words in profiles.items()}


def build_idf_profiles(conn: sqlite3.Connection) -> tuple:
    """
    Buduje profile TF-IDF dla każdego standardu.

    Zwraca:
      standard_profiles: {standard_code: {word: tf_score}}
      idf: {word: idf_score}  — niższe IDF = słowo mniej dyskryminujące
    """
    import math

    cur = conn.cursor()
    cur.execute("""
        SELECT m.standard_code, d.title_norm, d.path
        FROM doc_standard_mapping m
        JOIN docs d ON d.path = m.doc_path
        WHERE d.title_norm IS NOT NULL
    """)

    # Zbierz słowa per standard
    standard_word_counts: dict = defaultdict(lambda: defaultdict(int))
    for row in cur.fetchall():
        words = tokenize(row["title_norm"] or "")
        path_stem = Path(row["path"]).stem if row["path"] else ""
        words |= tokenize(path_stem.replace("_", " "))
        for w in words:
            standard_word_counts[row["standard_code"]][w] += 1

    num_standards = len(standard_word_counts)

    # Ile standardów zawiera dane słowo (document frequency)
    word_in_standards: dict = defaultdict(int)
    for code, wc in standard_word_counts.items():
        for word in wc:
            word_in_standards[word] += 1

    # IDF: słowa w wielu standardach = mało dyskryminujące
    idf = {word: math.log((1 + num_standards) / (1 + df)) for word, df in word_in_standards.items()}

    # TF-IDF profil per standard (top N najdyskryminujących słów)
    standard_profiles = {}
    for code, wc in standard_word_counts.items():
        total = sum(wc.values()) or 1
        tfidf = {word: (count / total) * idf.get(word, 0.0) for word, count in wc.items()}
        # Zachowaj tylko top 200 słów per standard dla wydajności
        top_words = sorted(tfidf.items(), key=lambda x: x[1], reverse=True)[:200]
        standard_profiles[code] = dict(top_words)

    return standard_profiles, idf


def get_unmapped_docs(conn: sqlite3.Connection) -> list:
    """Pobiera szablony bez żadnego mapowania standardu."""
    cur = conn.cursor()
    cur.execute("""
        SELECT d.path, d.title_norm, d.title
        FROM docs d
        WHERE d.path IS NOT NULL
          AND d.path NOT IN (SELECT doc_path FROM doc_standard_mapping)
        ORDER BY d.path
    """)
    return cur.fetchall()


def score_doc_against_profiles(
    doc_path: str,
    title_norm: str,
    standard_profiles: dict,
    idf: dict,
) -> list:
    """
    Oblicza score TF-IDF dla szablonu względem każdego standardu.
    Zwraca listę (standard_code, score) posortowaną malejąco.
    Score = suma TF-IDF wag pasujących słów / maksymalna możliwa suma.
    """
    doc_words = tokenize(title_norm or "")
    path_stem = Path(doc_path).stem if doc_path else ""
    doc_words |= tokenize(path_stem.replace("_", " "))

    if not doc_words:
        return []

    scores = []
    for code, profile in standard_profiles.items():
        # Suma TF-IDF dla słów które są w doc I w profilu
        match_score = sum(profile[w] for w in doc_words if w in profile)
        # Normalizacja: podziel przez max możliwy score dla tego standardu
        max_score = sum(sorted(profile.values(), reverse=True)[: len(doc_words)])
        if max_score > 0 and match_score > 0:
            normalized = match_score / max_score
            scores.append((code, round(normalized, 4)))

    return sorted(scores, key=lambda x: x[1], reverse=True)


def generate_suggestions(
    conn: sqlite3.Connection,
    min_confidence: float = 0.25,
    max_candidates: int = 3,
) -> list:
    """
    Generuje listę sugestii mapowań dla niezmapowanych szablonów.

    Zwraca listę dict:
      {doc_path, title, best_standard, confidence, alternatives: [(code, score), ...]}
    """
    standard_profiles, idf = build_idf_profiles(conn)
    unmapped = get_unmapped_docs(conn)

    suggestions = []
    for row in unmapped:
        scores = score_doc_against_profiles(row["path"], row["title_norm"], standard_profiles, idf)
        if not scores:
            continue

        best_code, best_score = scores[0]
        if best_score < min_confidence:
            continue

        suggestions.append(
            {
                "doc_path": row["path"],
                "title": row["title"] or row["title_norm"] or row["path"],
                "best_standard": best_code,
                "confidence": best_score,
                "alternatives": scores[1:max_candidates],
            }
        )

    return sorted(suggestions, key=lambda x: x["confidence"], reverse=True)


def apply_suggestions(
    conn: sqlite3.Connection,
    suggestions: list,
) -> int:
    """
    Wstawia sugestie do doc_standard_mapping z match_reason='candidate_match'.
    Zwraca liczbę wstawionych wierszy.
    """
    inserted = 0
    for s in suggestions:
        # Sprawdź czy nie istnieje już takie mapowanie
        existing = conn.execute(
            "SELECT id FROM doc_standard_mapping WHERE doc_path=? AND standard_code=?",
            (s["doc_path"], s["best_standard"]),
        ).fetchone()
        if existing:
            continue

        conn.execute(
            """INSERT INTO doc_standard_mapping (doc_path, standard_code, match_reason, confidence)
               VALUES (?, ?, 'candidate_match', ?)""",
            (s["doc_path"], s["best_standard"], s["confidence"]),
        )
        inserted += 1

    conn.commit()
    return inserted


def render_report(suggestions: list, total_unmapped: int) -> str:
    """Generuje raport Markdown z sugestiami."""
    lines = [
        "# Raport sugestii mapowań szablonów",
        "",
        f"**Niezmapowane szablony łącznie:** {total_unmapped}  ",
        f"**Szablony z sugestiami (confidence ≥ próg):** {len(suggestions)}  ",
        f"**Potencjalny wzrost pokrycia:** {len(suggestions) / total_unmapped * 100:.1f}%"
        if total_unmapped
        else "",
        "",
        "## Top 50 sugestii z najwyższą pewnością",
        "",
        "| Szablon | Sugerowany standard | Pewność | Alternatywy |",
        "|---------|--------------------|---------:|-------------|",
    ]
    for s in suggestions[:50]:
        alts = ", ".join(f"{c} ({sc:.2f})" for c, sc in s["alternatives"])
        title = s["title"][:60]
        lines.append(f"| {title} | {s['best_standard']} | {s['confidence']:.2f} | {alts} |")

    lines += [
        "",
        "## Dystrybucja sugestii wg standardu",
        "",
        "| Standard | Liczba sugestii |",
        "|----------|---------------:|",
    ]
    from collections import Counter

    by_std = Counter(s["best_standard"] for s in suggestions)
    for code, cnt in by_std.most_common(20):
        lines.append(f"| {code} | {cnt} |")

    lines += [
        "",
        "## Jak zastosować sugestie",
        "",
        "```bash",
        "# Preview (bez zapisu)",
        "python3 scripts/maintenance/suggest_mappings.py --analyze --min-confidence 0.35",
        "",
        "# Zastosuj sugestie z wysoką pewnością",
        "python3 scripts/maintenance/suggest_mappings.py --auto-approve --min-confidence 0.40",
        "```",
        "",
        "> match_reason = `candidate_match` — do późniejszej weryfikacji przez `interactive_audit.py`",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Sugestie mapowań dla niezmapowanych szablonów IT Dokumentacja"
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--analyze", action="store_true", help="Pokaż sugestie bez zapisu do DB")
    mode.add_argument(
        "--auto-approve",
        action="store_true",
        help="Zapisz sugestie do DB (match_reason=candidate_match)",
    )
    mode.add_argument("--dry-run", action="store_true", help="Jak --analyze, alias dla czytelności")
    mode.add_argument("--report", action="store_true", help="Wygeneruj raport Markdown na stdout")

    parser.add_argument(
        "--min-confidence",
        type=float,
        default=0.30,
        help="Minimalny próg pewności 0.0-1.0 (domyślnie 0.30)",
    )
    parser.add_argument("--top", type=int, default=30, help="Pokaż top N sugestii (domyślnie 30)")
    parser.add_argument("--db", metavar="PATH", default=str(DB_PATH), help="Ścieżka do bazy danych")
    parser.add_argument("--save", metavar="FILE", help="Zapisz raport Markdown do pliku")

    args = parser.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        print(f"Błąd: baza danych nie istnieje: {db_path}", file=sys.stderr)
        return 1

    conn = connect(db_path)

    # Sprawdź czy kolumna confidence istnieje w doc_standard_mapping
    cols = {row[1] for row in conn.execute("PRAGMA table_info(doc_standard_mapping)").fetchall()}
    if "confidence" not in cols:
        conn.execute("ALTER TABLE doc_standard_mapping ADD COLUMN confidence REAL")
        conn.commit()

    unmapped = get_unmapped_docs(conn)
    total_unmapped = len(unmapped)
    print(f"Niezmapowane szablony: {total_unmapped}", file=sys.stderr)

    print("Budowanie profili standardów...", file=sys.stderr)
    suggestions = generate_suggestions(conn, min_confidence=args.min_confidence)
    print(f"Sugestie (confidence ≥ {args.min_confidence}): {len(suggestions)}", file=sys.stderr)

    if args.report:
        report = render_report(suggestions, total_unmapped)
        print(report)
        if args.save:
            Path(args.save).write_text(report, encoding="utf-8")
            print(f"\nZapisano do: {args.save}", file=sys.stderr)
        conn.close()
        return 0

    if args.auto_approve:
        inserted = apply_suggestions(conn, suggestions)
        print(f"Wstawiono {inserted} nowych mapowań (candidate_match) do DB.")
        print("Użyj interactive_audit.py aby zweryfikować jakość sugestii.")
        conn.close()
        return 0

    # --analyze lub --dry-run: pokaż tabelę
    top = suggestions[: args.top]
    if not top:
        print(f"Brak sugestii powyżej progu pewności {args.min_confidence}.")
        conn.close()
        return 0

    print(f"\n{'Szablon':<55} {'Standard':<25} {'Pewność':>8}  {'Alternatywa #1'}")
    print("-" * 115)
    for s in top:
        alt = (
            f"{s['alternatives'][0][0]} ({s['alternatives'][0][1]:.2f})"
            if s["alternatives"]
            else ""
        )
        title = (s["title"] or s["doc_path"])[:54]
        print(f"{title:<55} {s['best_standard']:<25} {s['confidence']:>8.3f}  {alt}")

    print(f"\nŁącznie: {len(suggestions)} sugestii ≥ {args.min_confidence}")
    print(
        f"Aby zastosować: python3 suggest_mappings.py --auto-approve --min-confidence {args.min_confidence}"
    )

    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
