---
title: Service Implementation Schedule
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Service Implementation Schedule


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przedstawić harmonogram wdrożenia usługi (zakres, kamienie milowe, zależności, zasoby) z jasnymi kryteriami wejścia/wyjścia, aby zapewnić przewidywalne dostarczenie i minimalizować ryzyko opóźnień.


## Zakres i granice

- Obejmuje: plan etapów (analiza, build, test, pilot, prod), kamienie milowe, zależności techniczne i biznesowe, zasoby i role, okna serwisowe, plan ryzyk i mitigation, komunikację statusu.  
- Poza zakresem: szczegółowe zadania zesprintowe (w backlogu), budżet portfelowy.


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: zakres usługi, wymagania, lista systemów zależnych, SLA/OLA, dostępność zasobów, polityki change, okna serwisowe, ryzyka znane.  
- Wyjścia: harmonogram z datami/odpowiedzialnymi, lista zależności i blokad, plan testów/akceptacji, plan komunikacji, DoR/DoD dla etapów, raport statusu.


## Założenia

- Środowiska są stabilne i dostępne.  
- Zasoby (ludzie/budżet) przydzielone na cały harmonogram.  
- CAB/komitety są dostępne do decyzji.


## Otwarte pytania

- Jakie są sztywne daty zewnętrzne (regulator/klient)?  
- Jak dzielić status dla wielu stref czasowych?  
- Czy potrzebny jest rollout falowy (regiony/kontenery)?

## Powiązania (meta)

- Key Documents: project_execution_plan, change_impact_assessment, release_readiness_statement, risk_assessment, rollback_runbook, service_dependency_map.  
- Key Document Structures: etapy, kamienie, zależności, ryzyka, testy/akceptacja, komunikacja.  
- Document Dependencies: CMDB, CI/CD, środowiska test/pilot/prod, CAB, monitoring.


## Zależności dokumentu

Wymaga: uzgodnionego zakresu i właścicieli, listy systemów zależnych, dostępności środowisk, okien serwisowych, planu testów i akceptacji biznesowej, zasobów (ludzie, budżet). Braki = brak DoR.


## Fazy cyklu życia

- Planowanie harmonogramu.  
- Egzekucja etapów i monitorowanie.  
- Przeglądy Go/No‑Go i korekty.  
- Rollout/pilot → produkcja.  
- Zamknięcie i retrospektywa.



## Struktura sekcji (szkielet)
- Cel i zakres wdrożenia
- Środowiska i okna wdrożeniowe
- Architektura docelowa i przepływy danych
- Kroki/migracja (pilot → produkcja)
- Plan testów i kryteria go/no-go
- Monitoring/observability i runbooki
- Rollback/contingency i komunikacja
- Ryzyka, zależności, RACI
## Szybkie powiązania

- linkage_index.jsonl (service/implementation/schedule)  
- project_execution_plan, service_dependency_map, release_readiness_statement


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

1. Zdefiniuj etapy i kamienie z datami i wejściami/wyjściami.  
2. Zmapuj zależności i ryzyka; przypisz rezerwy i właścicieli.  
3. Ustal plan testów/akceptacji i okna serwisowe.  
4. Monitoruj postęp, aktualizuj status i decyzje Go/No‑Go; zamknij DoD.


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

- Kamień milowy: punkt kontrolny z mierzalnym rezultatem.  
- Go/No‑Go: decyzja o przejściu do kolejnego etapu.  
- RAG: status kolorystyczny (Red/Amber/Green).


## Przykłady użycia

- Wdrożenie nowej usługi SaaS dla klientów enterprise.  
- Migracja usługi z data center do chmury.  
- Uruchomienie pilota funkcji w wybranym regionie.


## Ryzyka i ograniczenia

- Niedoszacowane zależności → opóźnienia.  
- Brak rezerw → kaskadowe przesunięcia.  
- Nieuzgodnione okna serwisowe → konflikt z innymi zmianami.  
- Niepełne testy → regresje w produkcji.


## Decyzje i uzasadnienia

- Daty kamieni i priorytety.  
- Zakres testów vs czas.  
- Kryteria stop/rollback.  
- Przydział zasobów i rezerw.


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

- Etapy ↔ Kamienie ↔ Testy/akceptacje ↔ Go/No‑Go.  
- Zależności ↔ Ryzyka ↔ Plan mitigacji ↔ Rezerwy czasu.  
- Komunikacja ↔ Harmonogram ↔ Interesariusze.


## Struktura sekcji

1) Zakres i cele wdrożenia  
2) Etapy i kamienie milowe z datami i rolami  
3) Zależności i blokady (techniczne/biznesowe)  
4) Plan testów i akceptacji (UAT/Pilot/Prod)  
5) Ryzyka i rezerwy, kryteria Go/No‑Go  
6) Plan komunikacji/statusy  
7) DoR/DoD, otwarte pytania


## Wymagane rozwinięcia

- Tabela etapów/kamieni z datami, właścicielem, wejściami/wyjściami.  
- Lista zależności z datą gotowości i wpływem.  
- Plan testów (zakres, środowiska, dane) i akceptacji.  
- Kryteria Go/No‑Go i plan rollback.  
- Szablon raportu statusowego (RAG, ryzyka, decyzje).


## Wymagane streszczenia

- Executive summary: kluczowe daty, ryzyka, rezerwa.  
- Skrót zależności krytycznych i blokad.


## Guidance (skrót)

- Wyraźnie oznacz kamienie „blocking” i ich właścicieli.  
- Zawsze przypisz rezerwy czasowe do ryzyk wysokich.  
- Synchronizuj harmonogram z CAB/oknami serwisowymi.  
- Aktualizuj status w cyklu stałym (np. tygodniowo); eskaluj blokady.  
- Odhacz DoR/DoD na każdym etapie; nie przechodź dalej bez spełnienia.


## Checklisty Definition of Ready (DoR)

- [ ] Zakres i właściciele potwierdzeni.  
- [ ] Zależności i środowiska dostępne.  
- [ ] Plan testów/akceptacji i dane testowe gotowe.  
- [ ] Okna serwisowe uzgodnione; komunikacja przygotowana.  
- [ ] Ryzyka zidentyfikowane; rezerwy zaplanowane.


## Checklisty Definition of Done (DoD)

- [ ] Kamienie osiągnięte; testy/akceptacje zaliczone.  
- [ ] Brak otwartych blokad na bieżący etap.  
- [ ] Raport statusowy zaktualizowany; interesariusze poinformowani.  
- [ ] linkage_index/CMDB zaktualizowane o zmiany.  
- [ ] Retrospektywa etapu wykonana; decyzje zapisane.

