"""tests/test_template_quality.py — testy jakości szablonów IT Dokumentacja.

Sprawdzają że szablony mają wymagane sekcje, poprawny frontmatter i zero placeholderów.
"""

import re
from pathlib import Path

import pytest

from itdoc.template import load_template, validate_template, get_required_sections
from itdoc.exceptions import TemplateError

_CORE_DIR = Path(__file__).parent.parent / "generated_templates" / "core"


@pytest.fixture(scope="module")
def ten_sample_templates():
    """10 szablonów z core/ — do szybkich sprawdzeń."""
    if not _CORE_DIR.exists():
        pytest.skip(f"Brak katalogu: {_CORE_DIR}")
    templates = sorted(_CORE_DIR.glob("*.md"))[:10]
    if len(templates) < 5:
        pytest.skip("Za mało szablonów w core/")
    return [load_template(p) for p in templates]


@pytest.fixture(scope="module")
def first_template():
    """Pierwszy szablon z core/."""
    if not _CORE_DIR.exists():
        pytest.skip(f"Brak katalogu: {_CORE_DIR}")
    templates = sorted(_CORE_DIR.glob("*.md"))
    if not templates:
        pytest.skip("Brak szablonów w core/")
    return load_template(templates[0])


class TestLoadTemplate:
    def test_load_returns_dict(self, first_template):
        assert isinstance(first_template, dict)

    def test_load_has_required_keys(self, first_template):
        for key in ("path", "frontmatter", "body", "headings"):
            assert key in first_template, f"Brakuje klucza: {key}"

    def test_frontmatter_is_dict(self, first_template):
        assert isinstance(first_template["frontmatter"], dict)

    def test_body_is_string(self, first_template):
        assert isinstance(first_template["body"], str)

    def test_headings_is_list(self, first_template):
        assert isinstance(first_template["headings"], list)

    def test_nonexistent_file_raises(self):
        with pytest.raises(TemplateError):
            load_template(Path("/nonexistent/file.md"))


class TestFrontmatterFields:
    def test_title_present(self, ten_sample_templates):
        for tmpl in ten_sample_templates:
            assert "title" in tmpl["frontmatter"], f"{tmpl['path']}: brak 'title' w frontmatter"

    def test_status_present(self, ten_sample_templates):
        for tmpl in ten_sample_templates:
            assert "status" in tmpl["frontmatter"], f"{tmpl['path']}: brak 'status' w frontmatter"

    def test_aligned_present(self, ten_sample_templates):
        for tmpl in ten_sample_templates:
            assert "aligned" in tmpl["frontmatter"], f"{tmpl['path']}: brak 'aligned' w frontmatter"


class TestRequiredSections:
    def test_get_required_sections_returns_list(self):
        sections = get_required_sections()
        assert isinstance(sections, list)
        assert len(sections) >= 3

    def test_cel_dokumentu_present(self, ten_sample_templates):
        for tmpl in ten_sample_templates:
            headings = [h.lower() for h in tmpl["headings"]]
            assert any("cel dokumentu" in h for h in headings), \
                f"{tmpl['path']}: brak sekcji '## Cel dokumentu'"

    def test_zakres_present(self, ten_sample_templates):
        for tmpl in ten_sample_templates:
            headings = [h.lower() for h in tmpl["headings"]]
            assert any("zakres" in h for h in headings), \
                f"{tmpl['path']}: brak sekcji '## Zakres...'"

    def test_wejscia_wyjscia_present(self, ten_sample_templates):
        for tmpl in ten_sample_templates:
            headings = [h.lower() for h in tmpl["headings"]]
            assert any("wej" in h or "wyj" in h for h in headings), \
                f"{tmpl['path']}: brak sekcji wejścia/wyjścia"


class TestNoForbiddenPlaceholders:
    def test_no_rola_interesariusz_placeholder(self, ten_sample_templates):
        """[Rola / interesariusz] musi być zastąpiony konkretnymi rolami."""
        for tmpl in ten_sample_templates:
            assert "[Rola / interesariusz]" not in tmpl["body"], \
                f"{tmpl['path']}: zawiera niedozwolony placeholder [Rola / interesariusz]"

    def test_no_osoba_rola_placeholder(self, ten_sample_templates):
        """[osoba/rola] musi być zastąpiony konkretną rolą."""
        for tmpl in ten_sample_templates:
            assert "[osoba/rola]" not in tmpl["body"], \
                f"{tmpl['path']}: zawiera niedozwolony placeholder [osoba/rola]"


class TestNoEmoji:
    _EMOJI_RE = re.compile(
        "["
        "\U0001f600-\U0001f64f"
        "\U0001f300-\U0001f5ff"
        "\U0001f680-\U0001f6ff"
        "\U0001fa00-\U0001faff"
        "\U00002702-\U000027b0"
        "]+",
        flags=re.UNICODE,
    )

    def test_no_emoji_in_body(self, ten_sample_templates):
        for tmpl in ten_sample_templates:
            assert not self._EMOJI_RE.search(tmpl["body"]), \
                f"{tmpl['path']}: zawiera emoji (hard gate)"


class TestValidateTemplate:
    def test_validate_passes_for_real_template(self, first_template):
        errors = validate_template(first_template)
        assert errors == [], f"validate_template() zwróciło błędy: {errors}"

    def test_validate_detects_missing_section(self):
        bad_tmpl = {
            "path": "fake.md",
            "frontmatter": {"title": "Test", "status": "draft", "aligned": "true"},
            "body": "# Test\n\n## Jakieś info\nCoś\n",
            "headings": ["Jakieś info"],
        }
        errors = validate_template(bad_tmpl)
        assert any("Cel dokumentu" in e for e in errors), \
            f"Oczekiwano błędu o braku 'Cel dokumentu', got: {errors}"

    def test_validate_detects_placeholder(self):
        bad_tmpl = {
            "path": "fake.md",
            "frontmatter": {"title": "T", "status": "x", "aligned": "true"},
            "body": "## Cel dokumentu\nTest\n## Zakres i granice\nTest\n## Wejścia i wyjścia\n[Rola / interesariusz]",
            "headings": ["Cel dokumentu", "Zakres i granice", "Wejścia i wyjścia"],
        }
        errors = validate_template(bad_tmpl)
        assert any("interesariusz" in e for e in errors), \
            f"Oczekiwano błędu o placeholderze, got: {errors}"
