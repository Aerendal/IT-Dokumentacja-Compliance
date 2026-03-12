#!/usr/bin/env python3
"""Build deterministic file_index from templates_manifest_v2.csv + file titles.
Uses title from YAML front-matter (title:) or first H1 as fallback.
Stores collisions of title_norm for audit.
"""

import csv
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from ulid import ulid

BASE = Path(__file__).resolve().parent.parent
MASTER_DB = BASE / "reports" / "it_doc_matrix.db"
TEMPLATES_ROOT = BASE / "generated_templates"
MANIFEST_V2 = BASE / "reports" / "latest" / "templates_manifest_v2.csv"

EMOJI_RE = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
NUM_PREFIX_RE = re.compile(r"^\s*(\d+[\.\)]\s+)+")  # e.g. "1. " / "1) " / "1.2. "


def utc_now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_title_norm(s: str) -> str:
    s = (s or "").strip()
    s = EMOJI_RE.sub("", s)
    s = NUM_PREFIX_RE.sub("", s)
    s = s.strip().lower()
    s = " ".join(s.split())
    return s


def infer_source(path: str) -> str:
    p = path.replace("\\", "/")
    if p.startswith("core/"):
        return "core"
    if p.startswith("imported/files(13)/templates/"):
        return "imported_template"
    if p.startswith("imported/"):
        return "imported_other"
    return "unknown"


def extract_title(text: str) -> str | None:
    # YAML front-matter first
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[3:end].splitlines()
            for ln in fm:
                if ln.strip().lower().startswith("title:"):
                    return ln.split(":", 1)[1].strip().strip('"').strip("'")
    # fallback: first H1
    for ln in text.splitlines():
        if ln.startswith("# "):
            return ln[2:].strip()
    return None


def main():
    assert MASTER_DB.exists(), f"Missing master DB: {MASTER_DB}"
    assert MANIFEST_V2.exists(), f"Missing manifest v2: {MANIFEST_V2}"
    assert TEMPLATES_ROOT.exists(), f"Missing templates root: {TEMPLATES_ROOT}"

    conn = sqlite3.connect(str(MASTER_DB))
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    now = utc_now_iso()

    # load manifest
    rows = []
    with MANIFEST_V2.open("r", encoding="utf-8", newline="") as f:
        rdr = csv.DictReader(f)
        if not rdr.fieldnames or "path" not in rdr.fieldnames:
            raise RuntimeError(f"manifest missing 'path' column: {rdr.fieldnames}")
        for r in rdr:
            path = (r.get("path") or "").strip()
            h2 = (r.get("hash_sha256_v2") or "").strip() or None
            if not path:
                continue
            rows.append((path, h2))

    conn.execute("BEGIN IMMEDIATE")
    cur.execute("DELETE FROM file_index")
    cur.execute("DELETE FROM title_norm_collisions")

    title_norm_to_paths = {}
    inserted = missing_files = missing_titles = 0

    for path, h2 in rows:
        fp = TEMPLATES_ROOT / path
        if not fp.exists():
            missing_files += 1
            continue
        txt = fp.read_text(encoding="utf-8", errors="replace")
        title = extract_title(txt)
        if not title:
            missing_titles += 1
            tn = None
        else:
            tn = normalize_title_norm(title)

        src = infer_source(path)
        cur.execute(
            "INSERT INTO file_index(path,title,title_norm,source,hash_sha256_v2) VALUES(?,?,?,?,?)",
            (path, title, tn, src, h2),
        )
        inserted += 1

        if tn:
            title_norm_to_paths.setdefault(tn, []).append((path, title, src, h2))

    coll = 0
    for tn, items in title_norm_to_paths.items():
        if len(items) > 1:
            coll += 1
            for path, title, src, h2 in items:
                cur.execute(
                    "INSERT OR IGNORE INTO title_norm_collisions(title_norm,path,title,source,hash_sha256_v2) VALUES(?,?,?,?,?)",
                    (tn, path, title, src, h2),
                )

    cur.execute(
        "INSERT INTO sync_runs(sync_id,ran_at_utc,kind,status,notes) VALUES(?,?,?,?,?)",
        (
            ulid(),
            now,
            "file_index",
            "OK",
            f"inserted={inserted}, missing_files={missing_files}, missing_titles={missing_titles}, collisions={coll}",
        ),
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
