"""
tests/test_review_mappings.py

Unit tests for scripts/maintenance/review_mappings.py.

Run:
    cd dokumentacja
    python3 -m pytest tests/test_review_mappings.py -v --tb=short
"""

import sqlite3

import pytest

from scripts.maintenance.review_mappings import (
    export_pending,
    import_reviewed,
    stats,
)

pytestmark = pytest.mark.unit

# ---------------------------------------------------------------------------
# Fixture
# ---------------------------------------------------------------------------


@pytest.fixture
def conn():
    c = sqlite3.connect(":memory:")
    c.executescript("""
    CREATE TABLE doc_standard_mapping (
        id INTEGER PRIMARY KEY,
        doc_path TEXT, standard_code TEXT,
        match_reason TEXT, confidence REAL, evidence TEXT
    );
    INSERT INTO doc_standard_mapping VALUES (1,'core/a.md','ISO/IEC 27001','keyword_match_scored',0.25,'tokens: security');
    INSERT INTO doc_standard_mapping VALUES (2,'core/b.md','NIST CSF','keyword_match_scored',0.15,'tokens: ');
    INSERT INTO doc_standard_mapping VALUES (3,'core/c.md','ISO/IEC 27001','explicit_audit',0.95,'expert verified');
    INSERT INTO doc_standard_mapping VALUES (4,'core/d.md','ISO/IEC 27001','keyword_match_scored',0.50,'tokens: ok');
    """)
    c.commit()
    return c


# ---------------------------------------------------------------------------
# 1. export_pending returns only low-confidence rows
# ---------------------------------------------------------------------------


def test_export_pending_returns_low_confidence(conn):
    rows = export_pending(conn, threshold=0.6)
    ids = {r["id"] for r in rows}
    # rows 1 (0.25), 2 (0.15), 4 (0.50) are below 0.6 and not audited
    assert 1 in ids
    assert 2 in ids
    assert 4 in ids


# ---------------------------------------------------------------------------
# 2. export_pending excludes explicit_audit rows
# ---------------------------------------------------------------------------


def test_export_pending_excludes_explicit_audit(conn):
    rows = export_pending(conn, threshold=1.0)  # high threshold → catches all
    ids = {r["id"] for r in rows}
    assert 3 not in ids, "explicit_audit row should be excluded"


# ---------------------------------------------------------------------------
# 3. threshold filter: only rows 1 and 2 (conf < 0.3)
# ---------------------------------------------------------------------------


def test_export_threshold_filter(conn):
    rows = export_pending(conn, threshold=0.3)
    ids = {r["id"] for r in rows}
    assert 1 in ids  # 0.25 < 0.3
    assert 2 in ids  # 0.15 < 0.3
    assert 4 not in ids  # 0.50 >= 0.3
    assert 3 not in ids  # explicit_audit excluded regardless


# ---------------------------------------------------------------------------
# 4. standard filter: only row 2 (NIST CSF)
# ---------------------------------------------------------------------------


def test_export_standard_filter(conn):
    rows = export_pending(conn, threshold=1.0, standard="NIST CSF")
    assert len(rows) == 1
    assert rows[0]["id"] == 2
    assert rows[0]["standard_code"] == "NIST CSF"


# ---------------------------------------------------------------------------
# 5. approved=yes updates match_reason to 'expert_reviewed'
# ---------------------------------------------------------------------------


def test_import_approved_updates_match_reason(conn):
    rows = [{"id": 1, "approved": "yes", "confidence": 0.25, "notes": "looks good"}]
    import_reviewed(conn, rows, dry_run=False)
    row = conn.execute("SELECT match_reason FROM doc_standard_mapping WHERE id=1").fetchone()
    assert row[0] == "expert_reviewed"


# ---------------------------------------------------------------------------
# 6. approved=yes with original conf=0.25 → confidence becomes 0.8
# ---------------------------------------------------------------------------


def test_import_approved_sets_min_confidence_08(conn):
    rows = [{"id": 1, "approved": "yes", "confidence": 0.25, "notes": ""}]
    import_reviewed(conn, rows, dry_run=False)
    row = conn.execute("SELECT confidence FROM doc_standard_mapping WHERE id=1").fetchone()
    assert row[0] == pytest.approx(0.8)


# ---------------------------------------------------------------------------
# 7. approved=no deletes row from DB
# ---------------------------------------------------------------------------


def test_import_rejected_deletes_row(conn):
    rows = [{"id": 2, "approved": "no", "confidence": 0.15, "notes": "false positive"}]
    import_reviewed(conn, rows, dry_run=False, keep_rejected=False)
    row = conn.execute("SELECT id FROM doc_standard_mapping WHERE id=2").fetchone()
    assert row is None, "Row should have been deleted"


# ---------------------------------------------------------------------------
# 8. approved='' (empty) → no change
# ---------------------------------------------------------------------------


def test_import_skipped_no_change(conn):
    rows = [{"id": 1, "approved": "", "confidence": 0.25, "notes": ""}]
    counts = import_reviewed(conn, rows, dry_run=False)
    assert counts["skipped"] == 1
    row = conn.execute(
        "SELECT match_reason, confidence FROM doc_standard_mapping WHERE id=1"
    ).fetchone()
    assert row[0] == "keyword_match_scored"
    assert row[1] == pytest.approx(0.25)


# ---------------------------------------------------------------------------
# 9. dry_run=True → no DB changes
# ---------------------------------------------------------------------------


def test_import_dry_run_no_changes(conn):
    rows = [
        {"id": 1, "approved": "yes", "confidence": 0.25, "notes": "great"},
        {"id": 2, "approved": "no", "confidence": 0.15, "notes": "bad"},
    ]
    counts = import_reviewed(conn, rows, dry_run=True)
    assert counts["approved"] == 1
    assert counts["rejected"] == 1

    # DB must be unchanged
    row1 = conn.execute(
        "SELECT match_reason, confidence FROM doc_standard_mapping WHERE id=1"
    ).fetchone()
    assert row1[0] == "keyword_match_scored"
    assert row1[1] == pytest.approx(0.25)

    row2 = conn.execute("SELECT id FROM doc_standard_mapping WHERE id=2").fetchone()
    assert row2 is not None, "Row 2 should still exist after dry run"


# ---------------------------------------------------------------------------
# 10. stats() returns dict with required keys
# ---------------------------------------------------------------------------


def test_stats_returns_dict_with_keys(conn):
    s = stats(conn)
    assert isinstance(s, dict)
    assert "total" in s
    assert "by_reason" in s
    assert "by_confidence_tier" in s
    assert "pending_review" in s

    assert s["total"] == 4
    assert isinstance(s["by_reason"], dict)
    assert isinstance(s["by_confidence_tier"], dict)
    assert isinstance(s["pending_review"], int)

    # Fixture has 2 rows below 0.4 that are not audited (rows 1 and 2)
    assert s["pending_review"] == 2


# ---------------------------------------------------------------------------
# 11. keep_rejected flag → UPDATE instead of DELETE
# ---------------------------------------------------------------------------


def test_keep_rejected_flag(conn):
    rows = [{"id": 2, "approved": "no", "confidence": 0.15, "notes": "bad match"}]
    import_reviewed(conn, rows, dry_run=False, keep_rejected=True)
    row = conn.execute(
        "SELECT match_reason, confidence FROM doc_standard_mapping WHERE id=2"
    ).fetchone()
    assert row is not None, "Row should NOT be deleted when keep_rejected=True"
    assert row[0] == "rejected"
    assert row[1] == pytest.approx(0.0)
