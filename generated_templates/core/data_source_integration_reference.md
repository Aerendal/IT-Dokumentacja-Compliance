---
title: Data Source Integration Reference
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Data Source Integration Reference


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Referencyjne wytyczne dla podłączania źródeł danych: wymagania, bezpieczeństwo, schematy, jakość i operacje. Ma zapewnić spójne, bezpieczne i monitorowane integracje.


## Zakres i granice

- Obejmuje: typy źródeł (DB, files, API, stream, SaaS), autoryzację i sieć (VPC peering/VPN/IP allowlist), schematy i mapowanie, PII/klasyfikację, harmonogram/latencję, walidację i DQ, retry/idempotencję, wersjonowanie schematów, monitoring/alerty, SLA/OLA, dokumentację i runbooki.  
- Poza zakresem: projekt modeli analitycznych downstream (oddzielne dokumenty).


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia

- Wejścia: opis źródła, właściciel, typ danych, PII/RODO, schemat, endpointy/creds, wymagania sieci, oczekiwana latencja/SLA, wolumen, wzorce zmian.  
- Wyjścia: karta integracji (schemat/mapowanie, auth, sieć, SLA), konfiguracja pipeline (ingest/ETL/ELT), testy DQ, monitoring, checklisty DoR/DoD, linki do runbooków.


## Założenia

- Dostępne są narzędzia ingest/DQ/monitoringu.  
- Możliwe jest peering/VPN lub allowlist.  
- Właściciel źródła współpracuje.


## Otwarte pytania

- Jak często zmienia się schemat?  
- Czy wymagane są audyty/raporty regulatora dla tego źródła?  
- Jak obsłużyć retry z limitem rate API?


## Powiązania (meta)

- Key Documents: data_governance_requirements, security_requirements, data_quality_playbook, schema_registry_policy, monitoring_strategy_document, access_control_policy.  
- Key Document Structures: źródło, auth/sieć, schemat, DQ, SLA, monitoring, runbook.  
- Document Dependencies: ingest platform, secrets manager, schema registry, CI/CD, monitoring, CMDB/source catalog.


## Zależności dokumentu

Wymaga: klasyfikacji danych (PII/PHI), właściciela źródła, schematu i wolumenu, decyzji sieci (VPC/VPN), polityk bezpieczeństwa, narzędzi DQ/monitoringu. Braki = DoR otwarte.


## Fazy cyklu życia

- Ocena źródła i wymagania.  
- Konfiguracja i testy integracji.  
- Operacje i monitoring.  
- Zmiany/wersjonowanie i przeglądy.



## Struktura sekcji (szkielet)
- Cel i definicja sukcesu (KPI)
- Zakres, założenia i ograniczenia
- Interesariusze i role/RACI
- Kamienie milowe i daty
- Plan fal/sprintów z deliverables
- Zależności i ryzyka oraz plan mitigacji
- Budżet/zasoby i obłożenie
- Plan komunikacji i raportowania
- Kryteria akceptacji/go-live i plan rewizji
## Szybkie powiązania

- linkage_index.jsonl (data/source/integration/reference)  
- schema_registry_policy, data_quality_playbook, monitoring_strategy_document, access_control_policy


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)

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

1. Wypełnij kartę integracji (dane, PII, auth, sieć, SLA).  
2. Skonfiguruj ingest/pipeline z DQ i monitoringiem.  
3. Publikuj schemat i wersje; odhacz DoR/DoD, zaktualizuj linkage_index.


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

- Idempotencja: wielokrotne przetworzenie nie zmienia wyniku.  
- Schema registry: źródło prawdy dla kontraktów danych.  
- OLA: wewnętrzne SLA dla zespołów.


## Przykłady użycia

- Podłączenie SaaS CRM przez API.  
- Ingest danych DB poprzez CDC.  
- Stream danych sensorów przez MQTT/Kafka.


## Ryzyka i ograniczenia

- Zmiana schematu bez wersji → przerwy dla konsumentów.  
- Brak DQ → złe decyzje analityczne.  
- Błędy sieci/auth → opóźnienia lub luki danych.


## Decyzje i uzasadnienia

- Harmonogram vs stream dla źródła.  
- Wybór metody auth i sieci (VPN/peering/IP).  
- Progi DQ i alertów.


## Powiązania z innymi dokumentami

- data_governance_requirements — polityki danych.  
- security_requirements — bezpieczeństwo i IAM.  
- data_quality_playbook — testy i progi.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- RODO/PII, wewnętrzne standardy bezpieczeństwa i danych.  
- Wymogi regulatora dla danych specyficznych (fin/health/public).

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

- Auth/sieć → Bezpieczeństwo → Monitoring.  
- Schemat → DQ → SLA → Alerty.  
- Zmiany schematu → Wersjonowanie → Konsumenci.


## Struktura sekcji

1) Opis źródła i dane (typ, PII, wolumen, SLA)  
2) Dostęp i sieć (auth, IP/VPN/peering, rate limits)  
3) Schemat i mapowanie (typy, klucze, wersjonowanie)  
4) Ingest/pipeline (harmonogram/stream, idempotencja, deduplikacja)  
5) Jakość danych (DQ testy, progi, wyjątki)  
6) Bezpieczeństwo/RODO (maskowanie, szyfrowanie, audyt)  
7) Monitoring/alerty (opóźnienie, błędy, DQ, wolumen)  
8) SLA/OLA i runbooki (incident, change, schema change)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Karta integracji (owner, PII, auth, sieć, SLA, schemat).  
- Lista DQ testów i progów; alerty.  
- Plan wersjonowania schematów i komunikacji do konsumentów.  
- Runbook incident/change/schema-change.


## Wymagane streszczenia

- Executive snapshot: status integracji, PII, SLA, top alerty.  
- Krótka karta sieć/auth (peering/VPN/IP, klucze).


## Guidance (skrót)

- Minimalizuj dane i PII; szyfruj w tranzycie/spoczynku.  
- Używaj idempotentnych pipeline’ów i wersjonuj schematy.  
- Dodaj DQ i monitoring od startu; alerty na opóźnienie i anomalie.  
- Dokumentuj właściciela i SLA; aktualizuj przy zmianach.  
- Testuj zmianę schematu na staging przed prod.


## Checklisty Definition of Ready (DoR)

- [ ] Owner, PII i schemat źródła zidentyfikowane.  
- [ ] Decyzje sieć/auth (VPN/peering/IP, klucze) podjęte.  
- [ ] Wolumen/SLA i harmonogram/stream znane.  
- [ ] Narzędzia DQ/monitoringu dostępne.  
- [ ] Plan wersjonowania schematów uzgodniony.


## Checklisty Definition of Done (DoD)

- [ ] Integracja działa; DQ/monitoring włączone; status/wersja/data uzupełnione.  
- [ ] Schemat opublikowany w registry; wersje i breaking changes opisane.  
- [ ] Runbooki incident/change/schema-change dostępne; alerty ustawione.  
- [ ] PII zabezpieczone; wyjątki udokumentowane.  
- [ ] Linkage_index i source catalog zaktualizowane.

