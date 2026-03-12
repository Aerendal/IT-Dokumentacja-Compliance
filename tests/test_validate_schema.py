"""Unit tests for scripts/validate_template_schema.py"""

import sys
from pathlib import Path

import pytest

# Ensure scripts/ is importable
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from validate_template_schema import (  # noqa: E402
    check_sections,
    parse_frontmatter,
    validate_file,
)

pytestmark = pytest.mark.unit

VALID_FRONTMATTER = "---\ntitle: Test Document\nstatus: draft\n---\n"
REQUIRED_SECTIONS_CONTENT = (
    "## Cel dokumentu\nSome content here.\n\n"
    "## Zakres i granice\nScope content.\n\n"
    "## Wejścia i wyjścia\nInputs and outputs.\n"
)


class TestFrontmatterParsing:
    def test_valid_frontmatter_with_title(self):
        content = "---\ntitle: My Doc\nstatus: draft\n---\n# Body"
        has_fm, has_title = parse_frontmatter(content)
        assert has_fm is True
        assert has_title is True

    def test_missing_frontmatter(self):
        content = "# Just a heading\nNo frontmatter here."
        has_fm, has_title = parse_frontmatter(content)
        assert has_fm is False
        assert has_title is False

    def test_frontmatter_no_title(self):
        content = "---\nstatus: draft\nauthor: someone\n---\n# Body"
        has_fm, has_title = parse_frontmatter(content)
        assert has_fm is True
        assert has_title is False

    def test_frontmatter_with_title_and_extra_fields(self):
        content = (
            "---\n"
            "title: Complex Document\n"
            "status: approved\n"
            "aligned: true\n"
            "aligned_rev: 3\n"
            "---\n"
            "# Content"
        )
        has_fm, has_title = parse_frontmatter(content)
        assert has_fm is True
        assert has_title is True


class TestSectionChecks:
    def test_all_required_sections_present(self):
        content = VALID_FRONTMATTER + REQUIRED_SECTIONS_CONTENT
        violations = check_sections(content)
        assert violations == []

    def test_missing_cel_dokumentu(self):
        content = (
            VALID_FRONTMATTER
            + "## Zakres i granice\nScope.\n\n"
            + "## Wejścia i wyjścia\nIO.\n"
        )
        violations = check_sections(content)
        missing = [v for v in violations if v[0] == "SECTION_MISSING"]
        assert any("Cel dokumentu" in v[1] for v in missing)

    def test_missing_zakres(self):
        content = (
            VALID_FRONTMATTER
            + "## Cel dokumentu\nGoal.\n\n"
            + "## Wejścia i wyjścia\nIO.\n"
        )
        violations = check_sections(content)
        missing = [v for v in violations if v[0] == "SECTION_MISSING"]
        assert any("Zakres i granice" in v[1] for v in missing)

    def test_missing_wejscia_wyjscia(self):
        content = (
            VALID_FRONTMATTER
            + "## Cel dokumentu\nGoal.\n\n"
            + "## Zakres i granice\nScope.\n"
        )
        violations = check_sections(content)
        missing = [v for v in violations if v[0] == "SECTION_MISSING"]
        assert any("Wejścia i wyjścia" in v[1] for v in missing)

    def test_empty_section_detection(self):
        content = (
            VALID_FRONTMATTER
            + "## Cel dokumentu\n   \n\n"
            + "## Zakres i granice\nScope.\n\n"
            + "## Wejścia i wyjścia\nIO.\n"
        )
        violations = check_sections(content)
        empty = [v for v in violations if v[0] == "EMPTY_SECTION"]
        assert any("Cel dokumentu" in v[1] for v in empty)


class TestValidateFile:
    def test_valid_file_returns_empty_violations(self, tmp_path):
        md = tmp_path / "valid.md"
        md.write_text(
            VALID_FRONTMATTER
            + REQUIRED_SECTIONS_CONTENT,
            encoding="utf-8",
        )
        violations = validate_file(md)
        assert violations == []

    def test_multiple_violations_single_file(self, tmp_path):
        md = tmp_path / "broken.md"
        # No frontmatter, missing all required sections
        md.write_text("# Just a title\nSome random content.\n", encoding="utf-8")
        violations = validate_file(md)
        vtypes = {v["violation_type"] for v in violations}
        assert "FRONTMATTER_MISSING" in vtypes
        assert "SECTION_MISSING" in vtypes

    def test_section_detection_case_sensitive(self, tmp_path):
        md = tmp_path / "case.md"
        # Lowercase heading should NOT satisfy the requirement
        md.write_text(
            VALID_FRONTMATTER
            + "## cel dokumentu\nContent.\n\n"
            + "## zakres i granice\nScope.\n\n"
            + "## wejścia i wyjścia\nIO.\n",
            encoding="utf-8",
        )
        violations = validate_file(md)
        missing = [v for v in violations if v["violation_type"] == "SECTION_MISSING"]
        # All three required sections (with proper casing) should be reported missing
        assert len(missing) == 3
