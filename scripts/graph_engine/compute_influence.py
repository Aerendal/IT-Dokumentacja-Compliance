#!/usr/bin/env python3
"""Compute influence v1 from manual blocking/required edges and node hierarchy."""

from __future__ import annotations

import argparse
import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB_ARG = "reports/it_doc_matrix.db"
PROJECT_DB = Path(__file__).resolve().parents[2] / "reports" / "it_doc_matrix.db"
DDL_PATH = Path(__file__).resolve().parent / "ddl_nodes.sql"
RUN_KIND = "graph_influence"
ALGORITHM_VERSION = "influence_v1"
BATCH_SIZE = 10000
LEVEL_BY_SEVERITY = {1: "low", 2: "medium", 3: "high", 4: "critical"}
NEEDS_STATUSES = {"needs_structure", "needs_content", "needs_links"}


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


def latest_sync_ts(cur: sqlite3.Cursor, kind: str) -> str | None:
    cur.execute(
        "SELECT ran_at_utc FROM sync_runs WHERE kind=? AND status IN ('OK','WARN') ORDER BY ran_at_utc DESC LIMIT 1",
        (kind,),
    )
    row = cur.fetchone()
    return row[0] if row else None


def gate_sync_runs(cur: sqlite3.Cursor) -> tuple[bool, str]:
    nodes_ts = latest_sync_ts(cur, "build_nodes")
    edges_ts = latest_sync_ts(cur, "migrate_edges_manual")
    if not nodes_ts:
        return False, "missing sync_runs kind=build_nodes (OK/WARN)"
    if not edges_ts:
        return False, "missing sync_runs kind=migrate_edges_manual (OK/WARN)"
    if edges_ts < nodes_ts:
        return False, f"migrate_edges_manual older than build_nodes: edges_ts={edges_ts} < nodes_ts={nodes_ts}"
    return True, "ok"


def new_influence_id() -> str:
    return f"gif_{uuid.uuid4().hex}"


def normalize_quality(raw: str | None) -> str:
    if raw is None:
        return "unknown"
    s = str(raw).strip().lower()
    allowed = {"ok", "needs_structure", "needs_content", "needs_links", "blocked", "unknown"}
    if s == "filled":
        return "ok"
    return s if s in allowed else "unknown"


def severity_from_edge(strength: str, from_quality: str, to_quality: str) -> int:
    sev = 3 if strength == "blocking" else 2
    qualities = {from_quality, to_quality}
    if "blocked" in qualities:
        return 4
    if qualities & NEEDS_STATUSES:
        return max(sev, 3)
    if qualities == {"ok"}:
        return max(1, sev - 1)
    return sev


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compute influence v1.")
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


def compute_v1(cur: sqlite3.Cursor, now: str) -> tuple[int, int, int, int]:
    cur.execute("SELECT node_uid,kind,doc_uid,parent_node_uid,status FROM nodes")
    nodes = {
        node_uid: {
            "kind": kind,
            "doc_uid": doc_uid,
            "parent": parent_node_uid,
            "status": status,
        }
        for node_uid, kind, doc_uid, parent_node_uid, status in cur.fetchall()
    }

    doc_quality: dict[str, str] = {}
    section_quality: dict[str, str] = {}
    if table_exists(cur, "doc_quality"):
        cur.execute("SELECT doc_uid,status FROM doc_quality")
        doc_quality = {doc_uid: normalize_quality(status) for doc_uid, status in cur.fetchall()}
    if table_exists(cur, "section_quality"):
        cur.execute("SELECT section_uid,status FROM section_quality")
        section_quality = {section_uid: normalize_quality(status) for section_uid, status in cur.fetchall()}

    ancestors_cache: dict[str, list[str]] = {}

    def ancestors(node_uid: str) -> list[str]:
        cached = ancestors_cache.get(node_uid)
        if cached is not None:
            return cached
        out = [node_uid]
        seen = {node_uid}
        cur_uid = node_uid
        while True:
            parent = nodes.get(cur_uid, {}).get("parent")
            if parent is None or parent in seen or parent not in nodes:
                break
            out.append(parent)
            seen.add(parent)
            cur_uid = parent
        ancestors_cache[node_uid] = out
        return out

    def quality_for_node(node_uid: str) -> str:
        node = nodes.get(node_uid)
        if node is None:
            return "unknown"
        kind = node["kind"]
        doc_uid = node["doc_uid"]
        node_status = normalize_quality(node["status"])
        if kind == "doc":
            return doc_quality.get(doc_uid, node_status)
        return section_quality.get(node_uid, doc_quality.get(doc_uid, node_status))

    cur.execute("DELETE FROM influence WHERE algorithm_version=?", (ALGORITHM_VERSION,))
    deleted_previous = cur.rowcount if cur.rowcount != -1 else 0

    cur.execute(
        """
        SELECT edge_uid,from_node_uid,to_node_uid,strength,COALESCE(status,'active'),source
        FROM edges_manual
        WHERE strength IN ('required','blocking')
          AND COALESCE(status,'active') IN ('active','unknown')
        """
    )
    manual_edges = cur.fetchall()
    processed = len(manual_edges)
    skipped_missing_nodes = 0

    aggregate: dict[tuple[str, str, str], dict[str, object]] = {}

    def upsert(src: str, dst: str, influence_type: str, severity: int, details: dict[str, object], notes: str) -> None:
        key = (src, dst, influence_type)
        current = aggregate.get(key)
        if current is None or severity > int(current["severity"]):
            aggregate[key] = {
                "severity": severity,
                "details": details,
                "notes": notes,
            }

    for edge_uid, from_node_uid, to_node_uid, strength, _status, source in manual_edges:
        if from_node_uid not in nodes or to_node_uid not in nodes:
            skipped_missing_nodes += 1
            continue

        from_q = quality_for_node(from_node_uid)
        to_q = quality_for_node(to_node_uid)
        base_severity = severity_from_edge(strength, from_q, to_q)
        base_details = {
            "method": "manual_edge_1hop",
            "edge_uid": edge_uid,
            "strength": strength,
            "from_quality": from_q,
            "to_quality": to_q,
            "source": source,
            "aggregation_distance": 0,
        }
        upsert(from_node_uid, to_node_uid, "blocks", base_severity, base_details, f"manual:{strength}")

        src_anc = ancestors(from_node_uid)
        dst_anc = ancestors(to_node_uid)
        for i, src_uid in enumerate(src_anc):
            for j, dst_uid in enumerate(dst_anc):
                if i == 0 and j == 0:
                    continue
                if src_uid == dst_uid:
                    continue
                dist = i + j
                agg_severity = max(1, base_severity - min(2, dist))
                agg_details = {
                    "method": "hierarchy_aggregation",
                    "edge_uid": edge_uid,
                    "strength": strength,
                    "from_quality": from_q,
                    "to_quality": to_q,
                    "source": source,
                    "aggregation_distance": dist,
                    "src_depth": i,
                    "dst_depth": j,
                    "src_base": from_node_uid,
                    "dst_base": to_node_uid,
                }
                upsert(src_uid, dst_uid, "blocks", agg_severity, agg_details, f"agg:{strength}:d{dist}")

    rows: list[tuple] = []
    for (src_uid, dst_uid, influence_type), payload in aggregate.items():
        severity = int(payload["severity"])
        level = LEVEL_BY_SEVERITY[severity]
        rows.append(
            (
                src_uid,
                dst_uid,
                influence_type,
                level,
                json.dumps([src_uid, dst_uid], ensure_ascii=False),
                now,
                new_influence_id(),
                src_uid,
                dst_uid,
                round(severity / 4.0, 3),
                ALGORITHM_VERSION,
                str(payload["notes"]),
                json.dumps(payload["details"], ensure_ascii=False),
            )
        )
        if len(rows) >= BATCH_SIZE:
            cur.executemany(
                """
                INSERT INTO influence(
                  src_node_uid,dst_node_uid,influence_type,level,path_json,computed_at_utc,
                  influence_id,source_node_uid,target_node_uid,score,algorithm_version,notes,details_json
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                rows,
            )
            rows.clear()
    if rows:
        cur.executemany(
            """
            INSERT INTO influence(
              src_node_uid,dst_node_uid,influence_type,level,path_json,computed_at_utc,
              influence_id,source_node_uid,target_node_uid,score,algorithm_version,notes,details_json
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            rows,
        )

    return processed, deleted_previous, len(aggregate), skipped_missing_nodes


def main() -> None:
    args = parse_args()
    db_path = resolve_db_path(args.db)
    now = utc_now_iso()
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    try:
        conn.execute("BEGIN IMMEDIATE")
        apply_ddl(cur)
        require_tables(cur, ["sync_runs", "nodes", "edges_manual", "influence"])

        gate_ok, reason = gate_sync_runs(cur)
        if not gate_ok:
            insert_sync_run(cur, status="WARN", notes=f"skip: gate: {reason}", now=now)
            conn.commit()
            return

        processed, deleted_previous, inserted, skipped_missing_nodes = compute_v1(cur, now)
        status = "WARN" if skipped_missing_nodes else "OK"
        notes = (
            f"gate=ok, processed_manual={processed}, deleted_previous={deleted_previous}, inserted={inserted}, "
            f"skipped_missing_nodes={skipped_missing_nodes}, algorithm={ALGORITHM_VERSION}"
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
