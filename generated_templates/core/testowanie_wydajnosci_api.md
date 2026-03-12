---
title: Testowanie wydajności API
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Testowanie wydajności API


## Metadane

- Właściciel: QA Lead
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan i standard testów wydajności API (load/stress/soak), aby potwierdzić spełnienie SLO/SLA i wykryć regresje przed produkcją.


## Zakres i granice

- Obejmuje: profile ruchu i SLO, scenariusze testowe (baseline, peak, spike, soak), dane i środowiska, metryki/progi (latencja, throughput, błędy, saturation), monitoring/trace, raportowanie i regresje.  
- Poza zakresem: testy bezpieczeństwa (testowanie_bezpieczenstwa_api) i ogólna strategia rate limit (api_rate_limiting_requirements).


## Użytkownicy i interesariusze
- **QA Lead / Test Manager** — planuje strategię testowania i zarządza procesem QA
- **QA Engineer** — projektuje i wykonuje przypadki testowe
- **Development Team** — naprawia defekty i dostarcza testowalny kod
- **Product Owner** — definiuje kryteria akceptacji i priorytetyzuje defekty

## Wejścia i wyjścia

- Wejścia: kontrakt API i krytyczne ścieżki, SLO/SLA, profile ruchu (dobowe/sezonowe), limity/gateway, dane testowe, środowisko perf, narzędzia (k6/JMeter/Gatling), budżet czasowy.  
- Wyjścia: plan scenariuszy i obciążeń, konfiguracje narzędzi, metryki/progi i raporty, lista regresji i rekomendacji, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: api_rate_limiting_requirements, design_bezpieczenstwa_api, logging_strategy, strategia_wersjonowania_api, incident_response_runbook.  
- Key Document Structures: profile/SLO, scenariusze, dane/środowiska, metryki, monitoring/trace, raport/regresje.  
- Document Dependencies: gateway/WAF, observability stack, CI/CD pipeline, test data management.



## Zależności dokumentu

- Konsumuje: [dokumenty wejściowe — co musi istnieć zanim ten dokument powstanie]
- Dostarcza do: [dokumenty wyjściowe — co korzysta z tego dokumentu]

## Fazy cyklu życia

- Faza 1: Koncepcja i Wizja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 2: Analiza Wymagań: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 3: Projekt / Design: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 4: Planowanie: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 5: Implementacja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 6: Testowanie / QA: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 7: Bezpieczeństwo / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 8: Wdrożenie / Deployment: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 9: Operacje / Maintenance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)

- Zakres testów i kryteria akceptacji
- Przypadki testowe (TC)
- Środowisko testowe
- Dane testowe
- Wyniki i raporty
- Defekty i status

## Szybkie powiązania

- linkage_index.jsonl (api/performance_testing)  
- api_rate_limiting_requirements, design_bezpieczenstwa_api, logging_strategy


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

1. Ustal profile ruchu i SLO; zmapuj krytyczne ścieżki.  
2. Przygotuj scenariusze, dane i środowisko; uruchom testy z monitoringiem/trace.  
3. Raportuj wyniki, otwórz regresje/ticki; zaktualizuj linkage_index i checklisty.


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

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

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

- [ ] Scenariusze pokrywają krytyczne ścieżki i peak/burst/soak; SLO/progi zdefiniowane.  
- [ ] Monitoring/trace działa; raport zawiera bottlenecks i rekomendacje.  
- [ ] Linkage_index uzupełniony; plan retestu istnieje.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Skrypty k6/JMeter/Gatling, dane testowe, dashboardy/trace, raporty i ticket list, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Spełnienie SLO (p95/p99, error rate), throughput vs cel, liczba regresji wydajności, MTTR dla regresji, koszt testów (czas/zasoby).

## Kryteria ukończenia

- [ ] Plan testów wydajności gotowy i używany w CI/pre‑prod, zapewnia spełnienie SLO/SLA.


## Struktura sekcji

1) Profile ruchu i SLO (rampa, peak, burst, średnie; per endpoint/plan)  
2) Scenariusze obciążenia (baseline, load, stress/spike, soak, failover/chaos)  
3) Dane i środowiska (anonymized/synthetic, separacja środowisk, config limitów)  
4) Metryki i progi (latencja p50/p95/p99, throughput, error rate, saturation, retries)  
5) Monitoring i trace (logi, APM, distributed tracing, korelacja z gateway)  
6) Raport i regresje (wyniki, bottlenecks, rekomendacje, ticketing, go/no‑go)  
7) Załączniki (skrypty k6/JMeter, dane testowe, ADR/waiver log)


## Wymagane rozwinięcia

- Tabela SLO per endpoint/plan; kryteria go/no‑go.  
- Definicje ramp-up/ramp-down, długość testów soak, limity concurrency.  
- Lista metryk i progi alertów; sposób liczenia retriable vs fatal errors.  
- Plan testów w CI/CD (smoke perf na PR, pełne cyklicznie) i kryteria blokujące merge/release.


## Wymagane streszczenia

- Executive: status SLO, główne bottlenecks, ryzyka wydajności i rekomendacje.


## Guidance (skrót)

- Testuj realistycznymi danymi i payloadami; uwzględnij limity/gateway.  
- Oddziel retriable od fatal errors; licz p99 i error budget.  
- Trace’uj kluczowe ścieżki; koreluj z logami/gateway.  
- Automatyzuj smoke perf w CI; pełne testy przed większym releasem.  
- Dokumentuj regressions i ich naprawy; aktualizuj linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] SLO i profile ruchu znane; środowisko perf gotowe; dane testowe przygotowane.  
- [ ] Narzędzia i skrypty dostępne; limity/gateway skonfigurowane.


## Checklisty Definition of Done (DoD)

- [ ] Testy wykonane, raport i rekomendacje gotowe; regresje otwarte; linkage_index zaktualizowany.  
- [ ] Metryki/progi spełnione lub wyjątki/waivery z planem; status/metadane aktualne; checklisty DoR/DoD odhaczone.  
- [ ] Plan retestu po fixach ustalony.

