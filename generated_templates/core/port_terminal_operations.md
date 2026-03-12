---
title: Port Terminal Operations
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Port Terminal Operations


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Ustala spójne zasady prowadzenia operacji terminalowych (morskich/śródlądowych): planowanie zawinięć, cumowanie, przeładunki (kontenery, ro‑ro, masowe), kolejki ciężarówek/kolei, bezpieczeństwo i ciągłość działania. Minimalizuje opóźnienia, kolizje procesów i incydenty HSE oraz zapewnia zgodność z wymaganiami portowymi i celnymi.


## Zakres i granice

- Obejmuje: planowanie okien nabrzeżnych (berth planning), przydział suwnic/RTG/straddle carriers, harmonogramy przeładunków, TOS/WMS/yard management, kolejki gate/rail, safety & security (ISPS, HSE), monitoring KPI (throughput, dwell time), scenariusze awaryjne.  
- Poza zakresem: taryfy i rozliczenia (osobny dokument finansowy), projekty budowlane nabrzeży, projekt sieci OT/IT, utrzymanie statków.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: rozkład zawinięć, manifesty ładunkowe, plany stowarzyszeń linii (VSA), dostępność sprzętu i załóg, SLA z klientami, wymagania celne, dane pogodowe/pływy.  
- Wyjścia: plan operacyjny na dobę/tydzień, przydział zasobów (suwnice, bramy, składy), procedury bezpieczeństwa i komunikacji, plan kolejkowania ciężarówek/kolei, alerty i runbooki incydentów, raport KPI.


## Założenia

- Dostępność TOS, łączności radiowej/IT i danych AIS.  
- Współpraca służb portowych i celnych.  
- Stała dostępność sprzętu i załóg wg planu.


## Otwarte pytania

- Czy wymagane są dodatkowe kontrole celne dla określonych ładunków?  
- Jakie SLA z liniami priorytetują przydział okien?  
- Jak często testować runbooki awaryjne?  
- Czy kolejkowanie gate będzie dynamiczne (ETA‑driven) czy slotowe?

## Powiązania (meta)

- Key Documents: safety_management_plan, crisis_management_playbook, network_ot_security, customs_clearance_procedure, tos_configuration_reference, asset_maintenance_plan.  
- Key Document Structures: okno nabrzeżne, przydział zasobów, bezpieczeństwo, kolejka gate/rail, monitoring KPI, scenariusze awaryjne.  
- Document Dependencies: TOS/WMS/rail system, CCTV/VMS, IoT/RFID, meteo/tide feed, workforce planning.  
- Standardy/Compliance: ISPS Code, IMO/IAPH zalecenia, lokalne przepisy portowe, HSE.


## Zależności dokumentu

Wymaga: dostępności TOS i jego API, integracji z systemem kolejki gate, danych AIS/ETA, planów sprzętu i utrzymania, polityk HSE/ISPS, kontaktów do służb (port, cło, straż). Braki = blokery DoR.


## Fazy cyklu życia

- Inicjacja okna nabrzeżnego.  
- Planowanie szczegółowe (resource planning).  
- Operacje i monitoring w czasie rzeczywistym.  
- Rozliczenie/raport KPI i wnioski.  
- Retrospektywa i zmiany procedur.



## Struktura sekcji (szkielet)

- Cel i zakres dokumentu
- Główne sekcje merytoryczne
- Powiązania z innymi dokumentami
- Wymagane zatwierdzenia i przeglądy
- Historia zmian

## Szybkie powiązania

- linkage_index.jsonl (port/terminal/operations)  
- tos_configuration_reference, customs_clearance_procedure, safety_management_plan


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

1. Wypełnij kartę statku i plan zasobów.  
2. Potwierdź bezpieczeństwo (ISPS/HSE) i komunikację.  
3. Uruchom operacje, monitoruj KPI/alerty, aktualizuj plan.  
4. Po zakończeniu zamknij raport dzienny i odhacz DoD.


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

- TOS: Terminal Operating System do planowania i realizacji ruchu.  
- Berth window: zarezerwowane okno czasowe przy nabrzeżu.  
- Moves per hour (MPH): kluczowy KPI wydajności suwnic.


## Przykłady użycia

- Planowanie serwisu kontenerowego z trzema statkami jednocześnie.  
- Przeładunek ro‑ro z priorytetem pojazdów ciężkich.  
- Zarządzanie kolejką gate w szczycie i przekierowanie na rail.


## Ryzyka i ograniczenia

- Sztorm/opóźnienia pogodowe → przesunięcia okien i koszty.  
- Awaria TOS/komunikacji → przestoje.  
- Incydent HSE/ISPS → zatrzymanie operacji.  
- Niedoszacowanie zasobów → kongestia yard/gate.


## Decyzje i uzasadnienia

- Priorytetyzacja serwisów wg SLA i demurrage.  
- Model kolejki (sloty vs FCFS) i kanały komunikacji.  
- Progi KPI dla alertów i eskalacji.


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

- Planowanie okien ↔ Przydział zasobów ↔ Kolejka gate/rail (spójność czasowa).  
- Bezpieczeństwo ↔ Scenariusze awaryjne ↔ Komunikacja.  
- KPI ↔ Raporty dzienne ↔ Ciągłe doskonalenie.


## Struktura sekcji

1) Kontekst statku/ładunku i okno nabrzeżne  
2) Przydział zasobów (sprzęt, ludzie, sloty gate/rail)  
3) Bezpieczeństwo (ISPS/HSE)  
4) Operacje dzienne i komunikacja (mostek, terminal, cło)  
5) Monitoring i KPI (throughput, dwell, moves/h)  
6) Scenariusze awaryjne i runbooki  
7) Raportowanie i doskonalenie


## Wymagane rozwinięcia

- Karta statku/serwisu: ETA/ETD, ładunek, wymagania specjalne.  
- Plan zasobów: macierz sprzęt × zmiana × zadanie.  
- Procedury bezpieczeństwa: kontrole, strefy, ewakuacja.  
- Runbooki awaryjne: sztorm, wypadek, awaria TOS, blackout.  
- Plan komunikacji: kto, kiedy, jak (radio/IT).  
- KPI z progami i alertami.


## Wymagane streszczenia

- Executive summary: status operacji dnia, główne ryzyka, okna.  
- Skrócona karta bezpieczeństwa: strefy, kontakty, zasady.


## Guidance (skrót)

- Synchronizuj ETA/ETD z AIS i TOS; zmiany od razu komunikuj.  
- Planuj zasoby z buforami pogodowymi i na awarie sprzętu.  
- Utrzymuj jeden kanał prawdy dla kolejki gate/rail.  
- Monitoruj moves/h i dwell w czasie rzeczywistym.  
- Bezpieczeństwo przed wydajnością: ISPS/HSE ma pierwszeństwo.  
- Testuj runbooki awaryjne co kwartał.


## Checklisty Definition of Ready (DoR)

- [ ] ETA/ETD, ładunek i wymagania specjalne potwierdzone.  
- [ ] Dostępne zasoby (sprzęt, załoga, sloty gate/rail).  
- [ ] Aktualne procedury bezpieczeństwa i kontakty służb.  
- [ ] TOS/komunikacja działa; alerty skonfigurowane.  
- [ ] Warunki pogodowe/pływy ocenione; ryzyka zapisane.


## Checklisty Definition of Done (DoD)

- [ ] Operacje zakończone; KPI i zdarzenia zarejestrowane.  
- [ ] Brak zaległych alertów; odnotowano wyjątki i działania.  
- [ ] Raport dzienny wysłany; lessons learned zanotowane.  
- [ ] Aktualizacja linkage_index i planów na kolejne okna.

