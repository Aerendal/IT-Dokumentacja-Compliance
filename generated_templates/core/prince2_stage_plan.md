---
title: PRINCE2 Stage Plan
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-03-09
aligned_by: codex
---

# PRINCE2 Stage Plan

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Zdefiniować szczegółowy plan dla bieżącego etapu zarządzania projektem PRINCE2. Stage Plan jest kluczowym artefaktem PRINCE2 (komponent „Plans") i opisuje: produkty do dostarczenia w etapie, działania i zasoby, harmonogram, budżet etapu, kontrole jakości, ryzyka i tolerancje. Jest podstawą autoryzacji etapu przez Project Board (proces Authorising a Stage or Exception Plan, SB).

## Zakres i granice
- Obejmuje: opis etapu i jego kontekstu w projekcie, listę produktów etapu (Product Descriptions), plan działań i harmonogram (Gantt/checkpoints), zasoby i budżet etapu, tolerancje (zakres/czas/koszt/jakość/ryzyko/korzyści), plan jakości etapu, rejestr ryzyk etapu, punkty kontrolne (Checkpoint Reports), kryteria akceptacji etapu.
- Poza zakresem: Project Plan (poziom projektu) — Stage Plan jest bardziej szczegółowy i obejmuje tylko bieżący etap.

## Wejścia i wyjścia
- Wejścia: Project Plan (wyższy poziom), Project Initiation Documentation (PID), rejestr ryzyk projektu, rejestr zagadnień, doświadczenia z poprzednich etapów (Lessons Log), Product Descriptions produktów etapu.
- Wyjścia: Stage Plan (autoryzowany przez Project Board), zaktualizowany Project Plan, zaktualizowane rejestry ryzyk i zagadnień, plan komunikacji etapu, harmonogram Checkpoint Reports.

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- Project Initiation Documentation (PID) — Stage Plan musi być zgodny z PID.
- Project Plan — Stage Plan jest dekompozycją Project Plan dla danego etapu.
- Risk Register — ryzyka etapu są podzestawem ryzyk projektu.
- Product Descriptions — każdy produkt etapu musi mieć Product Description.

## Struktura Stage Plan

### 1. Kontekst etapu
- Numer i nazwa etapu
- Daty: start — koniec
- Cel etapu w kontekście projektu

### 2. Produkty etapu
| ID Produktu | Nazwa | Opis | Jakość | Odpowiedzialny |
|-------------|-------|------|--------|----------------|
| P-XX-01 | [Nazwa] | [Opis] | [Kryteria] | [Owner] |

### 3. Plan działań i zasoby
- Harmonogram kluczowych działań
- Przypisanie zasobów (Role → Osoba → Dostępność %)
- Budżet etapu: [kwota] ± tolerancja [%]

### 4. Tolerancje etapu
| Wymiar | Tolerancja dolna | Tolerancja górna |
|--------|-----------------|-----------------|
| Czas | -X dni | +Y dni |
| Koszt | -X% | +Y% |
| Zakres | [opis] | [opis] |

### 5. Plan jakości etapu
- Metody przeglądu i testowania per produkt
- Harmonogram Quality Reviews

### 6. Ryzyka etapu
Odniesienie do Risk Register — podzbiór ryzyk aktywnych w tym etapie.

### 7. Plan raportowania
- Checkpoint Reports: co [X] tygodni do [osoba]
- Highlight Reports: co [X] tygodni do Project Board
