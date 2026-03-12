---
title: ARIA Patterns Library
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# ARIA Patterns Library


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Biblioteka wzorców ARIA dla komponentów UI: role, atrybuty, stany i przykłady. Celem jest zapewnienie zgodności z WCAG/ARIA i spójne doświadczenie dla użytkowników AT.


## Zakres i granice

- Obejmuje: komponenty (menu, dialog, tabs, accordion, alert, form controls, toast, table, modal, combobox), role/aria-* wymagane i zalecane, focus management, keyboard nav, live regions, error states, przykłady kodu, testy manual/auto, checklisty.  
- Poza zakresem: pełny design system (linkowany), styling CSS (tylko minimalne wskazówki).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wytyczne WCAG/ARIA, design system komponentów, wymagania produktów, wyniki audytów A11y, lista urządzeń/AT.  
- Wyjścia: wzorce i snippet’y kodu, checklisty DoR/DoD, scenariusze testów AT, tabela ról/atrybutów, linki do komponentów DS.


## Założenia

- Istnieje design system z komponentami.  
- Zespół ma dostęp do SR i narzędzi.  
- Polityki A11y obowiązują.


## Otwarte pytania

- Jakie lokalizacje/języki wymagają dodatkowych ARIA-label?  
- Jak często audytować DS pod kątem A11y?  
- Czy trzeba wspierać high-contrast mode?


## Powiązania (meta)

- Key Documents: accessibility_compliance, design_system_guidelines, keyboard_navigation_standard, error_handling_guidelines, testing_plan_accessibility.  
- Key Document Structures: komponent, role/atrybuty, focus/keyboard, testy, przykłady.  
- Document Dependencies: design system repo, storybook, lint/rules, test tooling (axe, pa11y), screen readers.


## Zależności dokumentu

Wymaga: aktualnych komponentów DS, wytycznych WCAG/ARIA, listy docelowych AT/przeglądarek, narzędzi testowych. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja wzorców.  
- Integracja z DS/komponentami.  
- Audyty i aktualizacje po zmianach WCAG/produktów.



## Struktura sekcji (szkielet)
- Cel i zakres zbioru
- Taksonomia i definicje
- Standardy/wytyczne
- Szablony/wzorce z przykładami
- Kryteria jakości i walidacja
- Utrzymanie i sposób zgłaszania zmian
## Szybkie powiązania

- linkage_index.jsonl (aria/patterns/library)  
- design_system_guidelines, accessibility_compliance, testing_plan_accessibility


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

1. Wybierz komponent; zastosuj tabelę role/aria/keyboard.  
2. Implementuj z przykładami; uruchom testy auto + manual.  
3. Zaktualizuj checklisty/PR; odnotuj w linkage_index; zaplanuj audyt regresji.


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

## Powiązania sekcja↔sekcja

- Role/aria → Focus/keyboard → Testy AT.  
- Error states → Live regions → Komunikaty.  
- Przykłady → Checklisty → Audyty.


## Struktura sekcji

1) Zakres i cele A11y  
2) Lista komponentów i wymogów ARIA/keyboard/focus  
3) Role/aria-* i stany (required/recommended)  
4) Focus management i kolejność TAB  
5) Keyboard interactions per komponent  
6) Live regions i komunikaty błędów/sukcesów  
7) Przykłady kodu (HTML/JS/React)  
8) Testy A11y (manual/auto, SR scenariusze)  
9) Checklisty i maintenance (audyty, regresje)  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Tabele role/aria/states per komponent.  
- Scenariusze keyboard i SR (NVDA/JAWS/VoiceOver).  
- Snippety DS/React z hookami focus.  
- Lista testów automatycznych i manualnych.


## Wymagane streszczenia

- One‑pager: minimalne wymagania ARIA/keyboard dla kluczowych komponentów.  
- Snapshot audytu A11y (pass/fail, top błędy).


## Guidance (skrót)

- Zacznij od semantycznego HTML; ARIA dodawaj tam, gdzie potrzebne.  
- Zapewnij focus management i klawisze zgodne ze wzorcami WAI-ARIA Authoring Practices.  
- Używaj live regionów do dynamicznych komunikatów; unikaj nadmiaru.  
- Testuj na docelowych SR/przeglądarkach; automaty + manual.  
- Wymuś checklisty w PR/CI.


## Checklisty Definition of Ready (DoR)

- [ ] Komponent i wymagania A11y zidentyfikowane.  
- [ ] Wytyczne WCAG/ARIA i APG dostępne.  
- [ ] Docelowe AT/przeglądarki znane.  
- [ ] Test tools (axe, SR) dostępne.  
- [ ] Wersja komponentu w DS ustalona.


## Checklisty Definition of Done (DoD)

- [ ] Role/aria/keyboard zaimplementowane; testy auto+manual zaliczone; status/wersja/data uzupełnione.  
- [ ] Snippety i checklisty opublikowane w DS; linkage_index zaktualizowany.  
- [ ] Audyt A11y pass lub wyjątki/waivery opisane.  
- [ ] Scenariusze SR i focus documented.  
- [ ] Plan regresji A11y ustawiony.

