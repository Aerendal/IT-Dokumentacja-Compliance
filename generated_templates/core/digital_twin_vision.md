---
title: Digital Twin Vision
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Digital Twin Vision


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przedstawia wizję i cele wdrożenia cyfrowych bliźniaków (Digital Twin) dla produktu/obiektu/procesu: wartość biznesowa, zakres, dane, integracje, architektura i roadmapa. Ma być kompasem dla zespołów technicznych i biznesu.


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
- Streszczenie i wizja
- Diagnoza stanu i kontekst
- Cele i KPI
- Filar/priorytety i inicjatywy
- Horyzonty/roadmapa i zależności
- Ryzyka i założenia
- Governance, finansowanie i raportowanie
## Szybkie powiązania

- linkage_index.jsonl (digital_twin/vision)
- iot_strategy, data_strategy, security_ot_policy, edge_architecture, model_governance, integration_strategy, plm_strategy


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

1. Zdefiniuj cele/KPI i top use case’y; zbierz dane/systemy i wymagania bezpieczeństwa.
2. Nakreśl architekturę i plan pilota; określ kryteria go/no‑go.
3. Wykonaj pilota, zmierz KPI, zaktualizuj roadmapę; zamknij DoR/DoD i linkage_index.


## Checklisty jakości

### Kompletność
- **Kryterium:** Wszystkie wymagane sekcje i pola są wypełnione
- **Metryka:** Odsetek wypełnionych sekcji do wymaganych
- **Próg OK:** 90%
- **Narzędzie:** template_auditor.py, checklist_atomic.jsonl

### Dokładność
- **Kryterium:** Informacje są poprawne merytorycznie i aktualne
- **Metryka:** Przegląd ekspercki; data ostatniej aktualizacji
- **Próg OK:** Przegląd co 3 mies.
- **Narzędzie:** regulation_updater.py

### Spójność
- **Kryterium:** Terminologia i struktura są spójne w całej bibliotece
- **Metryka:** Liczba niespójności terminologicznych i strukturalnych
- **Próg OK:** 0 niespójności
- **Narzędzie:** bulk_section_patcher.py

### Śledzalność
- **Kryterium:** Każda sekcja ma źródło (standard, regulacja, decyzja)
- **Metryka:** Odsetek sekcji z wypełnionymi standards_refs
- **Próg OK:** 80%
- **Narzędzie:** impact_analyzer.py

### Aktualność
- **Kryterium:** Dokument jest aktualny względem obowiązujących regulacji
- **Metryka:** Czas od ostatniej aktualizacji vs. częstotliwość przeglądów
- **Próg OK:** < 6 mies.
- **Narzędzie:** changelog_tracker.py

### Użyteczność
- **Kryterium:** Użytkownik końcowy może efektywnie wypełnić dokument na podstawie guidance
- **Metryka:** Ocena guidance (score z template_auditor); feedback użytkowników
- **Próg OK:** Score >= 70
- **Narzędzie:** template_auditor.py

## Definicje robocze

- Digital Twin, Edge, OT/IT, ModelOps, SCADA, PLM, CMMS.


## Przykłady użycia

- Pilotaż linii produkcyjnej: monitoring + predykcja awarii, architektura edge+cloud, KPI: downtime -X%.
- Miasto smart: twin infrastruktury, symulacja ruchu, KPI: czas przejazdu -Y%.


## Ryzyka i ograniczenia

- Brak danych jakościowych; bezpieczeństwo OT; brak KPI → trudny zwrot z inwestycji; integracje legacy.


## Decyzje i uzasadnienia

- [Decyzja] Use case pilota i KPI — uzasadnienie wartości/ryzyka.
- [Decyzja] Architektura edge/cloud i integracje — uzasadnienie danych/bezpieczeństwa.


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

- [ ] Use case’y/KPI spójne z danymi i architekturą; kryteria pilota jasne.
- [ ] Bezpieczeństwo/governance opisane; relacje cross‑doc wpisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy use case ma KPI, dane, architekturę i plan pilota.
- [ ] Każdy pilot ma kryteria go/no‑go i metryki; relacje cross‑doc opisane.


## Artefakty powiązane

- Mapy assetów/systemów, diagram architektury, plan pilota, KPI, raport pilota, roadmapa.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Product/Architecture → Security/OT → Data/Analytics → Exec/Owner sign‑off.


## Metryki jakości

- Postęp pilotów vs plan, osiągnięcie KPI, czas do decyzji scale/no‑go, zgodność bezpieczeństwa/governance.

## Kryteria ukończenia

- [ ] Wizja/use case/KPI/architektura/pilot/roadmapa opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Use case → Dane/architektura → Bezpieczeństwo/governance → KPI → Roadmapa.
- Pilot → Metryki → Decyzje scale/no‑go.


## Struktura sekcji

1) Wizja i cele biznesowe (wartość, KPI, mierniki)  
2) Use case’y i priorytety (monitoring, optymalizacja, symulacja, predykcja)  
3) Dane i źródła (sensory/OT/IT/edge/cloud, częstotliwości, jakość, governance)  
4) Architektura high‑level (edge/ingest/stream/storage/model/visualization/integracje)  
5) Bezpieczeństwo i prywatność (segregacja OT/IT, IAM, szyfrowanie, bezpieczeństwo modeli, privacy)  
6) Modelowanie/analityka (typy modeli, lifecycle, MLOps/ModelOps)  
7) Integracje (SCADA/IoT/ERP/PLM/CMMS, API/eventy)  
8) Roadmapa i pilot (zakres, KPI, budżet, ryzyka, kryteria go/no‑go)  
9) Governance i operacje (role, RACI, dane, modele, zmiany)  
10) Ryzyka, decyzje, open issues


## Wymagane rozwinięcia

- Use case’y z KPI; inwentarz assetów i danych; wymagania bezpieczeństwa/governance.
- Architektura referencyjna (edge/ingest/processing/storage/visualization) i integracje.
- Plan pilota (zakres, KPI, metody pomiaru, budżet) i kryteria go/no‑go.


## Wymagane streszczenia

- Wizja, top use case’y, KPI, architektura high‑level, plan pilota i kryteria go/no‑go.


## Guidance (skrót)

- Zacznij od wartości biznesowej i KPI; unikaj „tech for tech”.
- Wybierz 1–2 use case’y na pilota; zapewnij dane i bezpieczeństwo OT/IT.
- Ustal governance danych/modeli; uwzględnij segregację domen i privacy.
- Planuj architekturę modularną (edge+cloud), z integracjami standardowymi.
- Mierz pilot twardymi KPI; skaluj etapowo na podstawie wyników.


## Checklisty Definition of Ready (DoR)

- [ ] Use case’y i KPI wstępnie zdefiniowane; inwentarz assetów/systemów zebrany.
- [ ] Wymagania bezpieczeństwa/governance znane; budżet pilota wstępny.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Wizja, use case’y, KPI, architektura i plan pilota opisane.
- [ ] Kryteria go/no‑go i roadmapa zdefiniowane; dokument w linkage_index.
- [ ] Wersja/data/właściciel zaktualizowane.

