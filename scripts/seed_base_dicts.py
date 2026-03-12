#!/usr/bin/env python3
"""
scripts/seed_base_dicts.py

Faza 9A: Zasilenie słowników bazowych w it_doc_matrix.db:
  - roles (~40 ról IT)
  - phases (23 fazy cyklu życia)
  - industries (~30 branż ISIC z nazwami PL)
  - document_categories (~15 kategorii dokumentów)
  - relationship_types (~10 typów relacji)
  - quality_dimensions (~8 wymiarów jakości)
"""

import logging
import sqlite3
from pathlib import Path

_log = logging.getLogger(__name__)

DB_PATH = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"

# ─── ROLES ────────────────────────────────────────────────────────────────────
ROLES = [
    ("PO",    "Product Owner",             "Product Owner",             "Właściciel produktu; odpowiada za backlog i priorytety"),
    ("PM",    "Project Manager",           "Project Manager",           "Kierownik projektu; planowanie, harmonogram, budżet"),
    ("BA",    "Business Analyst",          "Business Analyst",          "Analityk biznesowy; wymagania, procesy, luki"),
    ("ARCH",  "Architekt",                 "Architect",                 "Projektuje architekturę systemów IT"),
    ("SA",    "Architekt rozwiązań",       "Solution Architect",        "Projektuje rozwiązanie w kontekście biznesowym"),
    ("EA",    "Architekt korporacyjny",    "Enterprise Architect",      "Architektura całej organizacji (TOGAF)"),
    ("DEV",   "Deweloper",                 "Developer",                 "Tworzy kod aplikacji i mikroserwisów"),
    ("SDEV",  "Senior Deweloper",          "Senior Developer",          "Prowadzi techniczne aspekty rozwoju"),
    ("DEVLEAD","Tech Lead",               "Tech Lead",                  "Lider techniczny zespołu deweloperskiego"),
    ("QA",    "Inżynier QA",              "QA Engineer",               "Zapewnienie jakości: testy manualne i automatyczne"),
    ("QALEAD","QA Lead",                  "QA Lead",                   "Prowadzi strategię testowania i zespół QA"),
    ("DEVOPS","Inżynier DevOps",          "DevOps Engineer",           "CI/CD, infrastruktura, automatyzacja wdrożeń"),
    ("SRE",   "SRE",                      "Site Reliability Engineer", "Niezawodność systemów produkcyjnych, SLO/SLA"),
    ("OPS",   "Administrator systemów",   "Systems Administrator",     "Administracja serwerami, sieciami, systemami"),
    ("DBA",   "Administrator baz danych", "Database Administrator",    "Zarządzanie bazami danych, performance, backup"),
    ("SEC",   "Inżynier bezpieczeństwa",  "Security Engineer",         "Implementacja i utrzymanie zabezpieczeń"),
    ("CISO",  "CISO",                     "Chief Information Security Officer", "Strategia i zarządzanie bezpieczeństwem IT"),
    ("DPO",   "Inspektor Ochrony Danych", "Data Protection Officer",   "Zgodność z RODO/GDPR, ochrona danych osobowych"),
    ("DE",    "Inżynier danych",          "Data Engineer",             "Pipelines danych, ETL/ELT, hurtownie danych"),
    ("DS",    "Data Scientist",           "Data Scientist",            "Modele ML, analiza statystyczna, eksperymentowanie"),
    ("MLOPS", "MLOps Engineer",           "MLOps Engineer",            "Wdrożenie i monitorowanie modeli ML na produkcji"),
    ("UX",    "Projektant UX",            "UX Designer",               "Badania użyteczności, prototypy, testy użytkowników"),
    ("UI",    "Projektant UI",            "UI Designer",               "Interfejsy graficzne, system designu"),
    ("SCRUM", "Scrum Master",             "Scrum Master",              "Facylitacja Scruma, usuwanie przeszkód"),
    ("CPO",   "Chief Product Officer",    "Chief Product Officer",     "Strategia produktowa całej organizacji"),
    ("CTO",   "CTO",                      "Chief Technology Officer",  "Strategia technologiczna organizacji"),
    ("MGR",   "Menedżer IT",              "IT Manager",                "Zarządzanie zespołem i zasobami IT"),
    ("LEGAL", "Prawnik / Compliance",     "Legal / Compliance",        "Aspekty prawne, regulacyjne, umowy"),
    ("AUDIT", "Audytor",                  "Auditor",                   "Audyt wewnętrzny i zewnętrzny IT"),
    ("VENDOR","Dostawca",                 "Vendor",                    "Zewnętrzny dostawca usług lub oprogramowania"),
    ("STAKE", "Interesariusz",            "Stakeholder",               "Osoba zainteresowana wynikiem projektu"),
    ("END",   "Użytkownik końcowy",       "End User",                  "Bezpośredni użytkownik systemu lub dokumentu"),
    ("CLOUD", "Architekt chmury",         "Cloud Architect",           "Projektowanie i optymalizacja infrastruktury chmurowej"),
    ("NETW",  "Inżynier sieci",           "Network Engineer",          "Infrastruktura sieciowa, LAN/WAN, firewall"),
    ("ITSM",  "Menadżer ITSM",           "ITSM Manager",              "Zarządzanie usługami IT (ITIL)"),
    ("CHANGE","Menedżer zmian",           "Change Manager",            "Zarządzanie zmianami organizacyjnymi i IT"),
    ("RISK",  "Menedżer ryzyka",          "Risk Manager",              "Identyfikacja, ocena i mitygacja ryzyk IT"),
    ("CONT",  "Content Manager",          "Content Manager",           "Zarządzanie treścią dokumentacji i wiedzy"),
    ("TRAIN", "Trener IT",                "IT Trainer",                "Szkolenia z systemów i procesów IT"),
    ("PART",  "Partner biznesowy IT",     "IT Business Partner",       "Łącznik między IT a jednostkami biznesowymi"),
]

# ─── PHASES ───────────────────────────────────────────────────────────────────
PHASES = [
    (1,  "Inicjacja / Odkrycie",          "Initiation / Discovery",     "strategy",   False, "Wizja, cele, wstępny zakres, studium wykonalności"),
    (2,  "Analiza Wymagań",               "Requirements Analysis",       "analysis",   False, "Wymagania funkcjonalne i niefunkcjonalne, user stories"),
    (3,  "Projekt / Design",              "Design",                      "design",     False, "Architektura, projekt systemu, prototypy"),
    (4,  "Planowanie",                    "Planning",                    "planning",   False, "Harmonogram, zasoby, budżet, plan projektu"),
    (5,  "Implementacja",                 "Implementation",              "build",      True,  "Kodowanie, budowanie komponentów"),
    (6,  "Testowanie / QA",              "Testing / QA",                "quality",    True,  "Testy jednostkowe, integracyjne, systemowe, UAT"),
    (7,  "Bezpieczeństwo / Compliance",   "Security / Compliance",      "security",   False, "Testy bezpieczeństwa, audyt zgodności, certyfikacja"),
    (8,  "Wdrożenie / Deployment",        "Deployment",                  "delivery",   False, "Wdrożenie na produkcję, migracja danych"),
    (9,  "Operacje / Maintenance",        "Operations / Maintenance",    "operations", True,  "Eksploatacja, wsparcie, monitorowanie"),
    (10, "Incydenty i eskalacje",         "Incident Management",         "operations", True,  "Obsługa incydentów, eskalacje, SLA"),
    (11, "Monitoring / Observability",    "Monitoring / Observability",  "operations", True,  "Metryki, logi, alerty, dashboardy"),
    (12, "Optymalizacja wydajności",      "Performance Optimization",    "operations", True,  "Tuning, skalowanie, capacity planning"),
    (13, "Zarządzanie konfiguracją",      "Configuration Management",    "operations", True,  "CMDB, IaC, zarządzanie konfiguracją"),
    (14, "Komunikacja stakeholders",      "Stakeholder Communication",   "governance", True,  "Raporty statusowe, spotkania przeglądowe"),
    (15, "Knowledge Management",          "Knowledge Management",        "governance", True,  "Dokumentacja, baza wiedzy, onboarding"),
    (16, "Postmortem / Retrospektywa",    "Postmortem / Retrospective",  "governance", True,  "Analiza incydentów, wyciąganie wniosków"),
    (17, "Budżetowanie / Cost Mgmt",      "Budgeting / Cost Management", "governance", False, "Planowanie budżetu, rozliczenia, FinOps"),
    (18, "Vendor Management",             "Vendor Management",           "governance", True,  "Zarządzanie dostawcami, kontrakty, SLA"),
    (19, "Governance / Compliance",       "Governance / Compliance",     "governance", True,  "Zarządzanie ładem IT, audyty, regulacje"),
    (20, "Decommission / Sunset",         "Decommission / Sunset",       "closure",    False, "Wycofanie systemu, archiwizacja, migracja"),
    (21, "DR / BCP",                      "DR / BCP",                    "resilience", False, "Plan ciągłości działania, odtwarzanie po awarii"),
    (22, "Change Management",             "Change Management",           "governance", True,  "Zarządzanie zmianami (ITIL Change Mgmt)"),
    (23, "Capacity Planning",             "Capacity Planning",           "operations", True,  "Planowanie pojemności, prognozowanie wzrostu"),
]

# ─── INDUSTRIES ───────────────────────────────────────────────────────────────
INDUSTRIES = [
    ("62", "IT i oprogramowanie",           "IT and Software",            "Technologia"),
    ("63", "Usługi informacyjne",           "Information Services",       "Technologia"),
    ("61", "Telekomunikacja",               "Telecommunications",         "Technologia"),
    ("64", "Bankowość i finanse",           "Banking and Finance",        "Finanse"),
    ("65", "Ubezpieczenia",                 "Insurance",                  "Finanse"),
    ("66", "Działalność finansowa pomocnicza","Auxiliary Financial",     "Finanse"),
    ("86", "Ochrona zdrowia",               "Healthcare",                 "Zdrowie"),
    ("87", "Opieka stacjonarna",            "Residential Care",           "Zdrowie"),
    ("85", "Edukacja",                      "Education",                  "Usługi publiczne"),
    ("84", "Administracja publiczna",       "Public Administration",      "Usługi publiczne"),
    ("47", "Handel detaliczny",             "Retail",                     "Handel"),
    ("46", "Handel hurtowy",                "Wholesale",                  "Handel"),
    ("56", "Gastronomia",                   "Food and Beverage",          "Hospitality"),
    ("55", "Hotele i zakwaterowanie",       "Hotels and Accommodation",   "Hospitality"),
    ("49", "Transport lądowy",              "Land Transport",             "Transport"),
    ("50", "Transport wodny",               "Water Transport",            "Transport"),
    ("51", "Transport lotniczy",            "Air Transport",              "Transport"),
    ("52", "Magazynowanie i logistyka",     "Warehousing and Logistics",  "Transport"),
    ("35", "Energetyka",                    "Energy",                     "Przemysł"),
    ("19", "Rafinerie / paliwa",            "Oil Refining",               "Przemysł"),
    ("20", "Przemysł chemiczny",            "Chemical Industry",          "Przemysł"),
    ("26", "Elektronika",                   "Electronics",                "Przemysł"),
    ("41", "Budownictwo",                   "Construction",               "Nieruchomości"),
    ("68", "Nieruchomości",                 "Real Estate",                "Nieruchomości"),
    ("73", "Reklama i marketing",           "Advertising and Marketing",  "Media"),
    ("59", "Film i media",                  "Film and Media",             "Media"),
    ("60", "Nadawanie",                     "Broadcasting",               "Media"),
    ("79", "Turystyka",                     "Tourism",                    "Usługi"),
    ("01", "Rolnictwo",                     "Agriculture",                "Pierwotne"),
    ("75", "Usługi weterynaryjne",          "Veterinary",                 "Usługi"),
]

# ─── DOCUMENT CATEGORIES ──────────────────────────────────────────────────────
DOC_CATEGORIES = [
    ("GOVERNANCE",    "Governance",                  "Governance",                 "Dokumenty zarządcze i strategiczne IT",                "#2C3E50"),
    ("SECURITY",      "Bezpieczeństwo",              "Security",                   "Polityki, procedury i standardy bezpieczeństwa",        "#E74C3C"),
    ("ARCHITECTURE",  "Architektura",                "Architecture",               "Decyzje, diagramy i dokumenty architektoniczne",        "#3498DB"),
    ("DEVELOPMENT",   "Rozwój oprogramowania",       "Software Development",       "Wymagania, specyfikacje, dokumenty deweloperskie",      "#27AE60"),
    ("QUALITY",       "Jakość i testowanie",         "Quality and Testing",        "Plany testów, raporty jakości, strategie QA",           "#F39C12"),
    ("OPERATIONS",    "Operacje IT",                 "IT Operations",              "Runbooki, procedury operacyjne, monitoring",            "#8E44AD"),
    ("DATA",          "Zarządzanie danymi",          "Data Management",            "Modele danych, katalogi, pipeline'y",                  "#16A085"),
    ("COMPLIANCE",    "Zgodność i regulacje",        "Compliance and Regulations", "Dokumenty audytowe, zgodności, regulacyjne",           "#D35400"),
    ("PROJECT",       "Zarządzanie projektem",       "Project Management",         "Plany, harmonogramy, raporty statusowe",               "#2980B9"),
    ("INCIDENT",      "Incydenty i eskalacje",       "Incident Management",        "Playbooki, runbooki incydentowe, postmortem",          "#C0392B"),
    ("CONTINUITY",    "Ciągłość działania",          "Business Continuity",        "BCP, DRP, plany odtwarzania po awarii",                "#1ABC9C"),
    ("VENDOR",        "Zarządzanie dostawcami",      "Vendor Management",          "Kontrakty, SLA, ocena dostawców",                     "#7F8C8D"),
    ("KNOWLEDGE",     "Zarządzanie wiedzą",          "Knowledge Management",       "Bazy wiedzy, onboarding, dokumentacja procesów",      "#BDC3C7"),
    ("INFRASTRUCTURE","Infrastruktura",              "Infrastructure",             "Dokumenty infrastruktury, sieci, chmury",              "#34495E"),
    ("PRODUCT",       "Produkt i UX",                "Product and UX",             "Dokumenty produktowe, user research, roadmapy",       "#9B59B6"),
]

# ─── RELATIONSHIP TYPES ───────────────────────────────────────────────────────
REL_TYPES = [
    ("REQUIRES",    "Wymaga",           "Requires",         True,  "Dokument A nie może istnieć bez dokumentu B"),
    ("RELATES_TO",  "Powiązany z",      "Relates to",       True,  "Luźne powiązanie tematyczne lub informacyjne"),
    ("EXTENDS",     "Rozszerza",        "Extends",          False, "Dokument A jest rozwinięciem/specjalizacją B"),
    ("SUPERSEDES",  "Zastępuje",        "Supersedes",       False, "Dokument A zastępuje dokument B (nowa wersja)"),
    ("IMPLEMENTS",  "Implementuje",     "Implements",       False, "Dokument A implementuje wymagania z dokumentu B"),
    ("REFERENCES",  "Odwołuje się do",  "References",       False, "Dokument A cytuje lub odwołuje się do B"),
    ("DERIVED_FROM","Pochodzi z",       "Derived from",     False, "Dokument A jest wyprowadzony z dokumentu B"),
    ("PRECEDES",    "Poprzedza",        "Precedes",         False, "Dokument A jest tworzony przed dokumentem B (fazowo)"),
    ("VALIDATES",   "Weryfikuje",       "Validates",        False, "Dokument A weryfikuje poprawność dokumentu B"),
    ("TRIGGERS",    "Inicjuje",         "Triggers",         False, "Istnienie/zmiana dokumentu A inicjuje pracę nad B"),
]

# ─── QUALITY DIMENSIONS ───────────────────────────────────────────────────────
QUALITY_DIMS = [
    ("COMPLETENESS",  "Kompletność",    "Completeness",
     "Wszystkie wymagane sekcje i pola są wypełnione",
     "Odsetek wypełnionych sekcji do wymaganych",
     "Sprawdź listę wymaganych sekcji; szukaj pustych nagłówków",
     "70%", "90%", "template_auditor.py, checklist_atomic.jsonl"),
    ("ACCURACY",      "Dokładność",     "Accuracy",
     "Informacje są poprawne merytorycznie i aktualne",
     "Przegląd ekspercki; data ostatniej aktualizacji",
     "Porównaj z aktualnymi standardami i regulacjami",
     "Przegląd co 6 mies.", "Przegląd co 3 mies.", "regulation_updater.py"),
    ("CONSISTENCY",   "Spójność",       "Consistency",
     "Terminologia i struktura są spójne w całej bibliotece",
     "Liczba niespójności terminologicznych i strukturalnych",
     "Porównaj z szablonem wzorcowym; sprawdź słownik terminów",
     "Brak krytycznych", "0 niespójności", "bulk_section_patcher.py"),
    ("TRACEABILITY",  "Śledzalność",    "Traceability",
     "Każda sekcja ma źródło (standard, regulacja, decyzja)",
     "Odsetek sekcji z wypełnionymi standards_refs",
     "Sprawdź doc_section_guidance.standards_refs",
     "50%", "80%", "impact_analyzer.py"),
    ("TIMELINESS",    "Aktualność",     "Timeliness",
     "Dokument jest aktualny względem obowiązujących regulacji",
     "Czas od ostatniej aktualizacji vs. częstotliwość przeglądów",
     "Sprawdź datę w ## Metadane; porównaj z datą nowelizacji regulacji",
     "< 12 mies.", "< 6 mies.", "changelog_tracker.py"),
    ("USABILITY",     "Użyteczność",    "Usability",
     "Użytkownik końcowy może efektywnie wypełnić dokument na podstawie guidance",
     "Ocena guidance (score z template_auditor); feedback użytkowników",
     "Uruchom template_auditor.py; sprawdź score >= 60",
     "Score >= 40", "Score >= 70", "template_auditor.py"),
    ("LINKAGE",       "Powiązania",     "Linkage",
     "Powiązania między dokumentami są poprawne i rozwiązane",
     "Odsetek content_links_resolved do content_links",
     "Sprawdź content_links_resolved; uruchom resolve_content_links_extended.py",
     "20%", "50%", "resolve_content_links_extended.py"),
    ("COMPLIANCE",    "Zgodność formalna","Formal Compliance",
     "Dokument spełnia wymogi formalne (brak emoji, struktura, metadane)",
     "Wynik emoji_check; obecność ## Metadane; brak TODO",
     "Uruchom pipeline_run.py; sprawdź emoji_report.json",
     "0 emoji, metadane", "0 emoji, 0 TODO, metadane", "pipeline_run.py"),
]


def seed_roles(cur):
    cur.executemany("""
        INSERT OR IGNORE INTO roles (role_code, role_name_pl, role_name_en, description)
        VALUES (?, ?, ?, ?)
    """, [(r[0], r[1], r[2], r[3]) for r in ROLES])
    return len(ROLES)


def seed_phases(cur):
    rows = []
    for p in PHASES:
        rows.append((p[0], p[1], p[2], p[3], 1 if p[4] else 0, p[5]))
    cur.executemany("""
        INSERT OR IGNORE INTO phases
          (phase_number, phase_name_pl, phase_name_en, phase_category, is_iterative, phase_description)
        VALUES (?, ?, ?, ?, ?, ?)
    """, rows)
    return len(rows)


def seed_industries(cur):
    rows = [(r[0], r[1], r[2], r[3]) for r in INDUSTRIES]
    cur.executemany("""
        INSERT OR IGNORE INTO industries (industry_code, name_pl, name_en, category)
        VALUES (?, ?, ?, ?)
    """, rows)
    return len(rows)


def seed_doc_categories(cur):
    rows = [(r[0], r[1], r[2], r[3], r[4]) for r in DOC_CATEGORIES]
    cur.executemany("""
        INSERT OR IGNORE INTO document_categories
          (category_code, category_name_pl, category_name_en, description, color_hex)
        VALUES (?, ?, ?, ?, ?)
    """, rows)
    return len(rows)


def seed_rel_types(cur):
    rows = [(r[0], r[1], r[2], 1 if r[3] else 0, r[4]) for r in REL_TYPES]
    cur.executemany("""
        INSERT OR IGNORE INTO relationship_types
          (rel_type_code, rel_type_name_pl, rel_type_name_en, is_bidirectional, description)
        VALUES (?, ?, ?, ?, ?)
    """, rows)
    return len(rows)


def seed_quality_dims(cur):
    rows = [(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]) for r in QUALITY_DIMS]
    cur.executemany("""
        INSERT OR IGNORE INTO quality_dimensions
          (dimension, name, name, description, measurement_method, example_checks, good_threshold, target_threshold, tools)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, rows)
    return len(rows)


def main():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # Check columns for each table before inserting
    def get_cols(table):
        cur.execute(f'PRAGMA table_info("{table}")')
        return {r[1] for r in cur.fetchall()}

    results = {}

    # roles
    cols = get_cols("roles")
    if "role_name_pl" in cols:
        cur.executemany("INSERT OR IGNORE INTO roles (role_code, role_name_pl, role_name_en, description) VALUES (?,?,?,?)",
                        [(r[0], r[1], r[2], r[3]) for r in ROLES])
    elif "role_name" in cols:
        cur.executemany("INSERT OR IGNORE INTO roles (role_code, role_name, description) VALUES (?,?,?)",
                        [(r[0], r[1], r[3]) for r in ROLES])
    results["roles"] = len(ROLES)

    # phases
    cols = get_cols("phases")
    if "phase_number" in cols and "phase_name_pl" in cols:
        rows = [(p[0], p[1], p[2], p[3], 1 if p[4] else 0, p[5]) for p in PHASES]
        cur.executemany("""INSERT OR IGNORE INTO phases
            (phase_number, phase_name_pl, phase_name_en, phase_category, is_iterative, phase_description)
            VALUES (?,?,?,?,?,?)""", rows)
    elif "phase_number" in cols and "name_pl" in cols:
        rows = [(p[0], p[1], p[2], p[3]) for p in PHASES]
        cur.executemany("INSERT OR IGNORE INTO phases (phase_number, name_pl, name_en, phase_category) VALUES (?,?,?,?)", rows)
    elif "phase_number" in cols:
        rows = [(p[0], p[1], p[3]) for p in PHASES]
        cur.executemany("INSERT OR IGNORE INTO phases (phase_number, name, phase_category) VALUES (?,?,?)", rows)
    results["phases"] = len(PHASES)

    # industries
    cols = get_cols("industries")
    if "industry_code" in cols and "name_pl" in cols:
        rows = [(r[0], r[1], r[2], r[3]) for r in INDUSTRIES]
        cur.executemany("INSERT OR IGNORE INTO industries (industry_code, name_pl, name_en, category) VALUES (?,?,?,?)", rows)
    elif "industry_code" in cols and "industry_name_pl" in cols:
        rows = [(r[0], r[1], r[2], r[3]) for r in INDUSTRIES]
        cur.executemany("INSERT OR IGNORE INTO industries (industry_code, industry_name_pl, industry_name_en, category) VALUES (?,?,?,?)", rows)
    elif "industry_code" in cols:
        rows = [(r[0], r[1]) for r in INDUSTRIES]
        cur.executemany("INSERT OR IGNORE INTO industries (industry_code, name) VALUES (?,?)", rows)
    results["industries"] = len(INDUSTRIES)

    # document_categories
    cols = get_cols("document_categories")
    if "category_code" in cols and "category_name_pl" in cols:
        rows = [(r[0], r[1], r[2], r[3], r[4]) for r in DOC_CATEGORIES]
        cur.executemany("""INSERT OR IGNORE INTO document_categories
            (category_code, category_name_pl, category_name_en, description, color_hex)
            VALUES (?,?,?,?,?)""", rows)
    elif "category_code" in cols and "category_name_en" in cols:
        rows = [(r[0], r[2], r[3]) for r in DOC_CATEGORIES]
        cur.executemany("INSERT OR IGNORE INTO document_categories (category_code, category_name_en, description) VALUES (?,?,?)", rows)
    elif "category_code" in cols:
        rows = [(r[0], r[1]) for r in DOC_CATEGORIES]
        cur.executemany("INSERT OR IGNORE INTO document_categories (category_code, description) VALUES (?,?)", rows)
    results["document_categories"] = len(DOC_CATEGORIES)

    # relationship_types
    cols = get_cols("relationship_types")
    if "rel_type_code" in cols and "rel_type_name_pl" in cols:
        rows = [(r[0], r[1], r[2], 1 if r[3] else 0, r[4]) for r in REL_TYPES]
        cur.executemany("""INSERT OR IGNORE INTO relationship_types
            (rel_type_code, rel_type_name_pl, rel_type_name_en, is_bidirectional, description)
            VALUES (?,?,?,?,?)""", rows)
    elif "rel_type_code" in cols:
        rows = [(r[0], r[2], r[4]) for r in REL_TYPES]
        cur.executemany("INSERT OR IGNORE INTO relationship_types (rel_type_code, rel_type_name_en, description) VALUES (?,?,?)", rows)
    elif "rel_code" in cols:
        rows = [(r[0], r[2], r[1], r[4]) for r in REL_TYPES]
        cur.executemany("INSERT OR IGNORE INTO relationship_types (rel_code, rel_name_en, rel_name_pl, description) VALUES (?,?,?,?)", rows)
    results["relationship_types"] = len(REL_TYPES)

    # quality_dimensions
    cols = get_cols("quality_dimensions")
    if "dimension" in cols and "name" in cols:
        for r in QUALITY_DIMS:
            try:
                cur.execute("""INSERT OR IGNORE INTO quality_dimensions
                    (dimension, name, description, measurement_method, example_checks, good_threshold, target_threshold, tools)
                    VALUES (?,?,?,?,?,?,?,?)""",
                    (r[0], r[1], r[3], r[4], r[5], r[6], r[7], r[8]))
            except Exception:
                # fallback — fewer columns
                try:
                    cur.execute("INSERT OR IGNORE INTO quality_dimensions (dimension, name, description) VALUES (?,?,?)",
                                (r[0], r[1], r[3]))
                except Exception as exc:
                    _log.debug("quality_dimensions fallback insert failed: %s: %s", type(exc).__name__, exc)
    results["quality_dimensions"] = len(QUALITY_DIMS)

    conn.commit()
    conn.close()

    print("Faza 9A — Zasilenie słowników bazowych:")
    for table, n in results.items():
        print(f"  {table:25s}: {n} wierszy")
    print("\nGotowe.")


if __name__ == "__main__":
    main()
