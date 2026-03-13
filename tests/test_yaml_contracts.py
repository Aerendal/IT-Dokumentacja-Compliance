"""
test_yaml_contracts.py — Testy kontraktowe dla plików YAML w config/.

Cel: wykryć breaking changes w strukturze danych zanim trafiają do runtime.
Testujemy realne pliki — zero mockowania.

Hierarchia wg "Jak pisać testy.md": Krok 3 — Contract tests.
"""

from __future__ import annotations

import pytest
import yaml
from pathlib import Path

# Ścieżka do katalogu config/ — katalog projektu jest dwa poziomy nad tests/
_CONFIG = Path(__file__).parent.parent / "config"
_BASE_DICTS = _CONFIG / "base_dicts"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load(path: Path) -> dict | list:
    """Ładuje YAML i zwraca sparsowany obiekt."""
    return yaml.safe_load(path.read_text(encoding="utf-8"))


# ===========================================================================
# standards_catalog.yaml
# ===========================================================================

class TestStandardsCatalogContract:
    """Kontrakt dla config/standards_catalog.yaml."""

    @pytest.fixture(scope="class")
    def catalog(self) -> dict:
        return _load(_CONFIG / "standards_catalog.yaml")

    def test_file_exists(self):
        assert (_CONFIG / "standards_catalog.yaml").is_file()

    def test_top_level_is_dict(self, catalog):
        assert isinstance(catalog, dict), "Top-level musi być dict[standard_code -> list]"

    def test_has_minimum_standards(self, catalog):
        assert len(catalog) >= 44, f"Oczekiwano ≥ 44 standardów, mamy {len(catalog)}"

    def test_all_values_are_lists(self, catalog):
        for code, entries in catalog.items():
            assert isinstance(entries, list), f"Standard {code!r}: wartość musi być listą"

    def test_all_entries_are_dicts(self, catalog):
        for code, entries in catalog.items():
            for i, entry in enumerate(entries):
                assert isinstance(entry, dict), f"{code}[{i}]: każdy wpis musi być dict"

    def test_required_fields_present(self, catalog):
        required_fields = {"doc_type_id", "title", "required", "category"}
        for code, entries in catalog.items():
            for i, entry in enumerate(entries):
                missing = required_fields - entry.keys()
                assert not missing, f"{code}[{i}]: brakuje pól {missing}"

    def test_doc_type_id_is_string(self, catalog):
        for code, entries in catalog.items():
            for i, entry in enumerate(entries):
                assert isinstance(entry["doc_type_id"], str), (
                    f"{code}[{i}].doc_type_id musi być stringiem"
                )
                assert entry["doc_type_id"].strip(), (
                    f"{code}[{i}].doc_type_id nie może być pustym stringiem"
                )

    def test_title_is_nonempty_string(self, catalog):
        for code, entries in catalog.items():
            for i, entry in enumerate(entries):
                assert isinstance(entry["title"], str) and entry["title"].strip(), (
                    f"{code}[{i}].title musi być niepustym stringiem"
                )

    def test_required_field_is_bool(self, catalog):
        for code, entries in catalog.items():
            for i, entry in enumerate(entries):
                assert isinstance(entry["required"], bool), (
                    f"{code}[{i}].required musi być booleanem, got {type(entry['required'])}"
                )

    def test_url_starts_with_http_when_present(self, catalog):
        for code, entries in catalog.items():
            for i, entry in enumerate(entries):
                url = entry.get("url")
                if url:
                    assert str(url).startswith("http"), (
                        f"{code}[{i}].url musi zaczynać się od 'http', got {url!r}"
                    )

    def test_doc_type_id_unique_within_standard(self, catalog):
        for code, entries in catalog.items():
            ids = [e["doc_type_id"] for e in entries]
            duplicates = {x for x in ids if ids.count(x) > 1}
            assert not duplicates, (
                f"Standard {code!r}: zduplikowane doc_type_id: {duplicates}"
            )

    def test_known_standards_present(self, catalog):
        for standard in ["ISO/IEC 27001", "NIST CSF"]:
            assert standard in catalog, f"Standard {standard!r} musi być w katalogu"


# ===========================================================================
# doc_archetypes.yaml
# ===========================================================================

class TestDocArchetypesContract:
    """Kontrakt dla config/doc_archetypes.yaml."""

    @pytest.fixture(scope="class")
    def archetypes(self) -> list[dict]:
        data = _load(_CONFIG / "doc_archetypes.yaml")
        return data["archetypes"]

    def test_file_exists(self):
        assert (_CONFIG / "doc_archetypes.yaml").is_file()

    def test_top_key_is_archetypes(self):
        data = _load(_CONFIG / "doc_archetypes.yaml")
        assert "archetypes" in data, "Top-level klucz musi być 'archetypes'"

    def test_archetypes_is_list(self, archetypes):
        assert isinstance(archetypes, list)

    def test_has_minimum_archetypes(self, archetypes):
        assert len(archetypes) >= 34, f"Oczekiwano ≥ 34 archetypów, mamy {len(archetypes)}"

    def test_all_entries_are_dicts(self, archetypes):
        for i, a in enumerate(archetypes):
            assert isinstance(a, dict), f"archetypes[{i}] musi być dict"

    def test_required_fields_present(self, archetypes):
        required = {"name", "keywords", "purpose", "inputs", "outputs"}
        for i, a in enumerate(archetypes):
            missing = required - a.keys()
            assert not missing, f"archetypes[{i}] ({a.get('name', '?')}): brakuje pól {missing}"

    def test_name_is_nonempty_string(self, archetypes):
        for i, a in enumerate(archetypes):
            assert isinstance(a["name"], str) and a["name"].strip(), (
                f"archetypes[{i}].name musi być niepustym stringiem"
            )

    def test_keywords_is_list(self, archetypes):
        """keywords musi być listą. Tylko 'generic' (catch-all fallback) może mieć pustą listę."""
        for i, a in enumerate(archetypes):
            assert isinstance(a["keywords"], list), (
                f"archetypes[{i}] ({a['name']}): keywords musi być listą"
            )

    def test_keywords_nonempty_except_generic_catchall(self, archetypes):
        """Każdy archetype poza 'generic' musi mieć co najmniej jedno słowo kluczowe."""
        for i, a in enumerate(archetypes):
            if a["name"] == "generic":
                continue  # generic = catch-all fallback, celowo bez keywords
            assert len(a["keywords"]) > 0, (
                f"archetypes[{i}] ({a['name']}): keywords nie może być pustą listą"
            )

    def test_names_are_unique(self, archetypes):
        names = [a["name"] for a in archetypes]
        duplicates = {x for x in names if names.count(x) > 1}
        assert not duplicates, f"Zduplikowane nazwy archetypów: {duplicates}"

    def test_purpose_is_nonempty_string(self, archetypes):
        for i, a in enumerate(archetypes):
            assert isinstance(a["purpose"], str) and a["purpose"].strip(), (
                f"archetypes[{i}] ({a['name']}): purpose musi być niepustym stringiem"
            )


# ===========================================================================
# standard_rules.yaml
# ===========================================================================

class TestStandardRulesContract:
    """Kontrakt dla config/standard_rules.yaml."""

    @pytest.fixture(scope="class")
    def rules(self) -> list[dict]:
        data = _load(_CONFIG / "standard_rules.yaml")
        return data["rules"]

    def test_file_exists(self):
        assert (_CONFIG / "standard_rules.yaml").is_file()

    def test_top_key_is_rules(self):
        data = _load(_CONFIG / "standard_rules.yaml")
        assert "rules" in data

    def test_rules_is_list(self, rules):
        assert isinstance(rules, list)

    def test_has_minimum_rules(self, rules):
        assert len(rules) >= 21

    def test_each_rule_has_keywords_and_standards(self, rules):
        for i, rule in enumerate(rules):
            assert "keywords" in rule, f"rules[{i}]: brak pola 'keywords'"
            assert "standards" in rule, f"rules[{i}]: brak pola 'standards'"

    def test_keywords_is_nonempty_list(self, rules):
        for i, rule in enumerate(rules):
            assert isinstance(rule["keywords"], list) and rule["keywords"], (
                f"rules[{i}].keywords musi być niepustą listą"
            )

    def test_standards_is_nonempty_list(self, rules):
        for i, rule in enumerate(rules):
            assert isinstance(rule["standards"], list) and rule["standards"], (
                f"rules[{i}].standards musi być niepustą listą"
            )

    def test_all_keywords_are_strings(self, rules):
        for i, rule in enumerate(rules):
            for kw in rule["keywords"]:
                assert isinstance(kw, str), f"rules[{i}]: keyword {kw!r} musi być stringiem"

    def test_all_standards_are_strings(self, rules):
        for i, rule in enumerate(rules):
            for s in rule["standards"]:
                assert isinstance(s, str), f"rules[{i}]: standard {s!r} musi być stringiem"


# ===========================================================================
# regulation_rules.yaml (naprawiony bug z refaktoru Fazy 1C)
# ===========================================================================

class TestRegulationRulesContract:
    """Kontrakt dla config/regulation_rules.yaml — plik odzyskany podczas naprawy bugu."""

    @pytest.fixture(scope="class")
    def rules(self) -> list[dict]:
        data = _load(_CONFIG / "regulation_rules.yaml")
        return data["regulation_rules"]

    def test_file_exists(self):
        assert (_CONFIG / "regulation_rules.yaml").is_file()

    def test_top_key_is_regulation_rules(self):
        data = _load(_CONFIG / "regulation_rules.yaml")
        assert "regulation_rules" in data

    def test_rules_is_list(self, rules):
        assert isinstance(rules, list)

    def test_has_minimum_rules(self, rules):
        assert len(rules) >= 12

    def test_each_rule_has_keywords_and_standards(self, rules):
        for i, rule in enumerate(rules):
            assert "keywords" in rule, f"regulation_rules[{i}]: brak 'keywords'"
            assert "standards" in rule, f"regulation_rules[{i}]: brak 'standards'"

    def test_keywords_is_nonempty_list(self, rules):
        for i, rule in enumerate(rules):
            assert isinstance(rule["keywords"], list) and rule["keywords"], (
                f"regulation_rules[{i}].keywords musi być niepustą listą"
            )

    def test_standards_is_nonempty_list(self, rules):
        for i, rule in enumerate(rules):
            assert isinstance(rule["standards"], list) and rule["standards"], (
                f"regulation_rules[{i}].standards musi być niepustą listą"
            )


@pytest.mark.parametrize("filename,top_key,min_len,required_fields", [
    ("roles.yaml",               "roles",              40, {"code", "name_pl", "name_en", "description"}),
    ("phases.yaml",              "phases",             23, {"name_pl", "name_en", "category"}),
    ("industries.yaml",          "industries",         30, {"code", "name_pl", "name_en"}),
    ("document_categories.yaml", "document_categories", 15, {"code", "name_pl", "name_en"}),
    ("rel_types.yaml",           "rel_types",          10, {"code", "name_pl", "name_en"}),
    ("quality_dims.yaml",        "quality_dims",        8, {"dimension", "name_pl", "name_en"}),
])
class TestBaseDictsContract:
    """Kontrakty dla config/base_dicts/*.yaml — wspólna logika przez parametryzację."""

    def test_file_exists(self, filename, top_key, min_len, required_fields):
        assert (_BASE_DICTS / filename).is_file(), f"Plik {filename} nie istnieje"

    def test_top_key_present(self, filename, top_key, min_len, required_fields):
        data = _load(_BASE_DICTS / filename)
        assert top_key in data, f"{filename}: oczekiwano klucza {top_key!r}"

    def test_list_is_nonempty(self, filename, top_key, min_len, required_fields):
        data = _load(_BASE_DICTS / filename)
        entries = data[top_key]
        assert isinstance(entries, list) and len(entries) >= min_len, (
            f"{filename}: oczekiwano ≥ {min_len} wpisów, mamy {len(entries) if isinstance(entries, list) else '?'}"
        )

    def test_all_entries_are_dicts(self, filename, top_key, min_len, required_fields):
        data = _load(_BASE_DICTS / filename)
        for i, entry in enumerate(data[top_key]):
            assert isinstance(entry, dict), f"{filename}[{i}]: każdy wpis musi być dict"

    def test_required_fields_present(self, filename, top_key, min_len, required_fields):
        data = _load(_BASE_DICTS / filename)
        for i, entry in enumerate(data[top_key]):
            missing = required_fields - entry.keys()
            assert not missing, f"{filename}[{i}]: brakuje pól {missing}"

    def test_required_fields_nonempty(self, filename, top_key, min_len, required_fields):
        data = _load(_BASE_DICTS / filename)
        for i, entry in enumerate(data[top_key]):
            for field in required_fields:
                val = entry[field]
                # None lub pusty string = błąd
                assert val is not None, f"{filename}[{i}].{field} = None"
                if isinstance(val, str):
                    assert val.strip(), f"{filename}[{i}].{field} jest pustym stringiem"
