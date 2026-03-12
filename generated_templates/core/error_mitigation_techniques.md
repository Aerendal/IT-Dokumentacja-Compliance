---
title: Error Mitigation Techniques
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Error Mitigation Techniques


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zbiera techniki ograniczania błędów w systemach (software/infra/ML): zapobieganie, detekcja, odporność i szybkie odzyskanie. Ma zmniejszyć wpływ błędów na użytkowników i biznes.


## Zakres i granice

- Obejmuje: prewencję (lint/static analysis, type safety, schema validation), walidację danych, retries/backoff/idempotencję, circuit breaker/bulkhead, timeouts, chaos/testing fault injection, graceful degradation/feature flags, canary/rollbacks, data correctness (checksums, reconciliation), ML (data drift/guardrails), monitoring/alerting, dokumentację runbooków.  
- Poza zakresem: pełne procedury incident response (linkowane).


## Użytkownicy i interesariusze
- QA, PM/Release, Dev, Security/Perf, Product/Business.
## Wejścia i wyjścia

- Wejścia: architektura usług, profile błędów/awarii, SLA/SLO, logi/incydenty, standardy kodu i testów, wymagania danych, polityki reliability.  
- Wyjścia: lista technik do zastosowania, rekomendacje per komponent, checklisty DoR/DoD, plan wdrożeń i testów, powiązania z runbookami i alertami.


## Założenia

- Monitoring i logi są dostępne.  
- Feature flags/CI-CD dostępne.  
- Zgoda biznesu na testy resilience.


## Otwarte pytania

- Jakie są limity SLO/SLA dla krytycznych zależności?  
- Które systemy można objąć chaos w produkcji vs staging?  
- Jak mierzyć skuteczność technik (metryki przed/po)?


## Powiązania (meta)

- Key Documents: reliability_engineering_guide, resiliency_patterns, incident_response_runbook, observability_plan, data_quality_playbook, ml_model_guardrails.  
- Key Document Structures: prewencja, detekcja, reakcja, dane, ML, deployment.  
- Document Dependencies: CI/CD, feature flags, monitoring/logging/tracing, chaos/load tools, schema registry.


## Zależności dokumentu

Wymaga: profilu błędów/incydentów, SLO/SLA, narzędzi monitoringu/chaos, standardów kodu/testów, danych o zależnościach. Braki = DoR otwarte.


## Fazy cyklu życia

- Ocena i wybór technik.  
- Wdrożenia i testy (chaos/fault injection).  
- Operacje i monitoring.  
- Postmortem i iteracje.



## Struktura sekcji (szkielet)
- Kontekst i cele
- Zakres
- Wejścia/Wyjścia
- Struktura sekcji
- Powiązania i quick-links
- DoR/DoD
- Artefakty
- Metryki
- Utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (error/mitigation/techniques)  
- resiliency_patterns, data_quality_playbook, ml_model_guardrails, observability_plan


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

1. Zmapuj ryzyka/błędy i zależności; wybierz techniki.  
2. Wdróż konfiguracje i testy; uruchom chaos/game-day.  
3. Monitoruj metryki, aktualizuj runbooki i DoR/DoD; uzupełnij linkage_index.


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

- Circuit breaker: wstrzymuje wywołania do zawodnej zależności.  
- Bulkhead: izolacja zasobów, by awaria jednej części nie zalała reszty.  
- Fault injection: celowe wprowadzanie błędów do testów odporności.


## Przykłady użycia

- Dodanie circuit breaker i retry dla zależności płatności.  
- Chaos test network loss na usłudze streamingowej.  
- Guardrails ML: blokada predykcji przy braku cech krytycznych.


## Ryzyka i ograniczenia

- Nadmierne retry → thundering herd.  
- Zbyt agresywne timeouts → fałszywe błędy.  
- Chaos bez kontroli → realny outage.


## Decyzje i uzasadnienia

- Progi timeout/retry/circuit.  
- Zakres chaos/game-day i częstotliwość.  
- Jakie guardrails ML są obowiązkowe.


## Powiązania z innymi dokumentami

- incident_response_runbook — reakcje.  
- resiliency_patterns — wzorce.  
- data_quality_playbook — dane.


## Powiązania z sekcjami innych dokumentów
- Incident Response Plan → Lessons Learned → nowe lub zmodyfikowane mitygacje.
- Architecture Decision Records → decyzje projektowe wpływające na wybór mitygacji.
- SLA/SLO → wpływ na kryteria sukcesu i metryki monitoringu.
## Słownik pojęć w dokumencie
- Residual Risk — ryzyko po wdrożeniu mitygacji; może wymagać akceptacji.
- Compensating Control — kontrola zastępcza, gdy podstawowa mitygacja nie jest możliwa.
- Sunset Date — data wygaśnięcia akceptacji lub potrzeby utrzymywania mitygacji tymczasowej.
## Wymagane odwołania do standardów

- Wewnętrzne standardy reliability/security.  
- Regulacje branżowe, jeśli dotyczą danych/availability.

## Mapa relacji sekcja→sekcja
- Kryteria włączenia -> Tabela mitygacji: filtruje, które ryzyka trafiają do planu.
- Tabela mitygacji -> Integracja z harmonogramem: działania wprowadzane jako zadania/kamienie milowe.
- Integracja -> Monitoring: metryki i SLO obserwują skuteczność działań.
- Monitoring -> Eskalacja: brak postępu lub niespełnione kryteria sukcesu wyzwalają eskalację.
## Mapa relacji dokument→dokument
- Risk Mitigation Plan -> Risk Register: korzysta z rankingów i parametrów ryzyk.
- Risk Mitigation Plan -> Change/Release Plan: wymaga wdrożenia mitygacji przed releasami.
- Risk Mitigation Plan -> Test Strategy/Security Testing: definiuje testy potwierdzające skuteczność.
- Risk Mitigation Plan -> Incident/Postmortem: aktualizuje działania po incydentach.
## Ścieżki informacji
- „Ryzyko P1 data exposure” → Kryteria włączenia → Tabela mitygacji (szyfrowanie/KMS/DLP/runbook) → Testy/Scan → Status/raport.
- „Ryzyko downtime 4h” → Tabela mitygacji (HA/auto‑scale/failover drills) → Integracja z release i SLO → Monitoring → Eskalacja gdy SLO naruszone.
- „Ryzyko vendor lock‑in” → Tabela mitygacji (exit plan, dual vendor, escrow) → SLA → Przegląd TPRM.
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
- Harmonogram runów, raporty runów, metryki, defekt log, decyzje go/conditional/no‑go, retrospektywa.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- QA/PM → Security/Perf (jeśli dotyczy) → Product/Business → Release/CAB.
## Metryki jakości
- Pass rate, Defect leakage, Flake rate, Czas cyklu testów, MTTR defektów w cyklu, dotrzymanie harmonogramu.
## Kryteria ukończenia
- [ ] Plan wykonany; decyzje i raporty zapisane; retrospektywa z lekcjami.  
- [ ] Dokument w linkage_index/checklistach; wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

- Prewencja → Detekcja → Reakcja → Uczenie się (postmortem).  
- Dane/ML → Walidacje → Guardrails → Monitoring/drift.  
- Deployment → Canary/rollback → Observability.


## Struktura sekcji

1) Cel i profil błędów (history/incydenty)  
2) Prewencja kodu/danych (lint/type/schema, kontrakty, DQ)  
3) Odporność runtime (timeouts, retries/backoff, circuit breaker, bulkhead)  
4) Deploy/rollback i zmiany (canary, feature flags, blue-green)  
5) Dane i integralność (checksums, reconciliation, idempotencja)  
6) ML‑specific (drift, guardrails, safe defaults)  
7) Testy resilience (chaos, fault injection, game days)  
8) Monitoring i alerty (SLO, synthetics, anomaly detection)  
9) Runbooki i edukacja (checklisty, playbooki)  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Lista technik per komponent/ryzyko; priorytety.  
- Plany testów fault/chaos i kryteria akceptacji.  
- Tabela retries/backoff/timeout/circuit breaker per zależność.  
- Guardrails danych/ML i monitorowane metryki.


## Wymagane streszczenia

- Executive snapshot: top ryzyka i techniki, status wdrożeń, SLO.  
- Run sheet game-day/chaos.


## Guidance (skrót)

- Zacznij od danych i kontraktów: waliduj na wejściu i wyjściu.  
- Ustal timeouts/retry z backoff + idempotencja.  
- Circuit breakers/bulkheads na zależnościach krytycznych.  
- Stosuj canary/feature flags + automatyczny rollback.  
- Testuj resilience regularnie (chaos) i ucz się z postmortemów.


## Checklisty Definition of Ready (DoR)

- [ ] Profil błędów/incydentów i SLO zebrane.  
- [ ] Zależności i wymagania danych znane.  
- [ ] Narzędzia monitoringu/chaos dostępne.  
- [ ] Wstępne progi timeout/retry/circuit określone.  
- [ ] Właściciele komponentów wyznaczeni.


## Checklisty Definition of Done (DoD)

- [ ] Techniki wdrożone; testy/chaos zaliczone; status/wersja/data uzupełnione.  
- [ ] Tabela timeout/retry/circuit opublikowana; wyjątki opisane.  
- [ ] Guardrails danych/ML aktywne; monitoring/alerty działają.  
- [ ] Runbooki zaktualizowane; linkage_index uzupełniony.  
- [ ] Lessons learned i decyzje zapisane.

