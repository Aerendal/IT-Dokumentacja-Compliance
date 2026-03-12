---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Frontend/Web Development - Documentation Matrix
## ŚCIĄGA PROJEKTU - Pełny Kontekst

**Branża:** Frontend/Web Development  
**Wersja:** 1.0  
**Data:** 2026-01-30

---

##  STATYSTYKI

| Metryka | Wartość |
|---------|---------|
| Fazy projektu | 23 |
| Typy dokumentów | 117 |
| Relacje między dokumentami | 72 |
| Mapowania do faz | 111 |
| Triggery cyklu życia | 113 |

---

##  STRUKTURA PROJEKTU

```
frontend-doc-matrix/
├── db/
│   ├── schema.sql              # Schemat bazy danych
│   ├── data_phases.sql         # 23 fazy projektu
│   ├── data_documents_part1.sql # Dokumenty faz 1-12
│   ├── data_documents_part2.sql # Dokumenty faz 13-23
│   ├── data_relationships.sql   # Relacje między dokumentami
│   ├── data_phase_mapping.sql   # Mapowanie dok→faz
│   ├── data_lifecycle.sql       # Cykl życia dokumentów
│   └── doc_matrix.db           # Baza SQLite
├── scripts/
│   └── db_manager.py           # Skrypt zarządzający
├── templates/                   # Wygenerowane szablony
├── exports/                     # Eksporty JSON
└── reference/
    ├── CONTEXT.md              # Ten plik
    └── REPORT.md               # Wygenerowany raport
```

---

##  23 FAZ PROJEKTU FRONTEND

| # | Kod | Nazwa | Liczba dok. |
|---|-----|-------|-------------|
| 1 | CONCEPT | Koncepcja i Wizja | 3 |
| 2 | REQUIREMENTS | Analiza Wymagań | 5 |
| 3 | DESIGN | Projekt / Design | 7 |
| 4 | PLANNING | Planowanie | 4 |
| 5 | IMPLEMENTATION | Implementacja | 6 |
| 6 | TESTING | Testowanie / QA | 6 |
| 7 | SECURITY | Bezpieczeństwo | 4 |
| 8 | DEPLOYMENT | Wdrożenie | 4 |
| 9 | OPERATIONS | Operacje | 4 |
| 10 | INCIDENT | Incident Management | 3 |
| 11 | MONITORING | Monitoring | 3 |
| 12 | REFERENCE | Dokumentacja Ref. | 4 |
| 13 | TRAINING | Szkolenie/Onboarding | 4 |
| 14 | STAKEHOLDER_COMM | Komunikacja | 4 |
| 15 | KNOWLEDGE | Knowledge Management | 4 |
| 16 | RETROSPECTIVE | Retrospektywa | 3 |
| 17 | BUDGETING | Budżetowanie | 6 |
| 18 | VENDOR | Vendor Management | 7 |
| 19 | GOVERNANCE | Governance | 7 |
| 20 | DECOMMISSION | Decommissioning | 7 |
| 21 | DISASTER_RECOVERY | DR/BCP | 8 |
| 22 | CHANGE_MGMT | Change Management | 7 |
| 23 | CAPACITY | Capacity Planning | 7 |

---

##  KLUCZOWE DOKUMENTY WEDŁUG FAZ

### Faza 1-3: Koncepcja → Design
- **PVS** - Product Vision Statement
- **URS** - User Research Summary
- **USD** - User Stories Document
- **FRS** - Functional Requirements
- **NFR** - Non-Functional Requirements
- **UIUX** - UI/UX Design Document
- **DSL** - Design System / Component Library
- **A11Y** - Accessibility Design Guide

### Faza 4-5: Planowanie → Implementacja
- **SPD** - Sprint Planning Document
- **BSM** - Browser/Device Support Matrix
- **FAD** - Frontend Architecture Document
- **CMP** - Component Specification
- **SMD** - State Management Design
- **CSS** - CSS/Styling Guidelines

### Faza 6-8: Testowanie → Deployment
- **UTS** - UI Test Strategy
- **VRT** - Visual Regression Test Spec
- **ATC** - Accessibility Testing Checklist
- **SEC** - Frontend Security Checklist
- **BDG** - Build and Deployment Guide
- **PBL** - Performance Baseline

### Faza 9-12: Operacje → Dokumentacja
- **MON** - Frontend Monitoring Guide
- **ABT** - A/B Testing Guide
- **IRP** - Incident Response for Frontend
- **MDF** - Frontend Metrics Definition (CWV)
- **CLD** - Component Library Documentation (Storybook)

---

##  KLUCZOWE ZALEŻNOŚCI DOKUMENTÓW

### Przepływ: Wymagania → Design
```
User Research (URS)
    ↓
User Stories (USD) → User Journey (UJM) → Wireframes (WFS)
    ↓                                         ↓
Functional Req (FRS)                    UI/UX Design (UIUX)
    ↓                                         ↓
NFR ─────────────────────────────→ Design System (DSL)
```

### Przepływ: Design → Implementacja
```
UI/UX Design (UIUX)
    ↓
Frontend Architecture (FAD)
    ↓
Component Specification (CMP) ←── Design System (DSL)
    ↓
State Management (SMD) + API Integration (API)
    ↓
Component Library Docs (CLD)
```

### Przepływ: A11Y przez cały projekt
```
NFR (a11y requirements)
    ↓
A11Y Design Guide (A11Y)
    ↓
Component Spec (CMP) [a11y considerations]
    ↓
A11Y Testing Checklist (ATC)
    ↓
Accessibility Guidelines (AGL) [team knowledge]
```

---

##  TRIGGERY CYKLU ŻYCIA - PRZYKŁADY

| Dokument | Trigger | Warunek | Rezultat |
|----------|---------|---------|----------|
| DSL | CREATED_WHEN | ui_design_started | Na starcie designu |
| DSL | UPDATE_REQUIRED | new_component_added | Przy nowym komponencie |
| DSL | REVIEW_REQUIRED | monthly | Przegląd miesięczny |
| CMP | CREATED_WHEN | design_system_created | Po design system |
| CMP | UPDATE_REQUIRED | component_api_changed | Przy zmianie API |
| PBL | CREATED_WHEN | first_deployment | Po pierwszym deploy |
| PBL | REVIEW_REQUIRED | monthly | Przegląd miesięczny |
| VRT | UPDATE_REQUIRED | visual_change | Przy zmianie wizualnej |

---

##  UŻYCIE SKRYPTU

```bash
# Inicjalizacja bazy
python db_manager.py init

# Lista dokumentów
python db_manager.py list

# Generowanie szablonu
python db_manager.py template DSL
python db_manager.py template UIUX
python db_manager.py template CMP

# Eksport do JSON
python db_manager.py export

# Raport podsumowujący
python db_manager.py report

# Zapytanie SQL
python db_manager.py query "SELECT * FROM v_documents_full WHERE phase_number = 3"
```

---

##  STANDARDY DOKUMENTACJI

| Standard | Zastosowanie |
|----------|--------------|
| WCAG 2.1/2.2 | Dostępność (A11Y) |
| Core Web Vitals | Metryki wydajności (LCP, INP, CLS) |
| OWASP Top 10 | Bezpieczeństwo frontend |
| GDPR | Ochrona danych, cookies |
| Atomic Design | Struktura design system |
| BEM | Metodologia CSS |
| WAI-ARIA | Dostępność interaktywna |

---

##  ROLE W PROJEKCIE (RACI)

| Rola | Główne dokumenty |
|------|------------------|
| UI Designer | UIUX, DSL, BRG, IDS |
| UX Designer | URS, UJM, A11Y, IAD |
| Frontend Developer | FAD, CMP, SMD, CSS, JSG |
| Frontend Lead | FAD, CMP, DDL |
| QA Engineer | UTS, VRT, ATC, CBT |
| A11Y Specialist | A11Y, ATC, AGL |
| DevOps | BDG, MON, DRP |
| Product Owner | PVS, USD, RMP |

---

##  NASTĘPNE KROKI

1. **[DONE]** Schemat bazy danych
2. **[DONE]** Dane o fazach (23)
3. **[DONE]** Dane o dokumentach (117)
4. **[DONE]** Relacje między dokumentami (72)
5. **[DONE]** Mapowanie do faz (111)
6. **[DONE]** Cykl życia dokumentów (113)
7. **[DONE]** Skrypt zarządzający
8. **[TODO]** Sekcje wewnątrz dokumentów (DSL, CMP, FAD, A11Y)
9. **[TODO]** RACI dla każdego dokumentu
10. **[TODO]** Generator szablonów DOCX

---

##  WIDOKI SQL

```sql
-- Wszystkie dokumenty z fazami
SELECT * FROM v_documents_full;

-- Macierz dokumenty × fazy
SELECT * FROM v_document_phase_matrix;

-- Graf zależności
SELECT * FROM v_document_dependencies;

-- Cykl życia
SELECT * FROM v_document_lifecycle;

-- Dokumenty design
SELECT * FROM v_documents_full WHERE category_code = 'DESIGN';

-- Dokumenty obowiązkowe w fazie 3
SELECT * FROM v_document_phase_matrix 
WHERE phase_number = 3 AND requirement_level = 'MANDATORY';
```

---

*Wygenerowano automatycznie przez IT Documentation Matrix System*
