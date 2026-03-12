---
title: Runbook monitorowania API
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Runbook monitorowania API


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Procedura monitorowania API: metryki, alerty, triage i komunikacja, żeby szybko wykrywać i ograniczać problemy wydajności/dostępności.


## Zakres i granice

- Obejmuje: metryki (latencja p50/p95/p99, error rate 4xx/5xx, rate limit/429, quota, availability), alerty/progi per endpoint/region/plan, triage ścieżkę (deploy, partner, downstream), feature flags/experymenty, komunikację i raportowanie, postmortem/tuning.  
- Poza zakresem: bezpieczeństwo API (design_bezpieczenstwa_api), pełny incident IR (incident_response_playbook).


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: dashboardy APM/gateway, logi/trace z request-id, release notes, lista partnerów/krytycznych klientów, tabela SLO/SLA, feature flags.  
- Wyjścia: progi alertów, ścieżka triage, checklisty, szablony komunikacji/status page, raporty i action items, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: logging_strategy, audit_logging, api_rate_limiting_requirements, incident_response_playbook, testowanie_wydajnosci_api.  
- Key Document Structures: metryki, alerty, triage, komunikacja, postmortem/tuning.  
- Document Dependencies: gateway/APM, tracing, status page, ticketing, feature flag system, CI/CD deploy feed.



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

- Warunki wstępne i wymagania
- Kroki wykonania (krok po kroku)
- Weryfikacja poprawności
- Kroki rollback
- Typowe problemy i rozwiązania
- Log akcji

## Szybkie powiązania

- linkage_index.jsonl (api/runbook_monitorowania)  
- logging_strategy, incident_response_playbook, api_rate_limiting_requirements


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **OWASP ASVS** — Standard Weryfikacji Bezpieczeństwa Aplikacji (OWASP)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

1. Skonfiguruj metryki/alerty; zdefiniuj SLO/progi.  
2. W incydencie wykonuj triage wg checklist; komunikuj zgodnie z szablonami.  
3. Po incydencie raportuj, tunuj progi, zaktualizuj linkage_index i checklisty.


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

- [ ] Metryki/alerty pokrywają krytyczne endpointy; routing on-call działa.  
- [ ] Triage flow obejmuje deploy, partnerów, downstream, rate limit; trace/logi dostępne.  
- [ ] Linkage_index uzupełniony; postmortem/tuning zaplanowane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Dashboardy APM/gateway, konfiguracje alertów, checklisty triage, szablony komunikacji, raporty incydentów, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Średni czas triage, liczba alertów szumowych, czas publikacji status page, spełnienie SLO, liczba regresji po tuningu progów.

## Kryteria ukończenia

- [ ] Runbook monitorowania API gotowy do użycia i osadzony w linkage_index.


## Struktura sekcji

1) Metryki i progi (latencja p50/p95/p99, error rate 4xx/5xx, 429, throughput, availability/SLO)  
2) Alerty i routing (per endpoint/region/plan; who/on-call; noise policy)  
3) Triage (sprawdź deployy, partnerów, downstreamy, rate limit, feature flags; narzędzia/logi/trace)  
4) Komunikacja (status page, klient/partner, wewnętrzna; szablony initial/update/closure)  
5) Postmortem i tuning (rapport, action items, threshold tuning, testy perf)  
6) Załączniki (checklist triage, szablony komunikacji, ADR/waiver log)


## Wymagane rozwinięcia

- Tabela progów per endpoint/plan; SLO/SLA i error budget.  
- Flow triage krok po kroku; wymagane dane (trace id, request id, deployment id).  
- Szablony komunikacji (wewn./zewn., status page) i kryteria publikacji.  
- Polityka alert noise: agregacje, deduplikacja, ciche godziny, auto close.


## Wymagane streszczenia

- Executive: stan SLO, główne źródła alertów, ostatnie działania tuning.


## Guidance (skrót)

- Alerty opieraj o SLO i error budget; unikaj alert fatigue.  
- Triage zaczynaj od „co się zmieniło”: deployment, feature flag, ruch partnera.  
- Zawsze używaj trace/request id w komunikacji; loguj decyzje i czasy.  
- Po incydencie tuning progów i testów; aktualizuj linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Dashboardy i trace działają; SLO/progi wstępne zdefiniowane.  
- [ ] Status page i kanały komunikacji gotowe; on-call zdefiniowany.


## Checklisty Definition of Done (DoD)

- [ ] Metryki/alerty i triage flow opisane; szablony komunikacji dołączone; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Postmortem/tuning proces opisany; checklisty DoR/DoD odhaczone.

