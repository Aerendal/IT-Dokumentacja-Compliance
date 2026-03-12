"""Tests for scripts/maintenance/backfill_mapping_confidence.py"""

import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts" / "maintenance"))
from backfill_mapping_confidence import (
    add_evidence_column,
    build_caches,
    doc_title_from_path,
    get_real_title,
    rough_slug,
    score_row,
    tokenize,
)
from backfill_mapping_confidence import (
    jaccard as _jaccard,
)

# ---------------------------------------------------------------------------
# Fixture
# ---------------------------------------------------------------------------


@pytest.fixture
def conn():
    c = sqlite3.connect(":memory:")
    c.row_factory = sqlite3.Row
    c.executescript("""
    CREATE TABLE doc_standard_mapping (
        id INTEGER PRIMARY KEY,
        doc_path TEXT,
        standard_code TEXT,
        match_reason TEXT,
        confidence REAL,
        evidence TEXT
    );
    CREATE TABLE standards (
        standard_code TEXT PRIMARY KEY,
        standard_name TEXT,
        description TEXT,
        applicable_industries TEXT,
        url TEXT,
        version TEXT
    );
    CREATE TABLE doc_section_guidance (
        id INTEGER PRIMARY KEY,
        doc_title TEXT,
        section_title TEXT,
        guidance TEXT,
        standards_refs TEXT,
        regulations_refs TEXT
    );
    INSERT INTO standards VALUES (
        'ISO/IEC 27001', 'ISMS',
        'security management information systems controls',
        'IT', '', '2022'
    );
    INSERT INTO standards VALUES (
        'NIST CSF', 'NIST Framework',
        'cybersecurity framework identify protect detect respond',
        'IT', '', '2.0'
    );
    """)
    c.commit()
    return c


# ---------------------------------------------------------------------------
# tokenize
# ---------------------------------------------------------------------------


def test_tokenize_basic():
    result = tokenize("Security Management Systems")
    assert "security" in result
    assert "systems" in result


def test_tokenize_removes_stopwords():
    result = tokenize("the security of it")
    assert "the" not in result
    assert "of" not in result
    assert "it" not in result
    assert "security" in result


def test_tokenize_polish():
    result = tokenize("Zarządzanie bezpieczeństwem informatycznym")
    # Polish chars are normalized: bezpieczeństwem→bezpieczenstwem (maps to 'security')
    # informatycznym stays as is; zarządzanie is in STOP list
    assert "informatycznym" in result or "security" in result or "bezpieczenstwem" in result


def test_tokenize_short_words_excluded():
    result = tokenize("go do it to be")
    # all words ≤2 chars should be excluded
    for w in result:
        assert len(w) >= 3, f"Short word '{w}' should not appear"


def test_tokenize_returns_set():
    result = tokenize("foo bar foo")
    assert isinstance(result, set)
    assert len(result) == len(set(result))  # no duplicates


def test_tokenize_empty_string():
    assert tokenize("") == set()


# ---------------------------------------------------------------------------
# jaccard
# ---------------------------------------------------------------------------


def test_jaccard_identical():
    assert _jaccard({"a", "b"}, {"a", "b"}) == pytest.approx(1.0)


def test_jaccard_disjoint():
    assert _jaccard({"a"}, {"b"}) == pytest.approx(0.0)


def test_jaccard_partial():
    result = _jaccard({"a", "b", "c"}, {"b", "c", "d"})
    assert result == pytest.approx(2 / 4)


def test_jaccard_empty_sets():
    assert _jaccard(set(), set()) == pytest.approx(0.0)


def test_jaccard_one_empty():
    assert _jaccard({"a", "b"}, set()) == pytest.approx(0.0)


# ---------------------------------------------------------------------------
# Confidence / score_row
# ---------------------------------------------------------------------------


def test_confidence_capped_at_1(conn):
    # Insert a standard whose description fully overlaps a doc title
    conn.execute(
        "INSERT INTO standards VALUES ('TEST-STD', 'Test', 'alpha beta gamma delta epsilon', 'IT', '', '1.0')"
    )
    # Also add guidance so bonus = 0.3
    conn.execute(
        "INSERT INTO doc_section_guidance VALUES (1, 'alpha beta gamma delta epsilon', 'sec', 'g', '[\"TEST-STD\"]', '[]')"
    )
    conn.commit()
    standards_cache, guidance_cache, _ = build_caches(conn)

    row = {"doc_path": "alpha_beta_gamma_delta_epsilon.md", "standard_code": "TEST-STD"}
    confidence, evidence = score_row(row, standards_cache, guidance_cache)
    assert confidence <= 1.0


def test_evidence_string_format(conn):
    standards_cache, guidance_cache, _ = build_caches(conn)
    row = {"doc_path": "information_security_controls.md", "standard_code": "ISO/IEC 27001"}
    _, evidence = score_row(row, standards_cache, guidance_cache)
    assert "tokens:" in evidence
    assert "guidance_refs:" in evidence


def test_no_match_gives_low_confidence(conn):
    standards_cache, guidance_cache, _ = build_caches(conn)
    row = {"doc_path": "cooking_recipes_pasta.md", "standard_code": "ISO/IEC 27001"}
    confidence, _ = score_row(row, standards_cache, guidance_cache)
    assert confidence < 0.3


def test_related_title_gives_higher_confidence(conn):
    standards_cache, guidance_cache, _ = build_caches(conn)
    row = {"doc_path": "information_security_controls_isms.md", "standard_code": "ISO/IEC 27001"}
    confidence, _ = score_row(row, standards_cache, guidance_cache)
    assert confidence > 0.3


# ---------------------------------------------------------------------------
# add_evidence_column
# ---------------------------------------------------------------------------


def test_add_evidence_column_idempotent(conn):
    """Calling twice must not raise."""
    add_evidence_column(conn)
    add_evidence_column(conn)  # second call must be a no-op


# ---------------------------------------------------------------------------
# build_caches
# ---------------------------------------------------------------------------


def test_build_caches_returns_standards(conn):
    standards_cache, _, __ = build_caches(conn)
    assert "ISO/IEC 27001" in standards_cache
    assert "NIST CSF" in standards_cache


def test_build_caches_guidance_populated(conn):
    conn.execute(
        "INSERT INTO doc_section_guidance VALUES (1, 'My Doc', 'sec', 'g', '[\"ISO/IEC 27001\"]', '[]')"
    )
    conn.commit()
    _, guidance_cache, __ = build_caches(conn)
    assert ("my doc", "ISO/IEC 27001") in guidance_cache


# ---------------------------------------------------------------------------
# doc_title_from_path
# ---------------------------------------------------------------------------


def test_doc_title_from_path_replaces_underscores():
    assert doc_title_from_path("foo/bar_baz_qux.md") == "bar baz qux"


def test_doc_title_from_path_strips_extension():
    result = doc_title_from_path("docs/security_policy.pdf")
    assert ".pdf" not in result
    assert "security" in result


# ---------------------------------------------------------------------------
# rough_slug / get_real_title
# ---------------------------------------------------------------------------


def test_rough_slug_polish():
    slug = rough_slug("Zarządzanie bezpieczeństwem")
    # Must contain no Polish diacritics
    polish_chars = set("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ")
    assert not any(c in polish_chars for c in slug), f"Polish chars left in slug: {slug}"
    assert slug  # non-empty


def test_get_real_title_fallback():
    # Unknown path → fallback: underscores→spaces, strip .md
    result = get_real_title("core/unknown.md", {})
    assert result == "unknown"
