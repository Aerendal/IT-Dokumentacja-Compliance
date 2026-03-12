---
title: Integration Failure
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Integration Failure


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać typowe scenariusze awarii integracji (API, kolejki, ETL, webhooki, pliki, partnerzy), ich symptomy, diagnostykę, obejścia, naprawę i zapobieganie, aby skrócić MTTR i ograniczyć wpływ na użytkowników.


## Zakres i granice

- Obejmuje: błędy transportu (timeout, TLS, DNS), kontraktu (schemat, brak pól), limity/rate limiting, idempotencję i duplikaty, kolejki/backpressure, transformacje ETL, harmonogramy, wersjonowanie API, auth/klucze, monitoring i alerty, runbooki rollback/retry.  
- Poza zakresem: projektowanie nowych integracji (osobny dokument), strategiczne umowy partnerskie (osobne materiały).


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia

- Wejścia: logi i metryki integracji, schematy kontraktów, SLA, konfiguracje retry/backoff, alerty, dane o zmianach partnera, runbooki, status systemów zależnych.  
- Wyjścia: katalog awarii i ich runbooki, checklisty diagnostyczne, macierz przyczyn/rozwiązań, rekomendacje zapobiegawcze, plan komunikacji, DoR/DoD.


## Założenia

- Monitoring i registry działają.  
- Partnerzy mają SLA i kanały eskalacji.  
- Systemy wspierają idempotentne operacje.


## Otwarte pytania

- Jakie integracje są krytyczne 24/7 vs biurowe?  
- Czy potrzebne są testy syntetyczne dla każdej integracji?  
- Jak długo trzymać logi/zdarzenia do RCA?

## Powiązania (meta)

- Key Documents: service_dependency_map, rollback_runbook, api_versioning_maintenance, error_handling_standards, data_source_integration_reference, communication_failure.  
- Key Document Structures: typ awarii, symptomy, diagnostyka, naprawa, zapobieganie, komunikacja.  
- Document Dependencies: monitoring/logging, schema registry, API gateway, queue/broker, ETL/ELT, ticketing/status page.


## Zależności dokumentu

Wymaga: aktualnych kontraktów API, konfiguracji retry/backoff, listy zależności i wersji, dostępu do logów/monitoringu, polityk komunikacji z partnerami, statusu środowisk. Braki = brak DoR.


## Fazy cyklu życia

- Detekcja i klasyfikacja awarii.  
- Diagnostyka i obejście.  
- Naprawa/rollback; komunikacja.  
- Walidacja i przywrócenie.  
- Post‑mortem i działania zapobiegawcze.



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

- linkage_index.jsonl (integration/failure)  
- api_versioning_maintenance, rollback_runbook, communication_failure


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

1. Zidentyfikuj typ awarii i skorzystaj z checklisty diagnostycznej.  
2. Zastosuj obejście/rollback i komunikację do partnerów/klientów.  
3. Napraw przyczynę, waliduj testami kontraktów.  
4. Zaktualizuj runbook, alerty i linkage_index; wykonaj post‑mortem.


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

- Idempotent key: klucz zapobiegający duplikatom przy retry.  
- Backpressure: ograniczenie przetwarzania przy zbyt dużym napływie danych.  
- Breaking change: zmiana kontraktu niezgodna wstecznie.


## Przykłady użycia

- Partner wprowadził nowe pole wymagane → 400 w produkcji.  
- Kolejka Kafka ma rosnący lag po deployu → throttling konsumentów.  
- Webhooki timeoutują przez blokadę firewall → fallback na kolejkę.


## Ryzyka i ograniczenia

- Brak testów kontraktów → częste regresje.  
- Złe retry → duplikaty transakcji.  
- Brak kanału eskalacji z partnerem → długie przestoje.  
- Nieznane zależności → efekt domina.


## Decyzje i uzasadnienia

- Progi alertów i retry/backoff.  
- Które integracje mają tryb degradacji/łagodzenia.  
- Kryteria rollback vs hotfix.  
- Zakres komunikacji do klientów/partnerów.


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

- Symptomy ↔ Diagnostyka ↔ Naprawa ↔ Zapobieganie.  
- Limit/rate ↔ Retry/backoff ↔ Idempotencja.  
- Zmiany kontraktów ↔ Wersjonowanie ↔ Komunikacja partnera.


## Struktura sekcji

1) Typy awarii i symptomy  
2) Checklisty diagnostyczne per typ  
3) Naprawa/obejścia/rollback  
4) Zapobieganie i twardnienie integracji  
5) Komunikacja (partnerzy/klienci)  
6) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Matryca: typ awarii → symptomy → metryki/logi → akcje.  
- Szablon checklisty dla API, kolejek, ETL, webhooków.  
- Polityka retry/backoff i idempotentnych kluczy.  
- Procedura awaryjna dla breaking change partnera.  
- Plan testów kontraktów i monitoringu syntetycznego.  
- Szablony komunikatów do partnerów/klientów.


## Wymagane streszczenia

- Executive summary: aktywne/ostatnie awarie, MTTR, główne przyczyny.  
- Skrót zależności i podatnych integracji.


## Guidance (skrót)

- Utrzymuj kontrakty w registry i testy kontraktowe w CI.  
- Stosuj idempotentne klucze i deduplikację dla retry.  
- Ustaw alerty na anomalie (timeouty, error rate, lag).  
- Miej fallback kanał komunikacji z partnerem; eskaluj przy breaking changes.  
- Po incydencie aktualizuj runbooki i progi alertów.


## Checklisty Definition of Ready (DoR)

- [ ] Kontrakty i wersje API aktualne w registry.  
- [ ] Dostęp do logów/monitoringu i metryk.  
- [ ] Konfiguracje retry/backoff i idempotencji znane.  
- [ ] Lista partnerów i kanałów komunikacji gotowa.  
- [ ] Runbooki rollback/testy kontraktów dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Awarie usunięte; metryki w normie.  
- [ ] Przyczyna źródłowa znana; działania zapobiegawcze zapisane.  
- [ ] Komunikaty wysłane; status/ticket zamknięty.  
- [ ] Testy kontraktów dodane/aktualne; alerty dostrojone.  
- [ ] linkage_index/CMDB zaktualizowane.

