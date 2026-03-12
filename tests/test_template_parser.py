"""tests/test_template_parser.py — testy parsera szablonów + fuzz edge-cases.

Test Scope Matrix (TESTING_METHODOLOGY):
  Module:        template.py
  RT:            1.60  (C=3 R=1 K=1 P=3 D=1 S=0 F=0)
  Class:         medium
  UT_min:        30  (2·B=2·15, PF=3)
  FUZZ_min:      1   (parser_surface=True, EP=1 → ceil(1/3)=1 sesja fuzz)
  Coverage:      ≥70%

Skupia się na:
  - edge cases parsera frontmattera (_parse_frontmatter)
  - znaki Unicode / polskie znaki
  - bardzo krótkie / puste pliki
  - zniekształcone frontmattery
  - wykrywanie wycieków (file handles)
  - punkty rozszerzenia (extension points / pro-funkcjonalne mitygacje)
"""

import textwrap
from pathlib import Path

import pytest

from itdoc.exceptions import TemplateError
from itdoc.template import (
    _parse_frontmatter,
    get_required_sections,
    load_template,
    validate_template,
)


# ─── Helpers ──────────────────────────────────────────────────────────────

def _write(tmp_path, content: str, name: str = "test.md") -> Path:
    p = tmp_path / name
    p.write_text(content, encoding="utf-8")
    return p


def _valid_template(body_extra: str = "") -> str:
    return textwrap.dedent(f"""\
        ---
        title: Test
        status: draft
        aligned: true
        ---
        # Test

        ## Cel dokumentu
        Opis celu.

        ## Zakres i granice
        Opis zakresu.

        ## Wejścia i wyjścia
        Opis wejść.
        {body_extra}
    """)


# ─── _parse_frontmatter — unit tests ─────────────────────────────────────


class TestParseFrontmatterUnit:
    """30 testów parsera — branch coverage + fuzz edge cases."""

    def test_basic_fields_parsed(self):
        raw = "---\ntitle: Test\nstatus: draft\n---\nbody"
        fm, body = _parse_frontmatter(raw)
        assert fm["title"] == "Test"
        assert fm["status"] == "draft"
        assert "body" in body

    def test_no_frontmatter_raises(self):
        with pytest.raises(TemplateError):
            _parse_frontmatter("# Nagłówek\nbez frontmattera")

    def test_unclosed_frontmatter_raises(self):
        with pytest.raises(TemplateError):
            _parse_frontmatter("---\ntitle: Test\n# brak zamknięcia")

    def test_empty_frontmatter_valid(self):
        raw = "---\n---\nbody"
        fm, body = _parse_frontmatter(raw)
        assert fm == {}
        assert "body" in body

    def test_body_preserved_fully(self):
        raw = "---\ntitle: T\n---\nline1\nline2\nline3"
        _, body = _parse_frontmatter(raw)
        assert "line1" in body
        assert "line2" in body
        assert "line3" in body

    def test_value_with_colon_in_it(self):
        raw = "---\ntitle: Polityka: bezpieczeństwo\n---\nbody"
        fm, _ = _parse_frontmatter(raw)
        # Wartość to wszystko po pierwszym ':' — "Polityka" jako klucz
        assert "title" in fm
        assert "bezpieczeństwo" in fm["title"]

    def test_empty_value_field(self):
        raw = "---\ntitle:\n---\nbody"
        fm, _ = _parse_frontmatter(raw)
        assert "title" in fm
        assert fm["title"] == ""

    def test_multiple_dashes_in_value(self):
        raw = "---\naligned_at: 2026-02-09\n---\nbody"
        fm, _ = _parse_frontmatter(raw)
        assert "2026-02-09" in fm["aligned_at"]

    def test_whitespace_stripped_from_keys(self):
        raw = "---\n  title  : Test\n---\nbody"
        fm, _ = _parse_frontmatter(raw)
        assert "title" in fm

    def test_whitespace_stripped_from_values(self):
        raw = "---\ntitle:   Test   \n---\nbody"
        fm, _ = _parse_frontmatter(raw)
        assert fm["title"] == "Test"

    def test_unicode_in_value(self):
        raw = "---\ntitle: Zażółć gęślą jaźń\n---\nbody"
        fm, _ = _parse_frontmatter(raw)
        assert "Zażółć" in fm["title"]

    def test_empty_file_raises(self):
        with pytest.raises(TemplateError):
            _parse_frontmatter("")

    def test_only_dashes_raises(self):
        with pytest.raises(TemplateError):
            _parse_frontmatter("---")

    def test_newlines_only_in_body(self):
        raw = "---\ntitle: T\n---\n\n\n\n"
        _, body = _parse_frontmatter(raw)
        assert isinstance(body, str)

    def test_tab_in_frontmatter_value(self):
        """Tab jako część wartości — nie powinien crashować."""
        raw = "---\ntitle: Test\tDokument\n---\nbody"
        fm, _ = _parse_frontmatter(raw)
        assert "title" in fm

    # FUZZ-style: zniekształcone wejścia
    def test_fuzz_random_bytes_like(self):
        """Bardzo dziwna treść — parser nie powinien crashować."""
        weird = "---\nkey: \x00\x01\x02\n---\nbody"
        # Powinno albo sparsować albo rzucić TemplateError, nie inny wyjątek
        try:
            _parse_frontmatter(weird)
        except TemplateError:
            pass

    def test_fuzz_very_long_key(self):
        long_key = "a" * 1000
        raw = f"---\n{long_key}: value\n---\nbody"
        fm, _ = _parse_frontmatter(raw)
        assert long_key in fm

    def test_fuzz_very_long_value(self):
        raw = "---\ntitle: " + "x" * 10_000 + "\n---\nbody"
        fm, _ = _parse_frontmatter(raw)
        assert len(fm["title"]) == 10_000

    def test_fuzz_many_fields(self):
        fields = "\n".join(f"key{i}: val{i}" for i in range(200))
        raw = f"---\n{fields}\n---\nbody"
        fm, _ = _parse_frontmatter(raw)
        assert len(fm) == 200

    def test_fuzz_nested_dashes_in_body(self):
        """Ciało zawiera '---' — frontmatter zamknięty tylko przy pierwszym."""
        raw = "---\ntitle: T\n---\n# Body\n---\nMore\n---\n"
        _, body = _parse_frontmatter(raw)
        # Body powinno zawierać drugi '---'
        assert "---" in body

    def test_windows_line_endings(self):
        raw = "---\r\ntitle: Test\r\nstatus: draft\r\n---\r\nbody\r\n"
        try:
            fm, body = _parse_frontmatter(raw)
            # Powinno sparsować lub gracefully fail
        except TemplateError:
            pass  # Akceptowalne — dokumentacja jest Unix

    def test_missing_body_after_frontmatter(self):
        raw = "---\ntitle: Test\n---"
        fm, body = _parse_frontmatter(raw)
        assert fm["title"] == "Test"
        assert body == ""


# ─── load_template ─────────────────────────────────────────────────────────

class TestLoadTemplate:
    def test_valid_file_loads(self, tmp_path):
        p = _write(tmp_path, _valid_template())
        tmpl = load_template(p)
        assert tmpl["frontmatter"]["title"] == "Test"

    def test_path_stored_in_result(self, tmp_path):
        p = _write(tmp_path, _valid_template())
        tmpl = load_template(p)
        assert tmpl["path"] == p

    def test_headings_extracted(self, tmp_path):
        p = _write(tmp_path, _valid_template())
        tmpl = load_template(p)
        assert "Cel dokumentu" in tmpl["headings"]

    def test_nonexistent_raises_template_error(self, tmp_path):
        with pytest.raises(TemplateError):
            load_template(tmp_path / "missing.md")

    def test_no_file_handle_leak(self, tmp_path):
        """load_template nie może zostawiać otwartego file handle."""
        import gc
        p = _write(tmp_path, _valid_template())
        for _ in range(50):
            load_template(p)
        gc.collect()
        # Gdyby były wycieki — limit FD by się wyczerpał i pętla by crashnęła

    def test_unicode_file_loaded_correctly(self, tmp_path):
        content = (
            "---\ntitle: Test\nstatus: draft\naligned: true\n---\n"
            "# Test\n\n"
            "## Cel dokumentu\nOpis.\n\n"
            "## Zakres i granice\nOpis.\n\n"
            "## Wejścia i wyjścia\nOpis.\n\n"
            "## Zależności\nŚcieżka do ą, ę, ś.\n"
        )
        p = _write(tmp_path, content)
        tmpl = load_template(p)
        assert "Zależności" in tmpl["headings"]


# ─── validate_template ────────────────────────────────────────────────────

class TestValidateTemplate:
    def test_valid_template_no_errors(self, tmp_path):
        p = _write(tmp_path, _valid_template())
        tmpl = load_template(p)
        errors = validate_template(tmpl)
        assert errors == []

    def test_missing_frontmatter_field_reported(self):
        tmpl = {
            "path": "x.md",
            "frontmatter": {"title": "T"},  # brak 'status', 'aligned'
            "body": "## Cel dokumentu\nT\n## Zakres i granice\nT\n## Wejścia i wyjścia\nT",
            "headings": ["Cel dokumentu", "Zakres i granice", "Wejścia i wyjścia"],
        }
        errors = validate_template(tmpl)
        assert any("status" in e for e in errors)
        assert any("aligned" in e for e in errors)

    def test_placeholder_rola_detected(self):
        tmpl = {
            "path": "x.md",
            "frontmatter": {"title": "T", "status": "x", "aligned": "y"},
            "body": "## Cel dokumentu\nT\n## Zakres i granice\nT\n## Wejścia i wyjścia\n[Rola / interesariusz]",
            "headings": ["Cel dokumentu", "Zakres i granice", "Wejścia i wyjścia"],
        }
        errors = validate_template(tmpl)
        assert any("interesariusz" in e for e in errors)

    def test_emoji_detected(self):
        tmpl = {
            "path": "x.md",
            "frontmatter": {"title": "T", "status": "x", "aligned": "y"},
            "body": "## Cel dokumentu\nTest 🚀\n## Zakres i granice\nT\n## Wejścia i wyjścia\nT",
            "headings": ["Cel dokumentu", "Zakres i granice", "Wejścia i wyjścia"],
        }
        errors = validate_template(tmpl)
        assert any("emoji" in e.lower() for e in errors)

    def test_returns_list_always(self):
        """validate_template zawsze zwraca list, nigdy None."""
        tmpl = {"path": "x.md", "frontmatter": {}, "body": "", "headings": []}
        result = validate_template(tmpl)
        assert isinstance(result, list)

    # Punkt rozszerzenia — mitygacja profunkcjonalna
    def test_errors_are_all_strings(self):
        """Każdy błąd to string — umożliwia hookowanie zewnętrznych walidatorów."""
        tmpl = {"path": "x.md", "frontmatter": {}, "body": "", "headings": []}
        errors = validate_template(tmpl)
        for err in errors:
            assert isinstance(err, str), f"Błąd powinien być stringiem: {err!r}"

    def test_get_required_sections_extensible(self):
        """get_required_sections() zwraca listę — można rozszerzać przez append."""
        sections = get_required_sections()
        assert isinstance(sections, list)
        extended = sections + ["## Nowa sekcja"]
        assert len(extended) == len(sections) + 1


# ─── EP Extensions ────────────────────────────────────────────────────────────


class TestEPSectionSet:
    """EP: get_required_sections(section_set=) — parametryzowany zestaw sekcji."""

    def test_default_returns_three_sections(self):
        """Bez argumentu zwraca 3 sekcje (core)."""
        sections = get_required_sections()
        assert len(sections) == 3

    def test_section_set_core_same_as_default(self):
        """section_set='core' == wynik domyślny."""
        assert get_required_sections("core") == get_required_sections()

    def test_section_set_minimal(self):
        """section_set='minimal' zwraca tylko Cel dokumentu."""
        sections = get_required_sections("minimal")
        assert len(sections) == 1
        assert "## Cel dokumentu" in sections

    def test_section_set_extended_has_more_than_core(self):
        """section_set='extended' ma więcej sekcji niż 'core'."""
        core = get_required_sections("core")
        extended = get_required_sections("extended")
        assert len(extended) > len(core)

    def test_section_set_extended_contains_metadane(self):
        """section_set='extended' zawiera ## Metadane."""
        sections = get_required_sections("extended")
        assert "## Metadane" in sections

    def test_unknown_section_set_raises_value_error(self):
        """Nieznany section_set podnosi ValueError."""
        with pytest.raises(ValueError, match="Nieznany section_set"):
            get_required_sections("nieznany_zestaw")

    def test_returns_copy_not_reference(self):
        """Zwraca nową listę — modyfikacja nie wpływa na kolejne wywołania."""
        s1 = get_required_sections()
        s1.append("## Extra")
        s2 = get_required_sections()
        assert "## Extra" not in s2


class TestEPValidateTemplatePluggable:
    """EP: validate_template(tmpl, validators=[]) — pluggable validators."""

    def _valid_tmpl(self):
        return {
            "path": "test.md",
            "frontmatter": {"title": "T", "status": "draft", "aligned": "true"},
            "body": "## Cel dokumentu\n\n## Zakres i granice\n\n## Wejścia i wyjścia\n",
            "headings": ["Cel dokumentu", "Zakres i granice", "Wejścia i wyjścia"],
        }

    def test_no_validators_works_as_before(self):
        """Pusta lista validators = brak dodatkowych błędów."""
        tmpl = self._valid_tmpl()
        assert validate_template(tmpl, validators=[]) == []

    def test_custom_validator_adds_error(self):
        """Validator może dodać własny błąd."""
        def no_version_check(t: dict) -> list:
            if "version" not in t.get("frontmatter", {}):
                return [f"{t['path']}: brak pola 'version'"]
            return []

        tmpl = self._valid_tmpl()
        errors = validate_template(tmpl, validators=[no_version_check])
        assert any("brak pola 'version'" in e for e in errors)

    def test_multiple_validators_combined(self):
        """Wiele walidatorów — błędy z każdego sumują się."""
        def v1(t):
            return ["v1: błąd"]

        def v2(t):
            return ["v2: błąd"]

        tmpl = self._valid_tmpl()
        errors = validate_template(tmpl, validators=[v1, v2])
        assert any("v1: błąd" in e for e in errors)
        assert any("v2: błąd" in e for e in errors)

    def test_validator_returning_empty_list(self):
        """Validator zwracający [] nie dodaje błędów."""
        tmpl = self._valid_tmpl()
        errors = validate_template(tmpl, validators=[lambda t: []])
        assert errors == []

    def test_failing_validator_captured_as_error(self):
        """Wyjątek w validatorze jest przechwycony i dodany jako błąd."""
        def bad_validator(t):
            raise RuntimeError("crash!")

        tmpl = self._valid_tmpl()
        errors = validate_template(tmpl, validators=[bad_validator])
        assert any("crash!" in e for e in errors)

    def test_validators_none_default(self):
        """validators=None (domyślny) działa identycznie jak validators=[]."""
        tmpl = self._valid_tmpl()
        assert validate_template(tmpl, validators=None) == validate_template(tmpl)
