---
title: App Performance Metrics
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# App Performance Metrics


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Zdefiniować zestaw metryk wydajności aplikacji (web/mobile/desktop), sposoby pomiaru i progi SLO, aby monitorować doświadczenie użytkownika i wykrywać regresje.


## Zakres i granice

- Obejmuje: metryki klienta (TTFB, FCP, LCP, INP, CLS, app start, ANR/Crash), backend (latencja, error rate), sieć (TLS, DNS, RTT), narzędzia pomiaru (RUM, synthetic), progi SLO.
- Nie obejmuje: szczegółowego planu optymalizacji (osobny Performance Improvement Plan) ani definicji alertów (są w runbookach/alertach).


## Użytkownicy i interesariusze
- SRE/Perf, Engineering, Product, Observability, Support, Exec (raporty).
## Wejścia i wyjścia

- Wejścia: wymagania UX/SLO, architektura aplikacji, dane z RUM/APM, benchmarki.
- Wyjścia: katalog metryk, sposoby pomiaru (RUM/synthetic/APM), progi SLO, sposób raportowania, lista alertów powiązana z metrykami.


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

- SLO/SLI Policy.
- Monitoring/Alerting Guide.
- Performance Test Plan.


## Fazy cyklu życia
- Definicja metryk i transakcji; wybór narzędzi.
- Ustalenie celów/progów i alertów; konfiguracja dashboardów.
- Operacje: monitoring, raporty, tuning progów; retrospektywy.
## Struktura sekcji (szkielet)

1. Zakres aplikacji (platformy, główne ścieżki użytkownika).
2. Metryki klienta (web/mobile/desktop) i definicje.
3. Metryki backend i API (latencja, błędy, throughput).
4. Progi SLO/cele i segmentacja (np. region, urządzenie).
5. Źródła danych i narzędzia (RUM, synthetic, APM).
6. Raportowanie i alertowanie (jak, jak często, kto odbiera).


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


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

- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.



## Checklisty jakości

- [ ] Metryki klienta i backend jasno zdefiniowane.
- [ ] SLO/progi ustalone i mierzalne.
- [ ] Źródła danych/narzędzia wskazane.
- [ ] Raportowanie i alerty opisane.


## Definicje robocze

- **LCP/INP/CLS** — metryki Web Vitals.
- **RUM** — Real User Monitoring; dane z realnych sesji.

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
- Dashboardy, alert config, definicje metryk, SLO map, raporty, release/regression noty.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- SRE/Perf → Engineering/Product → Observability → Owner sign‑off.
## Metryki jakości
- Czas wykrycia regresji, liczba fałszywych alertów, stabilność progów, czas korekty progów, pokrycie krytycznych ścieżek, zgodność z SLO.
## Kryteria ukończenia
- [ ] Metryki/progi/alerty/raporty gotowe; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

- „Metryki i SLO” **constrains** „Alerty i raportowanie”.
- „Narzędzia pomiaru” **defines_structure** „Źródła danych”.



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

 na odchylenie od SLO.

