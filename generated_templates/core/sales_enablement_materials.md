---
title: Sales Enablement Materials
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Sales Enablement Materials


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Opisuje i standaryzuje pakiet materiałów enablement dla sprzedaży/CS/partnerów: co tworzymy, dla kogo, w jakiej formie, z jakimi komunikatami i miernikami użycia/efektywności. Celem jest skrócenie time-to-first-closed i zwiększenie win rate.


## Zakres i granice

- Obejmuje: messaging/value props, battlecards, demo scripts, objection handling, case studies, FAQ, pricing/packaging highlights, competitive intel, compliance/privacy notes, checklista aktualizacji i dystrybucji, metryki użycia/efektywności.
- Poza zakresem: pełne playbooki sprzedażowe (osobny dokument), szczegółowe umowy prawne.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: product/GTM messaging, ICP/persony, konkurencja, pricing/packaging, regulacje (treści/dane/płatności), feedback sprzedaży/CS, wyniki demo/PQL, brand guidelines.
- Wyjścia: zestaw materiałów enablement (battlecards, decki, skrypty demo/objections, FAQ, case studies, compliance notes), repo dystrybucji, plan aktualizacji, KPI użycia/efektywności.


## Założenia
- Dane i logi są dostępne; platforma A/B działa.  
- Zespół ma możliwość szybkiego rollbacku konfiguracji.  
- Metryki są zdefiniowane i monitorowane.
## Otwarte pytania
- Jak obsłużyć sezonowość zapytań w metrykach?  
- Jak długo trzymać warianty A/B?  
- Jak łączyć metryki online z ankietami jakości?
## Powiązania (meta)

- Key Documents: product_strategy_document, go_to_market_strategy, go_to_market_vision, pricing_engine_design, sales_training_on_solution, sales_performance_report, marketing_plan, partner_program.
- Document Structures: ICP → messaging → materiały → kanały → KPI.
- Dependencies: brand/compliance wytyczne, dane konkurencji/pricing, aktualne fakty o produkcie, dostęp do repo i narzędzi (LMS/CRM/CPQ).


## Zależności dokumentu

- Upstream: strategia produktu/GTM, pricing/packaging, regulacje, decyzje brand/comms.
- Downstream: szkolenia enablement, kampanie marketingowe, playbooki sprzedażowe, CS/support playbooks, raporty KPI.
- Zewnętrzne: partnerzy/resellery, marketplace guidelines, regulacje treści/płatności/danych.


## Fazy cyklu życia

- Discovery: ICP, pain points, konkurencja, luki w materiałach.
- Design: messaging, pakiet materiałów, kanały dystrybucji, KPI.
- Rollout: publikacja, szkolenia, pilot na wybranych zespołach.
- Monitoring i rewizje: usage/feedback, A/B, aktualizacje kwartalne.



## Struktura sekcji (szkielet)

1) Streszczenie i cel (czas do produktywności, win rate)
2) ICP/persony i kluczowe use case’y
3) Messaging/value props i pozycjonowanie (różnicowanie vs konkurencja)
4) Pakiet materiałów (battlecards, deck, demo script, objections, FAQ, case studies, pricing highlights, compliance notes)
5) Kanały i formaty dystrybucji (repo, LMS, CRM/CPQ integracje, wersjonowanie)
6) KPI/KR i pomiar (użycie, win rate, deal cycle, PQL→SQL, CSAT/NPS z demo)
7) Proces aktualizacji i governance (częstotliwość, ownerzy, feedback loop, A/B)
8) Ryzyka i założenia (brand/regulacje, nieaktualne dane, spójność messagingu)
9) Decyzje (ADR) i otwarte pytania


## Szybkie powiązania

- product_strategy_document, go_to_market_strategy, go_to_market_vision, pricing_engine_design, sales_training_on_solution, sales_performance_report, marketing_plan, partner_program


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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
- NDCG: Normalized Discounted Cumulative Gain.  
- Zero results rate: odsetek zapytań bez wyników.  
- Budget ruchu: procent ruchu przeznaczony na eksperyment.
## Przykłady użycia
- Tuning boostów popularności vs świeżość.  
- Dodanie synonimów dla branżowych zapytań.  
- Regulacja scoringu wektorowego i BM25 w hybrydzie.
## Ryzyka i ograniczenia
- Eksperymenty bez reprezentatywności → złe wnioski.  
- Brak rollback → utrzymana degradacja.  
- Zbyt częste zmiany → niestabilne metryki.  
- Niepełne logi → ślepe tuningi.
## Decyzje i uzasadnienia
- Kadencja tuningów i budżet ruchu.  
- Progi decyzji rollout/rollback.  
- Zakres logowania/segmentów.  
- Priorytetyzacja hipotez (impact/effort).
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

- [ ] Każdy materiał ma ownera, datę rewizji i spójny messaging.
- [ ] KPI mierzą użycie i wpływ na win rate/deal cycle; feedback loop działa.
- [ ] Kanały dystrybucji i wersjonowanie działają; compliance/brand uwzględnione.

## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Repo materiałów (decki, battlecards, FAQ, case studies), demo scripts, objection handling, compliance notes, dashboard KPI, plan szkoleń, ADR log.


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

- ICP/value prop → messaging → materiały → KPI użycia/efektywności.
- Pricing/konkurencja → battlecards → objection handling → deal velocity/win rate.


## Wymagane rozwinięcia

- Spis materiałów i właścicieli, linki do repo, SLA aktualizacji.
- Battlecards (pain/value/proof/objections), demo script, objection handling, FAQ, case studies, compliance notes.
- Plan szkoleń enablement (kickoff, refresh), integracja z CRM/CPQ/LMS.
- KPI dashboard (użycie, win rate, cycle time, adoption, feedback).


## Wymagane streszczenia

- Executive summary: ICP, messaging, pakiet, kanały, KPI, ryzyka.
- One-pager: co/komu/jak, top 3 materiały, terminy aktualizacji.


## Guidance (skrót)

- DoR: ICP/persony, konkurencja, pricing, brand/regulacje znane; feedback z sales/CS zebrany; ownerzy materiałów wyznaczeni.
- DoD: pakiet materiałów opublikowany w repo z wersjonowaniem; KPI i dashboard; plan aktualizacji i szkoleń; ryzyka/założenia; metadane aktualne; dokument w linkage_index.
- Spójność: messaging spójny z product i pricing; materiały mają właścicieli i daty rewizji; KPI mierzą użycie i efekt na win rate/deal cycle.


## Checklisty Definition of Ready (DoR)

- [ ] ICP/persony i konkurencja opisane; pricing/packaging znane; brand/regulacje uwzględnione.
- [ ] Ownerzy materiałów i kanały dystrybucji ustalone; feedback z sales/CS zebrany.


## Checklisty Definition of Done (DoD)

- [ ] Pakiet materiałów opublikowany i wersjonowany; KPI użycia/efektywności zdefiniowane i mierzone.
- [ ] Plan aktualizacji/szkoleń, ryzyka/założenia; metadane aktualne; dokument w linkage_index.

