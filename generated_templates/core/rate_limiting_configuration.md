---
title: Rate Limiting Configuration
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Rate Limiting Configuration


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Środowiska: [dev/test/stage/prod]


## Cel dokumentu

Opisać praktyczną konfigurację rate limiting/throttling zgodną z wymaganiami biznesu i bezpieczeństwa, z planem rollout/rollback, testami i observability.


## Zakres i granice

- Zakres: polityki limitów (per klient/tenant/IP/endpoint/plan; burst vs sustained; read/write), algorytmy (token/leaky bucket, fixed/sliding window), warstwa egzekwowania (gateway/mesh/app), nagłówki i komunikaty (RateLimit-*, Retry-After), wyjątki/override/waiver, observability (metryki/alerty), testy i rollout.
- Poza zakresem: definicja wymagań biznesowych (w `api_rate_limiting_requirements.md`), runbook incydentów (`obsluga_incydentow_rate_limit.md`).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: wymagania, projekt/ADR, inwentarz systemów/danych, okna wdrożeniowe, zasoby.
- Wyjścia: plan wdrożenia, skrypty/konfiguracje, walidacja/testy, plan rollback, lista ryzyk i właścicieli.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Przygotowanie/migracja danych.
- Rollout (pilot → fala → pełne wdrożenie).
- Walidacja i smoke testy.
- Stabilizacja/monitoring i przekazanie do operacji.
## Struktura sekcji (szkielet)

1. Polityki i wartości (per klient/endpoint/plan, burst/sustained, read/write).
2. Algorytmy i storage (token/leaky bucket, fixed/sliding; redis/in‑memory; clock sync).
3. Warstwa egzekwowania (gateway vs mesh vs app; fail‑open/closed; shadow mode).
4. Nagłówki/komunikaty i UX klienta (RateLimit-*, Retry-After, 429/503 semantyka, dokumentacja).
5. Wyjątki, tier’y i override (allowlist, czasowe podniesienia, approvals, waiver log).
6. Observability i alerty (metryki near-breach/breach, 429/503, latency overhead, sampling).
7. Testy i rollout (canary, chaos/flood, contract tests limitów, backoff klienta, rollback plan).
8. Załączniki (policy files, przykłady config, ADR/waiver log).


## Szybkie powiązania
- wymagania-rate-limiting
- rate-limiting-strategy
- rate-limiting-implementation
- konfiguracja-rate-limiting
- api-rate-limiting-requirements

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

- Na bazie wymagań wypełnij sekcje 1–3, odwzorowując limity w configu gateway/mesh.
- Skonfiguruj nagłówki, metryki/alerty (sekcje 4–6); przygotuj testy i rollout (sekcja 7).
- Udokumentuj wyjątki/overrides; zaktualizuj quick links i checklisty w `reports/checklist_atomic.jsonl`.


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

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

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

## Wejścia

- Tabele limitów/planów, profile ruchu, architektura gateway/mesh, polityka wyjątków, wymagania nagłówków, środowiska testowe, budżet opóźnień.


## Wyjścia

- Polityki jako kod (config dla gateway/mesh), wybór algorytmów i storage, nagłówki/komunikaty, dashboardy/alerty, plan rollout/kanary, aktualizacje w `linkage_index.jsonl`.



## Szybkie powiązania (uzupełnij po zlinkowaniu)

- [ ] `linkage_index.jsonl` → `api_rate_limiting_requirements.md`, `obsluga_incydentow_rate_limit.md`
- [ ] `linkage_index.jsonl` → `public_api_gateway.md`, `logging_and_audit_trail.md`
- [ ] `linkage_index.jsonl` → `api_change_communication.md`, `audit_logging.md`


## Wymagane rozwinięcia / streszczenia

- Mapowanie limitów na config (bucket size, refill rate, window) i przykłady odpowiedzi 429/503.
- Procedura override/waiver z automatycznym wygaśnięciem i logiem.
- Streszczenie ryzyk (hot endpoints/clients, koszt/latencja) i planu rollout/rollback.


## Wymagane powiązania

- Gateway/WAF/mesh, distributed cache (Redis/memcache), IdP/tenant registry, CI/CD, telemetry stack.
- Waiver log, status page, dokumentacja klienta (backoff/idempotency).


## Kryteria DoR (Definition of Ready)

- [ ] Tabele limitów/planów i architektura gateway/mesh znane; środowisko testowe dostępne.
- [ ] Polityka wyjątków/overrides i format nagłówków uzgodnione.


## Kryteria DoD (Definition of Done)

- [ ] Polityki/algorytmy skonfigurowane, nagłówki poprawne, observability działa; quick links uzupełnione.
- [ ] Rollout/testy (canary/chaos/contract) zaplanowane lub wykonane; overrides mają log/expiry.
- [ ] Status/metadane aktualne; checklisty DoR/DoD odhaczone.


## Artefakty do załączenia

- Pliki policy-as-code, config gateway/mesh, przykładowe nagłówki, dashboardy/alerty, wyniki testów flood/chaos, ADR/waiver log.


## Walidacja / testy

- Symulacje ruchu (spikes, abusive patterns), testy kontraktowe limitów, shadow/canary.
- Walidacja nagłówków RateLimit/Retry-After; test klienta (jitter/backoff).
- Przegląd bezpieczeństwa i kosztów (latencja, cache hit, blokady).


## Metryki monitorowane

- % requestów w limitach, liczba 429/503 na 1k req, latency overhead per gateway.
- Near-breach alert rate, liczba override/waiver, skuteczność alertów.


## Utrzymanie i aktualizacje

- Przegląd kwartalny limitów/progów i konfiguracji storage; aktualizacja przy zmianie planów/SLA.
- Rejestr zmian w `reports/change_log.jsonl`; synchronizacja z gateway/WAF config.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, odhacz checklisty, dodaj powiązania w `linkage_index.jsonl` oraz wpis w `reports/checklist_atomic.jsonl`.
