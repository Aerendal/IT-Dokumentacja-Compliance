---
title: Port Efficiency Monitoring
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Port Efficiency Monitoring


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Monitorowanie efektywności portu (morskiego/rzecznego): przepustowość, czasy postoju, wykorzystanie zasobów, bezpieczeństwo i zgodność. Ma wspierać decyzje operacyjne, inwestycje i raportowanie do regulatorów.


## Zakres i granice

- Obejmuje: KPI (vessel turnaround, berth occupancy, crane moves/hour, truck/rail dwell, yard utilization, gate throughput), dane źródłowe (TOS, AIS, RFID, WMS, sensorty IoT), metryki bezpieczeństwa (incydenty, near-miss), SLA z operatorami, alerty i dashboardy, raporty regulatora, integracje (celna, linie, terminale), dane pogodowe i ETA.  
- Poza zakresem: szczegółowe procedury bezpieczeństwa portowego (osobne SOP), plan inwestycji (osobny dokument).


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: harmonogramy statków, dane TOS/berth plan, AIS/ETA, operacje suwnic/gate/yard, pogoda, SLA i kontrakty, dane bezpieczeństwa, raporty historyczne.  
- Wyjścia: dashboard KPI, alerty operacyjne, raporty dzienne/tygodniowe/miesięczne, rekomendacje optymalizacji, dane dla regulatorów/armatorów, checklisty DoR/DoD.


## Założenia

- Systemy TOS/AIS/WMS dostępne i możliwe do integracji.  
- Operatorzy współdzielą dane KPI.  
- Dostęp do pogody i danych bezpieczeństwa.


## Otwarte pytania

- Czy wymagane są prognozy ETA z ML?  
- Jakie są wymagania raportowe regulatorów lokalnych?  
- Jak obsłużyć blackout danych (AIS/offline)?


## Powiązania (meta)

- Key Documents: port_operations_plan, safety_compliance, maintenance_schedule, capacity_planning, incident_response_runbook, data_integration_plan.  
- Key Document Structures: KPI, źródła danych, alerty, raporty, bezpieczeństwo, integracje.  
- Document Dependencies: TOS, AIS, WMS/YMS, IoT sensorty, weather API, data warehouse/BI, SLA repo, CMMS.


## Zależności dokumentu

Wymaga: dostępu do danych TOS/AIS/WMS/IoT, zdefiniowanych KPI i SLA, integracji danych, polityk bezpieczeństwa i raportowania, harmonogramów statków, mapy interesariuszy. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja KPI i źródeł; integracja danych.  
- Budowa dashboardów/alertów i pilota.  
- Operacje ciągłe i doskonalenie; przeglądy okresowe.  
- Aktualizacje przy zmianach infrastruktury/regulacji.



## Struktura sekcji (szkielet)
- Cel monitoringu i zakres (usługi/ścieżki)
- SLO/SLI i priorytety alertowania
- Metryki/logi/traces i źródła danych
- Alerty/reguły, progi i runbooki
- Dashboardy i testy syntetyczne
- Operacje: on-call, eskalacje, przeglądy
- Utrzymanie, budżety zdarzeń i ciągłe doskonalenie
## Szybkie powiązania

- linkage_index.jsonl (port/efficiency/monitoring)  
- port_operations_plan, capacity_planning, safety_compliance, data_integration_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Zdefiniuj KPI i źródła; zbuduj integracje i walidacje.  
2. Skonfiguruj dashboardy/alerty i raporty; przypisz właścicieli.  
3. Monitoruj, reaguj, raportuj; aktualizuj DoR/DoD i linkage_index.


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

- Vessel turnaround: czas od wejścia do wyjścia.  
- Berth occupancy: % czasu zajętości nabrzeża.  
- Dwell time: czas postoju kontenera/pojazdu.


## Przykłady użycia

- Analiza wąskich gardeł w suwnicach i gate.  
- Raport do regulatora o incydentach i KPI.  
- Optymalizacja harmonogramu na podstawie AIS/ETA i pogody.


## Ryzyka i ograniczenia

- Dane z wielu systemów o różnej jakości.  
- Pogoda i zdarzenia losowe zakłócają KPI.  
- Brak wspólnych definicji KPI między operatorami.


## Decyzje i uzasadnienia

- Wybór KPI krytycznych i progów RAG.  
- Integracja danych (batch vs near-real-time).  
- Zakres alertów operacyjnych vs analitycznych.


## Powiązania z innymi dokumentami

- safety_compliance — raportowanie incydentów.  
- data_integration_plan — integracje.  
- capacity_planning — planowanie przepustowości.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Regulacje portowe/lokalne, wymogi bezpieczeństwa.  
- Wewnętrzne standardy danych i raportowania.

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

- KPI → Alerty → Decyzje operacyjne.  
- Źródła danych → Jakość danych → Raporty/BI → Regulator.  
- Bezpieczeństwo → Raporty incydentów → Działania korygujące.


## Struktura sekcji

1) Kontekst i cele (operacyjne, regulacyjne)  
2) KPI i definicje (turnaround, berth occupancy, yard, gate, safety)  
3) Źródła i integracje danych (TOS, AIS, IoT, WMS, pogoda, SLA)  
4) Jakość danych i walidacja (completeness, timeliness)  
5) Alerty i dashboardy (progi, RAG, kanały)  
6) Raportowanie i compliance (regulatorzy, armatorzy, operatorzy)  
7) Bezpieczeństwo/near-miss i korekty operacyjne  
8) Ciągłe doskonalenie i przeglądy KPI  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Definicje KPI z formułami i źródłami.  
- Mapy integracji danych i harmonogramy odświeżania.  
- Matryca alertów (progi, kanały, właściciele).  
- Szablon raportu dla regulatora/armatorów.


## Wymagane streszczenia

- Executive snapshot: RAG KPI, bottlenecki, rekomendacje.  
- Raport bezpieczeństwa (incydenty/near-miss, działania).


## Guidance (skrót)

- Ustal wspólne definicje KPI z operatorami; inaczej dane nieporównywalne.  
- Waliduj dane AIS/ETA z rzeczywistością; pogoda wpływa na planowanie.  
- Alerty mają być operacyjne (kto, kiedy, co zrobić).  
- Łącz KPI operacyjne z bezpieczeństwem — incydenty spowalniają ruch.  
- Regularnie przeglądaj RAG i aktualizuj progi sezonowo.


## Checklisty Definition of Ready (DoR)

- [ ] KPI i SLA uzgodnione z interesariuszami.  
- [ ] Dostępy do źródeł danych (TOS/AIS/WMS/IoT) zapewnione.  
- [ ] Harmonogramy statków i mapy procesów zebrane.  
- [ ] Progi alertów i odbiorcy wstępnie ustalone.  
- [ ] Wymagania regulatora znane.


## Checklisty Definition of Done (DoD)

- [ ] Dashboardy/alerty działają; KPI raportowane; status/wersja/data uzupełnione.  
- [ ] Jakość danych monitorowana; walidacje wdrożone.  
- [ ] Raporty regulator/armator opublikowane; SLA śledzone.  
- [ ] Rekomendacje i działania korygujące zapisane; linkage_index zaktualizowany.  
- [ ] Ryzyka i decyzje udokumentowane.

