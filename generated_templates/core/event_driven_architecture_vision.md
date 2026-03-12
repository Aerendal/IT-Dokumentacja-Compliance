---
title: Event-Driven Architecture Vision
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Event-Driven Architecture Vision

## Metadane
- Właściciel: Solution Architect
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Opisuje wizję architektury zdarzeniowej: model publikacja/subskrypcja, kontrakty zdarzeń, topologie (broker/mesh/log), gwarancje dostarczenia i kolejności, bezpieczeństwo/compliance, obserwowalność, standardy schema/versioning oraz roadmapę adopcji. Definiuje trade‑offy i kryteria akceptacji.


## Zakres i granice
- Obejmuje: domeny i use case’y zdarzeniowe (integracje, async workflows, CQRS/ES, realtime), topologie (topic/stream/log, broker vs log), standardy zdarzeń (schema/kontrakty/versioning), gwarancje (at-least/at-most/exactly-once), kolejność/partitioning, idempotencja, deduplikacja, DLQ/parking lot, bezpieczeństwo/prywatność, zgodność, obserwowalność (tracing/metrics/logi), NFR (przepustowość, opóźnienia, dostępność), FinOps/GreenOps kosztów przetwarzania, plan migracji z sync do async.
- Poza zakresem: implementacja pojedynczych mikroserwisów/handlerów (w innych dokumentach).



## Wejścia i wyjścia
- Wejścia: katalog domen i use case’ów async/realtime, istniejące integracje sync, wymagania na opóźnienia/throughput/dokładność, ograniczenia regulacyjne (dane w zdarzeniach), standardy org (naming/tagging), decyzje architektoniczne (broker vs log, multi-region), koszty/TCO.
- Wyjścia: target/interim architektura EDA (topologie, partitioning, retention), standardy zdarzeń/kontraktów i wersjonowania, policy bezpieczeństwa/prywatności (masking/PII), wzorce (saga, outbox, idempotencja, retries, DLQ), plan migracji i rollout, ADR z trade‑offami, ryzyka/mitigacje.



## Powiązania (meta)
- Key Documents: enterprise_architecture_vision, data_architecture_vision, integration_strategy, security_architecture_vision, cloud_architecture_vision, observability_architecture, mlops_architecture, api_strategy, event_schema_registry_guidelines.
- Key Document Structures: zdarzenie → kontrakt → producent → transport (broker/log/mesh) → konsument → obserwowalność → koszt/FinOps.
- Document Dependencies: polityki danych/PII, standardy schematów, katalog zdarzeń, SLAs/SLOs, umowy z dostawcami brokerów/mesh.
- RACI: EDA owner/platform, Domain teams (producers/consumers), Security/Privacy, Data, Observability, FinOps.
- Standardy/compliance: schema registry, wersjonowanie (backward/forward), podpisy/szyfrowanie, ACL/RBAC, audyt, retencja.

## Zależności dokumentu
- Upstream: strategia integracji, decyzje dot. platformy (Kafka/Pulsar/NATS/EventBridge/etc.), regulacje danych w zdarzeniach, polityki bezpieczeństwa, wymagania latency/availability.
- Downstream: implementacje usług/stream processors, katalog zdarzeń, testy kontraktowe, dashboardy obserwowalności, FinOps kosztów throughput/storage, DR runbooki.
- Zewnętrzne: managed brokers (CSP), partnerzy/3rd party producenci/konsumenci, regulator (retencja/audyt/PII w zdarzeniach).



## Powiązania sekcja↔sekcja
- Use case/NFR → Kontrakty i topologia → Gwarancje dostarczenia/kolejność → Bezpieczeństwo/prywatność → Observability → FinOps/GreenOps.
- Schema/wersjonowanie → Konsumenci → Backward/forward compatibility → Testy kontraktowe.



## Fazy cyklu życia
- Discovery: identyfikacja use case async/realtime, ocena gotowości, wybór platformy.
- Design: topologie, kontrakty, gwarancje, kolejność, idempotencja, DLQ; ADR.
- Review: arch/security/privacy/FinOps; koszty throughput/retencji; regulacje danych.
- Implementation & Test: schema registry, outbox/saga, testy kontraktowe, testy obciążeniowe/latency, DR/chaos.
- Rollout & Ops: migration z sync na async, canary konsumentów, monitoring SLA, budżety kosztów, postmortem i tuning.




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
## Struktura sekcji (szkielet)
1) Streszczenie i cele (biznes, techniczne, latency/throughput)
2) Zakres, założenia, ograniczenia (dane w zdarzeniach, regulacje, RTO/RPO, limity kosztów)
3) Domeny i use case’y zdarzeniowe (producenci/konsumenci, scenariusze async/realtime)
4) Architektura target/interim (topologie: broker/log/mesh, partitioning, retention, multi-region)
5) Kontrakty zdarzeń i schema/versioning (backward/forward, katalog, ewolucja)
6) Gwarancje dostarczenia/kolejność, idempotencja, retries, DLQ/parking lot
7) Bezpieczeństwo/prywatność/compliance (PII, szyfrowanie, ACL, podpisy, audyt, data residency)
8) Observability (metryki/trace/log, lag, DLQ, contract tests, chaos/DR)
9) NFR i FinOps/GreenOps (throughput, latency, dostępność, koszt, ślad węglowy)
10) Plan migracji/rollout (sync→async, strangle fig, canary konsumentów, testy kontraktowe)
11) Ryzyka i mitigacje; założenia i zależności
12) Decyzje (ADR) i otwarte pytania



## Wymagane rozwinięcia
- Diagramy topologii, przepływów, kontraktów; sequence/stream processing; DR/topologie multi-region.
- RACI dla platformy EDA, producentów, konsumentów, bezpieczeństwa, obserwowalności, FinOps.
- ADR: wybór platformy, gwarancje, kolejność/partitioning, standardy schema, retencja, multi-region.
- Plan migracji sync→async z kontraktami, testami, walidacją lag/throughput.
- Policy na dane w zdarzeniach (masking/minimalizacja), katalog zdarzeń.



## Wymagane streszczenia
- Executive summary: model EDA, platforma, top use case’y, SLA/SLO, koszty, ryzyka, plan migracji.
- One-pager: topologia, kontrakty/schema, gwarancje, observability, plan rollout.



## Guidance (skrót)
- DoR: use case’y async/realtime zebrane; dane/PII i regulacje znane; wymagania latency/throughput/availability i koszty wstępnie policzone; warianty platform/topologii i ownerzy potwierdzeni.
- DoD: topologie, kontrakty, gwarancje, bezpieczeństwo/privacy, observability, NFR/FinOps opisane; plan migracji i rollout (sync→async) z testami; ryzyka/założenia; metadane aktualne; dokument w linkage_index.
- Spójność: każde zdarzenie ma kontrakt/schema/versioning, ownera, reguły privacy; producenci/konsumenci mają testy kontraktowe; lag/throughput/KPI mierzone.



## Szybkie powiązania
- enterprise_architecture_vision, data_architecture_vision, integration_strategy, security_architecture_vision, cloud_architecture_vision, observability_architecture, api_strategy, event_schema_registry_guidelines, mlops_architecture

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty Definition of Ready (DoR)
- [ ] Use case’y async/realtime zebrane; regulacje/PII i dane w zdarzeniach znane; NFR/latency/throughput i limity kosztów oszacowane.
- [ ] Warianty platform/topologii i ownerzy potwierdzeni; standardy schema/versioning wstępnie uzgodnione.

## Checklisty Definition of Done (DoD)
- [ ] Topologie EDA, kontrakty/schema, gwarancje dostarczenia/kolejność, bezpieczeństwo/privacy, observability opisane; ADR udokumentowane.
- [ ] Plan migracji/rollout sync→async z testami kontraktowymi/obciążeniowymi i rollbackiem; FinOps/GreenOps KPI zdefiniowane.
- [ ] Ryzyka/założenia opisane; metadane aktualne; dokument w linkage_index.

## Definicje robocze
- Kontrakt zdarzenia — schemat i reguły ewolucji; gwarancje kompatybilności (backward/forward).
- Idempotencja — przetwarzanie zdarzenia bez skutków ubocznych przy powtórzeniach.
- DLQ/Parking lot — kanał do obsługi zdarzeń nieprzetworzonych/niezgodnych z kontraktem.

## Przykłady użycia
- E-commerce: koszyk/płatność/fraud jako zdarzenia, outbox, exactly-once na płatnościach, saga i DLQ, monitoring lag/KPI.
- IIoT: telemetry stream + alerting, edge buffering, multi-region, privacy/PII w zdarzeniach, chaos/DR testy.

## Artefakty powiązane
- Katalog zdarzeń i kontraktów, schema registry, ADR log, diagramy topologii/partitioning, testy kontraktowe, dashboardy lag/throughput/error rate, plan migracji sync→async, RACI, polityki danych w zdarzeniach.

## Weryfikacja spójności
- [ ] Każde zdarzenie ma kontrakt, wersjonowanie i ownera; konsumenci mają testy kontraktowe.
- [ ] Gwarancje dostarczenia/kolejność i idempotencja są opisane i testowane; DLQ/parking lot działa.
- [ ] Plan migracji pokrywa dane/PII, testy obciążeniowe i rollback; KPI (lag/throughput/errors/koszt) mierzone.

## Ryzyka i ograniczenia
- [Ryzyko 1 — wpływ i sposób ograniczenia]
- [Ryzyko 2 — wpływ i sposób ograniczenia]

## Decyzje i uzasadnienia
- [Decyzja 1 — uzasadnienie]
- [Decyzja 2 — uzasadnienie]

## Założenia
- [Założenie 1]
- [Założenie 2]

## Otwarte pytania
- [Pytanie 1]
- [Pytanie 2]

## Powiązania z innymi dokumentami
- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów
- [Dokument X → Sekcja Y] — [powód powiązania]
- [Dokument Z → Sekcja W] — [powód powiązania]

## Słownik pojęć w dokumencie
- [Pojęcie 1] — [definicja i źródło]
- [Pojęcie 2] — [definicja i źródło]
- [Pojęcie 3] — [definicja i źródło]

## Wymagane odwołania do standardów
- [Standard 1] — [sekcja/fragment, którego dotyczy]
- [Standard 2] — [sekcja/fragment, którego dotyczy]

## Mapa relacji sekcja→sekcja
- [Sekcja A] -> [Sekcja B] : [typ relacji]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument
- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji
- [Wejście] → [Sekcja źródłowa] → [Sekcja rozwinięcia] → [Wyjście]
- [Wejście] → [Sekcja źródłowa] → [Sekcja streszczenia] → [Wyjście]

## Weryfikacja spójności
- [ ] Czy wszystkie ścieżki informacji są zamknięte?
- [ ] Czy istnieją pętle lub sprzeczne relacje?
- [ ] Czy sekcje krytyczne mają wskazane źródła i rozwinięcia?

## Lista kontrolna spójności relacji
- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań (np. wzajemne wykluczanie)?
- [ ] Czy relacje cross‑doc mają uzasadnienie i są zgodne z fazą?
- [ ] Czy relacje wymagają rozwinięć lub streszczeń są odnotowane?

## Artefakty powiązane
- [Artefakt 1] — [opis i relacja do dokumentu]
- [Artefakt 2] — [opis i relacja do dokumentu]

## Ścieżka decyzji
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]

## Użytkownicy i interesariusze
- **Solution / Enterprise Architect** — projektuje i zatwierdza architekturę
- **Tech Lead** — odpowiada za spójność techniczną implementacji
- **Product Owner** — definiuje wymagania biznesowe wchodzące na wejście
- **Development Team** — implementuje na podstawie projektu

## Ścieżka akceptacji
- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]

## Kryteria ukończenia
- [ ] Kryterium 1 — [opis]
- [ ] Kryterium 2 — [opis]

## Metryki jakości
- [Metryka 1] — [cel / próg]
- [Metryka 2] — [cel / próg]

## Monitoring i utrzymanie
- [Co monitorujemy] — [narzędzie / częstotliwość]
- [Kto utrzymuje] — [rola]

## Kontrola zmian
- [Zmiana] — [powód] — [data] — [akceptacja]

## Wymogi prawne i regulacyjne
- [Wymóg 1] — [źródło / akt prawny / standard]
- [Wymóg 2] — [źródło / akt prawny / standard]

## Zasady bezpieczeństwa informacji
- [Zasada 1] — [opis i wpływ na dokument]
- [Zasada 2] — [opis i wpływ na dokument]

## Ochrona danych i prywatność
- [Wymaganie 1] — [opis i sekcja docelowa]
- [Wymaganie 2] — [opis i sekcja docelowa]

## Wersjonowanie treści
- [Wersja] — [zmiana] — [autor] — [data]
- [Wersja] — [zmiana] — [autor] — [data]

## Historia zmian sekcji
- [Sekcja] — [zmiana] — [data]
- [Sekcja] — [zmiana] — [data]

## Wymagane aktualizacje
- [Sekcja] — [powód aktualizacji] — [termin]
- [Sekcja] — [powód aktualizacji] — [termin]

## Integracje i interfejsy
- [System / API] — [zakres integracji] — [wymagania]
- [System / API] — [zakres integracji] — [wymagania]

## Wymagania danych
- [Dane wejściowe] — [format] — [walidacja]
- [Dane wyjściowe] — [format] — [walidacja]

## Logowanie i audyt
- [Zdarzenie] — [poziom] — [retencja]
- [Zdarzenie] — [poziom] — [retencja]

## Utrzymanie i operacje
- [Procedura] — [cel] — [częstotliwość]
- [Procedura] — [cel] — [częstotliwość]

## KPI i SLA
- [KPI] — [cel] — [pomiar]
- [SLA] — [cel] — [pomiar]

## Scenariusze awaryjne
- [Scenariusz] — [objawy] — [reakcja]
- [Scenariusz] — [objawy] — [reakcja]

## Wpływ na inne systemy
- [System] — [rodzaj wpływu] — [ryzyko]
- [System] — [rodzaj wpływu] — [ryzyko]

## Zależności danych między systemami
- [Źródło danych] → [Odbiorca] — [opis]
- [Źródło danych] → [Odbiorca] — [opis]

## Harmonogram przeglądów
- [Obszar] — [częstotliwość] — [właściciel]
- [Obszar] — [częstotliwość] — [właściciel]

## Wymagania wydajnościowe
- [Wymaganie] — [metryka] — [próg]
- [Wymaganie] — [metryka] — [próg]

## Wymagania dostępnościowe
- [Wymaganie] — [SLA] — [metoda pomiaru]
- [Wymaganie] — [SLA] — [metoda pomiaru]

## Wymagania skalowalności
- [Wymaganie] — [cel] — [warunki]
- [Wymaganie] — [cel] — [warunki]

## Wymagania dostępności danych
- [Dane] — [częstotliwość dostępu] — [SLA]
- [Dane] — [częstotliwość dostępu] — [SLA]

## Retencja i archiwizacja
- [Dane] — [retencja] — [archiwizacja]
- [Dane] — [retencja] — [archiwizacja]

## Dostępność w sytuacjach awaryjnych
- [Scenariusz] — [zachowanie] — [priorytet]
- [Scenariusz] — [zachowanie] — [priorytet]

## Testy i weryfikacja
- [Test] — [cel] — [wynik oczekiwany]
- [Test] — [cel] — [wynik oczekiwany]

## Walidacja zgodności
- [Wymóg] — [metoda weryfikacji]
- [Wymóg] — [metoda weryfikacji]

## Audyty i przeglądy
- [Audyty] — [częstotliwość] — [odpowiedzialny]
- [Audyty] — [częstotliwość] — [odpowiedzialny]
