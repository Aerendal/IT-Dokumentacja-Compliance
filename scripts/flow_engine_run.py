#!/usr/bin/env python3
"""Flow Engine runner: computes section_quality, edge_health, blockers and summary report.
- Deterministic, DB-first, offline.
- Assumes earlier steps already ran: file_index -> sync_docs_ids -> extract_sections -> materialize_edges -> resolve_content_links -> extract_section_metrics.
"""

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DB = BASE / "reports" / "it_doc_matrix.db"
REPORT_OUT = BASE / "reports" / "latest" / "flow_engine_report.json"


def utc_now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def j(x):
    return json.dumps(x, ensure_ascii=False)


def compute_section_quality(conn):
    cur = conn.cursor()
    now = utc_now_iso()

    conn.execute("BEGIN IMMEDIATE")
    cur.execute("DELETE FROM section_quality")

    # contracts cache
    cur.execute("SELECT scope_kind, scope_uid, gates_json FROM contracts")
    contracts = {}
    for kind, uid, gates_json in cur.fetchall():
        try:
            gates = json.loads(gates_json or "[]")
        except json.JSONDecodeError:
            gates = []
        contracts[(kind, uid)] = gates

    cur.execute(
        """
        SELECT s.section_uid, s.doc_uid, s.status,
               COALESCE(m.lines, 0), COALESCE(m.checkbox_count, 0)
        FROM sections s
        LEFT JOIN section_metrics m ON m.section_uid = s.section_uid
        """
    )
    rows = cur.fetchall()

    for section_uid, doc_uid, sec_status, lines, cb in rows:
        gates = contracts.get(("section", section_uid), contracts.get(("doc", doc_uid), []))
        missing = []
        score = 100
        status = "ok"

        # base rules
        if lines == 0:
            status = "needs_structure"
            score = 0
            missing.append({"gate": "metrics_missing"})
        else:
            if sec_status == "placeholder":
                status = "needs_content"
                score -= 40
                missing.append({"gate": "no_placeholder"})
            if lines < 3:
                status = "needs_content" if status == "ok" else status
                score -= 20
                missing.append({"gate": "min_lines", "min": 3})

        # contract gates
        for g in gates:
            if g.get("gate") == "min_checkboxes":
                mn = int(g.get("min", 0))
                if cb < mn:
                    status = "needs_content" if status == "ok" else status
                    score -= 10
                    missing.append({"gate": "min_checkboxes", "min": mn, "have": cb})

        score = max(score, 0)

        cur.execute(
            """
            INSERT INTO section_quality(section_uid, doc_uid, status, score, missing_gates_json, last_scan_at_utc)
            VALUES (?,?,?,?,?,?)
            """,
            (section_uid, doc_uid, status, score, j(missing), now),
        )

    conn.commit()


def compute_edge_health(conn):
    cur = conn.cursor()
    now = utc_now_iso()

    conn.execute("BEGIN IMMEDIATE")
    cur.execute("DELETE FROM edge_health")

    cur.execute("SELECT doc_uid FROM docs")
    docs_set = {r[0] for r in cur.fetchall()}
    cur.execute("SELECT section_uid FROM sections")
    sec_set = {r[0] for r in cur.fetchall()}

    cur.execute(
        """
        SELECT edge_uid, from_kind, from_uid, to_kind, to_uid,
               link_type, direction, rationale, strength, source
        FROM edges
        """
    )
    for edge_uid, _fk, _fu, tk, tu, _lt, _dr, rat, strength, source in cur.fetchall():
        reasons = []
        status = "ok"

        # unresolved content link -> warn; do not target-check content_links
        raw_content_link = source == "content_links"
        if raw_content_link:
            if isinstance(tu, str) and tu.startswith("section::"):
                reasons.append({"code": "CONTENT_LINK_UNRESOLVED"})
            else:
                reasons.append({"code": "CONTENT_LINK_UNRESOLVED"})
            status = "warn"
        else:
            # target existence (only for resolved UIDs)
            if tk == "doc" and tu not in docs_set:
                reasons.append({"code": "TARGET_MISSING", "detail": "doc missing"})
                status = "fail"
            if tk == "section" and tu not in sec_set:
                reasons.append({"code": "TARGET_MISSING", "detail": "section missing"})
                status = "fail"

        # missing rationale for required/blocking
        if strength in ("required", "blocking") and (rat is None or str(rat).strip() == ""):
            reasons.append({"code": "MISSING_RATIONALE"})
            status = "fail" if strength == "blocking" else ("warn" if status != "fail" else status)

        cur.execute(
            """
            INSERT INTO edge_health(edge_uid, status, reasons_json, last_scan_at_utc)
            VALUES (?,?,?,?)
            """,
            (edge_uid, status, j(reasons), now),
        )

    conn.commit()


def compute_blockers(conn):
    cur = conn.cursor()
    now = utc_now_iso()

    cur.execute("SELECT doc_uid, status FROM doc_quality")
    doc_q = dict(cur.fetchall())
    cur.execute("SELECT section_uid, status FROM section_quality")
    sec_q = dict(cur.fetchall())

    def is_ok(kind, uid):
        if kind == "doc":
            return doc_q.get(uid) == "ok"
        return sec_q.get(uid) == "ok"

    conn.execute("BEGIN IMMEDIATE")
    cur.execute("DELETE FROM blockers")

    cur.execute(
        """
        SELECT edge_uid, from_kind, from_uid, to_kind, to_uid, strength, link_type
        FROM edges
        WHERE strength IN ('required','blocking')
        """
    )
    for edge_uid, fk, fu, tk, tu, strength, lt in cur.fetchall():
        if tk == "section" and isinstance(tu, str) and tu.startswith("section::"):
            continue  # unresolved; handled in edge_health

        if not is_ok(fk, fu):
            sev = "H" if strength == "blocking" else "M"
            cur.execute(
                """
                INSERT OR IGNORE INTO blockers(
                  blocked_kind, blocked_uid, blocker_kind, blocker_uid,
                  reason_code, severity, evidence_json, created_at_utc
                ) VALUES (?,?,?,?,?,?,?,?)
                """,
                (
                    tk,
                    tu,
                    fk,
                    fu,
                    "UPSTREAM_REQUIRED_NOT_OK",
                    sev,
                    j({"edge_uid": edge_uid, "link_type": lt, "strength": strength}),
                    now,
                ),
            )

    conn.commit()


def summarize(conn) -> dict:
    cur = conn.cursor()
    cur.execute("SELECT status, COUNT(*) FROM doc_quality GROUP BY status")
    doc_status = dict(cur.fetchall())
    cur.execute("SELECT status, COUNT(*) FROM section_quality GROUP BY status")
    sec_status = dict(cur.fetchall())
    cur.execute("SELECT status, COUNT(*) FROM edge_health GROUP BY status")
    edge_status = dict(cur.fetchall())
    cur.execute("SELECT severity, COUNT(*) FROM blockers GROUP BY severity")
    blocker_sev = dict(cur.fetchall())
    return {
        "doc_quality": doc_status,
        "section_quality": sec_status,
        "edge_health": edge_status,
        "blockers": blocker_sev,
    }


def main():
    assert DB.exists(), f"Missing DB: {DB}"
    conn = sqlite3.connect(str(DB))
    conn.execute("PRAGMA foreign_keys = ON")

    # ensure tables exist (idempotent)
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS contracts (
          contract_id TEXT PRIMARY KEY,
          scope_kind TEXT NOT NULL CHECK(scope_kind IN ('doc','section')),
          scope_uid TEXT NOT NULL,
          version INTEGER NOT NULL DEFAULT 1,
          inputs_json TEXT NOT NULL DEFAULT '[]',
          outputs_json TEXT NOT NULL DEFAULT '[]',
          gates_json TEXT NOT NULL DEFAULT '[]',
          impact_json TEXT NOT NULL DEFAULT '{}',
          owner TEXT,
          notes TEXT,
          created_at_utc TEXT NOT NULL DEFAULT '',
          updated_at_utc TEXT NOT NULL DEFAULT ''
        );
        CREATE INDEX IF NOT EXISTS idx_contracts_scope ON contracts(scope_kind, scope_uid);

        CREATE TABLE IF NOT EXISTS edge_health (
          edge_uid TEXT PRIMARY KEY REFERENCES edges(edge_uid) ON DELETE CASCADE,
          status TEXT NOT NULL CHECK(status IN ('ok','warn','fail')),
          reasons_json TEXT NOT NULL,
          last_scan_at_utc TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_edge_health_status ON edge_health(status);

        CREATE TABLE IF NOT EXISTS blockers (
          blocked_kind TEXT NOT NULL CHECK(blocked_kind IN ('doc','section')),
          blocked_uid TEXT NOT NULL,
          blocker_kind TEXT NOT NULL CHECK(blocker_kind IN ('doc','section')),
          blocker_uid TEXT NOT NULL,
          reason_code TEXT NOT NULL,
          severity TEXT NOT NULL CHECK(severity IN ('H','M','L')),
          evidence_json TEXT NOT NULL DEFAULT '{}',
          created_at_utc TEXT NOT NULL,
          PRIMARY KEY (blocked_kind, blocked_uid, blocker_kind, blocker_uid, reason_code)
        );
        CREATE INDEX IF NOT EXISTS idx_blockers_blocked ON blockers(blocked_kind, blocked_uid);
        CREATE INDEX IF NOT EXISTS idx_blockers_sev ON blockers(severity);

        CREATE TABLE IF NOT EXISTS section_quality (
          section_uid TEXT PRIMARY KEY REFERENCES sections(section_uid) ON DELETE CASCADE,
          doc_uid TEXT NOT NULL REFERENCES docs(doc_uid) ON DELETE CASCADE,
          status TEXT NOT NULL CHECK(status IN ('ok','needs_structure','needs_content','needs_links','blocked')),
          score INTEGER NOT NULL,
          missing_gates_json TEXT NOT NULL DEFAULT '[]',
          last_scan_at_utc TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_section_quality_doc ON section_quality(doc_uid);
        CREATE INDEX IF NOT EXISTS idx_section_quality_status ON section_quality(status);
        """
    )

    compute_section_quality(conn)
    compute_edge_health(conn)
    compute_blockers(conn)

    rep = {"ran_at_utc": utc_now_iso(), "summary": summarize(conn)}
    REPORT_OUT.parent.mkdir(parents=True, exist_ok=True)
    REPORT_OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    conn.close()


if __name__ == "__main__":
    main()
