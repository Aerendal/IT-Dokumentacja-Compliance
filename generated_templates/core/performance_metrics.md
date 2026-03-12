---
title: Performance Metrics
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Performance Metrics


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje metryki wydajności (aplikacje/usługi/systemy) wraz z celami, progami alertów i sposobem pomiaru. Ma zapewnić spójne monitorowanie, diagnozę i raportowanie wydajności w zgodzie z SLO/SLA.


## Zakres i granice

- Obejmuje: metryki czasu odpowiedzi (p50/p90/p95/p99), throughput/QPS, błędy/timeouts, zasoby (CPU/RAM/dysk/sieć), kolejek, cache hit, GC, cold starts, perf mobilne/web (LCP/TTFB/CLS/INP), batch/ETL (czas/okno SLA), zależności zewnętrzne, progi alertów, sampling, raportowanie, segmentację (region/tenant/device/release), SLO/SLA mapowanie.
- Poza zakresem: testy przedrelease (osobne plany), metryki kosztowe (FinOps – link).


## Użytkownicy i interesariusze

- SRE/Perf, Engineering, Product, Observability, Support, Exec (raporty).


## Wejścia i wyjścia

- Wejścia: architektura i krytyczne ścieżki, SLO/SLA, definicje transakcji, dane z APM/RUM/logów/metrics, profile ruchu, release/flags, zależności zewnętrzne, polityka alertów.
- Wyjścia: katalog metryk i definicji, cele/progi, konfiguracja alertów i dashboardów, segmentacja, raporty cykliczne, lista właścicieli, mapa do SLO.


## Założenia

- Dane z APM/RUM/metrics są dostępne; SLO/SLA określone; narzędzia alerting działają.


## Otwarte pytania

- Jak często przeglądać progi i SLO? 
- Czy wymagane są osobne progi per klient/tenant?


## Powiązania (meta)

- Key Documents: observability_standards, sla_slo_policy, api_performance_baseline, rum_metrics_guidelines, capacity_planning, incident_response_plan.
- Key Document Structures: definicje, cele, alerty, segmentacja, raporty.
- Document Dependencies: APM/RUM/metrics/logging, alerting, tracing, config management, release data.


## Zależności dokumentu

Wymaga SLO/SLA, listy krytycznych ścieżek/tras, danych APM/RUM/metrics, polityki alertów, właścicieli usług. Bez tego DoR otwarte.


## Fazy cyklu życia

- Definicja metryk i transakcji; wybór narzędzi.
- Ustalenie celów/progów i alertów; konfiguracja dashboardów.
- Operacje: monitoring, raporty, tuning progów; retrospektywy.



## Struktura sekcji (szkielet)

- Podsumowanie wykonawcze
- Kluczowe metryki i KPI
- Trendy i analiza
- Problemy i rekomendacje
- Kolejne kroki

## Szybkie powiązania

- linkage_index.jsonl (perf/metrics)
- observability_standards, sla_slo_policy, api_performance_baseline, rum_metrics_guidelines, capacity_planning, incident_response_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

1. Zdefiniuj ścieżki krytyczne, metryki i cele/SLO.
2. Skonfiguruj alerty/burn-rate i dashboardy; dodaj segmentację.
3. Monitoruj, raportuj i tunuj progi; aktualizuj po release/zmianach ruchu.


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

- p95/p99, Burn-rate, Error rate, Web Vitals (LCP/CLS/INP/TTFB), QPS, Saturation.


## Przykłady użycia

- API: p95 latency < 200 ms, error rate <0.1%, burn-rate alert 2x/4h.
- Web: LCP < 2.5s, CLS < 0.1, INP < 200 ms, segmentacja mobile/desktop.


## Ryzyka i ograniczenia

- Złe progi → alert fatigue lub brak detekcji; brak segmentacji → ukryte regresje; brak aktualizacji → przestarzałe cele.


## Decyzje i uzasadnienia
- Wybór metryk/SLO na dashboardzie.  
- Progi i kanały eskalacji.  
- Layout (kolejność, grupowanie).  
- Retencja i wersjonowanie zmian.
## Powiązania z innymi dokumentami

- Observability Standards, SLA/SLO Policy, API Performance Baseline, RUM Metrics Guidelines, Capacity Planning, Incident Response Plan.


## Powiązania z sekcjami innych dokumentów

- SLO Policy → progi; Observability → narzędzia; Release → regresje; Capacity → forecast.


## Słownik pojęć w dokumencie

- p95/p99, Burn-rate, Error rate, Web Vitals, QPS, Saturation.


## Wymagane odwołania do standardów

- Organizacyjne SLO/SLA, Web Vitals, ewentualne normy branżowe SLA.


## Mapa relacji sekcja→sekcja

- Ścieżki → Metryki → Progi/alerty → Segmentacja → Raporty → Tuning.


## Mapa relacji dokument→dokument

- Performance Metrics → Observability/SLO → Incident/Capacity → Release/Change.


## Ścieżki informacji

- Krytyczne ścieżki → Metryki → Alerty → Incydenty → Raporty → Korekta progów.


## Weryfikacja spójności

- [ ] Metryki/progi/alerty spójne z SLO; segmentacja ustawiona.
- [ ] Dashboardy/raporty działają; relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każda metryka ma definicję, cel, próg, właściciela, alert.
- [ ] Każdy alert ma kanał i eskalację; każdy raport ma odbiorców.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Dashboardy, alert config, definicje metryk, SLO map, raporty, release/regression noty.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- SRE/Perf → Engineering/Product → Observability → Owner sign‑off.


## Metryki jakości

- Czas wykrycia regresji, liczba fałszywych alertów, stabilność progów, czas korekty progów, pokrycie krytycznych ścieżek, zgodność z SLO.

## Kryteria ukończenia

- [ ] Metryki/progi/alerty/raporty gotowe; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Definicje transakcji → Metryki → Progi/alerty → Raporty → Incident/Problem.
- Segmentacja → Diagnoza → Priorytety → SLO.


## Struktura sekcji

1) Zakres i krytyczne ścieżki (transakcje, komponenty, regiony)  
2) Definicje metryk i jednostki (RT, QPS, error, resource, web vitals, batch SLA)  
3) Cele/SLO i progi alertów (p95/p99, error rate, resource thresholds)  
4) Segmentacja (region/tenant/device/release/deps)  
5) Monitoring i alerting (narzędzia, sampling, kanały, eskalacje)  
6) Dashboardy i raportowanie (widoki exec/ops, cadence)  
7) Właściciele i governance metryk (kto utrzymuje, zmiany progów)  
8) Ryzyka, decyzje, open issues


## Wymagane rozwinięcia

- Lista metryk z definicjami (wzory, okna, źródła) i mapą do SLO.
- Progi alertów i reguły (multi-window, burn-rate); kanały i eskalacje.
- Segmentacja i tagi (region/tenant/device/release) oraz wymagane filtry na dashboardach.


## Wymagane streszczenia

- Top metryki i progi, SLO map, krytyczne ścieżki, właściciele i kanały alertów.


## Guidance (skrót)

- Definiuj metryki od ścieżek krytycznych i SLO; używaj percentyli (p95/p99) i error rate.
- Ustal burn-rate alerty dla SLO; unikaj alert fatigue (multi-window, deduplikacja).
- Segmentuj metryki; obserwuj regresje po release/flagach.
- Utrzymuj dashboardy exec/ops; regularnie przeglądaj progi w retros.


## Checklisty Definition of Ready (DoR)

- [ ] SLO/SLA i ścieżki krytyczne zidentyfikowane; źródła danych dostępne.
- [ ] Polityka alertów i narzędzia monitoring/trace/RUM/APM gotowe.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Metryki/cele/progi opisane; alerty/dashboards skonfigurowane; segmentacja ustawiona.
- [ ] Właściciele/eskalacje zdefiniowane; dokument w linkage_index.
- [ ] Wersja/data/właściciel zaktualizowane.

