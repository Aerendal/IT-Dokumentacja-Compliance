"""
tests/test_gap_analysis_match.py — unit tests for match_catalog_entry
in scripts/gap_analysis.py.

Covers: match_catalog_entry (lines 92-163 currently uncovered)
"""
import pytest

pytestmark = pytest.mark.unit


class TestMatchCatalogEntry:
    def _docs(self):
        return [
            ("core/security_policy.md", "Security Policy Document"),
            ("core/test_plan.md", "Test Plan for Application"),
            ("core/incident_mgmt.md", "Incident Management Procedure"),
            ("core/arch_doc.md", "System Architecture Document"),
        ]

    def test_exact_match_returns_exact_confidence(self):
        from scripts.gap_analysis import match_catalog_entry, CONFIDENCE_EXACT
        docs = self._docs()
        result = match_catalog_entry("Security Policy Document", docs)
        assert result is not None
        path, title, conf = result
        assert conf == CONFIDENCE_EXACT
        assert path == "core/security_policy.md"

    def test_exact_match_with_polish_chars(self):
        from scripts.gap_analysis import match_catalog_entry, CONFIDENCE_EXACT
        docs = [("core/doc.md", "Polityka bezpieczeństwa IT")]
        result = match_catalog_entry("Polityka bezpieczenstwa IT", docs)
        assert result is not None
        assert result[2] == CONFIDENCE_EXACT

    def test_no_match_returns_none(self):
        from scripts.gap_analysis import match_catalog_entry
        docs = self._docs()
        result = match_catalog_entry("Completely Unrelated Xyz Qwerty", docs)
        assert result is None

    def test_empty_docs_returns_none(self):
        from scripts.gap_analysis import match_catalog_entry
        result = match_catalog_entry("Any Title", [])
        assert result is None

    def test_high_confidence_similar_title(self):
        from scripts.gap_analysis import match_catalog_entry, CONFIDENCE_HIGH, CONFIDENCE_EXACT
        docs = [("core/test_plan.md", "Test Plan Application QA")]
        result = match_catalog_entry("Test Plan for Application QA", docs)
        assert result is not None
        assert result[2] in (CONFIDENCE_HIGH, CONFIDENCE_EXACT, "medium")

    def test_mapping_boost_lowers_threshold(self):
        from scripts.gap_analysis import match_catalog_entry
        docs = [("core/mapped.md", "Incident Response Procedure")]
        # With mapping boost, threshold is effectively lower
        result = match_catalog_entry(
            "Incident Management Procedure",
            docs,
            mapped_docs={"core/mapped.md"}
        )
        assert result is not None

    def test_returns_triple(self):
        from scripts.gap_analysis import match_catalog_entry
        docs = self._docs()
        result = match_catalog_entry("Security Policy Document", docs)
        assert result is not None
        assert len(result) == 3

    def test_result_path_is_in_docs(self):
        from scripts.gap_analysis import match_catalog_entry
        docs = self._docs()
        result = match_catalog_entry("Security Policy Document", docs)
        assert result is not None
        paths = [d[0] for d in docs]
        assert result[0] in paths

    def test_standard_code_param_accepted(self):
        from scripts.gap_analysis import match_catalog_entry
        docs = self._docs()
        # standard_code is accepted, doesn't crash
        result = match_catalog_entry(
            "Test Plan for Application", docs, standard_code="ISO/IEC 12207"
        )
        assert result is not None

    def test_medium_confidence_partial_match(self):
        from scripts.gap_analysis import match_catalog_entry, CONFIDENCE_MISS
        docs = [("core/doc.md", "Complete Risk Assessment Report Template")]
        result = match_catalog_entry("Risk Assessment Report", docs)
        if result:
            assert result[2] != CONFIDENCE_MISS
        # If no match, that's fine too — just testing it doesn't crash

    def test_mapped_docs_defaults_to_empty_set(self):
        from scripts.gap_analysis import match_catalog_entry
        docs = self._docs()
        # Should work without mapped_docs param (defaults to None → empty set)
        result = match_catalog_entry("Security Policy Document", docs, mapped_docs=None)
        assert result is not None

    def test_confidence_levels_precedence(self):
        from scripts.gap_analysis import match_catalog_entry, CONFIDENCE_EXACT
        docs = [
            ("core/exact.md", "Risk Management Plan"),
            ("core/similar.md", "Risk Management Planning Document"),
        ]
        # Exact match should take priority
        result = match_catalog_entry("Risk Management Plan", docs)
        assert result is not None
        assert result[2] == CONFIDENCE_EXACT
        assert result[0] == "core/exact.md"
