"""
tests/test_standard_controls.py — Unit tests for seed_standard_controls and map_docs_to_controls.
"""
import sqlite3
import sys
import os
import pytest

pytestmark = pytest.mark.unit

# Make scripts importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts", "maintenance"))

from seed_standard_controls import (
    CREATE_TABLE_SQL as SEED_TABLE_SQL,
    ALL_CONTROLS,
)
from map_docs_to_controls import (
    CREATE_TABLE_SQL as MAP_TABLE_SQL,
    map_docs_to_controls,
)


# ── helpers ──────────────────────────────────────────────────────────────────

def make_seed_db():
    """In-memory DB with standard_controls table seeded."""
    conn = sqlite3.connect(":memory:")
    conn.executescript(SEED_TABLE_SQL)
    conn.executemany(
        "INSERT OR IGNORE INTO standard_controls "
        "(standard_code, control_id, control_name, theme, description) VALUES (?,?,?,?,?)",
        ALL_CONTROLS,
    )
    conn.commit()
    return conn


def make_mapping_db():
    """In-memory DB with standard_controls + doc_standard_mapping + docs for mapping tests."""
    conn = sqlite3.connect(":memory:")
    # seed standard_controls
    conn.executescript(SEED_TABLE_SQL)
    conn.executemany(
        "INSERT OR IGNORE INTO standard_controls "
        "(standard_code, control_id, control_name, theme, description) VALUES (?,?,?,?,?)",
        ALL_CONTROLS,
    )
    # minimal docs table
    conn.execute(
        "CREATE TABLE docs (doc_uid TEXT PRIMARY KEY, title TEXT NOT NULL, "
        "title_norm TEXT NOT NULL, path TEXT, origin TEXT NOT NULL DEFAULT 'core', "
        "created_at_utc TEXT NOT NULL, updated_at_utc TEXT NOT NULL)"
    )
    conn.execute(
        "CREATE TABLE doc_standard_mapping "
        "(id INTEGER PRIMARY KEY, doc_path TEXT, standard_code TEXT, "
        "method TEXT, confidence REAL, notes TEXT)"
    )
    # insert a handful of test docs
    test_docs = [
        ("uid1", "Access Control Policy",          "access control policy",          "core/access_control.md"),
        ("uid2", "Incident Management Procedure",  "incident management procedure",  "core/incident_mgmt.md"),
        ("uid3", "Data Backup and Recovery Plan",  "data backup and recovery plan",  "core/backup_recovery.md"),
        ("uid4", "Supplier Risk Assessment",       "supplier risk assessment",       "core/supplier_risk.md"),
        ("uid5", "Network Security Architecture",  "network security architecture",  "core/network_security.md"),
        ("uid6", "Cryptography Standards",         "cryptography standards",         "core/cryptography.md"),
    ]
    conn.executemany(
        "INSERT INTO docs (doc_uid, title, title_norm, path, created_at_utc, updated_at_utc) VALUES (?,?,?,?,?,?)",
        [(u, t, n, p, "2025-01-01T00:00:00Z", "2025-01-01T00:00:00Z") for u, t, n, p in test_docs],
    )
    for _, _, _, path in test_docs:
        conn.execute(
            "INSERT INTO doc_standard_mapping (doc_path, standard_code, method, confidence) VALUES (?,?,?,?)",
            (path, "ISO/IEC 27001", "test", 0.5),
        )
    conn.executescript(MAP_TABLE_SQL)
    conn.commit()
    return conn


# ── tests ─────────────────────────────────────────────────────────────────────

def test_seed_creates_table():
    conn = make_seed_db()
    cur = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='standard_controls'"
    )
    assert cur.fetchone() is not None


def test_seed_iso27001_count():
    conn = make_seed_db()
    cur = conn.execute(
        "SELECT COUNT(*) FROM standard_controls WHERE standard_code='ISO/IEC 27001'"
    )
    assert cur.fetchone()[0] == 93


def test_seed_nist_csf_count():
    conn = make_seed_db()
    cur = conn.execute(
        "SELECT COUNT(*) FROM standard_controls WHERE standard_code='NIST CSF 2.0'"
    )
    assert cur.fetchone()[0] == 22


def test_iso27001_themes():
    conn = make_seed_db()
    cur = conn.execute(
        "SELECT DISTINCT theme FROM standard_controls WHERE standard_code='ISO/IEC 27001'"
    )
    themes = {row[0] for row in cur.fetchall()}
    assert {"Organizational", "People", "Physical", "Technological"} == themes


def test_control_ids_unique():
    conn = make_seed_db()
    cur = conn.execute(
        "SELECT standard_code, control_id, COUNT(*) as cnt "
        "FROM standard_controls GROUP BY standard_code, control_id HAVING cnt > 1"
    )
    duplicates = cur.fetchall()
    assert duplicates == [], f"Duplicate controls found: {duplicates}"


def test_doc_control_mapping_table_created():
    conn = make_mapping_db()
    cur = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='doc_control_mapping'"
    )
    assert cur.fetchone() is not None


def test_map_assigns_top5_max():
    conn = make_mapping_db()
    map_docs_to_controls(":memory:", apply=True, standard="ISO/IEC 27001",
                         min_confidence=0.05, _conn=conn)
    cur = conn.execute(
        "SELECT doc_path, COUNT(*) as cnt FROM doc_control_mapping "
        "WHERE standard_code='ISO/IEC 27001' GROUP BY doc_path HAVING cnt > 5"
    )
    over_five = cur.fetchall()
    assert over_five == [], f"Some docs have >5 controls: {over_five}"


def test_map_dry_run_no_changes():
    conn = make_mapping_db()
    map_docs_to_controls(":memory:", dry_run=True, standard="ISO/IEC 27001",
                         min_confidence=0.05, _conn=conn)
    cur = conn.execute("SELECT COUNT(*) FROM doc_control_mapping")
    assert cur.fetchone()[0] == 0, "Dry-run should not write rows"


def test_map_min_confidence_filter():
    conn = make_mapping_db()
    map_docs_to_controls(":memory:", apply=True, standard="ISO/IEC 27001",
                         min_confidence=0.9, _conn=conn)
    cur = conn.execute("SELECT COUNT(*) FROM doc_control_mapping WHERE confidence < 0.9")
    below_threshold = cur.fetchone()[0]
    assert below_threshold == 0, f"{below_threshold} rows below min_confidence threshold"


def test_nist_functions():
    conn = make_seed_db()
    cur = conn.execute(
        "SELECT DISTINCT theme FROM standard_controls WHERE standard_code='NIST CSF 2.0'"
    )
    functions = {row[0] for row in cur.fetchall()}
    expected = {"GOVERN", "IDENTIFY", "PROTECT", "DETECT", "RESPOND", "RECOVER"}
    assert expected == functions, f"Missing NIST functions: {expected - functions}"


def test_iso27001_organizational_count():
    """Organizational theme should have exactly 37 controls."""
    conn = make_seed_db()
    cur = conn.execute(
        "SELECT COUNT(*) FROM standard_controls "
        "WHERE standard_code='ISO/IEC 27001' AND theme='Organizational'"
    )
    assert cur.fetchone()[0] == 37


def test_iso27001_technological_count():
    """Technological theme should have exactly 34 controls."""
    conn = make_seed_db()
    cur = conn.execute(
        "SELECT COUNT(*) FROM standard_controls "
        "WHERE standard_code='ISO/IEC 27001' AND theme='Technological'"
    )
    assert cur.fetchone()[0] == 34
