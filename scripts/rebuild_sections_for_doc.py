#!/usr/bin/env python3
"""
Rebuild sections for a single document with diagnostics.

- Parses the markdown under generated_templates/ and rewrites sections/metrics/quality for that doc only.
- Dumps debug info to reports/latest/rebuild_sections_for_doc_debug.json.
- Robust to current working directory; discovers DB/templates relative to this file.
"""

import argparse
import json
import os
import re
import sqlite3
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

HDR_RE = re.compile(r"^(#{1,6})\s*(.+?)\s*$")  # allow '#Title' or '# Title'


# ---------- helpers ----------
def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def find_project_root() -> Path:
    """Walk upward from this script until generated_templates is found."""
    here = Path(__file__).resolve()
    for up in [
        here.parent,
        here.parent.parent,
        here.parent.parent.parent,
        here.parent.parent.parent.parent,
    ]:
        if (up / "generated_templates").exists():
            return up
    return here.parent.parent  # fallback


def find_db(root: Path) -> Path:
    """Locate it_doc_matrix.db in common locations."""
    candidates = [
        root / "reports" / "it_doc_matrix.db",
        root / "dokumentacja" / "reports" / "it_doc_matrix.db",
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError(f"Cannot find it_doc_matrix.db; tried: {candidates}")


def find_latest_dir(root: Path) -> Path:
    for d in [root / "reports" / "latest", root / "dokumentacja" / "reports" / "latest"]:
        d.mkdir(parents=True, exist_ok=True)
        return d
    d = root / "reports" / "latest"
    d.mkdir(parents=True, exist_ok=True)
    return d


def heading_norm(s: str) -> str:
    s = (s or "").strip()
    s = re.sub(r"[\U00010000-\U0010ffff]", "", s)
    s = re.sub(r"^\s*(\d+[\.\)]\s+)+", "", s)
    s = s.strip().lower()
    s = " ".join(s.split())
    return s


def slugify(s: str) -> str:
    s = heading_norm(s)
    s = re.sub(r"[^a-z0-9\s\-]", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    return s or "section"


def extract_sections(md_text: str):
    lines = md_text.splitlines()
    headers = []
    for i, line in enumerate(lines, start=1):
        m = HDR_RE.match(line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            if text:
                headers.append((i, level, text))

    sections = []
    stack = []
    ord_map = {}

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
        status = "placeholder" if ("TODO" in body or "..." in body) else "unknown"

        sections.append(
            (
                line_no,
                end,
                level,
                text,
                hn,
                anchor,
                ordinal,
                heading_path,
                status,
            )
        )
    return sections, headers, lines


# ---------- main ----------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--doc-uid",
        help="doc_uid from table docs; alternative to --path",
    )
    ap.add_argument(
        "--path",
        help="relative path under generated_templates/, e.g. core/incident_escalation_matrix.md",
    )
    args = ap.parse_args()

    root = find_project_root()
    workspace_root = root.parent
    original_cwd = Path.cwd()

    # Re-exec from workspace_root if we weren't started there (sandbox writes may be limited to start cwd).
    if original_cwd.resolve() != workspace_root.resolve():
        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve())] + sys.argv[1:],
            cwd=str(workspace_root),
        )
        sys.exit(result.returncode)

    # Ensure cwd is the workspace root (already enforced by re-exec above).
    os.chdir(workspace_root)
    dbg = {
        "ran_at_utc": utc_now_iso(),
        "project_root": str(root),
        "workspace_root": str(workspace_root),
        "cwd": os.getcwd(),
    }
    db_path = find_db(root)
    templates_root = root / "generated_templates"
    latest_dir = find_latest_dir(root)
    debug_out = latest_dir / "rebuild_sections_for_doc_debug.json"

    dbg.update(
        {
            "db_path": str(db_path),
            "templates_root": str(templates_root),
            "args": {"doc_uid": args.doc_uid, "path": args.path},
        }
    )

    try:
        conn = sqlite3.connect(str(db_path), timeout=30, isolation_level=None)
        dbg["db_connect_ok"] = True
        conn.execute("PRAGMA journal_mode = DELETE")
        conn.execute("PRAGMA foreign_keys = ON")
        cur = conn.cursor()

        # Resolve doc
        if args.doc_uid:
            cur.execute("SELECT doc_uid, path, title FROM docs WHERE doc_uid=?", (args.doc_uid,))
        elif args.path:
            cur.execute("SELECT doc_uid, path, title FROM docs WHERE path=?", (args.path,))
        else:
            cur.execute(
                "SELECT doc_uid, path, title FROM docs WHERE path=?",
                ("core/incident_escalation_matrix.md",),
            )

        row = cur.fetchone()
        if not row:
            dbg["error"] = "Doc not found in docs for given identifier"
            debug_out.write_text(
                json.dumps(dbg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
            raise SystemExit("Doc not found in docs")

        doc_uid, rel_path, title = row
        dbg["doc_uid"] = doc_uid
        dbg["doc_title"] = title
        dbg["doc_path_in_db"] = rel_path

        fp = templates_root / rel_path
        dbg["file_abs_path"] = str(fp)
        dbg["file_exists"] = fp.exists()

        if not fp.exists():
            debug_out.write_text(
                json.dumps(dbg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
            raise SystemExit(f"File not found: {fp}")

        md_text = fp.read_text(encoding="utf-8")
        sections, headers, lines = extract_sections(md_text)
        dbg["line_count"] = len(lines)
        dbg["header_count"] = len(headers)
        dbg["header_examples"] = headers[:12]
        dbg["first_20_lines"] = lines[:20]
        dbg["sections_to_insert"] = len(sections)

        now = utc_now_iso()

        conn.execute("BEGIN IMMEDIATE")
        dbg["begin_immediate_ok"] = True

        cur.execute("DELETE FROM section_metrics WHERE doc_uid=?", (doc_uid,))
        cur.execute("DELETE FROM section_quality WHERE doc_uid=?", (doc_uid,))
        cur.execute("DELETE FROM sections WHERE doc_uid=?", (doc_uid,))

        inserted = 0
        for sl, el, lvl, ht, hn, anch, ordn, hpath, st in sections:
            section_uid = uuid.uuid4().hex
            cur.execute(
                """
                INSERT INTO sections(section_uid,doc_uid,heading_text,heading_norm,heading_level,heading_path,anchor,ordinal,status,text_fingerprint_sha256,start_line,end_line)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    section_uid,
                    doc_uid,
                    ht,
                    hn,
                    lvl,
                    hpath,
                    anch,
                    ordn,
                    st,
                    None,
                    sl,
                    el,
                ),
            )
            inserted += 1

        cur.execute(
            "INSERT INTO sync_runs(sync_id,ran_at_utc,kind,status,notes) VALUES(?,?,?,?,?)",
            (
                uuid.uuid4().hex,
                now,
                "sections_meta_doc_rebuild",
                "OK",
                f"doc_uid={doc_uid}, inserted={inserted}, path={rel_path}",
            ),
        )

        conn.commit()
        conn.close()

        dbg["inserted"] = inserted
        debug_out.write_text(json.dumps(dbg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"OK: inserted={inserted}, debug={debug_out}")
    except Exception as exc:  # catch-all to persist debug info
        dbg["exception"] = repr(exc)
        debug_out.write_text(json.dumps(dbg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        raise


if __name__ == "__main__":
    main()
