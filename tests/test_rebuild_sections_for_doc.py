"""Tests for pure functions in scripts/rebuild_sections_for_doc.py."""
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.rebuild_sections_for_doc import (
    utc_now_iso, heading_norm, slugify, extract_sections
)

pytestmark = pytest.mark.unit


class TestUtcNowIso:
    def test_returns_string(self):
        assert isinstance(utc_now_iso(), str)

    def test_ends_with_z(self):
        assert utc_now_iso().endswith("Z")

    def test_contains_date(self):
        import re
        assert re.match(r"\d{4}-\d{2}-\d{2}T", utc_now_iso())


class TestHeadingNorm:
    def test_lowercase(self):
        assert heading_norm("Hello World") == "hello world"

    def test_strips_whitespace(self):
        assert heading_norm("  Test  ") == "test"

    def test_removes_numeric_prefix(self):
        result = heading_norm("1. Introduction")
        assert result == "introduction"

    def test_removes_emoji(self):
        result = heading_norm("Security 🔒 Policy")
        assert "🔒" not in result
        assert "security" in result

    def test_collapses_spaces(self):
        assert heading_norm("too   many  spaces") == "too many spaces"

    def test_empty_string(self):
        assert heading_norm("") == ""

    def test_none_safe(self):
        assert heading_norm(None) == ""


class TestSlugify:
    def test_basic_slug(self):
        assert slugify("Hello World") == "hello-world"

    def test_special_chars_removed(self):
        result = slugify("Section: Overview!")
        assert ":" not in result
        assert "!" not in result

    def test_spaces_become_dashes(self):
        assert "-" in slugify("section heading")

    def test_empty_returns_section(self):
        assert slugify("") == "section"

    def test_numeric_prefix_stripped(self):
        result = slugify("1. Introduction")
        assert not result.startswith("1")

    def test_lowercase_result(self):
        result = slugify("UPPERCASE HEADING")
        assert result == result.lower()

    def test_no_leading_trailing_dashes(self):
        result = slugify("  Test  ")
        assert not result.startswith("-")
        assert not result.endswith("-")


class TestExtractSections:
    # extract_sections returns (sections, headers, lines)
    # each section tuple: (line_no, end, level, text, hn, anchor, ordinal, heading_path, status)
    SIMPLE_MD = """# Title

## Introduction

Some intro content.

## Methods

Method details here.

### Sub-method

Details.

## Conclusion

Final thoughts.
"""

    def test_returns_tuple_of_three(self):
        result = extract_sections(self.SIMPLE_MD)
        assert len(result) == 3

    def test_sections_is_list(self):
        sections, headers, lines = extract_sections(self.SIMPLE_MD)
        assert isinstance(sections, list)

    def test_detects_h2_sections(self):
        sections, headers, lines = extract_sections(self.SIMPLE_MD)
        headings = [s[3] for s in sections]  # index 3 = text
        assert "Introduction" in headings
        assert "Methods" in headings
        assert "Conclusion" in headings

    def test_detects_h1_and_h3(self):
        sections, headers, lines = extract_sections(self.SIMPLE_MD)
        headings = [s[3] for s in sections]
        assert "Title" in headings
        assert "Sub-method" in headings

    def test_section_tuple_has_nine_elements(self):
        sections, headers, lines = extract_sections(self.SIMPLE_MD)
        for sec in sections:
            assert len(sec) == 9

    def test_level_values(self):
        sections, headers, lines = extract_sections(self.SIMPLE_MD)
        for sec in sections:
            assert sec[2] in (1, 2, 3, 4, 5, 6)  # index 2 = level

    def test_empty_text_returns_empty_sections(self):
        sections, headers, lines = extract_sections("")
        assert sections == []
        assert headers == []

    def test_ordinal_starts_at_one(self):
        sections, headers, lines = extract_sections(self.SIMPLE_MD)
        assert any(s[6] == 1 for s in sections)  # index 6 = ordinal

    def test_no_headings_gives_empty_sections(self):
        sections, headers, lines = extract_sections("Just plain text\nno headings.")
        assert sections == []
        assert headers == []

    def test_lines_match_input(self):
        sections, headers, lines = extract_sections(self.SIMPLE_MD)
        assert len(lines) == len(self.SIMPLE_MD.splitlines())
