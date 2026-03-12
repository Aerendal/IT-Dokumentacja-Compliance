---
title: Wizja digital twin w produkcji
status: needs_content
aligned: true
aligned_rev: 3
aligned_at: 2026-02-09
aligned_by: codex
---
# Wizja digital twin w produkcji


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Wizja digital twin dla produkcji.



## Zakres i granice
- Obejmuje: przypadki użycia (monitoring, symulacja, optymalizacja, przewidywanie), domeny danych (OT/IT/IoT), źródła i częstotliwość danych, modele i analitykę, wizualizację, integracje (SCADA/IoT/ERP/PLM/CMMS), bezpieczeństwo i prywatność, governance danych, wskaźniki sukcesu, roadmapę i pilota.
- Poza zakresem: szczegółowy projekt techniczny (oddzielny dokument), hardware sensorów (link), kontrakty komercyjne.
## Użytkownicy i interesariusze
- Product/Business, Architecture, OT/IT, Security, Data/Analytics, Operations, Finance.
## Wejścia i wyjścia
- Wejścia: cele biznesowe, procesy/asset map, dane sensorów/OT/IT, obecna architektura (SCADA/IoT/cloud/edge), wymagania bezpieczeństwa i danych, ograniczenia regulacyjne, dostępne modele/algorytmy, budżet i zasoby.
- Wyjścia: opis wizji i use case’ów, definicja wartości (KPI), high‑level architektura, wymagania danych i integracji, podejście do bezpieczeństwa/governance, plan pilota i roadmapa, ryzyka i decyzje.
## Założenia
- Dostępne są dane i systemy źródłowe; sponsor biznesowy; budżet pilota.
## Otwarte pytania
- Jakie regulacje/bezpieczeństwo OT dotyczą środowiska? 
- Jaki horyzont zwrotu (ROI) jest akceptowalny?
## Powiązania (meta)
- Key Documents: iot_strategy, data_strategy, security_ot_policy, edge_architecture, model_governance, integration_strategy, plm_strategy.
- Key Document Structures: use case, dane, architektura, bezpieczeństwo, roadmapa.
- Document Dependencies: inwentarz assetów, systemy OT/IT, narzędzia IoT/stream, platforma analityczna, IAM/segregacja, governance danych.
## Zależności dokumentu
Wymaga: listy use case’ów, inwentarza assetów, mapy systemów OT/IT/IoT, wymagań bezpieczeństwa/governance, budżetu/pilota. Bez tego DoR otwarte.
## Fazy cyklu życia
- Wizja i cele; identyfikacja use case’ów.
- Analiza danych i architektury; bezpieczeństwo/governance.
- Pilot (MVP) i pomiar KPI; decyzja skalowania.
- Roadmapa i skalowanie; ciągłe doskonalenie.
## Struktura sekcji (szkielet)

1. Cel i zakres (linie/maszyny).
2. Dane i modele fizyczne.
3. Integracje: OT/IT, symulacje.
4. Use case: optymalizacja, predictive.
5. Architektura i technologia.
6. Roadmap i metryki.


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.

## Standardy i compliance


Lista standardów i wymagań regulacyjnych mających zastosowanie do tego dokumentu.
Uzupełnij na podstawie sekcji "Mające zastosowanie standardy i normy" oraz tabeli `doc_standard_mapping`.

- Standard / norma: [kod i nazwa]
- Wymaganie regulacyjne: [kod i treść]
- Polityka wewnętrzna: [nazwa polityki]


## RACI i role


Macierz RACI (Responsible / Accountable / Consulted / Informed) dla działań związanych z tym dokumentem.

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie | [rola]      | [rola]      | [rola]    | [rola]   |
| Przegląd  | [rola]      | [rola]      | [rola]    | [rola]   |
| Aktualizacja | [rola]   | [rola]      | [rola]    | [rola]   |
| Archiwizacja | [rola]   | [rola]      | [rola]    | [rola]   |

## Jak używać dokumentu

- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.



## Checklisty jakości

- [ ] Zakres/use case opisane.
- [ ] Dane/modele/integracje zmapowane.
- [ ] Architektura/roadmap zdefiniowane.
- [ ] Metryki ustalone.

## Definicje robocze
- Digital Twin, Edge, OT/IT, ModelOps, SCADA, PLM, CMMS.
## Przykłady użycia
- Pilotaż linii produkcyjnej: monitoring + predykcja awarii, architektura edge+cloud, KPI: downtime -X%.
- Miasto smart: twin infrastruktury, symulacja ruchu, KPI: czas przejazdu -Y%.
## Ryzyka i ograniczenia
- Brak danych jakościowych; bezpieczeństwo OT; brak KPI → trudny zwrot z inwestycji; integracje legacy.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- IoT Strategy, Data Strategy, Security OT Policy, Edge Architecture, Model Governance, Integration Strategy, PLM Strategy.
## Powiązania z sekcjami innych dokumentów
- Security OT → segmentacja; Data Strategy → governance; Model Governance → lifecycle modeli.
## Słownik pojęć w dokumencie
- Digital Twin, Edge, OT, IT, SCADA, PLM, CMMS, ModelOps.
## Wymagane odwołania do standardów
- Standardy OT security, wytyczne branżowe (np. ISA/IEC 62443), privacy danych IoT.
## Mapa relacji sekcja→sekcja
- Use case/KPI → Dane/architektura → Bezpieczeństwo/governance → Pilot → Roadmapa.
## Mapa relacji dokument→dokument
- Digital Twin Vision → IoT/Data/Security/Model Governance → Pilot → Roadmap.
## Ścieżki informacji
- Use case → Dane/architektura → Pilot → Wyniki → Roadmapa.
## Weryfikacja spójności

- [ ] Czy wszystkie ścieżki informacji są zamknięte (każde wejście ma wyjście)?
- [ ] Czy istnieją pętle lub sprzeczne relacje między sekcjami?
- [ ] Czy sekcje kluczowe mają wskazane źródła i odbiorców?
- [ ] Czy terminologia jest spójna z sekcją "Słownik pojęć"?

## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane
- Mapy assetów/systemów, diagram architektury, plan pilota, KPI, raport pilota, roadmapa.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Product/Architecture → Security/OT → Data/Analytics → Exec/Owner sign‑off.
## Metryki jakości
- Postęp pilotów vs plan, osiągnięcie KPI, czas do decyzji scale/no‑go, zgodność bezpieczeństwa/governance.
## Kryteria ukończenia
- [ ] Wizja/use case/KPI/architektura/pilot/roadmapa opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.
