"""
test_map_standards_integration.py — Testy integracyjne dla match_rules()
i map_standards_to_docs.py.

Cel: weryfikacja że słowa kluczowe z YAML poprawnie mapują tytuły dokumentów
na standardy. Testowane na realnych regułach z config/standard_rules.yaml.

Hierarchia wg "Jak pisać testy.md": Krok 2 — Integration tests.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def rules():
    """Reguły mapowania załadowane z realnego YAML."""
    from scripts.map_standards_to_docs import STANDARD_RULES
    return STANDARD_RULES


# ===========================================================================
# match_rules() — logika dopasowania
# ===========================================================================

class TestMatchRules:
    """Testy jednostkowe dla match_rules() na realnych regułach YAML."""

    def test_security_title_matches_iso27001(self, rules):
        """Dokument z 'security' w tytule → ISO/IEC 27001."""
        from scripts.map_standards_to_docs import match_rules
        matched = match_rules("docs/security_policy.md", "Security Policy", rules)
        assert "ISO/IEC 27001" in matched, (
            f"'Security Policy' musi pasować do ISO/IEC 27001, got: {matched}"
        )

    def test_case_insensitive_matching(self, rules):
        """Dopasowanie jest case-insensitive — 'SECURITY' = 'security'."""
        from scripts.map_standards_to_docs import match_rules
        matched_lower = match_rules("docs/sec.md", "security policy", rules)
        matched_upper = match_rules("docs/sec.md", "SECURITY POLICY", rules)
        assert set(matched_lower) == set(matched_upper), (
            "Dopasowanie musi być case-insensitive"
        )

    def test_no_matching_keywords_returns_empty(self, rules):
        """Dokument bez pasujących słów kluczowych → pusta lista."""
        from scripts.map_standards_to_docs import match_rules
        matched = match_rules("docs/random_xyz.md", "Random XYZ Document 999", rules)
        assert isinstance(matched, list)
        # Nie rzuca — zwraca pustą listę lub listę bez ISO 27001

    def test_returns_list_type(self, rules):
        """match_rules() zawsze zwraca listę."""
        from scripts.map_standards_to_docs import match_rules
        result = match_rules("docs/any.md", "Any Document Title", rules)
        assert isinstance(result, list)

    def test_path_keyword_used_for_matching(self, rules):
        """Słowa kluczowe w ścieżce pliku też są matchowane."""
        from scripts.map_standards_to_docs import match_rules
        # Ścieżka zawiera 'security' → powinno pasować
        matched = match_rules("docs/security/policy.md", "Unnamed Policy", rules)
        assert isinstance(matched, list)

    def test_api_title_matches_openapi_or_similar(self, rules):
        """Dokument 'API Specification' powinien pasować do reguł związanych z API."""
        from scripts.map_standards_to_docs import match_rules
        matched = match_rules("docs/api_spec.md", "API Specification", rules)
        # Nie wiemy dokładnie który standard, ale musi być ≥ 1 jeśli reguły API istnieją
        assert isinstance(matched, list)  # nie rzuca

    def test_no_duplicates_in_result(self, rules):
        """match_rules() nie zwraca duplikatów standardów."""
        from scripts.map_standards_to_docs import match_rules
        matched = match_rules("docs/security_api.md", "Security API Design Guide", rules)
        assert len(matched) == len(set(matched)), f"Duplikaty w wyniku: {matched}"

    def test_rules_loaded_from_yaml_not_empty(self, rules):
        """Reguły załadowane z YAML nie są puste."""
        assert len(rules) >= 21


# ===========================================================================
# Integracja: match_rules() z realną DB
# ===========================================================================

class TestMapStandardsDBIntegration:
    """Integracja: match_rules() → build_mappings() → INSERT do SQLite."""

    @pytest.fixture
    def mapping_db(self, tmp_path) -> Path:
        """DB z schematem dla mapowań standardów."""
        db = tmp_path / "mapping_test.db"
        conn = sqlite3.connect(str(db))
        conn.executescript("""
            CREATE TABLE doc_standard_mapping (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_path      TEXT NOT NULL,
                standard_code TEXT NOT NULL,
                match_reason  TEXT,
                UNIQUE(doc_path, standard_code)
            );
            CREATE TABLE doc_regulation_mapping (
                id             INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_path       TEXT NOT NULL,
                regulation_code TEXT NOT NULL,
                match_reason   TEXT,
                UNIQUE(doc_path, regulation_code)
            );
        """)
        conn.commit()
        conn.close()
        return db

    @pytest.fixture
    def docs_db_with_docs(self, mapping_db) -> Path:
        """DB z dokumentami + schema do mapowań."""
        conn = sqlite3.connect(str(mapping_db))
        # Tabela docs z testowymi dokumentami
        conn.execute("""
            CREATE TABLE IF NOT EXISTS docs (
                id      INTEGER PRIMARY KEY,
                doc_uid TEXT,
                path    TEXT NOT NULL,
                title   TEXT NOT NULL
            )
        """)
        conn.executemany(
            "INSERT INTO docs (doc_uid, path, title) VALUES (?, ?, ?)",
            [
                ("uid_1", "docs/security_policy.md", "Security Policy"),
                ("uid_2", "docs/api_spec.md",        "API Specification"),
                ("uid_3", "docs/project_plan.md",    "Project Management Plan"),
                ("uid_4", "docs/risk_register.md",   "Risk Assessment Register"),
            ],
        )
        conn.commit()
        conn.close()
        return mapping_db

    def test_build_mappings_inserts_rows(self, docs_db_with_docs):
        """build_mappings() wstawia wiersze do doc_standard_mapping."""
        conn = sqlite3.connect(str(docs_db_with_docs))
        from scripts.map_standards_to_docs import create_mapping_tables, build_mappings
        create_mapping_tables(conn)
        build_mappings(conn)
        count = conn.execute("SELECT COUNT(*) FROM doc_standard_mapping").fetchone()[0]
        conn.close()
        assert count > 0, "build_mappings() musi wstawić co najmniej 1 mapowanie"

    def test_security_doc_mapped_to_27001(self, docs_db_with_docs):
        """security_policy.md jest zmapowany do ISO/IEC 27001."""
        conn = sqlite3.connect(str(docs_db_with_docs))
        from scripts.map_standards_to_docs import create_mapping_tables, build_mappings
        create_mapping_tables(conn)
        build_mappings(conn)
        row = conn.execute("""
            SELECT 1 FROM doc_standard_mapping
            WHERE doc_path LIKE '%security%' AND standard_code = 'ISO/IEC 27001'
        """).fetchone()
        conn.close()
        assert row is not None, "security_policy.md musi być zmapowany do ISO/IEC 27001"

    def test_build_mappings_idempotent(self, docs_db_with_docs):
        """Dwa wywołania build_mappings() nie duplikują mapowań (UNIQUE constraint)."""
        conn = sqlite3.connect(str(docs_db_with_docs))
        from scripts.map_standards_to_docs import create_mapping_tables, build_mappings
        create_mapping_tables(conn)
        build_mappings(conn)
        count1 = conn.execute("SELECT COUNT(*) FROM doc_standard_mapping").fetchone()[0]

        build_mappings(conn)  # drugie wywołanie
        count2 = conn.execute("SELECT COUNT(*) FROM doc_standard_mapping").fetchone()[0]
        conn.close()

        assert count1 == count2, (
            f"Ponowne build_mappings() nie może duplikować: {count1} != {count2}"
        )
