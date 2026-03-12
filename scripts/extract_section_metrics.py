#!/usr/bin/env python3
"""Extract lightweight quality metrics per section/document (deterministic).
- No content is written back to DB; only counts and statuses.
- Designed to run after: build_file_index -> sync_docs_ids -> extract_sections -> materialize_edges -> resolve_content_links.
"""
import logging
import re
import sqlite3
from pathlib import Path
from datetime import datetime, timezone
from ulid import ulid

from itdoc._batch import batch_continue

_log = logging.getLogger(__name__)

MASTER_DB = Path(__file__).resolve().parent.parent / "reports" / "it_doc_matrix.db"
TEMPLATES_ROOT = Path(__file__).resolve().parent.parent / "generated_templates"

CHECKBOX_RE = re.compile(r"^\s*[-*]\s*\[\s*[xX ]\s*\]\s+")
BULLET_RE = re.compile(r"^\s*[-*]\s+")
TABLE_RE = re.compile(r"^\s*\|.+\|\s*$")
LINK_LIKE_RE = re.compile(r"\[[^\]]+\]\([^)]+\)|https?://\S+")
PHASE_BULLET_RE = re.compile(r"^\s*[-*]\s*Faza\s+(\d{1,2})\s*:", re.IGNORECASE)

# Core required headings (heading_norm, diacritics kept)
CORE_REQUIRED = [
    "metadane",
    "cel dokumentu",
    "fazy cyklu życia",
    "szybkie powiązania",
    "checklisty jakości",
    "jak używać dokumentu",
]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fetch_profiles(cur):
    cur.execute(
        "SELECT profile, max_placeholder_ratio, min_sections, min_checkboxes, "
        "require_phases, min_phase_bullets, require_quick_links FROM quality_profile"
    )
    profiles = {}
    for row in cur.fetchall():
        profiles[row[0]] = {
            "max_placeholder_ratio": float(row[1]),
            "min_sections": int(row[2]),
            "min_checkboxes": int(row[3]),
            "require_phases": int(row[4]),
            "min_phase_bullets": int(row[5]),
            "require_quick_links": int(row[6]),
        }
    return profiles


def profile_for_origin(origin: str) -> str:
    if origin == "core":
        return "core"
    if origin == "imported_template":
        return "imported_template"
    return "default"


def score_and_status(profile, sections_count, placeholder_sections, missing_required, checkbox_count, phase_bullets, req_links_missing_rationale, unresolved_content_links):
    score = 100
    if sections_count < profile["min_sections"]:
        score -= 20
    ratio = (placeholder_sections / sections_count) if sections_count else 1.0
    if ratio > profile["max_placeholder_ratio"]:
        score -= 25
    if missing_required > 0:
        score -= 30
    if checkbox_count < profile["min_checkboxes"]:
        score -= 10
    if profile["require_phases"] and phase_bullets < profile["min_phase_bullets"]:
        score -= 20
    if req_links_missing_rationale > 0:
        score -= 10
    if unresolved_content_links > 0:
        score -= 5
    if score < 0:
        score = 0

    if missing_required > 0 or sections_count < profile["min_sections"]:
        return score, "needs_structure"
    if ratio > profile["max_placeholder_ratio"] or checkbox_count < profile["min_checkboxes"]:
        return score, "needs_content"
    if req_links_missing_rationale > 0:
        return score, "needs_links"
    return score, "ok"


def main():
    assert MASTER_DB.exists(), f"Missing DB: {MASTER_DB}"
    assert TEMPLATES_ROOT.exists(), f"Missing templates root: {TEMPLATES_ROOT}"

    conn = sqlite3.connect(str(MASTER_DB))
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    profiles = fetch_profiles(cur)
    now = utc_now_iso()

    # sections grouped by doc
    cur.execute("SELECT section_uid, doc_uid, start_line, end_line, status, heading_norm FROM sections")
    by_doc = {}
    for su, du, sl, el, st, hn in cur.fetchall():
        by_doc.setdefault(du, []).append((su, int(sl or 0), int(el or 0), st, hn))

    # docs with paths
    cur.execute("SELECT doc_uid, path, origin FROM docs WHERE path IS NOT NULL")
    docs = cur.fetchall()

    # required links missing rationale per doc
    cur.execute(
        "SELECT from_uid, COUNT(*) FROM edges "
        "WHERE from_kind='doc' AND strength='required' AND (rationale IS NULL OR TRIM(rationale)='') "
        "GROUP BY from_uid"
    )
    req_missing = {du: int(c) for du, c in cur.fetchall()}

    # unresolved content links (global gap)
    cur.execute("SELECT COUNT(*) FROM content_links_resolved")
    resolved_count = int(cur.fetchone()[0])
    cur.execute("SELECT COUNT(*) FROM content_links")
    total_content = int(cur.fetchone()[0])
    unresolved_global = max(0, total_content - resolved_count)

    conn.execute("BEGIN IMMEDIATE")
    cur.execute("DELETE FROM section_metrics")
    cur.execute("DELETE FROM doc_quality")

    section_rows = 0
    doc_rows = 0

    for doc_uid, rel_path, origin in docs:
        fp = TEMPLATES_ROOT / rel_path
        if not fp.exists():
            continue
        lines = fp.read_text(encoding="utf-8", errors="replace").splitlines()

        secs = by_doc.get(doc_uid, [])
        sections_count = len(secs)
        placeholder_sections = 0
        checkbox_total = 0
        phase_total = 0

        present_hn = [hn for (_su, _sl, _el, _st, hn) in secs if hn]
        prof_name = profile_for_origin(origin)
        prof = profiles.get(prof_name, profiles["default"])
        if prof_name == "core":
            missing_required = 0
            for req in CORE_REQUIRED:
                if not any(hn.startswith(req) for hn in present_hn):
                    missing_required += 1
        else:
            missing_required = 0

        for su, sl, el, st, hn in secs:
            sl = max(1, sl)
            el = min(len(lines), el) if el else len(lines)
            body_lines = lines[sl - 1 : el]

            chars = sum(len(l) for l in body_lines)
            ln = len(body_lines)
            cb = sum(1 for l in body_lines if CHECKBOX_RE.match(l))
            bl = sum(1 for l in body_lines if BULLET_RE.match(l))
            tb = sum(1 for l in body_lines if TABLE_RE.match(l))
            lk = sum(1 for l in body_lines if LINK_LIKE_RE.search(l))
            ph = sum(1 for l in body_lines if PHASE_BULLET_RE.match(l))

            checkbox_total += cb
            phase_total += ph
            if st == "placeholder":
                placeholder_sections += 1

            cur.execute(
                """
                INSERT INTO section_metrics(
                  section_uid, doc_uid, chars, lines, checkbox_count, bullet_count,
                  table_like_lines, link_like_count, phase_bullet_count, last_scan_at_utc
                ) VALUES (?,?,?,?,?,?,?,?,?,?)
                """,
                (su, doc_uid, chars, ln, cb, bl, tb, lk, ph, now),
            )
            section_rows += 1

        score, status = score_and_status(
            prof,
            sections_count=sections_count,
            placeholder_sections=placeholder_sections,
            missing_required=missing_required,
            checkbox_count=checkbox_total,
            phase_bullets=phase_total,
            req_links_missing_rationale=req_missing.get(doc_uid, 0),
            unresolved_content_links=unresolved_global,
        )

        cur.execute(
            """
            INSERT INTO doc_quality(
              doc_uid, origin, sections_count, placeholder_sections, missing_required_sections,
              checkbox_count, phase_bullets, required_links_missing_rationale, unresolved_content_links,
              status, score, last_scan_at_utc, notes
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                doc_uid,
                origin,
                sections_count,
                placeholder_sections,
                missing_required,
                checkbox_total,
                phase_total,
                req_missing.get(doc_uid, 0),
                unresolved_global,
                status,
                score,
                now,
                None,
            ),
        )
        doc_rows += 1

    with batch_continue("sync_run telemetry", logger=_log):
        cur.execute(
            "INSERT INTO sync_runs(sync_id, ran_at_utc, kind, status, notes) VALUES(?,?,?,?,?)",
            (ulid(), now, "quality", "OK", f"docs={doc_rows}, sections={section_rows}"),
        )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
