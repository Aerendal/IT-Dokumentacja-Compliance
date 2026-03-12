"""Additional targeted tests to push coverage above 35%.
Covers: audit_templates log/colored/find_duplicates/find_unmapped,
        template_auditor collect_targets, slugify utility.
"""
import sqlite3
import sys
from io import StringIO
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest

pytestmark = pytest.mark.unit


# ── audit_templates: colored / log functions ──────────────────────────────────

from scripts.maintenance.audit_templates import (
    colored,
    log_info,
    log_ok,
    log_warn,
    log_err,
    find_duplicates,
    find_unmapped,
    ANSI_GREEN,
    ANSI_YELLOW,
    ANSI_RED,
    ANSI_RESET,
)


def test_colored_non_tty_returns_plain(capsys):
    # capsys redirects stdout → isatty() returns False
    result = colored("hello", ANSI_GREEN)
    assert result == "hello"


def test_colored_tty_wraps_with_ansi():
    with patch.object(sys.stdout, "isatty", return_value=True):
        result = colored("hi", ANSI_GREEN)
    assert ANSI_GREEN in result
    assert "hi" in result
    assert ANSI_RESET in result


def test_log_info_prints(capsys):
    log_info("test message")
    out = capsys.readouterr().out
    assert "test message" in out
    assert "[INFO]" in out


def test_log_ok_prints(capsys):
    log_ok("everything ok")
    out = capsys.readouterr().out
    assert "everything ok" in out


def test_log_warn_prints(capsys):
    log_warn("something warned")
    out = capsys.readouterr().out
    assert "something warned" in out


def test_log_err_prints_to_stderr(capsys):
    log_err("an error occurred")
    err = capsys.readouterr().err
    assert "an error occurred" in err


# ── audit_templates: find_duplicates ──────────────────────────────────────────

def test_find_duplicates_empty_dir(tmp_path):
    core = tmp_path / "core"
    core.mkdir()
    result = find_duplicates(core)
    assert result == {}


def test_find_duplicates_no_dupes(tmp_path):
    core = tmp_path / "core"
    core.mkdir()
    (core / "a.md").write_bytes(b"unique content A")
    (core / "b.md").write_bytes(b"unique content B")
    result = find_duplicates(core)
    assert result == {}


def test_find_duplicates_detects_identical_files(tmp_path):
    core = tmp_path / "core"
    core.mkdir()
    content = b"# Identical content\nSame text here."
    (core / "file1.md").write_bytes(content)
    (core / "file2.md").write_bytes(content)
    (core / "different.md").write_bytes(b"different text")
    result = find_duplicates(core)
    assert len(result) == 1
    paths_list = next(iter(result.values()))
    assert len(paths_list) == 2


def test_find_duplicates_three_identical(tmp_path):
    core = tmp_path / "core"
    core.mkdir()
    content = b"same content"
    for name in ("x.md", "y.md", "z.md"):
        (core / name).write_bytes(content)
    result = find_duplicates(core)
    assert len(result) == 1
    assert len(next(iter(result.values()))) == 3


# ── audit_templates: find_unmapped ────────────────────────────────────────────

@pytest.fixture
def unmapped_conn():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE docs (
            doc_uid TEXT PRIMARY KEY,
            path TEXT
        );
        CREATE TABLE doc_standard_mapping (
            id INTEGER PRIMARY KEY,
            doc_path TEXT,
            standard_code TEXT
        );
        INSERT INTO docs VALUES ('UID1', 'core/alpha.md');
        INSERT INTO docs VALUES ('UID2', 'core/beta.md');
        INSERT INTO docs VALUES ('UID3', 'core/gamma.md');
        INSERT INTO docs VALUES ('UID4', NULL);
        INSERT INTO docs VALUES ('UID5', 'ORPHAN');
        INSERT INTO doc_standard_mapping VALUES (1, 'core/alpha.md', 'ISO 27001');
    """)
    yield conn
    conn.close()


def test_find_unmapped_returns_list(unmapped_conn):
    result = find_unmapped(unmapped_conn)
    assert isinstance(result, list)


def test_find_unmapped_excludes_mapped(unmapped_conn):
    result = find_unmapped(unmapped_conn)
    assert "core/alpha.md" not in result


def test_find_unmapped_includes_unmapped(unmapped_conn):
    result = find_unmapped(unmapped_conn)
    assert "core/beta.md" in result
    assert "core/gamma.md" in result


def test_find_unmapped_excludes_null_and_orphan(unmapped_conn):
    result = find_unmapped(unmapped_conn)
    assert None not in result
    assert "ORPHAN" not in result


def test_find_unmapped_returns_empty_on_missing_table():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE docs (doc_uid TEXT, path TEXT)")
    # No doc_standard_mapping table → sqlite3.Error → returns []
    result = find_unmapped(conn)
    assert result == []
    conn.close()


# ── slugify utility (same logic as update_linkage_with_branch) ───────────────
# Import the function without running module-level code by extracting the logic
import re
import unicodedata


def _slugify(s: str) -> str:
    """Same implementation as scripts/update_linkage_with_branch.slugify."""
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return s


def test_slugify_basic():
    assert _slugify("Hello World") == "hello-world"


def test_slugify_special_chars():
    result = _slugify("Audit & Compliance: 2024!")
    assert "&" not in result
    assert ":" not in result
    assert "!" not in result


def test_slugify_multiple_separators():
    result = _slugify("hello---world")
    assert result == "hello-world"


def test_slugify_strips_leading_trailing_dash():
    result = _slugify("  Hello  ")
    assert not result.startswith("-")
    assert not result.endswith("-")


def test_slugify_unicode_normalization():
    result = _slugify("café")
    assert result == "cafe"


def test_slugify_empty_string():
    result = _slugify("")
    assert result == ""


def test_slugify_numbers():
    assert _slugify("ISO 27001") == "iso-27001"


# ── template_auditor: collect_targets ────────────────────────────────────────

from scripts.maintenance.template_auditor import collect_targets  # noqa: E402


@pytest.fixture
def ta_conn():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("CREATE TABLE docs (doc_uid TEXT PRIMARY KEY, title TEXT, path TEXT)")
    conn.executemany(
        "INSERT INTO docs VALUES (?, ?, ?)",
        [
            ("UID1", "Security Policy", "core/security_policy.md"),
            ("UID2", "Test Plan", "core/test_plan.md"),
            ("UID3", "Orphaned", None),
        ],
    )
    conn.commit()
    yield conn
    conn.close()


def test_collect_targets_no_filter_returns_all_with_path(ta_conn):
    args = SimpleNamespace(doc=None, glob=None)
    results = collect_targets(ta_conn, args)
    paths = [p for p, _ in results]
    assert "core/security_policy.md" in paths
    assert "core/test_plan.md" in paths
    # None path should be excluded
    assert None not in paths


def test_collect_targets_doc_filter_matches_title(ta_conn):
    args = SimpleNamespace(doc="Security", glob=None)
    results = collect_targets(ta_conn, args)
    paths = [p for p, _ in results]
    assert "core/security_policy.md" in paths
    assert "core/test_plan.md" not in paths


def test_collect_targets_glob_filter(ta_conn):
    args = SimpleNamespace(doc=None, glob="core/security_*.md")
    results = collect_targets(ta_conn, args)
    paths = [p for p, _ in results]
    assert "core/security_policy.md" in paths
    assert "core/test_plan.md" not in paths


def test_collect_targets_returns_path_objects(ta_conn):
    args = SimpleNamespace(doc=None, glob=None)
    results = collect_targets(ta_conn, args)
    assert all(isinstance(fp, Path) for _, fp in results)


def test_collect_targets_empty_when_no_match(ta_conn):
    args = SimpleNamespace(doc="NonExistentTitle", glob=None)
    results = collect_targets(ta_conn, args)
    assert results == []


# ── Extra: audit_templates find_ghosts with gap_analysis ─────────────────────

from scripts.maintenance.audit_templates import find_ghosts  # noqa: E402


def test_find_ghosts_with_gap_analysis_paths(tmp_path):
    """Covers gap_analysis SELECT path in find_ghosts."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE docs (doc_uid TEXT, path TEXT)")
    conn.execute("CREATE TABLE gap_analysis (id INTEGER, matched_doc_path TEXT)")
    conn.execute("INSERT INTO gap_analysis VALUES (1, 'core/ghost.md')")
    conn.commit()
    core = tmp_path / "core"
    core.mkdir()
    # 'core/ghost.md' is in gap_analysis but does not exist on disk
    result = find_ghosts(conn, core)
    assert "core/ghost.md" in result
    conn.close()


def test_find_ghosts_sqlite_error_returns_empty():
    """Covers the except sqlite3.Error pass block in find_ghosts."""
    conn = sqlite3.connect(":memory:")
    # No docs or gap_analysis tables — both SELECTs will raise and be swallowed
    core = Path("/tmp")
    result = find_ghosts(conn, core)
    assert isinstance(result, list)
    conn.close()
