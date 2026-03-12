#!/usr/bin/env python3
"""Migrate selected edges into graph_engine.edges_manual using node maps."""

from __future__ import annotations

import argparse
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB_ARG = "reports/it_doc_matrix.db"
PROJECT_DB = Path(__file__).resolve().parents[2] / "reports" / "it_doc_matrix.db"
DDL_PATH = Path(__file__).resolve().parent / "ddl_nodes.sql"
RUN_KIND = "migrate_edges_manual"
MIGRATION_SOURCES = ("doc_doc_links", "doc_section_links", "content_links_resolved")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def new_sync_id() -> str:
    return f"ge_{uuid.uuid4().hex}"


def new_edge_id() -> str:
    return f"gem_{uuid.uuid4().hex}"


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Migrate edges to graph_engine.edges_manual.")
    parser.add_argument(
        "--db",
        default=DEFAULT_DB_ARG,
        help="Path to SQLite database (default: reports/it_doc_matrix.db).",
    )
    return parser.parse_args()


def resolve_db_path(raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or path.exists():
        return path
    return PROJECT_DB if raw == DEFAULT_DB_ARG else path


def resolve_node_uid(
    kind: str | None,
    uid: str | None,
    doc_map: dict[str, str],
    sec_map: dict[str, str],
) -> tuple[str | None, str | None]:
    if uid is None:
        return None, "missing_uid"

    k = (kind or "").strip().lower()
    v = str(uid).strip()
    if not v:
        return None, "missing_uid"

    if k == "doc":
        return doc_map.get(v), ("missing_map" if v not in doc_map else None)
    if k == "section":
        if v.lower().startswith("section::"):
            return None, "raw_section_ref"
        return sec_map.get(v), ("missing_map" if v not in sec_map else None)
    return None, "unsupported_kind"


def main() -> None:
    args = parse_args()
    db_path = resolve_db_path(args.db)
    now = utc_now_iso()
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA temp_store = MEMORY")
    cur = conn.cursor()

    try:
        conn.execute("BEGIN IMMEDIATE")
        apply_ddl(cur)
        require_tables(cur, ["sync_runs", "nodes", "edges", "node_map_docs", "node_map_sections"])

        cur.execute("SELECT doc_uid, node_uid FROM node_map_docs")
        doc_map = {doc_uid: node_uid for doc_uid, node_uid in cur.fetchall()}
        cur.execute("SELECT section_uid, node_uid FROM node_map_sections")
        sec_map = {section_uid: node_uid for section_uid, node_uid in cur.fetchall()}

        cur.execute(
            """
            DELETE FROM edges_manual
            WHERE COALESCE(source, source_table) IN (?,?,?)
            """,
            MIGRATION_SOURCES,
        )
        deleted_previous = cur.rowcount if cur.rowcount != -1 else 0

        cur.execute("SELECT node_uid FROM nodes")
        known_nodes = {row[0] for row in cur.fetchall()}

        cur.execute(
            """
            SELECT from_kind,from_uid,to_kind,to_uid,link_type,strength,direction,rationale,source,source_row_id
            FROM edges
            WHERE source IN (?,?,?)
            """
            ,
            MIGRATION_SOURCES,
        )

        inserted = 0
        skipped = 0
        skipped_missing_nodes = 0
        skipped_raw_refs = 0
        skipped_unsupported_kind = 0
        skipped_missing_map = 0
        skipped_missing_uid = 0
        processed = 0
        for (
            from_kind,
            from_uid,
            to_kind,
            to_uid,
            link_type,
            strength,
            direction,
            rationale,
            source,
            source_row_id,
        ) in cur.fetchall():
            processed += 1

            from_node_uid, from_reason = resolve_node_uid(from_kind, from_uid, doc_map, sec_map)
            to_node_uid, to_reason = resolve_node_uid(to_kind, to_uid, doc_map, sec_map)

            reasons = [r for r in (from_reason, to_reason) if r is not None]
            if reasons:
                skipped += 1
                if "raw_section_ref" in reasons:
                    skipped_raw_refs += 1
                elif "unsupported_kind" in reasons:
                    skipped_unsupported_kind += 1
                elif "missing_uid" in reasons:
                    skipped_missing_uid += 1
                else:
                    skipped_missing_map += 1
                continue

            if from_node_uid not in known_nodes or to_node_uid not in known_nodes:
                skipped += 1
                skipped_missing_nodes += 1
                continue

            edge_id = new_edge_id()
            cur.execute(
                """
                INSERT INTO edges_manual(
                  edge_uid,edge_manual_id,from_node_uid,to_node_uid,link_type,direction,strength,
                  rationale,impact_area,impact_level,source,source_table,source_row_id,created_at_utc,updated_at_utc
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    edge_id,
                    edge_id,
                    from_node_uid,
                    to_node_uid,
                    link_type,
                    direction,
                    strength,
                    rationale,
                    None,
                    None,
                    source,
                    source,
                    source_row_id,
                    now,
                    now,
                ),
            )
            inserted += 1

        status = "WARN" if skipped else "OK"
        notes = (
            f"processed={processed}, deleted_previous={deleted_previous}, inserted={inserted}, skipped={skipped}, "
            f"skipped_raw_refs={skipped_raw_refs}, skipped_missing_map={skipped_missing_map}, "
            f"skipped_missing_uid={skipped_missing_uid}, skipped_unsupported_kind={skipped_unsupported_kind}, "
            f"skipped_missing_nodes={skipped_missing_nodes}"
        )
        insert_sync_run(cur, status=status, notes=notes, now=now)
        conn.commit()
    except Exception as exc:
        conn.rollback()
        try:
            conn.execute("BEGIN IMMEDIATE")
            if table_exists(cur, "sync_runs"):
                insert_sync_run(cur, status="FAIL", notes=str(exc)[:500], now=now)
                conn.commit()
        except Exception:
            conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
