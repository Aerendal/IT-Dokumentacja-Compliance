#!/usr/bin/env python3
"""Materialize UID-based edges from text relations.
- doc_doc_links: doc_title -> depends_on_title (dependency_type as link_type, direction='forward')
- doc_section_links: doc -> section within same doc
- content_links: stored as raw refs if section context is ambiguous
"""

import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from ulid import ulid

MASTER_DB = Path(__file__).resolve().parent.parent / "reports" / "it_doc_matrix.db"

EMOJI_RE = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
NUM_PREFIX_RE = re.compile(r"^\s*(\d+[\.\)]\s+)+")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def norm(s: str) -> str:
    s = (s or "").strip()
    s = EMOJI_RE.sub("", s)
    s = NUM_PREFIX_RE.sub("", s)
    s = s.strip().lower()
    s = " ".join(s.split())
    return s


def strength_from_required(required: int) -> str:
    return "required" if required == 1 else "navigational"


def main():
    conn = sqlite3.connect(str(MASTER_DB))
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    # cache existing link_types
    cur.execute("SELECT code FROM link_types")
    link_types = {c for (c,) in cur.fetchall()}

    def ensure_link_type(code: str):
        nonlocal link_types
        if code not in link_types:
            cur.execute(
                "INSERT OR IGNORE INTO link_types(code, description) VALUES(?, ?)",
                (code, "auto-imported from doc_doc_links"),
            )
            link_types.add(code)

    # title_norm -> doc_uid
    cur.execute("SELECT doc_uid, title_norm FROM docs")
    doc_map = {tn: du for (du, tn) in cur.fetchall()}

    # (doc_uid, heading_norm) -> section_uid (prefer ordinal=1)
    cur.execute("SELECT section_uid, doc_uid, heading_norm, ordinal FROM sections")
    sec_map = {}
    for su, du, hn, ordn in cur.fetchall():
        key = (du, hn)
        if key not in sec_map or ordn == 1:
            sec_map[key] = su

    now = utc_now_iso()
    conn.execute("BEGIN IMMEDIATE")
    cur.execute("DELETE FROM edges")

    # doc_doc_links
    cur.execute(
        "SELECT id, doc_title, depends_on_title, dependency_type, rationale FROM doc_doc_links"
    )
    for row_id, doc_title, dep_title, dep_type, rationale in cur.fetchall():
        du = doc_map.get(norm(doc_title))
        tu = doc_map.get(norm(dep_title))
        if not du or not tu:
            continue
        lt = (dep_type or "depends_on").lower()
        ensure_link_type(lt)
        cur.execute(
            """
            INSERT INTO edges(edge_uid,from_kind,from_uid,to_kind,to_uid,link_type,direction,rationale,strength,impact_area,impact_level,source,source_row_id)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                ulid(),
                "doc",
                du,
                "doc",
                tu,
                lt,
                "forward",
                rationale,
                "navigational",
                None,
                None,
                "doc_doc_links",
                row_id,
            ),
        )

    # doc_section_links
    cur.execute(
        "SELECT id, doc_title, section_title, link_type, direction, rationale FROM doc_section_links"
    )
    for row_id, doc_title, section_title, link_type, direction, rationale in cur.fetchall():
        du = doc_map.get(norm(doc_title))
        if not du:
            continue
        su = sec_map.get((du, norm(section_title)))
        if not su:
            continue
        ensure_link_type(link_type)
        cur.execute(
            """
            INSERT INTO edges(edge_uid,from_kind,from_uid,to_kind,to_uid,link_type,direction,rationale,strength,impact_area,impact_level,source,source_row_id)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                ulid(),
                "doc",
                du,
                "section",
                su,
                link_type,
                direction,
                rationale,
                "navigational",
                None,
                None,
                "doc_section_links",
                row_id,
            ),
        )

    # content_links (raw refs retained; can be resolved later when doc context is available)
    cur.execute(
        "SELECT id, from_type, from_ref, to_type, to_ref, link_type, direction, rationale, required, source FROM content_links"
    )
    for row in cur.fetchall():
        (
            row_id,
            from_type,
            from_ref,
            to_type,
            to_ref,
            link_type,
            direction,
            rationale,
            required,
            source,
        ) = row
        strength = strength_from_required(required)
        ensure_link_type(link_type)
        cur.execute(
            """
            INSERT INTO edges(edge_uid,from_kind,from_uid,to_kind,to_uid,link_type,direction,rationale,strength,impact_area,impact_level,source,source_row_id)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                ulid(),
                "section" if from_type == "section" else "doc",
                from_ref,
                "section" if to_type == "section" else "doc",
                to_ref,
                link_type,
                direction,
                rationale,
                strength,
                None,
                None,
                "content_links",
                row_id,
            ),
        )

    cur.execute(
        "INSERT INTO sync_runs(sync_id,ran_at_utc,kind,status,notes) VALUES(?,?,?,?,?)",
        (ulid(), now, "edges", "WARN", "content_links unresolved (raw refs stored)"),
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
