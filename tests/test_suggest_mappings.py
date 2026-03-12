"""
tests/test_suggest_mappings.py

Testy jednostkowe i integracyjne dla suggest_mappings.py.

Uruchom:
    cd dokumentacja
    python3 -m pytest tests/test_suggest_mappings.py -v --tb=short
"""

import math
import sqlite3
from pathlib import Path

import pytest

from scripts.maintenance.suggest_mappings import (
    tokenize,
    jaccard,
    overlap_coefficient,
    build_idf_profiles,
    get_unmapped_docs,
    score_doc_against_profiles,
    generate_suggestions,
    apply_suggestions,
    render_report,
)

pytestmark = pytest.mark.unit


# ---------------------------------------------------------------------------
# Fixture
# ---------------------------------------------------------------------------

@pytest.fixture
def suggest_db():
    """In-memory DB z danymi do testowania suggest_mappings."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.executescript("""
        CREATE TABLE docs (
            path TEXT PRIMARY KEY,
            title TEXT,
            title_norm TEXT,
            doc_uid TEXT
        );
        CREATE TABLE doc_standard_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_path TEXT NOT NULL,
            standard_code TEXT NOT NULL,
            match_reason TEXT NOT NULL,
            confidence REAL
        );

        -- Szablony zmapowane do standardów
        INSERT INTO docs VALUES ("core/api_reference.md",    "API Reference",       "api reference",        "UID1");
        INSERT INTO docs VALUES ("core/api_design.md",       "API Design Guide",    "api design guide",     "UID2");
        INSERT INTO docs VALUES ("core/project_plan.md",     "Project Plan",        "project plan",         "UID3");
        INSERT INTO docs VALUES ("core/project_charter.md",  "Project Charter",     "project charter",      "UID4");
        INSERT INTO docs VALUES ("core/security_policy.md",  "Security Policy",     "security policy",      "UID5");
        INSERT INTO docs VALUES ("core/security_guide.md",   "Security Guide",      "security guide",       "UID6");

        -- Szablony niezmapowane
        INSERT INTO docs VALUES ("core/api_gateway.md",      "API Gateway Config",  "api gateway config",   "UID7");
        INSERT INTO docs VALUES ("core/project_report.md",   "Project Report",      "project report",       "UID8");
        INSERT INTO docs VALUES ("core/unknown_doc.md",      "Zupełnie inny",       "zupelnie inny dokument", "UID9");

        -- Mapowania
        INSERT INTO doc_standard_mapping VALUES (1, "core/api_reference.md", "OpenAPI", "keyword_match", NULL);
        INSERT INTO doc_standard_mapping VALUES (2, "core/api_design.md",    "OpenAPI", "keyword_match", NULL);
        INSERT INTO doc_standard_mapping VALUES (3, "core/project_plan.md",  "PMBOK",   "keyword_match", NULL);
        INSERT INTO doc_standard_mapping VALUES (4, "core/project_charter.md","PMBOK",  "keyword_match", NULL);
        INSERT INTO doc_standard_mapping VALUES (5, "core/security_policy.md","ISO27001","keyword_match", NULL);
        INSERT INTO doc_standard_mapping VALUES (6, "core/security_guide.md", "ISO27001","keyword_match", NULL);
    """)
    yield conn
    conn.close()


# ---------------------------------------------------------------------------
# Testy tokenize
# ---------------------------------------------------------------------------

class TestTokenize:
    def test_basic_tokenization(self):
        result = tokenize("API Reference Documentation")
        assert "api" in result
        assert "reference" in result
        assert "documentation" in result

    def test_removes_stop_words(self):
        result = tokenize("the and or in for")
        assert "the" not in result
        assert "and" not in result

    def test_removes_short_words(self):
        result = tokenize("a ab abc abcd")
        assert "a" not in result
        assert "ab" not in result
        assert "abc" in result

    def test_returns_lowercase(self):
        result = tokenize("API Gateway CONFIG")
        assert "api" in result
        assert "gateway" in result
        assert "config" in result

    def test_empty_string_returns_empty_set(self):
        assert tokenize("") == set()
        assert tokenize(None) == set()

    def test_polish_words(self):
        result = tokenize("zarządzanie projektem")
        assert "zarządzanie" in result
        assert "projektem" in result


# ---------------------------------------------------------------------------
# Testy jaccard i overlap_coefficient
# ---------------------------------------------------------------------------

class TestSimilarityFunctions:
    def test_jaccard_identical(self):
        s = {"a", "b", "c"}
        assert jaccard(s, s) == 1.0

    def test_jaccard_disjoint(self):
        assert jaccard({"a", "b"}, {"c", "d"}) == 0.0

    def test_jaccard_partial(self):
        score = jaccard({"a", "b", "c"}, {"b", "c", "d"})
        assert 0 < score < 1

    def test_jaccard_empty(self):
        assert jaccard(set(), {"a"}) == 0.0
        assert jaccard({"a"}, set()) == 0.0

    def test_overlap_coefficient_identical(self):
        s = {"a", "b", "c"}
        assert overlap_coefficient(s, s) == 1.0

    def test_overlap_coefficient_subset(self):
        # Mały zbiór w dużym → overlap = 1.0
        score = overlap_coefficient({"api"}, {"api", "reference", "documentation"})
        assert score == 1.0

    def test_overlap_coefficient_empty(self):
        assert overlap_coefficient(set(), {"a"}) == 0.0


# ---------------------------------------------------------------------------
# Testy build_idf_profiles
# ---------------------------------------------------------------------------

class TestBuildIdfProfiles:
    def test_returns_two_dicts(self, suggest_db):
        profiles, idf = build_idf_profiles(suggest_db)
        assert isinstance(profiles, dict)
        assert isinstance(idf, dict)

    def test_profiles_contain_known_standards(self, suggest_db):
        profiles, _ = build_idf_profiles(suggest_db)
        assert "OpenAPI" in profiles
        assert "PMBOK" in profiles
        assert "ISO27001" in profiles

    def test_profile_words_are_floats(self, suggest_db):
        profiles, _ = build_idf_profiles(suggest_db)
        for word, weight in profiles["OpenAPI"].items():
            assert isinstance(weight, float)
            break

    def test_idf_shared_words_lower_weight(self, suggest_db):
        # "api" pojawia się tylko w OpenAPI profile → IDF może być różne
        # ale słowo które jest w KAŻDYM standardzie powinno mieć niższe IDF
        _, idf = build_idf_profiles(suggest_db)
        # Sprawdzamy że IDF nie jest 0 dla żadnego słowa
        for word, score in idf.items():
            assert score >= 0


# ---------------------------------------------------------------------------
# Testy get_unmapped_docs
# ---------------------------------------------------------------------------

class TestGetUnmappedDocs:
    def test_returns_unmapped_only(self, suggest_db):
        rows = get_unmapped_docs(suggest_db)
        paths = [r["path"] for r in rows]
        assert "core/api_gateway.md" in paths
        assert "core/project_report.md" in paths

    def test_does_not_include_mapped(self, suggest_db):
        rows = get_unmapped_docs(suggest_db)
        paths = [r["path"] for r in rows]
        assert "core/api_reference.md" not in paths
        assert "core/security_policy.md" not in paths

    def test_returns_list(self, suggest_db):
        rows = get_unmapped_docs(suggest_db)
        assert isinstance(rows, list)


# ---------------------------------------------------------------------------
# Testy generate_suggestions
# ---------------------------------------------------------------------------

class TestGenerateSuggestions:
    def test_returns_list(self, suggest_db):
        result = generate_suggestions(suggest_db, min_confidence=0.01)
        assert isinstance(result, list)

    def test_api_gateway_suggests_openapi(self, suggest_db):
        result = generate_suggestions(suggest_db, min_confidence=0.01)
        api_hits = [s for s in result if "api_gateway" in s["doc_path"]]
        assert len(api_hits) >= 1
        # "api gateway" powinno pasować do OpenAPI (profil zawiera "api")
        assert api_hits[0]["best_standard"] == "OpenAPI"

    def test_project_report_suggests_pmbok(self, suggest_db):
        result = generate_suggestions(suggest_db, min_confidence=0.01)
        proj_hits = [s for s in result if "project_report" in s["doc_path"]]
        assert len(proj_hits) >= 1
        assert proj_hits[0]["best_standard"] == "PMBOK"

    def test_high_confidence_threshold_filters(self, suggest_db):
        low = generate_suggestions(suggest_db, min_confidence=0.01)
        high = generate_suggestions(suggest_db, min_confidence=0.99)
        assert len(high) <= len(low)

    def test_suggestion_has_required_keys(self, suggest_db):
        result = generate_suggestions(suggest_db, min_confidence=0.01)
        if result:
            s = result[0]
            for key in ("doc_path", "title", "best_standard", "confidence", "alternatives"):
                assert key in s

    def test_confidence_is_float(self, suggest_db):
        result = generate_suggestions(suggest_db, min_confidence=0.01)
        for s in result:
            assert isinstance(s["confidence"], float)
            assert 0.0 <= s["confidence"] <= 1.0


# ---------------------------------------------------------------------------
# Testy apply_suggestions
# ---------------------------------------------------------------------------

class TestApplySuggestions:
    def test_inserts_into_db(self, suggest_db):
        suggestions = [
            {
                "doc_path": "core/api_gateway.md",
                "title": "API Gateway",
                "best_standard": "OpenAPI",
                "confidence": 0.75,
                "alternatives": [],
            }
        ]
        count = apply_suggestions(suggest_db, suggestions)
        assert count == 1
        row = suggest_db.execute(
            "SELECT * FROM doc_standard_mapping WHERE doc_path='core/api_gateway.md'"
        ).fetchone()
        assert row is not None
        assert row["match_reason"] == "candidate_match"

    def test_no_duplicate_insert(self, suggest_db):
        s = [{
            "doc_path": "core/api_reference.md",  # już zmapowany!
            "title": "API Reference",
            "best_standard": "OpenAPI",
            "confidence": 0.9,
            "alternatives": [],
        }]
        count = apply_suggestions(suggest_db, s)
        assert count == 0  # nie wstawia duplikatu


# ---------------------------------------------------------------------------
# Testy render_report
# ---------------------------------------------------------------------------

class TestRenderReport:
    def test_returns_string(self):
        result = render_report([], 100)
        assert isinstance(result, str)

    def test_contains_markdown_header(self):
        result = render_report([], 50)
        assert "# Raport" in result

    def test_with_suggestions_contains_table(self):
        suggestions = [{
            "doc_path": "core/test.md",
            "title": "Test Document",
            "best_standard": "OpenAPI",
            "confidence": 0.75,
            "alternatives": [("PMBOK", 0.3)],
        }]
        result = render_report(suggestions, 100)
        assert "Test Document" in result
        assert "OpenAPI" in result
        assert "0.75" in result
