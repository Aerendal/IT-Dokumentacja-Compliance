---
title: Monitoring syntetyczny
status: needs_content
aligned: true
aligned_rev: 3
aligned_at: 2026-02-09
aligned_by: codex
---
# Monitoring syntetyczny


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Stworzyć syntetyczne testy transakcyjne, aby proaktywnie wykrywać degradacje dostępności i wydajności.



## Zakres i granice
- Obejmuje: metryki biznesowe i techniczne, SLO/SLA/SLI, logi, tracery, alerting, dashboards, runbooki, właścicieli, standardy tagów i retencji, budżet kosztów, wymagania compliance (PII, audyt), proces przeglądów i ciągłego doskonalenia.
- Poza zakresem: szczegółowe konfiguracje narzędzi (osobne runbooki), procedury IR (link do incident_response), projekt infrastruktury (link do architecture docs).
## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia
- Wejścia: katalog usług (CMDB), krytyczne ścieżki i zależności, SLO/SLA, mapa KPI biznesowych, standardy tagowania, wymagania compliance/audytu, budżet kosztów observability, narzędzia (Prometheus/Grafana/ELK/APM).
- Wyjścia: standard monitoringu (metryki/logi/traces), lista SLI/SLO z progami, macierz pokrycia (service x signal), standard alertów i eskalacji, dashboardy referencyjne, harmonogram przeglądów, plan optymalizacji kosztów i retencji.
## Założenia
- Stabilne źródła metryk/logów/traces i kontrola PII.  
- On‑call rota dostępna i aktualna.  
- Narzędzia wspierają etykiety/tagi i multi‑region.
## Otwarte pytania
- Czy wszystkie SLO muszą być customer‑facing czy tylko wewnętrzne?  
- Jakie synthetic tests są wymagane per krytyczna ścieżka?  
- Jakie limity kosztów są akceptowalne per usługa?
## Powiązania (meta)
- Key Documents: incident_response_runbook, service_level_objectives, observability_architecture, logging_standards, alerting_policy, cost_management_observability.
- Key Document Structures: sygnały (metrics/logs/traces), SLI/SLO, alerting, dashboardy, runbooki, koszt/retencja.
- Document Dependencies: CMDB/usługi, katalog zależności, narzędzia monitoringowe, system ticketowy, on‑call rota, polityki bezpieczeństwa danych.
## Zależności dokumentu
Wymaga: aktualnego CMDB/katalogu usług, zdefiniowanych SLO/SLA, przyjętych standardów tagowania i retencji, dostępów do narzędzi monitoringu/logowania/APM. Braki = DoR otwarte.
## Fazy cyklu życia
- Definicja strategii i priorytetów (services tiering).  
- Rollout standardów monitoringu i alertów.  
- Ciągłe przeglądy: coverage, fałszywe alarmy, koszty, audyty.  
- Ewolucja narzędzi/architektury observability.
## Struktura sekcji (szkielet)

1. Scenariusze syntetyczne: login, checkout, kluczowe API, edge cases; częstotliwość.
2. Lokacje i urządzenia: regiony, sieci, typy przeglądarek/OS; mobile/desktop.
3. Metryki: availability, latency (p95), błędy, czas DNS/SSL/TTFB, page weight.
4. Alerty: progi, korelacja z RUM/infra, tłumienie false positives.
5. Utrzymanie: wersjonowanie scenariuszy, aktualizacje po zmianach UI/API, testy wsteczne.
6. Raporty: trend SLA, raporty dzienne/tygodniowe, związki z release.


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


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

- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.



## Checklisty jakości

- [ ] Scenariusze pokrywają krytyczne ścieżki i są uruchamiane regularnie z różnych regionów.
- [ ] Metryki (availability/latency/errors) z alertami skonfigurowane.
- [ ] Scenariusze aktualizowane po zmianach UI/API; wersjonowanie zachowane.
- [ ] Raporty trendów i korelacja z RUM/infra dostępne.

## Definicje robocze
- SLI: mierzalny wskaźnik jakości usługi (np. availability 99.9%, latency p95).  
- SLO: cel dla SLI w okresie (np. 99.9% / 28 dni).  
- Error budget: 1 − SLO; budżet na zmiany/awarie.
## Przykłady użycia
- Zmiana architektury logowania — ocena kosztów i tagów.  
- Nowa usługa Tier1 — nadanie SLI/SLO i alertów.  
- Post‑mortem fałszywych alarmów — tuning progów i reguł.
## Ryzyka i ograniczenia
- Alert fatigue z nadmiarem reguł lub złymi progami.  
- Brak standardu tagów uniemożliwia pivotowanie danych.  
- Niekontrolowane koszty retencji/indeksów.
## Decyzje i uzasadnienia
- Zakres SLO (global vs per region) — zależnie od architektury.  
- Retencja logów/traces — kompromis koszt vs potrzeba audytu/IR.  
- Sampling/aggregation — kompromis dokładność vs koszt.
## Powiązania z innymi dokumentami
- incident_response_runbook — reakcja na alerty.  
- logging_standards — formaty i PII.  
- cost_management_observability — budżet i optymalizacje.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- ISO 27001 / SOC2 (logowanie, audyt).  
- Wewnętrzne standardy PII/RODO i retencji.
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
