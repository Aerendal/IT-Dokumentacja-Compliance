---
title: Port Operations Design
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Port Operations Design


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaprojektować procesy i systemy operacyjne portu (morskiego/śródlądowego): planowanie okien nabrzeżnych, przydział zasobów, kolejki gate/rail, bezpieczeństwo i monitoring KPI, by zwiększyć przepustowość i zgodność.


## Zakres i granice

- Obejmuje: berth planning, yard/stack plan, przydział suwnic/zasobów, TOS/WMS integracje, kolejki gate/rail, bezpieczeństwo (ISPS/HSE), customs interface, monitoring KPI (moves/h, dwell time), scenariusze awaryjne.  
- Poza zakresem: taryfy/rozliczenia (oddzielne dokumenty finansowe), projekty infrastruktury fizycznej.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: rozkład zawinięć, manifesty, dostępność sprzętu i załóg, SLA, wymagania celne, dane pogody/pływów, polityki bezpieczeństwa, TOS/WMS konfiguracje.  
- Wyjścia: projekt procesów operacyjnych, plany zasobów i kolejek, interfejsy systemów, runbooki awaryjne, KPI i alerty, checklisty DoR/DoD.


## Założenia

- Dostępne systemy TOS/WMS/customs.  
- Zasoby portowe (sprzęt, załogi) dostępne.  
- Dane AIS/meteo wiarygodne.


## Otwarte pytania

- Jakie SLA z liniami i klientami?  
- Jak obsłużyć multi-terminal/port współdzielony?  
- Jak długo przechowywać logi operacyjne i KPI?

## Powiązania (meta)

- Key Documents: port_terminal_operations, safety_management_plan, customs_clearance_procedure, tos_configuration_reference, crisis_management_playbook.  
- Key Document Structures: okna nabrzeżne, zasoby, kolejka gate/rail, bezpieczeństwo, KPI, scenariusze awaryjne.  
- Document Dependencies: TOS/WMS, rail/gate systems, AIS/meteo feeds, CCTV/IoT, CMDB.


## Zależności dokumentu

Wymaga: danych ETA/ETD, planów sprzętu, konfiguracji TOS/WMS, procedur bezpieczeństwa i celnych, danych meteo, polityk SLA. Brak = brak DoR.


## Fazy cyklu życia

- Analiza ruchu i zasobów.  
- Projekt procesów i interfejsów.  
- Testy/koordynacja z TOS/WMS/gate.  
- Operacje pilotażowe i iteracje.  
- Rollout i przeglądy KPI.



## Struktura sekcji (szkielet)

- Kontekst i wymagania
- Decyzje architektoniczne (ADR)
- Komponenty i integracje
- Diagramy (C4/UML/flowchart)
- Bezpieczeństwo i compliance
- Skalowalność i ograniczenia

## Szybkie powiązania

- linkage_index.jsonl (port/operations/design)  
- port_terminal_operations, tos_configuration_reference


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

1. Zbierz dane ruchu/statków i zasobów.  
2. Zaprojektuj procesy i integracje; przygotuj runbooki.  
3. Przeprowadź testy/piloty; wdroż zasady kolejkowania.  
4. Monitoruj KPI, poprawiaj i aktualizuj dokument/linkage_index.


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

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ relacji: rozszerza/streszcza/wymaga/wyklucza]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji

- [Wejście] -> [Sekcja źródłowa] -> [Sekcja rozwinięcia] -> [Wyjście]
- [Wejście] -> [Sekcja źródłowa] -> [Sekcja streszczenia] -> [Wyjście]

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

- [Artefakt 1, np. diagram architektury] — [opis i relacja do tego dokumentu]
- [Artefakt 2, np. schemat bazy danych] — [opis i relacja do tego dokumentu]

## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

- Berth planning ↔ Zasoby ↔ Kolejka gate/rail.  
- Bezpieczeństwo ↔ Scenariusze awaryjne ↔ Komunikacja.  
- KPI ↔ Raporty ↔ Ciągłe doskonalenie.


## Struktura sekcji

1) Kontekst i cele operacyjne  
2) Planowanie okien i przydział zasobów  
3) Kolejka gate/rail i ruch lądowy  
4) Integracje systemowe (TOS/WMS/customs)  
5) Bezpieczeństwo i scenariusze awaryjne  
6) Monitoring KPI i raportowanie  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Schemat procesu od ETA do wyjścia ładunku.  
- Matryca zasoby × zmiany × statki.  
- Polityka kolejkowania (slot vs FCFS) i priorytety.  
- Plan integracji TOS/WMS/customs i interfejsy.  
- Runbooki awaryjne (pogoda, awaria TOS, incydent HSE).  
- Dashboard KPI i alerty.


## Wymagane streszczenia

- Executive summary: przepustowość, główne ryzyka, zasoby.  
- Skrót planów kolejkowania i bezpieczeństwa.


## Guidance (skrót)

- Synchronizuj ETA/ETD z AIS/TOS; aktualizuj plany na bieżąco.  
- Planuj zasoby z buforami; monitoruj moves/h i dwell.  
- Jedno źródło prawdy dla kolejki gate/rail; unikaj duplikatów slotów.  
- Testuj scenariusze awaryjne i komunikację.  
- Raportuj KPI dziennie; wprowadzaj kaizen.  
- Aktualizuj linkage_index po zmianach procesów.


## Checklisty Definition of Ready (DoR)

- [ ] ETA/ETD i manifesty dostępne.  
- [ ] Zasoby i TOS/WMS skonfigurowane.  
- [ ] Polityki bezpieczeństwa/celne znane.  
- [ ] Plan kolejkowania uzgodniony.  
- [ ] Runbooki awaryjne wstępnie przygotowane.


## Checklisty Definition of Done (DoD)

- [ ] Procesy działają w operacji/pilocie; KPI w normie.  
- [ ] Integracje TOS/WMS/customs przetestowane.  
- [ ] Runbooki i komunikacja awaryjna działają.  
- [ ] Dashboard KPI aktywny; raporty publikowane.  
- [ ] Dokument/linkage_index zaktualizowane; brak krytycznych luk.

