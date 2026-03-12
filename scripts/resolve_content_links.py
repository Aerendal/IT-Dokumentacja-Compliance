#!/usr/bin/env python3
"""Resolve content_links raw refs to UID where unambiguous.
- explicit format: doc::<ULID>::section::<anchor>::<ordinal?>
- global label format: section::Label
  * if context_doc_uid is set on the row, resolution is restricted to that doc
  * otherwise resolve globally (unique heading_norm/anchor or override)
Stores results in content_links_resolved; unresolved remain implicit (ambiguous/missing counters).
Adds SLA metric for manual/meta links.
"""

import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from ulid import ulid

MASTER_DB = Path(__file__).resolve().parent.parent / "reports" / "it_doc_matrix.db"
META_DOC_UID = "01KH6M5X8S920N682CBQN2ZDJC"
SLA_KIND = "manual_meta_sla"
SLA_OUT = Path(__file__).resolve().parent.parent / "reports" / "latest" / "manual_meta_sla.json"

SECTION_REF_RE = re.compile(r"^section::(.+)$", re.IGNORECASE)
EXPLICIT_RE = re.compile(r"^doc::([0-9A-Z]{26})::section::([a-z0-9\-]+)(::(\d+))?$", re.IGNORECASE)
EMOJI_RE = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
NUM_PREFIX_RE = re.compile(r"^\s*(\d+[\.\)]\s+)+")
META_PREFIX_RE = re.compile(r"^\s*meta\s*[:\-–—]\s*", re.IGNORECASE)


def utc_now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def norm_label(s: str) -> str:
    s = (s or "").strip()
    s = EMOJI_RE.sub("", s)
    s = NUM_PREFIX_RE.sub("", s)
    s = s.replace("\ufeff", "")
    s = s.lower()
    s = META_PREFIX_RE.sub("", s)
    s = " ".join(s.split())
    return s


def strength_from_required(required: int) -> str:
    return "required" if required == 1 else "navigational"


def table_exists(cur, name: str) -> bool:
    cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,))
    return cur.fetchone() is not None


def compute_manual_meta_sla(cur) -> dict:
    """
    SLA liczona deterministycznie na poziomie content_links.id:
    - total: manual + context_doc_uid = META_DOC_UID + ma przynajmniej jedno section:: w from/to
    - resolved: te same id, które mają wpis w content_links_resolved
    """
    cur.execute(
        """
        SELECT COUNT(*)
        FROM content_links
        WHERE source='manual'
          AND context_doc_uid=?
          AND (
            (from_type='section' AND from_ref LIKE 'section::%')
            OR
            (to_type='section' AND to_ref LIKE 'section::%')
          )
        """,
        (META_DOC_UID,),
    )
    total = int(cur.fetchone()[0])

    cur.execute(
        """
        SELECT COUNT(*)
        FROM content_links c
        WHERE c.source='manual'
          AND c.context_doc_uid=?
          AND (
            (c.from_type='section' AND c.from_ref LIKE 'section::%')
            OR
            (c.to_type='section' AND c.to_ref LIKE 'section::%')
          )
          AND EXISTS (
            SELECT 1 FROM content_links_resolved r
            WHERE r.content_link_id = c.id
          )
        """,
        (META_DOC_UID,),
    )
    resolved = int(cur.fetchone()[0])

    missing = max(0, total - resolved)
    return {
        "meta_doc_uid": META_DOC_UID,
        "total": total,
        "resolved": resolved,
        "missing": missing,
        "ambiguous": 0,
        "pass": (total > 0 and missing == 0),
    }


def build_section_indexes(cur):
    """Build lookup maps:
    - doc_index: {doc_uid: {label_key: [section_uid, ...]}}
    - global_index: {label_key: [section_uid, ...]}

    label_key covers heading_norm, heading_norm slug (spaces -> '-') and anchor (lower).
    """

    def add(mapping, key, su):
        if not key:
            return
        mapping.setdefault(key, []).append(su)

    doc_index = {}
    global_index = {}
    cur.execute("SELECT section_uid, doc_uid, heading_norm, anchor FROM sections")
    for su, du, hn, anchor in cur.fetchall():
        doc_bucket = doc_index.setdefault(du, {})

        if hn:
            add(doc_bucket, hn, su)
            add(global_index, hn, su)
            slug = hn.replace(" ", "-")
            if slug != hn:
                add(doc_bucket, slug, su)
                add(global_index, slug, su)

        if anchor:
            anchor_key = anchor.lower()
            add(doc_bucket, anchor_key, su)
            add(global_index, anchor_key, su)

    return doc_index, global_index


def main():
    conn = sqlite3.connect(str(MASTER_DB))
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    # section indexes (contextual + global)
    doc_index, global_index = build_section_indexes(cur)

    # overrides
    overrides = {}
    if table_exists(cur, "section_label_overrides"):
        cur.execute("SELECT label_norm, section_uid FROM section_label_overrides")
        overrides = dict(cur.fetchall())

    now = utc_now_iso()

    conn.execute("BEGIN IMMEDIATE")
    cur.execute("DELETE FROM content_links_resolved")

    cur.execute(
        "SELECT id, from_type, from_ref, to_type, to_ref, link_type, direction, rationale, required, source, context_doc_uid "
        "FROM content_links"
    )
    rows = cur.fetchall()

    resolved = ambiguous = missing = 0

    def resolve_ref(ref: str, context_doc_uid: str | None):
        if not ref:
            return None
        ref = ref.strip()

        m = EXPLICIT_RE.match(ref)
        if m:
            doc_uid = m.group(1)
            anchor = m.group(2)
            ordn = int(m.group(4)) if m.group(4) else 1
            cur.execute(
                "SELECT section_uid FROM sections WHERE doc_uid=? AND anchor=? AND ordinal=?",
                (doc_uid, anchor, ordn),
            )
            r = cur.fetchone()
            return ("section", r[0], "explicit", 1.0) if r else ("section", None, "missing", 0.0)

        m = SECTION_REF_RE.match(ref)
        if m:
            label = norm_label(m.group(1))
            keys = [label]
            slug = label.replace(" ", "-")
            if slug != label:
                keys.append(slug)

            if label in overrides:
                return ("section", overrides[label], "manual", 1.0)

            # context-first resolution
            if context_doc_uid:
                bucket = doc_index.get(context_doc_uid, {})
                cands = []
                for k in keys:
                    cands.extend(bucket.get(k, []))
                cands = list(dict.fromkeys(cands))  # de-dup preserving order
                if len(cands) == 1:
                    return ("section", cands[0], "context_doc", 0.95)
                if len(cands) > 1:
                    return ("section", None, "ambiguous", 0.0)

            # global fallback
            cands = []
            for k in keys:
                cands.extend(global_index.get(k, []))
            cands = list(dict.fromkeys(cands))
            if len(cands) == 1:
                return ("section", cands[0], "global_unique", 0.9)
            if len(cands) > 1:
                return ("section", None, "ambiguous", 0.0)
            return ("section", None, "missing", 0.0)

        return None

    for (
        cid,
        from_type,
        from_ref,
        to_type,
        to_ref,
        link_type,
        direction,
        rationale,
        required,
        _source,
        context_doc_uid,
    ) in rows:
        strength = strength_from_required(required)

        fr = resolve_ref(from_ref, context_doc_uid) if from_type == "section" else None
        tr = resolve_ref(to_ref, context_doc_uid) if to_type == "section" else None

        if fr and tr and fr[1] and tr[1]:
            method = fr[2] if fr[2] == tr[2] else "mixed"
            conf = min(fr[3], tr[3])
            cur.execute(
                """
                INSERT INTO content_links_resolved(
                  content_link_id, from_kind, from_uid, to_kind, to_uid,
                  link_type, direction, rationale, strength,
                  resolution_method, resolution_confidence, notes
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    cid,
                    "section",
                    fr[1],
                    "section",
                    tr[1],
                    link_type,
                    direction,
                    rationale,
                    strength,
                    method
                    if method in ("explicit", "global_unique", "manual", "context_doc")
                    else "mixed",
                    conf,
                    context_doc_uid if method == "context_doc" else None,
                ),
            )
            resolved += 1
        else:
            if (fr and fr[2] == "ambiguous") or (tr and tr[2] == "ambiguous"):
                ambiguous += 1
            else:
                missing += 1

    cur.execute(
        "INSERT INTO sync_runs(sync_id,ran_at_utc,kind,status,notes) VALUES(?,?,?,?,?)",
        (
            ulid(),
            now,
            "content_links_resolved",
            "OK",
            f"resolved={resolved}, ambiguous={ambiguous}, missing={missing}",
        ),
    )

    # SLA for manual/meta links
    sla = compute_manual_meta_sla(cur)
    SLA_OUT.parent.mkdir(parents=True, exist_ok=True)
    SLA_OUT.write_text(json.dumps(sla, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sla_status = "OK" if sla["pass"] else ("WARN" if sla["resolved"] > 0 else "FAIL")
    cur.execute(
        "INSERT INTO sync_runs(sync_id,ran_at_utc,kind,status,notes) VALUES(?,?,?,?,?)",
        (
            ulid(),
            now,
            SLA_KIND,
            sla_status,
            f"meta_doc_uid={META_DOC_UID}, total={sla['total']}, resolved={sla['resolved']}, missing={sla['missing']}",
        ),
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
