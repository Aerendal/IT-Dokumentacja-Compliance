"""Tests for scripts/generate_audit_report.py — run() function with in-memory DB."""
import sqlite3
import pytest

from scripts.generate_audit_report import run


def _make_full_db(
    docs=None,
    standards=None,
    standards_catalog=None,
    gap_analysis=None,
    doc_standard_mapping=None,
):
    """Build an in-memory SQLite DB with the schema expected by run()."""
    conn = sqlite3.connect(":memory:")

    conn.execute("""
        CREATE TABLE docs (
            path TEXT,
            title TEXT,
            doc_uid TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE standards (
            code TEXT PRIMARY KEY,
            name TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE standards_catalog (
            id INTEGER PRIMARY KEY,
            standard_code TEXT,
            doc_title TEXT,
            catalog_category TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE gap_analysis (
            id INTEGER PRIMARY KEY,
            standard_code TEXT,
            doc_title TEXT,
            matched_doc_title TEXT,
            matched_doc_path TEXT,
            status TEXT,
            is_required INTEGER,
            confidence TEXT,
            catalog_category TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE doc_standard_mapping (
            id INTEGER PRIMARY KEY,
            doc_path TEXT,
            standard_code TEXT,
            match_reason TEXT
        )
    """)

    if docs:
        conn.executemany("INSERT INTO docs VALUES (?,?,?)", docs)
    if standards:
        conn.executemany("INSERT INTO standards VALUES (?,?)", standards)
    if standards_catalog:
        conn.executemany("INSERT INTO standards_catalog VALUES (?,?,?,?)", standards_catalog)
    if gap_analysis:
        conn.executemany(
            "INSERT INTO gap_analysis VALUES (?,?,?,?,?,?,?,?,?)", gap_analysis
        )
    if doc_standard_mapping:
        conn.executemany(
            "INSERT INTO doc_standard_mapping VALUES (?,?,?,?)", doc_standard_mapping
        )

    conn.commit()
    return conn


def _empty_db():
    return _make_full_db()


# ---------------------------------------------------------------------------
# Basic return type and structure
# ---------------------------------------------------------------------------

class TestRunReturnType:
    def test_returns_string(self):
        conn = _empty_db()
        result = run(conn)
        assert isinstance(result, str)

    def test_result_not_empty(self):
        conn = _empty_db()
        result = run(conn)
        assert len(result) > 0

    def test_contains_markdown_header(self):
        conn = _empty_db()
        result = run(conn)
        assert "# Raport Audytu" in result

    def test_contains_section_1(self):
        conn = _empty_db()
        result = run(conn)
        assert "## 1." in result

    def test_contains_section_2(self):
        conn = _empty_db()
        result = run(conn)
        assert "## 2." in result

    def test_contains_section_5(self):
        conn = _empty_db()
        result = run(conn)
        assert "## 5." in result


# ---------------------------------------------------------------------------
# Coverage percentage calculation
# ---------------------------------------------------------------------------

class TestCoverageCalculation:
    def test_zero_catalog_zero_coverage(self):
        conn = _empty_db()
        result = run(conn)
        assert "0%" in result

    def test_100_percent_coverage(self):
        conn = _make_full_db(
            standards_catalog=[(1, "ISO27001", "Policy", "governance")],
            gap_analysis=[(1, "ISO27001", "Policy", "policy.md", "docs/policy.md", "present", 0, "exact", "governance")],
        )
        result = run(conn)
        assert "100.0%" in result

    def test_partial_coverage(self):
        conn = _make_full_db(
            standards_catalog=[
                (1, "ISO27001", "Policy", "governance"),
                (2, "ISO27001", "Procedure", "governance"),
            ],
            gap_analysis=[
                (1, "ISO27001", "Policy", "policy.md", "docs/policy.md", "present", 0, "exact", "governance"),
                (2, "ISO27001", "Procedure", None, None, "missing", 1, None, "governance"),
            ],
        )
        result = run(conn)
        assert "50.0%" in result


# ---------------------------------------------------------------------------
# Missing templates section
# ---------------------------------------------------------------------------

class TestMissingSection:
    def test_no_missing_shows_checkmark(self):
        conn = _empty_db()
        result = run(conn)
        assert "Brak brakujących" in result or "✅" in result

    def test_missing_required_shown(self):
        conn = _make_full_db(
            gap_analysis=[
                (1, "ISO27001", "Missing Doc", None, None, "missing", 1, None, "governance"),
            ],
        )
        result = run(conn)
        assert "Missing Doc" in result
        assert "REQUIRED" in result

    def test_missing_recommended_shown(self):
        conn = _make_full_db(
            gap_analysis=[
                (1, "ISO27001", "Recommended Doc", None, None, "missing", 0, None, "ops"),
            ],
        )
        result = run(conn)
        assert "Recommended Doc" in result
        assert "recommended" in result


# ---------------------------------------------------------------------------
# Extra docs section
# ---------------------------------------------------------------------------

class TestExtraDocsSection:
    def test_extra_doc_listed(self):
        conn = _make_full_db(
            docs=[("docs/extra.md", "Extra Doc", "uid-extra")],
        )
        result = run(conn)
        assert "Extra Doc" in result

    def test_orphan_excluded(self):
        conn = _make_full_db(
            docs=[("ORPHAN", "Orphan Doc", "uid-orphan")],
        )
        result = run(conn)
        # ORPHAN path should not count in extra
        assert "0 szablonów" in result or "Łącznie: 0" in result

    def test_mapped_doc_not_extra(self):
        conn = _make_full_db(
            docs=[("docs/policy.md", "Policy Doc", "uid-1")],
            doc_standard_mapping=[(1, "docs/policy.md", "ISO27001", "keyword_match")],
        )
        result = run(conn)
        assert "0 szablonów" in result or "Łącznie: 0" in result


# ---------------------------------------------------------------------------
# Low-confidence rows
# ---------------------------------------------------------------------------

class TestLowConfidenceSection:
    def test_low_confidence_row_shown(self):
        conn = _make_full_db(
            gap_analysis=[
                (1, "GDPR", "Privacy Policy", "Privacy Procedures", "docs/priv.md", "present", 0, "low", "legal"),
            ],
        )
        result = run(conn)
        assert "GDPR" in result

    def test_no_low_confidence_empty_table(self):
        conn = _empty_db()
        result = run(conn)
        # Section header still present
        assert "## 4." in result


# ---------------------------------------------------------------------------
# Summary per-standard section
# ---------------------------------------------------------------------------

class TestSummarySection:
    def test_ok_status_when_no_missing(self):
        conn = _make_full_db(
            standards_catalog=[(1, "ISO27001", "Policy", "gov")],
            gap_analysis=[
                (1, "ISO27001", "Policy", "policy.md", "docs/p.md", "present", 0, "exact", "gov"),
            ],
        )
        result = run(conn)
        assert "✅ OK" in result

    def test_warning_status_when_missing(self):
        conn = _make_full_db(
            standards_catalog=[(1, "ISO27001", "Policy", "gov")],
            gap_analysis=[
                (1, "ISO27001", "Policy", None, None, "missing", 1, None, "gov"),
            ],
        )
        result = run(conn)
        assert "⚠️ LUKI" in result

    def test_multiple_standards_in_summary(self):
        conn = _make_full_db(
            standards_catalog=[
                (1, "ISO27001", "Policy", "gov"),
                (2, "GDPR", "Privacy", "legal"),
            ],
            gap_analysis=[
                (1, "ISO27001", "Policy", "pol.md", "docs/pol.md", "present", 0, "exact", "gov"),
                (2, "GDPR", "Privacy", "priv.md", "docs/priv.md", "present", 0, "high", "legal"),
            ],
        )
        result = run(conn)
        assert "ISO27001" in result
        assert "GDPR" in result
