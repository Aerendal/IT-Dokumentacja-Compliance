#!/usr/bin/env python3
"""Infer v1 edges from node structure and heading similarity."""

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
RUN_KIND = "graph_edges_inferred"
ALGORITHM_VERSION = "infer_v1"
SOURCE_TAG = "infer_edges_v1"
MIN_SHARED_HEADINGS = 5
TOP_N_PER_DOC = 20
MAX_DOCS_PER_HEADING = 50
MAX_NODES_PER_ANCHOR = 80
BATCH_SIZE = 10000
DOC_HEADING_STOPLIST = frozenset(
    {
        "cel dokumentu",
        "metadane",
        "jak używać dokumentu",
        "szybkie powiązania",
        "struktura sekcji (szkielet)",
        "checklisty jakości",
        "zakres i granice",
        "wejścia i wyjścia",
        "wymagane rozwinięcia",
        "wymagane streszczenia",
        "powiązania (meta)",
        "zależności dokumentu",
        "powiązania sekcja↔sekcja",
        "fazy cyklu życia",
        "definicje robocze",
        "otwarte pytania",
        "założenia",
        "guidance",
        "decyzje i uzasadnienia",
        "ryzyka i ograniczenia",
        "przykłady użycia",
        "artefakty powiązane",
        "weryfikacja spójności",
        "metryki jakości",
        "powiązania z innymi dokumentami",
        "wymagane odwołania do standardów",
        "kryteria ukończenia",
        "mapa relacji dokument→dokument",
        "mapa relacji sekcja→sekcja",
        "ścieżki informacji",
    }
)


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


def new_edge_id() -> str:
    return f"gei_{uuid.uuid4().hex}"


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
        return (
            False,
            f"migrate_edges_manual older than build_nodes: edges_ts={edges_ts} < nodes_ts={nodes_ts}",
        )
    return True, "ok"


def doc_pair(a: str, b: str) -> tuple[str, str]:
    return (a, b) if a < b else (b, a)


def doc_related_confidence(shared: int) -> float:
    return min(0.95, 0.35 + 0.1 * min(shared, 6))


def infer_doc_related(cur: sqlite3.Cursor, now: str) -> dict[str, int]:
    cur.execute("SELECT doc_uid,node_uid FROM node_map_docs")
    doc_map = dict(cur.fetchall())
    pair_shared: dict[tuple[str, str], int] = {}
    skipped_common_headings = 0
    skipped_stoplist_headings = 0
    total_headings = 0

    cur.execute(
        """
        SELECT key_norm, doc_uid
        FROM (
          SELECT key_norm, doc_uid
          FROM nodes
          WHERE kind IN ('sec','subsec')
            AND key_norm IS NOT NULL
            AND TRIM(key_norm) <> ''
          GROUP BY key_norm, doc_uid
        )
        ORDER BY key_norm, doc_uid
        """
    )

    current_heading: str | None = None
    docs_for_heading: list[str] = []

    def flush_heading(heading: str | None, docs: list[str]) -> None:
        nonlocal skipped_common_headings, skipped_stoplist_headings, total_headings
        if heading is None:
            return
        total_headings += 1
        if heading in DOC_HEADING_STOPLIST:
            skipped_stoplist_headings += 1
            return
        if len(docs) > MAX_DOCS_PER_HEADING:
            skipped_common_headings += 1
            return
        for i in range(len(docs)):
            for j in range(i + 1, len(docs)):
                key = doc_pair(docs[i], docs[j])
                pair_shared[key] = pair_shared.get(key, 0) + 1

    for key_norm, doc_uid in cur:
        if key_norm != current_heading:
            flush_heading(current_heading, docs_for_heading)
            current_heading = key_norm
            docs_for_heading = [doc_uid]
        elif not docs_for_heading or docs_for_heading[-1] != doc_uid:
            docs_for_heading.append(doc_uid)
    flush_heading(current_heading, docs_for_heading)

    candidates_by_doc: dict[str, list[tuple[str, int, float]]] = {}
    pairs_meeting_threshold = 0
    for (doc_a, doc_b), shared in pair_shared.items():
        if shared < MIN_SHARED_HEADINGS:
            continue
        from_node = doc_map.get(doc_a)
        to_node = doc_map.get(doc_b)
        if from_node is None or to_node is None:
            continue
        pairs_meeting_threshold += 1
        confidence = doc_related_confidence(shared)
        candidates_by_doc.setdefault(doc_a, []).append((doc_b, shared, confidence))
        candidates_by_doc.setdefault(doc_b, []).append((doc_a, shared, confidence))

    selected_pairs: set[tuple[str, str]] = set()
    for doc_uid, candidates in candidates_by_doc.items():
        candidates.sort(key=lambda item: (-item[1], -item[2], item[0]))
        for other_doc_uid, _shared, _confidence in candidates[:TOP_N_PER_DOC]:
            selected_pairs.add(doc_pair(doc_uid, other_doc_uid))

    rows: list[tuple] = []
    inserted = 0
    for doc_a, doc_b in sorted(selected_pairs):
        shared = pair_shared[(doc_a, doc_b)]
        from_node = doc_map[doc_a]
        to_node = doc_map[doc_b]
        confidence = doc_related_confidence(shared)
        evidence = json.dumps(
            {
                "method": "shared_heading_norm",
                "shared_heading_count": shared,
                "threshold": MIN_SHARED_HEADINGS,
                "top_n_per_doc": TOP_N_PER_DOC,
            },
            ensure_ascii=False,
        )
        edge_uid = new_edge_id()
        rows.append(
            (
                edge_uid,
                from_node,
                to_node,
                "related",
                "undirected",
                "navigational",
                None,
                None,
                confidence,
                evidence,
                now,
                "active",
                edge_uid,
                "related",
                ALGORITHM_VERSION,
                now,
                SOURCE_TAG,
                None,
            )
        )
        inserted += 1
        if len(rows) >= BATCH_SIZE:
            cur.executemany(
                """
                INSERT INTO edges_inferred(
                  edge_uid,from_node_uid,to_node_uid,link_type,direction,strength,impact_area,impact_level,confidence,evidence_json,
                  created_at_utc,status,edge_inferred_id,relation_kind,algorithm_version,updated_at_utc,source,source_row_id
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                rows,
            )
            rows.clear()

    if rows:
        cur.executemany(
            """
            INSERT INTO edges_inferred(
              edge_uid,from_node_uid,to_node_uid,link_type,direction,strength,impact_area,impact_level,confidence,evidence_json,
              created_at_utc,status,edge_inferred_id,relation_kind,algorithm_version,updated_at_utc,source,source_row_id
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            rows,
        )

    return {
        "doc_related_inserted": inserted,
        "doc_related_pairs": len(pair_shared),
        "doc_related_pairs_meeting_threshold": pairs_meeting_threshold,
        "doc_related_pairs_selected_top_n": len(selected_pairs),
        "doc_top_n_per_doc": TOP_N_PER_DOC,
        "doc_headings_total": total_headings,
        "doc_headings_skipped_common": skipped_common_headings,
        "doc_headings_skipped_stoplist": skipped_stoplist_headings,
        "doc_headings_stoplist_size": len(DOC_HEADING_STOPLIST),
    }


def infer_subsec_anchor_alignment(cur: sqlite3.Cursor, now: str) -> dict[str, int]:
    cur.execute(
        """
        SELECT anchor,node_uid,doc_uid
        FROM nodes
        WHERE kind='subsec'
          AND anchor IS NOT NULL
          AND TRIM(anchor) <> ''
        ORDER BY anchor, doc_uid, node_uid
        """
    )

    current_anchor: str | None = None
    group: list[tuple[str, str]] = []
    inserted = 0
    skipped_common_anchors = 0
    anchors_total = 0
    seen_pairs: set[tuple[str, str]] = set()
    rows: list[tuple] = []

    def flush_anchor(anchor: str | None, nodes_group: list[tuple[str, str]]) -> None:
        nonlocal inserted, skipped_common_anchors, anchors_total
        if anchor is None:
            return
        anchors_total += 1
        if len(nodes_group) > MAX_NODES_PER_ANCHOR:
            skipped_common_anchors += 1
            return

        group_size = len(nodes_group)
        confidence = max(0.55, min(0.92, 0.92 - 0.01 * max(0, group_size - 2)))
        for i in range(group_size):
            left_node, left_doc = nodes_group[i]
            for j in range(i + 1, group_size):
                right_node, right_doc = nodes_group[j]
                if left_doc == right_doc:
                    continue
                pair = doc_pair(left_node, right_node)
                if pair in seen_pairs:
                    continue
                seen_pairs.add(pair)

                evidence = json.dumps(
                    {
                        "method": "anchor_match",
                        "anchor": anchor,
                        "anchor_group_size": group_size,
                    },
                    ensure_ascii=False,
                )
                edge_uid = new_edge_id()
                rows.append(
                    (
                        edge_uid,
                        pair[0],
                        pair[1],
                        "aligns_with",
                        "undirected",
                        "navigational",
                        None,
                        None,
                        confidence,
                        evidence,
                        now,
                        "active",
                        edge_uid,
                        "aligns_with",
                        ALGORITHM_VERSION,
                        now,
                        SOURCE_TAG,
                        None,
                    )
                )
                inserted += 1

                if len(rows) >= BATCH_SIZE:
                    cur.executemany(
                        """
                        INSERT INTO edges_inferred(
                          edge_uid,from_node_uid,to_node_uid,link_type,direction,strength,impact_area,impact_level,confidence,evidence_json,
                          created_at_utc,status,edge_inferred_id,relation_kind,algorithm_version,updated_at_utc,source,source_row_id
                        ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                        """,
                        rows,
                    )
                    rows.clear()

    for anchor, node_uid, doc_uid in cur:
        if anchor != current_anchor:
            flush_anchor(current_anchor, group)
            current_anchor = anchor
            group = [(node_uid, doc_uid)]
        else:
            group.append((node_uid, doc_uid))
    flush_anchor(current_anchor, group)

    if rows:
        cur.executemany(
            """
            INSERT INTO edges_inferred(
              edge_uid,from_node_uid,to_node_uid,link_type,direction,strength,impact_area,impact_level,confidence,evidence_json,
              created_at_utc,status,edge_inferred_id,relation_kind,algorithm_version,updated_at_utc,source,source_row_id
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            rows,
        )

    return {
        "subsec_align_inserted": inserted,
        "anchors_total": anchors_total,
        "anchors_skipped_common": skipped_common_anchors,
        "subsec_pairs_seen": len(seen_pairs),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Infer edges v1.")
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
        require_tables(cur, ["sync_runs", "nodes", "node_map_docs", "edges_inferred"])

        gate_ok, reason = gate_sync_runs(cur)
        if not gate_ok:
            insert_sync_run(cur, status="WARN", notes=f"skip: gate: {reason}", now=now)
            conn.commit()
            return

        cur.execute(
            "DELETE FROM edges_inferred WHERE source=? OR algorithm_version=?",
            (SOURCE_TAG, ALGORITHM_VERSION),
        )
        deleted_previous = cur.rowcount if cur.rowcount != -1 else 0

        stats_doc = infer_doc_related(cur, now)
        stats_subsec = infer_subsec_anchor_alignment(cur, now)
        inserted_total = stats_doc["doc_related_inserted"] + stats_subsec["subsec_align_inserted"]
        notes = (
            f"gate=ok, deleted_previous={deleted_previous}, inserted_total={inserted_total}, "
            f"doc_related_inserted={stats_doc['doc_related_inserted']}, doc_related_pairs={stats_doc['doc_related_pairs']}, "
            f"doc_related_pairs_meeting_threshold={stats_doc['doc_related_pairs_meeting_threshold']}, "
            f"doc_related_pairs_selected_top_n={stats_doc['doc_related_pairs_selected_top_n']}, "
            f"doc_top_n_per_doc={stats_doc['doc_top_n_per_doc']}, min_shared_headings={MIN_SHARED_HEADINGS}, "
            f"doc_headings_total={stats_doc['doc_headings_total']}, doc_headings_skipped_common={stats_doc['doc_headings_skipped_common']}, "
            f"doc_headings_skipped_stoplist={stats_doc['doc_headings_skipped_stoplist']}, "
            f"doc_headings_stoplist_size={stats_doc['doc_headings_stoplist_size']}, "
            f"subsec_align_inserted={stats_subsec['subsec_align_inserted']}, subsec_pairs_seen={stats_subsec['subsec_pairs_seen']}, "
            f"anchors_total={stats_subsec['anchors_total']}, anchors_skipped_common={stats_subsec['anchors_skipped_common']}, "
            f"algorithm={ALGORITHM_VERSION}"
        )
        insert_sync_run(cur, status="OK", notes=notes, now=now)
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
