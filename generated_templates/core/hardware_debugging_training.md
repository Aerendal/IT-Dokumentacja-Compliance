---
title: Hardware Debugging Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Hardware Debugging Training


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Program szkoleniowy z debugowania sprzętu/embedded: metody, narzędzia, bezpieczeństwo ESD, procedury i scenariusze awarii. Celem jest szybsza diagnoza usterek i zmniejszenie ryzyka uszkodzeń.


## Zakres i granice

- Obejmuje: ESD/safety, podstawy pomiarów (multimetr/oscyloskop/logic analyzer), JTAG/SWD, UART/console, analizę zasilania i termiki, firmware flashing/recovery, boundary scan, debug PCB/prototypów, typowe awarie (boot, komunikacja, pamięć, zegar), logowanie i ticketing, checklisty i laboratoria.  
- Poza zakresem: pełny kurs projektowania PCB; zaawansowane RF (oddzielne).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: lista platform/SoC, schematy/boM, narzędzia debug (JTAG pods, oscyloskopy), procedury bezpieczeństwa, przykładowe defekty, środowiska lab.  
- Wyjścia: sylabus, laby i scenariusze, checklisty DoR/DoD, notatki techniczne, wyniki ewaluacji uczestników, lista usprawnień narzędzi/procesu.


## Założenia

- Laboratoria i sprzęt są dostępne i zgodne z BHP.  
- Zespoły mają czas na szkolenie.  
- Dostępne są licencje/sterowniki narzędzi.


## Otwarte pytania

- Jak często powtarzać szkolenie?  
- Czy wymagane są certyfikaty/odznaki po szkoleniu?  
- Jak archiwizować logi i wyniki labów?


## Powiązania (meta)

- Key Documents: esd_safety_procedure, board_bringup_checklist, firmware_recovery_guide, logging_standards_embedded, lab_access_policy.  
- Key Document Structures: safety, narzędzia, scenariusze, procedury, ewaluacja.  
- Document Dependencies: lab sprzęt, debug pods, firmware repo, schematy, ticketing/logs.


## Zależności dokumentu

Wymaga: dostępnych narzędzi/labów, schematów i datasheetów, procedur ESD/safety, przykładowych defektów, uprawnień do flashowania/odczytu. Braki = DoR otwarte.


## Fazy cyklu życia

- Przygotowanie sylabusa i labów.  
- Szkolenie + ćwiczenia hands‑on.  
- Ewaluacja i feedback.  
- Aktualizacja materiałów i narzędzi.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (hardware/debugging/training)  
- esd_safety_procedure, board_bringup_checklist, firmware_recovery_guide, lab_access_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

1. Przygotuj lab i narzędzia; odśwież ESD/safety.  
2. Przeprowadź laby według scenariuszy; zbieraj logi/tickety.  
3. Oceń wyniki, zbierz feedback; aktualizuj materiały i linkage_index.


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

- ESD: Electrostatic Discharge.  
- Boundary scan: test IEEE 1149.x.  
- Logic analyzer: narzędzie do analizy cyfrowych przebiegów.


## Przykłady użycia

- Szkolenie nowych inżynierów hardware.  
- Warsztat z debugowania prototypu z SoC + DDR.  
- Scenariusz naprawy niedziałającego portu komunikacyjnego.


## Ryzyka i ograniczenia

- Uszkodzenie sprzętu przy błędnych pomiarach/flashu.  
- Brak ESD → sporadyczne, trudne do powtórzenia błędy.  
- Brak logów → utrata wiedzy i czasu.


## Decyzje i uzasadnienia

- Zakres scenariuszy w zależności od produktów/SoC.  
- Wybór narzędzi (open-source vs vendor).  
- Standard logów/ticketów (format danych pomiarowych).


## Powiązania z innymi dokumentami

- board_bringup_checklist — debug prototypów.  
- firmware_recovery_guide — flash/recovery.  
- logging_standards_embedded — format logów.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Zasady BHP/ESD labów.  
- IEEE 1149.x (boundary scan) gdzie stosowalne.

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

- Safety → Dostęp do lab → Laby/scenariusze → Ewaluacja.  
- Narzędzia → Procedury pomiarów → Analiza awarii.  
- Logowanie → Ticketing → Lessons learned.


## Struktura sekcji

1) Bezpieczeństwo i ESD (PPE, uziemienie, zasilanie)  
2) Narzędzia i konfiguracja (multimetr, scope, LA, JTAG/UART)  
3) Procedury pomiarów i logowania (power, clocks, signals)  
4) Scenariusze debug (boot failures, comms, memory, power/thermal)  
5) Firmware flashing/recovery i zabezpieczenia (locks, keys)  
6) Boundary scan i testy produkcyjne (opcjonalnie)  
7) Checklisty i laboratoria (kroki, oczekiwane wyniki)  
8) Ewaluacja uczestników i feedback  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Checklisty ESD/safety i konfiguracji stanowiska.  
- Scenariusze lab (np. brak zegara, zwarcie linii, uszkodzona pamięć).  
- Szablon logów/ticketów z danymi pomiarowymi.  
- Plan ewaluacji (quiz + praktyka).


## Wymagane streszczenia

- Executive snapshot: pokrycie uczestników, główne scenariusze, wyniki ewaluacji.  
- Krótka karta ESD/safety przy wejściu do labu.


## Guidance (skrót)

- Zawsze zacznij od bezpieczeństwa i zasilania; mierz, zanim zmienisz.  
- Dokumentuj pomiary i ustawienia; pozwala odtworzyć i porównać.  
- Używaj minimalnie inwazyjnych metod (passive probes, diff).  
- Ogranicz ryzyko: current limits, termika, ESD.  
- Ucz scenariuszami: od prostych do złożonych, na realnych płytkach.


## Checklisty Definition of Ready (DoR)

- [ ] Sprzęt i narzędzia dostępne; ESD/safety potwierdzone.  
- [ ] Schematy/datasheety i firmware w repo dostępne.  
- [ ] Scenariusze lab i checklisty przygotowane.  
- [ ] Uprawnienia do flashowania/odczytu nadane.  
- [ ] Plan ewaluacji ustalony.


## Checklisty Definition of Done (DoD)

- [ ] Laby wykonane; logi/tickety zapisane; status/wersja/data uzupełnione.  
- [ ] Ewaluacje przeprowadzone; feedback zebrany.  
- [ ] Materiały/checklisty zaktualizowane; lessons learned zapisane.  
- [ ] Linkage_index uzupełniony; ryzyka/dec. odnotowane.  
- [ ] Sprzęt/lab przywrócony do stanu bezpiecznego.

