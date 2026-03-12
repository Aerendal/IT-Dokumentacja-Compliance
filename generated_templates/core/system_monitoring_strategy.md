---
title: System Monitoring Strategy
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# System Monitoring Strategy


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje strategię monitoringu systemów/usług: co mierzyć, jak mierzyć, progi i alerty, odpowiedzialności i raportowanie. Ma zapewnić wczesne wykrywanie problemów, minimalny MTTR i zgodność z SLO/SLA.


## Zakres i granice

- Obejmuje: złote sygnały (latency, traffic, errors, saturation), metryki biznesowe/kontenstowe, logi, trace, syntetyki, RUM, health checks, dependency monitoring, progi/alerty, SLO/SLA mapping, sampling, retention, dashboardy, incident hooks, runbooki i testy alertów.
- Poza zakresem: szczegółowe runbooki usług (link), pełne plany perf/security (osobne dokumenty).


## Użytkownicy i interesariusze

- SRE/Observability, Engineering, Product, Security/Privacy, FinOps.


## Wejścia i wyjścia

- Wejścia: architektura, krytyczne ścieżki, SLO/SLA, dependency map, dane APM/RUM/metrics/logs, polityka alertów, release/flags, compliance (retention, PII), koszty obserwowalności.
- Wyjścia: katalog metryk/logów/trace, progi alertów i reguły, dashboardy, plan testów alertów, RACI monitoringu, zasady retention/sampling, raporty (exec/ops).


## Założenia

- Narzędzia observability istnieją; właściciele są przypisani; SLO określone.


## Otwarte pytania

- Jak często testujemy alerty? 
- Jakie limity kosztów observability per usługa?


## Powiązania (meta)

- Key Documents: observability_standards, performance_metrics, incident_response_plan, sla_slo_policy, dependency_catalog, privacy_policy, cost_optimization_observability.
- Key Document Structures: sygnały, progi, alerty, dashboardy, governance.
- Document Dependencies: APM/RUM/logging/metrics/trace, alerting system, CMDB/deps, SLO data, cost data.


## Zależności dokumentu

Wymaga: SLO/SLA i krytycznych ścieżek, mapy zależności, narzędzi obserwowalności, polityki alertów/retencji, danych PII/privacy. Bez tego DoR otwarte.


## Fazy cyklu życia

- Definicja sygnałów/metryk i źródeł.
- Ustalenie progów/alertów, dashboardów, RACI.
- Testy alertów i runbooków.
- Operacje: monitoring, tuning progów, koszt, raporty.
- Przeglądy SLO/alertów po incydentach.



## Struktura sekcji (szkielet)

- Kontekst i motywacja
- Cele i wskaźniki sukcesu
- Zakres i ograniczenia
- Alternatywy rozważone
- Plan realizacji i kamienie milowe
- Ryzyka i plany mitygacji

## Szybkie powiązania

- linkage_index.jsonl (monitoring/strategy)
- observability_standards, performance_metrics, incident_response_plan, sla_slo_policy, dependency_catalog, privacy_policy, cost_optimization_observability


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Wpisz ścieżki/SLO; zmapuj sygnały i progi.
2. Ustal alerty/dashboardy i RACI; dodaj runbooki/testy.
3. Ustal retencję/sampling/privacy i budżet; monitoruj koszty.
4. Aktualizuj po incydentach/przeglądach; zamknij DoR/DoD i linkage_index.


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

- Golden signals, Burn-rate, Error budget, Sampling, Retention, RUM, APM.


## Przykłady użycia

- API: latency p95, error rate, saturation; burn-rate alert; runbook 5xx.
- Frontend: Web Vitals + errors; RUM; alert na spadek LCP/INP.


## Ryzyka i ograniczenia

- Alert fatigue; brak privacy w logach; wysokie koszty observability; brak testów alertów.


## Decyzje i uzasadnienia

- Zakres SLO (global vs per region) — zależnie od architektury.  
- Retencja logów/traces — kompromis koszt vs potrzeba audytu/IR.  
- Sampling/aggregation — kompromis dokładność vs koszt.

## Powiązania z innymi dokumentami

- Observability Standards, Performance Metrics, Incident Response, SLA/SLO Policy, Dependency Catalog, Privacy Policy, Cost Optimization Observability.


## Powiązania z sekcjami innych dokumentów

- SLO Policy → progi; IR → eskalacje; Privacy → logi/trace redakcja.


## Słownik pojęć w dokumencie

- Golden signals, Burn-rate, Error budget, Sampling, Retention, RUM, APM.


## Wymagane odwołania do standardów

- Organizacyjne SLO/SLA, polityki privacy/logging, standardy observability.


## Mapa relacji sekcja→sekcja

- Ścieżki/SLO → Sygnały → Progi/alerty → Runbooki → Raporty → Tuning.


## Mapa relacji dokument→dokument

- Monitoring Strategy → Observability/SLO → Incident/Performance → Cost/Privacy.


## Ścieżki informacji

- SLO → Metryki → Alerty → Incydent → Raport → Korekta progów.


## Weryfikacja spójności

- [ ] Sygnały/progi zgodne z SLO; alerty/testy i runbooki gotowe.
- [ ] Privacy/retencja/koszt ujęte; relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy alert ma próg, owner, runbook i kanał.
- [ ] Każda metryka ma źródło, segmentację i powiązanie z SLO.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Dashboardy, alert config, runbooki, testy alertów, raporty, koszt/retencja ustawienia.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- SRE/Observability → Engineering/Product → Privacy/FinOps → Owner sign‑off.


## Metryki jakości

- MTTR, liczba fałszywych alertów, pokrycie ścieżek krytycznych, koszt observability, zgodność z SLO, częstotliwość testów alertów.

## Kryteria ukończenia

- [ ] Strategia opisana; alerty/dashboards/runbooki/testy zdefiniowane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Sygnały/metryki → Progi/alerty → Runbooki/IR → Raporty.
- Retencja/sampling → Koszt → Zakres danych.


## Struktura sekcji

1) Krytyczne ścieżki i SLO/SLA (mapa na sygnały)  
2) Sygnały/metryki/logi/trace (definicje, źródła, sampling)  
3) Progi i alerty (reguły, multi-window, burn-rate, kanały, eskalacje)  
4) Dashboardy i raportowanie (exec/ops, cadence)  
5) Runbooki i testy alertów (ćwiczenia, chaos, tabletop)  
6) Retencja, privacy i koszty (PII, redakcja, retention, budżet)  
7) Governance i RACI (ownerzy, zmiany progów, przeglądy)  
8) Ryzyka, decyzje, open issues


## Wymagane rozwinięcia

- Lista metryk/sygnałów i mapowanie do SLO; progi/alerty (burn-rate, error budgets).
- Zasady sampling/retention i privacy dla logów/trace; koszt/budżet.
- RACI i proces zmiany progów; plan testów alertów.


## Wymagane streszczenia

- Top sygnały/KPI, progi/alerty, odpowiedzialni, koszty/retencja, plan testów alertów.


## Guidance (skrót)

- Start od SLO i ścieżek krytycznych; zdefiniuj sygnały/goldens i progi burn-rate.
- Unikaj alert fatigue: multi-window, deduplikacja, szumy; testuj alerty.
- Uwzględnij privacy/PII w logach/trace; trzymaj retencję/koszt pod kontrolą.
- Utrzymuj runbooki i przeglądy po incydentach; aktualizuj progi.


## Checklisty Definition of Ready (DoR)

- [ ] SLO/SLA i ścieżki krytyczne znane; narzędzia APM/RUM/logs/trace dostępne.
- [ ] Polityka alertów/retencji/privacy dostępna; ownerzy zmapowani.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Sygnały/metryki/progi/alerty opisane; dashboardy skonfigurowane.
- [ ] Runbooki/testy alertów i RACI gotowe; privacy/retencja/koszt ujęte.
- [ ] Dokument w linkage_index; wersja/data/właściciel aktualne.

