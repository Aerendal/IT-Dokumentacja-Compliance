---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# IT Documentation Matrix — Część 2
## CONTEXT.md — Przewodnik systemu

---

### Zakres
Branże **10–18** (9 branż), **23 fazy** cyklu życia, **1074 dokumenty**.

### Branże
| ID | Код | Nazwa |
|----|-----|-------|
| 10 | QA | Quality Assurance / Testing |
| 11 | SYSADM | System Administration |
| 12 | NET | Network Engineering |
| 13 | DBA | Database Administration / Engineering |
| 14 | GAME | Game Development |
| 15 | EMBED | Embedded Systems |
| 16 | SRE | Site Reliability Engineering |
| 17 | SOLARCH | Solutions Architecture |
| 18 | ENTARCH | Enterprise Architecture |

### Fazy (23)
**PLANNING** (1–4): Koncepcja → Analiza Wymagań → Design → Planowanie  
**EXECUTION** (5–8): Implementacja → Testing → Security → Deployment  
**OPERATIONS** (9–16): Operacje → Incident Mgmt → Monitoring → Dokumentacja Ref → Szkolenie → Komunikacja → Knowledge Mgmt → Postmortem  
**GOVERNANCE** (17–23): Budżet → Vendor → Governance → Decommission → DR/BCP → Change Mgmt → Capacity Planning

> Fazy 17–23 są **wspólne** dla wszystkich branż (is_common=1).

---

### Struktura bazy danych

| Tabela | Zawartość | Wiersze |
|--------|-----------|---------|
| `industries` | 9 branż | 9 |
| `phases` | 23 fazy | 23 |
| `documents` | Wszystkie dokumenty | 1074 |
| `document_dependencies` | Zależności między dokumentami | 528 |
| `document_lifecycle` | CREATE/UPDATE/REFERENCE/ARCHIVE per faza | 2179 |
| `document_sections` | Sekcje wewnątrz dokumentów | 1870 |
| `document_roles` | RACI mapowanie | 2822 |
| `document_standards` | Mapowanie do standardów | 342 |
| `roles` | 18 roli | 18 |
| `standards` | 14 standardów | 14 |

---

### Typy dokumentów (doc_type)
`STRATEGY` | `PLAN` | `SPEC` | `DESIGN` | `REPORT` | `PROCEDURE` | `GUIDE` | `REFERENCE` | `TEMPLATE` | `POLICY` | `ANALYSIS`

### Lifecycle States
- **CREATE** — dokument powstaje w tej fazie (priority=1=primary)
- **UPDATE** — dokument jest aktualizowany
- **REFERENCE** — dokument jest odwoływany/pady
- **ARCHIVE** — dokument wygasa

### Dependency Types
- **REQUIRES** — dokument wymaga istnienia innego
- **INFORMED_BY** — bazuje na danych z innego dokumentu
- **UPDATES** — aktualizuje inny dokument
- **REPLACES** — zastępuje inny dokument
- **REFERENCES** — odwołuje się do innego dokumentu

---

### Standardy zastosowane
| Std | Branża/Typ | Zastosowanie |
|-----|-----------|--------------|
| IEEE 829 | QA (10) | Test Plan, Test Case, Test Strategy (16 sekcji per IEEE 829) |
| IEEE 830 | EMBED (15) | SRS — Software Requirements Specification |
| ITIL 4 | SYSADM (11), SRE (16) | Runbook (10 sekcji), Incident Response |
| TOGAF | SOLARCH (17), ENTARCH (18) | Solution & Enterprise Architecture (10 sekcji) |
| ISO 22301 | Wspólne | Disaster Recovery Plan (10 sekcji) |
| IEC 61508 | EMBED (15) | Safety Analysis (8 sekcji) |
| MISRA C | EMBED (15) | Embedded coding standards |
| SRE Book | SRE (16) | SLO Document (8 sekcji) |
| OWASP | Bezpieczeństwo | Security testing |

---

### Użycie skriptów

```bash
# Podsumowanie branż
python3 scripts/db_manager.py industry_summary

# Lista dokumentów dla branży QA
python3 scripts/db_manager.py list_docs --industry 10

# Szczegóły dokumentu (sekcje, lifecycle, zależności, RACI)
python3 scripts/db_manager.py doc_detail --doc_id 9

# Drzewo zależności
python3 scripts/db_manager.py dependencies --doc_id 9

# Wyszukiwanie
python3 scripts/db_manager.py search --query "runbook"

# Podsumowanie fazy
python3 scripts/db_manager.py phase_summary --phase 3

# RACI matrix dla branży
python3 scripts/db_manager.py raci --industry 16

# Raport standardów
python3 scripts/db_manager.py standards_report

# Export do CSV
python3 scripts/db_manager.py export_csv --industry 13
```

---

### Pliki systemu
```
doc-matrix-part2/
├── db/
│   ├── schema.sql                  — Schemat SQLite
│   └── it_doc_matrix_part2.db      — Baza danych (SQLite)
├── scripts/
│   ├── populate_db.py              — Populacja bazy (source of truth)
│   └── db_manager.py               — CLI tool do query/raportowania
├── reference/
│   └── CONTEXT.md                  — Ten plik
└── extracted_part2.json            — Surowe dane z ekstrakcji
```
