---
title: Sales Support Plan
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Sales Support Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Definiuje, jak organizacja wspiera sprzedaż w cyklu pre-/post-sale: wsparcie techniczne i operacyjne, narzędzia, SLA/OLA, eskalacje, runbooki, mierzenie skuteczności i satysfakcji.


## Zakres i granice

- Obejmuje: zakres wsparcia (pre-sale, PoC, oferty, RFP), kanały kontaktu, SLA/OLA, narzędzia (CRM/CPQ/Support), role i RACI, proces eskalacji, szablony/artefakty, metryki (czas reakcji, wygrane z supportem, CSAT), runbooki referencyjne.
- Poza zakresem: ogólne playbooki sprzedażowe (osobny dokument), pełne SOP-y techniczne (w runbookach technicznych).


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: proces sprzedaży/GTM, SLA/OLA firmowe, katalog produktów/feature flag, regulacje/umowy, narzędzia (CRM/CPQ/Support), kalendarz release, ryzyka znane.
- Wyjścia: plan wsparcia (role, kanały, SLA/OLA, eskalacje), zestaw runbooków i szablonów (odpowiedzi na RFP, PoC, demo), plan szkoleń, dashboard KPI, harmonogram aktualizacji.


## Założenia
- Dane i interesariusze dostępni.  
- Budżet/własność zatwierdzone.  
- Strategia firmy stabilna.
## Otwarte pytania
- Jakie są zależności z innymi programami?  
- Jakie ryzyka prawne/regulacyjne?  
- Jakie są limity budżetu/czasu?
## Powiązania (meta)

- Key Documents: go_to_market_strategy, go_to_market_vision, product_roadmap, pricing_engine_design, sales_enablement_materials, incident_response_playbook, change_management_process, solution_support_plan.
- Document Structures: etap sprzedaży → wsparcie → artefakty → KPI.
- Dependencies: release calendar, feature flags, product docs, SLAs firmowe, narzędzia CRM/CPQ/Support.
- RACI: Sales, Sales Engineering, Support, Product, Legal/Compliance, Finance, Security.


## Zależności dokumentu

- Upstream: strategia GTM, roadmap, polityki SLA/OLA, product docs, release plan.
- Downstream: runbooki, szkolenia, dashboardy KPI, kontrakty/umowy, PoC playbooks.
- Zewnętrzne: partnerzy/klienci (kanały kontaktu), narzędzia supportu, regulator (jeśli dot. treści/płatności/danych).


## Fazy cyklu życia

- Discovery: potrzeby zespołów sprzedaży, luki wsparcia, SLA/OLA.
- Design: role, kanały, SLA/OLA, eskalacje, szablony i runbooki, KPI.
- Rollout: publikacja, szkolenia, pilot, dostrojenie SLA/OLA.
- Monitoring i rewizje: KPI/CSAT, retrospektywy, aktualizacje kwartalne.



## Struktura sekcji (szkielet)

1) Streszczenie i cel (KPI: win rate, time-to-response, CSAT)
2) Zakres wsparcia (pre-sale/PoC/oferty/RFP/post-sale handoff)
3) Role i RACI (Sales, SE, Support, Product, Legal/Compliance, Finance, Security)
4) Kanały i SLA/OLA (kontakt, czasy, okna, języki, coverage)
5) Proces eskalacji i komunikacja (drabinka, on-call, wyjątki)
6) Runbooki i szablony (PoC/demo, RFP, security/IT questionnaires, pricing/CPQ wsparcie)
7) Narzędzia i integracje (CRM/CPQ/Support, tagowanie, raportowanie)
8) KPI/KR i pomiar (win rate z supportem, czas reakcji/rozwiązania, CSAT/NPS, deal cycle)
9) Plan szkoleń i aktualizacji (cadence, ownerzy, release/feature flag alignment)
10) Ryzyka i założenia; decyzje (ADR) i otwarte pytania


## Szybkie powiązania

- go_to_market_strategy, go_to_market_vision, product_roadmap, pricing_engine_design, sales_enablement_materials, solution_support_plan, incident_response_playbook, change_management_process


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

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
- Vision: opis „dlaczego i co”, zanim „jak”.  
- Scope: co robimy i czego nie robimy w tej iteracji.
## Przykłady użycia
- Nowa platforma danych.  
- Replatforming legacy.  
- Wprowadzenie nowej linii produktu.
## Ryzyka i ograniczenia
- Niejasny scope → creep.  
- Cele bez metryk → brak oceny sukcesu.  
- Brak alignment → sprzeczne decyzje.
## Decyzje i uzasadnienia
- Priorytety faz.  
- Architektura docelowa high-level.  
- Kryteria sukcesu.
## Powiązania z innymi dokumentami
- product_strategy — kierunek biznesu.  
- architecture_vision — kierunek tech.  
- risk_register — ryzyka.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Wewnętrzne standardy architektoniczne i procesowe.  
- Polityki prawne/compliance jeśli wpływają.
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

- [ ] Każdy etap sprzedaży ma przypisane wsparcie, kanał i SLA/OLA.
- [ ] Eskalacje mają jasną drabinkę/on-call i okna; runbooki są aktualne po release.
- [ ] KPI mierzą wpływ wsparcia na wygrane, czas reakcji i satysfakcję; raportowanie działa.

## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- SLA/OLA tabela, drabinka eskalacji, runbooki PoC/demo/RFP, szablony odpowiedzi security, dashboard KPI, ADR log.


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

- Etapy sprzedaży → rodzaj wsparcia → kanał/SLA → artefakty → KPI (win rate z supportem, time-to-response).
- Release/feature flag → materiały i runbooki → aktualizacje → komunikacja.


## Wymagane rozwinięcia

- Tabela SLA/OLA per kanał/etap, szablony RFP/odpowiedzi security, runbooki PoC/demo.
- RACI i drabinka eskalacji z kontaktami/on-call, okna czasowe, języki.
- Dashboard KPI i plan aktualizacji materiałów po release.


## Wymagane streszczenia

- Executive summary: zakres wsparcia, kanały/SLA, KPI, ryzyka.
- One-pager: kto/kiedy/jak kontakt, drabinka eskalacji, główne SLA, link do repo materiałów.


## Guidance (skrót)

- DoR: etapy sprzedaży i wymagania wsparcia zebrane; SLA/OLA firmowe znane; ownerzy kanałów; dostęp do product/release info.
- DoD: role/RACI, kanały, SLA/OLA, eskalacje, runbooki/szablony, KPI/dashboard, plan szkoleń/aktualizacji; metadane aktualne; dokument w linkage_index.
- Spójność: każde zapytanie ma kanał i SLA; runbooki i materiały są wersjonowane; KPI mierzą wpływ wsparcia na wygrane i czas odpowiedzi.


## Checklisty Definition of Ready (DoR)

- [ ] Etapy sprzedaży i wymagania wsparcia opisane; SLA/OLA firmowe znane; ownerzy kanałów.
- [ ] Dostęp do aktualnych product/release info i materiałów.


## Checklisty Definition of Done (DoD)

- [ ] Kanały, SLA/OLA, eskalacje, runbooki/szablony, KPI/dashboard opisane; plan szkoleń/aktualizacji.
- [ ] Ryzyka/założenia opisane; metadane aktualne; dokument w linkage_index.

