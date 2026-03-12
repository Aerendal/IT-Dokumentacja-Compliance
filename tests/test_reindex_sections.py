"""Tests for pure functions in scripts/reindex_sections.py."""
import pytest
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.reindex_sections import to_anchor, make_section_uid

pytestmark = pytest.mark.unit


class TestToAnchor:
    def test_basic_lowercase(self):
        result = to_anchor("Introduction")
        assert result == "introduction"

    def test_polish_phase_format(self):
        result = to_anchor("Faza 1: Koncepcja")
        assert result == "phase-01"

    def test_polish_phase_two_digits(self):
        result = to_anchor("Faza 10: Operacje")
        assert result == "phase-10"

    def test_spaces_become_dashes(self):
        result = to_anchor("Security Policy Overview")
        assert "-" in result
        assert " " not in result

    def test_non_ascii_stripped(self):
        result = to_anchor("Bezpieczeństwo systemu")
        assert "ń" not in result
        assert "bezpiecze" in result

    def test_special_chars_removed(self):
        result = to_anchor("Section: 1.2 Overview!")
        assert ":" not in result
        assert "!" not in result
        assert "." not in result

    def test_no_leading_trailing_dashes(self):
        result = to_anchor("  Test Section  ")
        assert not result.startswith("-")
        assert not result.endswith("-")

    def test_empty_returns_empty(self):
        assert to_anchor("") == ""

    def test_multiple_dashes_collapsed(self):
        result = to_anchor("Hello   World")
        assert "--" not in result


class TestMakeSectionUid:
    def test_returns_string(self):
        result = make_section_uid("UID001", "Introduction", 1)
        assert isinstance(result, str)

    def test_deterministic(self):
        uid1 = make_section_uid("DOC001", "Introduction", 1)
        uid2 = make_section_uid("DOC001", "Introduction", 1)
        assert uid1 == uid2

    def test_length_is_26(self):
        result = make_section_uid("DOC001", "Introduction", 1)
        assert len(result) == 26

    def test_uppercase(self):
        result = make_section_uid("doc001", "intro", 1)
        assert result == result.upper()

    def test_different_ordinals_differ(self):
        uid1 = make_section_uid("DOC001", "Introduction", 1)
        uid2 = make_section_uid("DOC001", "Introduction", 2)
        assert uid1 != uid2

    def test_different_docs_differ(self):
        uid1 = make_section_uid("DOC001", "Introduction", 1)
        uid2 = make_section_uid("DOC002", "Introduction", 1)
        assert uid1 != uid2

    def test_different_headings_differ(self):
        uid1 = make_section_uid("DOC001", "Introduction", 1)
        uid2 = make_section_uid("DOC001", "Conclusion", 1)
        assert uid1 != uid2

    def test_matches_manual_sha256(self):
        raw = "DOC001|Introduction|1"
        expected = hashlib.sha256(raw.encode()).hexdigest()[:26].upper()
        assert make_section_uid("DOC001", "Introduction", 1) == expected
