"""tests/test_compliance_check.py

Unit tests for scripts/compliance_check.py.
"""

import sqlite3
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

pytestmark = pytest.mark.unit

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))


class TestGetDbStats:
    def test_returns_dict_with_required_keys(self, tmp_path):
        db = tmp_path / "test.db"
        conn = sqlite3.connect(db)
        conn.executescript("""
            CREATE TABLE doc_standard_mapping (id INTEGER PRIMARY KEY, confidence REAL);
            CREATE TABLE template_violations (id INTEGER PRIMARY KEY, severity TEXT);
            INSERT INTO doc_standard_mapping VALUES (1, 0.5);
            INSERT INTO doc_standard_mapping VALUES (2, NULL);
            INSERT INTO template_violations VALUES (1, 'ERROR');
            INSERT INTO template_violations VALUES (2, 'WARNING');
        """)
        conn.commit()
        conn.close()

        from scripts.compliance_check import get_db_stats

        stats = get_db_stats(db)
        assert "total_mappings" in stats
        assert stats["total_mappings"] == 2
        assert stats["null_confidence"] == 1
        assert stats["error_violations"] == 1

    def test_get_db_stats_null_confidence_count(self, tmp_path):
        db = tmp_path / "test2.db"
        conn = sqlite3.connect(db)
        conn.executescript("""
            CREATE TABLE doc_standard_mapping (id INTEGER PRIMARY KEY, confidence REAL);
            CREATE TABLE template_violations (id INTEGER PRIMARY KEY, severity TEXT);
            INSERT INTO doc_standard_mapping VALUES (1, NULL);
            INSERT INTO doc_standard_mapping VALUES (2, NULL);
            INSERT INTO doc_standard_mapping VALUES (3, 0.9);
        """)
        conn.commit()
        conn.close()

        from scripts.compliance_check import get_db_stats

        stats = get_db_stats(db)
        assert stats["null_confidence"] == 2
        assert stats["total_mappings"] == 3

    def test_get_db_stats_missing_tables_returns_zeros(self, tmp_path):
        db = tmp_path / "empty.db"
        conn = sqlite3.connect(db)
        conn.close()

        from scripts.compliance_check import get_db_stats

        stats = get_db_stats(db)
        assert stats["total_mappings"] == 0
        assert stats["null_confidence"] == 0
        assert stats["error_violations"] == 0
        assert stats["warning_violations"] == 0

    def test_get_db_stats_warning_violations(self, tmp_path):
        db = tmp_path / "warn.db"
        conn = sqlite3.connect(db)
        conn.executescript("""
            CREATE TABLE doc_standard_mapping (id INTEGER PRIMARY KEY, confidence REAL);
            CREATE TABLE template_violations (id INTEGER PRIMARY KEY, severity TEXT);
            INSERT INTO template_violations VALUES (1, 'WARNING');
            INSERT INTO template_violations VALUES (2, 'WARNING');
            INSERT INTO template_violations VALUES (3, 'WARNING');
        """)
        conn.commit()
        conn.close()

        from scripts.compliance_check import get_db_stats

        stats = get_db_stats(db)
        assert stats["warning_violations"] == 3
        assert stats["error_violations"] == 0


class TestRunCheckSchema:
    @patch("subprocess.run")
    def test_calls_validate_script(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="0 violations", stderr="")
        from scripts.compliance_check import run_check_schema

        result = run_check_schema(Path("/fake/db.db"))
        assert mock_run.called
        assert result["exit_code"] == 0

    @patch("subprocess.run")
    def test_strict_mode_passes_flag(self, mock_run):
        mock_run.return_value = MagicMock(returncode=1, stdout="1 ERROR", stderr="")
        from scripts.compliance_check import run_check_schema

        run_check_schema(Path("/fake/db.db"), strict=True)
        call_args = str(mock_run.call_args)
        assert "--strict" in call_args

    @patch("subprocess.run")
    def test_exit_code_from_subprocess(self, mock_run):
        mock_run.return_value = MagicMock(returncode=1, stdout="", stderr="")
        from scripts.compliance_check import run_check_schema

        result = run_check_schema(Path("/fake/db.db"), strict=True)
        assert result["exit_code"] == 1

    @patch("subprocess.run")
    def test_non_strict_no_strict_flag(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
        from scripts.compliance_check import run_check_schema

        run_check_schema(Path("/fake/db.db"), strict=False)
        call_args = str(mock_run.call_args)
        assert "--strict" not in call_args


class TestRunCoverageReport:
    @patch("subprocess.run")
    def test_calls_coverage_script(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
        from scripts.compliance_check import run_coverage_report

        run_coverage_report(Path("/fake/db.db"), fmt="html")
        assert mock_run.called

    @patch("subprocess.run")
    def test_format_passed_to_subprocess(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
        from scripts.compliance_check import run_coverage_report

        run_coverage_report(Path("/fake/db.db"), fmt="json")
        call_args = str(mock_run.call_args)
        assert "json" in call_args

    @patch("subprocess.run")
    def test_exit_code_propagated(self, mock_run):
        mock_run.return_value = MagicMock(returncode=1, stdout="", stderr="")
        from scripts.compliance_check import run_coverage_report

        result = run_coverage_report(Path("/fake/db.db"), fmt="csv")
        assert result["exit_code"] == 1


class TestRunBackfill:
    @patch("subprocess.run")
    def test_backfill_dry_run_default(self, mock_run):
        """When no --apply, passes --dry-run"""
        mock_run.return_value = MagicMock(returncode=0, stdout="0 rows updated", stderr="")
        from scripts.compliance_check import run_backfill

        run_backfill(Path("/fake/db.db"), apply=False)
        call_args = str(mock_run.call_args)
        assert "--dry-run" in call_args
        assert "--apply" not in call_args

    @patch("subprocess.run")
    def test_backfill_apply_passes_apply_flag(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="5 rows updated", stderr="")
        from scripts.compliance_check import run_backfill

        run_backfill(Path("/fake/db.db"), apply=True)
        call_args = str(mock_run.call_args)
        assert "--apply" in call_args


class TestRunFullAudit:
    @patch("scripts.compliance_check.run_check_schema")
    @patch("scripts.compliance_check.run_coverage_report")
    @patch("scripts.compliance_check.run_backfill")
    @patch("scripts.compliance_check.get_db_stats")
    def test_returns_zero_on_success(self, mock_stats, mock_bf, mock_cov, mock_schema):
        mock_stats.return_value = {
            "total_mappings": 100,
            "null_confidence": 0,
            "error_violations": 0,
            "warning_violations": 0,
        }
        mock_schema.return_value = {"violations_error": 0, "violations_warning": 0, "exit_code": 0}
        mock_cov.return_value = {"exit_code": 0, "output_file": "x.html"}
        mock_bf.return_value = {"exit_code": 0, "rows_updated": 0}
        from scripts.compliance_check import run_full_audit

        code = run_full_audit(Path("/fake/db.db"))
        assert code == 0

    @patch("scripts.compliance_check.run_check_schema")
    @patch("scripts.compliance_check.run_coverage_report")
    @patch("scripts.compliance_check.run_backfill")
    @patch("scripts.compliance_check.get_db_stats")
    def test_ci_mode_exits_1_on_violations(self, mock_stats, mock_bf, mock_cov, mock_schema):
        mock_stats.return_value = {
            "total_mappings": 100,
            "null_confidence": 0,
            "error_violations": 3,
            "warning_violations": 0,
        }
        mock_schema.return_value = {"violations_error": 3, "violations_warning": 0, "exit_code": 1}
        mock_cov.return_value = {"exit_code": 0, "output_file": "x.html"}
        mock_bf.return_value = {"exit_code": 0, "rows_updated": 0}
        from scripts.compliance_check import run_full_audit

        code = run_full_audit(Path("/fake/db.db"), ci_mode=True)
        assert code == 1

    @patch("scripts.compliance_check.run_check_schema")
    @patch("scripts.compliance_check.run_coverage_report")
    @patch("scripts.compliance_check.run_backfill")
    @patch("scripts.compliance_check.get_db_stats")
    def test_ci_mode_ok_on_no_violations(self, mock_stats, mock_bf, mock_cov, mock_schema):
        mock_stats.return_value = {
            "total_mappings": 21660,
            "null_confidence": 0,
            "error_violations": 0,
            "warning_violations": 5,
        }
        mock_schema.return_value = {"violations_error": 0, "violations_warning": 5, "exit_code": 0}
        mock_cov.return_value = {"exit_code": 0, "output_file": "x.html"}
        mock_bf.return_value = {"exit_code": 0, "rows_updated": 0}
        from scripts.compliance_check import run_full_audit

        code = run_full_audit(Path("/fake/db.db"), ci_mode=True)
        assert code == 0

    @patch("scripts.compliance_check.run_check_schema")
    @patch("scripts.compliance_check.run_coverage_report")
    @patch("scripts.compliance_check.run_backfill")
    @patch("scripts.compliance_check.get_db_stats")
    def test_full_audit_calls_all_three_subcommands(
        self, mock_stats, mock_bf, mock_cov, mock_schema
    ):
        """All three mock functions must be called during full-audit"""
        mock_stats.return_value = {
            "total_mappings": 50,
            "null_confidence": 0,
            "error_violations": 0,
            "warning_violations": 0,
        }
        mock_schema.return_value = {"violations_error": 0, "violations_warning": 0, "exit_code": 0}
        mock_cov.return_value = {"exit_code": 0, "output_file": "report.html"}
        mock_bf.return_value = {"exit_code": 0, "rows_updated": 0}
        from scripts.compliance_check import run_full_audit

        run_full_audit(Path("/fake/db.db"))
        assert mock_schema.called, "run_check_schema should be called"
        assert mock_cov.called, "run_coverage_report should be called"
        assert mock_bf.called, "run_backfill should be called"
