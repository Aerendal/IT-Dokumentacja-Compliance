#!/usr/bin/env python3
"""
map_standards_to_docs.py
Mapuje standardy miedzynarodowe i polskie regulacje do szablonow dokumentow
na podstawie slow kluczowych w tytule i sciezce szablonu.

Tworzy/wypelnia tabele:
  - doc_standard_mapping  (nowa: lekka tabela path -> standard_code)
  - doc_regulation_mapping (nowa: path -> regulation_code)

Oraz wstrzykuje sekcje "Majace zastosowanie standardy i normy" do plikow .md
jesli jeszcze jej nie ma.
"""

import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"
TEMPLATES_ROOT = Path(__file__).parent.parent / "generated_templates"

# ---------------------------------------------------------------------------
# Reguly mapowania: lista (pattern_in_path_or_title, [lista kodow standardow])
# Dopasowanie case-insensitive do sciezki pliku lub tytulu.
# ---------------------------------------------------------------------------
STANDARD_RULES: list[tuple[list[str], list[str]]] = [
    # Bezpieczenstwo informacji
    (
        [
            "security",
            "bezpiecze",
            "isms",
            "access_control",
            "access control",
            "vulnerability",
            "penetration",
            "pentest",
            "threat",
            "risk",
            "incident",
            "forensic",
            "soc ",
            "siem",
            "dlp",
            "encryption",
            "cryptograph",
            "firewall",
            "iam",
            "identity",
            "authentication",
            "authorization",
            "zero_trust",
            "zero trust",
            "hardening",
        ],
        ["ISO/IEC 27001", "ISO/IEC 27002", "ISO/IEC 27005", "CIS Controls v8", "NIST CSF"],
    ),
    # API i aplikacje webowe
    (
        [
            "api_security",
            "api security",
            "owasp",
            "web_security",
            "application_security",
            "secure_coding",
            "code_review_security",
            "xss",
            "sql_injection",
            "csrf",
        ],
        ["OWASP ASVS", "ISO/IEC 27001", "ISO/IEC 27002"],
    ),
    # Mobile
    (
        ["mobile_security", "android_security", "ios_security", "masvs", "mstg"],
        ["OWASP MASVS", "ISO/IEC 27001"],
    ),
    # Chmura
    (
        [
            "cloud",
            "chmura",
            "azure",
            "aws",
            "gcp",
            "kubernetes",
            "container",
            "serverless",
            "saas",
            "paas",
            "iaas",
        ],
        ["ISO/IEC 27017", "ISO/IEC 27018", "SOC 2", "CIS Controls v8"],
    ),
    # Prywatnosc i dane osobowe
    (
        [
            "privacy",
            "prywatno",
            "gdpr",
            "rodo",
            "personal_data",
            "dane_osobowe",
            "pii",
            "dpia",
            "data_protection",
            "ochrona_danych",
            "consent",
            "anonymiz",
            "pseudonymiz",
        ],
        ["GDPR / RODO", "ISO/IEC 27701", "ISO/IEC 27018"],
    ),
    # Jakosc oprogramowania
    (
        [
            "quality",
            "jakosc",
            "test",
            "qa",
            "defect",
            "bug",
            "verification",
            "validation",
            "acceptance",
            "review",
            "inspection",
            "metric",
            "kpi",
            "sla",
            "nfr",
            "non_functional",
            "performance",
            "load_test",
            "stress_test",
        ],
        ["ISO/IEC 25010", "ISO 9001", "IEEE 829"],
    ),
    # Wymagania
    (
        [
            "requirement",
            "wymagani",
            "srs",
            "brd",
            "frs",
            "use_case",
            "user_story",
            "backlog",
            "specification",
        ],
        ["IEEE 830", "ISO/IEC 12207", "ISO 9001"],
    ),
    # Projekt / Design
    (
        [
            "design",
            "architecture",
            "architektur",
            "sdd",
            "adr",
            "decision",
            "pattern",
            "uml",
            "diagram",
            "blueprint",
            "solution",
        ],
        ["IEEE 1016", "IEEE 42010", "TOGAF ADM", "ISO/IEC 15288"],
    ),
    # Zarzadzanie projektami
    (
        [
            "project",
            "projekt",
            "gantt",
            "roadmap",
            "milestone",
            "sprint",
            "scrum",
            "agile",
            "kanban",
            "wbs",
            "charter",
            "kickoff",
            "retrospect",
            "standup",
            "planning",
        ],
        ["PMBOK 7", "PRINCE2 7", "SCRUM Guide", "ISO/IEC 12207"],
    ),
    # Zarzadzanie produktem
    (
        [
            "product",
            "produkt",
            "vision",
            "wizja",
            "okr",
            "north_star",
            "go_to_market",
            "launch",
            "roadmap",
        ],
        ["PMBOK 7", "SCRUM Guide"],
    ),
    # ITSM / Operacje
    (
        [
            "incident_management",
            "problem_management",
            "change_management",
            "service_desk",
            "helpdesk",
            "cmdb",
            "configuration_management",
            "release_management",
            "itsm",
            "servicedesk",
            "service_catalog",
            "sla",
            "escalation",
            "on_call",
        ],
        ["ITIL 4", "ISO 20000-1"],
    ),
    # Ciaglosc dzialania / DR
    (
        [
            "business_continuity",
            "disaster_recovery",
            "bcp",
            "drp",
            "rto",
            "rpo",
            "backup",
            "failover",
            "restore",
            "recovery",
            "ciaglo",
            "bcm",
        ],
        ["ISO 22301", "ISO/IEC 27001", "ITIL 4"],
    ),
    # DevOps / CI-CD
    (
        [
            "devops",
            "ci_cd",
            "cicd",
            "pipeline",
            "deployment",
            "release",
            "infrastructure_as_code",
            "iac",
            "terraform",
            "ansible",
            "gitops",
            "monitoring",
            "observability",
            "alerting",
            "sre",
            "reliability",
        ],
        ["ISO/IEC 12207", "ITIL 4", "CIS Controls v8"],
    ),
    # AI / ML
    (
        [
            "machine_learning",
            "deep_learning",
            "ai_",
            "_ai",
            "mlops",
            "model",
            "neural",
            "llm",
            "nlp",
            "computer_vision",
            "dataset",
            "training",
            "inference",
            "bias",
            "fairness",
            "explainab",
            "ai_ethics",
        ],
        ["ISO/IEC 42001", "ISO/IEC 23053", "NIST CSF"],
    ),
    # Dane / Data Engineering
    (
        [
            "data_governance",
            "data_quality",
            "data_catalog",
            "data_lineage",
            "data_warehouse",
            "data_lake",
            "etl",
            "elt",
            "pipeline_data",
            "master_data",
            "metadata",
            "big_data",
            "analytics",
            "bi_",
        ],
        ["ISO/IEC 20546", "ISO 9001", "ISO/IEC 25010"],
    ),
    # API (ogolnie)
    (
        [
            "api_design",
            "api_documentation",
            "openapi",
            "swagger",
            "rest_api",
            "graphql",
            "grpc",
            "api_gateway",
            "api_versioning",
            "api_management",
        ],
        ["OpenAPI 3.x", "ISO/IEC 27001", "ITIL 4"],
    ),
    # Platnosci / Fintech
    (
        [
            "payment",
            "platno",
            "pci",
            "card",
            "transaction",
            "billing",
            "fintech",
            "banking",
            "wallet",
            "checkout",
        ],
        ["PCI DSS", "GDPR / RODO", "ISO/IEC 27001"],
    ),
    # Zdrowie
    (
        [
            "health",
            "medical",
            "clinical",
            "patient",
            "ehr",
            "fhir",
            "hl7",
            "telemedicine",
            "telemedycyn",
            "dicom",
            "hipaa",
        ],
        ["HL7 FHIR", "ISO/IEC 27001", "GDPR / RODO"],
    ),
    # Architektura korporacyjna / Lad IT
    (
        [
            "enterprise_architecture",
            "ea_",
            "_ea_",
            "governance",
            "lad",
            "board",
            "audit",
            "compliance",
            "regulatory",
            "cobit",
        ],
        ["COBIT 2019", "TOGAF ADM", "ISO/IEC 38500"],
    ),
    # Dokumentacja techniczna
    (
        [
            "technical_documentation",
            "system_documentation",
            "software_documentation",
            "dokumentacja_techniczna",
            "release_notes",
            "changelog",
            "wiki",
        ],
        ["ISO/IEC 12207", "IEEE 829", "ISO 9001"],
    ),
    # Scaled Agile / Enterprise Agile
    (
        ["safe_", "agile_at_scale", "scaled_agile", "pi_planning", "art_", "portfolio_management"],
        ["SAFe 6.0", "PMBOK 7"],
    ),
]

REGULATION_RULES: list[tuple[list[str], list[str]]] = [
    # Cyberbezpieczenstwo / KSC
    (
        [
            "security",
            "bezpiecze",
            "ksc",
            "csirt",
            "incident",
            "vulnerability",
            "penetration",
            "cybersecu",
            "nis2",
            "dora",
        ],
        ["KSC-PL", "CERT-PL-WYTYCZNE"],
    ),
    # Dane osobowe / RODO
    (
        [
            "privacy",
            "prywatno",
            "gdpr",
            "rodo",
            "personal_data",
            "dane_osobowe",
            "dpia",
            "data_protection",
            "ochrona_danych",
            "consent",
            "anonymiz",
            "pii",
        ],
        ["UODO-PL"],
    ),
    # E-commerce / serwisy online
    (
        [
            "e_commerce",
            "ecommerce",
            "web_service",
            "online_service",
            "portal",
            "sklep",
            "marketplace",
            "cookies",
            "regulamin",
        ],
        ["UŚUDE-PL", "UODO-PL"],
    ),
    # Finanse / fintech
    (
        [
            "payment",
            "platno",
            "billing",
            "fintech",
            "banking",
            "financial",
            "finans",
            "trading",
            "investment",
            "portfolio_financial",
            "mifid",
            "kyc",
            "aml",
            "credit",
            "loan",
        ],
        ["MIFID2-PL", "KNF-REKOM-IT", "UODO-PL"],
    ),
    # Ubezpieczenia
    (
        ["insurance", "ubezpiecz", "solvency", "actuarial", "claim", "policy_insurance"],
        ["SOLVENCY2-PL", "KNF-REKOM-IT"],
    ),
    # Administracja publiczna
    (
        [
            "public_sector",
            "administrac",
            "government",
            "e_government",
            "public_procurement",
            "zamowien",
            "pzp",
            "epuap",
            "obywatel",
        ],
        ["PZP-PL", "MC-INTEROP-PL", "CYBERSEC-STRATEGIA-PL"],
    ),
    # Telekomunikacja
    (
        ["telecom", "telekomunikac", "network", "5g", "lte", "uke", "carrier", "operator"],
        ["PT-PL", "UKE-WYTYCZNE", "KSC-PL"],
    ),
    # Rachunkowosc / ERP
    (
        [
            "accounting",
            "rachunko",
            "erp",
            "financial_reporting",
            "ledger",
            "invoice",
            "faktura",
            "ksiegowosc",
        ],
        ["UoR-PL"],
    ),
    # Podpis elektroniczny / KEP
    (
        [
            "electronic_signature",
            "podpis_elektroniczny",
            "kep",
            "eidas",
            "qualified_signature",
            "timestamp",
            "certificate_management",
        ],
        ["KEP-PL"],
    ),
    # Standardy jakosci (normy PN)
    (
        [
            "quality",
            "jakosc",
            "iso_9001",
            "qms",
            "iso_27001",
            "isms",
            "iso_20000",
            "itsm",
            "iso_25010",
            "squale",
        ],
        ["PN-EN-ISO-9001", "PN-ISO/IEC-27001", "PN-EN-ISO-IEC-20000-1"],
    ),
    # Ciaglosc dzialania
    (["business_continuity", "disaster_recovery", "bcp", "drp", "bcm"], ["PN-ISO-22301", "KSC-PL"]),
    # AI / ML
    (
        ["machine_learning", "ai_", "_ai", "mlops", "artificial_intelligence", "deep_learning"],
        ["UODO-PL"],
    ),  # RODO dotyczy AI przetwarzajacego dane osobowe
]


def create_mapping_tables(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS doc_standard_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_path TEXT NOT NULL,
            standard_code TEXT NOT NULL,
            match_reason TEXT,
            UNIQUE(doc_path, standard_code)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS doc_regulation_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_path TEXT NOT NULL,
            regulation_code TEXT NOT NULL,
            match_reason TEXT,
            UNIQUE(doc_path, regulation_code)
        )
    """)
    conn.commit()


def match_rules(path: str, title: str, rules: list) -> list[str]:
    """Zwraca liste dopasowanych kodow dla danej sciezki/tytulu."""
    combined = (path + " " + title).lower()
    matched = set()
    for keywords, codes in rules:
        for kw in keywords:
            if kw.lower() in combined:
                matched.update(codes)
                break
    return sorted(matched)


def build_mappings(conn: sqlite3.Connection, dry_run: bool = False):
    cur = conn.cursor()

    # Pobierz wszystkie dokumenty
    cur.execute("SELECT doc_uid, path, title FROM docs")
    docs = cur.fetchall()
    print(f"  Dokumentow do przetworzenia: {len(docs)}")

    std_inserts = []
    reg_inserts = []
    std_total = 0
    reg_total = 0

    for _doc_uid, path, title in docs:
        path = path or ""
        title = title or ""

        std_codes = match_rules(path, title, STANDARD_RULES)
        for code in std_codes:
            std_inserts.append((path, code, "keyword_match"))
            std_total += 1

        reg_codes = match_rules(path, title, REGULATION_RULES)
        for code in reg_codes:
            reg_inserts.append((path, code, "keyword_match"))
            reg_total += 1

    print(f"  doc_standard_mapping: {std_total} wpisow dla {len(docs)} dokumentow")
    print(f"  doc_regulation_mapping: {reg_total} wpisow dla {len(docs)} dokumentow")

    if not dry_run:
        cur.execute("DELETE FROM doc_standard_mapping")
        cur.execute("DELETE FROM doc_regulation_mapping")
        cur.executemany(
            "INSERT OR IGNORE INTO doc_standard_mapping (doc_path, standard_code, match_reason) VALUES (?,?,?)",
            std_inserts,
        )
        cur.executemany(
            "INSERT OR IGNORE INTO doc_regulation_mapping (doc_path, regulation_code, match_reason) VALUES (?,?,?)",
            reg_inserts,
        )
        conn.commit()
        print("  Zapisano do DB.")


def inject_standards_section(dry_run: bool = False, limit: int = 0):
    """
    Wstrzykuje sekcje 'Majace zastosowanie standardy i normy' do plikow .md.
    Pomija pliki, ktore juz maja te sekcje.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Pobierz mapowanie path -> standardy + regulacje
    cur.execute("""
        SELECT m.doc_path,
               GROUP_CONCAT(DISTINCT s.standard_code) AS stds,
               GROUP_CONCAT(DISTINCT s.standard_name) AS std_names
        FROM doc_standard_mapping m
        JOIN standards s ON m.standard_code = s.standard_code
        GROUP BY m.doc_path
    """)
    std_map = {
        r[0]: list(zip(r[1].split(","), r[2].split(","))) if r[1] else [] for r in cur.fetchall()
    }

    cur.execute("""
        SELECT m.doc_path,
               GROUP_CONCAT(DISTINCT r.regulation_code) AS regs,
               GROUP_CONCAT(DISTINCT r.regulation_name) AS reg_names
        FROM doc_regulation_mapping m
        JOIN compliance_regulations r ON m.regulation_code = r.regulation_code
        GROUP BY m.doc_path
    """)
    reg_map = {
        r[0]: list(zip(r[1].split(","), r[2].split(","))) if r[1] else [] for r in cur.fetchall()
    }
    conn.close()

    SECTION_HEADER = "## Mające zastosowanie standardy i normy"
    INJECT_BEFORE = "## Jak używać dokumentu"  # wstrzyknij przed ta sekcja

    modified = 0
    skipped = 0
    processed = 0

    for md_file in sorted(TEMPLATES_ROOT.rglob("*.md")):
        if limit and processed >= limit:
            break

        rel_path = md_file.relative_to(TEMPLATES_ROOT).as_posix()
        stds = std_map.get(rel_path, [])
        regs = reg_map.get(rel_path, [])

        if not stds and not regs:
            skipped += 1
            continue

        content = md_file.read_text(encoding="utf-8")
        if SECTION_HEADER in content:
            skipped += 1
            continue

        # Buduj sekcje
        lines = [SECTION_HEADER, ""]
        if stds:
            lines.append("### Standardy międzynarodowe")
            for code, name in stds:
                lines.append(f"- **{code}** — {name}")
            lines.append("")
        if regs:
            lines.append("### Polskie normy i regulacje")
            for code, name in regs:
                lines.append(f"- **{code}** — {name}")
            lines.append("")
        lines.append(
            "> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe "
            "normy/regulacje specyficzne dla kontekstu projektu."
        )
        lines.append("")
        section_text = "\n".join(lines)

        # Wstrzyknij przed "## Jak używać dokumentu" lub na koniec
        if INJECT_BEFORE in content:
            new_content = content.replace(INJECT_BEFORE, section_text + INJECT_BEFORE, 1)
        else:
            new_content = content.rstrip() + "\n\n" + section_text

        processed += 1
        if not dry_run:
            md_file.write_text(new_content, encoding="utf-8")
        modified += 1

    print(
        f"  Zmodyfikowano: {modified} plikow | Pominieto (brak mapowania lub juz ma sekcje): {skipped}"
    )
    if dry_run:
        print("  DRY-RUN — pliki nie zostaly zapisane.")


def main():
    dry_run = "--dry-run" in sys.argv
    limit = 0
    for arg in sys.argv:
        if arg.startswith("--limit="):
            limit = int(arg.split("=")[1])

    if dry_run:
        print("=== TRYB DRY-RUN ===")

    conn = sqlite3.connect(DB_PATH)
    create_mapping_tables(conn)
    build_mappings(conn, dry_run=dry_run)
    conn.close()

    print("\nWstrzykiwanie sekcji standardow do szablonow .md...")
    inject_standards_section(dry_run=dry_run, limit=limit)
    print("Gotowe.")


if __name__ == "__main__":
    main()
