"""tests/test_user_scenarios.py — testy 32 scenariuszy użycia biblioteki IT_Dokumentacja.

Grupy:
  A — Onboarding nowego pracownika IT        (A1–A4)
  B — Przygotowanie do audytu               (B1–B4)
  C — Start projektu IT                     (C1–C4)
  D — Zarządzanie incydentem bezpieczeństwa (D1–D4)
  E — Wdrożenie systemu AI                  (E1–E4)
  F — Zarządzanie ciągłością działania      (F1–F4)
  G — Rozwój aplikacji (SecDevOps)          (G1–G4)
  H — Cloud i infrastruktura                (H1–H4)

Wszystkie testy używają real_db_conn (pomijane gdy brak DB).
"""

import pytest

from itdoc.query import find_by_standard

pytestmark = pytest.mark.usefixtures()


def _paths(results):
    """Zwraca zbiór basename'ów z wyników find_by_standard."""
    return {r["doc_path"].rsplit("/", 1)[-1] for r in results}


def _high_exact(results):
    """Filtruje wyniki do gap_analysis (explicit_audit + primary_standard), pomijając keyword_match."""
    return [r for r in results if r.get("match_reason") not in ("keyword_match",)]


# ===========================================================================
# Grupa A — Onboarding
# ===========================================================================


class TestGroupAOnboarding:
    """Scenariusze A1–A4: nowy pracownik szuka szablonów na start."""

    def test_a1_iso27001_starter_templates(self, real_db_conn):
        """A1: ISO 27001 — minimum 10 szablonów dla nowego pracownika security."""
        results = find_by_standard(real_db_conn, "ISO/IEC 27001")
        assert len(results) >= 10, f"Zbyt mało szablonów ISO 27001: {len(results)}"
        paths = _paths(results)
        for required in ("isms_scope_statement.md", "audit_report.md", "risk_assessment.md"):
            assert required in paths, f"Brak wymaganego szablonu: {required}"

    def test_a2_devops_owasp_sdlc(self, real_db_conn):
        """A2: DevOps — szablony OWASP ASVS do bezpiecznego SDLC."""
        results = find_by_standard(real_db_conn, "OWASP ASVS")
        assert len(results) >= 5, f"Zbyt mało szablonów OWASP ASVS: {len(results)}"
        paths = _paths(results)
        assert (
            "api_security_design.md" in paths or "security_requirements_specification.md" in paths
        ), "Brak szablonu API security / security requirements"

    def test_a3_pm_prince2_pmbok_starter(self, real_db_conn):
        """A3: PM — szablony startowe PRINCE2 i PMBOK."""
        prince2 = find_by_standard(real_db_conn, "PRINCE2 7")
        pmbok = find_by_standard(real_db_conn, "PMBOK 7")
        assert len(prince2) >= 12, f"Za mało szablonów PRINCE2: {len(prince2)}"
        assert len(pmbok) >= 10, f"Za mało szablonów PMBOK: {len(pmbok)}"
        prince2_paths = _paths(prince2)
        assert "project_business_case.md" in prince2_paths, "Brak project_business_case.md"

    def test_a4_security_engineer_owasp_asvs_high_confidence(self, real_db_conn):
        """A4: Security Engineer — szablony OWASP ASVS z wysoką pewnością dopasowania."""
        results = find_by_standard(real_db_conn, "OWASP ASVS")
        high_conf = _high_exact(results)
        assert len(high_conf) >= 5, f"Za mało wysokiej jakości szablonów ASVS: {len(high_conf)}"
        paths = _paths(high_conf)
        assert (
            "owasp_asvs_cryptography_policy.md" in paths
        ), "Brak owasp_asvs_cryptography_policy.md w wynikach wysokiej pewności"


# ===========================================================================
# Grupa B — Audyt
# ===========================================================================


class TestGroupBAudit:
    """Scenariusze B1–B4: CISO / compliance officer przygotowuje dowody na audyt."""

    def test_b1_iso27001_full_audit_package(self, real_db_conn):
        """B1: ISO 27001 — komplet dokumentów na audyt (scope, SoA, risk, audit report)."""
        results = find_by_standard(real_db_conn, "ISO/IEC 27001")
        paths = _paths(results)
        required = [
            "isms_scope_statement.md",
            "statement_of_applicability.md",
            "audit_report.md",
            "risk_assessment.md",
        ]
        missing = [r for r in required if r not in paths]
        assert not missing, f"Brakujące dokumenty ISO 27001: {missing}"

    def test_b2_soc2_trust_service_criteria(self, real_db_conn):
        """B2: SOC 2 — szablony dla każdego Trust Service Criteria."""
        results = find_by_standard(real_db_conn, "SOC 2")
        paths = _paths(results)
        assert len(results) >= 5, f"Za mało szablonów SOC 2: {len(results)}"
        required = [
            "soc2_system_description.md",
            "soc2_availability_policy.md",
            "soc2_confidentiality_policy.md",
        ]
        missing = [r for r in required if r not in paths]
        assert not missing, f"Brakujące szablony SOC 2 TSC: {missing}"

    def test_b3_nis2_regulatory_package(self, real_db_conn):
        """B3: NIS2 — dokumentacja dla organu nadzorczego."""
        results = find_by_standard(real_db_conn, "NIS2")
        assert len(results) >= 4, f"Za mało szablonów NIS2: {len(results)}"
        paths = _paths(results)
        assert (
            "incident_transparency_report.md" in paths
        ), "Brak szablonu raportowania incydentów NIS2"
        assert "risk_assessment.md" in paths, "Brak szablonu oceny ryzyka NIS2"

    def test_b4_dora_eba_artifacts(self, real_db_conn):
        """B4: DORA — artefakty dla regulatora finansowego (EBA)."""
        results = find_by_standard(real_db_conn, "DORA")
        assert len(results) >= 7, f"Za mało szablonów DORA: {len(results)}"
        paths = _paths(results)
        required = [
            "ict_third_party_provider_register.md",
            "incident_classification.md",
            "ict_contractual_arrangements.md",
        ]
        missing = [r for r in required if r not in paths]
        assert not missing, f"Brakujące kluczowe szablony DORA: {missing}"


# ===========================================================================
# Grupa C — Start projektu
# ===========================================================================


class TestGroupCProjectStart:
    """Scenariusze C1–C4: PM / Scrum Master inicjuje nowy projekt."""

    def test_c1_prince2_initiation_stage(self, real_db_conn):
        """C1: PRINCE2 — dokumenty na etap Initiation."""
        results = find_by_standard(real_db_conn, "PRINCE2 7")
        assert len(results) >= 12, f"Za mało szablonów PRINCE2: {len(results)}"
        paths = _paths(results)
        assert "project_business_case.md" in paths, "Brak Project Business Case"
        assert "prince2_stage_plan.md" in paths, "Brak Stage Plan"

    def test_c2_scrum_sprint_start(self, real_db_conn):
        """C2: Scrum — szablony do startu sprintu."""
        results = find_by_standard(real_db_conn, "SCRUM Guide")
        assert len(results) >= 6, f"Za mało szablonów Scrum: {len(results)}"

    def test_c3_safe_pi_planning(self, real_db_conn):
        """C3: SAFe — szablony do PI Planning."""
        results = find_by_standard(real_db_conn, "SAFe 6.0")
        assert len(results) >= 6, f"Za mało szablonów SAFe: {len(results)}"
        paths = _paths(results)
        assert "safe_pi_planning_inputs.md" in paths, "Brak PI Planning Inputs"
        assert "safe_team_iteration_plan.md" in paths, "Brak Team Iteration Plan"

    def test_c4_pmbok_scope_wbs(self, real_db_conn):
        """C4: PMBOK — szablony do zarządzania zakresem."""
        results = find_by_standard(real_db_conn, "PMBOK 7")
        assert len(results) >= 10, f"Za mało szablonów PMBOK: {len(results)}"
        paths = _paths(results)
        assert "scope_baseline.md" in paths, "Brak Scope Baseline (WBS)"


# ===========================================================================
# Grupa D — Incydent bezpieczeństwa
# ===========================================================================


class TestGroupDIncident:
    """Scenariusze D1–D4: Incident Manager reaguje na zdarzenie."""

    def test_d1_data_breach_rodo_iso27035(self, real_db_conn):
        """D1: Naruszenie danych — szablony RODO i ISO 27035."""
        rodo = find_by_standard(real_db_conn, "GDPR / RODO")
        iso27035 = find_by_standard(real_db_conn, "ISO/IEC 27035")
        assert len(rodo) >= 6, f"Za mało szablonów RODO: {len(rodo)}"
        assert len(iso27035) >= 4, f"Za mało szablonów ISO 27035: {len(iso27035)}"
        rodo_paths = _paths(rodo)
        required = ["data_breach_response.md", "data_privacy_impact_assessment.md"]
        missing = [r for r in required if r not in rodo_paths]
        assert not missing, f"Brakujące szablony naruszenia danych: {missing}"

    def test_d2_dora_major_ict_incident(self, real_db_conn):
        """D2: DORA — raportowanie Major ICT Incident do regulatora."""
        results = find_by_standard(real_db_conn, "DORA")
        assert len(results) >= 7, f"Za mało szablonów DORA: {len(results)}"
        paths = _paths(results)
        assert "incident_classification.md" in paths, "Brak klasyfikacji incydentu DORA"
        assert "incident_transparency_report.md" in paths, "Brak raportu przejrzystości DORA"

    def test_d3_itil4_problem_management(self, real_db_conn):
        """D3: ITIL 4 — zarządzanie problemem w produkcji."""
        results = find_by_standard(real_db_conn, "ITIL 4")
        assert len(results) >= 10, f"Za mało szablonów ITIL 4: {len(results)}"
        paths = _paths(results)
        assert "itil4_incident_record.md" in paths, "Brak Incident Record ITIL 4"
        assert "itil4_problem_record.md" in paths, "Brak Problem Record ITIL 4"

    def test_d4_lessons_learned_post_incident(self, real_db_conn):
        """D4: Lessons Learned po incydencie (ISO 27035 + PRINCE2)."""
        iso27035 = find_by_standard(real_db_conn, "ISO/IEC 27035")
        prince2 = find_by_standard(real_db_conn, "PRINCE2 7")
        assert len(iso27035) >= 4, f"Za mało szablonów ISO 27035: {len(iso27035)}"
        assert len(prince2) >= 10, f"Za mało szablonów PRINCE2: {len(prince2)}"
        prince2_paths = _paths(prince2)
        assert "lessons_learned_log.md" in prince2_paths, "Brak Lessons Learned Log"


# ===========================================================================
# Grupa E — AI
# ===========================================================================


class TestGroupEAI:
    """Scenariusze E1–E4: AI Lead wdraża system AI zgodnie z ISO/IEC 42001."""

    def test_e1_iso42001_ai_system_docs(self, real_db_conn):
        """E1: ISO 42001 — komplet dokumentów dla nowego systemu AI."""
        results = find_by_standard(real_db_conn, "ISO/IEC 42001")
        assert len(results) >= 5, f"Za mało szablonów ISO 42001: {len(results)}"
        paths = _paths(results)
        required = [
            "ai_governance_framework.md",
            "iso42001_ai_policy.md",
            "ai_ethics_assessment.md",
        ]
        missing = [r for r in required if r not in paths]
        assert not missing, f"Brakujące szablony AI: {missing}"

    def test_e2_ai_risk_assessment(self, real_db_conn):
        """E2: AI Risk Assessment przed wdrożeniem produkcyjnym."""
        results = find_by_standard(real_db_conn, "ISO/IEC 42001")
        paths = _paths(results)
        assert "ai_ethics_assessment.md" in paths, "Brak AI Ethics Assessment"
        # ai_governance_framework zawiera risk assessment dla AI
        assert "ai_governance_framework.md" in paths, "Brak AI Governance Framework z ryzykiem AI"

    def test_e3_ai_incident_log(self, real_db_conn):
        """E3: Rejestracja incydentu AI."""
        results = find_by_standard(real_db_conn, "ISO/IEC 42001")
        paths = _paths(results)
        assert "experiments_log.md" in paths, "Brak rejestru eksperymentów/incydentów AI"

    def test_e4_ai_policy_template(self, real_db_conn):
        """E4: AI Policy dla organizacji."""
        results = find_by_standard(real_db_conn, "ISO/IEC 42001")
        paths = _paths(results)
        assert "iso42001_ai_policy.md" in paths, "Brak szablonu AI Policy ISO 42001"


# ===========================================================================
# Grupa F — Ciągłość działania
# ===========================================================================


class TestGroupFBCM:
    """Scenariusze F1–F4: BCM Manager tworzy i testuje BCMS."""

    def test_f1_iso22301_bcms_documents(self, real_db_conn):
        """F1: ISO 22301 — lista obowiązkowych dokumentów BCMS."""
        results = find_by_standard(real_db_conn, "ISO 22301")
        assert len(results) >= 6, f"Za mało szablonów ISO 22301: {len(results)}"
        paths = _paths(results)
        required = [
            "bcms_policy.md",
            "business_continuity_plan_bcp.md",
            "business_impact_analysis.md",
        ]
        missing = [r for r in required if r not in paths]
        assert not missing, f"Brakujące podstawowe dokumenty BCMS: {missing}"

    def test_f2_bia_risk_assessment(self, real_db_conn):
        """F2: BIA i Risk Assessment — oba szablony dostępne."""
        results = find_by_standard(real_db_conn, "ISO 22301")
        paths = _paths(results)
        assert "business_impact_analysis.md" in paths, "Brak BIA (klauzula 8.2.2 ISO 22301)"
        assert "risk_assessment.md" in paths, "Brak Risk Assessment (klauzula 8.2.3 ISO 22301)"

    def test_f3_drp_exercise_report(self, real_db_conn):
        """F3: Test DRP — szablon raportu z ćwiczenia."""
        results = find_by_standard(real_db_conn, "ISO 22301")
        paths = _paths(results)
        # compliance_testing_report lub inny szablon testowania BCP
        test_templates = [
            p for p in paths if "test" in p or "exercise" in p or "compliance_test" in p
        ]
        assert (
            len(test_templates) >= 1
        ), f"Brak szablonu testowania/ćwiczenia DRP w ISO 22301. Dostępne: {sorted(paths)[:10]}"

    def test_f4_major_incident_report_bcm(self, real_db_conn):
        """F4: Raport po incydencie ciągłości (ISO 22301 + ITIL 4)."""
        iso22301 = find_by_standard(real_db_conn, "ISO 22301")
        itil4 = find_by_standard(real_db_conn, "ITIL 4")
        assert len(iso22301) >= 6, f"Za mało szablonów ISO 22301: {len(iso22301)}"
        assert len(itil4) >= 10, f"Za mało szablonów ITIL 4: {len(itil4)}"
        itil_paths = _paths(itil4)
        assert "itil4_incident_record.md" in itil_paths, "Brak Incident Record"


# ===========================================================================
# Grupa G — SecDevOps
# ===========================================================================


class TestGroupGSecDevOps:
    """Scenariusze G1–G4: Developer / Security Champion."""

    def test_g1_owasp_asvs_web_app(self, real_db_conn):
        """G1: OWASP ASVS — dokumenty przed go-live aplikacji webowej."""
        results = find_by_standard(real_db_conn, "OWASP ASVS")
        assert len(results) >= 5, f"Za mało szablonów OWASP ASVS: {len(results)}"
        paths = _paths(results)
        assert "owasp_asvs_cryptography_policy.md" in paths, "Brak Crypto Policy ASVS"
        assert (
            "api_security_design.md" in paths or "security_requirements_specification.md" in paths
        ), "Brak szablonu security requirements"

    def test_g2_api_design_openapi_asyncapi(self, real_db_conn):
        """G2: API design — szablony OpenAPI i AsyncAPI."""
        openapi = find_by_standard(real_db_conn, "OpenAPI 3.x")
        asyncapi = find_by_standard(real_db_conn, "AsyncAPI 3.x")
        assert len(openapi) >= 2, f"Za mało szablonów OpenAPI: {len(openapi)}"
        assert len(asyncapi) >= 2, f"Za mało szablonów AsyncAPI: {len(asyncapi)}"

    def test_g3_owasp_masvs_mobile(self, real_db_conn):
        """G3: OWASP MASVS — szablony dla aplikacji mobilnych."""
        results = find_by_standard(real_db_conn, "OWASP MASVS")
        assert len(results) >= 4, f"Za mało szablonów OWASP MASVS: {len(results)}"

    def test_g4_microservices_architecture(self, real_db_conn):
        """G4: Architektura mikroserwisów — IEEE 42010 i TOGAF."""
        ieee42010 = find_by_standard(real_db_conn, "IEEE 42010")
        togaf = find_by_standard(real_db_conn, "TOGAF ADM")
        assert len(ieee42010) >= 3, f"Za mało szablonów IEEE 42010: {len(ieee42010)}"
        assert len(togaf) >= 8, f"Za mało szablonów TOGAF: {len(togaf)}"
        all_paths = _paths(ieee42010) | _paths(togaf)
        assert "system_architecture_design.md" in all_paths, "Brak System Architecture Design"


# ===========================================================================
# Grupa H — Cloud i infrastruktura
# ===========================================================================


class TestGroupHCloud:
    """Scenariusze H1–H4: Cloud Architect / IT Operations."""

    def test_h1_cloud_migration_iso27017_cis(self, real_db_conn):
        """H1: Migracja do chmury — ISO/IEC 27017 i CIS Controls v8."""
        iso27017 = find_by_standard(real_db_conn, "ISO/IEC 27017")
        cis = find_by_standard(real_db_conn, "CIS Controls v8")
        assert len(iso27017) >= 3, f"Za mało szablonów ISO 27017: {len(iso27017)}"
        assert len(cis) >= 6, f"Za mało szablonów CIS Controls: {len(cis)}"
        iso_paths = _paths(iso27017)
        assert "cloud_security_architecture.md" in iso_paths, "Brak Cloud Security Architecture"

    def test_h2_production_env_config_availability(self, real_db_conn):
        """H2: Środowisko produkcyjne — Configuration Management i Availability Plan."""
        itil4 = find_by_standard(real_db_conn, "ITIL 4")
        iso20000 = find_by_standard(real_db_conn, "ISO 20000-1")
        itil_paths = _paths(itil4)
        iso20000_paths = _paths(iso20000)
        assert (
            "configuration_management_document.md" in itil_paths
        ), "Brak Configuration Management Document w ITIL 4"
        assert (
            "iso20000_availability_plan.md" in iso20000_paths
        ), "Brak Availability Plan ISO 20000-1"

    def test_h3_pci_dss_compliance_package(self, real_db_conn):
        """H3: PCI DSS — komplet dokumentów dla środowiska CDE."""
        results = find_by_standard(real_db_conn, "PCI DSS")
        assert len(results) >= 7, f"Za mało szablonów PCI DSS: {len(results)}"
        paths = _paths(results)
        assert (
            "payment_card_security_pci_dss.md" in paths or "pci_dss_compliance.md" in paths
        ), "Brak podstawowego szablonu PCI DSS compliance"
        assert "access_control.md" in paths, "Brak szablonu kontroli dostępu"
        assert "data_flow_diagram.md" in paths, "Brak Data Flow Diagram (wymagany PCI DSS req. 1)"

    def test_h4_nist_sp80053_ato_package(self, real_db_conn):
        """H4: NIST SP 800-53 — artefakty Authorization to Operate (ATO)."""
        results = find_by_standard(real_db_conn, "NIST SP 800-53")
        assert len(results) >= 6, f"Za mało szablonów NIST SP 800-53: {len(results)}"
        paths = _paths(results)
        required = ["authorization_requirements.md", "it_contingency_plan.md"]
        missing = [r for r in required if r not in paths]
        assert not missing, f"Brakujące szablony ATO: {missing}"
