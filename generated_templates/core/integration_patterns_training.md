---
title: Integration Patterns Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Integration Patterns Training


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Przygotować program szkoleniowy z wzorców integracyjnych (API/event/ETL/ESB), aby zespoły stosowały spójne podejście do integracji systemów.


## Zakres i granice

- Obejmuje: patterny (request/response, pub-sub, CQRS, event sourcing, batch/stream, saga/choreography/orchestration, idempotencja, retry, dead-letter), kontrakty API i eventy, bezpieczeństwo, monitoring, testy integracyjne, narzędzia (gateway, ESB, message broker).
- Poza zakresem: szczegółowe projekty pojedynczych integracji (osobne).


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia

- Wejścia: katalog integracji w organizacji, standardy API/event, narzędzia (gateway/broker/ETL), wymagania bezpieczeństwa/PII, przykłady defektów.
- Wyjścia: sylabus modułów, materiały i laby, checklisty DoR/DoD, scenariusze ćwiczeń (API/event/batch), kryteria oceny, harmonogram sesji.


## Założenia
- Dostępne są brokers/API gateway i registry.  
- Zespół zna standardy.  
- Monitoring działa end-to-end.
## Otwarte pytania
- Jak obsłużyć migracje wzorców (np. batch → async)?  
- Jakie SLO dla każdego wzorca?  
- Czy partnerzy akceptują podpisy/kontrakty?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: standardy integracji, katalog integracji, narzędzia, polityki security/PII, monitoring, testy; brak – odnotuj.


## Fazy cyklu życia

Plan → Materiały/laby → Sesje → Ocena → Utrzymanie programu.



## Struktura sekcji (szkielet)

- Cele i KPI szkolenia.
- Moduły (API patterns, event patterns, batch/ETL, reliability/retry/idempotency, security, monitoring/testing).
- Ćwiczenia i laby (gateway/broker/ETL).
- Narzędzia i środowiska.
- Ocena/certyfikacja i feedback.
- Plan utrzymania i aktualizacji.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
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

- Dostosuj moduły do grupy; przygotuj laby; przeprowadź sesje; oceń; aktualizuj program.


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
- DLQ: Dead Letter Queue.  
- CDC: Change Data Capture.  
- Correlation ID: identyfikator śledzenia żądań.
## Przykłady użycia
- Webhook + podpisy do powiadomień partnerów.  
- Pub/sub do rozsyłania eventów biznesowych.  
- Batch/CDC do synchronizacji danych referencyjnych.
## Ryzyka i ograniczenia
- Brak idempotencji → duplikaty.  
- Zły wzorzec → wysokie koszty lub opóźnienia.  
- Brak versioning → breaking changes.  
- Słaba observability → trudna diagnostyka.
## Decyzje i uzasadnienia
- Wybór wzorca per domena.  
- Polityka retry/backoff.  
- Standardy kontraktów i wersjonowania.  
- Zakres logów/traces.
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

Patterny → laby → ocena; bezpieczeństwo → PII; monitoring → testy.


## Wymagane rozwinięcia

- Laby → repo i dane.
- Checklisty → DoR/DoD integracji.


## Wymagane streszczenia

- One-pager: moduły, KPI, harmonogram.


## Guidance

Cel: wspólne wzorce integracji. DoR: standardy/narzędzia, katalog integracji, polityki PII. DoD: sylabus/laby/checklisty/ocena; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Standardy integracji i narzędzia; [ ] Katalog integracji; [ ] Polityki security/PII.
- DoD: [ ] Sylabus/laby/checklisty/ocena gotowe; [ ] Sekcje N/A uzasadnione; metadane aktualne.
