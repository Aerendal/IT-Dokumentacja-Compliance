"""
test_yaml_loaders.py — Unit testy dla YAML loaderów wydzielonych w refaktorze Fazy 1.

Cel: weryfikacja że loadery zwracają poprawne typy i zachowują backward compatibility.
Testujemy na realnych plikach config/ — zero mockowania loaderów.

Hierarchia wg "Jak pisać testy.md": Krok 1 — Unit tests.
"""

from __future__ import annotations

import pytest
import yaml
from pathlib import Path

# ---------------------------------------------------------------------------
# build_standards_catalog — _load_catalog_data() i CATALOG
# ---------------------------------------------------------------------------

class TestBuildStandardsCatalogLoader:
    """Unit testy dla _load_catalog_data() i CATALOG w build_standards_catalog.py."""

    @pytest.fixture(scope="class")
    def catalog_data(self):
        from scripts.build_standards_catalog import _load_catalog_data
        return _load_catalog_data()

    def test_returns_dict(self, catalog_data):
        assert isinstance(catalog_data, dict)

    def test_has_minimum_44_standards(self, catalog_data):
        assert len(catalog_data) >= 44

    def test_values_are_lists_of_dicts(self, catalog_data):
        for code, entries in catalog_data.items():
            assert isinstance(entries, list), f"{code}: wartość musi być listą"
            for i, entry in enumerate(entries):
                assert isinstance(entry, dict), f"{code}[{i}]: wpis musi być dict"

    def test_each_entry_has_doc_type_id(self, catalog_data):
        for code, entries in catalog_data.items():
            for entry in entries:
                assert "doc_type_id" in entry, f"{code}: brakuje doc_type_id"

    def test_each_entry_has_required_bool(self, catalog_data):
        for code, entries in catalog_data.items():
            for entry in entries:
                assert isinstance(entry.get("required"), bool), (
                    f"{code}: required musi być booleanem"
                )

    def test_known_standards_present(self, catalog_data):
        assert "ISO/IEC 27001" in catalog_data
        assert "NIST CSF" in catalog_data

    def test_module_level_catalog_constant(self):
        """CATALOG moduł-level jest załadowany przy imporcie."""
        from scripts.build_standards_catalog import CATALOG
        assert isinstance(CATALOG, dict)
        assert len(CATALOG) >= 44

    def test_catalog_access_by_key_name(self, catalog_data):
        """Refaktor: dostęp przez nazwy pól, nie indeksy tuple."""
        first_standard = list(catalog_data.keys())[0]
        first_entry = catalog_data[first_standard][0]
        # Musi działać dostęp po nazwie klucza
        assert "doc_type_id" in first_entry
        assert "title" in first_entry
        assert "required" in first_entry


# ---------------------------------------------------------------------------
# enrich_placeholders — _load_archetypes()
# ---------------------------------------------------------------------------

class TestEnrichPlaceholdersLoader:
    """Unit testy dla _load_archetypes() w enrich_placeholders.py."""

    @pytest.fixture(scope="class")
    def archetypes(self):
        from scripts.maintenance.enrich_placeholders import _load_archetypes
        return _load_archetypes()

    def test_returns_list(self, archetypes):
        assert isinstance(archetypes, list)

    def test_has_minimum_34_archetypes(self, archetypes):
        assert len(archetypes) >= 34

    def test_each_element_is_tuple(self, archetypes):
        """Backward compat: _load_archetypes() zwraca tuple, nie dict."""
        for i, arch in enumerate(archetypes):
            assert isinstance(arch, tuple), (
                f"archetypes[{i}]: element musi być krotką (backward compat)"
            )

    def test_tuple_has_7_elements(self, archetypes):
        """Format: (keywords, purpose, inputs, outputs, impacts, dependencies, relationships)."""
        for i, arch in enumerate(archetypes):
            assert len(arch) == 7, (
                f"archetypes[{i}]: krotka musi mieć 7 elementów, ma {len(arch)}"
            )

    def test_first_element_is_keywords_list(self, archetypes):
        """arch[0] = keywords (lista stringów)."""
        for i, arch in enumerate(archetypes):
            assert isinstance(arch[0], list), (
                f"archetypes[{i}][0] (keywords) musi być listą"
            )

    def test_purpose_is_string(self, archetypes):
        """arch[1] = purpose (string)."""
        for i, arch in enumerate(archetypes):
            assert isinstance(arch[1], str) and arch[1].strip(), (
                f"archetypes[{i}][1] (purpose) musi być niepustym stringiem"
            )

    def test_module_level_archetypes_constant(self):
        """ARCHETYPES moduł-level jest załadowany przy imporcie."""
        from scripts.maintenance.enrich_placeholders import ARCHETYPES
        assert isinstance(ARCHETYPES, list)
        assert len(ARCHETYPES) >= 34

    def test_last_archetype_is_generic_catch_all(self, archetypes):
        """Ostatni archetype to 'generic' — catch-all z pustymi keywords."""
        last = archetypes[-1]
        assert last[0] == [], "Ostatni archetype (generic) musi mieć puste keywords []"


# ---------------------------------------------------------------------------
# map_standards_to_docs — _load_rules()
# ---------------------------------------------------------------------------

class TestMapStandardsLoader:
    """Unit testy dla _load_rules() w map_standards_to_docs.py."""

    @pytest.fixture(scope="class")
    def rules(self):
        from scripts.map_standards_to_docs import _load_rules
        return _load_rules()

    def test_returns_list_of_tuples(self, rules):
        """Backward compat: _load_rules() zwraca list[tuple[list,list]]."""
        assert isinstance(rules, list)
        for i, rule in enumerate(rules):
            assert isinstance(rule, tuple), f"rules[{i}]: musi być krotką"
            assert len(rule) == 2, f"rules[{i}]: krotka musi mieć 2 elementy (keywords, standards)"

    def test_each_keywords_is_list(self, rules):
        for i, (kws, standards) in enumerate(rules):
            assert isinstance(kws, list), f"rules[{i}][0] (keywords) musi być listą"

    def test_each_standards_is_list(self, rules):
        for i, (kws, standards) in enumerate(rules):
            assert isinstance(standards, list), f"rules[{i}][1] (standards) musi być listą"

    def test_has_minimum_21_rules(self, rules):
        assert len(rules) >= 21

    def test_all_keywords_are_strings(self, rules):
        for i, (kws, _) in enumerate(rules):
            for kw in kws:
                assert isinstance(kw, str), f"rules[{i}]: keyword {kw!r} musi być stringiem"

    def test_all_standards_are_strings(self, rules):
        for i, (_, standards) in enumerate(rules):
            for s in standards:
                assert isinstance(s, str), f"rules[{i}]: standard {s!r} musi być stringiem"

    def test_module_level_standard_rules_constant(self):
        from scripts.map_standards_to_docs import STANDARD_RULES
        assert isinstance(STANDARD_RULES, list)
        assert len(STANDARD_RULES) >= 21

    def test_module_level_regulation_rules_constant(self):
        """REGULATION_RULES jest załadowany przy imporcie (naprawiony bug z refaktoru Fazy 1C)."""
        from scripts.map_standards_to_docs import REGULATION_RULES
        assert isinstance(REGULATION_RULES, list)
        assert len(REGULATION_RULES) >= 12

    def test_iso27001_present_in_some_rule(self, rules):
        all_standards = [s for _, standards in rules for s in standards]
        assert "ISO/IEC 27001" in all_standards, "ISO/IEC 27001 musi być w regułach mapowania"


# ---------------------------------------------------------------------------
# seed_base_dicts — _load_dict() i _load_as_tuples()
# ---------------------------------------------------------------------------

class TestSeedBaseDictsLoader:
    """Unit testy dla _load_dict() i _load_as_tuples() w seed_base_dicts.py."""

    def test_load_dict_roles_returns_list_of_dicts(self):
        from scripts.seed_base_dicts import _load_dict
        result = _load_dict("roles")
        assert isinstance(result, list)
        assert len(result) >= 40
        for entry in result:
            assert isinstance(entry, dict)

    def test_load_dict_roles_has_expected_keys(self):
        from scripts.seed_base_dicts import _load_dict
        result = _load_dict("roles")
        for entry in result:
            assert "code" in entry
            assert "name_pl" in entry
            assert "name_en" in entry

    def test_load_dict_phases_minimum_count(self):
        from scripts.seed_base_dicts import _load_dict
        result = _load_dict("phases")
        assert len(result) >= 23

    @pytest.mark.parametrize("dict_name,min_len", [
        ("roles", 40),
        ("phases", 23),
        ("industries", 30),
        ("document_categories", 15),
        ("rel_types", 10),
        ("quality_dims", 8),
    ])
    def test_all_base_dicts_load(self, dict_name, min_len):
        from scripts.seed_base_dicts import _load_dict
        result = _load_dict(dict_name)
        assert len(result) >= min_len, (
            f"{dict_name}: oczekiwano ≥ {min_len} wpisów, mamy {len(result)}"
        )

    def test_load_dict_nonexistent_raises(self):
        from scripts.seed_base_dicts import _load_dict
        with pytest.raises((FileNotFoundError, OSError)):
            _load_dict("nieistniejacy_slownik_xyz")

    def test_load_as_tuples_roles_returns_tuples(self):
        from scripts.seed_base_dicts import _load_as_tuples
        fields = ["code", "name_pl", "name_en", "description"]
        result = _load_as_tuples("roles", fields)
        assert isinstance(result, list)
        for t in result:
            assert isinstance(t, tuple)
            assert len(t) == 4

    def test_load_as_tuples_preserves_field_order(self):
        from scripts.seed_base_dicts import _load_as_tuples, _load_dict
        fields = ["code", "name_pl", "name_en", "description"]
        tuples = _load_as_tuples("roles", fields)
        dicts = _load_dict("roles")
        # Pierwsza krotka musi odpowiadać pierwszemu dict w tej samej kolejności pól
        first_tuple = tuples[0]
        first_dict = dicts[0]
        assert first_tuple[0] == first_dict["code"]
        assert first_tuple[1] == first_dict["name_pl"]
        assert first_tuple[2] == first_dict["name_en"]

    def test_load_as_tuples_length_matches_dict(self):
        from scripts.seed_base_dicts import _load_as_tuples, _load_dict
        fields = ["code", "name_pl", "name_en", "description"]
        tuples = _load_as_tuples("roles", fields)
        dicts = _load_dict("roles")
        assert len(tuples) == len(dicts)

    def test_module_level_constants_are_loaded(self):
        """ROLES, PHASES itd. są załadowane przy imporcie modułu."""
        from scripts.seed_base_dicts import ROLES, PHASES, INDUSTRIES, DOC_CATEGORIES, REL_TYPES, QUALITY_DIMS
        assert len(ROLES) >= 40
        assert len(PHASES) >= 23
        assert len(INDUSTRIES) >= 30
        assert len(DOC_CATEGORIES) >= 15
        assert len(REL_TYPES) >= 10
        assert len(QUALITY_DIMS) >= 8

    def test_roles_tuples_backward_compat(self):
        """Backward compat: ROLES[i][0] = code, [1] = name_pl, [2] = name_en, [3] = description."""
        from scripts.seed_base_dicts import ROLES
        first = ROLES[0]
        assert isinstance(first[0], str), "ROLES[0][0] (code) musi być stringiem"
        assert isinstance(first[1], str), "ROLES[0][1] (name_pl) musi być stringiem"
        assert isinstance(first[2], str), "ROLES[0][2] (name_en) musi być stringiem"
