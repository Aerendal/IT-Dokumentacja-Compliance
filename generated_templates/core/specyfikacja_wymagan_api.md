---
title: Specyfikacja wymagań API
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Specyfikacja wymagań API


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zebrać wymagania funkcjonalne i niefunkcjonalne dla API: use case, zasoby, limity/SLA, bezpieczeństwo, obserwowalność i kryteria akceptacji.


## Zakres i granice

- Obejmuje: persony/use case, zakres funkcji i zasobów, kontrakt (OpenAPI/AsyncAPI), NFR (wydajność, dostępność, bezpieczeństwo, skalowalność), limity/rate limit/SLA, dane i prywatność, monitoring/audyt, testy i kryteria akceptacji.  
- Poza zakresem: szczegółowy design bezpieczeństwa (design_bezpieczenstwa_api), wersjonowanie/deprecjacja (strategia_wersjonowania_api).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania biznesowe, procesy domenowe, dane źródłowe, profile ruchu, polityki bezpieczeństwa/prywatności, SLO/SLA, ograniczenia platformy.  
- Wyjścia: specyfikacja kontraktu API, katalog zasobów/operacji, NFR i limity, wymagania bezpieczeństwa/observability, kryteria testów/akceptacji, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: design_bezpieczenstwa_api, strategia_wersjonowania_api, api_gateway_architecture, api_change_communication, logging_strategy, audit_logging, rate_limiting_requirements.  
- Key Document Structures: use case/persony, funkcje/zasoby, NFR/limity/SLA, bezpieczeństwo/prywatność, monitoring/audyt, testy/akceptacja.  
- Document Dependencies: IdP/gateway, data contracts, SLO platformy, privacy policy, observability stack.



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
1. Cele wydajności: latency/throughput.
2. Obciążenia i profile ruchu.
3. Budżety zasobów i koszty.
4. Scenariusze testów.
5. Monitoring i SLO.
6. Kryteria akceptacji.
## Szybkie powiązania

- linkage_index.jsonl (api/requirements)  
- design_bezpieczenstwa_api, strategia_wersjonowania_api, api_gateway_architecture


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **OWASP ASVS** — Standard Weryfikacji Bezpieczeństwa Aplikacji (OWASP)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)

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

1. Zbierz use case i zasoby; opisz kontrakt i kody błędów.  
2. Ustal NFR/limity, bezpieczeństwo/prywatność oraz monitoring/audyt.  
3. Dodaj testy i kryteria akceptacji; zaktualizuj linkage_index i checklisty.


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

- [ ] Zasoby/operacje mają opis i kody błędów; NFR/limity per operacja.  
- [ ] Wymagania bezpieczeństwa i prywatności spójne z design_bezpieczenstwa_api.  
- [ ] Monitoring/testy zdefiniowane; linkage_index zawiera dokument.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Plik OpenAPI/AsyncAPI, tabela limitów/SLO, error catalog, test plans, log/audit schematy, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Pokrycie kontraktem (OpenAPI completeness), liczba braków w testach kontraktowych, czas reakcji na change requests, liczba incydentów SLA/limitu, zgodność błędów z katalogiem.

## Kryteria ukończenia

- [ ] Specyfikacja wymagań API kompletna, spójna z bezpieczeństwem/wersjonowaniem i gotowa do implementacji.


## Struktura sekcji

1) Use case i odbiorcy (persony, kanały, scenariusze, priorytety)  
2) Funkcje i zasoby (CRUD/verbs, kontrakt, walidacja schematów, błędy)  
3) NFR i limity (wydajność/latencja, dostępność, skalowanie, rate limit/burst, payload size)  
4) Bezpieczeństwo i prywatność (AuthN/AuthZ, dane wrażliwe, maskowanie, logging bez PII)  
5) Monitoring i audyt (metryki, logi, trace, audit events, SLO/SLA, alerty)  
6) Testy i kryteria akceptacji (contract tests, happy/sad paths, bezpieczeństwo, obciążenie)  
7) Załączniki (OpenAPI/AsyncAPI, tabele limitów, error catalog, ADR/waiver log)


## Wymagane rozwinięcia

- Tabela zasobów/operacji z parametrami, kodami błędów i przykładami payloadów.  
- Limity i SLO per operacja; polityka retries/idempotency.  
- Wymagania bezpieczeństwa (AuthN/AuthZ, rate limit, WAF/validation) i prywatności (masking).  
- Plan testów: contract, e2e, performance, security; kryteria blokujące.  
- Kanały i cadence komunikacji zmian (changelog, status page, webhooks).


## Wymagane streszczenia

- Executive: zakres i odbiorcy, kluczowe NFR/SLA, główne ryzyka (bezpieczeństwo/skalowanie).


## Guidance (skrót)

- Opisuj kontrakt w OpenAPI/AsyncAPI i utrzymuj jako źródło prawdy.  
- Definiuj SLO na poziomie operacji; limity muszą uwzględniać burst/abuse.  
- Wymagaj idempotency dla mutacji; błędy standaryzuj (kody, trace id).  
- Zaplanuj observability przed implementacją; alerty powiąż z ownerami.  
- Każda zmiana kontraktu przechodzi review i jest komunikowana klientom.


## Checklisty Definition of Ready (DoR)

- [ ] Persony/use case i dane źródłowe zebrane; polityki bezpieczeństwa/prywatności znane.  
- [ ] SLO/SLA i limity wstępnie uzgodnione; narzędzia observability dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Kontrakt opisany (OpenAPI/AsyncAPI), NFR/limity i bezpieczeństwo zdefiniowane; monitoring/audyt i testy opisane.  
- [ ] Linkage_index zaktualizowany; status/metadane aktualne; checklisty DoR/DoD odhaczone.  
- [ ] Kryteria akceptacji pokrywają funkcję, bezpieczeństwo i wydajność.

