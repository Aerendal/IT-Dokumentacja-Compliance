---
title: API Reference Mobile
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# API Reference Mobile


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Jedno źródło prawdy dla backend API używanego przez aplikacje mobilne (Android/iOS): endpointy, parametry, błędy, limity, wersjonowanie i przykłady użycia.


## Zakres i granice

- Obejmuje: REST/GraphQL/gRPC dla mobile, auth (OAuth/JWT), paginacja, retry, ograniczenia sieci mobilnej, przykłady request/response, kody błędów.
- Nie obejmuje: logiki klienckiej UI, guideline UX, pełnych specyfikacji backendu web (te w „API Reference Web”).


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia

- Wejścia: kontrakty usług, modele domenowe, decyzje architektoniczne, wymagania bezpieczeństwa, limity rate limit.
- Wyjścia: opis endpointów, schematy pól, sekcja „Jak obsłużyć błąd X”, matryca kompatybilności wersji, przykłady kodu (curl, Kotlin, Swift).


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

- Security Requirements (auth, token refresh, cert pinning).
- Mobile Release Checklist (co wymaga aktualizacji przy zmianie API).
- SLA / SLO usług backendowych.
- Error Handling Guide & Logging/Tracing Guidelines.


## Fazy cyklu życia

- Projekt/Design: uzgodnienie kontraktów, typów, wersji.
- Implementacja: stabilizacja payloadów, testy kontraktowe.
- Testy/QA: testy integracyjne mobile-backend, chaos/retry na słabym łączu.
- Wdrożenie: publikacja changelog, deprecacja starych wersji.
- Operacje: monitoring, rate-limit alerts, backward compatibility.



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

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


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

- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.



## Checklisty jakości

- [ ] Wersjonowanie opisane, z polityką deprecacji.
- [ ] Endpointy kompletne: parametry, typy, przykłady request/response.
- [ ] Kody błędów i polityka retry/backoff zdefiniowane.
- [ ] Sekcja bezpieczeństwa: auth, TLS, cert pinning, PII w logach.
- [ ] Przykłady kodu dostępne dla Android/iOS i curl.


## Definicje robocze

- **Idempotencja** — powtórzenie żądania nie zmienia stanu (np. PUT z `Idempotency-Key`).
- **Rate limit** — ograniczenie liczby żądań; klient musi reagować na 429 i stosować backoff.
- **Backward compatibility** — nowa wersja nie psuje istniejących klientów; breaking changes muszą mieć migrację.

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

- „Endpointy” **defines_structure** „Przykłady użycia”.
- „Wersjonowanie” **constrains** „Deprecation policy”.
- „Błędy i retry” **guides_expansion** „Obsługa offline/edge cases”.


## Wymagane rozwinięcia

- Dla każdego endpointu: idempotencja, scenariusze błędów, zachowanie przy utracie sieci.
- Dla wersjonowania: jak długo wspieramy poprzednią wersję i ścieżka migracji.


## Wymagane streszczenia

- Krótka „Quickstart” dla nowych deweloperów mobile.
- Tabela różnic między wersjami API (breaking vs non-breaking).


## Guidance

Cel: skrócone wskazówki do wypełniania szablonów dokumentów (core/satellite).

- Cel dokumentu: 2–3 zdania o decyzjach, ryzykach i wartości dokumentu.
- Zakres i granice: co obejmuje (systemy/procesy/zespoły) i czego nie obejmuje; zaznacz granice odpowiedzialności.
- Wejścia: dane, wymagania, standardy, zależności potrzebne przed startem.
- Wyjścia: artefakty/rezultaty, kto je konsumuje, format (link/plik).
- Zależności dokumentu: wymagane dokumenty lub decyzje; właściciel; wpływ na kolejność prac.
- Powiązania sekcja↔sekcja: które sekcje się rozwijają/streszczają; podaj uzasadnienie.
- Struktura sekcji: utrzymuj układ logiczny; sekcje bez treści oznacz jako N/A z krótkim uzasadnieniem.
- Fazy cyklu życia: zaznacz, w których fazach dokument powstaje/aktualizuje się/archiwizuje; kto odpowiada.
- DoR (Definition of Ready): zakres, wejścia, role, zależności, kryteria akceptacji gotowe.
- DoD (Definition of Done): sekcje uzupełnione lub N/A, powiązania wpisane, checklisty jakości sprawdzone, wersja/data/właściciel, linki/artefakty działają.
- Język: polski; nazwy własne pozostają bez zmian; liczby w nazwach plików usunięte już w szablonach.
- Filozofia: optymalizuj przez rozwój, nie ucinanie — dodawaj, nie kasuj; elementy „satelitarne” zostają.

ontraktowe przechodzą.

