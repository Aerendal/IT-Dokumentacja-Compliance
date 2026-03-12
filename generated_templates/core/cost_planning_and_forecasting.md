---
title: Cost Planning and Forecasting
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Cost Planning and Forecasting


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje planowanie kosztów i prognozowanie wydatków (OPEX/CAPEX) dla produktu/usług/portfela, łącząc finanse z danymi technicznymi. Ma umożliwić przewidywalność budżetu, kontrolę kosztów i decyzje inwestycyjne.


## Zakres i granice

- Obejmuje: model kosztów (infra/chmura/licencje/people/3rd party), budżety i scenariusze, forecast (krótkie/średnie), założenia (ruch, wzrost, ceny), metryki FinOps (cost/GB/call/user), alokację kosztów (tagi/chargeback/showback), ryzyka i bufory, progi alertów/anomalii, raportowanie (exec/ops), zgodność (umowy/licencje), plan działań optymalizacyjnych.
- Poza zakresem: szczegółowa księgowość (GL) – link; strategia pricingu (oddzielna).


## Użytkownicy i interesariusze

- Finance/FinOps, Product, Engineering/Infra, Leadership, Procurement/Vendor.


## Wejścia i wyjścia

- Wejścia: dane billing (cloud/on-prem/licencje), wykorzystanie (metrics/APM), plany wzrostu/ruchu, roadmapa produktu, umowy/kontrakty, kursy walut, stawki zespołów, polityki FinOps, historia kosztów, ryzyka.
- Wyjścia: budżet i forecast (scenariusze), założenia, metryki FinOps/KPI, plan optymalizacji, progi alertów, raporty (exec/ops), mapa alokacji kosztów.


## Założenia

- Dostępne są dane billing/usage i polityki FinOps; współpraca z produkt/infra/finance.


## Otwarte pytania

- Jak często rewizja założeń? 
- Jakie limity kosztów per klient/tenant?


## Powiązania (meta)

- Key Documents: finops_policy, capacity_planning, pricing_strategy, sourcing_vendor_strategy, tag_policy, budget_approval_process, risk_management_plan.
- Key Document Structures: model kosztów, scenariusze, założenia, metryki, raporty.
- Document Dependencies: billing data, usage metrics, tagging/allocations, contracts, HR rates, currency data.


## Zależności dokumentu

Wymaga: danych billing/usage, polityki tagowania/allocations, roadmapy, stawek zespołów, kontraktów/licencji, polityki FinOps. Bez tego DoR otwarte.


## Fazy cyklu życia

- Analiza danych i założeń.
- Budżet i scenariusze (base/optimistic/pessimistic).
- Forecast i aktualizacje cykliczne.
- Monitorowanie i alerty (anomalie, odchylenia vs budżet).
- Optymalizacja kosztów; retrospektywy.



## Struktura sekcji (szkielet)
- Cel i definicja sukcesu (KPI)
- Zakres, założenia i ograniczenia
- Interesariusze i role/RACI
- Kamienie milowe i daty
- Plan fal/sprintów z deliverables
- Zależności i ryzyka oraz plan mitigacji
- Budżet/zasoby i obłożenie
- Plan komunikacji i raportowania
- Kryteria akceptacji/go-live i plan rewizji
## Szybkie powiązania

- linkage_index.jsonl (finops/cost_planning)
- finops_policy, capacity_planning, pricing_strategy, sourcing_vendor_strategy, tag_policy, budget_approval_process, risk_management_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **SCRUM Guide** — Przewodnik Scrum

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

1. Zbierz dane billing/usage i założenia; zbuduj scenariusze.
2. Ustal metryki FinOps i alokacje; przygotuj budżet/forecast.
3. Skonfiguruj alerty/anomalie i raporty; zaplanuj optymalizacje.
4. Aktualizuj cyklicznie; zamknij DoR/DoD i linkage_index.


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

- OPEX/CAPEX, Unit economics, Cost per X, Showback/Chargeback, Anomalia kosztowa.


## Przykłady użycia

- Forecast chmury na 12 m-cy: base/opt/pess, alerty >10% odchylenia, plan rightsizing.
- Budżet produktu: cost per aktywny użytkownik, rezerwacje, CDN optymalizacja.


## Ryzyka i ograniczenia

- Brak tagów/allocations → złe dane; niestabilne założenia → nietrafiony forecast; opóźnione reakcje → nadmierne koszty.


## Decyzje i uzasadnienia

- [Decyzja] Scenariusze i bufory — uzasadnienie ryzyka/niepewności.
- [Decyzja] Metryki FinOps i progi alertów — uzasadnienie SLA/kosztów.


## Powiązania z innymi dokumentami

- FinOps Policy, Capacity Planning, Pricing Strategy, Sourcing/Vendor Strategy, Tag Policy, Budget Approval, Risk Management.


## Powiązania z sekcjami innych dokumentów

- Tag Policy → alokacja; Capacity → założenia; Pricing → unit economics.


## Słownik pojęć w dokumencie

- OPEX, CAPEX, Unit economics, Cost per X, Showback, Chargeback.


## Wymagane odwołania do standardów

- Polityki finansowe, FinOps, IFRS/GAAP jeśli dotyczy raportowania.


## Mapa relacji sekcja→sekcja

- Założenia → Scenariusze → Budżet/Forecast → Alerty/Raporty → Optymalizacje.


## Mapa relacji dokument→dokument

- Cost Planning → FinOps/Capacity/Pricing → Budget/Approval → Risk Mgmt.


## Ścieżki informacji

- Billing/usage → Model kosztów → Forecast → Alerty → Działania → Raporty.


## Weryfikacja spójności

- [ ] Założenia spójne z roadmapą; forecast/budżet oparty na danych.
- [ ] Metryki/allocations i alerty skonfigurowane; plan optymalizacji ma ownerów.
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy driver kosztu ma metrykę i ownera; każda optymalizacja ma KPI/ETA.
- [ ] Alerty mają progi i kanały; scenariusze mają wrażliwości.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Billing/usage dane, model forecast, scenariusze, raporty, alert config, plan optymalizacji.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Finance/FinOps → Product/Engineering → Leadership → Owner sign‑off.


## Metryki jakości

- Dokładność forecast vs. rzeczywistość, czas reakcji na anomalię, % kosztu z tagami, odchylenie vs budżet, ROI z optymalizacji.

## Kryteria ukończenia

- [ ] Budżet/forecast/scenariusze gotowe; alerty/metryki/allocations ustawione; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Założenia/ruch → Forecast → Budżet → Alerty/KPI.
- Tagging/allocations → Metryki FinOps → Raporty → Decyzje optymalizacji.


## Struktura sekcji

1) Model kosztów i zakres (infra/chmura/licencje/people/3rd party)  
2) Założenia i scenariusze (ruch, wzrost, ceny, kursy)  
3) Budżet i forecast (krótki/średni; base/opt/pess)  
4) Metryki FinOps/KPI (cost/GB/call/user, unit economics)  
5) Alokacja kosztów (tagging, showback/chargeback)  
6) Alerty/anomalie i progi  
7) Raportowanie (exec/ops, cadence, dashboardy)  
8) Plan optymalizacji (działania, owner, ETA, wpływ)  
9) Ryzyka, decyzje, open issues


## Wymagane rozwinięcia

- Założenia (ruch, wzrost, ceny usług/licencji, kursy); scenariusze i wrażliwości.
- Metryki FinOps i unit economics; mapping do tagów/allocations.
- Progi alertów (odchylenie vs budżet/forecast) i kanały.


## Wymagane streszczenia

- Budżet/forecast, kluczowe założenia, top 5 driverów kosztu, plan optymalizacji.


## Guidance (skrót)

- Ustal tagging/allocations jako fundament; bez tego brak prawdziwego cost per X.
- Twórz scenariusze i wrażliwość (ruch, ceny, kursy); pilnuj buforów.
- Monitoruj regularnie odchylenia i anomalie; działaj szybko (rightsizing, rezerwacje, caching/CDN, redukcja waste).
- Powiąż metryki FinOps z KPI produktu (cost per user/GB/transaction).


## Checklisty Definition of Ready (DoR)

- [ ] Billing/usage i tagowanie dostępne; założenia zebrane.
- [ ] Roadmapa/kontrakty/stawki znane; polityka FinOps gotowa.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Budżet/forecast i scenariusze gotowe; metryki/allocations opisane.
- [ ] Alerty/raporty działają; plan optymalizacji zapisany.
- [ ] Dokument w linkage_index; wersja/data/właściciel aktualne.

