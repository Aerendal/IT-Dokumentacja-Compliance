---
title: ICT Third-Party Provider Register
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-03-09
aligned_by: codex
---

# ICT Third-Party Provider Register

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Prowadzić Rejestr Dostawców Usług ICT wymagany przez Art. 28 DORA (Digital Operational Resilience Act). Rejestr ewidencjonuje wszystkich zewnętrznych dostawców usług ICT wspierających funkcje krytyczne lub istotne instytucji finansowej, ze szczegółami dotyczącymi umów, ryzyk, koncentracji i nadzoru. Jest podstawą do raportowania do właściwego organu nadzoru finansowego (EBA/ESMA/EIOPA).

## Zakres i granice
- Obejmuje: pełną listę dostawców ICT (krytycznych i nieistotnych), nazwy i dane kontaktowe, opis świadczonych usług ICT, klasyfikacja (krytyczny/istotny/inny), opis funkcji wspieranych, lokalizacje przetwarzania danych, ocena ryzyka koncentracji (Art. 29 DORA), status umów i daty przeglądu, wyniki ocen dostawców, plany wyjścia (exit plans).
- Poza zakresem: treść umów kontraktowych (oddzielny dokument), szczegółowe oceny TLPT dostawców.

## Wejścia i wyjścia
- Wejścia: rejestr umów z dostawcami ICT, oceny ryzyka ICT, klasyfikacja funkcji krytycznych/istotnych, wyniki due diligence dostawców, raporty z audytów dostawców.
- Wyjścia: kompletny rejestr dostawców ICT (Art. 28 ust. 3 DORA), raport dla organu nadzoru, wkład do oceny ryzyka koncentracji, lista dostawców ICT "critical third-party providers" (CTPPs).

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- ICT Risk Management Framework (DORA Art. 6) — rejestr jest częścią frameworku.
- Contractual Arrangements with ICT Providers (DORA Art. 30) — każdy dostawca w rejestrze musi mieć umowę.
- ICT Incident Report — incydenty przypisuje się do dostawców z rejestru.
- Business Impact Analysis — krytyczność funkcji z BIA wpływa na klasyfikację dostawcy.

## Struktura rejestru (Art. 28 DORA)

### Dane per dostawca

| Pole | Opis |
|------|------|
| ID dostawcy | Unikalny identyfikator |
| Nazwa dostawcy | Pełna nazwa prawna |
| Kraj siedziby | |
| Opis usług ICT | Co dokładnie dostarcza |
| Typ usługi | Cloud / SaaS / On-prem / Outsourcing |
| Krytyczność | Krytyczna / Istotna / Inna |
| Wspierana funkcja | Opis funkcji biznesowej |
| Lokalizacja danych | Kraj przetwarzania i przechowywania |
| Data zawarcia umowy | |
| Data wygaśnięcia umowy | |
| Data ostatniego przeglądu | |
| Status exit plan | Istnieje / W trakcie / Brak |
| Ocena ryzyka | Niskie / Średnie / Wysokie |
| Uwagi | |

### Ocena ryzyka koncentracji (Art. 29 DORA)
- Zidentyfikowane punkty koncentracji (single points of failure)
- Alternatywni dostawcy lub strategie wyjścia
- Poziom uzależnienia organizacji od każdego CTP

### Przegląd i aktualizacja
- Przegląd rejestru: min. raz w roku lub przy każdej zmianie dostawcy
- Odpowiedzialny: [Chief Risk Officer / CISO]
- Raportowanie do organu nadzoru: zgodnie z harmonogramem nadzorczym
