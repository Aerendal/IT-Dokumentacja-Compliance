---
title: ConTech API Documentation
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# ConTech API Documentation


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przedstawić spójne, kompletne i bezpieczne API dla rozwiązań ConTech (construction technology): kontrakty, modele danych, auth, przykłady, ograniczenia i wersjonowanie, aby ułatwić integracje z partnerami/projektami.


## Zakres i granice

- Obejmuje: opis endpointów i schematów (OpenAPI/GraphQL), auth (OAuth2/OIDC, API keys), rate limiting, wersjonowanie, paginację/filtry, webhooks, błędy i kody, przykłady użycia (cURL/SDK), dane budowy (projekty, zadania, urządzenia, sensoring), bezpieczeństwo (PII, projekty poufne), testy kontraktów i sandbox.  
- Poza zakresem: UI/UX aplikacji, dokumenty wewnętrzne niezwiązane z API.


## Użytkownicy i interesariusze
- HRIT/Platform, Security/Privacy, Integratorzy, Product, Compliance.
## Wejścia i wyjścia

- Wejścia: model domenowy ConTech, wymagania partnerów, polityka auth/licencji, wzorce błędów, ograniczenia rate, schematy danych (BIM/IoT), przykłady integracji.  
- Wyjścia: specyfikacja API, przykłady i SDK fragmenty, tabela błędów, limity i zasady, instrukcja webhooków, checklisty DoR/DoD kontraktów, changelog.


## Założenia

- API gateway i IdP dostępne.  
- CI/CD i contract testing możliwe.  
- Dane nie zawierają PII/klasyfikowane są poprawnie.


## Otwarte pytania

- Jakie standardy branżowe (BIM/IFC) musimy uwzględnić w API?  
- Jak publikować breaking changes (beta kanały)?  
- Jak długo utrzymywać stare wersje?  
- Czy partnerzy potrzebują SDK w określonych językach?

## Powiązania (meta)

- Key Documents: api_versioning_maintenance, error_handling_standards, logging_and_audit_trail, data_protection_compliance, security_controls_reference, documentation_publishing_plan.  
- Key Document Structures: kontrakty, auth, limity, webhooki, przykłady, testy.  
- Document Dependencies: API gateway, IdP, schema registry, monitoring, sandbox environment.


## Zależności dokumentu

Wymaga: aktualnego modelu danych i API gateway, polityki auth, limitów, sandboxu, listy use-case partnerów, procedury publikacji/changelog. Brak = brak DoR.


## Fazy cyklu życia

- Definicja kontraktów i auth/limity.  
- Implementacja i testy kontraktów.  
- Publikacja i sandbox.  
- Monitoring i wersjonowanie.  
- Deprecacje i komunikacja.



## Struktura sekcji (szkielet)
- Kontekst i zakres
- Auth i bezpieczeństwo
- Endpointy i parametry
- Przykłady i błędy
- Rate limiting/SLA
- Changelog
- Kanały wsparcia
## Szybkie powiązania

- linkage_index.jsonl (contech/api/documentation)  
- api_versioning_maintenance, error_handling_standards, documentation_publishing_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **OpenAPI 3.x** — Specyfikacja Interfejsu API (OpenAPI Initiative)

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

1. Uzupełnij specyfikację endpointów i schematów.  
2. Zdefiniuj auth/limity/webhooki; opublikuj sandbox.  
3. Uruchom testy kontraktów w CI; przygotuj changelog.  
4. Publikuj dokumentację; utrzymuj wersje i linkage_index.


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

- ConTech: technologie dla budownictwa.  
- Webhook signature: podpis służący do weryfikacji źródła zdarzenia.  
- Contract testing: testy zgodności payloadów z API.


## Przykłady użycia

- Pobranie zadań i statusów z placu budowy.  
- Subskrypcja webhooków o nowych odczytach sensorów.  
- Publikacja dokumentów projektowych przez API.


## Ryzyka i ograniczenia

- Breaking changes bez wersji → przerwy partnerów.  
- Brak podpisów webhooków → spoofing.  
- Niewłaściwe limity → abuse lub DoS.  
- Niespójne błędy → trudna integracja.


## Decyzje i uzasadnienia

- Wersjonowanie (path/header) i okres deprecacji.  
- Zakres rate limits i retry polityk.  
- Format błędów i standard payload.  
- Zakres danych w sandboxie (bez PII).


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
## Powiązania sekcja↔sekcja

- Schematy ↔ Kontrakty ↔ Testy.  
- Auth ↔ Rate limits ↔ Bezpieczeństwo/PII.  
- Webhooki ↔ Eventy ↔ Retry/idempotencja.


## Struktura sekcji

1) Przegląd i zakres API  
2) Auth i bezpieczeństwo (OIDC/API keys, scopes)  
3) Endpointy/typy (projekty, urządzenia, zadania, sensory, dokumenty)  
4) Parametry: paginacja, filtry, sortowanie  
5) Webhooki i eventy (retry, podpisy, idempotencja)  
6) Błędy i kody (format, kategorie)  
7) Rate limits i fair use  
8) Wersjonowanie i changelog  
9) Przykłady (cURL/SDK) i sandbox  
10) Testy kontraktów i DoR/DoD


## Wymagane rozwinięcia

- OpenAPI/GraphQL spec + przykłady request/response.  
- Polityka auth (scopes, tokens), podpisy webhooków.  
- Tabela błędów i kody; standard payload.  
- Limity rate i polityka retry/backoff.  
- Schematy danych dla głównych bytów ConTech (projekt, device, task, file, sensor reading).  
- Szablon changelog i deprecacji.


## Wymagane streszczenia

- Executive summary: zakres API, auth, limity.  
- Skrót zmian w najnowszej wersji (release notes).


## Guidance (skrót)

- Stosuj jasne kontrakty i wersjonowanie; nie wprowadzaj breaking bez deprecacji.  
- Używaj podpisów webhooków, idempotentnych kluczy; dokumentuj retry.  
- Format błędów spójny (np. RFC 7807).  
- Dodaj sandbox z danymi przykładowymi; testy kontraktów w CI.  
- Dokumentuj i publikuj changelog; aktualizuj linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Model danych i use-case partnerów zebrane.  
- [ ] Polityka auth/limity i bezpieczeństwa ustalone.  
- [ ] Sandbox i narzędzia testowe dostępne.  
- [ ] Szablon changelog i publikacji gotowy.  
- [ ] Struktura dokumentacji uzgodniona.


## Checklisty Definition of Done (DoD)

- [ ] Specyfikacja kompletna; przykłady/testy kontraktów zielone.  
- [ ] Auth/limity/webhooki opisane i działają w sandbox.  
- [ ] Błędy/formaty spójne; changelog zaktualizowany.  
- [ ] Dokumentacja opublikowana; linkage_index uzupełniony.  
- [ ] Brak krytycznych luk bezpieczeństwa/PII.

