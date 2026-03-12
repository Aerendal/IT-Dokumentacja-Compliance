"""Tests for pure helper functions in scripts/maintenance/interactive_audit.py."""

import sqlite3
import sys

from scripts.maintenance.interactive_audit import (
    ANSI_GREEN,
    ANSI_RED,
    ANSI_RESET,
    VALID_CONFIDENCE,
    VALID_REASONS,
    _colored,
    _progress_bar,
    build_filter_query,
    format_preview,
    parse_keypress,
)

# ---------------------------------------------------------------------------
# parse_keypress
# ---------------------------------------------------------------------------


class TestParseKeypress:
    def test_y_confirm(self):
        assert parse_keypress("y") == "confirm"

    def test_n_delete(self):
        assert parse_keypress("n") == "delete"

    def test_s_skip(self):
        assert parse_keypress("s") == "skip"

    def test_o_open(self):
        assert parse_keypress("o") == "open"

    def test_q_quit(self):
        assert parse_keypress("q") == "quit"

    def test_uppercase_y(self):
        assert parse_keypress("Y") == "confirm"

    def test_uppercase_q(self):
        assert parse_keypress("Q") == "quit"

    def test_unknown_key(self):
        assert parse_keypress("x") == "invalid"

    def test_empty_string(self):
        assert parse_keypress("") == "invalid"

    def test_whitespace_stripped(self):
        assert parse_keypress(" y ") == "confirm"

    def test_number_invalid(self):
        assert parse_keypress("1") == "invalid"

    def test_special_char_invalid(self):
        assert parse_keypress("!") == "invalid"


# ---------------------------------------------------------------------------
# _progress_bar
# ---------------------------------------------------------------------------


class TestProgressBar:
    def test_zero_total(self):
        assert _progress_bar(0, 0) == "[brak wpisow]"

    def test_full_progress(self):
        bar = _progress_bar(10, 10)
        assert "100%" in bar
        assert "10/10" in bar

    def test_half_progress(self):
        bar = _progress_bar(5, 10)
        assert "50%" in bar
        assert "5/10" in bar

    def test_zero_current(self):
        bar = _progress_bar(0, 10)
        assert "0%" in bar
        assert "0/10" in bar

    def test_format_contains_brackets(self):
        bar = _progress_bar(3, 10)
        assert bar.startswith("[")
        assert "]" in bar

    def test_custom_width(self):
        bar = _progress_bar(5, 10, width=20)
        assert "5/10" in bar

    def test_one_of_one(self):
        bar = _progress_bar(1, 1)
        assert "100%" in bar


# ---------------------------------------------------------------------------
# _colored
# ---------------------------------------------------------------------------


class TestColored:
    def test_non_tty_returns_plain_text(self, monkeypatch):
        monkeypatch.setattr(sys.stdout, "isatty", lambda: False)
        result = _colored("hello", ANSI_GREEN)
        assert result == "hello"

    def test_tty_returns_colored(self, monkeypatch):
        monkeypatch.setattr(sys.stdout, "isatty", lambda: True)
        result = _colored("hello", ANSI_GREEN)
        assert ANSI_GREEN in result
        assert "hello" in result
        assert ANSI_RESET in result

    def test_empty_text_non_tty(self, monkeypatch):
        monkeypatch.setattr(sys.stdout, "isatty", lambda: False)
        assert _colored("", ANSI_RED) == ""


# ---------------------------------------------------------------------------
# format_preview
# ---------------------------------------------------------------------------


class TestFormatPreview:
    def test_basic_output_contains_path(self):
        result = format_preview("docs/policy.md", "ISO27001", "keyword_match", "Policy Document")
        assert "docs/policy.md" in result

    def test_output_contains_standard(self):
        result = format_preview("docs/policy.md", "ISO27001", "keyword_match", None)
        assert "ISO27001" in result

    def test_output_contains_reason(self):
        result = format_preview("docs/policy.md", "ISO27001", "keyword_match", None)
        assert "keyword_match" in result

    def test_title_included_when_provided(self):
        result = format_preview("docs/policy.md", "ISO27001", "explicit_audit", "My Title")
        assert "My Title" in result

    def test_title_absent_when_none(self):
        result = format_preview("docs/policy.md", "ISO27001", "keyword_match", None)
        # Should not crash, just no title line
        assert "ISO27001" in result

    def test_multiline_output(self):
        result = format_preview("docs/policy.md", "ISO27001", "keyword_match", "Title")
        assert "\n" in result

    def test_all_valid_reasons(self):
        for reason in VALID_REASONS:
            result = format_preview("path.md", "STD", reason, None)
            assert reason in result


# ---------------------------------------------------------------------------
# build_filter_query
# ---------------------------------------------------------------------------


class TestBuildFilterQuery:
    def test_no_filters(self):
        sql, params = build_filter_query(None, None, 50)
        assert "SELECT" in sql
        assert params == [50]
        assert "WHERE" not in sql

    def test_standard_filter(self):
        sql, params = build_filter_query("ISO27001", None, 20)
        assert "WHERE" in sql
        assert "standard_code" in sql.lower() or "standard" in sql.lower()
        assert "%ISO27001%" in params
        assert 20 in params

    def test_reason_filter(self):
        sql, params = build_filter_query(None, "keyword_match", 10)
        assert "WHERE" in sql
        assert "keyword_match" in params
        assert 10 in params

    def test_both_filters(self):
        sql, params = build_filter_query("GDPR", "explicit_audit", 5)
        assert "WHERE" in sql
        assert "%GDPR%" in params
        assert "explicit_audit" in params
        assert 5 in params

    def test_returns_tuple(self):
        result = build_filter_query(None, None, 100)
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_limit_always_appended(self):
        _, params = build_filter_query(None, None, 99)
        assert params[-1] == 99

    def test_sql_has_order_by(self):
        sql, _ = build_filter_query(None, None, 10)
        assert "ORDER BY" in sql.upper()

    def test_sql_has_limit(self):
        sql, _ = build_filter_query(None, None, 10)
        assert "LIMIT" in sql.upper()

    def test_query_executable_on_inmemory_db(self):
        """The generated query must run without syntax errors on a compatible schema."""
        conn = sqlite3.connect(":memory:")
        conn.execute("""
            CREATE TABLE doc_standard_mapping (
                id INTEGER PRIMARY KEY,
                doc_path TEXT,
                standard_code TEXT,
                match_reason TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE gap_analysis (
                matched_doc_path TEXT,
                standard_code TEXT,
                matched_doc_title TEXT
            )
        """)
        sql, params = build_filter_query(None, None, 10)
        rows = conn.execute(sql, params).fetchall()
        assert rows == []


# ---------------------------------------------------------------------------
# VALID_CONFIDENCE / VALID_REASONS constants
# ---------------------------------------------------------------------------


class TestConstants:
    def test_valid_confidence_contains_expected(self):
        assert "exact" in VALID_CONFIDENCE
        assert "high" in VALID_CONFIDENCE
        assert "medium" in VALID_CONFIDENCE
        assert "low" in VALID_CONFIDENCE

    def test_valid_reasons_contains_expected(self):
        assert "keyword_match" in VALID_REASONS
        assert "explicit_audit" in VALID_REASONS
