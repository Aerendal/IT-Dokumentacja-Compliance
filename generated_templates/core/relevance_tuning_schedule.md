---
title: Relevance Tuning Schedule
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Relevance Tuning Schedule


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaplanuj cykliczne strojenie trafności wyszukiwarki/rankingu (feature weights, boosting, synonimy, filtracja), aby utrzymać lub poprawić metryki jakości i doświadczenie użytkowników.


## Zakres i granice

- Obejmuje: harmonogram eksperymentów/tuningów, wybór metryk (NDCG, CTR, success rate, zero results), dane etykietowane i feedback, backlog hipotez, procedury A/B, rollout/rollback, monitoring po wdrożeniu, aktualizacje słowników (synonimy/stopwords), testy regresji.  
- Poza zakresem: implementacja nowej architektury wyszukiwania (osobne dokumenty).


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: metryki bazowe, logi zapytań, feedback użytkowników, dane etykietowane, hipotezy/eksperymenty, budżet ruchu na testy.  
- Wyjścia: kalendarz tuningów, lista eksperymentów z priorytetami, wyniki A/B, zmiany konfiguracji (boosting, synonimy), checklisty DoR/DoD, raporty post-release.


## Założenia

- Dane i logi są dostępne; platforma A/B działa.  
- Zespół ma możliwość szybkiego rollbacku konfiguracji.  
- Metryki są zdefiniowane i monitorowane.


## Otwarte pytania

- Jak obsłużyć sezonowość zapytań w metrykach?  
- Jak długo trzymać warianty A/B?  
- Jak łączyć metryki online z ankietami jakości?

## Powiązania (meta)

- Key Documents: search_product_vision, search_api_documentation, zero_results_monitoring, query_success_rate, experimentation_playbook, rollback_runbook.  
- Key Document Structures: harmonogram, metryki, eksperymenty, konfiguracje, rollout, monitoring.  
- Document Dependencies: search engine config (ES/Solr/vector), feature store, experimentation platform, monitoring/dashboards.


## Zależności dokumentu

Wymaga: metryk bazowych i celów, logów zapytań, danych etykietowanych/feedbacku, platformy A/B, możliwości rollbacku konfiguracji, dostępu do słowników/schematów. Brak = brak DoR.


## Fazy cyklu życia

- Planowanie harmonogramu i priorytetów.  
- Przygotowanie eksperymentów i danych.  
- Wykonanie A/B i analiza.  
- Rollout/rollback i monitoring.  
- Retrospektywa i aktualizacja backlogu.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (relevance/tuning/schedule)  
- query_success_rate, zero_results_monitoring, experimentation_playbook


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

1. Zaplanuj tygodniowe/miesięczne sloty tuningów.  
2. Wybierz hipotezy, przygotuj eksperymenty i dane.  
3. Uruchom A/B, analizuj metryki; decyzja rollout/rollback.  
4. Dokumentuj wyniki, aktualizuj konfiguracje i linkage_index.


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

- NDCG: Normalized Discounted Cumulative Gain.  
- Zero results rate: odsetek zapytań bez wyników.  
- Budget ruchu: procent ruchu przeznaczony na eksperyment.


## Przykłady użycia

- Tuning boostów popularności vs świeżość.  
- Dodanie synonimów dla branżowych zapytań.  
- Regulacja scoringu wektorowego i BM25 w hybrydzie.


## Ryzyka i ograniczenia

- Eksperymenty bez reprezentatywności → złe wnioski.  
- Brak rollback → utrzymana degradacja.  
- Zbyt częste zmiany → niestabilne metryki.  
- Niepełne logi → ślepe tuningi.


## Decyzje i uzasadnienia

- Kadencja tuningów i budżet ruchu.  
- Progi decyzji rollout/rollback.  
- Zakres logowania/segmentów.  
- Priorytetyzacja hipotez (impact/effort).


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

- Hipotezy ↔ Eksperymenty ↔ Rollout.  
- Metryki ↔ Monitoring ↔ Decyzje.  
- Słowniki/schematy ↔ Konfiguracja ↔ Regresja.


## Struktura sekcji

1) Cele i metryki trafności  
2) Harmonogram tuningów i budżet ruchu  
3) Backlog hipotez/eksperymentów  
4) Procedury A/B i kryteria sukcesu  
5) Konfiguracje (boost, synonimy, stopwords, scoring)  
6) Rollout/rollback i monitoring po wdrożeniu  
7) Raporty i DoR/DoD  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Kalendarz eksperymentów i właścicieli.  
- Definicje metryk (NDCG/CTR/zero results) i targetów.  
- Szablon eksperymentu (hipoteza, warianty, czas, wymagany ruch).  
- Procedura rollout/rollback konfiguracji.  
- Lista słowników/schematów do regularnej aktualizacji.  
- Raporty post-A/B i checklisty regresji.


## Wymagane streszczenia

- Executive summary: ostatnie i planowane tuningy, wyniki.  
- Skrót decyzji rollout vs rollback.


## Guidance (skrót)

- Eksperymentuj często, ale w małych zmianach; mierz konsekwentnie.  
- Używaj reprezentatywnych próbek zapytań i segmentów użytkowników.  
- Monitoruj zero results i degradacje metryk na bieżąco.  
- Aktualizuj słowniki/boosty iteracyjnie; rollback jeśli metryki spadają.  
- Dokumentuj decyzje i zmiany w linkage_index.  
- Synchronizuj z kalendarzem release search.


## Checklisty Definition of Ready (DoR)

- [ ] Metryki bazowe i cele ustalone.  
- [ ] Logi zapytań i dane etykietowane dostępne.  
- [ ] Platforma A/B i mechanizm rollback gotowe.  
- [ ] Właściciele i kalendarz tuningów uzgodnieni.  
- [ ] Słowniki/schematy do modyfikacji zidentyfikowane.


## Checklisty Definition of Done (DoD)

- [ ] Eksperyment zakończony; wyniki przeanalizowane.  
- [ ] Decyzja rollout/rollback wdrożona; monitoring OK.  
- [ ] Konfiguracje i słowniki zaktualizowane; regresja zaliczona.  
- [ ] Raport i linkage_index uzupełnione.  
- [ ] Backlog hipotez zaktualizowany.

