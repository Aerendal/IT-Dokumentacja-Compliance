#!/usr/bin/env python3
"""Extract headings from markdown into sections table (ULID-based).
Rebuilds sections table from current docs with paths.
"""
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict

# ensure local scripts (including ulid.py) are importable
import sys
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

try:
    from ulid import ulid
except Exception:  # fallback if ulid module missing
    import uuid
    def ulid():
        return uuid.uuid4().hex

BASE = Path(__file__).resolve().parent.parent
MASTER_DB = BASE / "reports" / "it_doc_matrix.db"
TEMPLATES_ROOT = BASE / "generated_templates"

EMOJI_RE = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
NUM_PREFIX_RE = re.compile(r"^\s*(\d+[\.\)]\s+)+")  # e.g., "1. " / "1) "
PHASE_BULLET_RE = re.compile(r"^\s*[-*]\s*Faza\s+(\d{1,2})\s*:\s*(.+?)\s*$", re.IGNORECASE)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def heading_norm(s: str) -> str:
    s = (s or "").strip()
    s = EMOJI_RE.sub("", s)
    s = NUM_PREFIX_RE.sub("", s)
    s = s.strip().lower()
    s = " ".join(s.split())
    return s


def slugify(s: str) -> str:
    s = heading_norm(s)
    s = re.sub(r"[^a-z0-9\s\-]", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    return s or "section"


def detect_placeholder(text: str) -> str:
    t = (text or "").strip()
    if not t:
        return "placeholder"
    low = t.lower()
    if "..." in t or "todo" in low or "tbd" in low:
        return "placeholder"
    return "filled"


def extract_phase_bullets(lines, start_line: int, end_line: int):
    """Find bullet lines 'Faza N: ...' between start_line..end_line (1-based inclusive)."""
    phases = []
    for i in range(start_line, min(end_line, len(lines)) + 1):
        m = PHASE_BULLET_RE.match(lines[i - 1])
        if not m:
            continue
        n = int(m.group(1))
        name = m.group(2).strip()
        # if bullet has extra description after second colon, keep only title part
        name_main = name.split(":", 1)[0].strip()
        phases.append({"line_no": i, "phase_n": n, "heading_text": f"Faza {n}: {name_main}"})
    return phases


def extract_sections_from_md(md_text: str) -> List[Dict]:
    lines = md_text.splitlines()
    headers = []
    for i, line in enumerate(lines, start=1):
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            headers.append((i, level, text))

    sections = []
    ord_map = {}
    stack = []

    for idx, (line_no, level, text) in enumerate(headers):
        end = (headers[idx + 1][0] - 1) if idx + 1 < len(headers) else len(lines)
        hn = heading_norm(text)
        anchor = slugify(text)
        ord_map[anchor] = ord_map.get(anchor, 0) + 1
        ordinal = ord_map[anchor]

        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, text))
        heading_path = " > ".join([x[1] for x in stack])

        body = "\n".join(lines[line_no:end]).strip()
        status = detect_placeholder(body)

        sections.append(
            {
                "start_line": line_no,
                "end_line": end,
                "heading_level": level,
                "heading_text": text,
                "heading_norm": hn,
                "anchor": anchor,
                "ordinal": ordinal,
                "heading_path": heading_path,
                "status": status,
            }
        )

        # Add logical sub-sections for phase bullets inside "Fazy cyklu życia"
        if hn == heading_norm("Fazy cyklu życia"):
            phase_items = extract_phase_bullets(lines, start_line=line_no, end_line=end)
            for p in phase_items:
                n = p["phase_n"]
                p_text = p["heading_text"]
                p_norm = heading_norm(p_text)
                p_anchor = f"phase-{n:02d}"
                p_ordinal = 1
                p_path = f"{heading_path} > {p_text}"
                sections.append(
                    {
                        "start_line": p["line_no"],
                        "end_line": end,
                        "heading_level": level + 1,
                        "heading_text": p_text,
                        "heading_norm": p_norm,
                        "anchor": p_anchor,
                        "ordinal": p_ordinal,
                        "heading_path": p_path,
                        "status": "placeholder",
                    }
                )
    return sections


def main():
    conn = sqlite3.connect(str(MASTER_DB))
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    cur.execute("SELECT doc_uid, path FROM docs WHERE path IS NOT NULL")
    docs = cur.fetchall()

    now = utc_now_iso()
    inserted = 0

    conn.execute("BEGIN IMMEDIATE")
    cur.execute("DELETE FROM sections")

    for doc_uid, rel_path in docs:
        rel_path = rel_path.lstrip("./")
        if rel_path.startswith("generated_templates/"):
            rel_path = rel_path[len("generated_templates/") :]
        fp = TEMPLATES_ROOT / rel_path
        if not fp.exists():
            continue
        text = fp.read_text(encoding="utf-8", errors="replace")
        secs = extract_sections_from_md(text)
        for s in secs:
            su = ulid()
            cur.execute(
                """
                INSERT INTO sections(section_uid,doc_uid,heading_text,heading_norm,heading_level,heading_path,anchor,ordinal,status,text_fingerprint_sha256,start_line,end_line)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    su,
                    doc_uid,
                    s["heading_text"],
                    s["heading_norm"],
                    s["heading_level"],
                    s["heading_path"],
                    s["anchor"],
                    s["ordinal"],
                    s["status"],
                    None,
                    s["start_line"],
                    s["end_line"],
                ),
            )
            inserted += 1

    cur.execute(
        "INSERT INTO sync_runs(sync_id,ran_at_utc,kind,status,notes) VALUES(?,?,?,?,?)",
        (ulid(), now, "sections", "OK", f"inserted={inserted}"),
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
