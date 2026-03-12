#!/usr/bin/env python3
"""Sync docs/docs_final_map using file_index (built from manifest).
Deterministic, DB-first, ULID IDs.
"""
from datetime import datetime, timezone
import sqlite3
from pathlib import Path

from ulid import ulid

MASTER_DB = Path(__file__).resolve().parent.parent / "reports" / "it_doc_matrix.db"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_title_norm(s: str) -> str:
    s = (s or "").strip().lower()
    s = " ".join(s.split())
    return s


def load_file_index(cur):
    cur.execute("SELECT title_norm, path, source FROM file_index WHERE title_norm IS NOT NULL")
    idx = {}
    collisions = set()
    for tn, path, source in cur.fetchall():
        if tn in idx:
            collisions.add(tn)
        else:
            idx[tn] = (path, source)
    return idx, collisions


def main():
    conn = sqlite3.connect(str(MASTER_DB))
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    idx, collisions = load_file_index(cur)
    now = utc_now_iso()

    cur.execute("SELECT id, title FROM documents_final")
    rows = cur.fetchall()

    created = ambiguous = missing = 0

    conn.execute("BEGIN IMMEDIATE")
    for doc_id, title in rows:
        tn = normalize_title_norm(title)

        if tn in collisions:
            du = ulid()
            cur.execute(
                "INSERT OR IGNORE INTO docs(doc_uid,title,title_norm,path,origin,created_at_utc,updated_at_utc) VALUES(?,?,?,?,?,?,?)",
                (du, title, tn, None, "unknown", now, now),
            )
            # ensure we reuse existing doc_uid and do not overwrite path
            cur.execute("SELECT doc_uid FROM docs WHERE title_norm=?", (tn,))
            du = cur.fetchone()[0]
            cur.execute(
                "INSERT OR REPLACE INTO docs_final_map(documents_final_id,doc_uid,match_method,match_confidence,notes) VALUES(?,?,?,?,?)",
                (doc_id, du, "ambiguous", 0.0, "title_norm collision in file_index"),
            )
            ambiguous += 1
            continue

        if tn not in idx:
            du = ulid()
            cur.execute(
                "INSERT OR IGNORE INTO docs(doc_uid,title,title_norm,path,origin,created_at_utc,updated_at_utc) VALUES(?,?,?,?,?,?,?)",
                (du, title, tn, None, "unknown", now, now),
            )
            cur.execute("SELECT doc_uid FROM docs WHERE title_norm=?", (tn,))
            du = cur.fetchone()[0]
            cur.execute(
                "INSERT OR REPLACE INTO docs_final_map(documents_final_id,doc_uid,match_method,match_confidence,notes) VALUES(?,?,?,?,?)",
                (doc_id, du, "missing", 0.0, "no match in file_index"),
            )
            missing += 1
            continue

        path, source = idx[tn]
        origin_map = {
            "core": "core",
            "imported_template": "imported_template",
            "imported_other": "imported_other",
        }
        origin = origin_map.get(source, "unknown")
        du = ulid()
        cur.execute(
            "INSERT OR IGNORE INTO docs(doc_uid,title,title_norm,path,origin,created_at_utc,updated_at_utc) VALUES(?,?,?,?,?,?,?)",
            (du, title, tn, path, origin, now, now),
        )
        # if doc already existed, refresh path/origin when they differ or are NULL
        cur.execute("SELECT doc_uid, path, origin FROM docs WHERE title_norm=?", (tn,))
        row = cur.fetchone()
        du = row[0]
        existing_path, existing_origin = row[1], row[2]
        if (existing_path or "") != path or (existing_origin or "") != origin:
            cur.execute(
                "UPDATE docs SET path=?, origin=?, updated_at_utc=? WHERE doc_uid=?",
                (path, origin, now, du),
            )
        cur.execute(
            "INSERT OR REPLACE INTO docs_final_map(documents_final_id,doc_uid,match_method,match_confidence,notes) VALUES(?,?,?,?,?)",
            (doc_id, du, "title_norm", 1.0, None),
        )
        created += 1

    cur.execute(
        "INSERT INTO sync_runs(sync_id,ran_at_utc,kind,status,notes) VALUES(?,?,?,?,?)",
        (ulid(), now, "docs", "OK", f"created={created}, ambiguous={ambiguous}, missing={missing}"),
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
