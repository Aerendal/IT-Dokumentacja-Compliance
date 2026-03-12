"""Tests for scripts/maintenance/enrich_niche_domains.py pure functions."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.maintenance.enrich_niche_domains import PLACEHOLDER, match_archetype, pattern_guidance

pytestmark = pytest.mark.unit


class TestMatchArchetype:
    def test_quantum_key_match(self):
        result = match_archetype("Quantum Key Distribution Protocol")
        assert result is not None
        assert "QKD" in result or "kwantow" in result.lower()

    def test_post_quantum_match(self):
        result = match_archetype("Post-Quantum Cryptography Migration")
        assert result is not None
        assert "PQC" in result or "kwant" in result.lower()

    def test_aircraft_maintenance_match(self):
        result = match_archetype("Aircraft Maintenance Procedures")
        assert result is not None
        assert "EASA" in result or "lotni" in result.lower()

    def test_scada_match(self):
        result = match_archetype("SCADA System Integration Guide")
        assert result is not None
        assert len(result) > 20

    def test_ota_update_match(self):
        result = match_archetype("OTA Update Service Configuration")
        assert result is not None
        assert "OTA" in result or "firmware" in result.lower()

    def test_clinical_trial_match(self):
        result = match_archetype("Clinical Trial Data Management")
        assert result is not None
        assert "GCP" in result or "kliniczn" in result.lower()

    def test_bim_match(self):
        result = match_archetype("BIM Model Coordination Standards")
        assert result is not None
        assert "ISO 19650" in result or "BIM" in result

    def test_no_match_returns_none(self):
        result = match_archetype("Completely Unrelated Title XYZ")
        assert result is None

    def test_case_insensitive(self):
        lower = match_archetype("quantum key distribution")
        upper = match_archetype("QUANTUM KEY DISTRIBUTION")
        assert lower is not None
        assert upper is not None

    def test_vessel_fleet_match(self):
        result = match_archetype("Vessel Fleet Tracking System")
        assert result is not None
        assert "AIS" in result or "flot" in result.lower()

    def test_payroll_match(self):
        result = match_archetype("Payroll Processing Automation")
        assert result is not None
        assert "ZUS" in result or "wynagrodze" in result.lower()

    def test_citizen_portal_match(self):
        result = match_archetype("Citizen Portal Digital Services")
        assert result is not None
        assert "WCAG" in result or "obywatel" in result.lower()


class TestPatternGuidance:
    def test_common_issues_pattern(self):
        result = pattern_guidance("Common Network Issues and Solutions")
        assert "Network" in result
        assert "decision tree" in result or "diagnos" in result.lower()

    def test_access_control_pattern(self):
        result = pattern_guidance("Access Control for Database Systems")
        assert "Database Systems" in result or "database systems" in result.lower()
        assert "RBAC" in result or "uprawnie" in result.lower()

    def test_failure_pattern(self):
        result = pattern_guidance("Database Failure Response Procedure")
        assert "P1" in result or "awari" in result.lower() or "severity" in result.lower()

    def test_tracking_pattern(self):
        result = pattern_guidance("Asset Tracking Dashboard")
        assert "KPI" in result or "śledzeni" in result.lower() or "metryki" in result.lower()

    def test_analytics_pattern(self):
        result = pattern_guidance("Sales Analytics Report")
        assert "KPI" in result or "metryki" in result.lower() or "analityk" in result.lower()

    def test_management_system_pattern(self):
        result = pattern_guidance("Inventory Management System")
        assert "system" in result.lower() or "zarządzan" in result.lower()

    def test_operations_pattern(self):
        result = pattern_guidance("Database Operations Runbook")
        assert "SLA" in result or "operacyjn" in result.lower() or "procedur" in result.lower()

    def test_security_pattern(self):
        result = pattern_guidance("API Security Guidelines")
        assert (
            "ISO 27001" in result or "bezpiecze" in result.lower() or "security" in result.lower()
        )

    def test_policy_pattern(self):
        result = pattern_guidance("Data Retention Policy")
        assert (
            "polityk" in result.lower()
            or "policy" in result.lower()
            or "standard" in result.lower()
        )

    def test_migration_pattern(self):
        result = pattern_guidance("Database Migration Plan")
        assert "rollback" in result or "wdroże" in result.lower() or "migracji" in result.lower()

    def test_development_pattern(self):
        result = pattern_guidance("API Development Implementation Guide")
        assert (
            "architektur" in result.lower()
            or "stack" in result.lower()
            or "wymagania" in result.lower()
        )

    def test_generic_fallback(self):
        result = pattern_guidance("Some Completely Random Document Title")
        assert len(result) > 30
        assert "Some Completely Random Document Title" in result

    def test_returns_string(self):
        assert isinstance(pattern_guidance("Any Title"), str)

    def test_announcement_pattern(self):
        result = pattern_guidance("System Downtime Announcement")
        assert (
            "kanał" in result.lower()
            or "komunikat" in result.lower()
            or "announcement" in result.lower()
        )


class TestPlaceholder:
    def test_placeholder_is_string(self):
        assert isinstance(PLACEHOLDER, str)
        assert len(PLACEHOLDER) > 5
