"""
Generate an audit of manual content link labels against the meta-doc sections.

The script outputs two files in reports/latest/:
- content_labels_audit.csv  (quick glance)
- content_labels_audit.json (full candidate details)
"""

import json
import re
import sqlite3
import unicodedata
from pathlib import Path

# Paths and constants
BASE_DIR = Path(__file__).resolve().parent.parent
DB = BASE_DIR / "reports/it_doc_matrix.db"
META_DOC_UID = "01KH6M5X8S920N682CBQN2ZDJC"

SECTION_REF_RE = re.compile(r"^section::(.+)$", re.IGNORECASE)
META_PREFIX_RE = re.compile(r"^\s*meta\s*[:\-–—]\s*", re.IGNORECASE)
EMOJI_RE = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
NUM_PREFIX_RE = re.compile(r"^\s*(\d+[.\)]\s+)+")


def strip_diacritics(text: str) -> str:
    """Remove diacritical marks."""
    text = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in text if not unicodedata.combining(ch))


def key_norm(text: str) -> str:
    """Normalize labels/headings to a matching key."""
    text = (text or "").strip().replace("\ufeff", "")
    text = EMOJI_RE.sub("", text)
    text = META_PREFIX_RE.sub("", text)
    text = NUM_PREFIX_RE.sub("", text)
    text = strip_diacritics(text)
    text = text.lower()
    text = " ".join(text.split())
    return text


def load_meta_sections(cur):
    """Return index: norm_key -> list of candidate tuples."""
    cur.execute(
        """
        SELECT section_uid, heading_text, heading_norm, anchor, ordinal
        FROM sections
        WHERE doc_uid=?
        ORDER BY start_line
        """,
        (META_DOC_UID,),
    )
    meta_sections = cur.fetchall()

    idx = {}
    for section_uid, heading_text, heading_norm, anchor, ordinal in meta_sections:
        norm = key_norm(heading_norm if heading_norm else heading_text)
        idx.setdefault(norm, []).append((section_uid, heading_text, anchor, ordinal))
    return idx


def collect_labels(cur):
    """Collect the 53 manual labels (from_ref/to_ref) targeting sections."""
    cur.execute(
        """
        SELECT id, from_ref, to_ref
        FROM content_links
        WHERE source='manual'
          AND context_doc_uid=?
          AND (
            (from_type='section' AND from_ref LIKE 'section::%')
            OR
            (to_type='section' AND to_ref LIKE 'section::%')
          )
        ORDER BY id
        """,
        (META_DOC_UID,),
    )
    rows = cur.fetchall()

    labels = []

    def add_label(content_id, ref_text, side):
        if not ref_text:
            return
        match = SECTION_REF_RE.match(ref_text.strip())
        if not match:
            return
        raw_label = match.group(1).strip()
        norm = key_norm(raw_label)
        labels.append((content_id, side, raw_label, norm))

    for content_id, from_ref, to_ref in rows:
        add_label(content_id, from_ref, "from")
        add_label(content_id, to_ref, "to")

    return labels


def build_report(labels, idx):
    """Return report rows: (label_norm, raw_label, status, candidates)."""
    report = []
    seen = {}
    for content_id, side, raw_label, norm in labels:
        if norm in seen:
            continue
        seen[norm] = raw_label
        candidates = idx.get(norm, [])
        if len(candidates) == 1:
            status = "unique"
        elif len(candidates) > 1:
            status = "ambiguous"
        else:
            status = "missing"
        report.append((norm, raw_label, status, candidates))
    return report


def write_outputs(report):
    out_csv = BASE_DIR / "reports/latest/content_labels_audit.csv"
    out_json = BASE_DIR / "reports/latest/content_labels_audit.json"
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        f.write(
            "label_norm,raw_label,status,candidates_count,first_section_uid,first_anchor\n"
        )
        for norm, raw, status, candidates in report:
            first = candidates[0] if candidates else ("", "", "", "")
            first_uid, _ht, first_anchor, _ord = first
            safe_raw = raw.replace(",", " ")
            f.write(
                f"{norm},{safe_raw},{status},{len(candidates)},{first_uid},{first_anchor}\n"
            )

    json_report = []
    for norm, raw, status, candidates in report:
        json_report.append(
            {
                "label_norm": norm,
                "raw_label": raw,
                "status": status,
                "candidates": [
                    {
                        "section_uid": su,
                        "heading_text": ht,
                        "anchor": anchor,
                        "ordinal": ordinal,
                    }
                    for su, ht, anchor, ordinal in candidates
                ],
            }
        )

    out_json.write_text(
        json.dumps(json_report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Wrote: {out_csv} and {out_json}")


def main():
    conn = sqlite3.connect(str(DB))
    cur = conn.cursor()

    idx = load_meta_sections(cur)
    labels = collect_labels(cur)
    report = build_report(labels, idx)
    write_outputs(report)

    conn.close()


if __name__ == "__main__":
    main()
