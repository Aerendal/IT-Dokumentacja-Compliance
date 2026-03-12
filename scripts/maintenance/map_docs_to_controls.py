#!/usr/bin/env python3
"""
map_docs_to_controls.py — Mapuje szablony do granularnych kontroli.

Dla każdego (doc_path, standard_code) w doc_standard_mapping,
przypisz najbardziej pasujące kontrole z standard_controls
na podstawie keyword overlap między title(doc) a control_name+description.

Użycie:
  python3 map_docs_to_controls.py [--db PATH] [--apply] [--dry-run] [--standard CODE] [--min-confidence FLOAT]
"""
import argparse
import re
import sqlite3

DB_DEFAULT = "reports/it_doc_matrix.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS doc_control_mapping (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_path TEXT NOT NULL,
    standard_code TEXT NOT NULL,
    control_id TEXT NOT NULL,
    confidence REAL,
    match_reason TEXT DEFAULT 'keyword_overlap',
    UNIQUE(doc_path, standard_code, control_id)
);
"""

STOPWORDS = {
    "and", "or", "of", "the", "in", "to", "for", "a", "an", "with", "on",
    "at", "by", "from", "as", "is", "are", "be", "it", "its", "this", "that",
    "their", "other", "use", "used", "using", "within", "during", "after",
    "before", "not", "no", "any", "all", "each", "into", "via", "per",
    "information", "security",
}


def tokenize(text: str) -> frozenset:
    if not text:
        return frozenset()
    words = re.findall(r"[a-zA-Z]+", text.lower())
    return frozenset(w for w in words if w not in STOPWORDS and len(w) > 2)


def jaccard(a: frozenset, b: frozenset) -> float:
    if not a or not b:
        return 0.0
    union = a | b
    inter = a & b
    return len(inter) / len(union)


def load_doc_titles(conn):
    """Returns {doc_path: title} from docs table."""
    cur = conn.cursor()
    cur.execute("SELECT path, title FROM docs WHERE path IS NOT NULL")
    return {row[0]: row[1] for row in cur.fetchall()}


def map_docs_to_controls(db_path, apply=False, dry_run=False, standard=None,
                          min_confidence=0.05, limit=None, _conn=None):
    """Main mapping function. Pass _conn to use an existing connection (testing)."""
    _external_conn = _conn is not None
    conn = _conn if _external_conn else sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executescript(CREATE_TABLE_SQL)

    # Preload doc path → title
    doc_titles = load_doc_titles(conn)

    # Determine which standards to process
    if standard:
        standards = [standard]
    else:
        cur.execute("SELECT DISTINCT standard_code FROM standard_controls")
        standards = [r[0] for r in cur.fetchall()]

    total_inserted = 0
    total_skipped = 0

    for std_code in standards:
        cur.execute(
            "SELECT control_id, control_name, description FROM standard_controls WHERE standard_code=?",
            (std_code,),
        )
        controls = cur.fetchall()
        if not controls:
            print(f"[WARN] No controls found for standard: {std_code}")
            continue

        # Precompute control token sets
        ctrl_tokens = {
            ctrl_id: tokenize(ctrl_name + " " + (description or ""))
            for ctrl_id, ctrl_name, description in controls
        }

        # Distinct doc_paths for this standard
        cur.execute(
            "SELECT DISTINCT doc_path FROM doc_standard_mapping WHERE standard_code=?",
            (std_code,),
        )
        doc_paths = [r[0] for r in cur.fetchall()]
        if limit:
            doc_paths = doc_paths[:limit]

        print(f"[{std_code}] {len(doc_paths)} docs × {len(controls)} controls")

        for doc_path in doc_paths:
            title = doc_titles.get(doc_path)
            if not title:
                # Derive from path filename
                title = doc_path.split("/")[-1].replace(".md", "").replace("-", " ").replace("_", " ")

            doc_tokens = tokenize(title)
            if not doc_tokens:
                continue

            # Score all controls
            scores = [
                (ctrl_id, jaccard(doc_tokens, ctrl_tok))
                for ctrl_id, ctrl_tok in ctrl_tokens.items()
            ]
            # Filter by min_confidence, sort desc, top 5
            scores = [(cid, s) for cid, s in scores if s >= min_confidence]
            scores.sort(key=lambda x: x[1], reverse=True)
            top = scores[:5]

            for ctrl_id, score in top:
                if dry_run:
                    total_inserted += 1
                    continue
                try:
                    cur.execute(
                        "INSERT INTO doc_control_mapping "
                        "(doc_path, standard_code, control_id, confidence, match_reason) "
                        "VALUES (?,?,?,?,?)",
                        (doc_path, std_code, ctrl_id, round(score, 4), "keyword_overlap"),
                    )
                    total_inserted += 1
                except sqlite3.IntegrityError:
                    total_skipped += 1

    if dry_run:
        conn.rollback()
        print(f"[dry-run] Would insert: {total_inserted} rows. No changes written.")
    elif apply:
        conn.commit()
        print(f"Inserted: {total_inserted}, Skipped (already exist): {total_skipped}")
    else:
        conn.rollback()
        print(f"[simulation] Would insert: {total_inserted}  (use --apply to write)")

    if not _external_conn:
        conn.close()
    return total_inserted


def main():
    parser = argparse.ArgumentParser(description="Map docs to granular controls")
    parser.add_argument("--db", default=DB_DEFAULT)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true")
    parser.add_argument("--standard", default=None)
    parser.add_argument("--min-confidence", dest="min_confidence", type=float, default=0.05)
    parser.add_argument("--limit", type=int, default=None, help="Limit docs per standard")
    args = parser.parse_args()

    map_docs_to_controls(
        args.db,
        apply=args.apply,
        dry_run=args.dry_run,
        standard=args.standard,
        min_confidence=args.min_confidence,
        limit=args.limit,
    )


if __name__ == "__main__":
    main()
