#!/usr/bin/env python3
"""
seed_standard_controls.py — Tworzy i wypełnia tabelę standard_controls.

Użycie:
  python3 seed_standard_controls.py [--db PATH] [--apply] [--dry-run] [--standard CODE]
"""

import argparse
import sqlite3

DB_DEFAULT = "reports/it_doc_matrix.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS standard_controls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    standard_code TEXT NOT NULL,
    control_id TEXT NOT NULL,
    control_name TEXT NOT NULL,
    theme TEXT,
    description TEXT,
    UNIQUE(standard_code, control_id)
);
"""

ISO27001_CONTROLS = [
    # Organizational (A.5.x)
    ("ISO/IEC 27001", "A.5.1", "Policies for information security", "Organizational", None),
    (
        "ISO/IEC 27001",
        "A.5.2",
        "Information security roles and responsibilities",
        "Organizational",
        None,
    ),
    ("ISO/IEC 27001", "A.5.3", "Segregation of duties", "Organizational", None),
    ("ISO/IEC 27001", "A.5.4", "Management responsibilities", "Organizational", None),
    ("ISO/IEC 27001", "A.5.5", "Contact with authorities", "Organizational", None),
    ("ISO/IEC 27001", "A.5.6", "Contact with special interest groups", "Organizational", None),
    ("ISO/IEC 27001", "A.5.7", "Threat intelligence", "Organizational", None),
    (
        "ISO/IEC 27001",
        "A.5.8",
        "Information security in project management",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.9",
        "Inventory of information and other associated assets",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.10",
        "Acceptable use of information and other associated assets",
        "Organizational",
        None,
    ),
    ("ISO/IEC 27001", "A.5.11", "Return of assets", "Organizational", None),
    ("ISO/IEC 27001", "A.5.12", "Classification of information", "Organizational", None),
    ("ISO/IEC 27001", "A.5.13", "Labelling of information", "Organizational", None),
    ("ISO/IEC 27001", "A.5.14", "Information transfer", "Organizational", None),
    ("ISO/IEC 27001", "A.5.15", "Access control", "Organizational", None),
    ("ISO/IEC 27001", "A.5.16", "Identity management", "Organizational", None),
    ("ISO/IEC 27001", "A.5.17", "Authentication information", "Organizational", None),
    ("ISO/IEC 27001", "A.5.18", "Access rights", "Organizational", None),
    (
        "ISO/IEC 27001",
        "A.5.19",
        "Information security in supplier relationships",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.20",
        "Addressing information security within supplier agreements",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.21",
        "Managing information security in the ICT supply chain",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.22",
        "Monitoring, review and change management of supplier services",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.23",
        "Information security for use of cloud services",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.24",
        "Information security incident management planning and preparation",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.25",
        "Assessment and decision on information security events",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.26",
        "Response to information security incidents",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.27",
        "Learning from information security incidents",
        "Organizational",
        None,
    ),
    ("ISO/IEC 27001", "A.5.28", "Collection of evidence", "Organizational", None),
    ("ISO/IEC 27001", "A.5.29", "Information security during disruption", "Organizational", None),
    ("ISO/IEC 27001", "A.5.30", "ICT readiness for business continuity", "Organizational", None),
    (
        "ISO/IEC 27001",
        "A.5.31",
        "Legal, statutory, regulatory and contractual requirements",
        "Organizational",
        None,
    ),
    ("ISO/IEC 27001", "A.5.32", "Intellectual property rights", "Organizational", None),
    ("ISO/IEC 27001", "A.5.33", "Protection of records", "Organizational", None),
    (
        "ISO/IEC 27001",
        "A.5.34",
        "Privacy and protection of personally identifiable information",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.35",
        "Independent review of information security",
        "Organizational",
        None,
    ),
    (
        "ISO/IEC 27001",
        "A.5.36",
        "Compliance with policies, rules and standards for information security",
        "Organizational",
        None,
    ),
    ("ISO/IEC 27001", "A.5.37", "Documented operating procedures", "Organizational", None),
    # People (A.6.x)
    ("ISO/IEC 27001", "A.6.1", "Screening", "People", None),
    ("ISO/IEC 27001", "A.6.2", "Terms and conditions of employment", "People", None),
    (
        "ISO/IEC 27001",
        "A.6.3",
        "Information security awareness, education and training",
        "People",
        None,
    ),
    ("ISO/IEC 27001", "A.6.4", "Disciplinary process", "People", None),
    (
        "ISO/IEC 27001",
        "A.6.5",
        "Responsibilities after termination or change of employment",
        "People",
        None,
    ),
    ("ISO/IEC 27001", "A.6.6", "Confidentiality or non-disclosure agreements", "People", None),
    ("ISO/IEC 27001", "A.6.7", "Remote working", "People", None),
    ("ISO/IEC 27001", "A.6.8", "Information security event reporting", "People", None),
    # Physical (A.7.x)
    ("ISO/IEC 27001", "A.7.1", "Physical security perimeters", "Physical", None),
    ("ISO/IEC 27001", "A.7.2", "Physical entry", "Physical", None),
    ("ISO/IEC 27001", "A.7.3", "Securing offices, rooms and facilities", "Physical", None),
    ("ISO/IEC 27001", "A.7.4", "Physical security monitoring", "Physical", None),
    (
        "ISO/IEC 27001",
        "A.7.5",
        "Protecting against physical and environmental threats",
        "Physical",
        None,
    ),
    ("ISO/IEC 27001", "A.7.6", "Working in secure areas", "Physical", None),
    ("ISO/IEC 27001", "A.7.7", "Clear desk and clear screen", "Physical", None),
    ("ISO/IEC 27001", "A.7.8", "Equipment siting and protection", "Physical", None),
    ("ISO/IEC 27001", "A.7.9", "Security of assets off-premises", "Physical", None),
    ("ISO/IEC 27001", "A.7.10", "Storage media", "Physical", None),
    ("ISO/IEC 27001", "A.7.11", "Supporting utilities", "Physical", None),
    ("ISO/IEC 27001", "A.7.12", "Cabling security", "Physical", None),
    ("ISO/IEC 27001", "A.7.13", "Equipment maintenance", "Physical", None),
    ("ISO/IEC 27001", "A.7.14", "Secure disposal or re-use of equipment", "Physical", None),
    # Technological (A.8.x)
    ("ISO/IEC 27001", "A.8.1", "User endpoint devices", "Technological", None),
    ("ISO/IEC 27001", "A.8.2", "Privileged access rights", "Technological", None),
    ("ISO/IEC 27001", "A.8.3", "Information access restriction", "Technological", None),
    ("ISO/IEC 27001", "A.8.4", "Access to source code", "Technological", None),
    ("ISO/IEC 27001", "A.8.5", "Secure authentication", "Technological", None),
    ("ISO/IEC 27001", "A.8.6", "Capacity management", "Technological", None),
    ("ISO/IEC 27001", "A.8.7", "Protection against malware", "Technological", None),
    ("ISO/IEC 27001", "A.8.8", "Management of technical vulnerabilities", "Technological", None),
    ("ISO/IEC 27001", "A.8.9", "Configuration management", "Technological", None),
    ("ISO/IEC 27001", "A.8.10", "Information deletion", "Technological", None),
    ("ISO/IEC 27001", "A.8.11", "Data masking", "Technological", None),
    ("ISO/IEC 27001", "A.8.12", "Data leakage prevention", "Technological", None),
    ("ISO/IEC 27001", "A.8.13", "Information backup", "Technological", None),
    (
        "ISO/IEC 27001",
        "A.8.14",
        "Redundancy of information processing facilities",
        "Technological",
        None,
    ),
    ("ISO/IEC 27001", "A.8.15", "Logging", "Technological", None),
    ("ISO/IEC 27001", "A.8.16", "Monitoring activities", "Technological", None),
    ("ISO/IEC 27001", "A.8.17", "Clock synchronization", "Technological", None),
    ("ISO/IEC 27001", "A.8.18", "Use of privileged utility programs", "Technological", None),
    (
        "ISO/IEC 27001",
        "A.8.19",
        "Installation of software on operational systems",
        "Technological",
        None,
    ),
    ("ISO/IEC 27001", "A.8.20", "Networks security", "Technological", None),
    ("ISO/IEC 27001", "A.8.21", "Security of network services", "Technological", None),
    ("ISO/IEC 27001", "A.8.22", "Segregation of networks", "Technological", None),
    ("ISO/IEC 27001", "A.8.23", "Web filtering", "Technological", None),
    ("ISO/IEC 27001", "A.8.24", "Use of cryptography", "Technological", None),
    ("ISO/IEC 27001", "A.8.25", "Secure development life cycle", "Technological", None),
    ("ISO/IEC 27001", "A.8.26", "Application security requirements", "Technological", None),
    (
        "ISO/IEC 27001",
        "A.8.27",
        "Secure system architecture and engineering principles",
        "Technological",
        None,
    ),
    ("ISO/IEC 27001", "A.8.28", "Secure coding", "Technological", None),
    (
        "ISO/IEC 27001",
        "A.8.29",
        "Security testing in development and acceptance",
        "Technological",
        None,
    ),
    ("ISO/IEC 27001", "A.8.30", "Outsourced development", "Technological", None),
    (
        "ISO/IEC 27001",
        "A.8.31",
        "Separation of development, test and production environments",
        "Technological",
        None,
    ),
    ("ISO/IEC 27001", "A.8.32", "Change management", "Technological", None),
    ("ISO/IEC 27001", "A.8.33", "Test information", "Technological", None),
    (
        "ISO/IEC 27001",
        "A.8.34",
        "Protection of information systems during audit testing",
        "Technological",
        None,
    ),
]

NIST_CSF_CONTROLS = [
    # GOVERN
    ("NIST CSF 2.0", "GV.OC", "Organizational Context", "GOVERN", None),
    ("NIST CSF 2.0", "GV.RM", "Risk Management Strategy", "GOVERN", None),
    ("NIST CSF 2.0", "GV.RR", "Roles, Responsibilities, and Authorities", "GOVERN", None),
    ("NIST CSF 2.0", "GV.PO", "Policy", "GOVERN", None),
    ("NIST CSF 2.0", "GV.OV", "Oversight", "GOVERN", None),
    ("NIST CSF 2.0", "GV.SC", "Cybersecurity Supply Chain Risk Management", "GOVERN", None),
    # IDENTIFY
    ("NIST CSF 2.0", "ID.AM", "Asset Management", "IDENTIFY", None),
    ("NIST CSF 2.0", "ID.RA", "Risk Assessment", "IDENTIFY", None),
    ("NIST CSF 2.0", "ID.IM", "Improvement", "IDENTIFY", None),
    # PROTECT
    (
        "NIST CSF 2.0",
        "PR.AA",
        "Identity Management, Authentication, and Access Control",
        "PROTECT",
        None,
    ),
    ("NIST CSF 2.0", "PR.AT", "Awareness and Training", "PROTECT", None),
    ("NIST CSF 2.0", "PR.DS", "Data Security", "PROTECT", None),
    ("NIST CSF 2.0", "PR.PS", "Platform Security", "PROTECT", None),
    ("NIST CSF 2.0", "PR.IR", "Technology Infrastructure Resilience", "PROTECT", None),
    # DETECT
    ("NIST CSF 2.0", "DE.CM", "Continuous Monitoring", "DETECT", None),
    ("NIST CSF 2.0", "DE.AE", "Adverse Event Analysis", "DETECT", None),
    # RESPOND
    ("NIST CSF 2.0", "RS.MA", "Incident Management", "RESPOND", None),
    ("NIST CSF 2.0", "RS.AN", "Incident Analysis", "RESPOND", None),
    ("NIST CSF 2.0", "RS.CO", "Incident Response Reporting and Communication", "RESPOND", None),
    ("NIST CSF 2.0", "RS.MI", "Incident Mitigation", "RESPOND", None),
    # RECOVER
    ("NIST CSF 2.0", "RC.RP", "Incident Recovery Plan Execution", "RECOVER", None),
    ("NIST CSF 2.0", "RC.CO", "Incident Recovery Communication", "RECOVER", None),
]

ALL_CONTROLS = ISO27001_CONTROLS + NIST_CSF_CONTROLS


def get_controls(standard=None):
    if standard is None:
        return ALL_CONTROLS
    return [c for c in ALL_CONTROLS if c[0] == standard]


def seed(db_path, apply=False, dry_run=False, standard=None):
    controls = get_controls(standard)
    print(f"Controls to insert: {len(controls)}")

    if dry_run:
        from collections import Counter

        counts = Counter(c[0] for c in controls)
        for std, n in sorted(counts.items()):
            print(f"  {std}: {n}")
        print("[dry-run] No changes written.")
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executescript(CREATE_TABLE_SQL)

    inserted = 0
    skipped = 0
    for std_code, ctrl_id, ctrl_name, theme, desc in controls:
        try:
            cur.execute(
                "INSERT INTO standard_controls (standard_code, control_id, control_name, theme, description) VALUES (?,?,?,?,?)",
                (std_code, ctrl_id, ctrl_name, theme, desc),
            )
            inserted += 1
        except sqlite3.IntegrityError:
            skipped += 1

    if apply:
        conn.commit()
        print(f"Inserted: {inserted}, Skipped (already exist): {skipped}")
    else:
        conn.rollback()
        print(
            f"[simulation] Would insert: {inserted}, Would skip: {skipped}  (use --apply to write)"
        )

    conn.close()


def main():
    parser = argparse.ArgumentParser(description="Seed standard_controls table")
    parser.add_argument("--db", default=DB_DEFAULT, help="Path to SQLite DB")
    parser.add_argument("--apply", action="store_true", help="Execute INSERT statements")
    parser.add_argument(
        "--dry-run", dest="dry_run", action="store_true", help="Show counts only, no write"
    )
    parser.add_argument("--standard", default=None, help="Seed only one standard (code)")
    args = parser.parse_args()

    seed(args.db, apply=args.apply, dry_run=args.dry_run, standard=args.standard)


if __name__ == "__main__":
    main()
