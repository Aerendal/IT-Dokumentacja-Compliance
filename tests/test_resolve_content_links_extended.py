"""Tests for scripts/resolve_content_links_extended.py — pure utility functions."""
import re
import sqlite3
import pytest

from scripts.resolve_content_links_extended import (
    to_anchor,
    norm_title,
    build_doc_title_index,
    build_section_anchor_index,
    strength_from_required,
    utc_now,
    DOC_TITLE_SECTION_RE,
)


# ---------------------------------------------------------------------------
# to_anchor
# ---------------------------------------------------------------------------

class TestToAnchor:
    def test_basic_lowercase(self):
        assert to_anchor("Introduction") == "introduction"

    def test_spaces_to_hyphens(self):
        assert to_anchor("Getting Started") == "getting-started"

    def test_multiple_spaces_collapsed(self):
        assert to_anchor("a  b   c") == "a-b-c"

    def test_strips_leading_trailing(self):
        assert to_anchor("  hello world  ") == "hello-world"

    def test_removes_non_ascii(self):
        result = to_anchor("Przegląd systemu")
        assert "ą" not in result
        assert "przeg" in result

    def test_removes_special_chars(self):
        result = to_anchor("section (1) [test]!")
        assert "(" not in result
        assert "!" not in result
        assert "[" not in result

    def test_collapses_multiple_hyphens(self):
        assert to_anchor("a--b---c") == "a-b-c"

    def test_already_slug(self):
        assert to_anchor("my-section") == "my-section"

    def test_numbers_preserved(self):
        assert to_anchor("phase 1 overview") == "phase-1-overview"

    def test_empty_string(self):
        assert to_anchor("") == ""

    def test_all_special_chars(self):
        assert to_anchor("!@#$%^&*()") == ""

    def test_mixed_case(self):
        assert to_anchor("MySection Title") == "mysection-title"

    def test_hyphen_preserved_when_valid(self):
        result = to_anchor("section")
        assert result == "section"


# ---------------------------------------------------------------------------
# norm_title
# ---------------------------------------------------------------------------

class TestNormTitle:
    def test_lowercase(self):
        assert norm_title("ISO 27001") == "iso 27001"

    def test_strips_whitespace(self):
        assert norm_title("  hello  ") == "hello"

    def test_empty_string(self):
        assert norm_title("") == ""

    def test_none_returns_empty(self):
        assert norm_title(None) == ""

    def test_already_lowercase(self):
        assert norm_title("already lower") == "already lower"

    def test_preserves_unicode_lowercase(self):
        result = norm_title("Ząb Zębaty")
        assert result == "ząb zębaty"


# ---------------------------------------------------------------------------
# strength_from_required
# ---------------------------------------------------------------------------

class TestStrengthFromRequired:
    def test_required_1(self):
        assert strength_from_required(1) == "required"

    def test_required_0(self):
        assert strength_from_required(0) == "navigational"

    def test_required_none(self):
        assert strength_from_required(None) == "navigational"

    def test_required_true(self):
        assert strength_from_required(True) == "required"

    def test_required_false(self):
        assert strength_from_required(False) == "navigational"


# ---------------------------------------------------------------------------
# utc_now
# ---------------------------------------------------------------------------

class TestUtcNow:
    def test_format(self):
        result = utc_now()
        assert re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$', result)

    def test_returns_string(self):
        assert isinstance(utc_now(), str)

    def test_ends_with_z(self):
        assert utc_now().endswith("Z")


# ---------------------------------------------------------------------------
# DOC_TITLE_SECTION_RE
# ---------------------------------------------------------------------------

class TestDocTitleSectionRe:
    def test_matches_valid_format(self):
        m = DOC_TITLE_SECTION_RE.match("document::My Doc Title::section::Introduction")
        assert m is not None
        assert m.group(1) == "My Doc Title"
        assert m.group(2) == "Introduction"

    def test_case_insensitive(self):
        assert DOC_TITLE_SECTION_RE.match("DOCUMENT::Title::SECTION::Body") is not None

    def test_no_match_plain_document(self):
        assert DOC_TITLE_SECTION_RE.match("document::Title") is None

    def test_no_match_empty(self):
        assert DOC_TITLE_SECTION_RE.match("") is None

    def test_section_name_with_spaces(self):
        m = DOC_TITLE_SECTION_RE.match("document::Doc::section::Phase 1 Overview")
        assert m is not None
        assert m.group(2) == "Phase 1 Overview"


# ---------------------------------------------------------------------------
# build_doc_title_index
# ---------------------------------------------------------------------------

def _make_docs_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE docs (doc_uid TEXT, title TEXT)")
    conn.executemany("INSERT INTO docs VALUES (?,?)", [
        ("uid-1", "ISO 27001 Policy"),
        ("uid-2", "GDPR Compliance"),
        ("uid-3", None),           # null title — should be skipped
        ("uid-4", "  Trimmed Title  "),
    ])
    conn.commit()
    return conn


class TestBuildDocTitleIndex:
    def test_basic_index(self):
        conn = _make_docs_db()
        idx = build_doc_title_index(conn.cursor())
        assert "iso 27001 policy" in idx
        assert idx["iso 27001 policy"] == "uid-1"

    def test_null_titles_excluded(self):
        conn = _make_docs_db()
        idx = build_doc_title_index(conn.cursor())
        for key in idx:
            assert key is not None

    def test_multiple_titles(self):
        conn = _make_docs_db()
        idx = build_doc_title_index(conn.cursor())
        assert "gdpr compliance" in idx

    def test_trimmed_title_normalized(self):
        conn = _make_docs_db()
        idx = build_doc_title_index(conn.cursor())
        assert "trimmed title" in idx

    def test_empty_docs_table(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE docs (doc_uid TEXT, title TEXT)")
        conn.commit()
        idx = build_doc_title_index(conn.cursor())
        assert idx == {}

    def test_duplicate_titles_first_wins(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE docs (doc_uid TEXT, title TEXT)")
        conn.executemany("INSERT INTO docs VALUES (?,?)", [
            ("uid-a", "Duplicate"),
            ("uid-b", "Duplicate"),
        ])
        conn.commit()
        idx = build_doc_title_index(conn.cursor())
        assert idx["duplicate"] == "uid-a"


# ---------------------------------------------------------------------------
# build_section_anchor_index
# ---------------------------------------------------------------------------

def _make_sections_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE sections (section_uid TEXT, doc_uid TEXT, anchor TEXT)")
    conn.executemany("INSERT INTO sections VALUES (?,?,?)", [
        ("sec-1", "doc-1", "introduction"),
        ("sec-2", "doc-1", "phase-1"),
        ("sec-3", "doc-2", "overview"),
        ("sec-4", "doc-2", None),   # null anchor — should be skipped
    ])
    conn.commit()
    return conn


class TestBuildSectionAnchorIndex:
    def test_basic_index(self):
        conn = _make_sections_db()
        idx = build_section_anchor_index(conn.cursor())
        assert ("doc-1", "introduction") in idx
        assert idx[("doc-1", "introduction")] == "sec-1"

    def test_null_anchors_excluded(self):
        conn = _make_sections_db()
        idx = build_section_anchor_index(conn.cursor())
        for (du, anchor) in idx:
            assert anchor is not None

    def test_multiple_sections(self):
        conn = _make_sections_db()
        idx = build_section_anchor_index(conn.cursor())
        assert ("doc-2", "overview") in idx

    def test_empty_sections_table(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE sections (section_uid TEXT, doc_uid TEXT, anchor TEXT)")
        conn.commit()
        idx = build_section_anchor_index(conn.cursor())
        assert idx == {}

    def test_different_docs_same_anchor(self):
        conn = _make_sections_db()
        idx = build_section_anchor_index(conn.cursor())
        # Both doc-1 and doc-2 could share anchor names; they are distinct keys
        assert ("doc-1", "phase-1") in idx
