"""Tests for scripts/maintenance/changelog_tracker.py."""
import pytest
import sqlite3
import json
import sys
from pathlib import Path
from argparse import Namespace
from io import StringIO
import contextlib

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.maintenance.changelog_tracker import ensure_table, cmd_list, cmd_stats, cmd_export

pytestmark = pytest.mark.unit


@pytest.fixture
def mem_conn():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    return conn


@pytest.fixture
def populated_conn(mem_conn):
    ensure_table(mem_conn)
    mem_conn.executemany(
        "INSERT INTO template_changelog (template_path, changed_at, change_type, change_reason, diff_summary, patch_args) VALUES (?,?,?,?,?,?)",
        [
            ("core/security_policy.md", "2026-03-01T10:00:00", "bulk_patch", "Reason A", "Added section", None),
            ("core/access_control.md", "2026-03-02T11:00:00", "regulation_update", "Reason B", "Updated regulation ref", None),
            ("core/security_policy.md", "2026-03-03T12:00:00", "bulk_patch", "Reason C", "Modified intro", None),
            ("docs/incident_response.md", "2026-02-15T09:00:00", "inject_aspirational", "Reason D", "Injected section", None),
        ]
    )
    mem_conn.commit()
    return mem_conn


class TestEnsureTable:
    def test_creates_table(self, mem_conn):
        ensure_table(mem_conn)
        cur = mem_conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='template_changelog'")
        assert cur.fetchone() is not None

    def test_idempotent(self, mem_conn):
        ensure_table(mem_conn)
        ensure_table(mem_conn)  # should not raise
        cur = mem_conn.execute("SELECT COUNT(*) FROM template_changelog")
        assert cur.fetchone()[0] == 0

    def test_table_has_required_columns(self, mem_conn):
        ensure_table(mem_conn)
        cur = mem_conn.execute("PRAGMA table_info(template_changelog)")
        cols = {row[1] for row in cur.fetchall()}
        assert {"id", "template_path", "changed_at", "change_type"}.issubset(cols)


class TestCmdList:
    def test_list_all(self, populated_conn, capsys):
        args = Namespace(template=None, since=None, type=None, limit=50, output="table")
        cmd_list(populated_conn, args)
        out = capsys.readouterr().out
        assert "security_policy" in out
        assert "access_control" in out

    def test_list_filter_by_template(self, populated_conn, capsys):
        args = Namespace(template="security_policy", since=None, type=None, limit=50, output="table")
        cmd_list(populated_conn, args)
        out = capsys.readouterr().out
        assert "security_policy" in out
        assert "access_control" not in out

    def test_list_filter_by_type(self, populated_conn, capsys):
        args = Namespace(template=None, since=None, type="bulk_patch", limit=50, output="table")
        cmd_list(populated_conn, args)
        out = capsys.readouterr().out
        assert "bulk_patch" in out

    def test_list_filter_by_since(self, populated_conn, capsys):
        args = Namespace(template=None, since="2026-03-01", type=None, limit=50, output="table")
        cmd_list(populated_conn, args)
        out = capsys.readouterr().out
        assert "2026-03" in out

    def test_list_json_output(self, populated_conn, capsys):
        args = Namespace(template=None, since=None, type=None, limit=50, output="json")
        cmd_list(populated_conn, args)
        out = capsys.readouterr().out
        data = json.loads(out)
        assert isinstance(data, list)
        assert len(data) > 0

    def test_list_empty_result(self, populated_conn, capsys):
        args = Namespace(template="nonexistent_file_xyz", since=None, type=None, limit=50, output="table")
        cmd_list(populated_conn, args)
        out = capsys.readouterr().out
        assert "Brak" in out or len(out.strip()) > 0

    def test_list_with_limit(self, populated_conn, capsys):
        args = Namespace(template=None, since=None, type=None, limit=1, output="json")
        cmd_list(populated_conn, args)
        out = capsys.readouterr().out
        data = json.loads(out)
        assert len(data) == 1


class TestCmdStats:
    def test_stats_shows_total(self, populated_conn, capsys):
        args = Namespace()
        cmd_stats(populated_conn, args)
        out = capsys.readouterr().out
        assert "4" in out  # 4 total entries

    def test_stats_shows_change_types(self, populated_conn, capsys):
        args = Namespace()
        cmd_stats(populated_conn, args)
        out = capsys.readouterr().out
        assert "bulk_patch" in out

    def test_stats_on_empty_table(self, mem_conn, capsys):
        ensure_table(mem_conn)
        args = Namespace()
        cmd_stats(mem_conn, args)
        out = capsys.readouterr().out
        assert "0" in out


class TestCmdExport:
    def test_export_stdout(self, populated_conn, capsys):
        args = Namespace(save=None)
        cmd_export(populated_conn, args)
        out = capsys.readouterr().out
        data = json.loads(out)
        assert isinstance(data, list)
        assert len(data) == 4

    def test_export_to_file(self, populated_conn, tmp_path, capsys):
        out_file = tmp_path / "changelog.json"
        args = Namespace(save=str(out_file))
        cmd_export(populated_conn, args)
        assert out_file.exists()
        data = json.loads(out_file.read_text())
        assert isinstance(data, list)
        assert len(data) == 4

    def test_export_empty(self, mem_conn, capsys):
        ensure_table(mem_conn)
        args = Namespace(save=None)
        cmd_export(mem_conn, args)
        out = capsys.readouterr().out
        data = json.loads(out)
        assert data == []
