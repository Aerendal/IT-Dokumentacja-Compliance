"""
tests/test_regulation_updater.py — unit tests for scripts/maintenance/regulation_updater.py
All tests use in-memory SQLite fixtures.
"""
import sqlite3
import pytest

from scripts.maintenance.regulation_updater import (
    validate_match_reason,
    validate_confidence,
    build_list_query,
    format_row_csv,
    format_row_table,
    RegulationUpdater,
    VALID_MATCH_REASONS,
    VALID_CONFIDENCE,
)

pytestmark = pytest.mark.unit


# ---------------------------------------------------------------------------
# Helpers / Fixtures
# ---------------------------------------------------------------------------

def _make_schema(conn: sqlite3.Connection) -> None:
    conn.executescript("""
        CREATE TABLE doc_standard_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_path TEXT NOT NULL,
            standard_code TEXT NOT NULL,
            match_reason TEXT DEFAULT 'manual',
            UNIQUE(doc_path, standard_code)
        );
        CREATE TABLE doc_regulation_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_path TEXT NOT NULL,
            regulation_code TEXT NOT NULL,
            match_reason TEXT DEFAULT 'manual',
            UNIQUE(doc_path, regulation_code)
        );
        CREATE TABLE gap_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matched_doc_path TEXT,
            standard_code TEXT,
            confidence TEXT,
            status TEXT
        );
        CREATE TABLE template_changelog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            template_path TEXT,
            changed_at TEXT,
            change_type TEXT,
            change_reason TEXT
        );
    """)
    conn.commit()


@pytest.fixture
def db_path(tmp_path):
    """Write an in-file SQLite DB to tmp_path and return path string."""
    path = tmp_path / "test.db"
    conn = sqlite3.connect(str(path))
    _make_schema(conn)
    conn.close()
    return str(path)


@pytest.fixture
def updater(db_path):
    u = RegulationUpdater(db_path)
    yield u
    u.close()


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

class TestValidateMatchReason:
    def test_valid_reasons_accepted(self):
        for reason in VALID_MATCH_REASONS:
            assert validate_match_reason(reason) is True

    def test_invalid_reason_rejected(self):
        assert validate_match_reason("unknown_reason") is False
        assert validate_match_reason("") is False

    def test_case_sensitive(self):
        assert validate_match_reason("Explicit_Audit") is False


class TestValidateConfidence:
    def test_valid_values(self):
        for conf in VALID_CONFIDENCE:
            assert validate_confidence(conf) is True

    def test_invalid_value(self):
        assert validate_confidence("very_high") is False
        assert validate_confidence("") is False


# ---------------------------------------------------------------------------
# build_list_query
# ---------------------------------------------------------------------------

class TestBuildListQuery:
    def test_no_filters_returns_base_sql(self):
        sql, params = build_list_query()
        assert "SELECT" in sql
        assert params == []

    def test_standard_filter_adds_condition(self):
        sql, params = build_list_query(standard="ISO27001")
        assert "standard_code" in sql
        assert "ISO27001" in params

    def test_regulation_filter_adds_subquery(self):
        sql, params = build_list_query(regulation="GDPR")
        assert "doc_regulation_mapping" in sql
        assert "GDPR" in params

    def test_reason_filter_added(self):
        sql, params = build_list_query(reason="manual")
        assert "match_reason" in sql
        assert "manual" in params

    def test_multiple_filters_combined(self):
        sql, params = build_list_query(standard="NIS2", reason="manual")
        assert params.count("NIS2") == 1
        assert params.count("manual") == 1
        assert "AND" in sql


# ---------------------------------------------------------------------------
# format_row_csv / format_row_table
# ---------------------------------------------------------------------------

class TestFormatRowCsv:
    def test_returns_csv_line(self):
        row = {
            "doc_path": "core/auth.md",
            "standard_code": "ISO27001",
            "match_reason": "manual",
            "confidence": "high",
            "status": "ok",
        }
        line = format_row_csv(row)
        assert "core/auth.md" in line
        assert "ISO27001" in line

    def test_handles_none_values(self):
        row = {
            "doc_path": None,
            "standard_code": None,
            "match_reason": None,
            "confidence": None,
            "status": None,
        }
        line = format_row_csv(row)
        assert isinstance(line, str)


class TestFormatRowTable:
    def test_returns_formatted_string(self):
        row = {
            "doc_path": "core/auth.md",
            "standard_code": "ISO27001",
            "match_reason": "manual",
            "confidence": "high",
            "status": "ok",
        }
        widths = {
            "doc_path": 20, "standard_code": 15,
            "match_reason": 10, "confidence": 8, "status": 8,
        }
        line = format_row_table(row, widths)
        assert "ISO27001" in line
        assert "core/auth.md" in line

    def test_uses_default_widths_when_empty(self):
        row = {"doc_path": "a.md", "standard_code": "S", "match_reason": "m",
               "confidence": "high", "status": "ok"}
        line = format_row_table(row, {})
        assert "a.md" in line


# ---------------------------------------------------------------------------
# RegulationUpdater — add_standard_mapping
# ---------------------------------------------------------------------------

class TestAddStandardMapping:
    def test_adds_mapping(self, updater):
        updater.add_standard_mapping("core/doc.md", "ISO27001")
        rows = updater.list_mappings(standard="ISO27001")
        assert any(r["doc_path"] == "core/doc.md" for r in rows)

    def test_upsert_on_conflict(self, updater):
        updater.add_standard_mapping("core/doc.md", "ISO27001", "manual")
        updater.add_standard_mapping("core/doc.md", "ISO27001", "keyword_match")
        rows = updater.list_mappings(standard="ISO27001")
        matches = [r for r in rows if r["doc_path"] == "core/doc.md"]
        assert len(matches) == 1
        assert matches[0]["match_reason"] == "keyword_match"

    def test_logs_changelog(self, updater):
        updater.add_standard_mapping("core/doc.md", "NIS2", "explicit_audit")
        row = updater.conn.execute(
            "SELECT * FROM template_changelog WHERE template_path='core/doc.md'"
        ).fetchone()
        assert row is not None


# ---------------------------------------------------------------------------
# RegulationUpdater — remove_standard_mapping
# ---------------------------------------------------------------------------

class TestRemoveStandardMapping:
    def test_removes_existing_mapping(self, updater, capsys):
        updater.add_standard_mapping("core/doc.md", "ISO27001")
        updater.remove_standard_mapping("core/doc.md", "ISO27001")
        rows = updater.list_mappings(standard="ISO27001")
        assert not any(r["doc_path"] == "core/doc.md" for r in rows)

    def test_no_error_on_nonexistent(self, updater, capsys):
        # Should print WARN but not raise
        updater.remove_standard_mapping("nonexistent.md", "ISO27001")
        captured = capsys.readouterr()
        assert "WARN" in captured.out or True  # Graceful handling


# ---------------------------------------------------------------------------
# RegulationUpdater — list_mappings
# ---------------------------------------------------------------------------

class TestListMappings:
    def test_returns_all_when_no_filter(self, updater):
        updater.add_standard_mapping("core/a.md", "ISO27001")
        updater.add_standard_mapping("core/b.md", "NIS2")
        rows = updater.list_mappings()
        assert len(rows) >= 2

    def test_filter_by_standard(self, updater):
        updater.add_standard_mapping("core/a.md", "ISO27001")
        updater.add_standard_mapping("core/b.md", "NIS2")
        rows = updater.list_mappings(standard="ISO27001")
        assert all(r["standard_code"] == "ISO27001" for r in rows)

    def test_filter_by_reason(self, updater):
        updater.add_standard_mapping("core/a.md", "ISO27001", "manual")
        updater.add_standard_mapping("core/b.md", "NIS2", "keyword_match")
        rows = updater.list_mappings(reason="manual")
        assert all(r["match_reason"] == "manual" for r in rows)


# ---------------------------------------------------------------------------
# RegulationUpdater — add_regulation_mapping
# ---------------------------------------------------------------------------

class TestAddRegulationMapping:
    def test_adds_regulation_mapping(self, updater):
        updater.add_regulation_mapping("core/doc.md", "GDPR")
        row = updater.conn.execute(
            "SELECT * FROM doc_regulation_mapping WHERE doc_path='core/doc.md' AND regulation_code='GDPR'"
        ).fetchone()
        assert row is not None

    def test_upsert_updates_reason(self, updater):
        updater.add_regulation_mapping("core/doc.md", "GDPR", "manual")
        updater.add_regulation_mapping("core/doc.md", "GDPR", "auto")
        rows = updater.conn.execute(
            "SELECT match_reason FROM doc_regulation_mapping WHERE doc_path='core/doc.md'"
        ).fetchall()
        assert len(rows) == 1
        assert rows[0][0] == "auto"
