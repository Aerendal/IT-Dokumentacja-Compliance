---
title: "Scope Baseline (WBS + WBS Dict + Scope Stmt)"
status: aktywny
aligned: PMBOK 7
---

# Scope Baseline (WBS + WBS Dict + Scope Stmt)

## Cel dokumentu
Ustanowić Scope Baseline projektu — zatwierdzony punkt odniesienia dla zakresu, składający się z trzech obowiązkowych komponentów PMBOK 7: (1) Project Scope Statement — szczegółowy opis zakresu projektu, (2) Work Breakdown Structure (WBS) — hierarchiczna dekompozycja pracy na deliverables i pakiety robocze, (3) WBS Dictionary — słownik definiujący każdy element WBS. Scope Baseline jest składową Performance Measurement Baseline i umożliwia kontrolę zakresu (Scope Control), zarządzanie zmianami przez Integrated Change Control i podstawę dla Earned Value Management.

## Zakres i granice
Scope Baseline jest zatwierdzany na etapie Planning Process Group i może być zmieniony wyłącznie przez formalny wniosek o zmianę (Change Request) zatwierdzony przez Project Sponsor lub Change Control Board.

## Wejścia i wyjścia
**Wejścia:**
- Project Charter (zatwierdzone cele i high-level scope)
- Requirements Documentation i Requirements Traceability Matrix
- Enterprise Environmental Factors (standardy branżowe, rynkowe)
- Organizational Process Assets (szablony WBS, historical data)

**Wyjścia:**
- Project Scope Statement (zatwierdzone)
- WBS (Work Breakdown Structure)
- WBS Dictionary
- Scope Baseline jako komponent Project Management Plan

## 1. Project Scope Statement

### Opis zakresu projektu (Project Scope Description)
[Szczegółowy opis produktów, usług lub wyników które zostaną dostarczone przez projekt.]

### Deliverables projektu
| # | Deliverable | Opis | Kryterium akceptacji |
|---|------------|------|---------------------|
| 1 | [Deliverable A] | [Opis] | [Mierzalne kryterium] |
| 2 | [Deliverable B] | [Opis] | [Mierzalne kryterium] |

### Co jest POZA zakresem (Exclusions)
- [Explicite wykluczenie 1]
- [Explicite wykluczenie 2]

### Ograniczenia i założenia
**Ograniczenia (Constraints):** [np. budżet max X, termin nieprzekraczalny, regulacyjny]
**Założenia (Assumptions):** [co przyjmujemy za prawdziwe bez pełnej weryfikacji]

### Kryteria akceptacji projektu
[Mierzalne warunki które muszą być spełnione aby Sponsor zaakceptował produkt końcowy.]

## 2. Work Breakdown Structure (WBS)

```
[Nazwa projektu]
├── 1.0 Project Management
│   ├── 1.1 Initiation
│   ├── 1.2 Planning
│   ├── 1.3 Monitoring & Controlling
│   └── 1.4 Closing
├── 2.0 [Faza/Komponent 1]
│   ├── 2.1 [Work Package A]
│   ├── 2.2 [Work Package B]
│   └── 2.3 [Work Package C]
├── 3.0 [Faza/Komponent 2]
│   ├── 3.1 [Work Package D]
│   └── 3.2 [Work Package E]
└── 4.0 [Deliverable końcowy]
    ├── 4.1 [Work Package F]
    └── 4.2 [Work Package G]
```

**Zasada 100%:** WBS musi obejmować 100% pracy niezbędnej do dostarczenia produktu projektu — nic więcej, nic mniej.

## 3. WBS Dictionary

| WBS ID | Nazwa elementu | Opis pracy | Właściciel | Szacunek (h/PLN) | Zależności |
|--------|---------------|-----------|----------|-----------------|-----------|
| 2.1 | [Work Package A] | [Co jest do zrobienia, jak, przez kogo] | [Team/Osoba] | [X h / Y PLN] | [Poprzednicy] |
| 2.2 | [Work Package B] | [Opis] | [Team] | [X h] | [2.1] |
| 3.1 | [Work Package D] | [Opis] | [Team] | [X h] | [2.3] |

### Szablon wpisu WBS Dictionary

**WBS ID:** [np. 2.1]  
**Nazwa:** [Work Package Name]  
**Opis:** [Szczegółowy opis pracy do wykonania]  
**Właściciel:** [Responsible Team/Person]  
**Deliverables:** [Co zostanie wytworzone]  
**Milestones:** [Kluczowe punkty kontrolne]  
**Zasoby:** [Ludzie, sprzęt, materiały]  
**Szacunek kosztów:** [PLN]  
**Szacunek czasu:** [godziny/dni]  
**Poprzednicy:** [WBS IDs]  
**Kryteria akceptacji:** [Mierzalne warunki ukończenia]  
**Assumptions:** [Założenia specyficzne dla tego WP]  
**Constraints:** [Ograniczenia specyficzne]

## Historia zatwierdzeń Scope Baseline
| Wersja | Data | Zmiana | Zatwierdził | Change Request # |
|--------|------|--------|-------------|-----------------|
| 1.0 | [Data] | Baseline inicjalny | [Sponsor] | — |
| 1.1 | [Data] | [Opis zmiany zakresu] | [CCB] | [CR-001] |

## Powiązania (meta)
- standardy-i-compliance: PMBOK 7 (Performance Domain: Planning), PMBOK 6 sekcja 5.4 (Create WBS), PMI Practice Standard for Work Breakdown Structures
- raci-i-role: Project Sponsor (Approver), Project Manager (Owner), Team Leads (Consulted), CCB (Scope Changes)
