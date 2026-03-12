---
title: Generowanie dokumentacji API
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Generowanie dokumentacji API


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Automatyzować generowanie dokumentacji API z kontraktów (OpenAPI/AsyncAPI) i kodu, zapewniając spójność, aktualność i publikację.


## Zakres i granice

- Obejmuje: źródło prawdy (OpenAPI/AsyncAPI), pipeline generowania (docs site/portal), przykłady i SDK, wersjonowanie/deprecje, bezpieczeństwo (auth info, rate limits), testy kontraktowe, publishing (CI/CD), monitoring aktualności.  
- Poza zakresem: manualne guide’y, które nie wynikają z kontraktu.


## Użytkownicy i interesariusze
- HRIT/Platform, Security/Privacy, Integratorzy, Product, Compliance.
## Wejścia i wyjścia

- Wejścia: kontrakty API, standard błędów, polityki bezpieczeństwa/rate, przykłady kodu.  
- Wyjścia: wygenerowana dokumentacja (HTML/portal), changelog, artefakty CI, linki w linkage_index.



## Założenia
- IAM/IdP, logging/trace, sandbox i testy dostępne; polityki PII/SoD obowiązują.
## Otwarte pytania
- Jakie pola są krytyczne PII i jak je maskujemy w logach? 
- Jaki cykl deprecations i komunikacji?
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
- Przygotowanie: cele, zakres, założenia.
- Planowanie: sekwencja prac, zasoby, daty.
- Realizacja: monitoring postępu, decyzje go/stop.
- Zamknięcie: retrospektywa, aktualizacja planów.
## Struktura sekcji (szkielet)
- Stan obecny i metryki bazowe
- Cele i KPI (DX, SLO, bezpieczeństwo)
- Obszary usprawnień i backlog
- Plan wdrożeń i testów (canary, beta, kontrakty)
- Komunikacja i wersjonowanie
- Ryzyka i zależności
## Szybkie powiązania

- linkage_index.jsonl (api/docs_generation)  
- dokumentacja_api_openapi, api_change_communication, logging_strategy


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **OWASP ASVS** — Standard Weryfikacji Bezpieczeństwa Aplikacji (OWASP)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

1. Ustal kontrakt jako źródło prawdy; skonfiguruj lint/validate w CI.  
2. Zbuduj pipeline generate+publish; dodaj przykłady/SDK i polityki.  
3. Monitoruj drift i aktualizuj linkage_index/changelog po każdej zmianie.

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
- PII, SoD, OAuth2/SAML/JWT, Problem+JSON, Idempotency, Webhook signing.
## Przykłady użycia
- Pobranie danych pracownika (scopes ograniczone, pola PII maskowane).
- Webhook time-off approved: signed payload, retry/backoff, idempotency key.
## Ryzyka i ograniczenia
- Wycieki PII; brak SoD; zbyt luźne rate limits; brak deprecations komunikacji.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- API Security Baseline, Data Privacy Policy, SoD, Versioning Policy, Observability Standards, Incident Response Plan.
## Powiązania z sekcjami innych dokumentów
- Privacy → PII/maskowanie; Security → auth/rate limits; Observability → monitoring/audyt.
## Słownik pojęć w dokumencie
- PII, SoD, OAuth2, SAML, JWT, Problem+JSON, Idempotency, Webhook signing.
## Wymagane odwołania do standardów
- Polityki privacy/PII, SoD, API security, regulacje HR danych.
## Mapa relacji sekcja→sekcja
- Zasoby/PII → Auth/SoD → Rate/Webhooks → Monitoring/Audyt → Deprecations.
## Mapa relacji dokument→dokument
- HRIS API → Security/Privacy/Versioning/Observability → Incident/Change.
## Ścieżki informacji
- Wymagania → Spec → Testy/Sandbox → Monitoring → Deprecations.
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
- OpenAPI spec, przykłady, testy kontraktowe, config rate/webhooks, audyt/access logi.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- HRIT/Platform → Security/Privacy → Product/Compliance → Owner sign‑off.
## Metryki jakości
- Liczba błędów 4xx/5xx, czas odpowiedzi, sukces webhooków, incydenty PII, coverage testów kontraktowych, zgodność z SLA.
## Kryteria ukończenia
- [ ] Spec, bezpieczeństwo/PII, webhooks, monitoring/deprecations opisane; dokument w linkage_index; wersja/data/właściciel aktualne.
## Struktura sekcji

1) Źródło prawdy i repo (OpenAPI/AsyncAPI, konwencje)  
2) Pipeline generowania (narzędzia, CI/CD, lint/validate, tests)  
3) Treść i przykłady (errors, auth, rate limits, SDK snippets)  
4) Wersjonowanie/deprecje i changelog  
5) Publikacja (portal/dev hub, access control, cache/SEO)  
6) Monitoring aktualności (diff vs prod, alerty, ownership)  
7) Załączniki (kontrakty, config tools, ADR/waiver log)


## Wymagane rozwinięcia

- Narzędzia (redoc/swagger/codegen), lint/validate; standard błędów.  
- Pipeline CI: validate → generate → test → publish; wersjonowanie semver.  
- Przykłady kodu i SDK; automatyczne sync z kontraktem.  
- Monitoring drift (kontrakt vs deploy) i alerty na przeterminowaną dokumentację.

