"""Tests for pure functions in scripts/fix_ghost_docs.py."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.fix_ghost_docs import build_slug_map, find_path, to_slug

pytestmark = pytest.mark.unit


class TestToSlug:
    def test_basic_ascii(self):
        assert to_slug("Security Policy") == "security_policy"

    def test_polish_transliteration(self):
        result = to_slug("Polityka Bezpieczeństwa")
        assert "bezpieczenstwa" in result or "bezpiecze" in result

    def test_lowercase(self):
        assert to_slug("HELLO WORLD") == "hello_world"

    def test_special_chars_removed(self):
        result = to_slug("Hello: World!")
        assert ":" not in result
        assert "!" not in result

    def test_spaces_become_underscores(self):
        assert "_" in to_slug("multi word title")

    def test_empty_string(self):
        assert to_slug("") == ""

    def test_numbers_preserved(self):
        result = to_slug("ISO 27001 Standard")
        assert "27001" in result

    def test_multiple_spaces_normalized(self):
        result = to_slug("too   many  spaces")
        assert "  " not in result
        assert "__" not in result

    def test_no_leading_trailing_underscores(self):
        result = to_slug("  test  ")
        assert not result.startswith("_")
        assert not result.endswith("_")


class TestBuildSlugMap:
    def test_returns_dict(self, tmp_path):
        (tmp_path / "security_policy.md").write_text("# Test")
        (tmp_path / "access_control.md").write_text("# Test")
        result = build_slug_map(tmp_path)
        assert isinstance(result, dict)

    def test_maps_stems_to_paths(self, tmp_path):
        f = tmp_path / "security_policy.md"
        f.write_text("# Test")
        result = build_slug_map(tmp_path)
        assert "security_policy" in result
        assert result["security_policy"] == f

    def test_empty_dir_returns_empty_dict(self, tmp_path):
        result = build_slug_map(tmp_path)
        assert result == {}

    def test_only_md_files(self, tmp_path):
        (tmp_path / "readme.txt").write_text("text")
        (tmp_path / "policy.md").write_text("# Policy")
        result = build_slug_map(tmp_path)
        assert "policy" in result
        assert "readme" not in result


class TestFindPath:
    def test_exact_match(self, tmp_path):
        f = tmp_path / "security_policy.md"
        f.write_text("# Test")
        slug_map = build_slug_map(tmp_path)
        result = find_path("Security Policy", slug_map)
        assert result == f

    def test_no_match_returns_none(self, tmp_path):
        f = tmp_path / "access_control.md"
        f.write_text("# Test")
        slug_map = build_slug_map(tmp_path)
        result = find_path("NonExistentDocument XYZ", slug_map)
        assert result is None

    def test_empty_title_returns_none(self, tmp_path):
        slug_map = {}
        result = find_path("", slug_map)
        assert result is None

    def test_substring_match(self, tmp_path):
        f = tmp_path / "security_policy_document.md"
        f.write_text("# Test")
        slug_map = build_slug_map(tmp_path)
        result = find_path("Security Policy", slug_map)
        assert result == f

    def test_empty_slug_map_returns_none(self):
        result = find_path("Any Title", {})
        assert result is None


# Extra tests for map_standards_to_docs.match_rules (to boost coverage)
from scripts.map_standards_to_docs import match_rules


class TestMatchRules:
    RULES = [
        (["security", "iso27001"], ["ISO/IEC 27001"]),
        (["privacy", "gdpr", "rodo"], ["RODO", "GDPR"]),
        (["quality"], ["ISO 9001"]),
    ]

    def test_exact_keyword_match(self):
        result = match_rules("core/security_policy.md", "Security Policy", self.RULES)
        assert "ISO/IEC 27001" in result

    def test_no_match_returns_empty(self):
        result = match_rules("core/unrelated.md", "Unrelated Document", self.RULES)
        assert result == []

    def test_multiple_keywords_match(self):
        result = match_rules("core/privacy.md", "Privacy and GDPR Compliance", self.RULES)
        assert "RODO" in result
        assert "GDPR" in result

    def test_case_insensitive_matching(self):
        result = match_rules("CORE/SECURITY.MD", "SECURITY POLICY", self.RULES)
        assert "ISO/IEC 27001" in result

    def test_path_match_also_works(self):
        result = match_rules("security/access_control.md", "Access Control", self.RULES)
        assert "ISO/IEC 27001" in result

    def test_returns_sorted_list(self):
        result = match_rules("privacy_policy.md", "Privacy RODO Document", self.RULES)
        assert result == sorted(result)
