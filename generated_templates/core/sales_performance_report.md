---
title: Sales Performance Report
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Sales Performance Report


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Raportuje wyniki sprzedaży w zadanym okresie: KPI/OKR, pipeline, konwersje, tempo sprzedaży, retencję/NRR, podziały segment/kanał/produkt/region, ryzyka i rekomendacje. Ma służyć decyzjom operacyjnym i strategicznym.


## Zakres i granice

- Obejmuje: KPI sprzedażowe (bookings, revenue, NRR/GRR, churn), konwersje lejka (MQL→SQL→Closed), win rate, cycle time, ACV/ARPA, segment/kanał/region/produkt, prognoza (opcjonalnie snapshot), ryzyka i rekomendacje.
- Poza zakresem: szczegółowe dane osobowe klientów (przechowywane w CRM); pełne playbooki sprzedaży; budżet marketingowy.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: CRM/CPQ/Billing dane, pipeline snapshoty, dane marketingowe (MQL/SQL), dane cs/support (churn/NRR), plany/targety, kursy walut, kalendarz kampanii.
- Wyjścia: raport okresowy (PDF/Deck/BI), tabela KPI vs target, wnioski i rekomendacje, action items z ownerami, ryzyka/blokery, sekcja danych i definicji (glossary).


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: go_to_market_strategy, product_strategy_document, pricing_engine_design, sales_enablement_materials, sales_support_plan, sales_training_on_solution, risk_register.
- Dependencies: CRM/CPQ/Billing, definicje KPI/OKR, kalendarz kampanii, kursy FX.


## Zależności dokumentu

- Upstream: definicje KPI/OKR, dane z CRM/CPQ/Billing/Marketing/CS, targety.
- Downstream: plany działań (sales/marketing/CS), rewizje celów, decyzje o alokacji zasobów.
- Zewnętrzne: dane FX (jeśli raport w wielu walutach), sezonowość/zdarzenia rynkowe.


## Fazy cyklu życia

- Zbieranie danych (snapshoty), weryfikacja jakości.
- Analiza i wnioski.
- Rekomendacje i action items.
- Publikacja i follow-up.



## Struktura sekcji (szkielet)

1) Streszczenie (KPI vs target, top 3 wnioski, top 3 ryzyka)
2) KPI/OKR i definicje (bookings/revenue/NRR/GRR/churn/win rate/cycle time/ACV)
3) Pipeline i konwersje (lejki MQL→SQL→Opp→Closed, win rate, cycle time)
4) Segmenty/kanały/regiony/produkty (porównania, mix)
5) Retencja i NRR (churn logo/$, ekspansje, downsell)
6) Forecast i coverage (opcjonalnie, snapshot vs target)
7) Ryzyka i blokery (dane, proces, zasoby, konkurencja)
8) Rekomendacje i action items (owner, data, KPI wpływ)
9) Dane, metodologia, glossary


## Szybkie powiązania

- go_to_market_strategy, product_strategy_document, pricing_engine_design, sales_enablement_materials, sales_support_plan, sales_training_on_solution, risk_register, analytics_strategy


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

- [ ] KPI zgodne z definicją i targetami; FX/datę raportu wskazano.
- [ ] Wnioski wynikają z danych; rekomendacje mają ownera/termin/KPI wpływu.
- [ ] Ryzyka powiązane z obserwacjami; glossary/metodologia dołączone.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Dashboard/plik BI, tabele KPI, lejki, cohorty churn/expansion, action items log, glossary, ADR log (założenia metodologiczne).


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

- KPI vs target → wnioski → action items → właściciele i terminy.
- Pipeline/konwersje → win rate/cycle time → rekomendacje enablement/pricing/process.


## Wymagane rozwinięcia

- Tabele i wykresy KPI vs target; lejki konwersji; cohorty churn/expansion; podziały segment/kanał/produkt/region.
- Action items z ownerem/terminem i metryką efektu; ryzyka z mitigacją.
- Glossary definicji KPI i źródeł danych; noty o jakości danych.


## Wymagane streszczenia

- Executive summary: KPI vs target, 3 wnioski, 3 rekomendacje, 3 ryzyka.
- One-pager: KPI główne, trend, top ryzyko, top rekomendacja.


## Guidance (skrót)

- DoR: źródła danych dostępne i spójne; definicje KPI/OKR uzgodnione; zakres okresu ustalony; targety dostępne.
- DoD: KPI policzone, wizualizacje dodane, wnioski i rekomendacje z ownerami/terminami; glossary i metodologia; metadane aktualne; dokument w linkage_index.
- Spójność: KPI zgodne z definicją, daty/FX jasno wskazane; action items mierzalne; ryzyka powiązane z KPI.


## Checklisty Definition of Ready (DoR)

- [ ] Definicje KPI/OKR uzgodnione; zakres dat i targety znane; źródła danych dostępne.


## Checklisty Definition of Done (DoD)

- [ ] KPI policzone i zwizualizowane; wnioski/rekomendacje z ownerami; ryzyka i mitigacje; glossary/metodologia; dokument w linkage_index.

