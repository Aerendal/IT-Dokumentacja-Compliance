---
title: ARIA Implementation Design
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# ARIA Implementation Design


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaplanować poprawne użycie ARIA w aplikacji/web, aby zapewnić dostępność (WCAG) bez nadmiarowych atrybutów i bez łamania natywnych semantyk.


## Zakres i granice

- Obejmuje: dobór semantycznych elementów HTML, minimalne i właściwe użycie ARIA, role/states/properties, focus management, keyboard navigation, live regions, formularze i walidacje, komponenty custom (dropdown, modal, tabs), testy a11y (manual/automaty).  
- Poza zakresem: pełne wytyczne WCAG (osobny dokument), projekt UI/UX.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: komponenty i wzorce UI, wymagania WCAG, lista komponentów custom, narzędzia a11y (linters, axe, screen reader), target platformy/przeglądarki.  
- Wyjścia: specyfikacja ARIA per komponent, checklisty DoR/DoD, zasady focus i klawiatury, wytyczne testów, przykłady kodu, lista antywzorów.


## Założenia

- Design system jest dostępny do modyfikacji.  
- Zespół ma podstawy a11y.  
- Narzędzia SR działają na docelowych platformach.


## Otwarte pytania

- Jak często audytować a11y po releasach?  
- Czy wspierać wszystkie języki w SR (lokalizacja labeli)?  
- Jak raportować pokrycie a11y w CI?

## Powiązania (meta)

- Key Documents: accessibility_improvement_plan, ui_test_strategy, error_handling_standards, semantic_html_implementation, wcag_level_requirements.  
- Key Document Structures: komponenty, role/properties, focus, keyboard, live regions, testy.  
- Document Dependencies: design system, linting/CI, screen readers, test automation.


## Zależności dokumentu

Wymaga: listy komponentów i ich zachowań, standardów WCAG (poziom), decyzji dot. design systemu, narzędzi testowych, polityk dla języków/RTL. Brak = brak DoR.


## Fazy cyklu życia

- Inwentaryzacja komponentów i potrzeb ARIA.  
- Projekt roli/properties i focus/keyboard.  
- Implementacja i testy a11y.  
- Review i release.  
- Audyty okresowe.



## Struktura sekcji (szkielet)
- Streszczenie i cele biznesowe
- Zakres, założenia, ograniczenia
- Kontekst domenowy i interesariusze
- Wymagania funkcjonalne i niefunkcjonalne
- Architektura/komponenty i integracje
- Model danych i przepływy informacji
- Bezpieczeństwo, prywatność i compliance
- Plan wdrożenia/migracji i kryteria go/no-go
- Monitoring/operacje oraz ryzyka i mitigacje
- Decyzje i uzasadnienia, pytania otwarte
## Szybkie powiązania

- linkage_index.jsonl (aria/implementation/design)  
- accessibility_improvement_plan, ui_test_strategy, semantic_html_implementation


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

1. Wybierz komponenty; przypisz role/properties i mapę klawiatury.  
2. Implementuj; testuj klawiaturą i SR.  
3. Uruchom automaty (axe/lint) i review a11y.  
4. Zatwierdź, opublikuj; zaktualizuj dokument i linkage_index.


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

- Roving tabindex: technika sterowania focus w listach/menus.  
- Live region: miejsce, gdzie SR czyta dynamiczne zmiany.  
- Antywzór: błędne użycie ARIA psujące dostępność.


## Przykłady użycia

- Projekt modala z trap focus i aria-modal/labelledby.  
- Dropdown z roving tabindex i rolami menuitem.  
- Formularz z aria-invalid/errormessage i live region status.


## Ryzyka i ograniczenia

- Nadmiar ARIA → chaos i gorsza dostępność.  
- Brak focus management → UX niedostępne.  
- Brak testów SR → niewidoczne błędy.  
- Niespójność z design systemem → regresje.


## Decyzje i uzasadnienia

- Poziom WCAG (A/AA) i komponenty krytyczne.  
- Które komponenty wymagają ARIA vs natywne.  
- Narzędzia SR do testów i ich kadencja.  
- Polityka przeglądów a11y w CI/CD.


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

- Role/properties ↔ Focus/keyboard ↔ Testy.  
- Live regions ↔ Dynamic content ↔ Error handling.  
- Antywzory ↔ Review ↔ QA.


## Struktura sekcji

1) Zakres komponentów i poziom WCAG  
2) Role/ARIA per komponent (wzorce i antywzory)  
3) Focus i nawigacja klawiaturą (tab order, roving tabindex)  
4) Live regions i komunikaty (status, alert)  
5) Formularze i walidacje (aria-invalid, describedby)  
6) Testy (manual, SR: NVDA/JAWS/VoiceOver, axe/lint)  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Tabela komponent → rola, properties, keyboard map.  
- Wzorce dla modali, dropdownów, tabs, menus, autocomplete.  
- Reguły focus (trap, return focus) i skip links.  
- Live region use (status/alert) i komunikaty błędów.  
- Checklista testów SR i narzędzi (axe/lint).  
- Lista antywzorów (div‑aria, role presentation na form controls).


## Wymagane streszczenia

- Executive summary: poziom WCAG, komponenty krytyczne.  
- Skrót zasad focus/keyboard i najważniejszych ról.


## Guidance (skrót)

- Preferuj natywne elementy; ARIA tylko gdy konieczne.  
- Zachowaj poprawny focus order; testuj klawiaturą.  
- Używaj roli zgodnie z semantyką; unikaj duplikacji.  
- Komunikuj błędy/zmiany przez live regions; zapewnij opis (label/description).  
- Audytuj z SR + automaty; poprawiaj antywzory.  
- Aktualizuj linkage_index po zmianach design systemu.


## Checklisty Definition of Ready (DoR)

- [ ] Lista komponentów i poziom WCAG określone.  
- [ ] Narzędzia testowe (SR, axe/lint) dostępne.  
- [ ] Decyzje design systemu i RTL/lokalizacja znane.  
- [ ] Plan testów manual + automatycznych gotowy.  
- [ ] Role właścicieli i reviewerów ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Komponenty zaimplementowane zgodnie z rolami/props.  
- [ ] Focus/keyboard i live regions zweryfikowane w SR.  
- [ ] Automaty a11y zielone; brak krytycznych issue.  
- [ ] Dokumentacja/linkage_index zaktualizowane.  
- [ ] Brak antywzorów (div‑aria itp.) w code review.

