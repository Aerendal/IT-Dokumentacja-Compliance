---
title: Integration Patterns
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Integration Patterns


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przedstawić i ustandaryzować wzorce integracyjne (sync/async, messaging, eventing, batch), aby zespoły wybierały właściwy model zgodnie z wymaganiami wydajności, spójności i niezawodności.


## Zakres i granice

- Obejmuje: request/response, webhook, pub/sub, event sourcing, CQRS, batch/ETL, file-based, CDC, idempotencję i retry, schematy kontraktów, wersjonowanie, observability, bezpieczeństwo, wybór wzorca do scenariusza.  
- Poza zakresem: szczegółowa implementacja konkretnego systemu (oddzielne HLD).


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia

- Wejścia: wymagania systemów, SLA, spójność danych, latencja, wolumen, istniejące platformy (API gateway, broker, ETL), polityki bezpieczeństwa.  
- Wyjścia: katalog wzorców, kryteria wyboru, checklisty DoR/DoD, przykłady implementacji, matryca scenariusz→wzorzec, rekomendacje narzędzi.


## Założenia

- Dostępne są brokers/API gateway i registry.  
- Zespół zna standardy.  
- Monitoring działa end-to-end.


## Otwarte pytania

- Jak obsłużyć migracje wzorców (np. batch → async)?  
- Jakie SLO dla każdego wzorca?  
- Czy partnerzy akceptują podpisy/kontrakty?

## Powiązania (meta)

- Key Documents: integration_support_procedure, api_versioning_maintenance, data_source_integration_reference, rollback_runbook, security_controls_reference, communication_failure.  
- Key Document Structures: wzorce, kryteria, kontrakty, bezpieczeństwo, observability.  
- Document Dependencies: API gateway, message broker, schema registry, monitoring, ETL platform.


## Zależności dokumentu

Wymaga: listy scenariuszy i SLA, dostępnych platform integracyjnych, polityk bezpieczeństwa i wersjonowania, standardów kontraktów, narzędzi monitoringu. Brak = brak DoR.


## Fazy cyklu życia

- Definicja wzorców i kryteriów.  
- Mapowanie scenariuszy.  
- Implementacja referencyjnych przykładów.  
- Review i aktualizacje.  
- Ewangelizacja i szkolenia.



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

- linkage_index.jsonl (integration/patterns)  
- integration_support_procedure, data_source_integration_reference


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

1. Określ wymagania (latencja, spójność, wolumen).  
2. Wybierz wzorzec z matrycy; sprawdź checklisty.  
3. Zaprojektuj kontrakt i observability; ustaw retry/idempotencję.  
4. Zaimplementuj i przetestuj; zaktualizuj dokument i linkage_index.


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

- Wzorce ↔ Kryteria wyboru ↔ Matryca scenariusz→wzorzec.  
- Idempotencja/retry ↔ Bezpieczeństwo ↔ Observability.  
- Kontrakty ↔ Wersjonowanie ↔ Backward compatibility.


## Struktura sekcji

1) Kryteria wyboru (latencja, spójność, wolumen, SLA)  
2) Wzorce sync/async (HTTP/gRPC, pub/sub, queue, webhook, CDC, batch)  
3) Kontrakty i wersjonowanie (schema registry, semver)  
4) Idempotencja, retry, backoff, DLQ  
5) Observability (trace/log/metric), testy integracyjne  
6) Bezpieczeństwo (auth, podpisy, rate limit, PII)  
7) Matryca scenariusz→wzorzec + przykłady  
8) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Opisy wzorców z plusami/minusami.  
- Przykłady payloadów/kontraktów i testów.  
- Polityki retry/backoff i idempotent keys.  
- Schemat observability (trace IDs, correlation).  
- Szablony dla nowych integracji.  
- FAQ: kiedy wybrać który wzorzec.


## Wymagane streszczenia

- Executive summary: dostępne wzorce i kiedy używać.  
- Skrót kryteriów wyboru.


## Guidance (skrót)

- Wybieraj async dla dużych wolumenów/opóźnień; sync dla niskiej latencji.  
- Wymuszaj kontrakty w schema registry; wersjonuj bez breaking.  
- Idempotencja + retry to standard; testuj failure modes.  
- Mierz end-to-end (trace); loguj correlation IDs.  
- Bezpieczeństwo: auth, podpisy webhooków, rate limiting.  
- Aktualizuj linkage_index po dodaniu wzorca.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania SLA/spójności i scenariusz znane.  
- [ ] Platformy integracyjne dostępne.  
- [ ] Kontrakt/schemat i polityka wersji określone.  
- [ ] Plan observability i bezpieczeństwa gotowy.  
- [ ] Retry/idempotencja zaplanowane.


## Checklisty Definition of Done (DoD)

- [ ] Wzorzec zaaplikowany; testy integracyjne zielone.  
- [ ] Observability i alerty działają.  
- [ ] Kontrakty w registry; wersje opisane.  
- [ ] linkage_index zaktualizowany.  
- [ ] Dokumentacja i przykłady opublikowane.

