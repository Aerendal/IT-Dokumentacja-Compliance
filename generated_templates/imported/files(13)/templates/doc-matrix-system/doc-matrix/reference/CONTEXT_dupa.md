---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

#  IT DOCUMENTATION MATRIX - ŚCIĄGA REFERENCYJNA

##  CEL PROJEKTU

Stworzenie kompletnego systemu szablonów dokumentacji dla projektów **Backend/API Development** z:
- Pełnymi szablonami dokumentów
- Mapowaniem relacji między dokumentami
- Cyklem życia dokumentów (kiedy powstają, kiedy znikają)
- Mapowaniem do faz projektu

---

##  STRUKTURA PROJEKTU

```
/home/claude/doc-matrix/
├── db/
│   ├── schema.sql              # Schemat bazy danych
│   ├── data_phases.sql         # 23 fazy projektu
│   ├── data_documents_part1.sql # Dokumenty faz 1-8 (doc_id 1-44)
│   ├── data_documents_part2.sql # Dokumenty faz 9-23 (doc_id 45-132)
│   ├── data_relationships.sql   # Relacje między dokumentami
│   ├── data_phase_mapping.sql   # Mapowanie dokumentów do faz
│   ├── data_lifecycle.sql       # Triggery cyklu życia
│   └── doc_matrix.db           # Baza SQLite (po init)
├── scripts/
│   └── db_manager.py           # Skrypt zarządzający
├── templates/                   # Wygenerowane szablony
├── exports/                     # Eksporty JSON/CSV
└── reference/
    └── CONTEXT.md              # TEN PLIK
```

---

##  23 FAZY PROJEKTU

| # | Kod | Nazwa PL | Opis |
|---|-----|----------|------|
| 1 | CONCEPT | Koncepcja i Wizja | PVS, Problem Statement, Feasibility |
| 2 | REQUIREMENTS | Analiza Wymagań | FRS, NFR, BRD, Use Cases |
| 3 | DESIGN | Projekt / Design | ADR, RFC, TDD, SDD, API Spec, DB Schema |
| 4 | PLANNING | Planowanie | Charter, WBS, Timeline, Risk Register |
| 5 | IMPLEMENTATION | Implementacja | Implementation Plan, Coding Standards |
| 6 | TESTING | Testowanie / QA | Test Strategy, Test Plans, Reports |
| 7 | SECURITY | Bezpieczeństwo | Security Arch, Threat Model, Pentest |
| 8 | DEPLOYMENT | Wdrożenie | Deployment Plan, Release Notes, Go-Live |
| 9 | OPERATIONS | Operacje | Runbook, System Admin Guide, Backup |
| 10 | INCIDENT | Incident Mgmt | IRP, Escalation, Troubleshooting |
| 11 | MONITORING | Monitoring | Monitoring Strategy, Metrics, Alerts |
| 12 | REFERENCE | Dok. Referencyjna | API Reference, Code Docs, Arch Reference |
| 13 | TRAINING | Szkolenie | Dev Onboarding, Training Materials |
| 14 | STAKEHOLDER_COMM | Komunikacja | Status Reports, Changelog, Announcements |
| 15 | KNOWLEDGE | Knowledge Mgmt | ADL, Wiki, FAQ, Glossary, Patterns |
| 16 | RETROSPECTIVE | Retrospektywa | PIR, Project Retro, Lessons Learned |
| 17 | BUDGETING | Budżetowanie | Budget, CBA, TCO, ROI |
| 18 | VENDOR | Vendor Mgmt | RFP, RFI, Vendor Evaluation, Contracts |
| 19 | GOVERNANCE | Governance | Audit Checklist, Compliance, Certification |
| 20 | DECOMMISSION | Decommissioning | Retirement Plan, Data Migration, Archive |
| 21 | DISASTER_RECOVERY | DR / BCP | DRP, BCP, RPO/RTO, Failover |
| 22 | CHANGE_MGMT | Change Mgmt | RFC Form, CAB Notes, Change Calendar |
| 23 | CAPACITY | Capacity Planning | Capacity Forecast, Growth, Scaling |

---

##  KLUCZOWE DOKUMENTY (132 total)

### Faza 1-2: Inicjacja
- **PVS** (1) - Product Vision Statement
- **PROB** (2) - Problem Statement  
- **FEAS** (3) - Feasibility Study
- **FRS** (4) - Functional Requirements (IEEE 830)
- **NFR** (5) - Non-Functional Requirements
- **BRD** (6) - Business Requirements Document
- **UCS** (7) - Use Case Specification

### Faza 3: Design
- **ADR** (8) - Architecture Decision Records (MADR)
- **RFC** (9) - Request for Comments
- **TDD** (10) - Technical Design Document
- **SDD** (11) - System Design Document
- **API_SPEC** (12) - API Specification (OpenAPI 3.x)
- **DB_SCHEMA** (13) - Database Schema Design
- **DFD** (14) - Data Flow Diagram

### Faza 4: Planning
- **CHARTER** (15) - Project Charter
- **WBS** (16) - Work Breakdown Structure
- **TIMELINE** (17) - Project Timeline
- **RAP** (18) - Resource Allocation Plan
- **RISK_REG** (19) - Risk Register
- **CMP** (20) - Change Management Plan

### Faza 5-6: Implementation & Testing
- **IMP_PLAN** (21) - Implementation Plan
- **CAG** (22) - Code Architecture Guideline
- **CSD** (23) - Coding Standards Document
- **TST_STRAT** (26) - Test Strategy
- **TST_PLAN** (27) - Test Plan
- **TST_REPORT** (31) - Test Results Report

### Faza 7-8: Security & Deployment
- **SEC_ARCH** (32) - Security Architecture
- **THREAT** (33) - Threat Model
- **PENTEST** (35) - Penetration Test Report
- **DEP_PLAN** (38) - Deployment Plan
- **REL_NOTES** (39) - Release Notes
- **GOLIVE_CHK** (42) - Go-Live Checklist
- **ROLLBACK** (43) - Rollback Procedure

### Faza 9-11: Operations
- **RUNBOOK** (45) - Runbook
- **INC_RESP** (50) - Incident Response Plan
- **MON_STRAT** (55) - Monitoring Strategy
- **METRICS** (56) - Metrics Definition

### Faza 21-22: DR & Change
- **DRP** (111) - Disaster Recovery Plan
- **BCP** (112) - Business Continuity Plan
- **RFC_FORM** (119) - Change Request Form
- **CAB_NOTES** (120) - CAB Meeting Notes

---

##  TYPY RELACJI MIĘDZY DOKUMENTAMI

| ID | Kod | Opis |
|----|-----|------|
| 1 | DEPENDS_ON | Dokument wymaga istnienia innego |
| 2 | PRODUCES | Dokument jest wynikiem innego |
| 3 | REFERENCES | Odwołuje się do innego |
| 4 | SUPERSEDES | Zastępuje inny dokument |
| 5 | VALIDATES | Służy do walidacji innego |
| 6 | IMPLEMENTS | Jest implementacją wymagań |
| 7 | EXTENDS | Rozszerza/uzupełnia inny |
| 10 | TRIGGERS | Wyzwala potrzebę utworzenia |

---

##  TRIGGERY CYKLU ŻYCIA

| Trigger | Opis |
|---------|------|
| `CREATED_WHEN` | Kiedy dokument powstaje |
| `VALID_FROM` | Od kiedy obowiązuje |
| `VALID_UNTIL` | Do kiedy obowiązuje |
| `DEPRECATED_WHEN` | Kiedy staje się przestarzały |
| `SUPERSEDED_BY` | Czym jest zastępowany |
| `ARCHIVED_WHEN` | Kiedy archiwizowany |
| `REVIEW_REQUIRED` | Kiedy wymaga przeglądu |
| `UPDATE_REQUIRED` | Kiedy wymaga aktualizacji |

---

##  STANDARDY ZASTOSOWANE

| Standard | Wersja | Zastosowanie |
|----------|--------|--------------|
| IEEE 830 / ISO 29148 | 2018 | FRS, NFR, BRD |
| MADR | 3.0 | Architecture Decision Records |
| ITIL 4 | 4.0 | Incident, Change, Operations |
| OpenAPI | 3.1 | API Specification |
| ISO 22301 | 2019 | BCP, DRP |
| TOGAF | 10 | Architecture Documentation |
| ISO 27001 | 2022 | Security Documentation |
| NIST CSF | 2.0 | Security Framework |
| PMBOK | 7 | Project Management |

---

##  UŻYCIE SYSTEMU

### Inicjalizacja bazy danych
```bash
cd /home/claude/doc-matrix/scripts
python db_manager.py init
```

### Lista wszystkich dokumentów
```bash
python db_manager.py list
```

### Generowanie szablonu
```bash
python db_manager.py template ADR
python db_manager.py template FRS
python db_manager.py template DRP
```

### Eksport do JSON
```bash
python db_manager.py export
```

### Raport podsumowujący
```bash
python db_manager.py report
```

### Zapytania SQL
```bash
python db_manager.py query "SELECT * FROM phases"
python db_manager.py query "SELECT * FROM v_documents_full WHERE phase_number = 3"
python db_manager.py query "SELECT * FROM v_document_dependencies WHERE source_doc = 'FRS'"
```

---

##  WIDOKI SQL (gotowe do użycia)

| Widok | Opis |
|-------|------|
| `v_documents_full` | Dokumenty z kategoriami i fazami |
| `v_document_phase_matrix` | Macierz dokumenty × fazy |
| `v_document_dependencies` | Graf zależności dokumentów |
| `v_document_raci` | RACI dla dokumentów |
| `v_document_lifecycle` | Cykl życia dokumentów |

---

##  NASTĘPNE KROKI

1. **[DONE]** Schemat bazy danych
2. **[DONE]** Dane o fazach (23)
3. **[DONE]** Dane o dokumentach (132)
4. **[DONE]** Relacje między dokumentami (111)
5. **[DONE]** Mapowanie do faz (87)
6. **[DONE]** Cykl życia dokumentów (109)
7. **[DONE]** Skrypt zarządzający
8. **[DONE]** Sekcje wewnątrz dokumentów (65 - dla ADR, FRS, NFR, TDD, DRP, RUNBOOK)
9. **[TODO]** RACI dla każdego dokumentu
10. **[TODO]** Więcej sekcji dla pozostałych dokumentów
11. **[TODO]** Generator szablonów DOCX

---

##  NOTATKI

- Baza zawiera 132 typy dokumentów
- Każdy dokument ma przypisaną fazę główną
- Dokumenty mogą być wymagane w wielu fazach
- Relacje określają zależności i przepływ informacji
- Cykl życia określa triggery dla statusów dokumentu

---

*Ostatnia aktualizacja: 2026-01-30*
