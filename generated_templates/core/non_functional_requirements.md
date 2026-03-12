---
title: Non-Functional Requirements
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Non-Functional Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje mierzalne wymagania niefunkcjonalne (NFR) dla rozwiązania/systemu: wydajność, dostępność, bezpieczeństwo, skalowalność, użyteczność, obserwowalność, zgodność i operowalność. Kieruje decyzjami architektonicznymi, projektowaniem testów i kryteriami akceptacji releasu.


## Zakres i granice

- Obejmuje: SLO/SLA/SLI, opóźnienia/przepustowość, dostępność/HA/DR, odporność, bezpieczeństwo/prywatność, A11y/UX, zgodność (regulacje/branża), obserwowalność (metryki/logi/traces), operowalność (deploy, rollback, monitoring), limity środowiskowe i dane.  
- Poza zakresem: funkcjonalne wymagania biznesowe (FRS/BRD), szczegółowe projekty komponentów (osobne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: BRD/FRS, ryzyka biznesowe, profile obciążenia, polityki bezpieczeństwa/compliance, dane/PII klasyfikacja, standardy org, budżety (koszt/latency), zależności zewnętrzne.  
- Wyjścia: lista NFR z metrykami i progami, mapowanie do testów (perf/resilience/security/A11y), wymagania architektoniczne (HA/DR/cache/queue), kryteria go/no‑go, aktualizacje do planów monitoringu i runbooków.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: architecture_decision_records, performance_test_plan, resilience_testing_plan, security_requirements, accessibility_compliance, observability_architecture, dr_plan.  
- Key Document Structures: SLI/SLO/SLA, wydajność, HA/DR, bezpieczeństwo/prywatność, A11y/UX, obserwowalność, operowalność.  
- Document Dependencies: monitoring stack, CI/CD, load profiles, threat models, data classification, CMDB zależności.


## Zależności dokumentu

Wymaga: znanych scenariuszy biznesowych i profili ruchu, polityk security/privacy, wymagań regulacyjnych, danych o zależnościach zewnętrznych, wstępnej architektury logicznej. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja NFR (ideation/refinement).  
- Weryfikacja w design review/ADR.  
- Testy i walidacja w CI/CD i przed releasem.  
- Audyty i przeglądy okresowe; aktualizacja progów i SLO.



## Struktura sekcji (szkielet)
- Cel i kontekst biznesowy
- Interesariusze, persony i scenariusze
- Wymagania funkcjonalne (priorytety, reguły, wyjątki)
- Wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo, zgodność)
- Dane i integracje
- Kryteria akceptacji i miary sukcesu
- Zależności, ryzyka i założenia
- Śledzenie (traceability) do epik/testów
## Szybkie powiązania

- linkage_index.jsonl (non_functional/requirements)  
- performance_test_plan, resilience_testing_plan, security_requirements, accessibility_compliance, observability_architecture, dr_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
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

1. Zdefiniuj SLI/SLO i kluczowe domeny NFR dla systemu.  
2. Ustal progi i metody pomiaru; powiąż je z testami i monitoringiem.  
3. Zweryfikuj w design review, włącz do planu testów i release gate; aktualizuj DoR/DoD.


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

- SLI/SLO → Testy wydajności/odporności → Kryteria go/no‑go.  
- Bezpieczeństwo/PII → Kontrole/pen-test → Monitoring/alarmy.  
- HA/DR → Architektura → Testy odtwarzania → Runbooki.


## Struktura sekcji

1) Kontekst systemu i zakres NFR  
2) SLI/SLO/SLA i budżet błędów  
3) Wydajność i skalowalność (latency, throughput, burst, concurrency)  
4) Dostępność, odporność, HA/DR (RTO/RPO, failover, degradacja)  
5) Bezpieczeństwo i prywatność (authn/z, szyfrowanie, PII, audyt)  
6) Użyteczność i A11y (WCAG/UX)  
7) Obserwowalność i operowalność (metryki/logi/traces, alerty, deploy/rollback)  
8) Zgodność/regulacje (branża, dane, jurysdykcje)  
9) Dane i ograniczenia środowiskowe (rozmiar, retencja, edge cases)  
10) Kryteria akceptacji releasu, ryzyka, decyzje


## Wymagane rozwinięcia

- Tabela SLI/SLO/SLA z progami i metodą pomiaru.  
- Profile obciążenia i scenariusze testów wydajności/odporności.  
- Kontrole bezpieczeństwa (OWASP/ISO/NIST) i wymagania audytu.  
- Plan HA/DR z RTO/RPO i testami.


## Wymagane streszczenia

- Executive snapshot NFR: top SLO, progi, największe ryzyka, luki.  
- Krótka karta HA/DR (RTO/RPO, scenariusze failover).


## Guidance (skrót)

- NFR muszą być mierzalne, testowalne, powiązane z KPI biznesu.  
- Ustal budżet błędów i konsekwencje jego przekroczenia.  
- Testuj pod SLO, nie tylko pod „brak błędów”.  
- Integruj NFR z monitoringiem: te same metryki w testach i prod.  
- Aktualizuj NFR po zmianach architektury lub ruchu.


## Checklisty Definition of Ready (DoR)

- [ ] Scenariusze biznesowe i profile ruchu zebrane.  
- [ ] Polityki security/privacy/regulacje zidentyfikowane.  
- [ ] Wstępne SLI/SLO zdefiniowane; metody pomiaru dostępne.  
- [ ] Zależności zewnętrzne i ograniczenia środowiskowe opisane.  
- [ ] Plan testów niefunkcjonalnych i narzędzia uzgodnione.


## Checklisty Definition of Done (DoD)

- [ ] SLI/SLO/SLA wypełnione, progi zatwierdzone.  
- [ ] Testy wydajności/odporności/bezpieczeństwa/A11y wykonane lub wyjątki zaakceptowane.  
- [ ] HA/DR opisane i przetestowane (failover/fallback).  
- [ ] Monitoring/alerty i logi pod SLO działają; status/wersja/data zaktualizowane.  
- [ ] Linki do ADR/test planów/runbooków dodane; luki NFR odnotowane i przypisane.
