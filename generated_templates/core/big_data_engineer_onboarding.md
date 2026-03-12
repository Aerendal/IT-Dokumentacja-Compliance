---
title: Big Data Engineer Onboarding
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Big Data Engineer Onboarding


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnia spójny, szybki onboarding inżyniera Big Data: środowiska, dane, standardy, bezpieczeństwo, procesy delivery i utrzymania. Ma skrócić time‑to‑impact, zmniejszyć ryzyko błędów dostępowych/zgodności i ujednolicić praktyki zespołu.


## Zakres i granice

- Obejmuje: dostęp do środowisk (dev/stage/prod), konta i role, narzędzia (Spark, Flink, Airflow, Kafka, DB/DWH, lakehouse), standardy kodu i danych (naming, schemy, kontrakty), bezpieczeństwo/PII, CI/CD i testy danych, monitoring/observability, procesy review i change, ścieżkę wsparcia, szkolenia i materiały referencyjne.
- Poza zakresem: polityka wynagrodzeń, oceny performance, projektowanie konkretnych pipeline’ów (oddzielne ADR/runbooki).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: lista systemów i ról, polityki dostępu/PII, standardy danych, checklisty bezpieczeństwa, katalog źródeł danych, wzorce repozytoriów i szablony projektów, instrukcje CI/CD, on-call i eskalacje.
- Wyjścia: przydzielone dostępy i role, skonfigurowane środowisko dev, klucze/API, lokalne narzędzia, ukończone szkolenia, podpisane polityki, pierwsze zadanie/projekt z opiekunem, aktualizacje CMDB/HRIS jeśli wymagane.


## Założenia

- Dostęp do CMDB/katalogu danych.  
- Narzędzia wspierają audyt i tagowanie PII.  
- Są dostępne szablony repo i pipeline’ów.


## Otwarte pytania

- Czy potrzebne są lokalne zasoby GPU/TPU do pracy?  
- Jakie są limity budżetu na zasoby dev (clusters/slots)?  
- Które źródła danych wymagają E2EE lub dodatkowych kontroli?


## Powiązania (meta)

- Key Documents: data_platform_access_policy, data_contract_standard, data_quality_playbook, airflow_operational_runbook, kafka_usage_guidelines, spark_coding_standard, incident_response_runbook, privacy_and_pii_handling.
- Key Document Structures: dostęp, narzędzia, standardy, bezpieczeństwo/PII, CI/CD, obserwowalność, szkolenia, on-call.
- Document Dependencies: IAM/SSO, Secrets/PKI, DWH/lakehouse, Git/CI, ticketing/on-call rota, CMDB katalog danych.


## Zależności dokumentu

Wymaga: aktualnych ról/permission sets, listy źródeł danych i ich klasyfikacji PII, szablonów repo/projektów, checklist bezpieczeństwa i data quality, kontaktów opiekunów. Braki = DoR otwarte.


## Fazy cyklu życia

- Start: przydziały dostępu, narzędzia, polityki, szkolenia.  
- Pierwszy sprint: pierwsze zadanie z opiekunem, przegląd kodu, data quality checks.  
- Stabilizacja: wejście do on‑call (jeśli dotyczy), przegląd po 30/60 dni, feedback i uzupełnienia materiałów.



## Struktura sekcji (szkielet)
- Profil zespołu/projektów i narzędzia.
- Setup środowiska (IDE, CUDA, CLI, VPN, secrets).
- Dostępy: repo, dane, feature store, registry modeli.
- Eksperyment tracking i standardy repo (naming, review, testy).
- CI/CD modeli i deployment (batch/online).
- Bezpieczeństwo i PII (maskowanie, sandbox, licencje datasetów).
- Monitoring i observability (drift, latency, koszt, alerty).
- Runbooki i wsparcie (mentoring, slack, FAQ).
- Checklista onboarding.
## Szybkie powiązania

- linkage_index.jsonl (big_data/engineer/onboarding)  
- data_platform_access_policy, data_contract_standard, data_quality_playbook, airflow_operational_runbook, kafka_usage_guidelines, spark_coding_standard


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 20546** — Technologie Informacyjne — Big Data
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
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

1. Przydziel role/dostępy, skonfiguruj narzędzia; podpisz polityki.  
2. Uruchom szablon repo/pipeline, wykonaj pierwsze zadanie z buddy.  
3. Zaktualizuj checklisty DoR/DoD, potwierdzenia szkoleń i audyty dostępu.


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

- Data contract: umowa na schemat, SLA i jakość danych między producentem a konsumentem.  
- Data lineage: śledzenie przepływu danych i zależności transformacji.  
- DQ checks: walidacje jakości (schema, nulls, ranges, freshness).


## Przykłady użycia

- Nowy inżynier dołącza do zespołu streamingowego (Kafka/Flink).  
- Onboarding do zespołu batch (Spark/Airflow) z dostępem do lakehouse.  
- Wejście do on‑call po 60 dniach z weryfikacją runbooków.


## Ryzyka i ograniczenia

- Opóźnione dostępy → długi ramp‑up.  
- Brak standardów danych → niespójne schemy, błędy DQ.  
- Niedoszacowana ochrona PII → ryzyko compliance.


## Decyzje i uzasadnienia

- Zakres uprawnień (least privilege) vs produktywność.  
- Wspólny szablon repo/pipeline zamiast wielu wariantów – łatwiejsze utrzymanie.  
- Termin wejścia do on‑call zależny od ukończonych szkoleń/runbooków.


## Powiązania z innymi dokumentami

- data_contract_standard — zasady schematów/SLA.  
- data_quality_playbook — testy DQ.  
- incident_response_runbook — ścieżka eskalacji dla jobów danych.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- RODO/PII, polityka bezpieczeństwa danych, audyt dostępu.  
- Wewnętrzne standardy coding/data (naming, storage, encryption).

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

- Dostępy → Narzędzia → Pierwsze zadanie.  
- Standardy kodu/danych → CI/CD → Data quality/monitoring.  
- PII/bezpieczeństwo → Role/IAM → Logi/audyt.


## Struktura sekcji

1) Kontekst i cele onboardingu  
2) Role i dostępy (IAM, data domains, PII)  
3) Narzędzia i środowiska (local/dev/stage/prod, VPN/VPC, secrets)  
4) Standardy inżynierskie (naming, kontrakty danych, testy, code style)  
5) CI/CD i bezpieczeństwo danych (scan, lint, DQ, PII, klucze)  
6) Monitoring/observability (metryki, logi, lineage, alerty)  
7) Pierwsze zadanie i wsparcie (buddy, reviewer, ticket)  
8) Szkolenia obowiązkowe i materiały referencyjne  
9) On-call / rotacje / komunikacja  
10) Ryzyka, decyzje, otwarte punkty


## Wymagane rozwinięcia

- Lista ról/dostępów per system, z właścicielami.  
- Szablon repo i pipeline (build/test/deploy/DQ).  
- Checklista PII (klasy danych, maskowanie, logi).  
- Plan szkoleń (obowiązkowe, rekomendowane) z terminami.


## Wymagane streszczenia

- Jednostronicowy plan pierwszych 30/60 dni: cele, zadania, kontakty, metryki sukcesu.  
- Podsumowanie dostępu i potwierdzeń compliance.


## Guidance (skrót)

- Najpierw dostępy i PII, potem narzędzia i pierwsze zadanie.  
- Utrzymuj jeden szablon repo i pipeline – zmniejsza tarcie i błędy.  
- Każdy nowy inżynier ma buddy + reviewer + checklistę DoR/DoD.  
- Dokumentuj wszystkie nadane uprawnienia (audyt/RODO).


## Checklisty Definition of Ready (DoR)

- [ ] Role i dostępy nadane; PII/RODO podpisane.  
- [ ] Środowisko lokalne i dev działa (VPN, secrets, CLI).  
- [ ] Szablon repo i pipeline utworzone.  
- [ ] Buddy i reviewer przypisani; pierwsze zadanie zdefiniowane.  
- [ ] Plan szkoleń i terminy ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Pierwsze zadanie ukończone i zreviewowane.  
- [ ] Alerty/monitoring dla nowych jobów skonfigurowane.  
- [ ] Dostępy zarejestrowane w audycie; status/wersja/data uzupełnione.  
- [ ] Materiały/zauważone luki w onboarding zaktualizowane.  
- [ ] On-call (jeśli dotyczy) dodany do harmonogramu.

