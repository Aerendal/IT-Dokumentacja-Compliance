---
title: SAFe PI Planning Inputs
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-03-09
aligned_by: codex
---

# PI Planning Inputs (Vision, Backlog)

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Zebrać i przygotować wszystkie materiały wejściowe do Planowania Przyrostu Programu (PI Planning) w ramach SAFe 6.0. PI Planning to kluczowe wydarzenie SAFe (cadence-based, face-to-face lub online) dla całego Agile Release Train (ART), podczas którego zespoły planują pracę na nadchodzący PI (typowo 8–12 tygodni). Dokument konsoliduje: wizję produktu/programu, aktualną mapę drogową, backlog programowy (Program Backlog), architektoniczne Enablery i ograniczenia systemowe — aby wszystkie zespoły ART mogły zaplanować iteracje ze wspólnym kontekstem.

## Zakres i granice
- Obejmuje: wizję rozwiązania/programu (Solution Vision, Program Vision), mapę drogową na aktualny i kolejny PI, Program Backlog (posortowane Features), architektoniczne Enablery i runway, ograniczenia systemowe i zależności znane z góry, metryki z poprzedniego PI (velocity, predictability), dostępność zasobów na nadchodzący PI, agendy i logistykę PI Planning.
- Poza zakresem: szczegółowe plany iteracji poszczególnych zespołów (wyjście z PI Planning, nie wejście), PI Objectives (wyjście z PI Planning), System Demo (oddzielne wydarzenie).

## Wejścia i wyjścia
- Wejścia: Solution Backlog, Portfolio Kanban (Epics), metryki ART z poprzedniego PI, wyniki Inspect & Adapt (I&A), aktualny stan architectural runway, informacje o dostępności zespołów, priorytety od Product Management i Business Owners.
- Wyjścia: prezentacja PI Planning (briefing dla wszystkich uczestników), zaplanowane iteracje per zespół, PI Objectives per zespół i ART, zidentyfikowane ryzyka i plany mitygacji, zależności między zespołami i ART, Rozbite Features na Stories w backlogach iteracji.

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- Program Vision — nadaje kontekst i kierunek dla PI Planning.
- Program Backlog — Features do zaplanowania w PI.
- Architectural Runway Documentation — określa dostępność infrastruktury architektonicznej.
- Inspect and Adapt Report — wnioski z poprzedniego PI jako wejście.
- PI Objectives (wyjście) — wynik PI Planning, nie wejście.

## Struktura dokumentu wejściowego PI Planning

### 1. Kontekst PI
- Numer PI: PI-[N]
- Daty: [Start] — [Koniec]
- Liczba iteracji: [np. 4 × 2 tygodnie + 1 IP sprint]
- ART i uczestniczące zespoły

### 2. Wizja programu
- Solution/Product Vision (skrót — pełny dok. osobno)
- Kluczowe inicjatywy strategiczne na ten PI
- Top 3-5 priorytetów biznesowych

### 3. Mapa drogowa — aktualny PI
| Feature ID | Nazwa Feature | Priorytet | Przypisany zespół | Szacunek (SP) |
|-----------|--------------|-----------|------------------|--------------|
| F-XXX | [Nazwa] | [1–10] | [Zespół] | [SP] |

### 4. Architectural Enablers
- Lista Enablerów wymaganych w tym PI
- Status architectural runway (wystarczający / niewystarczający)
- Planowane prace architektoniczne

### 5. Znane ograniczenia i zależności
| Ograniczenie / Zależność | Wpływ | Właściciel |
|--------------------------|-------|-----------|
| [Opis] | [Jakie zespoły dotknięte] | [Osoba] |

### 6. Metryki z poprzedniego PI
- Velocity ART: [SP/iterację średnio]
- Predictability (PI Objectives met): [%]
- Kluczowe wnioski z I&A

### 7. Dostępność zasobów
- Dni robocze w PI: [N]
- Planowane urlopy i święta
- Dostępność per zespół: [%]

### 8. Logistyka PI Planning
- Format: face-to-face / remote / hybrid
- Agenda: [link do agendy]
- Narzędzia: Jira / Miro / AgilePM / itp.
