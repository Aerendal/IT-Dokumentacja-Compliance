---
title: Sales Performance Monitoring
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Sales Performance Monitoring


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Definiuje stały system monitorowania wyników sprzedaży: KPI, źródła danych, częstotliwość, dashboardy, alerty, odpowiedzialności i proces przeglądów. Ma zapewnić wczesne wykrywanie odchyleń i szybkie decyzje.


## Zakres i granice

- Obejmuje: definicje KPI/OKR, źródła danych i jakość, częstotliwość (daily/weekly/monthly/QBR), dashboardy, alerty/progi, ownership, proces przeglądów, zarządzanie wersją definicji, zgodność danych (PII/FX), audyt zmian.
- Poza zakresem: szczegółowe playbooki sprzedażowe i budżety marketingowe.


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: definicje KPI, targety, źródła CRM/CPQ/Billing/Marketing/CS, kursy FX, kalendarz kampanii i release.
- Wyjścia: dashboardy/raporty, alerty, harmonogram przeglądów (weekly/QBR), log zmian definicji, lista ownerów KPI, action items i backlog zmian danych.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: sales_performance_report, go_to_market_strategy, product_strategy_document, pricing_engine_design, analytics_strategy, data_quality_plan.
- Dependencies: CRM/CPQ/Billing/Marketing/CS źródła, definicje KPI/OKR, data contracts, governance danych, narzędzia BI/alerting.


## Zależności dokumentu

- Upstream: definicje KPI/OKR, źródła danych i kontrakty, targety, polityki danych.
- Downstream: cotygodniowe/kwartalne przeglądy, action items, roadmapy działań, audyt i compliance.
- Zewnętrzne: FX, sezonowość/święta, zdarzenia rynkowe.


## Fazy cyklu życia

- Ustalenie definicji i właścicieli KPI.
- Budowa dashboardów/alertów i testy jakości danych.
- Operacyjne przeglądy i iteracje (retrospektywy danych/KPI).



## Struktura sekcji (szkielet)

1) Streszczenie i cele monitoringu (early warning, decyzje)
2) Zakres KPI/OKR i definicje (bookings/revenue/NRR/churn/win rate/cycle/ACV itp.)
3) Źródła danych, jakość i kontrakty (CRM/CPQ/Billing/Marketing/CS, FX)
4) Dashboardy i alerty (narzędzia, progi, routing, SLO danych)
5) Ownership i proces przeglądów (cadence weekly/QBR, agenda, notatki, action items)
6) Wersjonowanie definicji i audyt zmian (kto, kiedy, dlaczego)
7) Zgodność i bezpieczeństwo danych (PII/PCI/GDPR, maskowanie, dostęp)
8) Ryzyka i plan doskonalenia danych/KPI; decyzje (ADR) i otwarte pytania


## Szybkie powiązania

- sales_performance_report, go_to_market_strategy, product_strategy_document, pricing_engine_design, analytics_strategy, data_quality_plan, risk_register


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
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

- [ ] KPI mają definicję, ownera, źródło, próg alertu; dane spełniają SLO.
- [ ] Alerty są routowane; przeglądy odbywają się wg cadence; action items śledzone.
- [ ] Zmiany definicji są wersjonowane i komunikowane; zgodność danych uwzględniona.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Tabela KPI, dashboardy/alerty (linki), log zmian definicji, notatki z przeglądów, action items log, ADR log.


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

- Definicje KPI → źródła/dane → dashboard/alerty → przeglądy → action items → rewizje KPI.
- Zmiana definicji → wersjonowanie → komunikacja → audyt.


## Wymagane rozwinięcia

- Tabela KPI z definicją, źródłem, ownerem, częstotliwością, progiem alertu.
- Opis dashboardów i alertów (linki), routing alertów, SLO dla danych.
- Log zmian definicji KPI, procedura wprowadzania zmian i komunikacji.


## Wymagane streszczenia

- Executive summary: top odchylenia vs target, alerty krytyczne, top action items.
- One-pager: lista KPI z progami, właściciele, cadence przeglądów.


## Guidance (skrót)

- DoR: uzgodnione definicje KPI/OKR i targety; dostęp do źródeł; narzędzia BI/alerting; ownerzy KPI.
- DoD: dashboardy/alerty działają; przeglądy w kalendarzu; log zmian i procedura komunikacji; ryzyka/założenia opisane; metadane aktualne; dokument w linkage_index.
- Spójność: KPI zgodne z definicją, dane mają SLO jakości, alerty mają routing i progi, zmiany są wersjonowane i audytowane.


## Checklisty Definition of Ready (DoR)

- [ ] Definicje KPI/OKR i targety uzgodnione; źródła danych i narzędzia dostępne; ownerzy KPI wyznaczeni.


## Checklisty Definition of Done (DoD)

- [ ] Dashboardy/alerty skonfigurowane, działające SLO danych; proces przeglądów i log zmian KPI wdrożony.
- [ ] Ryzyka/założenia opisane; metadane aktualne; dokument w linkage_index.

