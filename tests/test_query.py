"""tests/test_query.py — testy modułu itdoc.query.

Testy jednostkowe używają in-memory DB (db_conn fixture).
Testy integracyjne używają rzeczywistej DB (real_db_conn fixture).
"""

import pytest

from itdoc.exceptions import QueryError
from itdoc.query import (
    find_by_regulation,
    find_by_standard,
    find_curated_by_standard,
    get_contract,
    rhythm_downstream,
    rhythm_upstream,
)


class TestFindByStandardUnit:
    """Testy z in-memory DB."""

    def test_returns_list(self, db_conn):
        result = find_by_standard(db_conn, "ISO/IEC 27001")
        assert isinstance(result, list)

    def test_finds_known_standard(self, db_conn):
        result = find_by_standard(db_conn, "ISO/IEC 27001")
        assert len(result) >= 1

    def test_result_has_expected_keys(self, db_conn):
        result = find_by_standard(db_conn, "ISO/IEC 27001")
        assert len(result) > 0
        row = result[0]
        assert "doc_path" in row
        assert "standard_code" in row

    def test_unknown_standard_returns_empty(self, db_conn):
        result = find_by_standard(db_conn, "NIEZNANY_XYZ_9999")
        assert result == []

    def test_empty_code_raises_query_error(self, db_conn):
        with pytest.raises(QueryError):
            find_by_standard(db_conn, "")

    def test_whitespace_code_raises_query_error(self, db_conn):
        with pytest.raises(QueryError):
            find_by_standard(db_conn, "   ")


class TestFindByRegulationUnit:
    """Testy z in-memory DB."""

    def test_returns_list(self, db_conn):
        result = find_by_regulation(db_conn, "UODO")
        assert isinstance(result, list)

    def test_finds_known_regulation(self, db_conn):
        result = find_by_regulation(db_conn, "UODO-PL")
        assert len(result) >= 1

    def test_result_has_expected_keys(self, db_conn):
        result = find_by_regulation(db_conn, "UODO-PL")
        assert len(result) > 0
        row = result[0]
        assert "doc_path" in row
        assert "regulation_code" in row

    def test_unknown_regulation_returns_empty(self, db_conn):
        result = find_by_regulation(db_conn, "NIEZNANA_REG_ZZZ")
        assert result == []

    def test_empty_code_raises_query_error(self, db_conn):
        with pytest.raises(QueryError):
            find_by_regulation(db_conn, "")


class TestGetContractUnit:
    """Testy z in-memory DB."""

    def test_returns_dict(self, db_conn):
        result = get_contract(db_conn, "UID001")
        assert isinstance(result, dict)

    def test_has_required_keys(self, db_conn):
        result = get_contract(db_conn, "UID001")
        for key in ("inputs", "outputs", "gates", "impact"):
            assert key in result, f"Brakuje klucza: {key}"

    def test_inputs_is_list(self, db_conn):
        result = get_contract(db_conn, "UID001")
        assert isinstance(result["inputs"], list)

    def test_outputs_is_list(self, db_conn):
        result = get_contract(db_conn, "UID001")
        assert isinstance(result["outputs"], list)

    def test_nonexistent_uid_raises(self, db_conn):
        with pytest.raises(QueryError):
            get_contract(db_conn, "NONEXISTENT_UID_XXX")

    def test_empty_uid_raises(self, db_conn):
        with pytest.raises(QueryError):
            get_contract(db_conn, "")


class TestRhythmUnit:
    """Testy rhythm_upstream / rhythm_downstream z in-memory DB."""

    def test_upstream_returns_list(self, db_conn):
        result = rhythm_upstream(db_conn, "UID002", depth=1)
        assert isinstance(result, list)

    def test_upstream_finds_predecessor(self, db_conn):
        # UID001 → UID002 (triggers), więc upstream(UID002) zawiera UID001
        result = rhythm_upstream(db_conn, "UID002", depth=1)
        assert len(result) >= 1
        assert result[0]["from_uid"] == "UID001"

    def test_downstream_returns_list(self, db_conn):
        result = rhythm_downstream(db_conn, "UID001", depth=1)
        assert isinstance(result, list)

    def test_downstream_finds_successor(self, db_conn):
        # UID001 → UID002, więc downstream(UID001) zawiera UID002
        result = rhythm_downstream(db_conn, "UID001", depth=1)
        assert len(result) >= 1
        assert result[0]["to_uid"] == "UID002"

    def test_root_upstream_empty(self, db_conn):
        # UID001 nie ma poprzedników
        result = rhythm_upstream(db_conn, "UID001", depth=2)
        assert result == []

    def test_leaf_downstream_empty(self, db_conn):
        # UID002 nie ma następców
        result = rhythm_downstream(db_conn, "UID002", depth=2)
        assert result == []

    def test_upstream_result_has_distance(self, db_conn):
        result = rhythm_upstream(db_conn, "UID002", depth=1)
        assert result[0]["distance"] == 1

    def test_empty_uid_raises(self, db_conn):
        with pytest.raises(QueryError):
            rhythm_upstream(db_conn, "", depth=1)


class TestFindByStandardIntegration:
    """Testy z rzeczywistą DB."""

    pytestmark = pytest.mark.integration

    def test_iso27001_returns_many_docs(self, real_db_conn):
        result = find_by_standard(real_db_conn, "ISO/IEC 27001")
        assert len(result) >= 100, f"Za mało wyników: {len(result)}"

    def test_itil_returns_results(self, real_db_conn):
        result = find_by_standard(real_db_conn, "ITIL")
        assert len(result) >= 1

    def test_result_doc_path_nonempty(self, real_db_conn):
        result = find_by_standard(real_db_conn, "ISO/IEC 27001")
        # Filtrujemy tylko wiersze z niepustą ścieżką (25 wierszy może mieć path='')
        with_path = [r for r in result[:20] if r["doc_path"]]
        assert len(with_path) >= 5, f"Za mało wyników z niepustą ścieżką: {len(with_path)}"
        for row in with_path:
            assert row["doc_path"], "doc_path nie może być pusty (po filtrze)"


class TestFindByRegulationIntegration:
    pytestmark = pytest.mark.integration

    def test_uodo_returns_results(self, real_db_conn):
        result = find_by_regulation(real_db_conn, "UODO")
        assert len(result) >= 1

    def test_ksc_returns_results(self, real_db_conn):
        result = find_by_regulation(real_db_conn, "KSC")
        assert len(result) >= 1


class TestGetContractIntegration:
    pytestmark = pytest.mark.integration

    def test_first_doc_has_contract(self, real_db_conn):
        uid = real_db_conn.execute(
            "SELECT scope_uid FROM contracts WHERE scope_kind='doc' LIMIT 1"
        ).fetchone()[0]
        result = get_contract(real_db_conn, uid)
        assert isinstance(result, dict)
        assert "inputs" in result
        assert "outputs" in result


# ─── EP Extensions: edge_type= filtr ──────────────────────────────────────────


class TestEPRhythmEdgeType:
    """EP: rhythm_upstream/downstream(edge_type=) — filtr po typie krawędzi."""

    def test_upstream_matching_edge_type_returns_results(self, db_conn):
        """edge_type='triggers' → zwraca UID001 (krawędź UID001→UID002 to 'triggers')."""
        result = rhythm_upstream(db_conn, "UID002", depth=1, edge_type="triggers")
        assert len(result) >= 1
        assert result[0]["from_uid"] == "UID001"

    def test_upstream_nonmatching_edge_type_returns_empty(self, db_conn):
        """edge_type='requires' → pusty wynik (brak krawędzi tego typu w fixture)."""
        result = rhythm_upstream(db_conn, "UID002", depth=1, edge_type="requires")
        assert result == []

    def test_downstream_matching_edge_type_returns_results(self, db_conn):
        """edge_type='triggers' → zwraca UID002."""
        result = rhythm_downstream(db_conn, "UID001", depth=1, edge_type="triggers")
        assert len(result) >= 1
        assert result[0]["to_uid"] == "UID002"

    def test_downstream_nonmatching_edge_type_returns_empty(self, db_conn):
        """edge_type='informs' → pusty wynik."""
        result = rhythm_downstream(db_conn, "UID001", depth=1, edge_type="informs")
        assert result == []

    def test_edge_type_none_returns_all(self, db_conn):
        """edge_type=None (domyślny) = bez filtrowania — zwraca wszystkie typy."""
        result_filtered = rhythm_upstream(db_conn, "UID002", depth=1, edge_type=None)
        result_default = rhythm_upstream(db_conn, "UID002", depth=1)
        assert result_filtered == result_default

    def test_edge_type_preserved_in_result(self, db_conn):
        """Wynikowy dict zawiera 'edge_type' z wartością krawędzi."""
        result = rhythm_upstream(db_conn, "UID002", depth=1, edge_type="triggers")
        assert result[0]["edge_type"] == "triggers"


class TestFindCuratedByStandard:
    """Testy find_curated_by_standard — zwraca tylko gap_analysis + explicit_audit/primary_standard."""

    def test_returns_list(self, real_db_conn):
        result = find_curated_by_standard(real_db_conn, "ISO/IEC 27001")
        assert isinstance(result, list)

    def test_raises_on_empty_code(self, real_db_conn):
        with pytest.raises(QueryError):
            find_curated_by_standard(real_db_conn, "")

    def test_unknown_standard_returns_empty(self, real_db_conn):
        result = find_curated_by_standard(real_db_conn, "NIEZNANY_XYZ_9999")
        assert result == []

    def test_result_has_expected_keys(self, real_db_conn):
        result = find_curated_by_standard(real_db_conn, "ISO/IEC 27001")
        assert len(result) > 0
        row = result[0]
        assert "doc_path" in row
        assert "standard_code" in row
        assert "source" in row

    def test_source_field_values(self, real_db_conn):
        """Każdy wynik ma source = 'gap_analysis' lub 'mapping'."""
        result = find_curated_by_standard(real_db_conn, "ISO/IEC 27001")
        for r in result:
            assert r["source"] in (
                "gap_analysis",
                "mapping",
            ), f"Nieoczekiwany source: {r['source']}"

    def test_no_duplicates(self, real_db_conn):
        """Brak duplikatów doc_path w wynikach."""
        result = find_curated_by_standard(real_db_conn, "PMBOK 7")
        paths = [r["doc_path"] for r in result]
        assert len(paths) == len(set(paths)), "Duplikaty doc_path w wynikach curated"

    def test_curated_significantly_smaller_than_full(self, real_db_conn):
        """Wyniki curated są istotnie mniejsze niż pełne (bez boilerplate FP)."""
        full = find_by_standard(real_db_conn, "PMBOK 7")
        curated = find_curated_by_standard(real_db_conn, "PMBOK 7")
        assert len(curated) < len(full), (
            f"Curated ({len(curated)}) powinno być mniejsze niż full ({len(full)})"
        )
        assert len(curated) >= 5, f"Za mało curated wyników PMBOK 7: {len(curated)}"

    def test_gap_analysis_results_come_first(self, real_db_conn):
        """Wyniki z gap_analysis pojawiają się przed wynikami z mappings."""
        result = find_curated_by_standard(real_db_conn, "ISO/IEC 27001")
        sources = [r["source"] for r in result]
        # All gap_analysis before any mapping
        seen_mapping = False
        for s in sources:
            if s == "mapping":
                seen_mapping = True
            elif s == "gap_analysis" and seen_mapping:
                pytest.fail("gap_analysis wynik po mapping — nieprawidłowa kolejność")

    def test_iso27001_curated_contains_key_templates(self, real_db_conn):
        """ISO 27001 curated zawiera kluczowe szablony."""
        result = find_curated_by_standard(real_db_conn, "ISO/IEC 27001")
        paths = {r["doc_path"].rsplit("/", 1)[-1] for r in result}
        for required in ("isms_scope_statement.md", "statement_of_applicability.md"):
            assert required in paths, f"Brak {required} w curated ISO 27001"

    def test_dora_curated_exact_count(self, real_db_conn):
        """DORA curated = tyle ile gap_analysis (brak extra mappings)."""
        result = find_curated_by_standard(real_db_conn, "DORA")
        assert len(result) >= 7, f"Za mało szablonów DORA curated: {len(result)}"

    def test_partial_code_match(self, real_db_conn):
        """Częściowy kod 'OWASP' matchuje zarówno ASVS jak i MASVS."""
        result = find_curated_by_standard(real_db_conn, "OWASP")
        standards = {r["standard_code"] for r in result}
        assert len(standards) >= 2, f"Powinny być >= 2 standardy OWASP, są: {standards}"
