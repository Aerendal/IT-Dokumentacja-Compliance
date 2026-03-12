---
title: Code Documentation / API Docs
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Code Documentation / API Docs


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Standard dokumentacji kodu i API: jak pisać, wersjonować, publikować i utrzymywać docs (inline, README, ADR, OpenAPI/AsyncAPI, guides). Ma zapewnić spójność, łatwość użycia i zmniejszyć ryzyko błędnych integracji.


## Zakres i granice

- Obejmuje: struktury repo (README/CONTRIBUTING/ADR), styl i format (Markdown/OpenAPI), poziomy szczegółowości (overview/how‑to/reference/cookbook), przykłady i snippet’y, zasady aktualizacji i review, wersjonowanie i changelog, publikację (portal/docs site), dostępność językowa (PL/EN), compliance (PII/sekrety), automatyzację (doc generation, lint), monitoring jakości (broken links, coverage).  
- Poza zakresem: pełne tutoriale produktowe i marketing.


## Użytkownicy i interesariusze
- HRIT/Platform, Security/Privacy, Integratorzy, Product, Compliance.
## Wejścia i wyjścia

- Wejścia: architektura systemu, specyfikacje API, konwencje kodu, decyzje ADR, polityki bezpieczeństwa/PII, standardy stylu, narzędzia generatorów.  
- Wyjścia: kompletna dokumentacja (README, API reference, guides), OpenAPI/AsyncAPI, przykłady, changelog, checklisty jakości, publikacja w portalu, status DoR/DoD.


## Założenia

- Repo i pipeline CI/CD dostępne.  
- Portal/docs site istnieje i jest wspierany.  
- Zespół ma reviewerów technicznych i językowych.


## Otwarte pytania

- Czy wymagane są wielojęzyczne docs w tej iteracji?  
- Jakie SLA na aktualizację docs po zmianie API?  
- Jakie metryki jakości docs śledzić?


## Powiązania (meta)

- Key Documents: api_design_standards, coding_guidelines, adr_template, error_handling_guidelines, security_requirements, release_plan.  
- Key Document Structures: overview, quickstart, reference, examples, changelog, governance.  
- Document Dependencies: repo code, specyfikacje API, CI/CD docs pipeline, portal/docs site, access control.


## Zależności dokumentu

Wymaga: aktualnych specyfikacji API, decyzji architektonicznych, styl guide, narzędzi do generowania docs, polityk bezpieczeństwa/PII. Braki = DoR otwarte.


## Fazy cyklu życia

- Tworzenie/aktualizacja dokumentacji wraz z kodem.  
- Review (tech + language) i publikacja.  
- Monitoring jakości (broken links, coverage).  
- Aktualizacje przy zmianach wersji API/kodu.



## Struktura sekcji (szkielet)
- Kontekst i zakres
- Auth i bezpieczeństwo
- Endpointy i parametry
- Przykłady i błędy
- Rate limiting/SLA
- Changelog
- Kanały wsparcia
## Szybkie powiązania

- linkage_index.jsonl (code/documentation/api_docs)  
- api_design_standards, coding_guidelines, adr_template, error_handling_guidelines, security_requirements


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

1. Przygotuj spec i README; dodaj quickstart i przykłady.  
2. Uruchom lint/test docs, zrób review, opublikuj w portalu.  
3. Aktualizuj przy każdej zmianie API; odhacz DoR/DoD, zaktualizuj changelog i linkage_index.


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

- Reference docs: pełne kontrakty API, pola, kody błędów.  
- Quickstart: minimalny scenariusz „hello world” dla integratora.  
- ADR: decyzja architektoniczna z uzasadnieniem i alternatywami.


## Przykłady użycia

- Nowe API: publikacja OpenAPI + quickstart + sample SDK.  
- Refaktor modułu: aktualizacja README/ADR i changelog.  
- Audyt bezpieczeństwa: redakcja logów i przykładów.


## Ryzyka i ograniczenia

- Przestarzałe docs → błędy integracji.  
- Brak przykładów → wysokie tarcie deweloperów.  
- Sekrety/PII w przykładach → ryzyko bezpieczeństwa.


## Decyzje i uzasadnienia

- Format/wariant OpenAPI/AsyncAPI.  
- Zakres publikacji (internal vs external).  
- Poziom automatyzacji lint/test/publish.


## Powiązania z innymi dokumentami

- api_design_standards — zasady kontraktów.  
- adr_template — decyzje architektoniczne.  
- security_requirements — redakcja sekretów/PII.


## Powiązania z sekcjami innych dokumentów
- Privacy → PII/maskowanie; Security → auth/rate limits; Observability → monitoring/audyt.
## Słownik pojęć w dokumencie
- PII, SoD, OAuth2, SAML, JWT, Problem+JSON, Idempotency, Webhook signing.
## Wymagane odwołania do standardów

- Standardy organizacyjne API docs i bezpieczeństwa danych.  
- Rekomendacje ISO/IEC/OWASP dotyczącą dokumentacji/deweloper experience (jeśli stosowane).

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
## Powiązania sekcja↔sekcja

- Overview → Quickstart → Reference → Examples → Changelog.  
- ADR/decisions → Reference → Release notes.  
- Security/PII → Redakcja → Publikacja.


## Struktura sekcji

1) Zakres i standardy stylu (Markdown, OpenAPI/AsyncAPI)  
2) Struktura repo/docs (README, CONTRIBUTING, ADR, reference, guides)  
3) Wymagania dla API docs (kontrakty, błędy, auth, limity, wersje)  
4) Przykłady i quickstart (curl/SDK, sandbox)  
5) Wersjonowanie i changelog (semver, breaking changes, deprecjacje)  
6) Publikacja i dostęp (portal, permalinks, prawa dostępu)  
7) Jakość i automatyzacja (lint, broken links, tests, coverage)  
8) Bezpieczeństwo/PII (redakcja sekretów, logów)  
9) Governance i RACI (owners, reviewers, SLA na update)  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Szablon README i API reference; przykładowe snippet’y.  
- Lista obowiązkowych sekcji w OpenAPI (auth, errors, rate limits).  
- Checklista publikacji (review tech/lang, broken links, changelog).


## Wymagane streszczenia

- Executive snapshot: pokrycie docs, ostatnia aktualizacja, znane braki.  
- Quickstart 1‑pager dla integratora.


## Guidance (skrót)

- Docs aktualizuj razem z kodem (PR gate).  
- Jedno źródło prawdy: OpenAPI/ADR; reszta linkuje.  
- Przykłady uruchamialne; automatycznie testowane jeśli możliwe.  
- Wyrzucaj sekrety i PII; stosuj redakcję w logach/snippetach.  
- Utrzymuj changelog i wersjonowanie; komunikuj breaking changes.


## Checklisty Definition of Ready (DoR)

- [ ] Spec API i decyzje architektoniczne dostępne.  
- [ ] Wybrany styl/format i szablony.  
- [ ] Narzędzia do generacji/lintowania skonfigurowane.  
- [ ] Zasady bezpieczeństwa/PII określone.  
- [ ] Kanał publikacji (portal/docs) ustalony.


## Checklisty Definition of Done (DoD)

- [ ] README/reference/guides opublikowane; linki działają.  
- [ ] OpenAPI/AsyncAPI i przykłady gotowe; testy/linters przechodzą.  
- [ ] Changelog zaktualizowany; status/wersja/data uzupełnione.  
- [ ] Brak sekretów/PII w snippetach/logach; review security/language wykonane.  
- [ ] Linkage_index i ticket/ALM zaktualizowane.

