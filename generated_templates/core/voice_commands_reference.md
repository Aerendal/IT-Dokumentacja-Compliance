---
title: Voice Commands Reference
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Voice Commands Reference


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Udokumentować zestaw obsługiwanych komend głosowych, intencji, slotów i wariantów językowych wraz z odpowiedziami, stanami i ograniczeniami, by zapewnić spójne doświadczenie i ułatwić rozwój/utrzymanie asystenta głosowego.


## Zakres i granice

- Obejmuje: lista intencji i przykładowych wypowiedzi (utterances), sloty i typy, stany dialogu, odpowiedzi i błędy, polityki potwierdzeń, fallback i rozpoznawanie, języki/akcenty, dostępność (bariera mowy/hałas), telemetry/feedback, wersjonowanie i publikację komend.  
- Poza zakresem: niskopoziomowy ASR/TTS tuning (oddzielne dokumenty), UI ekranowe.


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia

- Wejścia: definicje intencji, dane treningowe, wymagania biznesowe, języki docelowe, polityki bezpieczeństwa/konfidencji, wytyczne UX, metryki jakości (ASR/intent), dane o błędach.  
- Wyjścia: katalog komend/intencji, specyfikacja slotów/typów, przykłady utterances, reguły odpowiedzi i błędów, DoR/DoD, plan testów regresji, wersjonowanie/publikacja.


## Założenia

- ASR/NLU infrastruktura dostępna.  
- Zespół ma dane treningowe i pipeline publikacji.  
- Telemetria jakości dostępna.


## Otwarte pytania

- Jak obsłużyć dialekty/akcenty per region?  
- Jak długo przechowywać logi audio/tekstowe?  
- Czy potrzebny jest tryb prywatny (bez logowania treści)?

## Powiązania (meta)

- Key Documents: nlp_model_monitoring_runbook, api_reference_for_mobile_developers, accessibility_improvement_plan, error_handling_standards, localization_guidelines.  
- Key Document Structures: intencje/utterances, sloty, stany, odpowiedzi, błędy/fallback, wersjonowanie.  
- Document Dependencies: NLU/NLP platform, ASR/TTS, analytics, localization/i18n, CI/CD voice model.


## Zależności dokumentu

Wymaga: listy intencji i wymagań biznesowych, metryk jakości ASR/NLU, narzędzi do lokalizacji, polityki bezpieczeństwa (np. dane wrażliwe), środowisk testowych i pipeline publikacji modeli. Braki = brak DoR.


## Fazy cyklu życia

- Definicja i projekt intencji/slotów.  
- Implementacja i trening.  
- Testy jakości i regresji.  
- Publikacja i monitoring.  
- Aktualizacje i lokalizacje.



## Struktura sekcji (szkielet)
- Kontekst i NFR.
- Diagramy (C4 lub inne) i wersje.
- Decyzje architektoniczne (ADR) i uzasadnienia.
- Standardy (security, observability, CI/CD, data).
- Zależności zewnętrzne i kontrakty.
- Wersjonowanie artefaktów i repo.
- Plan przeglądów i checklisty.
- Ryzyka i mitigacje.
## Szybkie powiązania

- linkage_index.jsonl (voice/commands/reference)  
- localization_guidelines, error_handling_standards, nlp_model_monitoring_runbook


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

1. Dodaj/edytuj intencje i sloty; zaktualizuj przykłady.  
2. Przeprowadź testy regresji i walidację jakości.  
3. Opublikuj nową wersję z notką release; monitoruj metryki.  
4. Utrzymuj katalog aktualny; aktualizuj linkage_index.


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

- Intent: cel użytkownika rozpoznany przez NLU.  
- Slot: parametr/argument intencji.  
- WER: Word Error Rate (ASR).


## Przykłady użycia

- Sterowanie odtwarzaniem (play/pause/next).  
- Pytania o pogodę z lokalizacją.  
- Rezerwacja stołu z datą/godziną/liczbą osób.


## Ryzyka i ograniczenia

- Wysoki WER → błędne intencje.  
- Brak walidacji slotów → niepełne lub niebezpieczne akcje.  
- Brak lokalizacji → słaba jakość w innych językach/akcentach.  
- Zmiany bez regresji → regresje UX.


## Decyzje i uzasadnienia

- Kryteria jakości (WER/intent) przed releasem.  
- Zakres potwierdzeń i fallbacków.  
- Polityka rollout (canary/A-B).  
- Zakres logowania i anonimizacji.


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

- Intencje ↔ Sloty ↔ Odpowiedzi.  
- Wersjonowanie ↔ Testy regresji ↔ Publikacja.  
- Bezpieczeństwo ↔ Dane wrażliwe ↔ Fallback/confirm.


## Struktura sekcji

1) Katalog intencji i utterances (per język)  
2) Sloty i typy (enum, free text, constrained)  
3) Stany dialogu i reguły odpowiedzi/confirm/fallback  
4) Błędy i polityki bezpieczeństwa (dane wrażliwe, niepełne dane)  
5) Testy regresji i kryteria jakości  
6) Wersjonowanie i publikacja komend  
7) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Tabela intencji z przykładami wypowiedzi (per język/akcent).  
- Definicje slotów i walidatorów; polityka domyślnych wartości.  
- Reguły odpowiedzi i confirm; komunikaty błędów/fallback.  
- Testy regresji (ASR WER, intent accuracy), scenariusze edge.  
- Polityka wersjonowania i rollout (A/B, canary).  
- Telemetria: co logować, progi alertów jakości.


## Wymagane streszczenia

- Executive summary: zasięg komend, języki, metryki jakości.  
- Skrót zmian między wersjami (release notes).


## Guidance (skrót)

- Projektuj komendy prosto; wspieraj parafrazy i różne akcenty.  
- Waliduj sloty i proś o potwierdzenia dla krytycznych akcji.  
- Wprowadzaj wersje stopniowo; mierz jakość i błędy użytkowników.  
- Zgodność z dostępnością: jasne komunikaty, powtórzenia przy szumie.  
- Chronić dane wrażliwe; wycisz logi, gdy pojawiają się PII.  
- Aktualizuj katalog i linkage_index po każdym releasie.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania biznesowe i lista intencji zebrane.  
- [ ] Sloty/typy i walidacje zdefiniowane.  
- [ ] Języki/akcenty i lokalizacja ustalone.  
- [ ] Środowiska/testy regresji przygotowane.  
- [ ] Polityka bezpieczeństwa logów/PII uzgodniona.


## Checklisty Definition of Done (DoD)

- [ ] Intencje/sloty wdrożone; testy regresji zielone.  
- [ ] Komunikaty błędów/fallback zgodne ze standardem.  
- [ ] Release opublikowany; metryki monitorowane.  
- [ ] Dokument i linkage_index zaktualizowane; notki release opublikowane.  
- [ ] Brak otwartych krytycznych defektów jakości.

