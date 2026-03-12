---
title: Sales Analytics Report
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Sales Analytics Report


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Analizuje wyniki i zachowania sprzedażowe ponad podstawowe KPI: segmenty, kohorty, lejki, miksery kanałów/produktów, elastyczność cenowa, efektywność promocji, predykcje/forecast, insighty i rekomendacje.


## Zakres i granice

- Obejmuje: KPI rozszerzone, segmentacje (kanał/produkt/region/ICP), kohorty (retencja/expansions), lejki (MQL→SQL→Opp→Closed), analizy promocji/cen, analizy win/loss, efektywność kanałów i kampanii, predykcję/forecast (opcjonalnie), rekomendacje.
- Poza zakresem: implementacja zmian operacyjnych; projekt samego silnika pricing (w osobnym dokumencie), szczegółowe playbooki marketing/sales.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: CRM/CPQ/Billing/Marketing/CS dane, definicje KPI/OKR, targety, kampanie/promocje, kursy FX, dane kosztowe (CAC), dane produktowe/pricing, kalendarz release.
- Wyjścia: raport z wizualizacjami i insightami, rekomendacje i action items, win/loss i promo effectiveness, noty metodologiczne/glossary.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: sales_performance_report, sales_performance_monitoring, pricing_engine_design, go_to_market_strategy, analytics_strategy, marketing_plan, sales_enablement_materials.
- Dependencies: definicje KPI, źródła danych, kampanie, pricing/promocje, data contracts, governance danych.


## Zależności dokumentu

- Upstream: definicje KPI/OKR, dane sprzedaż/marketing/CS, targety, kampanie, pricing.
- Downstream: decyzje dot. kanałów/segmentów/promocji/pricingu, plany enablement, backlog zmian danych/analityki.
- Zewnętrzne: FX, sezonowość, zdarzenia rynkowe.


## Fazy cyklu życia

- Zbieranie i walidacja danych (quality/coverage).
- Analiza segment/kohort/lejki/promocje.
- Insighty i rekomendacje.
- Publikacja i follow-up.



## Struktura sekcji (szkielet)

1) Streszczenie (top KPI/insighty/ryzyka/rekomendacje)
2) Zakres, okres, KPI i definicje, źródła danych
3) KPI rozszerzone i trendy (bookings/revenue/NRR/GRR/churn/win rate/cycle/ACV, CAC/LTV, payback)
4) Segmentacje (kanał/produkt/region/ICP/plan), mix i efektywność
5) Kohorty i retencja/expansions (NRR, logo/$ churn, upsell/cross-sell)
6) Lejki i zachowania (MQL→SQL→Opp→Closed, velocity, conversion, blockers)
7) Promocje/pricing (elasticity, promo ROI, discount impact, win/loss themes)
8) Forecast/predykcja (opcjonalnie, założenia, model, warianty)
9) Ryzyka i obserwacje; rekomendacje i action items (owner, termin, KPI wpływu)
10) Metodologia, dane, glossary, noty jakości


## Szybkie powiązania

- sales_performance_report, sales_performance_monitoring, pricing_engine_design, go_to_market_strategy, analytics_strategy, marketing_plan, sales_enablement_materials


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 20546** — Technologie Informacyjne — Big Data
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

- [ ] KPI zgodne z definicją; FX i data wskazane; noty metodologiczne dołączone.
- [ ] Rekomendacje mają ownera/termin/KPI wpływu; ryzyka powiązane z obserwacjami.
- [ ] Forecast (jeśli użyty) ma jawne założenia, warianty i zakres niepewności.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Dashboard/plik BI, tabele KPI, segmenty, kohorty, lejki, promo ROI, win/loss, forecast (jeśli jest), action items log, glossary, ADR log.


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

- KPI/segmenty/kohorty → insighty → rekomendacje → action items.
- Promocje/pricing → win/loss → rekomendacje kanał/pricing → action items.


## Wymagane rozwinięcia

- Tabele/wykresy KPI, segmentów, kohort, lejków, promocji; analizy win/loss; (opcjonalnie) forecast.
- Action items z ownerem/terminem i KPI wpływu; ryzyka z mitigacją.
- Glossary definicji KPI i źródeł; noty metodologiczne i jakości danych.


## Wymagane streszczenia

- Executive summary: KPI vs target, 3 insighty, 3 rekomendacje, 3 ryzyka.
- One-pager: KPI kluczowe, trend, top ryzyko, top rekomendacja.


## Guidance (skrót)

- DoR: definicje KPI/okres/źródeł uzgodnione; targety i kampanie znane; dane dostępne; właściciel raportu i zatwierdzający.
- DoD: KPI policzone/zwizualizowane; insighty i rekomendacje z ownerami; ryzyka; glossary/metodologia; metadane aktualne; dokument w linkage_index.
- Spójność: KPI zgodne z definicją i zakresem dat; FX i źródła wskazane; action items mierzalne; forecast opisuje założenia.


## Checklisty Definition of Ready (DoR)

- [ ] Definicje KPI/okres/źródeł i targety uzgodnione; dane dostępne; kampanie/promocje zebrane.


## Checklisty Definition of Done (DoD)

- [ ] KPI policzone/zwizualizowane; insighty/rekomendacje z ownerami; ryzyka; glossary/metodologia; dokument w linkage_index.

