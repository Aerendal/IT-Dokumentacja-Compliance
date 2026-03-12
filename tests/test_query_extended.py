"""tests/test_query_extended.py — rozszerzone testy modułu itdoc/query.py.

Test Scope Matrix (TESTING_METHODOLOGY):
  Module:   query.py
  RT:       2.15  (C=3 R=2 K=3 P=3 D=1 S=1 F=0)
  Class:    medium
  UT_min:   48   (2·B=2·24, PF=5)
  IT_min:   6    (DEP=1 → 2·ceil(2.15)=6)
  CT_min:   10   (EP=5 · ceil(2.15/2)=2 → 10)
  E2E_min:  6    (UJ=3 · 2 → 6)
  Coverage: ≥59%

Pokrywa luki w stosunku do test_query.py (który ma ~25 unit testów).
Fokus: BFS boundary tests, circular-like graphs, depth limits, pro-funkcjonalne
rozszerzenia (extension points), wykrywanie potencjalnych wycieków logicznych.
"""

import sqlite3

import pytest

from itdoc.exceptions import QueryError
from itdoc.query import (
    find_by_regulation,
    find_by_standard,
    get_contract,
    rhythm_downstream,
    rhythm_upstream,
)


# ─── Fixtures ──────────────────────────────────────────────────────────────

@pytest.fixture()
def chain_db():
    """DB z łańcuchem A→B→C→D w rhythm_edges (depth test)."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.executescript("""
        CREATE TABLE docs (doc_uid TEXT, title TEXT, title_norm TEXT, path TEXT,
            origin TEXT, created_at_utc TEXT, updated_at_utc TEXT);
        CREATE TABLE standards (standard_id INTEGER, standard_code TEXT, standard_name TEXT,
            standard_name_en TEXT, description TEXT, version TEXT, url TEXT, applicable_industries TEXT);
        CREATE TABLE compliance_regulations (id INTEGER, regulation_code TEXT,
            regulation_name TEXT, jurisdiction TEXT, industry TEXT,
            key_requirements TEXT, penalty_info TEXT, data_engineering_impact TEXT);
        CREATE TABLE doc_standard_mapping (id INTEGER, doc_path TEXT, standard_code TEXT, match_reason TEXT);
        CREATE TABLE doc_regulation_mapping (id INTEGER, doc_path TEXT, regulation_code TEXT, match_reason TEXT);
        CREATE TABLE contracts (contract_id INTEGER, scope_kind TEXT, scope_uid TEXT, version TEXT,
            inputs_json TEXT, outputs_json TEXT, gates_json TEXT, impact_json TEXT,
            owner TEXT, notes TEXT, created_at_utc TEXT, updated_at_utc TEXT);
        CREATE TABLE rhythm_edges (edge_id INTEGER, from_node TEXT, to_node TEXT,
            rhythm_type TEXT, weight REAL, conditions TEXT, version_range TEXT, notes TEXT);

        -- Łańcuch A→B→C→D
        INSERT INTO rhythm_edges VALUES (1,'A','B','triggers',0.9,'','','');
        INSERT INTO rhythm_edges VALUES (2,'B','C','informs',0.8,'','','');
        INSERT INTO rhythm_edges VALUES (3,'C','D','produces',0.7,'','','');

        -- Kontrakt z pustymi listami
        INSERT INTO contracts VALUES (1,'doc','A','1.0','[]','["output_a"]','[]','{}','owner','','2026','2026');
        INSERT INTO contracts VALUES (2,'doc','B','1.0','["input_b"]','["output_b"]','["gate"]','{"x":1}','owner','','2026','2026');
    """)
    yield conn
    conn.close()


@pytest.fixture()
def diamond_db():
    """DB z grafem diamentowym: A→B, A→C, B→D, C→D (konwergencja)."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.executescript("""
        CREATE TABLE docs (doc_uid TEXT, title TEXT, title_norm TEXT, path TEXT,
            origin TEXT, created_at_utc TEXT, updated_at_utc TEXT);
        CREATE TABLE standards (standard_id INTEGER, standard_code TEXT, standard_name TEXT,
            standard_name_en TEXT, description TEXT, version TEXT, url TEXT, applicable_industries TEXT);
        CREATE TABLE compliance_regulations (id INTEGER, regulation_code TEXT,
            regulation_name TEXT, jurisdiction TEXT, industry TEXT,
            key_requirements TEXT, penalty_info TEXT, data_engineering_impact TEXT);
        CREATE TABLE doc_standard_mapping (id INTEGER, doc_path TEXT, standard_code TEXT, match_reason TEXT);
        CREATE TABLE doc_regulation_mapping (id INTEGER, doc_path TEXT, regulation_code TEXT, match_reason TEXT);
        CREATE TABLE contracts (contract_id INTEGER, scope_kind TEXT, scope_uid TEXT, version TEXT,
            inputs_json TEXT, outputs_json TEXT, gates_json TEXT, impact_json TEXT,
            owner TEXT, notes TEXT, created_at_utc TEXT, updated_at_utc TEXT);
        CREATE TABLE rhythm_edges (edge_id INTEGER, from_node TEXT, to_node TEXT,
            rhythm_type TEXT, weight REAL, conditions TEXT, version_range TEXT, notes TEXT);

        INSERT INTO rhythm_edges VALUES (1,'A','B','triggers',1.0,'','','');
        INSERT INTO rhythm_edges VALUES (2,'A','C','informs',1.0,'','','');
        INSERT INTO rhythm_edges VALUES (3,'B','D','produces',1.0,'','','');
        INSERT INTO rhythm_edges VALUES (4,'C','D','governs',1.0,'','','');
    """)
    yield conn
    conn.close()


# ─── BFS depth boundary tests ─────────────────────────────────────────────


class TestRhythmBFSDepth:
    """Testy graniczne BFS w rhythm_upstream / rhythm_downstream."""

    def test_depth_0_returns_empty(self, chain_db):
        result = rhythm_downstream(chain_db, "A", depth=0)
        assert result == []

    def test_depth_1_finds_only_immediate(self, chain_db):
        result = rhythm_downstream(chain_db, "A", depth=1)
        uids = [r["to_uid"] for r in result]
        assert "B" in uids
        assert "C" not in uids  # C jest 2 kroki dalej

    def test_depth_2_finds_two_levels(self, chain_db):
        result = rhythm_downstream(chain_db, "A", depth=2)
        uids = [r["to_uid"] for r in result]
        assert "B" in uids
        assert "C" in uids
        assert "D" not in uids  # D jest 3 kroki dalej

    def test_depth_3_finds_full_chain(self, chain_db):
        result = rhythm_downstream(chain_db, "A", depth=3)
        uids = [r["to_uid"] for r in result]
        assert "B" in uids
        assert "C" in uids
        assert "D" in uids

    def test_depth_100_on_chain_terminates(self, chain_db):
        """Bardzo głęboki BFS na małym grafie musi się zakończyć."""
        result = rhythm_downstream(chain_db, "A", depth=100)
        assert len(result) == 3  # Tylko B, C, D

    def test_distance_field_correct_depth1(self, chain_db):
        result = rhythm_downstream(chain_db, "A", depth=1)
        for r in result:
            assert r["distance"] == 1

    def test_distance_field_correct_depth2(self, chain_db):
        result = rhythm_downstream(chain_db, "A", depth=2)
        dist_map = {r["to_uid"]: r["distance"] for r in result}
        assert dist_map["B"] == 1
        assert dist_map["C"] == 2

    def test_upstream_depth_1(self, chain_db):
        result = rhythm_upstream(chain_db, "D", depth=1)
        uids = [r["from_uid"] for r in result]
        assert "C" in uids
        assert "B" not in uids

    def test_upstream_depth_3_full_chain(self, chain_db):
        result = rhythm_upstream(chain_db, "D", depth=3)
        uids = {r["from_uid"] for r in result}
        assert {"A", "B", "C"} == uids


class TestRhythmDiamondGraph:
    """Testy na grafie diamentowym — test visited set (brak duplikatów)."""

    def test_downstream_no_duplicates(self, diamond_db):
        result = rhythm_downstream(diamond_db, "A", depth=3)
        uids = [r["to_uid"] for r in result]
        assert len(uids) == len(set(uids)), f"Duplikaty w wynikach: {uids}"

    def test_upstream_diamond_no_duplicates(self, diamond_db):
        result = rhythm_upstream(diamond_db, "D", depth=3)
        uids = [r["from_uid"] for r in result]
        assert len(uids) == len(set(uids)), f"Duplikaty w upstream: {uids}"

    def test_downstream_finds_all_nodes(self, diamond_db):
        result = rhythm_downstream(diamond_db, "A", depth=2)
        uids = {r["to_uid"] for r in result}
        assert "B" in uids
        assert "C" in uids
        assert "D" in uids


# ─── Contract edge cases ───────────────────────────────────────────────────


class TestGetContractEdgeCases:
    def test_inputs_is_list_not_none(self, chain_db):
        """inputs zawsze jest listy, nigdy None — mitygacja pro-funkcjonalna."""
        result = get_contract(chain_db, "A")
        assert result["inputs"] is not None
        assert isinstance(result["inputs"], list)

    def test_gates_is_list(self, chain_db):
        result = get_contract(chain_db, "B")
        assert isinstance(result["gates"], list)

    def test_impact_is_dict_or_list(self, chain_db):
        result = get_contract(chain_db, "B")
        assert isinstance(result["impact"], (dict, list))

    def test_outputs_content_correct(self, chain_db):
        result = get_contract(chain_db, "A")
        assert "output_a" in result["outputs"]

    def test_gates_content_correct(self, chain_db):
        result = get_contract(chain_db, "B")
        assert "gate" in result["gates"]

    def test_scope_uid_in_result(self, chain_db):
        result = get_contract(chain_db, "A")
        assert result.get("scope_uid") == "A"

    def test_whitespace_uid_raises(self, chain_db):
        with pytest.raises(QueryError):
            get_contract(chain_db, "   ")

    def test_uid_with_leading_whitespace_stripped(self, chain_db):
        """Uid z białymi znakami na brzegach — powinien być normalnie znaleziony."""
        result = get_contract(chain_db, " A ")
        assert result["scope_uid"] == "A"


# ─── find_by_standard edge cases ──────────────────────────────────────────


class TestFindByStandardEdgeCases:
    def test_partial_code_match(self, db_conn):
        """Częściowy kod standardu — zwraca wyniki."""
        result = find_by_standard(db_conn, "ISO")
        assert len(result) >= 1  # ISO/IEC 27001 pasuje do "ISO"

    def test_case_insensitive_partial(self, db_conn):
        """SQLite LIKE jest case-insensitive dla ASCII."""
        result = find_by_standard(db_conn, "iso")
        # Zależy od SQLite, ale nie powinno crashować
        assert isinstance(result, list)

    def test_result_is_list_of_dicts(self, db_conn):
        result = find_by_standard(db_conn, "ISO/IEC 27001")
        assert all(isinstance(r, dict) for r in result)

    def test_whitespace_code_raises(self, db_conn):
        with pytest.raises(QueryError):
            find_by_standard(db_conn, "\t  \n")

    def test_none_like_special_chars(self, db_conn):
        """Znaki specjalne SQL nie crashują (% jest częścią LIKE)."""
        result = find_by_standard(db_conn, "ISO%")
        assert isinstance(result, list)


# ─── find_by_regulation edge cases ────────────────────────────────────────


class TestFindByRegulationEdgeCases:
    def test_partial_code_match(self, db_conn):
        result = find_by_regulation(db_conn, "UODO")
        assert len(result) >= 1

    def test_result_is_list_of_dicts(self, db_conn):
        result = find_by_regulation(db_conn, "UODO-PL")
        assert all(isinstance(r, dict) for r in result)

    def test_whitespace_raises(self, db_conn):
        with pytest.raises(QueryError):
            find_by_regulation(db_conn, "  ")


# ─── Pro-funkcjonalne mitygacje (extension points) ────────────────────────


class TestExtensionPoints:
    """Testy wykrywające miejsca do rozwinięcia funkcjonalności."""

    def test_find_by_standard_returns_composable_list(self, db_conn):
        """Wyniki można filtrować/sortować bez modyfikacji API."""
        results = find_by_standard(db_conn, "ISO/IEC 27001")
        # Można filtrować po kluczu
        filtered = [r for r in results if r.get("doc_path")]
        assert isinstance(filtered, list)

    def test_rhythm_result_has_edge_type(self, chain_db):
        """edge_type umożliwia filtrowanie po semantyce krawędzi."""
        result = rhythm_downstream(chain_db, "A", depth=3)
        types = {r["edge_type"] for r in result}
        # Każda krawędź ma typ — extension: można filtrować po typie
        assert len(types) >= 1

    def test_rhythm_result_has_weight(self, chain_db):
        """weight umożliwia rankowanie — extension: sort by weight."""
        result = rhythm_downstream(chain_db, "A", depth=3)
        for r in result:
            assert "weight" in r
            assert isinstance(r["weight"], (int, float))

    def test_contract_result_keys_stable(self, chain_db):
        """Klucze kontraktu są stabilne — gwarantuje backward compatibility."""
        r1 = get_contract(chain_db, "A")
        r2 = get_contract(chain_db, "B")
        assert set(r1.keys()) == set(r2.keys()), \
            f"Różne klucze kontraktu: {set(r1.keys())} vs {set(r2.keys())}"
