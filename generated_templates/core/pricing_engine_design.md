---
title: Pricing Engine Design
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Pricing Engine Design


## Metadane

- Właściciel: Finance Manager
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Projektuje silnik cenowy (reguły, modele, dane, interfejsy) tak, aby obsługiwał warianty pricing/packaging, promocje, rabaty i podatki w sposób audytowalny, wydajny i zgodny. Określa architekturę, dane, integracje, bezpieczeństwo i kryteria akceptacji.


## Zakres i granice

- Obejmuje: modele cen (static/usage/tiers/add-ons), katalog produktów/planów, reguły promocji/rabatów, podatki/opłaty, waluty/lokalizacje, kalkulację sync/async, API/SDK, integracje z CPQ/CRM/Billing/Payments, audytowalność, SLO (latency/poprawność), bezpieczeństwo i zgodność (podatki, dane wrażliwe), testowanie i rollout.
- Poza zakresem: pełne procesy billing/invoicing (oddzielny system), manualne cenniki ad hoc, polityki sprzedażowe (playbooki).


## Użytkownicy i interesariusze
- **Finance Manager / CFO** — zatwierdza budżet i analizuje ROI
- **Project Manager** — zarządza kosztami projektu w czasie realizacji
- **Procurement** — negocjuje umowy z dostawcami
- **Technical Lead** — szacuje nakłady pracy i koszty techniczne

## Wejścia i wyjścia

- Wejścia: strategia pricing/packaging, katalog produktów/planów, podatki/jurysdykcje, regulacje płatności, dane użycia/meters, wymagania wydajności/dostępności, ograniczenia kosztowe, istniejące systemy CPQ/CRM/Billing/Payments, polityki rabatowe/promocyjne.
- Wyjścia: architektura pricing engine (komponenty, dane, API, cache), model danych i reguł, strategie kalkulacji (cache/invalidate, fallback), SLO, plan testów (funkcjonalne, NFR, ceny brzegowe), plan rollout/canary, ADR/trade-offy, ryzyka i mitigacje.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: product_strategy_document, go_to_market_strategy, billing_architecture, payment_security_pci_dss, tax_compliance, api_design_patterns, data_architecture_vision, finops_guidelines.
- Document Structures: produkt/plan → reguły ceny → kalkulacja → audyt → billing → raportowanie.
- Dependencies: stawki podatkowe, kursy walut, dane użycia/metryk, katalog produktów, polityki rabatów, PCI/PSD2/GDPR.
- RACI: Product/Monetization (owner), Architecture, Data, Payments/Billing, Security/Compliance, Finance/Tax, SRE.


## Zależności dokumentu

- Upstream: strategia pricing, podatki/regulacje, katalog produktowy, kursy walut, polityki rabatowe.
- Downstream: CPQ/CRM, checkout/API, billing/invoicing, raporty finansowe, analityka revenue, audyt/compliance.
- Zewnętrzne: dostawcy płatności, serwisy podatkowe, źródła FX, regulatorzy.


## Fazy cyklu życia

- Discovery: katalog planów, modele cen, podatki/FX, scenariusze wydajności.
- Design: architektura engine (komponenty/flow/cache), model danych/reguł, API/SDK, bezpieczeństwo/compliance, ADR.
- Review: arch/security/compliance/finance, koszty/SLO, podatki/PCI.
- Implementation & Test: build, testy funkcjonalne/NFR, ceny brzegowe, chaos/latency.
- Rollout & Ops: canary, monitoring SLO/KPI, audyt cen, procedury zmiany reguł, postmortem.



## Struktura sekcji (szkielet)

1) Streszczenie i cele (KPI: poprawność cen, latency, win rate, ARPU, revenue leakage)
2) Zakres i założenia (modele cen, podatki, waluty, kanały, RTO/RPO, SLO latency)
3) Wymagania funkcjonalne (modele, rabaty/promocje, podatki, waluty, wersjonowanie reguł)
4) Architektura i komponenty (kalkulator, rules store, cache, API/SDK, schema, audyt, admin UI)
5) Dane i integracje (katalog produktów, usage/meters, FX/tax, CPQ/CRM/billing/payments)
6) Bezpieczeństwo i zgodność (PCI/PSD2/GDPR, PII, tokeny, klucze, audyt, least privilege)
7) NFR i SLO (latency, throughput, dostępność, spójność, koszt/FinOps)
8) Plan testów i jakości (case’y brzegowe, property-based tests, kontrakty API, testy wydajności)
9) Plan rollout i zmiany reguł (canary, feature flags, approval workflow, audyt zmian)
10) Ryzyka i mitigacje; założenia i zależności
11) Decyzje (ADR) i otwarte pytania


## Szybkie powiązania

- product_strategy_document, go_to_market_strategy, billing_architecture, payment_security_pci_dss, tax_compliance, api_design_patterns, data_architecture_vision, finops_guidelines


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

- [ ] Kanały korzystają z jednolitego zestawu reguł/API; wersjonowanie i audyt działają.
- [ ] Latencja/poprawność cen mierzone; testy brzegowe i chaos regularnie wykonywane.
- [ ] Zmiany reguł mają workflow approvals, rollback i pełen audyt.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Diagramy architektury, schematy danych/reguł, kontrakty API, przypadki brzegowe, ADR log, SLO dashboard, playbook zmian reguł.


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

- Modele cen/reguły → Model danych → API/kalkulacja → Cache/invalidation → Audyt/raporty.
- Podatki/FX → Reguły → Kalkulacja → Billing → Zgodność/finanse.


## Wymagane rozwinięcia

- Diagramy: flow kalkulacji, architektura komponentów, cache/invalidation, integracje CPQ/CRM/Billing.
- Model danych/reguł (schema, wersjonowanie, testy property-based), matryca przypadków brzegowych.
- RACI i workflow zmian reguł (approval, audit, rollback), procedury awaryjne.
- SLO/NFR + plan testów (funkcjonalne/NFR/chaos), monitoring i alerting.


## Wymagane streszczenia

- Executive summary: modele cen, architektura, SLO, ryzyka, rollout.
- One-pager: co liczymy, jak, gdzie (API/cache), kto odpowiada, terminy kluczowe.


## Guidance (skrót)

- DoR: modele cen i podatki/FX zebrane; wymagania latency/SLO; systemy źródłowe i integracje znane; ownerzy i proces zmian reguł ustaleni.
- DoD: architektura i dane/reguły opisane; SLO/testy (funkcjonalne/NFR) gotowe; plan rollout i change workflow; ryzyka/założenia; metadane aktualne; dokument w linkage_index.
- Spójność: każdy kanał używa tych samych reguł/API; wersjonowanie reguł i audyt działają; latencja i poprawność cen są mierzone; zmiany mają approvals i rollback.


## Checklisty Definition of Ready (DoR)

- [ ] Modele cen, podatki/FX, kanały i SLO zebrane; systemy źródłowe i integracje znane; ownerzy i proces zmian ustaleni.


## Checklisty Definition of Done (DoD)

- [ ] Architektura/reguły/API/cache opisane; SLO/testy funkcjonalne/NFR/chaos gotowe; plan rollout i change workflow z audytem.
- [ ] Ryzyka/założenia opisane; metadane aktualne; dokument w linkage_index.

