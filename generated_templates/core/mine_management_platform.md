---
title: Mine Management Platform
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Mine Management Platform


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Zdefiniować wymagania i architekturę platformy zarządzania kopalnią (operacje, bezpieczeństwo, produkcja), zapewniając integrację systemów OT/IT i zgodność regulacyjną.


## Zakres i granice

- Obejmuje: moduły (planowanie wydobycia, dispatch, fleet management, safety, środowisko, utrzymanie ruchu), integracje OT (SCADA, telemetry, czujniki), geologia/GIS, dane produkcyjne, raportowanie, alerty bezpieczeństwa, mobilne aplikacje terenowe, dostępność offline, bezpieczeństwo (segregacja IT/OT, IAM), zgodność (BHP/środowisko), SLO.
- Poza zakresem: szczegółowy projekt sieci OT (osobny), system ERP/finansowy (linkowany).


## Użytkownicy i interesariusze

- [Rola] — [potrzeby/odpowiedzialności]
- [Rola] — [potrzeby/odpowiedzialności]


## Wejścia i wyjścia

- Wejścia: wymagania operacyjne, przepisy BHP/środowiskowe, mapy/GIS, katalog urządzeń/floty, integracje OT/SCADA, SLO, polityki bezpieczeństwa, warunki terenowe (offline/edge).
- Wyjścia: architektura platformy, moduły i integracje, model danych (produkcja/safety/fleet), wymagania offline/edge, bezpieczeństwo/segregacja, plan wdrożenia, KPI (produkcja, incydenty, MTBF floty), runbooki.


## Założenia
- Dostępne systemy TOS/WMS/customs.  
- Zasoby portowe (sprzęt, załogi) dostępne.  
- Dane AIS/meteo wiarygodne.
## Otwarte pytania
- Jakie SLA z liniami i klientami?  
- Jak obsłużyć multi-terminal/port współdzielony?  
- Jak długo przechowywać logi operacyjne i KPI?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: systemy OT/SCADA, GIS, flota, safety systems, polityki bezpieczeństwa IT/OT, przepisy, łączność terenowa; brak – odnotuj.


## Fazy cyklu życia

Discovery → Design → Pilot (site) → Rollout (site/region) → Operacje → Ewaluacja.



## Struktura sekcji (szkielet)

- Use-case operacyjne i KPI.
- Architektura logiczna/fizyczna (edge/OT/IT/cloud, sieć, bezpieczeństwo).
- Integracje OT/SCADA, GIS, flota, safety.
- Moduły funkcjonalne (production, dispatch, fleet, maintenance, safety, env, reporting).
- Dane i model (telemetria, produkcja, safety, geologia), offline/edge sync.
- Bezpieczeństwo i zgodność (segregacja, IAM, audyt, BHP, środowisko).
- UX i mobilność (teren, offline, języki).
- Observability i SLA.
- Plan wdrożenia (pilotaż, rollout, szkolenia).
- Ryzyka i mitigacje.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

- Zbierz wymagania i systemy; zaprojektuj architekturę i integracje; uwzględnij offline/safety; zaplanuj pilot i rollout; monitoruj KPI.


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
- TOS: Terminal Operating System.  
- FCFS: First Come First Served.  
- Dwell time: czas postoju kontenera/ładunku.
## Przykłady użycia
- Projekt procesu dla nowego terminala kontenerowego.  
- Optymalizacja kolejek gate/rail w szczycie.  
- Przygotowanie runbooków na sztorm/awarię TOS.
## Ryzyka i ograniczenia
- Zmiany pogody → opóźnienia i koszty.  
- Błędy TOS/integracji → przestoje.  
- Nieoptymalne kolejki → kongestia yard/gate.  
- Brak testów awaryjnych → chaos przy incydentach.
## Decyzje i uzasadnienia
- Model kolejkowania i priorytety.  
- Bufery zasobów i moves/h targety.  
- Zakres integracji i odpowiedzialności.  
- Kadencja raportów i przeglądów KPI.
## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód]
- [Dokument Z → Sekcja W] — [powód]


## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1]
- [Standard 2]


## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ]
- [Sekcja C] -> [Sekcja D] : [typ]


## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ]
- [Dokument C] -> [Dokument D] : [typ]


## Ścieżki informacji

- [Wejście] → [Źródło] → [Rozwinięcie] → [Wyjście]
- [Wejście] → [Źródło] → [Streszczenie] → [Wyjście]


## Weryfikacja spójności

- [ ] Ścieżki informacji zamknięte
- [ ] Brak sprzecznych relacji
- [ ] Sekcje krytyczne mają źródła


## Lista kontrolna spójności relacji

- [ ] Relacje mają sekcje źródłowe
- [ ] Relacje nie są sprzeczne
- [ ] Cross-doc uzasadnione
- [ ] Rozwinięcia/streszczenia odnotowane


## Artefakty powiązane

- [Artefakt 1]
- [Artefakt 2]


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]


## Ścieżka akceptacji

1. Autor przygotowuje wersję roboczą i przeprowadza samorecenzję.
2. Recenzent techniczny (Tech Lead / BA) weryfikuje merytorycznie.
3. Właściciel procesu zatwierdza treść i zakres.
4. PM / Scrum Master aktualizuje metadata (wersja, data, status).
5. Dokument trafia do repozytorium i jest linkowany w Szybkie powiązania.

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

Moduły → dane → integracje; bezpieczeństwo → segregacja/edge; offline → architektura/UX; KPI → raporty.


## Wymagane rozwinięcia

- Integracje OT/SCADA → protokoły, bramy, bezpieczeństwo.
- Offline → strategia sync i konfliktów.


## Wymagane streszczenia

- Mapa architektury i modułów + KPI.


## Guidance

Cel: spójna, bezpieczna platforma górnicza. DoR: wymagania operacyjne, systemy OT/GIS/flota, przepisy. DoD: architektura/moduły/dane/bezpieczeństwo/rollout opisane; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Wymagania operacyjne i systemy OT/SCADA/GIS/flota; [ ] Przepisy BHP/środowiskowe; [ ] SLO i łączność.
- DoD: [ ] Architektura/moduły/dane/bezpieczeństwo/rollout opisane; [ ] Ryzyka/mitigacje; [ ] Sekcje N/A uzasadnione; metadane aktualne.

