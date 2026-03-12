---
title: Interaction Design
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Interaction Design


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje projekt interakcji użytkownika: przepływy, stany, wzorce, feedback, dostępność i spójność. Ma zapewnić użyteczność, klarowność i zgodność z celami biznesowymi.


## Zakres i granice

- Obejmuje: persony/scenariusze, user flows, IA, wzorce UI, stany (loading/error/empty), mikrocopy, feedback i komunikaty, kontrolki i komponenty, A11y (WCAG), input validation, responsywność/adaptację, miary UX (task success, time, CSAT/NPS).  
- Poza zakresem: pełna biblioteka komponentów (design system) – linkujemy; implementacja techniczna front‑end.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: cele produktu, wymagania funkcjonalne, badania użytkowników, dane analityczne, guidelines brand/design system, wymagania A11y, ograniczenia techniczne.  
- Wyjścia: makiety/prototypy, diagramy flow, spec interakcji, stany i mikrocopy, zasady A11y, checklisty DoR/DoD, rekomendacje testów użyteczności.


## Założenia

- Dostępny design system i narzędzia prototypowania.  
- Zespół ma wsparcie research/content/A11y.  
- Dane analityczne dostępne.


## Otwarte pytania

- Jakie są KPI UX dla tego flow?  
- Czy potrzebne są warianty językowe/lokalizacja?  
- Jakie urządzenia/przeglądarki stanowią minimum wsparcia?


## Powiązania (meta)

- Key Documents: design_system_guidelines, accessibility_compliance, ux_research_findings, product_requirements, content_style_guide, error_handling_guidelines.  
- Key Document Structures: persony/scenariusze, flow, stany, wzorce, A11y, metryki.  
- Document Dependencies: design system, analytics, prototyping tools, usability lab, lokalizacja.


## Zależności dokumentu

Wymaga: zdefiniowanych celów produktu, person i scenariuszy, danych z badań/analizy, design systemu/brand, wymagań A11y, informacji o ograniczeniach technicznych. Braki = DoR otwarte.


## Fazy cyklu życia

- Discovery i koncept.  
- Prototypowanie i testy użyteczności.  
- Spec interakcji do implementacji.  
- Audyt i iteracje po danych/feedbacku.



## Struktura sekcji (szkielet)
- Cel i kontekst biznesowy
- Interesariusze, persony i scenariusze
- Wymagania funkcjonalne (priorytety, reguły, wyjątki)
- Wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo, zgodność)
- Dane i integracje
- Kryteria akceptacji i miary sukcesu
- Zależności, ryzyka i założenia
- Śledzenie (traceability) do epik/testów
## Szybkie powiązania

- linkage_index.jsonl (interaction/design)  
- design_system_guidelines, accessibility_compliance, error_handling_guidelines, ux_research_findings


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

1. Określ persony/scenariusze i flow; przygotuj makiety/stany.  
2. Zweryfikuj A11y i mikrocopy; ustal miary UX i testy.  
3. Przekaż spec do dev, zbierz feedback, iteruj; aktualizuj DoR/DoD i linkage_index.


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

- Interaction design: kształtowanie zachowania systemu w odpowiedzi na użytkownika.  
- Microcopy: krótkie teksty w UI.  
- IA: Information Architecture.


## Przykłady użycia

- Projekt nowego flow onboardingu.  
- Redesign błędów i empty states w aplikacji.  
- Audyt A11y kluczowych ekranów.


## Ryzyka i ograniczenia

- Brak spójności z design system → chaos w UI.  
- Niedostateczne stany błędów → frustracja użytkowników.  
- Ignorowanie A11y → ryzyko prawne i UX.


## Decyzje i uzasadnienia

- Wybór wzorców/patternów zamiast custom UI.  
- Poziom szczegółu spec (hi‑fi vs mid‑fi) zależnie od ryzyka.  
- Priorytety miar UX (czas zadania vs CSAT).


## Powiązania z innymi dokumentami

- design_system_guidelines — wzorce.  
- ux_research_findings — insighty.  
- accessibility_compliance — wymagania.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- WCAG/EN/ADA dla A11y.  
- Wewnętrzne brand/style guidelines.

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

- Persony/scenariusze → Flow → Wzorce/stany → Testy i metryki.  
- Mikrocopy → UX feedback → Komunikaty błędów/empty states.  
- A11y → Kontrolki/stany → Testy manual/auto.


## Struktura sekcji

1) Persony i scenariusze  
2) User flows i IA (diagramy)  
3) Wzorce i komponenty (reuse z design system)  
4) Stany i mikrocopy (default/hover/focus/loading/error/empty/success)  
5) A11y i responsywność (WCAG, keyboard, screen reader)  
6) Feedback i komunikacja (toast/dialog/error patterns)  
7) Miary UX i testy (usability, analityka, eksperymenty)  
8) Wytyczne implementacyjne i hand‑off (spec, tokens, assets)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Diagramy flow i makiety kluczowych ekranów.  
- Tabela stanów i mikrocopy.  
- Checklista A11y per komponent/flow.  
- Plan testów użyteczności i metryk.


## Wymagane streszczenia

- One‑pager kluczowego flow (np. onboarding/checkout).  
- Lista top zasad/wzorców do użycia.


## Guidance (skrót)

- Projektuj flow end‑to‑end, nie ekrany w izolacji.  
- Pokaż zawsze stan systemu (loading/error/progress).  
- Mikrocopy proste, empatyczne; kontekstowe błędy.  
- A11y wbudowane: focus, kontrast, ARIA, klawiatura.  
- Iteruj na danych: testy użyteczności + analityka.


## Checklisty Definition of Ready (DoR)

- [ ] Persony i scenariusze zdefiniowane.  
- [ ] Flow i makiety wstępne; design system dostępny.  
- [ ] Wymagania A11y i mikrocopy szkicowane.  
- [ ] Miary UX/testy zaplanowane.  
- [ ] Ograniczenia techniczne zebrane.


## Checklisty Definition of Done (DoD)

- [ ] Spec interakcji/makiety/stany gotowe; status/wersja/data uzupełnione.  
- [ ] A11y sprawdzone; mikrocopy zaakceptowane.  
- [ ] Miary UX i plan testów uzgodnione; hand‑off wykonany.  
- [ ] Linkage_index i artefakty opublikowane.  
- [ ] Feedback/ryzyka/ decyzje udokumentowane.

