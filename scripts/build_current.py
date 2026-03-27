#!/usr/bin/env python3
"""Build (or rebuild) the documents_current table in the current-snapshot DB.

Usage
-----
  python3 scripts/build_current.py \\
      --db reports/it_doc_matrix_clean.db \\
      --templates-root generated_templates \\
      --alignment-log reports/alignment_log.csv \\
      --mode rebuild          # rebuild | incremental

Exit codes
----------
  0  success
  1  missing required inputs or build failure
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Repo root on sys.path so itdoc is importable when run as subprocess
# ---------------------------------------------------------------------------
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

# ---------------------------------------------------------------------------
# Constants / regexes
# ---------------------------------------------------------------------------
EMOJI_RE = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
NUM_PREFIX_RE = re.compile(r"^\s*(\d+[\.\)]\s+)+")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_title(s: str) -> str:
    s = (s or "").strip()
    s = EMOJI_RE.sub("", s)
    s = NUM_PREFIX_RE.sub("", s)
    return " ".join(s.strip().lower().split())


def extract_title(text: str) -> str:
    """Return title from YAML front-matter or first H1, else empty string."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for ln in text[3:end].splitlines():
                if ln.strip().lower().startswith("title:"):
                    return ln.split(":", 1)[1].strip().strip('"').strip("'")
    for ln in text.splitlines():
        if ln.startswith("# "):
            return ln[2:].strip()
    return ""


def infer_source(rel_path: str) -> str:
    """Map relative path (relative to templates_root) → source column value."""
    p = rel_path.replace("\\", "/")
    if p.startswith("core/") or p.startswith("core\\"):
        return "core"
    if p.startswith("imported/") or p.startswith("imported\\"):
        return "imported"
    return "unknown"


def hash_v1(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def hash_v2(data: bytes) -> str:
    data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------
_DDL = """
CREATE TABLE IF NOT EXISTS documents_current (
    id INTEGER PRIMARY KEY,
    path TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    title_norm TEXT NOT NULL,
    source TEXT NOT NULL CHECK(source IN ('core','imported','unknown')),
    status TEXT,
    aligned INTEGER NOT NULL DEFAULT 0 CHECK(aligned IN (0,1)),
    aligned_at_utc TEXT,
    aligned_by TEXT,
    hash_sha256 TEXT,
    hash_sha256_v2 TEXT,
    template_id TEXT,
    encoding_issue INTEGER NOT NULL DEFAULT 0 CHECK(encoding_issue IN (0,1)),
    created_at_utc TEXT NOT NULL,
    updated_at_utc TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_doc_current_path     ON documents_current(path);
CREATE INDEX IF NOT EXISTS idx_doc_current_title_n  ON documents_current(title_norm);
CREATE INDEX IF NOT EXISTS idx_doc_current_source   ON documents_current(source);
CREATE INDEX IF NOT EXISTS idx_doc_current_hash_v2  ON documents_current(hash_sha256_v2);
"""


def ensure_schema(conn: sqlite3.Connection) -> None:
    for stmt in _DDL.strip().split(";"):
        s = stmt.strip()
        if s:
            conn.execute(s)
    # auto-migrate older DBs that lack new columns
    existing_cols = {
        r[1] for r in conn.execute("PRAGMA table_info(documents_current)")
    }
    for col, typ in [("hash_sha256_v2", "TEXT"), ("template_id", "TEXT")]:
        if col not in existing_cols:
            conn.execute(f"ALTER TABLE documents_current ADD COLUMN {col} {typ}")
    conn.commit()


# ---------------------------------------------------------------------------
# Alignment log loader
# ---------------------------------------------------------------------------

def load_alignment_log(path: Path) -> dict[str, dict]:
    """Return {full_path: {aligned_rev, aligned_at, aligned_by}} from CSV."""
    result: dict[str, dict] = {}
    if not path.exists():
        return result
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            p = (row.get("path") or "").strip()
            if p:
                result[p] = {
                    "aligned_rev": row.get("aligned_rev", ""),
                    "aligned_at": row.get("aligned_at", ""),
                    "aligned_by": row.get("aligned_by", ""),
                }
    return result


# ---------------------------------------------------------------------------
# Core build logic
# ---------------------------------------------------------------------------

def scan_templates(templates_root: Path) -> list[dict]:
    """Walk templates_root and return list of file records (not yet hashed)."""
    records = []
    for md_file in sorted(templates_root.rglob("*.md")):
        rel = md_file.relative_to(templates_root)
        full_path = f"generated_templates/{rel.as_posix()}"
        source = infer_source(rel.as_posix())

        encoding_issue = 0
        try:
            raw = md_file.read_bytes()
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            try:
                text = raw.decode("latin-1")
                encoding_issue = 1
            except Exception:
                text = ""
                encoding_issue = 1

        title = extract_title(text) or rel.stem.replace("_", " ").replace("-", " ").title()
        title_norm = normalize_title(title)

        records.append(
            {
                "path": full_path,
                "title": title,
                "title_norm": title_norm,
                "source": source,
                "raw": raw,
                "encoding_issue": encoding_issue,
            }
        )
    return records


def build_current(
    db_path: Path,
    templates_root: Path,
    alignment_log_path: Path,
    mode: str,
) -> dict:
    """Run the build. Returns result dict with status and counts."""
    now = utc_now_iso()

    # --- preflight ---
    errors = []
    if not templates_root.exists():
        errors.append(f"templates_root missing: {templates_root}")
    if not alignment_log_path.exists():
        errors.append(f"alignment_log missing: {alignment_log_path}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
            print(f"  → run scripts/bootstrap_runtime.py to create missing assets", file=sys.stderr)
        return {"status": "FAIL", "errors": errors}

    alignment = load_alignment_log(alignment_log_path)
    records = scan_templates(templates_root)

    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=DELETE;")
    conn.execute("PRAGMA foreign_keys=ON;")
    conn.execute("PRAGMA busy_timeout=5000;")
    ensure_schema(conn)

    if mode == "rebuild":
        conn.execute("DELETE FROM documents_current")
        conn.commit()

    # --- upsert ---
    inserted = 0
    updated = 0
    skipped = 0

    for rec in records:
        path = rec["path"]
        raw = rec.pop("raw")
        h1 = hash_v1(raw)
        h2 = hash_v2(raw)

        al = alignment.get(path, {})
        aligned = 1 if al else 0
        aligned_at = al.get("aligned_at") or None
        aligned_by = al.get("aligned_by") or None

        existing = conn.execute(
            "SELECT id, hash_sha256_v2 FROM documents_current WHERE path=?",
            (path,),
        ).fetchone()

        if existing is None:
            conn.execute(
                """
                INSERT INTO documents_current
                    (path, title, title_norm, source, aligned, aligned_at_utc,
                     aligned_by, hash_sha256, hash_sha256_v2, encoding_issue,
                     created_at_utc, updated_at_utc)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    path, rec["title"], rec["title_norm"], rec["source"],
                    aligned, aligned_at, aligned_by,
                    h1, h2, rec["encoding_issue"], now, now,
                ),
            )
            inserted += 1
        elif mode == "incremental":
            if existing[1] != h2:
                conn.execute(
                    """
                    UPDATE documents_current SET
                        title=?, title_norm=?, source=?, aligned=?,
                        aligned_at_utc=?, aligned_by=?,
                        hash_sha256=?, hash_sha256_v2=?,
                        encoding_issue=?, updated_at_utc=?
                    WHERE path=?
                    """,
                    (
                        rec["title"], rec["title_norm"], rec["source"],
                        aligned, aligned_at, aligned_by,
                        h1, h2, rec["encoding_issue"], now, path,
                    ),
                )
                updated += 1
            else:
                skipped += 1

    conn.commit()
    conn.close()

    total = conn = None
    with sqlite3.connect(str(db_path)) as c:
        total = c.execute("SELECT COUNT(*) FROM documents_current").fetchone()[0]

    result = {
        "status": "PASS",
        "mode": mode,
        "scanned": len(records),
        "inserted": inserted,
        "updated": updated,
        "skipped": skipped,
        "documents_current_total": total,
        "aligned_in_log": len(alignment),
    }
    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build documents_current table for IT-Dokumentacja pipeline."
    )
    parser.add_argument(
        "--db",
        default="reports/it_doc_matrix_clean.db",
        help="Path to target SQLite DB (default: reports/it_doc_matrix_clean.db)",
    )
    parser.add_argument(
        "--templates-root",
        default="generated_templates",
        dest="templates_root",
        help="Root of generated_templates/ (default: generated_templates)",
    )
    parser.add_argument(
        "--alignment-log",
        default="reports/alignment_log.csv",
        dest="alignment_log",
        help="Path to alignment_log.csv (default: reports/alignment_log.csv)",
    )
    parser.add_argument(
        "--mode",
        choices=["rebuild", "incremental"],
        default="rebuild",
        help="rebuild: truncate then insert all | incremental: upsert changed only",
    )
    args = parser.parse_args()

    db_path = Path(args.db)
    templates_root = Path(args.templates_root)
    alignment_log = Path(args.alignment_log)

    print(f"build_current: mode={args.mode} db={db_path}")
    result = build_current(db_path, templates_root, alignment_log, args.mode)

    for k, v in result.items():
        print(f"  {k}: {v}")

    return 0 if result.get("status") == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
