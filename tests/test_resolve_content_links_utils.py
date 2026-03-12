"""Tests for pure utility functions in scripts/resolve_content_links.py."""

import sqlite3
import sys
from unittest.mock import MagicMock

import pytest

pytestmark = pytest.mark.unit

# ---------------------------------------------------------------------------
# Mock 'ulid' before importing the module under test
# ---------------------------------------------------------------------------
_ulid_mock = MagicMock()
_ulid_mock.ulid = MagicMock(return_value="01TEST0000000000000000000A")
sys.modules.setdefault("ulid", _ulid_mock)

from scripts.resolve_content_links import (  # noqa: E402
    build_section_indexes,
    norm_label,
    strength_from_required,
    table_exists,
    utc_now_iso,
)

# ── utc_now_iso ──────────────────────────────────────────────────────────────


def test_utc_now_iso_format():
    ts = utc_now_iso()
    assert ts.endswith("Z")
    assert "T" in ts
    assert len(ts) == 20  # "2025-01-01T12:00:00Z"


def test_utc_now_iso_returns_string():
    assert isinstance(utc_now_iso(), str)


# ── norm_label ────────────────────────────────────────────────────────────────


def test_norm_label_lowercases():
    assert norm_label("Hello World") == "hello world"


def test_norm_label_strips_whitespace():
    assert norm_label("  hello  ") == "hello"


def test_norm_label_collapses_spaces():
    assert norm_label("hello   world") == "hello world"


def test_norm_label_strips_numeric_prefix():
    assert norm_label("1. Introduction") == "introduction"


def test_norm_label_strips_numeric_prefix_single_digit_dot():
    # The regex matches a single "digit." or "digit)" prefix; "1.2." is not stripped
    assert norm_label("2) Introduction") == "introduction"


def test_norm_label_strips_meta_prefix():
    assert norm_label("meta: Something") == "something"


def test_norm_label_handles_none():
    assert norm_label(None) == ""


def test_norm_label_handles_empty_string():
    assert norm_label("") == ""


def test_norm_label_removes_bom():
    assert norm_label("\ufeffTitle") == "title"


def test_norm_label_strips_emoji():
    result = norm_label("\U0001f680 Launch")
    assert "\U0001f680" not in result
    assert "launch" in result


# ── strength_from_required ────────────────────────────────────────────────────


def test_strength_required_returns_required():
    assert strength_from_required(1) == "required"


def test_strength_not_required_returns_navigational():
    assert strength_from_required(0) == "navigational"


def test_strength_other_value_returns_navigational():
    assert strength_from_required(2) == "navigational"


# ── table_exists ──────────────────────────────────────────────────────────────


@pytest.fixture
def mem_conn():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()


def test_table_exists_true(mem_conn):
    mem_conn.execute("CREATE TABLE foo (id INTEGER PRIMARY KEY)")
    cur = mem_conn.cursor()
    assert table_exists(cur, "foo") is True


def test_table_exists_false(mem_conn):
    cur = mem_conn.cursor()
    assert table_exists(cur, "nonexistent") is False


def test_table_exists_after_drop(mem_conn):
    mem_conn.execute("CREATE TABLE bar (id INTEGER PRIMARY KEY)")
    mem_conn.execute("DROP TABLE bar")
    cur = mem_conn.cursor()
    assert table_exists(cur, "bar") is False


# ── build_section_indexes ─────────────────────────────────────────────────────


@pytest.fixture
def sections_conn():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE sections (section_uid TEXT, doc_uid TEXT, heading_norm TEXT, anchor TEXT)"
    )
    conn.executemany(
        "INSERT INTO sections VALUES (?, ?, ?, ?)",
        [
            ("s1", "doc1", "introduction", "intro"),
            ("s2", "doc1", "scope", "scope"),
            ("s3", "doc2", "introduction", "intro"),
            ("s4", "doc2", "unique section", "unique-section"),
        ],
    )
    conn.commit()
    yield conn
    conn.close()


def test_build_section_indexes_doc_index_keys(sections_conn):
    cur = sections_conn.cursor()
    doc_index, _ = build_section_indexes(cur)
    assert "doc1" in doc_index
    assert "doc2" in doc_index


def test_build_section_indexes_doc_contains_heading(sections_conn):
    cur = sections_conn.cursor()
    doc_index, _ = build_section_indexes(cur)
    assert "introduction" in doc_index["doc1"]
    assert "s1" in doc_index["doc1"]["introduction"]


def test_build_section_indexes_global_aggregates_across_docs(sections_conn):
    cur = sections_conn.cursor()
    _, global_index = build_section_indexes(cur)
    assert "s1" in global_index["introduction"]
    assert "s3" in global_index["introduction"]


def test_build_section_indexes_anchor_key_present(sections_conn):
    cur = sections_conn.cursor()
    doc_index, _ = build_section_indexes(cur)
    assert "intro" in doc_index["doc1"]


def test_build_section_indexes_slug_added_when_spaces(sections_conn):
    cur = sections_conn.cursor()
    doc_index, global_index = build_section_indexes(cur)
    assert "unique-section" in doc_index["doc2"]
    assert "unique-section" in global_index


def test_build_section_indexes_empty_table():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE sections (section_uid TEXT, doc_uid TEXT, heading_norm TEXT, anchor TEXT)"
    )
    cur = conn.cursor()
    doc_index, global_index = build_section_indexes(cur)
    assert doc_index == {}
    assert global_index == {}
    conn.close()
