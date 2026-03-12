---
title: IT Contingency Plan
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-03-09
aligned_by: codex
---

# IT Contingency Plan

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Opisać plan awaryjny systemu IT zgodny z NIST SP 800-53 kontrolką CP-2 (Contingency Plan). Plan określa: cele odtworzeniowe (RTO/RPO), role i odpowiedzialności w sytuacji awaryjnej, procedury aktywacji, procedury odtworzenia systemu do stanu operacyjnego, kolejność przywracania usług, procedury testowania planu oraz plan szkoleń. Dokument jest wymagany przez NIST SP 800-53 dla systemów federalnych i stanowi podstawę autoryzacji (ATO).

## Zakres i granice
- Obejmuje: identyfikację systemu i interfejsów, analizę wpływu (BIA), cele RTO i RPO, role i kontakty awaryjne, procedury aktywacji planu, procedury dla etapów: Notification/Activation → Recovery → Reconstitution, lokalizacje zapasowe (cold/warm/hot site), dane kontaktowe dostawców, harmonogram testów i szkoleń, procedurę aktualizacji planu.
- Poza zakresem: Plan Ciągłości Działania organizacji (BCP) — Contingency Plan dotyczy konkretnego systemu IT; ogólna polityka bezpieczeństwa.

## Wejścia i wyjścia
- Wejścia: System Security Plan (SSP), Business Impact Analysis (BIA), architektura systemu, inwentaryzacja zasobów, umowy SLA z dostawcami, dane o lokalizacjach zapasowych, wyniki poprzednich testów planu.
- Wyjścia: zatwierdzony Contingency Plan, wyniki testów (Test Report), zaktualizowane procedury po każdym teście/incydencie, metryki RTO/RPO z testów.

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- System Security Plan (SSP) — Contingency Plan jest powiązany z SSP (NIST CP-2).
- Business Impact Analysis (BIA) — cele RTO/RPO wynikają z BIA.
- Incident Response Plan — aktywacja Contingency Plan często następuje po Incident Response.
- Disaster Recovery Plan (DRP) — DRP może być częścią lub uzupełnieniem Contingency Plan.

## Struktura planu

### 1. Identyfikacja systemu
- Nazwa systemu i właściciel
- Klasyfikacja systemu (High/Moderate/Low impact wg FIPS 199)
- Kluczowe interfejsy i zależności

### 2. Cel i zakres
- Cele odtworzeniowe (RTO: [X godz.] / RPO: [Y godz.])
- Zdarzenia wyzwalające aktywację planu

### 3. Role i odpowiedzialności
| Rola | Imię/Kontakt | Obowiązki |
|------|-------------|-----------|
| Contingency Plan Coordinator | | Koordynacja całego procesu |
| System Owner | | Decyzja o aktywacji |
| IT Recovery Team | | Odtworzenie infrastruktury |
| Communications Lead | | Komunikacja z interesariuszami |

### 4. Faza 1 — Notification/Activation
- Kryteria aktywacji
- Procedura powiadomień (kontakty, kolejność)
- Ocena szkód

### 5. Faza 2 — Recovery
- Procedury odtworzenia (krok po kroku)
- Lokalizacja zapasowa: [adres/cloud]
- Odtworzenie danych z backupu

### 6. Faza 3 — Reconstitution
- Weryfikacja systemu przed powrotem do produkcji
- Procedura powrotu z lokalizacji zapasowej
- Deaktywacja planu awaryjnego

### 7. Testowanie planu
- Harmonogram testów: [częstotliwość]
- Typy testów: tabletop / functional / full interruption
- Wymagania NIST CP-4: test min. raz w roku

### 8. Szkolenia i utrzymanie
- Szkolenia zespołu: [harmonogram]
- Przegląd i aktualizacja planu: [min. raz w roku lub po zmianie systemu]
