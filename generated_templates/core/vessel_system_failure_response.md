---
title: Vessel System Failure Response
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Vessel System Failure Response


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan reakcji na awarie systemów statku (napęd, ster, zasilanie, nawigacja, komunikacja). Ma minimalizować ryzyko dla załogi, ładunku i środowiska oraz spełnić wymagania bezpieczeństwa morskiego.


## Zakres i granice

- Obejmuje: typy awarii (propulsion/steering/power/nav/comm), detekcję i alarmowanie, procedury awaryjne, fallback/manual override, komunikację (VHF/GMDSS), współpracę z MRCC/portem/pilotem, ograniczenia manewrowe, zabezpieczenie ładunku/pasażerów, środki zapobiegające kolizji/grounding, logi i raporty, testy/ćwiczenia.  
- Poza zakresem: pożar/wyciek (osobne plany), piractwo.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: checklists systemów, instrukcje producentów, mapy/pozycja, stany pogodowe, status załogi, procedury ISM/IMO, kanały komunikacji, dane czujników.  
- Wyjścia: sekwencje działań per awaria, komunikaty (port/MRCC), zapis w logu, raport po zdarzeniu, aktualizacje checklists.


## Założenia

- Systemy komunikacji i logi działają.  
- Załoga zna role.  
- Przepisy lokalne/regionalne są znane.


## Otwarte pytania

- Jak integrujemy dane z ECDIS/VDR w raportach?  
- Czy potrzebne są dodatkowe procedury dla LNG/chem tankers?  
- Jakie wymagania ubezpieczyciela?


## Powiązania (meta)

- Key Documents: maritime_emergency_response, safety_compliance, navigation_manual, engineering_checklists, communication_plan_emergency, dr_plan.  
- Key Document Structures: detekcja, reakcja, komunikacja, logi, ćwiczenia.  
- Document Dependencies: systemy statku, czujniki/alarms, VHF/GMDSS, ECDIS/GPS, engine/steering controls.


## Zależności dokumentu

Wymaga: aktualnych checklists producentów, konfiguracji alarmów, kanałów komunikacji, szkolenia załogi, planów ISM/IMO, danych pozycji/pogody. Braki = DoR otwarte.


## Fazy cyklu życia

- Przygotowanie i ćwiczenia.  
- Reakcja na awarię i komunikacja.  
- Stabilizacja/holowanie jeśli potrzebne.  
- Raport i aktualizacja planów.



## Struktura sekcji (szkielet)
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (vessel/system/failure/response)  
- maritime_emergency_response, engineering_checklists, communication_plan_emergency


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów

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

1. Zidentyfikuj awarię; uruchom checklistę dla danego systemu.  
2. Zabezpiecz manewrowość; skomunikuj MRCC/port/pilota; loguj.  
3. Po zdarzeniu sporządź raport, wykonaj debrief; zaktualizuj DoR/DoD i linkage_index.


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

- MRCC: Maritime Rescue Coordination Centre.  
- ISM/IMO: Międzynarodowy Kodeks Zarządzania Bezpieczeństwem / Organizacja Morska.  
- Manual override: ręczne sterowanie/obejście automatyki.


## Przykłady użycia

- Utrata napędu w porcie – użycie holowników, komunikacja z VTS.  
- Awaria steru na otwartym morzu – manual steering/anchor, alarm MRCC.  
- Utrata zasilania – black start procedura.


## Ryzyka i ograniczenia

- Opóźniona komunikacja → kolizja/grounding.  
- Brak ćwiczeń → błędy załogi.  
- Niesprawne fallback/manual → brak manewru.


## Decyzje i uzasadnienia

- Kiedy wzywać holownik/pilota.  
- Priorytety między ochroną ładunku a manewrem.  
- Zakres zapasu energii/black start.


## Powiązania z innymi dokumentami

- safety_compliance — wymogi.  
- maritime_emergency_response — ogólne działania.  
- communication_plan_emergency — kanały.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- ISM/IMO, SOLAS, lokalne przepisy żeglugowe.  
- Standardy operatora/armatora.

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

- Detekcja → Reakcja → Komunikacja → Logi/raport.  
- Fallback/manual → Bezpieczeństwo manewru → Współpraca z portem/MRCC.  
- Ćwiczenia → Gotowość → Aktualizacje procedur.


## Struktura sekcji

1) Klasy awarii i priorytety (propulsion/steering/power/nav/comm)  
2) Detekcja/alarmy i identyfikacja źródła  
3) Procedury reakcji per typ awarii (kroki, role)  
4) Fallback/manual override i ograniczenia operacyjne  
5) Komunikacja (VHF/GMDSS, port/MRCC/pilot, wewnętrzna)  
6) Bezpieczeństwo ludzi/ładunku/środowiska  
7) Logi/raportowanie (ISM/IMO, rejestry)  
8) Ćwiczenia i testy (harmonogram, scenariusze)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Checklists per awaria (propulsion, steering, power, nav, comm).  
- Szablony komunikatów do MRCC/portu.  
- Procedura manual steering/anchor użycia w awarii.  
- Plan ćwiczeń i review po zdarzeniu.


## Wymagane streszczenia

- Executive snapshot: gotowość systemów, ostatnie ćwiczenia, top ryzyka.  
- Karta quick-response per awaria (kroki + kanały).


## Guidance (skrót)

- Ćwicz scenariusze awarii regularnie.  
- Komunikuj wcześnie z MRCC/portem; utrzymuj kanały awaryjne.  
- Utrzymuj logi i raporty zgodne z ISM/IMO.  
- Sprawdzaj manual override/anchor readiness.  
- Po zdarzeniu – debrief i aktualizacja planu.


## Checklisty Definition of Ready (DoR)

- [ ] Checklists producentów i alarmy aktualne.  
- [ ] Kanały VHF/GMDSS działają; kontakty MRCC/port/pilot dostępne.  
- [ ] Załoga przeszkolona; plan ćwiczeń ustalony.  
- [ ] Procedury logów/raportów ISM/IMO gotowe.  
- [ ] Manual override/anchor sprawne.


## Checklisty Definition of Done (DoD)

- [ ] Reakcja wykonana wg checklist; status/wersja/data uzupełnione.  
- [ ] Komunikaty wysłane; log/raport złożony.  
- [ ] Sprzęt/fallback sprawdzony po zdarzeniu.  
- [ ] Lessons learned i aktualizacje planu wykonane; linkage_index zaktualizowany.  
- [ ] Kolejne ćwiczenia zaplanowane.

