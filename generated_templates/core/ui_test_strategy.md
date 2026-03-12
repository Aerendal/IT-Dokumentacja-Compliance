---
title: UI Test Strategy
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# UI Test Strategy


## Metadane

- Właściciel: QA Lead
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zdefiniować strategię testów interfejsu użytkownika zapewniającą zgodność z wymaganiami funkcjonalnymi, dostępności, wydajności i bezpieczeństwa frontendu. Dokument kieruje wyborem narzędzi, piramidą testów, kryteriami jakości oraz integracją z CI/CD.


## Zakres i granice

- Obejmuje: testy jednostkowe komponentów, testy integracyjne UI, e2e (user flows), regresję wizualną, dostępność (WCAG), użyteczność techniczną, wydajność ładowania i interakcji, testy na różnych przeglądarkach/urządzeniach, dane testowe, mocki/stuby, raportowanie.  
- Poza zakresem: pełne badania UX/produktowe (oddzielne badania), testy back‑endowe API (osobne strategie), testy manualne eksploracyjne (opisane w playbooku QA).


## Użytkownicy i interesariusze
- **QA Lead / Test Manager** — planuje strategię testowania i zarządza procesem QA
- **QA Engineer** — projektuje i wykonuje przypadki testowe
- **Development Team** — naprawia defekty i dostarcza testowalny kod
- **Product Owner** — definiuje kryteria akceptacji i priorytetyzuje defekty

## Wejścia i wyjścia

- Wejścia: wymagania funkcjonalne/non‑functional, makiety/Design System, definicje dostępności, kryteria wydajności (LCP, INP), lista przeglądarek/urządzeń, dane testowe, kontrakty API, ryzyka.  
- Wyjścia: piramida testów i pokrycie, plan narzędzi (unit/integration/e2e/visual/a11y/perf), scenariusze krytycznych ścieżek, matryca zgodności przeglądarek/urządzeń, raporty jakości, checklisty DoR/DoD.


## Założenia

- CI/CD dostępne z równoległością; testy mogą działać izolowanie.  
- Mocki/stuby dostępne; feature flags do sterowania stanem UI.  
- Zespół ma dostęp do browser farm/device lab.


## Otwarte pytania

- Jakie procentowe pokrycie UI jest minimalnym celem?  
- Czy produkcyjny RUM będzie blokował release przy regresji?  
- Jak często aktualizować listę wspieranych przeglądarek/urządzeń?  
- Jak klasyfikować i egzekwować wyjątki a11y?

## Powiązania (meta)

- Key Documents: testing_methodology_training, accessibility_improvement_plan, api_test_strategy, performance_testing_plan, release_readiness_statement, change_management.  
- Key Document Structures: piramida testów, krytyczne ścieżki, dane/mocks, środowiska/CI, raporty.  
- Document Dependencies: CI/CD, feature flags, test runner (Jest/Vitest), e2e (Playwright/Cypress), snapshot/visual (Percy/Applitools), a11y linters (axe), browser farm, analytics dla real-user metrics (RUM).


## Zależności dokumentu

Wymaga: zdefiniowanych krytycznych ścieżek użytkownika, listy docelowych urządzeń/przeglądarek, akceptowalnych progów wydajności, kontraktów API, dostępnych środowisk testowych, polityki danych testowych. Braki = blokery DoR.


## Fazy cyklu życia

- Definicja kryteriów jakości i piramidy.  
- Przygotowanie środowisk, danych i narzędzi.  
- Implementacja i automatyzacja testów.  
- Ciągła regresja w CI/CD.  
- Raportowanie i doskonalenie.



## Struktura sekcji (szkielet)
- Cel, zakres i założenia
- Ryzyka jakości i priorytety (macierz ryzyko→test)
- Poziomy testów i zakres (unit, contract, integration, e2e, UAT, perf, sec, UX/a11y)
- Strategie danych testowych i środowisk
- Automatyzacja: kryteria, narzędzia, coverage, pipeline CI/CD
- Metryki i raportowanie (defect density, MTTR, test pass rate, flaki)
- Kryteria wejścia/wyjścia i Go/No-Go
- RACI i komunikacja
## Szybkie powiązania

- linkage_index.jsonl (ui/test/strategy)  
- accessibility_improvement_plan, performance_testing_plan, api_test_strategy


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

1. Zidentyfikuj krytyczne ścieżki i priorytety.  
2. Dobierz narzędzia i zbuduj piramidę testów z danymi/mocks.  
3. Włącz testy w CI/CD; ustaw budżety i alerty.  
4. Monitoruj flakiness i pokrycie; aktualizuj strategię i DoD.


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

- Flakiness: zmienny wynik testu bez zmiany kodu.  
- Budget performance: maksymalne dopuszczalne wartości metryk web vitals.  
- Visual regression: różnica wyglądu UI przekraczająca próg tolerancji.


## Przykłady użycia

- Dodanie nowego checkout flow z testami e2e + visual.  
- Audyt a11y dla głównej strony i panelu admina.  
- Wykrycie regresji LCP po zmianie obrazów hero.


## Ryzyka i ograniczenia

- Zbyt wiele e2e → długie pipeline’y i flakiness.  
- Brak budżetów perf → regresje użytkowe.  
- Niespójne dane testowe → fałszywe alarmy.  
- Pominięta a11y → niezgodność WCAG i ryzyko prawne.


## Decyzje i uzasadnienia

- Wybór narzędzi (Playwright/Cypress, axe, visual tool).  
- Progi flakiness i retry policy.  
- Budżety LCP/INP i blokery releasu.  
- Zakres manualnych a11y i kompatybilności.


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

- Piramida testów ↔ Dobór narzędzi ↔ CI/CD.  
- Dane/mocks ↔ Stabilność testów e2e ↔ Raportowanie.  
- Dostępność ↔ Visual ↔ Kryteria wyjścia release.


## Struktura sekcji

1) Kryteria jakości (funkcja, a11y, perf, bezpieczeństwo UI)  
2) Piramida testów i pokrycie (unit → integration → e2e → visual/a11y/perf)  
3) Narzędzia i standardy (linters, test runners, snapshot/visual, a11y, perf)  
4) Dane i mocki; kontrakty API; feature flags  
5) Środowiska, CI/CD, równoległość, retry/flaky policy  
6) Raportowanie, metryki (pass rate, MTTR testów, flakiness)  
7) DoR/DoD i kryteria releasu  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Lista krytycznych user flows z priorytetem.  
- Macierz pokrycia: komponenty → testy.  
- Polityka snapshot/visual (co, kiedy aktualizować).  
- Polityka flakiness: retry, quarantine, obowiązek naprawy.  
- Plan a11y (WCAG poziomy, narzędzia, manual checks).  
- Budżety wydajności (LCP/INP/TTI) i sposób pomiaru (lab/RUM).


## Wymagane streszczenia

- Executive summary: stan pokrycia, flakiness, top ryzyka releasu.  
- Krótka matryca przeglądarek/urządzeń i wyników a11y/perf.


## Guidance (skrót)

- Utrzymuj większość testów jako unit/integration; e2e tylko dla krytycznych ścieżek.  
- Mockuj nie-deterministyczne zależności; kontrakty API waliduj osobno.  
- Flaky test = bug; napraw w sprincie, nie odkładaj.  
- Automatyczne a11y + punktowe manualne; failuj release przy krytycznych.  
- Budżety wydajności w CI; blokuj build przy regresji.  
- Raportuj wyniki w jednym panelu (CI + jakości + RUM).


## Checklisty Definition of Ready (DoR)

- [ ] Krytyczne ścieżki i wymagania a11y/perf zdefiniowane.  
- [ ] Lista przeglądarek/urządzeń i środowisk testowych.  
- [ ] Dane testowe/mocks przygotowane; kontrakty API dostępne.  
- [ ] Narzędzia testowe i integracje CI ustalone.  
- [ ] Kryteria wyjścia releasu (quality gate) uzgodnione.


## Checklisty Definition of Done (DoD)

- [ ] Testy unit/integration/e2e/visual/a11y/perf uruchamiają się w CI i przechodzą.  
- [ ] Flaky < uzgodniony próg; naprawy w backlogu.  
- [ ] Raport jakości dostępny; budżety perf nieprzekroczone.  
- [ ] Wyniki a11y (WCAG) udokumentowane; wyjątki zatwierdzone.  
- [ ] linkage_index i metryki pokrycia zaktualizowane.

