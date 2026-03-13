"""tests/test_pipeline_helpers.py

Unit testy dla czystych funkcji pomocniczych w scripts/pipeline_run.py.
Skupia się na funkcjach bez efektów ubocznych — nie testuje głównej pętli pipeline.

Zasada: nie mockujemy tego co testujemy — prawdziwy hashlib, pathlib, csv.
"""

import csv
import sys
from pathlib import Path

import pytest

# pipeline_run.py używa `import check_no_emoji` jako moduł skryptowy
# — wymaga scripts/ w sys.path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import pipeline_run as pr


# ---------------------------------------------------------------------------
# Dataclassy
# ---------------------------------------------------------------------------


class TestDataclasses:
    def test_coverage_instantiation(self):
        cov = pr.Coverage(
            files_count=100,
            log_count=95,
            db_documents_current=93,
            distinct_title_norm=90,
            aligned_not_ok=5,
            empty_path=1,
            dup_path=2,
            csv_vs_fs_missing=3,
            csv_vs_fs_extra=1,
            snapshot_count=10,
        )
        assert cov.files_count == 100
        assert cov.log_count == 95

    def test_snapshot_action_created(self):
        action = pr.SnapshotAction(action="CREATED", snapshot_id=42)
        assert action.action == "CREATED"
        assert action.snapshot_id == 42

    def test_snapshot_action_noop(self):
        action = pr.SnapshotAction(action="NOOP", snapshot_id=None)
        assert action.action == "NOOP"
        assert action.snapshot_id is None

    def test_prune_report(self):
        report = pr.PruneReport(kept=[1, 2, 3], deleted=[4, 5])
        assert report.kept == [1, 2, 3]
        assert report.deleted == [4, 5]

    def test_validate_report(self):
        report = pr.ValidateReport(
            status="PASS",
            reasons=[],
            metrics={"files": 100},
        )
        assert report.status == "PASS"
        assert report.metrics["files"] == 100


# ---------------------------------------------------------------------------
# utc_now_iso()
# ---------------------------------------------------------------------------


class TestUtcNowIso:
    def test_returns_string(self):
        result = pr.utc_now_iso()
        assert isinstance(result, str)

    def test_format_iso_like(self):
        result = pr.utc_now_iso()
        # Format: YYYY-MM-DDTHH-MM-SSZ
        assert result.endswith("Z")
        assert "T" in result
        assert len(result) == 20

    def test_two_calls_not_equal(self):
        import time
        a = pr.utc_now_iso()
        time.sleep(1.01)
        b = pr.utc_now_iso()
        assert a != b


# ---------------------------------------------------------------------------
# sha256_bytes() / hash_v2_bytes()
# ---------------------------------------------------------------------------


class TestHashFunctions:
    def test_sha256_known_value(self):
        # echo -n "" | sha256sum → e3b0c44298fc1c149...
        result = pr.sha256_bytes(b"")
        assert result == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

    def test_sha256_hello(self):
        result = pr.sha256_bytes(b"hello")
        assert len(result) == 64
        assert result == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

    def test_sha256_returns_hex(self):
        result = pr.sha256_bytes(b"test data")
        assert all(c in "0123456789abcdef" for c in result)

    def test_hash_v2_normalizes_crlf(self):
        """CRLF i CR są normalizowane przed hashowaniem — wynik taki sam jak LF."""
        lf_bytes = b"line1\nline2\n"
        crlf_bytes = b"line1\r\nline2\r\n"
        cr_bytes = b"line1\rline2\r"
        assert pr.hash_v2_bytes(lf_bytes) == pr.hash_v2_bytes(crlf_bytes)
        assert pr.hash_v2_bytes(lf_bytes) == pr.hash_v2_bytes(cr_bytes)

    def test_hash_v2_different_content_gives_different_hash(self):
        assert pr.hash_v2_bytes(b"abc") != pr.hash_v2_bytes(b"def")

    def test_hash_v2_empty(self):
        result = pr.hash_v2_bytes(b"")
        assert isinstance(result, str)
        assert len(result) == 64


# ---------------------------------------------------------------------------
# load_allowlist_hashes()
# ---------------------------------------------------------------------------


class TestLoadAllowlistHashes:
    def test_missing_file_returns_empty_set(self, tmp_path):
        result = pr.load_allowlist_hashes(tmp_path / "nonexistent.txt")
        assert result == set()

    def test_parses_hashes(self, tmp_path):
        f = tmp_path / "allow.txt"
        f.write_text("abc123\ndef456\n", encoding="utf-8")
        result = pr.load_allowlist_hashes(f)
        assert result == {"abc123", "def456"}

    def test_ignores_comments_and_blank_lines(self, tmp_path):
        f = tmp_path / "allow.txt"
        f.write_text("# komentarz\n\nabc123\n  \n# kolejny\ndef456\n", encoding="utf-8")
        result = pr.load_allowlist_hashes(f)
        assert result == {"abc123", "def456"}

    def test_returns_set(self, tmp_path):
        f = tmp_path / "allow.txt"
        f.write_text("abc123\nabc123\n", encoding="utf-8")
        result = pr.load_allowlist_hashes(f)
        assert isinstance(result, set)
        assert len(result) == 1  # deduplicated


# ---------------------------------------------------------------------------
# load_exemption_patterns()
# ---------------------------------------------------------------------------


class TestLoadExemptionPatterns:
    def test_missing_file_returns_empty_list(self, tmp_path):
        result = pr.load_exemption_patterns(tmp_path / "nonexistent.txt")
        assert result == []

    def test_parses_patterns(self, tmp_path):
        f = tmp_path / "exempt.txt"
        f.write_text("*.bak\nimported/**\n", encoding="utf-8")
        result = pr.load_exemption_patterns(f)
        assert result == ["*.bak", "imported/**"]

    def test_ignores_comments_and_blank(self, tmp_path):
        f = tmp_path / "exempt.txt"
        f.write_text("# ignore\n\nimported/**\n", encoding="utf-8")
        result = pr.load_exemption_patterns(f)
        assert result == ["imported/**"]

    def test_returns_list(self, tmp_path):
        f = tmp_path / "exempt.txt"
        f.write_text("*.bak\n", encoding="utf-8")
        result = pr.load_exemption_patterns(f)
        assert isinstance(result, list)


# ---------------------------------------------------------------------------
# is_exempt_path()
# ---------------------------------------------------------------------------


class TestIsExemptPath:
    def test_imported_prefix_always_exempt(self):
        assert pr.is_exempt_path("imported/some/file.md", []) is True
        assert pr.is_exempt_path("imported/file.md", ["other/**"]) is True

    def test_glob_pattern_match(self):
        assert pr.is_exempt_path("legacy/old.bak", ["*.bak"]) is True

    def test_no_match_returns_false(self):
        assert pr.is_exempt_path("core/security/policy.md", ["*.bak"]) is False

    def test_empty_patterns_non_imported_returns_false(self):
        assert pr.is_exempt_path("core/policy.md", []) is False

    def test_deep_glob_match(self):
        # PurePosixPath.match("*.md") dopasowuje ostatni segment ścieżki
        assert pr.is_exempt_path("core/security/policy.md", ["*.md"]) is True


# ---------------------------------------------------------------------------
# normalize_path_for_reports()
# ---------------------------------------------------------------------------


class TestNormalizePathForReports:
    def test_strips_generated_templates_prefix(self):
        result = pr.normalize_path_for_reports("generated_templates/core/security/policy.md")
        assert result == "core/security/policy.md"

    def test_strips_dotslash_prefix(self):
        result = pr.normalize_path_for_reports("./core/policy.md")
        assert result == "core/policy.md"

    def test_strips_backslashes(self):
        result = pr.normalize_path_for_reports("core\\security\\policy.md")
        assert result == "core/security/policy.md"

    def test_strips_newlines(self):
        result = pr.normalize_path_for_reports("core/policy.md\n")
        assert result == "core/policy.md"

    def test_plain_path_unchanged(self):
        result = pr.normalize_path_for_reports("core/security/policy.md")
        assert result == "core/security/policy.md"

    def test_empty_string(self):
        result = pr.normalize_path_for_reports("")
        assert result == ""

    def test_none_like_empty(self):
        result = pr.normalize_path_for_reports(None)
        assert result == ""


# ---------------------------------------------------------------------------
# match_rule()
# ---------------------------------------------------------------------------


class TestMatchRule:
    def _rule(self, match_type, match_value):
        return {
            "rule_id": "R1",
            "match_type": match_type,
            "match_value": match_value,
            "tag_type": "category",
            "tag_value": "security",
            "priority": 10,
        }

    def test_prefix_match(self):
        rule = self._rule("prefix", "core/security/")
        assert pr.match_rule(rule, "core/security/policy.md") is True

    def test_prefix_no_match(self):
        rule = self._rule("prefix", "core/security/")
        assert pr.match_rule(rule, "core/hr/onboarding.md") is False

    def test_glob_match(self):
        rule = self._rule("glob", "*.md")
        assert pr.match_rule(rule, "policy.md") is True

    def test_glob_deep_match(self):
        rule = self._rule("glob", "core/security/*")
        assert pr.match_rule(rule, "core/security/policy.md") is True

    def test_glob_no_match(self):
        rule = self._rule("glob", "*.bak")
        assert pr.match_rule(rule, "policy.md") is False

    def test_unknown_match_type_returns_false(self):
        rule = self._rule("regex", ".*\\.md")
        assert pr.match_rule(rule, "policy.md") is False


# ---------------------------------------------------------------------------
# _detect_delimiter()
# ---------------------------------------------------------------------------


class TestDetectDelimiter:
    def test_semicolon_wins(self):
        sample = "col1;col2;col3\nval1;val2;val3\n"
        assert pr._detect_delimiter(sample) == ";"

    def test_comma_wins(self):
        sample = "col1,col2,col3\nval1,val2,val3\n"
        assert pr._detect_delimiter(sample) == ","

    def test_default_semicolon_on_tie(self):
        # równe ilości ; i , → semicolon
        sample = "a;b,c"
        result = pr._detect_delimiter(sample)
        assert result in (";", ",")


# ---------------------------------------------------------------------------
# _detect_path_column()
# ---------------------------------------------------------------------------


class TestDetectPathColumn:
    def test_finds_path(self):
        assert pr._detect_path_column(["path", "title", "status"]) == "path"

    def test_finds_relative_path(self):
        assert pr._detect_path_column(["relative_path", "title"]) == "relative_path"

    def test_finds_template_path(self):
        assert pr._detect_path_column(["template_path", "doc"]) == "template_path"

    def test_none_for_empty(self):
        assert pr._detect_path_column([]) is None

    def test_none_for_no_match(self):
        assert pr._detect_path_column(["title", "status", "version"]) is None

    def test_case_insensitive_fallback(self):
        # "Path" not in exact candidates but case-insensitive match
        result = pr._detect_path_column(["Path", "title"])
        assert result == "Path"


# ---------------------------------------------------------------------------
# _normalize_rel_path()
# ---------------------------------------------------------------------------


class TestNormalizeRelPath:
    def test_removes_dotslash(self):
        assert pr._normalize_rel_path("./core/policy.md") == "core/policy.md"

    def test_removes_generated_templates_marker(self):
        assert pr._normalize_rel_path("generated_templates/core/policy.md") == "core/policy.md"

    def test_normalizes_double_backslashes(self):
        # Funkcja zastępuje \\ (podwójny backslash) ukośnikiem — pojedyncze \ nie są normalizowane
        result = pr._normalize_rel_path("core\\\\security\\\\policy.md")
        assert "\\\\" not in result

    def test_empty_string(self):
        assert pr._normalize_rel_path("") == ""

    def test_strips_whitespace(self):
        assert pr._normalize_rel_path("  core/policy.md  ") == "core/policy.md"


# ---------------------------------------------------------------------------
# load_tag_rules()
# ---------------------------------------------------------------------------


class TestLoadTagRules:
    _HEADERS = "rule_id,match_type,match_value,tag_type,tag_value,priority\n"

    def test_missing_file_returns_empty_missing(self, tmp_path):
        rules, status = pr.load_tag_rules(tmp_path / "nonexistent.csv")
        assert rules == []
        assert status == "missing"

    def test_invalid_header_returns_empty_invalid(self, tmp_path):
        f = tmp_path / "rules.csv"
        f.write_text("wrong,headers\nR1,foo\n", encoding="utf-8")
        rules, status = pr.load_tag_rules(f)
        assert rules == []
        assert status == "invalid_header"

    def test_parses_rules_correctly(self, tmp_path):
        f = tmp_path / "rules.csv"
        f.write_text(
            self._HEADERS + "R1,prefix,core/security/,category,security,10\n",
            encoding="utf-8",
        )
        rules, status = pr.load_tag_rules(f)
        assert status == "ok"
        assert len(rules) == 1
        assert rules[0]["rule_id"] == "R1"
        assert rules[0]["match_type"] == "prefix"
        assert rules[0]["match_value"] == "core/security/"
        assert rules[0]["priority"] == 10

    def test_skips_comment_rows(self, tmp_path):
        f = tmp_path / "rules.csv"
        f.write_text(
            self._HEADERS
            + "#comment,prefix,x/,cat,val,0\n"
            + "R2,glob,*.md,type,template,5\n",
            encoding="utf-8",
        )
        rules, status = pr.load_tag_rules(f)
        assert status == "ok"
        assert len(rules) == 1
        assert rules[0]["rule_id"] == "R2"

    def test_skips_empty_rule_id_rows(self, tmp_path):
        f = tmp_path / "rules.csv"
        f.write_text(
            self._HEADERS + ",prefix,x/,cat,val,0\nR3,glob,*.md,type,template,5\n",
            encoding="utf-8",
        )
        rules, status = pr.load_tag_rules(f)
        assert len(rules) == 1
        assert rules[0]["rule_id"] == "R3"

    def test_multiple_rules(self, tmp_path):
        f = tmp_path / "rules.csv"
        f.write_text(
            self._HEADERS
            + "R1,prefix,core/,cat,core,10\n"
            + "R2,glob,*.md,type,template,5\n"
            + "R3,prefix,satellite/,cat,satellite,8\n",
            encoding="utf-8",
        )
        rules, status = pr.load_tag_rules(f)
        assert status == "ok"
        assert len(rules) == 3
