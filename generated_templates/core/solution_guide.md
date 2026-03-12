---
title: Solution Guide
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Solution Guide


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Przedstawić przewodnik rozwiązania (solution overview) dla interesariuszy: problem, propozycja, architektura, wymagania, plan wdrożenia.


## Zakres i granice

- Obejmuje: opis problemu i wartości biznesowej, persony/use‑case’y, architekturę wysokopoziomową, wymagania niefunkcjonalne, integracje, bezpieczeństwo/prywatność, plan wdrożenia i migracji, ryzyka, koszty/SLA, metryki sukcesu.
- Poza zakresem: szczegółowe specyfikacje komponentów (oddzielne dokumenty), backlog zadań.


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia
- Wejścia: insighty z badań/rynku/klientów, dane produktowe/operacyjne, KPI biznesowe, mapy procesów, strategia firmy/produktu, ograniczenia techniczne/prawne/finansowe, polityki security/compliance, dostępne capability/platformy.
- Wyjścia: karta wizji (one-pager), mapa architektury high-level, lista założeń i ryzyk, zakres/fazy i kamienie milowe, kryteria sukcesu/KPI, DoR/DoD dla kolejnych artefaktów (BRD/PRD/architektura), ścieżka komunikacji/alignment.
## Założenia
- Dane i interesariusze dostępni.  
- Budżet/własność zatwierdzone.  
- Strategia firmy stabilna.
## Otwarte pytania
- Jakie są zależności z innymi programami?  
- Jakie ryzyka prawne/regulacyjne?  
- Jakie są limity budżetu/czasu?
## Powiązania (meta)
- Key Documents: business_value_proposition, product_strategy_document, technology_strategy, market_analysis, architecture_vision, stakeholder_requirements, risk_register, roadmap, pricing_strategy, go_to_market_strategy.
- Key Document Structures: problem → wartość → cele/KPI → zakres → architektura → fazy → ryzyka/założenia → decyzje.
- Document Dependencies: KPI dashboardy, mapy architektury/CMDB, polityki prawne/security/privacy, budżet/finansowanie, dostępne capability/platformy.
## Zależności dokumentu
Wymaga: zdefiniowanych problemów/okazji i KPI, wyników badań/rynku, głównych ograniczeń, zaangażowania kluczowych interesariuszy. Braki = DoR otwarte.
## Fazy cyklu życia
- Definicja wizji i alignment interesariuszy.
- Komunikacja i decyzje go/no-go dla kolejnych artefaktów (BRD/PRD/Architecture Concept).
- Aktualizacje przy kamieniach milowych (pilot, MVP, GA, pivot).
## Struktura sekcji (szkielet)

- Problem i cele
- Persony/use‑case’y
- Architektura (diagram) i komponenty
- Integracje i dane
- Wymagania niefunkcjonalne (SLA, bezpieczeństwo, prywatność)
- Plan wdrożenia/migracji i release’y
- Ryzyka i mitigacje
- Koszty i metryki sukcesu


## Szybkie powiązania

- Architecture Decision Records, Security/Privacy, Migration Plan, SLA/SLO, Cost/TCO.


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
1. Zbierz problem/wartość i KPI; opisz zakres.  
2. Dodaj diagram high-level i fazy; uzgodnij z interesariuszami.  
3. Aktualizuj w kamieniach milowych; uzupełnij DoR/DoD i linkage_index.
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

## Wejścia

- Wymagania biznesowe, wstępny design, ograniczenia techniczne/prawne, dane kosztowe, zależności systemowe.


## Wyjścia

- Kompaktowy opis rozwiązania z diagramem, listą wymagań, ryzyk i planem wdrożenia.



## Jak używać (checklista)

- Opisz problem i cele; dodaj persony/use‑case’y.
- Wstaw diagram architektury i opis komponentów/integracji.
- Ustal NFR (SLA, bezpieczeństwo, dane); zdefiniuj plan wdrożenia i ryzyka.
- Zapisz metryki sukcesu i koszty; podlinkuj ADR/backlog.


## Wymagane rozwinięcia / powiązania

- Diagram architektury, tabela NFR, harmonogram wdrożeń, matryca ryzyk, szacunki kosztów.


## Kryteria DoR

- Zebrane wymagania biznesowe i ograniczenia; wstępny design dostępny.


## Kryteria DoD

- Przewodnik wypełniony, uzgodniony z architekturą/bezpieczeństwem/biznesem; metryki i plan wdrożenia gotowe.


## Artefakty

- Dokument guide, diagram, tabela NFR, harmonogram, matryca ryzyk/kosztów.


## Walidacja

- Przegląd architektoniczny i bezpieczeństwa; sanity cost; zgodność z NFR.


## Metryki

- Czas od idei do decyzji go/no-go; % pokrycia NFR; odchylenie kosztu vs prognoza po wdrożeniu.


## Utrzymanie

- Aktualizacja po decyzjach ADR, zmianach zakresu lub kosztów; przegląd per release.


## Zakończenie

Solution Guide daje spójny obraz rozwiązania; utrzymuj go z decyzjami architektonicznymi i planem wdrożeń.

