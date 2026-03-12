"""Tests for scripts/build_standards_catalog.py and scripts/sync_docs_ids.py."""

import sqlite3
import sys
from unittest.mock import MagicMock

import pytest

pytestmark = pytest.mark.unit

# ---------------------------------------------------------------------------
# Mock 'ulid' before importing sync_docs_ids (which does `from ulid import ulid`)
# ---------------------------------------------------------------------------
if "ulid" not in sys.modules:
    _ulid_mock = MagicMock()
    _ulid_mock.ulid = MagicMock(return_value="01TEST0000000000000000000A")
    sys.modules["ulid"] = _ulid_mock

from scripts.build_standards_catalog import (  # noqa: E402
    CATALOG,
    count_existing,
    create_table,
    load_catalog,
)
from scripts.sync_docs_ids import (
    load_file_index,
    normalize_title_norm,
)
from scripts.sync_docs_ids import (  # noqa: E402
    utc_now_iso as sync_utc_now_iso,
)

# ── Fixtures ──────────────────────────────────────────────────────────────────


@pytest.fixture
def catalog_conn():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = OFF")
    create_table(conn)
    yield conn
    conn.close()


# ── create_table ──────────────────────────────────────────────────────────────


def test_create_table_creates_standards_catalog(catalog_conn):
    cur = catalog_conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='standards_catalog'"
    )
    assert cur.fetchone() is not None


def test_create_table_idempotent():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = OFF")
    create_table(conn)
    create_table(conn)
    conn.close()


def test_create_table_has_expected_columns(catalog_conn):
    cur = catalog_conn.execute("PRAGMA table_info(standards_catalog)")
    cols = {row[1] for row in cur.fetchall()}
    assert "standard_code" in cols
    assert "doc_type_id" in cols
    assert "doc_title" in cols
    assert "is_required" in cols


# ── count_existing ────────────────────────────────────────────────────────────


def test_count_existing_empty(catalog_conn):
    assert count_existing(catalog_conn) == 0


def test_count_existing_after_insert(catalog_conn):
    catalog_conn.execute(
        "INSERT INTO standards_catalog (standard_code, doc_type_id, doc_title, is_required)"
        " VALUES (?, ?, ?, ?)",
        ("TEST 1", "test_doc", "Test Document", 1),
    )
    catalog_conn.commit()
    assert count_existing(catalog_conn) == 1


def test_count_existing_after_two_inserts(catalog_conn):
    catalog_conn.executemany(
        "INSERT INTO standards_catalog (standard_code, doc_type_id, doc_title, is_required)"
        " VALUES (?, ?, ?, ?)",
        [("T1", "doc_a", "Doc A", 1), ("T1", "doc_b", "Doc B", 0)],
    )
    catalog_conn.commit()
    assert count_existing(catalog_conn) == 2


# ── load_catalog ──────────────────────────────────────────────────────────────


def test_load_catalog_returns_dict(catalog_conn):
    stats = load_catalog(catalog_conn)
    assert isinstance(stats, dict)


def test_load_catalog_covers_all_standards(catalog_conn):
    stats = load_catalog(catalog_conn)
    for code in CATALOG:
        assert code in stats


def test_load_catalog_inserts_rows(catalog_conn):
    load_catalog(catalog_conn)
    n = count_existing(catalog_conn)
    expected = sum(len(v) for v in CATALOG.values())
    assert n == expected


def test_load_catalog_no_duplicate_on_second_call(catalog_conn):
    load_catalog(catalog_conn)
    n_first = count_existing(catalog_conn)
    load_catalog(catalog_conn)
    n_second = count_existing(catalog_conn)
    assert n_first == n_second


def test_load_catalog_replace_clears_and_reloads(catalog_conn):
    load_catalog(catalog_conn)
    n_before = count_existing(catalog_conn)
    load_catalog(catalog_conn, replace=True)
    n_after = count_existing(catalog_conn)
    assert n_before == n_after


def test_load_catalog_is_required_stored_as_int(catalog_conn):
    load_catalog(catalog_conn)
    row = catalog_conn.execute("SELECT is_required FROM standards_catalog LIMIT 1").fetchone()
    assert isinstance(row[0], int)


# ── CATALOG data integrity ────────────────────────────────────────────────────


def test_catalog_has_multiple_standards():
    assert len(CATALOG) >= 5


def test_catalog_each_entry_has_six_fields():
    for code, entries in CATALOG.items():
        for entry in entries:
            assert len(entry) == 6, f"Entry for {code} has wrong field count: {entry}"


def test_catalog_is_required_is_bool():
    for code, entries in CATALOG.items():
        for entry in entries:
            assert isinstance(entry[2], bool), f"is_required not bool in {code}: {entry}"


# ── sync_docs_ids: utc_now_iso ────────────────────────────────────────────────


def test_sync_utc_now_iso_format():
    ts = sync_utc_now_iso()
    assert ts.endswith("Z")
    assert "T" in ts
    assert len(ts) == 20


def test_sync_utc_now_iso_returns_string():
    assert isinstance(sync_utc_now_iso(), str)


# ── normalize_title_norm ──────────────────────────────────────────────────────


def test_normalize_title_norm_lowercases():
    assert normalize_title_norm("Hello World") == "hello world"


def test_normalize_title_norm_strips_whitespace():
    assert normalize_title_norm("  Title  ") == "title"


def test_normalize_title_norm_collapses_internal_spaces():
    assert normalize_title_norm("My   Document") == "my document"


def test_normalize_title_norm_handles_none():
    assert normalize_title_norm(None) == ""


def test_normalize_title_norm_handles_empty():
    assert normalize_title_norm("") == ""


def test_normalize_title_norm_already_normalized():
    assert normalize_title_norm("hello world") == "hello world"


# ── load_file_index ───────────────────────────────────────────────────────────


@pytest.fixture
def file_index_conn():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE file_index (title_norm TEXT, path TEXT, source TEXT)")
    conn.executemany(
        "INSERT INTO file_index VALUES (?, ?, ?)",
        [
            ("doc alpha", "/docs/alpha.md", "manifest"),
            ("doc beta", "/docs/beta.md", "manifest"),
            ("doc gamma", "/docs/gamma.md", "scan"),
        ],
    )
    conn.commit()
    yield conn
    conn.close()


def test_load_file_index_returns_dict_and_set(file_index_conn):
    cur = file_index_conn.cursor()
    idx, collisions = load_file_index(cur)
    assert isinstance(idx, dict)
    assert isinstance(collisions, set)


def test_load_file_index_contains_entries(file_index_conn):
    cur = file_index_conn.cursor()
    idx, _ = load_file_index(cur)
    assert "doc alpha" in idx
    assert "doc beta" in idx


def test_load_file_index_no_collisions_when_unique(file_index_conn):
    cur = file_index_conn.cursor()
    _, collisions = load_file_index(cur)
    assert len(collisions) == 0


def test_load_file_index_detects_collision(file_index_conn):
    file_index_conn.execute(
        "INSERT INTO file_index VALUES (?, ?, ?)",
        ("doc alpha", "/docs/alpha2.md", "manifest"),
    )
    file_index_conn.commit()
    cur = file_index_conn.cursor()
    idx, collisions = load_file_index(cur)
    assert "doc alpha" in collisions


def test_load_file_index_ignores_null_title_norm():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE file_index (title_norm TEXT, path TEXT, source TEXT)")
    conn.execute("INSERT INTO file_index VALUES (NULL, '/docs/noname.md', 'scan')")
    conn.commit()
    cur = conn.cursor()
    idx, collisions = load_file_index(cur)
    assert None not in idx
    conn.close()


def test_load_file_index_path_stored(file_index_conn):
    cur = file_index_conn.cursor()
    idx, _ = load_file_index(cur)
    path, source = idx["doc alpha"]
    assert path == "/docs/alpha.md"
    assert source == "manifest"
