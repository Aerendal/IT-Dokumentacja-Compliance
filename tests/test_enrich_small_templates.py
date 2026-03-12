"""Tests for pure functions in scripts/enrich_small_templates.py."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.enrich_small_templates import parse_file, rebuild_file

pytestmark = pytest.mark.unit


SIMPLE_FILE = """---
title: Test Document
status: needs_content
---

# Test Document

## Cel dokumentu

Content here.

## Zakres i granice

Scope content.
"""

FILE_NO_FM = """# Document Title

## Section One

Body text one.

## Section Two

Body text two.
"""

FILE_WITH_H3 = """---
title: Doc
---

## Main Section

Content.

### Sub Section

Sub content.
"""


class TestParseFile:
    def test_returns_four_tuple(self):
        result = parse_file(SIMPLE_FILE)
        assert len(result) == 4

    def test_extracts_frontmatter(self):
        fm, pre, sections, order = parse_file(SIMPLE_FILE)
        assert "title: Test Document" in fm
        assert fm.startswith("---")

    def test_extracts_sections(self):
        fm, pre, sections, order = parse_file(SIMPLE_FILE)
        assert "## Cel dokumentu" in sections
        assert "## Zakres i granice" in sections

    def test_preserves_section_order(self):
        fm, pre, sections, order = parse_file(SIMPLE_FILE)
        assert order.index("## Cel dokumentu") < order.index("## Zakres i granice")

    def test_no_frontmatter(self):
        fm, pre, sections, order = parse_file(FILE_NO_FM)
        assert fm == ""
        assert "## Section One" in sections
        assert "## Section Two" in sections

    def test_section_body_content(self):
        fm, pre, sections, order = parse_file(SIMPLE_FILE)
        assert "Content here" in sections["## Cel dokumentu"]

    def test_empty_file(self):
        fm, pre, sections, order = parse_file("")
        assert sections == {}
        assert order == []

    def test_h3_not_treated_as_h2_section(self):
        fm, pre, sections, order = parse_file(FILE_WITH_H3)
        assert "## Main Section" in sections
        assert "### Sub Section" not in sections

    def test_order_list_matches_sections_keys(self):
        fm, pre, sections, order = parse_file(SIMPLE_FILE)
        assert set(order) == set(sections.keys())


class TestRebuildFile:
    def test_roundtrip(self):
        fm, pre, sections, order = parse_file(SIMPLE_FILE)
        result = rebuild_file(fm, pre, sections, order)
        assert "## Cel dokumentu" in result
        assert "## Zakres i granice" in result

    def test_includes_frontmatter(self):
        fm, pre, sections, order = parse_file(SIMPLE_FILE)
        result = rebuild_file(fm, pre, sections, order)
        assert "title: Test Document" in result

    def test_section_heading_present(self):
        fm, pre, sections, order = parse_file(FILE_NO_FM)
        result = rebuild_file(fm, pre, sections, order)
        assert "## Section One" in result
        assert "## Section Two" in result

    def test_section_body_present(self):
        fm, pre, sections, order = parse_file(FILE_NO_FM)
        result = rebuild_file(fm, pre, sections, order)
        assert "Body text one" in result
        assert "Body text two" in result

    def test_empty_sections(self):
        result = rebuild_file("", "", {}, [])
        assert result == ""

    def test_order_is_respected(self):
        fm, pre, sections, order = parse_file(FILE_NO_FM)
        result = rebuild_file(fm, pre, sections, order)
        idx_one = result.index("Section One")
        idx_two = result.index("Section Two")
        assert idx_one < idx_two

    def test_custom_order(self):
        fm, pre, sections, order = parse_file(FILE_NO_FM)
        reversed_order = list(reversed(order))
        result = rebuild_file(fm, pre, sections, reversed_order)
        idx_one = result.index("Section One")
        idx_two = result.index("Section Two")
        assert idx_two < idx_one
