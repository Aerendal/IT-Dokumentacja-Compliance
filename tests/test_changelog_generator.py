"""
tests/test_changelog_generator.py — unit tests for scripts/maintenance/changelog_generator.py
All tests use in-memory SQLite and no real Git calls.
"""
import json
import sqlite3
import pytest
from pathlib import Path
from datetime import datetime

from scripts.maintenance.changelog_generator import (
    parse_git_log,
    group_into_sessions,
    format_date_range,
    render_markdown,
    render_json,
    render_csv,
    fetch_changelog_rows,
    STATUS_LABELS,
)

pytestmark = pytest.mark.unit


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SAMPLE_GIT_LOG = """\
COMMIT|abc123def456|2026-03-15|Add auth policy|Alice
M\tcore/auth_policy.md
A\tcore/new_template.md
COMMIT|111222333444|2026-03-14|Update GDPR notice|Bob
M\tcore/gdpr_notice.md
D\tcore/old_doc.md
COMMIT|aabbccdd1234|2026-01-10|Rename incident file|Charlie
R100\told_name.md\tnew_name.md
"""

SAMPLE_CHANGELOG_ROWS = [
    {
        "template_path": "core/auth_policy.md",
        "changed_at": "2026-03-15T10:00:00",
        "change_type": "mapping_add",
        "change_reason": "standard=ISO27001",
    },
    {
        "template_path": "core/gdpr_notice.md",
        "changed_at": "2026-03-14T09:00:00",
        "change_type": "mapping_add",
        "change_reason": "regulation=GDPR",
    },
]


@pytest.fixture
def db_with_changelog(tmp_path):
    """Create a SQLite DB with template_changelog data."""
    db = tmp_path / "test.db"
    conn = sqlite3.connect(str(db))
    conn.execute("""
        CREATE TABLE template_changelog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            template_path TEXT,
            changed_at TEXT,
            change_type TEXT,
            change_reason TEXT
        )
    """)
    conn.executemany(
        "INSERT INTO template_changelog (template_path, changed_at, change_type, change_reason) VALUES (?,?,?,?)",
        [
            ("core/auth.md",  "2026-03-15T10:00:00", "mapping_add",    "standard=ISO27001"),
            ("core/gdpr.md",  "2026-03-14T09:00:00", "mapping_add",    "regulation=GDPR"),
            ("core/nis2.md",  "2026-01-05T08:00:00", "mapping_remove", "standard=NIS2"),
        ],
    )
    conn.commit()
    conn.close()
    return str(db)


# ---------------------------------------------------------------------------
# parse_git_log
# ---------------------------------------------------------------------------

class TestParseGitLog:
    def test_returns_list_of_commits(self):
        commits = parse_git_log(SAMPLE_GIT_LOG)
        assert isinstance(commits, list)
        assert len(commits) == 3

    def test_commit_fields_present(self):
        commits = parse_git_log(SAMPLE_GIT_LOG)
        c = commits[0]
        assert c["hash"] == "abc123def456"
        assert c["date"] == "2026-03-15"
        assert c["subject"] == "Add auth policy"
        assert c["author"] == "Alice"

    def test_files_parsed(self):
        commits = parse_git_log(SAMPLE_GIT_LOG)
        files = commits[0]["files"]
        assert len(files) == 2
        statuses = [f["status"] for f in files]
        assert "M" in statuses
        assert "A" in statuses

    def test_rename_parsed_correctly(self):
        commits = parse_git_log(SAMPLE_GIT_LOG)
        rename_commit = commits[2]
        assert rename_commit["files"][0]["status"] == "R"
        assert rename_commit["files"][0]["old_path"] == "old_name.md"
        assert rename_commit["files"][0]["path"] == "new_name.md"

    def test_empty_string_returns_empty_list(self):
        assert parse_git_log("") == []

    def test_deleted_file_status(self):
        commits = parse_git_log(SAMPLE_GIT_LOG)
        files_2 = commits[1]["files"]
        statuses = [f["status"] for f in files_2]
        assert "D" in statuses


# ---------------------------------------------------------------------------
# group_into_sessions
# ---------------------------------------------------------------------------

class TestGroupIntoSessions:
    def _make_commit(self, date):
        return {"hash": "aaa", "date": date, "subject": "x", "author": "X", "files": []}

    def test_empty_returns_empty(self):
        assert group_into_sessions([]) == []

    def test_single_commit_one_session(self):
        commits = [self._make_commit("2026-03-15")]
        sessions = group_into_sessions(commits)
        assert len(sessions) == 1
        assert len(sessions[0]) == 1

    def test_same_day_same_session(self):
        commits = [
            self._make_commit("2026-03-15"),
            self._make_commit("2026-03-15"),
        ]
        sessions = group_into_sessions(commits, gap_minutes=60)
        assert len(sessions) == 1

    def test_different_days_different_sessions(self):
        commits = [
            self._make_commit("2026-03-15"),
            self._make_commit("2026-01-01"),
        ]
        sessions = group_into_sessions(commits, gap_minutes=60)
        assert len(sessions) == 2

    def test_preserves_commit_order(self):
        commits = [self._make_commit("2026-03-15"), self._make_commit("2026-03-14")]
        sessions = group_into_sessions(commits)
        assert sessions[0][0]["date"] == "2026-03-15"


# ---------------------------------------------------------------------------
# format_date_range
# ---------------------------------------------------------------------------

class TestFormatDateRange:
    def test_both_dates(self):
        result = format_date_range("2026-01-01", "2026-03-31")
        assert "2026-01-01" in result
        assert "2026-03-31" in result

    def test_only_since(self):
        result = format_date_range("2026-01-01", None)
        assert "2026-01-01" in result
        assert "None" not in result

    def test_only_until(self):
        result = format_date_range(None, "2026-03-31")
        assert "2026-03-31" in result

    def test_neither_returns_string(self):
        result = format_date_range(None, None)
        assert isinstance(result, str)
        assert len(result) > 0


# ---------------------------------------------------------------------------
# render_markdown
# ---------------------------------------------------------------------------

class TestRenderMarkdown:
    def test_contains_header(self):
        md = render_markdown([], [])
        assert "# Raport" in md

    def test_empty_shows_no_changes(self):
        md = render_markdown([], [])
        assert "Brak zmian" in md

    def test_sessions_appear_in_output(self):
        commits = parse_git_log(SAMPLE_GIT_LOG)
        sessions = group_into_sessions(commits)
        md = render_markdown(sessions, [])
        assert "Add auth policy" in md
        assert "Alice" in md

    def test_changelog_rows_appear_in_table(self):
        md = render_markdown([], SAMPLE_CHANGELOG_ROWS)
        assert "auth_policy.md" in md
        assert "ISO27001" in md

    def test_rename_shown_in_output(self):
        commits = parse_git_log(SAMPLE_GIT_LOG)
        sessions = group_into_sessions(commits)
        md = render_markdown(sessions, [])
        assert "old_name.md" in md or "new_name.md" in md


# ---------------------------------------------------------------------------
# render_json
# ---------------------------------------------------------------------------

class TestRenderJson:
    def test_valid_json(self):
        commits = parse_git_log(SAMPLE_GIT_LOG)
        sessions = group_into_sessions(commits)
        output = render_json(sessions, SAMPLE_CHANGELOG_ROWS)
        data = json.loads(output)
        assert isinstance(data, dict)

    def test_contains_sessions_count(self):
        commits = parse_git_log(SAMPLE_GIT_LOG)
        sessions = group_into_sessions(commits)
        data = json.loads(render_json(sessions, []))
        assert data["sessions_count"] == len(sessions)

    def test_contains_changelog_rows(self):
        data = json.loads(render_json([], SAMPLE_CHANGELOG_ROWS))
        assert data["changelog_rows_count"] == len(SAMPLE_CHANGELOG_ROWS)

    def test_generated_at_present(self):
        data = json.loads(render_json([], []))
        assert "generated_at" in data


# ---------------------------------------------------------------------------
# render_csv
# ---------------------------------------------------------------------------

class TestRenderCsv:
    def test_returns_string(self):
        output = render_csv([], [])
        assert isinstance(output, str)

    def test_git_rows_in_csv(self):
        commits = parse_git_log(SAMPLE_GIT_LOG)
        sessions = group_into_sessions(commits)
        output = render_csv(sessions, [])
        assert "core/auth_policy.md" in output

    def test_changelog_rows_in_csv(self):
        output = render_csv([], SAMPLE_CHANGELOG_ROWS)
        assert "template_changelog" in output
        assert "auth_policy.md" in output


# ---------------------------------------------------------------------------
# fetch_changelog_rows
# ---------------------------------------------------------------------------

class TestFetchChangelogRows:
    def test_returns_all_rows(self, db_with_changelog):
        rows = fetch_changelog_rows(db_with_changelog)
        assert len(rows) == 3

    def test_filter_by_since(self, db_with_changelog):
        rows = fetch_changelog_rows(db_with_changelog, since="2026-03-01")
        assert all(r["changed_at"] >= "2026-03-01" for r in rows)
        assert len(rows) == 2

    def test_filter_by_until(self, db_with_changelog):
        rows = fetch_changelog_rows(db_with_changelog, until="2026-01-31")
        assert len(rows) == 1

    def test_nonexistent_db_returns_empty(self, tmp_path):
        rows = fetch_changelog_rows(str(tmp_path / "missing.db"))
        assert rows == []

    def test_rows_are_dicts(self, db_with_changelog):
        rows = fetch_changelog_rows(db_with_changelog)
        for r in rows:
            assert isinstance(r, dict)
            assert "template_path" in r
