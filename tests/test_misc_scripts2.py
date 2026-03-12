"""
tests/test_misc_scripts2.py — additional unit tests for utility functions
in scripts with 0% coverage.

Covers:
  - scripts/audit_content_labels_meta.py
  - scripts/extract_sections.py
  - scripts/extract_section_metrics.py
"""
import pytest

pytestmark = pytest.mark.unit


# ---------------------------------------------------------------------------
# scripts/audit_content_labels_meta.py
# ---------------------------------------------------------------------------

class TestAuditContentLabelsMeta:
    def test_strip_diacritics_removes_polish(self):
        from scripts.audit_content_labels_meta import strip_diacritics
        result = strip_diacritics("zażółć gęślą jaźń")
        assert "ą" not in result
        assert "ę" not in result

    def test_strip_diacritics_plain_ascii_unchanged(self):
        from scripts.audit_content_labels_meta import strip_diacritics
        result = strip_diacritics("Hello World")
        assert result == "Hello World"

    def test_key_norm_lowercases(self):
        from scripts.audit_content_labels_meta import key_norm
        result = key_norm("Security Policy")
        assert result == "security policy"

    def test_key_norm_strips_whitespace(self):
        from scripts.audit_content_labels_meta import key_norm
        result = key_norm("  hello   world  ")
        assert result == "hello world"

    def test_key_norm_removes_emoji(self):
        from scripts.audit_content_labels_meta import key_norm
        result = key_norm("😀 Hello World")
        assert "😀" not in result
        assert "hello world" in result

    def test_key_norm_strips_meta_prefix(self):
        from scripts.audit_content_labels_meta import key_norm
        result = key_norm("meta: Security Policy")
        assert "meta" not in result.split()[0] if result else True

    def test_key_norm_strips_numeric_prefix(self):
        from scripts.audit_content_labels_meta import key_norm
        result = key_norm("1. Security policy")
        assert result == "security policy"

    def test_key_norm_removes_diacritics(self):
        from scripts.audit_content_labels_meta import key_norm
        result = key_norm("Zarządzanie bezpieczeństwem")
        assert "ą" not in result
        assert "ę" not in result


# ---------------------------------------------------------------------------
# scripts/extract_sections.py
# ---------------------------------------------------------------------------

class TestExtractSections:
    def test_utc_now_iso_format(self):
        from scripts.extract_sections import utc_now_iso
        result = utc_now_iso()
        assert "T" in result
        assert "Z" in result
        assert len(result) == 20

    def test_heading_norm_lowercase(self):
        from scripts.extract_sections import heading_norm
        result = heading_norm("Security Policy")
        assert result == "security policy"

    def test_heading_norm_strips_emoji(self):
        from scripts.extract_sections import heading_norm
        result = heading_norm("😀 Security Policy")
        assert "😀" not in result

    def test_heading_norm_strips_numeric_prefix(self):
        from scripts.extract_sections import heading_norm
        result = heading_norm("1. Security Policy")
        assert result == "security policy"

    def test_heading_norm_normalizes_spaces(self):
        from scripts.extract_sections import heading_norm
        result = heading_norm("  security   policy  ")
        assert result == "security policy"

    def test_slugify_basic(self):
        from scripts.extract_sections import slugify
        result = slugify("Security Policy")
        assert result == "security-policy"

    def test_slugify_removes_special_chars(self):
        from scripts.extract_sections import slugify
        result = slugify("Hello! World?")
        assert "!" not in result
        assert "?" not in result

    def test_slugify_empty_returns_section(self):
        from scripts.extract_sections import slugify
        result = slugify("")
        assert result == "section"

    def test_detect_placeholder_empty(self):
        from scripts.extract_sections import detect_placeholder
        assert detect_placeholder("") == "placeholder"
        assert detect_placeholder("   ") == "placeholder"

    def test_detect_placeholder_todo(self):
        from scripts.extract_sections import detect_placeholder
        assert detect_placeholder("TODO: fill this in") == "placeholder"
        assert detect_placeholder("TBD") == "placeholder"

    def test_detect_placeholder_real_content(self):
        from scripts.extract_sections import detect_placeholder
        result = detect_placeholder("This is a real security policy document.")
        assert result == "filled"

    def test_detect_placeholder_ellipsis(self):
        from scripts.extract_sections import detect_placeholder
        assert detect_placeholder("Content...") == "placeholder"

    def test_extract_phase_bullets_finds_phases(self):
        from scripts.extract_sections import extract_phase_bullets
        lines = [
            "## Fazy cyklu życia",
            "- Faza 1: Koncepcja",
            "- Faza 2: Realizacja",
            "- Not a phase",
        ]
        result = extract_phase_bullets(lines, 1, 4)
        assert len(result) == 2
        assert result[0]["phase_n"] == 1
        assert result[1]["phase_n"] == 2

    def test_extract_phase_bullets_empty(self):
        from scripts.extract_sections import extract_phase_bullets
        lines = ["no phases here", "just content"]
        result = extract_phase_bullets(lines, 1, 2)
        assert result == []

    def test_extract_phase_bullets_line_numbers(self):
        from scripts.extract_sections import extract_phase_bullets
        lines = ["intro", "- Faza 3: Testowanie", "outro"]
        result = extract_phase_bullets(lines, 1, 3)
        assert result[0]["line_no"] == 2


# ---------------------------------------------------------------------------
# scripts/extract_section_metrics.py
# ---------------------------------------------------------------------------

class TestExtractSectionMetrics:
    def test_utc_now_iso_format(self):
        from scripts.extract_section_metrics import utc_now_iso
        result = utc_now_iso()
        assert "T" in result
        assert "Z" in result

    def test_profile_for_origin_core(self):
        from scripts.extract_section_metrics import profile_for_origin
        assert profile_for_origin("core") == "core"

    def test_profile_for_origin_imported(self):
        from scripts.extract_section_metrics import profile_for_origin
        assert profile_for_origin("imported_template") == "imported_template"

    def test_profile_for_origin_default(self):
        from scripts.extract_section_metrics import profile_for_origin
        result = profile_for_origin("unknown_origin")
        assert result == "default"

    def _base_profile(self):
        return {
            "max_placeholder_ratio": 0.3,
            "min_sections": 5,
            "min_checkboxes": 0,
            "require_phases": 0,
            "min_phase_bullets": 0,
        }

    def test_score_and_status_ok(self):
        from scripts.extract_section_metrics import score_and_status
        profile = self._base_profile()
        score, status = score_and_status(profile, 10, 1, 0, 5, 0, 0, 0)
        assert status == "ok"
        assert score == 100

    def test_score_and_status_needs_structure_low_sections(self):
        from scripts.extract_section_metrics import score_and_status
        profile = self._base_profile()
        score, status = score_and_status(profile, 2, 0, 0, 0, 0, 0, 0)
        assert status == "needs_structure"
        assert score < 100

    def test_score_and_status_needs_content_high_placeholder_ratio(self):
        from scripts.extract_section_metrics import score_and_status
        profile = self._base_profile()
        # High placeholder ratio: 5/8 = 0.625 > 0.3
        score, status = score_and_status(profile, 8, 5, 0, 5, 0, 0, 0)
        assert status in ("needs_content", "needs_structure")
        assert score < 100

    def test_score_and_status_deducts_for_missing_required(self):
        from scripts.extract_section_metrics import score_and_status
        profile = self._base_profile()
        score_with, _ = score_and_status(profile, 10, 1, 1, 5, 0, 0, 0)
        score_without, _ = score_and_status(profile, 10, 1, 0, 5, 0, 0, 0)
        assert score_with < score_without

    def test_score_and_status_score_never_negative(self):
        from scripts.extract_section_metrics import score_and_status
        profile = self._base_profile()
        score, _ = score_and_status(profile, 0, 0, 10, 0, 0, 5, 5)
        assert score >= 0

    def test_score_and_status_needs_links(self):
        from scripts.extract_section_metrics import score_and_status
        profile = self._base_profile()
        score, status = score_and_status(profile, 10, 0, 0, 5, 0, 2, 0)
        assert status == "needs_links"
        assert score < 100

    def test_score_and_status_unresolved_links_deducted(self):
        from scripts.extract_section_metrics import score_and_status
        profile = self._base_profile()
        score_clean, _ = score_and_status(profile, 10, 0, 0, 5, 0, 0, 0)
        score_dirty, _ = score_and_status(profile, 10, 0, 0, 5, 0, 0, 3)
        assert score_dirty < score_clean


# ---------------------------------------------------------------------------
# scripts/enrich_guidance_standards.py — normalize utility
# ---------------------------------------------------------------------------

class TestEnrichGuidanceStandardsNormalize:
    def test_lowercases_string(self):
        from scripts.enrich_guidance_standards import normalize
        assert normalize("UPPER CASE") == "upper case"

    def test_strips_whitespace(self):
        from scripts.enrich_guidance_standards import normalize
        assert normalize("  trimmed  ") == "trimmed"

    def test_replaces_polish_diacritics(self):
        from scripts.enrich_guidance_standards import normalize
        result = normalize("Faza 7: Bezpieczeństwo")
        assert "ń" not in result
        assert "n" in result

    def test_replaces_all_pl_chars(self):
        from scripts.enrich_guidance_standards import normalize
        result = normalize("ą ć ę ł ń ó ś ź ż")
        assert result == "a c e l n o s z z"

    def test_empty_string(self):
        from scripts.enrich_guidance_standards import normalize
        assert normalize("") == ""

    def test_section_key_normalized(self):
        from scripts.enrich_guidance_standards import normalize, SECTION_STANDARDS
        # All dict keys in SECTION_STANDARDS should be normalized already
        for key in SECTION_STANDARDS:
            assert key == normalize(key), f"Key not normalized: {key!r}"
