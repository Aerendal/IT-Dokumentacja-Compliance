#!/usr/bin/env python3
"""Build graph_engine nodes and maps from docs/sections metadata only."""

from __future__ import annotations

import argparse
import json
import logging
import re
import sqlite3
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

_log = logging.getLogger(__name__)

DEFAULT_DB_ARG = "reports/it_doc_matrix.db"
PROJECT_DB = Path(__file__).resolve().parents[2] / "reports" / "it_doc_matrix.db"
DDL_PATH = Path(__file__).resolve().parent / "ddl_nodes.sql"
RUN_KIND = "build_nodes"
BATCH_SIZE = 10000
USE_STAGING_DEFAULT = True
ALLOWED_NODE_STATUS = {
    "unknown",
    "ok",
    "needs_structure",
    "needs_content",
    "needs_links",
    "blocked",
    "active",
    "inactive",
    "draft",
    "archived",
    "placeholder",
}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def new_sync_id() -> str:
    return f"ge_{uuid.uuid4().hex}"


def table_exists(cur: sqlite3.Cursor, name: str) -> bool:
    cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,))
    return cur.fetchone() is not None


def require_tables(cur: sqlite3.Cursor, required: list[str]) -> None:
    missing = [name for name in required if not table_exists(cur, name)]
    if missing:
        raise RuntimeError(f"Missing required tables: {', '.join(missing)}")


def apply_ddl(cur: sqlite3.Cursor) -> None:
    sql = DDL_PATH.read_text(encoding="utf-8")
    buffer: list[str] = []
    for line in sql.splitlines():
        buffer.append(line)
        chunk = "\n".join(buffer).strip()
        if not chunk or not sqlite3.complete_statement(chunk):
            continue
        try:
            cur.execute(chunk)
        except sqlite3.OperationalError as exc:
            if "duplicate column name" in str(exc).lower():
                buffer = []
                continue
            raise
        buffer = []


def insert_sync_run(cur: sqlite3.Cursor, status: str, notes: str, now: str) -> None:
    cur.execute(
        "INSERT INTO sync_runs(sync_id,ran_at_utc,kind,status,notes) VALUES(?,?,?,?,?)",
        (new_sync_id(), now, RUN_KIND, status, notes),
    )


def insert_sync_run_with_id(cur: sqlite3.Cursor, sync_id: str, status: str, notes: str, now: str) -> None:
    cur.execute(
        "INSERT INTO sync_runs(sync_id,ran_at_utc,kind,status,notes) VALUES(?,?,?,?,?)",
        (sync_id, now, RUN_KIND, status, notes),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build graph_engine nodes from docs and sections.")
    parser.add_argument(
        "--db",
        default=DEFAULT_DB_ARG,
        help="Path to SQLite database (default: reports/it_doc_matrix.db).",
    )
    parser.add_argument(
        "--staging",
        action=argparse.BooleanOptionalAction,
        default=USE_STAGING_DEFAULT,
        help="Use staging tables (nodes_tmp/node_map_*_tmp) then swap (default: enabled).",
    )
    parser.add_argument(
        "--limit-docs",
        type=int,
        default=0,
        help="Process only first N docs (for fast benchmark). 0 = all docs.",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=BATCH_SIZE,
        help=f"Batch size for executemany (default: {BATCH_SIZE}).",
    )
    parser.add_argument(
        "--timing",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Write timing breakdown to sync_runs.notes (default: enabled).",
    )
    return parser.parse_args()


def resolve_db_path(raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or path.exists():
        return path
    return PROJECT_DB if raw == DEFAULT_DB_ARG else path


def section_kind(heading_level: int | None) -> str:
    if heading_level is None:
        return "sec"
    return "subsec" if heading_level >= 3 else "sec"


def section_parent(doc_node_uid: str, level: int | None, stack: list[tuple[int, str]]) -> str:
    if level is None or level <= 0:
        return doc_node_uid
    while stack and stack[-1][0] >= level:
        stack.pop()
    return stack[-1][1] if stack else doc_node_uid


def normalize_status(raw_status: str | None) -> str:
    if raw_status is None:
        return "unknown"
    status = str(raw_status).strip().lower()
    if status == "filled":
        return "ok"
    return status if status in ALLOWED_NODE_STATUS else "unknown"


class Timer:
    def __init__(self) -> None:
        self.t0 = time.perf_counter()
        self.marks: list[tuple[str, float]] = []

    def mark(self, name: str) -> None:
        self.marks.append((name, time.perf_counter()))

    def summary(self) -> dict[str, float]:
        out: dict[str, float] = {}
        prev = self.t0
        for name, point in self.marks:
            out[name] = round(point - prev, 6)
            prev = point
        end = self.marks[-1][1] if self.marks else time.perf_counter()
        out["total"] = round(end - self.t0, 6)
        return out


def build_notes(
    *,
    doc_count: int,
    sec_count: int,
    subsec_count: int,
    map_docs_count: int,
    map_sections_count: int,
    skipped_missing_doc: int,
    chunk_size: int,
    staging: bool,
    limit_docs: int,
    timing: dict[str, float] | None = None,
) -> str:
    notes = (
        f"docs={doc_count}, sec={sec_count}, subsec={subsec_count}, "
        f"map_docs={map_docs_count}, map_sections={map_sections_count}, "
        f"skipped_missing_doc={skipped_missing_doc}, chunk_size={chunk_size}, "
        f"staging={staging}, limit_docs={limit_docs}"
    )
    if timing is not None:
        notes = f"{notes}, timing={json.dumps(timing, ensure_ascii=False, sort_keys=True)}"
    return notes


def create_staging_table_like(cur: sqlite3.Cursor, source_table: str, staging_table: str) -> None:
    row = cur.execute(
        "SELECT sql FROM sqlite_master WHERE type='table' AND name=?",
        (source_table,),
    ).fetchone()
    if row is None or row[0] is None:
        raise RuntimeError(f"Missing CREATE TABLE SQL for {source_table}")

    ddl = row[0].strip()
    pattern = re.compile(
        rf"^CREATE\s+TABLE\s+(IF\s+NOT\s+EXISTS\s+)?(\"?){re.escape(source_table)}\2",
        re.IGNORECASE,
    )
    replacement = f"CREATE TABLE {staging_table}"
    staging_ddl, count = pattern.subn(replacement, ddl, count=1)
    if count != 1:
        raise RuntimeError(f"Cannot rewrite CREATE TABLE for {source_table}")
    cur.execute(staging_ddl)


def recreate_nodes_objects(cur: sqlite3.Cursor) -> None:
    # Secondary indexes are not present on staging tables and must be rebuilt after swap.
    cur.execute("CREATE INDEX IF NOT EXISTS idx_nodes_kind ON nodes(node_kind)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_nodes_kind_v2 ON nodes(kind)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_nodes_doc_uid ON nodes(doc_uid)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_nodes_key_norm ON nodes(key_norm)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_nodes_status ON nodes(status)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_node_map_docs_node_uid ON node_map_docs(node_uid)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_node_map_sections_node_uid ON node_map_sections(node_uid)")

    # Nodes guard triggers are attached to the dropped old table; recreate for the swapped table.
    cur.execute(
        """
        CREATE TRIGGER IF NOT EXISTS trg_nodes_kind_guard_ins
        BEFORE INSERT ON nodes
        FOR EACH ROW
        WHEN NEW.kind IS NOT NULL AND NEW.kind NOT IN ('doc', 'sec', 'subsec', 'section')
        BEGIN
          SELECT RAISE(ABORT, 'nodes.kind invalid');
        END
        """
    )
    cur.execute(
        """
        CREATE TRIGGER IF NOT EXISTS trg_nodes_kind_guard_upd
        BEFORE UPDATE OF kind ON nodes
        FOR EACH ROW
        WHEN NEW.kind IS NOT NULL AND NEW.kind NOT IN ('doc', 'sec', 'subsec', 'section')
        BEGIN
          SELECT RAISE(ABORT, 'nodes.kind invalid');
        END
        """
    )
    cur.execute(
        """
        CREATE TRIGGER IF NOT EXISTS trg_nodes_status_guard_ins
        BEFORE INSERT ON nodes
        FOR EACH ROW
        WHEN NEW.status IS NOT NULL
          AND NEW.status NOT IN ('unknown', 'ok', 'needs_structure', 'needs_content', 'needs_links', 'blocked', 'active', 'inactive', 'draft', 'archived', 'placeholder')
        BEGIN
          SELECT RAISE(ABORT, 'nodes.status invalid');
        END
        """
    )
    cur.execute(
        """
        CREATE TRIGGER IF NOT EXISTS trg_nodes_status_guard_upd
        BEFORE UPDATE OF status ON nodes
        FOR EACH ROW
        WHEN NEW.status IS NOT NULL
          AND NEW.status NOT IN ('unknown', 'ok', 'needs_structure', 'needs_content', 'needs_links', 'blocked', 'active', 'inactive', 'draft', 'archived', 'placeholder')
        BEGIN
          SELECT RAISE(ABORT, 'nodes.status invalid');
        END
        """
    )


def flush_nodes(cur: sqlite3.Cursor, rows: list[tuple], table: str = "nodes") -> None:
    cur.executemany(  # nosec B608 -- table is a hardcoded default ("nodes"); callers pass only known table names
        f"""
        INSERT INTO {table}(
          node_uid,kind,node_kind,doc_uid,parent_node_uid,title,key_norm,title_norm,anchor,ordinal,start_line,end_line,
          metrics_json,status,source_table,created_at_utc,updated_at_utc
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        rows,
    )


def flush_doc_map(cur: sqlite3.Cursor, rows: list[tuple], table: str = "node_map_docs") -> None:
    cur.executemany(  # nosec B608 -- table is hardcoded default; no user-controlled input reaches this parameter
        f"""
        INSERT INTO {table}(doc_uid,node_uid,created_at_utc,updated_at_utc)
        VALUES(?,?,?,?)
        """,
        rows,
    )


def flush_section_map(cur: sqlite3.Cursor, rows: list[tuple], table: str = "node_map_sections") -> None:
    cur.executemany(  # nosec B608 -- table is hardcoded default; no user-controlled input reaches this parameter
        f"""
        INSERT INTO {table}(section_uid,node_uid,created_at_utc,updated_at_utc)
        VALUES(?,?,?,?)
        """,
        rows,
    )


def main() -> None:
    args = parse_args()
    chunk_size = max(1000, int(args.chunk_size))
    limit_docs = max(0, int(args.limit_docs))
    tm = Timer()
    db_path = resolve_db_path(args.db)
    now = utc_now_iso()
    sync_id = new_sync_id()
    conn = sqlite3.connect(str(db_path))
    # Staging swap drops/replaces tables, so foreign key checks are disabled for this run.
    # This script rebuilds nodes/maps end-to-end and edge mappings are refreshed separately.
    conn.execute("PRAGMA foreign_keys = OFF" if args.staging else "PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = DELETE")
    conn.execute("PRAGMA temp_store = MEMORY")
    conn.execute("PRAGMA synchronous = OFF")
    conn.execute("PRAGMA cache_size = -200000")
    cur = conn.cursor()

    try:
        conn.execute("BEGIN IMMEDIATE")
        conn.execute("PRAGMA defer_foreign_keys = ON")
        apply_ddl(cur)
        require_tables(cur, ["sync_runs", "docs", "sections", "nodes", "node_map_docs", "node_map_sections"])
        cur.execute("CREATE INDEX IF NOT EXISTS idx_sections_doc_start ON sections(doc_uid, start_line)")

        target_nodes = "nodes"
        target_map_docs = "node_map_docs"
        target_map_sections = "node_map_sections"
        if args.staging:
            cur.execute("DROP TABLE IF EXISTS nodes_tmp")
            cur.execute("DROP TABLE IF EXISTS node_map_docs_tmp")
            cur.execute("DROP TABLE IF EXISTS node_map_sections_tmp")
            create_staging_table_like(cur, "nodes", "nodes_tmp")
            create_staging_table_like(cur, "node_map_docs", "node_map_docs_tmp")
            create_staging_table_like(cur, "node_map_sections", "node_map_sections_tmp")
            target_nodes = "nodes_tmp"
            target_map_docs = "node_map_docs_tmp"
            target_map_sections = "node_map_sections_tmp"
        else:
            cur.execute("DELETE FROM node_map_sections")
            cur.execute("DELETE FROM node_map_docs")
            cur.execute("DELETE FROM nodes")

        cur.execute("SELECT doc_uid, path, origin, title_norm, title FROM docs ORDER BY doc_uid")
        docs = cur.fetchall()
        if limit_docs > 0:
            docs = docs[:limit_docs]
        tm.mark("load_docs")
        if limit_docs > 0:
            cur.execute("DROP TABLE IF EXISTS selected_docs_tmp")
            cur.execute("CREATE TEMP TABLE selected_docs_tmp(doc_uid TEXT PRIMARY KEY)")
            cur.executemany("INSERT INTO selected_docs_tmp(doc_uid) VALUES (?)", [(doc_uid,) for doc_uid, *_ in docs])
        tm.mark("prepare_doc_filter")

        doc_count = 0
        map_docs_count = 0
        doc_node_rows: list[tuple] = []
        doc_map_rows: list[tuple] = []
        for doc_uid, path, origin, title_norm, title in docs:
            metrics = json.dumps({"origin": origin, "path": path}, ensure_ascii=False)
            doc_node_rows.append(
                (
                    doc_uid,
                    "doc",
                    "doc",
                    doc_uid,
                    None,
                    title,
                    title_norm,
                    title_norm,
                    None,
                    None,
                    None,
                    None,
                    metrics,
                    "unknown",
                    "docs",
                    now,
                    now,
                )
            )
            doc_count += 1

            doc_map_rows.append((doc_uid, doc_uid, now, now))
            map_docs_count += 1

            if len(doc_node_rows) >= chunk_size:
                flush_nodes(cur, doc_node_rows, table=target_nodes)
                doc_node_rows.clear()
            if len(doc_map_rows) >= chunk_size:
                flush_doc_map(cur, doc_map_rows, table=target_map_docs)
                doc_map_rows.clear()

        if doc_node_rows:
            flush_nodes(cur, doc_node_rows, table=target_nodes)
            doc_node_rows.clear()
        if doc_map_rows:
            flush_doc_map(cur, doc_map_rows, table=target_map_docs)
            doc_map_rows.clear()
        tm.mark("insert_doc_nodes_done")

        if limit_docs > 0:
            cur.execute(
                """
                SELECT s.section_uid,s.doc_uid,s.heading_level,s.heading_text,s.heading_norm,s.anchor,s.ordinal,s.heading_path,s.start_line,s.end_line,s.status
                FROM sections s
                JOIN selected_docs_tmp d ON d.doc_uid = s.doc_uid
                ORDER BY s.doc_uid, COALESCE(s.start_line, 2147483647), COALESCE(s.heading_level, 2147483647), s.section_uid
                """
            )
        else:
            cur.execute(
                """
                SELECT section_uid,doc_uid,heading_level,heading_text,heading_norm,anchor,ordinal,heading_path,start_line,end_line,status
                FROM sections
                ORDER BY doc_uid, COALESCE(start_line, 2147483647), COALESCE(heading_level, 2147483647), section_uid
                """
            )
        tm.mark("load_sections_query")

        sec_count = 0
        subsec_count = 0
        map_sections_count = 0
        skipped_missing_doc = 0

        doc_ids = {doc_uid for doc_uid, _path, _origin, _title_norm, _title in docs}
        section_node_batch: list[tuple] = []
        section_map_batch: list[tuple] = []

        current_doc_uid: str | None = None
        stack: list[tuple[int, str]] = []

        def flush_section_batches() -> None:
            if section_node_batch:
                flush_nodes(cur, section_node_batch, table=target_nodes)
                section_node_batch.clear()
            if section_map_batch:
                flush_section_map(cur, section_map_batch, table=target_map_sections)
                section_map_batch.clear()

        for (
            section_uid,
            doc_uid,
            heading_level,
            heading_text,
            heading_norm,
            anchor,
            ordinal,
            heading_path,
            start_line,
            end_line,
            status,
        ) in cur:
            if doc_uid not in doc_ids:
                skipped_missing_doc += 1
                continue

            if doc_uid != current_doc_uid:
                current_doc_uid = doc_uid
                stack = []

            level = int(heading_level) if heading_level is not None else None
            kind = section_kind(level)
            parent_uid = section_parent(doc_uid, level, stack)
            metrics = json.dumps({"heading_path": heading_path, "heading_level": level}, ensure_ascii=False)
            normalized_status = normalize_status(status)

            section_node_batch.append(
                (
                    section_uid,
                    kind,
                    "section",
                    doc_uid,
                    parent_uid,
                    heading_text,
                    heading_norm,
                    heading_norm,
                    anchor,
                    ordinal,
                    start_line,
                    end_line,
                    metrics,
                    normalized_status,
                    "sections",
                    now,
                    now,
                )
            )
            section_map_batch.append((section_uid, section_uid, now, now))
            map_sections_count += 1

            if kind == "subsec":
                subsec_count += 1
            else:
                sec_count += 1

            if level is not None and level > 0:
                stack.append((level, section_uid))

            if len(section_node_batch) >= chunk_size or len(section_map_batch) >= chunk_size:
                flush_section_batches()

        flush_section_batches()
        tm.mark("insert_section_nodes_done")

        if args.staging:
            # Swap by drop+rename: avoids O(N) delete/insert on large target tables.
            cur.execute("DROP TABLE node_map_sections")
            cur.execute("DROP TABLE node_map_docs")
            cur.execute("DROP TABLE nodes")
            cur.execute("ALTER TABLE nodes_tmp RENAME TO nodes")
            cur.execute("ALTER TABLE node_map_docs_tmp RENAME TO node_map_docs")
            cur.execute("ALTER TABLE node_map_sections_tmp RENAME TO node_map_sections")
            recreate_nodes_objects(cur)
        tm.mark("swap_done")

        timing_data = tm.summary() if args.timing else None
        notes = build_notes(
            doc_count=doc_count,
            sec_count=sec_count,
            subsec_count=subsec_count,
            map_docs_count=map_docs_count,
            map_sections_count=map_sections_count,
            skipped_missing_doc=skipped_missing_doc,
            chunk_size=chunk_size,
            staging=bool(args.staging),
            limit_docs=limit_docs,
            timing=timing_data,
        )

        insert_sync_run_with_id(
            cur,
            sync_id=sync_id,
            status="OK",
            notes=notes,
            now=now,
        )
        tm.mark("sync_run_insert_done")
        commit_start = time.perf_counter()
        conn.commit()
        commit_elapsed = round(time.perf_counter() - commit_start, 6)
        tm.mark("commit_done")
        if args.timing:
            try:
                final_timing = tm.summary()
                final_timing["commit"] = commit_elapsed
                final_notes = build_notes(
                    doc_count=doc_count,
                    sec_count=sec_count,
                    subsec_count=subsec_count,
                    map_docs_count=map_docs_count,
                    map_sections_count=map_sections_count,
                    skipped_missing_doc=skipped_missing_doc,
                    chunk_size=chunk_size,
                    staging=bool(args.staging),
                    limit_docs=limit_docs,
                    timing=final_timing,
                )
                cur.execute("UPDATE sync_runs SET notes=? WHERE sync_id=?", (final_notes, sync_id))
                conn.commit()
            except Exception as exc:
                _log.debug("sync_runs notes update failed: %s: %s", type(exc).__name__, exc)
                conn.rollback()
    except Exception as exc:
        conn.rollback()
        try:
            conn.execute("BEGIN IMMEDIATE")
            if table_exists(cur, "sync_runs"):
                insert_sync_run(cur, status="FAIL", notes=str(exc)[:500], now=now)
                conn.commit()
        except Exception as exc:
            _log.debug("sync_runs FAIL insert failed: %s: %s", type(exc).__name__, exc)
            conn.rollback()
        raise
    finally:
        try:
            conn.execute("PRAGMA synchronous = NORMAL")
        except Exception as exc:
            _log.debug("PRAGMA synchronous reset failed: %s: %s", type(exc).__name__, exc)
        try:
            conn.execute("PRAGMA foreign_keys = ON")
        except Exception as exc:
            _log.debug("PRAGMA foreign_keys reset failed: %s: %s", type(exc).__name__, exc)
        conn.close()


if __name__ == "__main__":
    main()
