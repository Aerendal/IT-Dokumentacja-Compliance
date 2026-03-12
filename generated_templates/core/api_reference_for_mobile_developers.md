---
title: API Reference for Mobile Developers
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# API Reference for Mobile Developers


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnić mobilnym deweloperom spójne, stabilne i bezpieczne użycie API: kontrakty, autoryzacja, limity, wersjonowanie, formaty odpowiedzi/błędów oraz przykłady implementacji. Minimalizuje regresje i różnice między platformami iOS/Android.


## Zakres i granice

- Obejmuje: endpointy mobilne, auth (OAuth2/OIDC, PKCE), rate limiting, wersjonowanie, formaty payloadów (JSON/protobuf), obsługę błędów i retry, paginację/filtry, caching, offline/edge cases, telemetry (logs/metrics), bezpieczeństwo (cert pinning, TLS), testy kontraktów.  
- Poza zakresem: pełne wytyczne UI/UX, SDK build system, backend wewnętrzna architektura.


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia

- Wejścia: specyfikacje OpenAPI/GraphQL, polityka auth, limity, wymagania mobilne (offline, sieć niestabilna), kody błędów, przykładowe flow.  
- Wyjścia: referencja endpointów z przykładami, tablice kodów błędów, zalecenia caching/offline, sample requests w cURL/Kotlin/Swift, checklisty DoR/DoD kontraktu, matryca kompatybilności wersji.


## Założenia

- Gateway wspiera OIDC/OAuth2 + rate limiting.  
- Monitoring klienta (crash/metrics) jest dostępny.  
- Użytkownicy stosują najnowsze SDK lub mają ścieżkę migracji.


## Otwarte pytania

- Jak długo wspieramy starsze wersje API/SDK?  
- Czy potrzebna jest lokalizacja komunikatów błędów po stronie klienta?  
- Jaki poziom telemetry jest wymagany a co jest opcjonalne?  
- Jak obsługiwać tryb offline przy wymaganym tokenie (grace window)?

## Powiązania (meta)

- Key Documents: api_versioning_maintenance, authentication_metrics_report, mobile_security_guidelines, error_handling_standards, monitoring_strategy_document, client_release_checklist.  
- Key Document Structures: auth, kontrakty, błędy, wydajność/offline, wersjonowanie, testy.  
- Document Dependencies: API gateway, IdP, rate limiter, monitoring/analytics, schema registry.


## Zależności dokumentu

Wymaga aktualnej specyfikacji API, polityki auth, limitów, listy wspieranych wersji mobilnych SDK, środowisk testowych/stage, oraz dostępnych przykładów kontraktów. Braki = brak DoR.


## Fazy cyklu życia

- Definicja kontraktów i wersji.  
- Implementacja klienta i testy kontraktów.  
- Wydanie i monitorowanie.  
- Deprecacje/migracje i komunikacja.



## Struktura sekcji (szkielet)
1. Konwencje (URL, auth, nagłówki, daty, waluty, timezones).
2. Wersjonowanie i kompatybilność (URI vs nagłówek, breaking/non-breaking).
3. Endpointy (opis, parametry, body, odpowiedzi, statusy, idempotencja).
4. Błędy i retry (kody, komunikaty, polityka backoff, offline queue).
5. Limity i wydajność (rate limits, payload size, cache, compression).
6. Przykłady użycia (curl, Kotlin coroutines, Swift async/await).
7. Testy i walidacja (contract tests, mocked server, Postman/Insomnia).
8. Bezpieczeństwo (cert pinning, TLS, PII redaction w logach).
## Szybkie powiązania

- linkage_index.jsonl (api/reference/mobile)  
- api_versioning_maintenance, mobile_security_guidelines, error_handling_standards


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **OWASP ASVS** — Standard Weryfikacji Bezpieczeństwa Aplikacji (OWASP)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **OWASP MASVS** — Standard Weryfikacji Bezpieczeństwa Aplikacji Mobilnych (OWASP)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
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

1. Sprawdź wymagania auth i limity; skonfiguruj klienta.  
2. Implementuj endpointy wg przykładów; dodaj obsługę błędów/retry.  
3. Uruchom testy kontraktów i a11y sieci (offline/slaba sieć).  
4. Publikuj aplikację; monitoruj metryki i aktualizuj przy zmianach API.


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

- PKCE: rozszerzenie OAuth2 dla aplikacji publicznych.  
- ETag: nagłówek do walidacji cache.  
- Pinning: weryfikacja certyfikatu serwera przez klienta.


## Przykłady użycia

- Pobieranie feedu produktów z cache i walidacją ETag.  
- Odnawianie tokenu po 401 + retry z backoff.  
- Migracja z v1 na v2 endpointu z polami deprecated.


## Ryzyka i ograniczenia

- Brak pinning → ryzyko MITM.  
- Niespójne błędy → trudna diagnostyka i UX.  
- Agresywne retry → blokady rate limiting.  
- Brak wersjonowania → breaking changes w aplikacjach produkcyjnych.


## Decyzje i uzasadnienia

- Wersjonowanie (path vs header) i okno deprecacji.  
- Strategie cache/offline i limity retry.  
- Zestaw wymaganych nagłówków (request-id, locale, app-version).  
- Format błędów (np. RFC 7807) i logowania klienta.


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

- Auth ↔ Bezpieczeństwo klienta (pinning) ↔ Błędy/retry.  
- Wersjonowanie ↔ Kompatybilność SDK ↔ Migracje.  
- Rate limiting ↔ Retry/backoff ↔ Monitoring.


## Struktura sekcji

1) Auth i bezpieczeństwo klienta (OAuth2/OIDC, PKCE, pinning)  
2) Kontrakty endpointów (metody, parametry, schematy, przykłady)  
3) Błędy i retry (kody, komunikaty, backoff)  
4) Wersjonowanie, zgodność i migracje  
5) Wydajność i offline (cache, batching, timeouts)  
6) Telemetria i monitoring na kliencie  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Tabela endpointów z przykładami (cURL/Swift/Kotlin).  
- Matryca kodów błędów i zachowań klienta.  
- Polityka wersjonowania (header/path) i deprecacji.  
- Rekomendacje cache/offline (ETag/If-None-Match, store-and-forward).  
- Konfiguracja pinning TLS i rotacja certów.  
- Testy kontraktów (schemat vs payload) w CI.


## Wymagane streszczenia

- Executive summary: wersja API, wymagany poziom SDK, kluczowe zmiany.  
- Skrót limitów i polityki retry/backoff.


## Guidance (skrót)

- Używaj PKCE i odświeżania tokenów bez przechowywania haseł.  
- Stosuj stałe schematy błędów; nie polegaj na tekstach komunikatów.  
- Dodaj telemetry (request ID, latency) i centralny logging błędów klienta.  
- Wymuszaj TLS 1.2+ i pinning; rotuj piny przed wygaśnięciem.  
- Przy sieci słabej stosuj cache, kolejkę offline i exponential backoff.  
- Trzymaj kompatybilność: nie usuwaj pól, tylko oznaczaj jako deprecated.


## Checklisty Definition of Ready (DoR)

- [ ] Specyfikacja API aktualna i dostępna.  
- [ ] Limity i polityka auth potwierdzone.  
- [ ] Wersje SDK/OS wspierane zdefiniowane.  
- [ ] Strategie błędów/retry/cache ustalone.  
- [ ] Środowiska test/stage i dane testowe gotowe.


## Checklisty Definition of Done (DoD)

- [ ] Endpointy zaimplementowane i pokryte testami kontraktów.  
- [ ] Obsługa błędów/retry zgodna z tabelą.  
- [ ] Pinning TLS i polityka tokenów zaimplementowane.  
- [ ] Monitoring klienta wysyła metryki/logi; brak krytycznych błędów.  
- [ ] Dokumentacja i linkage_index zaktualizowane.

