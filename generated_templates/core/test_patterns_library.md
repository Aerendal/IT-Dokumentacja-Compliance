---
title: Test Patterns Library
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Test Patterns Library


## Metadane

- Właściciel: QA Lead
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zebrać wzorce testowe (setup/act/assert, parametrization, fixtures) do wielokrotnego użycia.


## Zakres i granice

- Obejmuje: wzorce dla unit/integration/API/UI, parametrization, fixtures/mocks, anty-wzorce, przykłady.
- Poza zakresem: specyficzne testy domenowe.


## Użytkownicy i interesariusze
- **QA Lead / Test Manager** — planuje strategię testowania i zarządza procesem QA
- **QA Engineer** — projektuje i wykonuje przypadki testowe
- **Development Team** — naprawia defekty i dostarcza testowalny kod
- **Product Owner** — definiuje kryteria akceptacji i priorytetyzuje defekty

## Wejścia i wyjścia
- Wejścia: cele biznesowe, backlog/epiki, wymagania niefunkcjonalne, ograniczenia prawne/techniczne, istniejące systemy/dane.
- Wyjścia: zaakceptowana wersja dokumentu, decyzje architektoniczne/procesowe, action items z właścicielami i terminami.
## Założenia
- Istnieje design system z komponentami.  
- Zespół ma dostęp do SR i narzędzi.  
- Polityki A11y obowiązują.
## Otwarte pytania
- Jakie lokalizacje/języki wymagają dodatkowych ARIA-label?  
- Jak często audytować DS pod kątem A11y?  
- Czy trzeba wspierać high-contrast mode?
## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)

- Kontekst i cele
- Wzorce (kategorie)
- Anti-patterns
- Przykłady kodu
- Wytyczne użycia
- Ryzyka


## Szybkie powiązania
- ui-ux-patterns-library
- solution-patterns-library
- integration-patterns-library
- infrastructure-patterns-library
- documentation-patterns-library

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
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

- Wypełnij sekcje według szkieletu; jeśli sekcja N/A, uzasadnij.
- Dodaj quick-links i uzupełnij checklisty DoR/DoD w reports/checklist_atomic.jsonl.
- Po review zaktualizuj metadane, artefakty i status.


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
- ARIA: Accessible Rich Internet Applications.  
- APG: Authoring Practices Guide.  
- Live region: obszar informujący SR o zmianach.
## Przykłady użycia
- Dodanie nowego komponentu modal w DS.  
- Audyt istniejących tabów/accordionów.  
- Naprawa błędów keyboard/focus zgłoszonych w audycie.
## Ryzyka i ograniczenia
- Nadmierne ARIA może pogorszyć UX SR.  
- Brak focus mgmt → pułapki klawiatury.  
- Brak testów SR → regresje niewidoczne.
## Decyzje i uzasadnienia
- Docelowe SR/przeglądarki do wsparcia.  
- Standard keybindings per komponent.  
- Poziom automatyzacji testów A11y.
## Powiązania z innymi dokumentami
- accessibility_compliance — standardy.  
- design_system_guidelines — komponenty.  
- testing_plan_accessibility — testy.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- WCAG 2.1 AA, WAI-ARIA APG.  
- Wewnętrzne wytyczne A11y/DS.
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

- Strategia testów
- Stack testowy
- Przykłady istniejące
- Problemy/flaki z historii


## Wyjścia

- Biblioteka wzorców
- Anti-patterns
- Checklisty DoR/DoD
- Przykłady kodu



## Szybkie powiązania (uzupełnij)

- [ ] testing_best_practices.md
- [ ] test_automation_framework_guide.md
- [ ] unit_test_documentation.md
- [ ] unit_test_specification.md
- [ ] api_testing_strategy.md
- [ ] performance_testing_plan.md


## Wymagane rozwinięcia / streszczenia

- Streszczenie kluczowych wniosków/ryzyk; rozwinięcia rekomendacji lub wzorców.


## Wymagane powiązania

- Strategia/plan testów, automatyzacja, dane/środowiska, monitoring, raportowanie release.


## Kryteria DoR

- [ ] Dane testowe/raporty dostępne
- [ ] Owner raportu/analizy przypisany
- [ ] Narzędzia raportowania działają
- [ ] Zakres release/iteracji znany


## Kryteria DoD

- [ ] Analiza/raport spisane
- [ ] Rekomendacje i ownerzy dodani
- [ ] Quick-links/checklisty uzupełnione
- [ ] Metadane/DoR/DoD zaktualizowane


## Artefakty do załączenia

- Raport/analiza
- Tabela defektów/flaky
- Dashboard/pokrycie
- Rekomendacje/plan


## Walidacja / testy

- Sanity raportów/metryk; weryfikacja spójności defektów/pokrycia.


## Metryki monitorowane

- Pass/fail rate
- Defect leakage
- Flaky rate
- Czas cyklu testów


## Utrzymanie i aktualizacje

- Przegląd co release; aktualizacja quick-links/checklist i szablonów raportów.


## Zakończenie

Po spełnieniu DoD zaktualizuj status, podlinkuj artefakty/quick-links i odhacz checklistę w reports/checklist_atomic.jsonl.
