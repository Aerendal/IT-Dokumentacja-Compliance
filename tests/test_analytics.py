"""
tests/test_analytics.py

Testy jednostkowe i integracyjne dla itdoc/analytics.py.
Testy nowych funkcji query.py: coverage_stats, find_unmapped, find_by_category, suggest_for_doc.

Uruchom:
    cd dokumentacja
    python3 -m pytest tests/test_analytics.py -v --tb=short
"""

import sqlite3

import pytest

from itdoc.analytics import (
    coverage_by_standard,
    library_health_report,
    match_reason_distribution,
    standard_gaps,
    unmapped_by_category,
)
from itdoc.exceptions import QueryError
from itdoc.query import (
    coverage_stats,
    find_by_category,
    find_unmapped,
    suggest_for_doc,
)

pytestmark = pytest.mark.unit


# ---------------------------------------------------------------------------
# Fixture
# ---------------------------------------------------------------------------


@pytest.fixture
def analytics_db():
    """In-memory DB z reprezentatywnym zestawem danych."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.executescript("""
        CREATE TABLE docs (
            path TEXT,
            title TEXT,
            title_norm TEXT,
            doc_uid TEXT PRIMARY KEY
        );
        CREATE TABLE doc_standard_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_path TEXT,
            standard_code TEXT,
            match_reason TEXT,
            confidence REAL
        );

        -- 6 zmapowanych do 2 standardów
        INSERT INTO docs VALUES ("core/iso_access_control.md",  "Access Control Policy",  "access control policy",  "UID01");
        INSERT INTO docs VALUES ("core/iso_risk_management.md", "Risk Management Plan",   "risk management plan",   "UID02");
        INSERT INTO docs VALUES ("core/iso_incident.md",        "Incident Response Plan", "incident response plan", "UID03");
        INSERT INTO docs VALUES ("core/pmbok_project_plan.md",  "Project Plan",           "project plan",           "UID04");
        INSERT INTO docs VALUES ("core/pmbok_charter.md",       "Project Charter",        "project charter",        "UID05");
        INSERT INTO docs VALUES ("core/pmbok_scope.md",         "Scope Statement",        "scope statement",        "UID06");

        -- 3 niezmapowane
        INSERT INTO docs VALUES ("core/orphan_a.md", "Orphan A", "orphan a", "UID07");
        INSERT INTO docs VALUES ("core/orphan_b.md", "Orphan B", "orphan b", "UID08");
        INSERT INTO docs VALUES ("core/orphan_c.md", "Orphan C", "orphan c", "UID09");

        -- ORPHAN (specjalny path)
        INSERT INTO docs VALUES ("ORPHAN", "Ghost Doc", "ghost doc", "UID10");

        -- Mapowania
        INSERT INTO doc_standard_mapping VALUES (1, "core/iso_access_control.md",  "ISO27001", "keyword_match", NULL);
        INSERT INTO doc_standard_mapping VALUES (2, "core/iso_risk_management.md", "ISO27001", "keyword_match", NULL);
        INSERT INTO doc_standard_mapping VALUES (3, "core/iso_incident.md",        "ISO27001", "explicit_audit", NULL);
        INSERT INTO doc_standard_mapping VALUES (4, "core/pmbok_project_plan.md",  "PMBOK",   "keyword_match", NULL);
        INSERT INTO doc_standard_mapping VALUES (5, "core/pmbok_charter.md",       "PMBOK",   "explicit_audit", NULL);
        INSERT INTO doc_standard_mapping VALUES (6, "core/pmbok_scope.md",         "PMBOK",   "explicit_audit", NULL);

        -- candidate_match dla sugestii
        INSERT INTO doc_standard_mapping VALUES (7, "core/orphan_a.md", "ISO27001", "candidate_match", 0.75);
        INSERT INTO doc_standard_mapping VALUES (8, "core/orphan_a.md", "PMBOK",    "candidate_match", 0.40);
    """)
    yield conn
    conn.close()


# ---------------------------------------------------------------------------
# Testy coverage_by_standard
# ---------------------------------------------------------------------------


class TestCoverageByStandard:
    def test_returns_dict(self, analytics_db):
        result = coverage_by_standard(analytics_db)
        assert isinstance(result, dict)

    def test_known_standards_present(self, analytics_db):
        result = coverage_by_standard(analytics_db)
        assert "ISO27001" in result
        assert "PMBOK" in result

    def test_counts_are_correct(self, analytics_db):
        result = coverage_by_standard(analytics_db)
        # ISO27001: 3 real + 1 candidate_match (orphan_a) = 4 total
        # PMBOK: 3 real + 1 candidate_match (orphan_a) = 4 total
        assert result["ISO27001"] >= 3
        assert result["PMBOK"] >= 3

    def test_sorted_descending(self, analytics_db):
        result = coverage_by_standard(analytics_db)
        counts = list(result.values())
        assert counts == sorted(counts, reverse=True)


# ---------------------------------------------------------------------------
# Testy unmapped_by_category
# ---------------------------------------------------------------------------


class TestUnmappedByCategory:
    def test_returns_dict(self, analytics_db):
        result = unmapped_by_category(analytics_db)
        assert isinstance(result, dict)

    def test_orphan_path_excluded(self, analytics_db):
        result = unmapped_by_category(analytics_db)
        for _cat, paths in result.items():
            assert "ORPHAN" not in paths

    def test_mapped_docs_excluded(self, analytics_db):
        result = unmapped_by_category(analytics_db)
        all_paths = [p for paths in result.values() for p in paths]
        assert "core/iso_access_control.md" not in all_paths

    def test_unmapped_included(self, analytics_db):
        result = unmapped_by_category(analytics_db)
        all_paths = [p for paths in result.values() for p in paths]
        # orphan_b i orphan_c nie mają żadnych mapowań (w tym candidate_match)
        assert "core/orphan_b.md" in all_paths
        assert "core/orphan_c.md" in all_paths


# ---------------------------------------------------------------------------
# Testy standard_gaps
# ---------------------------------------------------------------------------


class TestStandardGaps:
    def test_returns_list(self, analytics_db):
        result = standard_gaps(analytics_db, min_coverage=10)
        assert isinstance(result, list)

    def test_all_below_threshold(self, analytics_db):
        result = standard_gaps(analytics_db, min_coverage=10)
        for _code, cnt in result:
            assert cnt < 10

    def test_high_threshold_catches_all(self, analytics_db):
        result = standard_gaps(analytics_db, min_coverage=100)
        codes = [r[0] for r in result]
        assert "ISO27001" in codes
        assert "PMBOK" in codes

    def test_no_gaps_when_threshold_zero(self, analytics_db):
        result = standard_gaps(analytics_db, min_coverage=0)
        assert result == []


# ---------------------------------------------------------------------------
# Testy match_reason_distribution
# ---------------------------------------------------------------------------


class TestMatchReasonDistribution:
    def test_returns_dict(self, analytics_db):
        result = match_reason_distribution(analytics_db)
        assert isinstance(result, dict)

    def test_known_reasons_present(self, analytics_db):
        result = match_reason_distribution(analytics_db)
        assert "keyword_match" in result
        assert "explicit_audit" in result
        assert "candidate_match" in result

    def test_counts_correct(self, analytics_db):
        result = match_reason_distribution(analytics_db)
        assert result["keyword_match"] == 3
        assert result["explicit_audit"] == 3
        assert result["candidate_match"] == 2


# ---------------------------------------------------------------------------
# Testy library_health_report
# ---------------------------------------------------------------------------


class TestLibraryHealthReport:
    def test_returns_string(self, analytics_db):
        report = library_health_report(analytics_db)
        assert isinstance(report, str)
        assert len(report) > 50

    def test_contains_markdown_header(self, analytics_db):
        report = library_health_report(analytics_db)
        assert "# Raport" in report

    def test_contains_summary_table(self, analytics_db):
        report = library_health_report(analytics_db)
        assert "Zmapowane szablony" in report
        assert "Niezmapowane szablony" in report

    def test_contains_standard_coverage(self, analytics_db):
        report = library_health_report(analytics_db)
        assert "ISO27001" in report
        assert "PMBOK" in report

    def test_coverage_percentage_correct(self, analytics_db):
        report = library_health_report(analytics_db)
        # 7/9 mapped (6 real + orphan_a via candidate_match) = 77.8%
        assert "77.8" in report


# ---------------------------------------------------------------------------
# Testy nowych funkcji query.py
# ---------------------------------------------------------------------------


class TestCoverageStats:
    def test_returns_dict_with_keys(self, analytics_db):
        stats = coverage_stats(analytics_db)
        for key in (
            "total_docs",
            "mapped_docs",
            "unmapped_docs",
            "coverage_pct",
            "total_mappings",
            "unique_standards",
        ):
            assert key in stats

    def test_total_minus_mapped_equals_unmapped(self, analytics_db):
        stats = coverage_stats(analytics_db)
        assert stats["total_docs"] - stats["mapped_docs"] == stats["unmapped_docs"]

    def test_coverage_pct_range(self, analytics_db):
        stats = coverage_stats(analytics_db)
        assert 0.0 <= stats["coverage_pct"] <= 100.0

    def test_unique_standards_count(self, analytics_db):
        stats = coverage_stats(analytics_db)
        # Zliczamy tylko w keyword_match/explicit_audit, nie candidate_match (ale to też wlicza)
        assert stats["unique_standards"] >= 2


class TestFindUnmapped:
    def test_returns_list(self, analytics_db):
        result = find_unmapped(analytics_db, limit=10)
        assert isinstance(result, list)

    def test_mapped_not_in_results(self, analytics_db):
        result = find_unmapped(analytics_db, limit=10)
        paths = [r["path"] for r in result]
        assert "core/iso_access_control.md" not in paths
        assert "core/pmbok_charter.md" not in paths

    def test_limit_respected(self, analytics_db):
        result = find_unmapped(analytics_db, limit=2)
        assert len(result) <= 2

    def test_invalid_limit_raises(self, analytics_db):
        with pytest.raises(QueryError):
            find_unmapped(analytics_db, limit=0)

    def test_result_has_path_field(self, analytics_db):
        result = find_unmapped(analytics_db, limit=5)
        for row in result:
            assert "path" in row


class TestFindByCategory:
    def test_returns_list(self, analytics_db):
        result = find_by_category(analytics_db, "core")
        assert isinstance(result, list)

    def test_empty_category_raises(self, analytics_db):
        with pytest.raises(QueryError):
            find_by_category(analytics_db, "")

    def test_nonexistent_category_returns_empty(self, analytics_db):
        result = find_by_category(analytics_db, "nonexistent_xyz_category_9999")
        assert result == []


class TestSuggestForDoc:
    def test_returns_candidates_for_known_doc(self, analytics_db):
        result = suggest_for_doc(analytics_db, "core/orphan_a.md")
        assert len(result) == 2

    def test_best_first(self, analytics_db):
        result = suggest_for_doc(analytics_db, "core/orphan_a.md")
        scores = [r["confidence"] for r in result]
        assert scores == sorted(scores, reverse=True)

    def test_no_candidates_for_mapped_doc(self, analytics_db):
        result = suggest_for_doc(analytics_db, "core/iso_access_control.md")
        assert result == []

    def test_empty_path_raises(self, analytics_db):
        with pytest.raises(QueryError):
            suggest_for_doc(analytics_db, "")

    def test_result_has_standard_code(self, analytics_db):
        result = suggest_for_doc(analytics_db, "core/orphan_a.md")
        for row in result:
            assert "standard_code" in row
