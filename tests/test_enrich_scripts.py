"""
tests/test_enrich_scripts.py — unit tests for scripts/maintenance/enrich_niche_domains.py
and scripts/maintenance/enrich_placeholders.py.
All tests use in-memory or tmp_path fixtures only.
"""
import pytest
from pathlib import Path

from scripts.maintenance.enrich_niche_domains import (
    match_archetype,
    pattern_guidance,
    enrich_file,
    PLACEHOLDER,
)
from scripts.maintenance.enrich_placeholders import find_archetype

pytestmark = pytest.mark.unit

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_MD_TEMPLATE = """\
---
title: {title}
status: needs_content
---
# {title}

## Cel dokumentu
{title} — szablon dokumentu IT.

Opisuje cel, zakres i zastosowanie tego dokumentu w kontekście procesu lub systemu IT. Zawiera: definicję problemu lub potrzeby biznesowej adresowanej przez ten dokument, kluczowe decyzje które wspiera, ryzyka które ogranicza i wartość dostarczaną interesariuszom.

## Zakres i granice
- Obejmuje: kontekst biznesowy
"""


def _make_md(tmp_path: Path, title: str = "Test Document") -> Path:
    fpath = tmp_path / "test_doc.md"
    fpath.write_text(_MD_TEMPLATE.format(title=title), encoding="utf-8")
    return fpath


# ---------------------------------------------------------------------------
# Class A: TestMatchArchetype
# ---------------------------------------------------------------------------


class TestMatchArchetype:
    def test_quantum_kd(self):
        result = match_archetype("Quantum Key Distribution")
        assert result is not None
        assert "QKD" in result or "BB84" in result

    def test_aviation_aircraft(self):
        result = match_archetype("Aircraft Maintenance Operations")
        assert result is not None
        assert "EASA" in result or "MRO" in result

    def test_maritime_cargo(self):
        result = match_archetype("Cargo Handling Operations")
        assert result is not None
        assert "EDI" in result or "cargo" in result.lower()

    def test_iot_ota(self):
        result = match_archetype("OTA Update Service")
        assert result is not None
        assert "firmware" in result or "secure boot" in result or "OTA" in result

    def test_iot_alarm(self):
        result = match_archetype("Alarm Management")
        assert result is not None
        assert "ISA" in result or "SCADA" in result or "alarmów" in result

    def test_healthcare_clinical(self):
        result = match_archetype("Clinical Trial Operations")
        assert result is not None
        assert "ICH" in result or "eCRF" in result or "GCP" in result

    def test_legal(self):
        result = match_archetype("Attorney Client Privilege Protection")
        assert result is not None
        assert "privilege" in result.lower() or "attorney" in result.lower()

    def test_hr_ats(self):
        result = match_archetype("ATS Development")
        assert result is not None
        assert "rekrutac" in result or "TTF" in result or "ATS" in result

    def test_esg_carbon(self):
        result = match_archetype("Carbon Offset Tracking")
        assert result is not None
        assert "GHG" in result or "net-zero" in result or "CO2" in result

    def test_autonomous(self):
        result = match_archetype("Autonomous Vehicle Safety Standards")
        assert result is not None
        assert "SAE" in result or "SOTIF" in result or "autonomi" in result.lower()

    def test_adtech_attribution(self):
        result = match_archetype("Attribution Engine")
        assert result is not None
        assert "Last-Click" in result or "ROAS" in result or "atrybucj" in result.lower()

    def test_blockchain(self):
        result = match_archetype("Blockchain Use Case Document")
        assert result is not None
        # The archetype groups blockchain use cases with AI/ML use case guidance
        assert "AI" in result or "Canvas" in result or "pilotażu" in result

    def test_no_match(self):
        result = match_archetype("Zupelnie Nieznany Tytul Xyz123")
        assert result is None


# ---------------------------------------------------------------------------
# Class B: TestPatternGuidance
# ---------------------------------------------------------------------------


class TestPatternGuidance:
    def test_common_issues(self):
        result = pattern_guidance("Common Network Issues and Solutions")
        assert "Network" in result

    def test_access_control(self):
        result = pattern_guidance("Access Control for ITSM Tools")
        assert "itsm" in result.lower()

    def test_failure_response(self):
        result = pattern_guidance("Billing System Failure")
        assert "awari" in result.lower() or "severity" in result.lower() or "P1" in result

    def test_tracking_pattern(self):
        result = pattern_guidance("Budget Tracking")
        assert "metryki" in result or "KPI" in result or "śledzeni" in result

    def test_analytics_pattern(self):
        result = pattern_guidance("Sales Analytics")
        assert "analityk" in result.lower() or "KPI" in result or "BI" in result

    def test_operations_pattern(self):
        result = pattern_guidance("Warehouse Operations")
        assert "operacyjne" in result or "SLA" in result

    def test_development_no_double_spaces(self):
        result = pattern_guidance("Bot Development Standards")
        assert "  " not in result

    def test_generic_fallback(self):
        result = pattern_guidance("Zupelnie Nowy Dokument")
        assert result
        assert isinstance(result, str)
        assert len(result) > 0


# ---------------------------------------------------------------------------
# Class C: TestEnrichFile
# ---------------------------------------------------------------------------


class TestEnrichFile:
    def test_dry_run_returns_true(self, tmp_path):
        fpath = _make_md(tmp_path)
        original = fpath.read_text(encoding="utf-8")

        result = enrich_file(fpath, dry_run=True)

        assert result is True
        assert fpath.read_text(encoding="utf-8") == original

    def test_apply_removes_placeholder(self, tmp_path):
        fpath = _make_md(tmp_path)

        result = enrich_file(fpath, dry_run=False)

        assert result is True
        assert PLACEHOLDER not in fpath.read_text(encoding="utf-8")

    def test_apply_adds_guidance(self, tmp_path):
        fpath = _make_md(tmp_path)
        original_len = len(fpath.read_text(encoding="utf-8"))

        enrich_file(fpath, dry_run=False)

        assert len(fpath.read_text(encoding="utf-8")) >= original_len

    def test_no_placeholder_returns_false(self, tmp_path):
        fpath = tmp_path / "no_placeholder.md"
        fpath.write_text(
            "---\ntitle: Clean Doc\nstatus: done\n---\n# Clean Doc\n\nNo placeholder here.\n",
            encoding="utf-8",
        )

        result = enrich_file(fpath, dry_run=False)

        assert result is False

    def test_preserves_frontmatter(self, tmp_path):
        fpath = _make_md(tmp_path)

        enrich_file(fpath, dry_run=False)

        assert fpath.read_text(encoding="utf-8").startswith("---")


# ---------------------------------------------------------------------------
# Class D: TestFindArchetype
# ---------------------------------------------------------------------------


class TestFindArchetype:
    def test_incident_response(self):
        result = find_archetype("Incident Response Plan", "some content")
        assert result is not None
        cel = result[0]
        assert cel and ("incydent" in cel.lower() or "P1" in cel or "reagowania" in cel.lower())

    def test_disaster_recovery(self):
        result = find_archetype("Disaster Recovery Plan", "some content")
        assert result is not None
        cel = result[0]
        assert cel and ("RTO" in cel or "RPO" in cel or "odtworzeni" in cel.lower())

    def test_architecture_decision_record(self):
        result = find_archetype("Architecture Decision Record", "some content")
        assert result is not None
        cel = result[0]
        assert cel and ("ADR" in cel or "architektoniczn" in cel.lower() or "decyzj" in cel.lower())

    def test_unknown_title(self):
        result = find_archetype("Xyz Unknown Random Document 9999", "some content")
        # find_archetype always returns the generic fallback tuple, never None
        assert result is not None
        assert len(result) > 0
        assert result[0] and isinstance(result[0], str)
