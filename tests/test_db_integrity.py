"""tests/test_db_integrity.py — testy integralności danych w DB.

Wymagają połączenia z rzeczywistą DB (fixtures: real_db_conn z conftest).
Testy są oznaczone @pytest.mark.integration i pomijane gdy DB nie istnieje.
"""

import json

import pytest

pytestmark = pytest.mark.integration

CRITICAL_TABLES = [
    "docs",
    "sections",
    "standards",
    "compliance_regulations",
    "content_links",
    "content_links_resolved",
    "rhythm_edges",
    "contracts",
    "flags",
    "_schema_version",
]


class TestCriticalTablesNotEmpty:
    @pytest.mark.parametrize("table", CRITICAL_TABLES)
    def test_table_not_empty(self, real_db_conn, table):
        count = real_db_conn.execute(f"SELECT COUNT(*) FROM [{table}]").fetchone()[0]
        assert count > 0, f"Tabela '{table}' jest pusta"


class TestLinkResolutionCoverage:
    def test_coverage_at_least_99_9_percent(self, real_db_conn):
        from itdoc.db import check_link_resolution_coverage
        cov = check_link_resolution_coverage(real_db_conn)
        assert cov >= 0.999, f"Pokrycie resolucji linków zbyt niskie: {cov:.4f} (oczekiwano ≥ 0.999)"

    def test_coverage_does_not_exceed_1(self, real_db_conn):
        from itdoc.db import check_link_resolution_coverage
        cov = check_link_resolution_coverage(real_db_conn)
        assert cov <= 1.0, f"Pokrycie > 100%: {cov}"


class TestSectionIntegrity:
    def test_no_orphaned_sections(self, real_db_conn):
        """Żadna sekcja nie może mieć doc_uid nieistniejącego w docs."""
        count = real_db_conn.execute("""
            SELECT COUNT(*) FROM sections s
            WHERE NOT EXISTS (SELECT 1 FROM docs d WHERE d.doc_uid = s.doc_uid)
        """).fetchone()[0]
        assert count == 0, f"{count} sekcji jest osieroconych (doc_uid bez docs)"

    def test_filled_sections_ratio(self, real_db_conn):
        """Sekcje ze status='filled' stanowią ≥ 99.9% wszystkich sekcji."""
        total = real_db_conn.execute("SELECT COUNT(*) FROM sections").fetchone()[0]
        filled = real_db_conn.execute(
            "SELECT COUNT(*) FROM sections WHERE status = 'filled'"
        ).fetchone()[0]
        ratio = filled / total if total > 0 else 0
        assert ratio >= 0.999, f"filled ratio: {ratio:.4f} (oczekiwano ≥ 0.999)"

    def test_every_doc_has_at_least_one_section(self, real_db_conn):
        """Każdy dokument z prawidłową ścieżką ma ≥ 1 sekcję (path='ORPHAN' to wpisy bez pliku)."""
        count = real_db_conn.execute("""
            SELECT COUNT(*) FROM docs d
            WHERE d.path IS NOT NULL
              AND d.path != 'ORPHAN'
              AND NOT EXISTS (SELECT 1 FROM sections s WHERE s.doc_uid = d.doc_uid)
        """).fetchone()[0]
        assert count == 0, f"{count} dokumentów (z path!=NULL i path!='ORPHAN') nie ma żadnej sekcji"


class TestContractIntegrity:
    def test_contracts_count_matches_docs(self, real_db_conn):
        """Liczba kontraktów (scope_kind='doc') ≈ liczba dokumentów z plikiem (non-null, non-orphan)."""
        # Liczymy tylko docs które mają plik: path IS NOT NULL AND path != 'ORPHAN'
        # Docs z path IS NULL to nierozwiązane rekordy z documents_final bez pliku — nie mają kontraktów
        doc_count = real_db_conn.execute(
            "SELECT COUNT(*) FROM docs WHERE path IS NOT NULL AND path != 'ORPHAN'"
        ).fetchone()[0]
        contract_count = real_db_conn.execute(
            "SELECT COUNT(*) FROM contracts WHERE scope_kind = 'doc'"
        ).fetchone()[0]
        # Dopuszczamy ±1% różnicy (mogły powstać duplikaty lub braki)
        ratio = contract_count / doc_count if doc_count > 0 else 0
        assert ratio >= 0.99, f"Zbyt mało kontraktów: {contract_count}/{doc_count}"

    def test_contracts_inputs_valid_json(self, real_db_conn):
        """inputs_json w kontraktach musi być poprawnym JSONem (lub NULL)."""
        bad = real_db_conn.execute("""
            SELECT COUNT(*) FROM contracts
            WHERE inputs_json IS NOT NULL AND inputs_json != ''
              AND json_valid(inputs_json) = 0
        """).fetchone()[0]
        assert bad == 0, f"{bad} kontraktów ma niepoprawny inputs_json"

    def test_contracts_outputs_valid_json(self, real_db_conn):
        """outputs_json w kontraktach musi być poprawnym JSONem (lub NULL)."""
        bad = real_db_conn.execute("""
            SELECT COUNT(*) FROM contracts
            WHERE outputs_json IS NOT NULL AND outputs_json != ''
              AND json_valid(outputs_json) = 0
        """).fetchone()[0]
        assert bad == 0, f"{bad} kontraktów ma niepoprawny outputs_json"


class TestRhythmEdgesIntegrity:
    def test_weight_in_valid_range(self, real_db_conn):
        """Waga krawędzi rhythm_edges musi być w zakresie [0, 1]."""
        bad = real_db_conn.execute("""
            SELECT COUNT(*) FROM rhythm_edges
            WHERE weight < 0 OR weight > 1
        """).fetchone()[0]
        assert bad == 0, f"{bad} krawędzi ma wagę poza zakresem [0, 1]"

    def test_rhythm_edges_count_significant(self, real_db_conn):
        """Tabela rhythm_edges musi mieć co najmniej 100k krawędzi (dane są zasilone)."""
        count = real_db_conn.execute("SELECT COUNT(*) FROM rhythm_edges").fetchone()[0]
        assert count >= 100_000, f"rhythm_edges zbyt mała: {count} (oczekiwano ≥ 100k)"


class TestSchemaVersion:
    def test_schema_version_not_empty(self, real_db_conn):
        count = real_db_conn.execute("SELECT COUNT(*) FROM _schema_version").fetchone()[0]
        assert count > 0, "_schema_version jest pusta"

    def test_validate_schema_no_errors(self, real_db_conn):
        from itdoc.db import validate_schema
        errors = validate_schema(real_db_conn)
        assert errors == [], f"validate_schema() zwróciło błędy: {errors}"
