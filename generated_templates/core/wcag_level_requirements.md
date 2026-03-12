---
title: WCAG Level Requirements
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# WCAG Level Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Określić wymagany poziom zgodności z WCAG (A/AA/AAA) dla produktu, mapować kryteria sukcesu na komponenty i procesy, zapewniając jasne wymagania dla projektowania, developmentu i testów.


## Zakres i granice

- Obejmuje: wybór poziomu WCAG, lista kryteriów sukcesu, przypisanie do komponentów/widoków, wyjątki/wykluczenia z uzasadnieniem, metody weryfikacji (manual/automaty/SR), dokumentację i raportowanie zgodności.  
- Poza zakresem: szczegółowy plan napraw (w accessibility_improvement_plan), implementacja komponentów (aria_implementation_design).


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: standard WCAG 2.x/3 draft, audyty, listy komponentów, wymagania prawne/kontraktowe, urządzenia/platformy, języki/RTL.  
- Wyjścia: tabela kryteriów i poziomów, zakres komponentów, wyjątki z uzasadnieniem, wymagane testy i narzędzia, checklisty DoR/DoD, raport zgodności.


## Założenia

- Design system i lista komponentów istnieją.  
- Zespół ma dostęp do SR i narzędzi.  
- Jest kanał raportowania a11y.


## Otwarte pytania

- Czy są rynki z dodatkowymi wymaganiami (np. ADA)?  
- Jak długo przechowywać raporty?  
- Czy wymagamy certyfikacji zewnętrznej?

## Powiązania (meta)

- Key Documents: accessibility_improvement_plan, aria_implementation_design, ui_test_strategy, semantic_html_implementation, documentation_roadmap.  
- Key Document Structures: kryteria, komponenty, testy, wyjątki, raporty.  
- Document Dependencies: design system, repo komponentów, narzędzia a11y, SR/test lab.


## Zależności dokumentu

Wymaga: listy widoków/komponentów, kontekstu prawnego (kraje/kontrakty), audytów i luk, narzędzi testowych, design systemu. Brak = brak DoR.


## Fazy cyklu życia

- Ustalenie poziomu WCAG i zakresu.  
- Mapowanie kryteriów na komponenty/widoki.  
- Określenie testów i narzędzi.  
- Raportowanie i przeglądy okresowe.  
- Aktualizacje po audytach i zmianach produktu.



## Struktura sekcji (szkielet)
1. Kontekst prawny i poziom zgodności (A/AA/AAA).
2. Zasady WCAG (Perceivable, Operable, Understandable, Robust) z mapą kryteriów.
3. Wymagania projektowe (kolor, typografia, layout, stany focus/hover).
4. Wymagania techniczne (aria, semantyka, kolejność tab, media, formularze).
5. Wymagania dla treści (alt, transkrypcje, napisy, język).
6. Role i odpowiedzialności (product, design, dev, QA).
7. Narzędzia i proces testów (automaty, manual, czytniki ekranu).
8. Kryteria akceptacji i raportowanie niezgodności.
## Szybkie powiązania

- linkage_index.jsonl (wcag/level/requirements)  
- accessibility_improvement_plan, aria_implementation_design


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

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

1. Wybierz poziom WCAG i wypełnij tabelę kryteriów.  
2. Przypisz kryteria do komponentów/widoków; dodaj do DoR/DoD.  
3. Zdefiniuj testy i narzędzia; uruchom raportowanie.  
4. Aktualizuj dokument po audytach/zmianach produktu.


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

- WCAG: Web Content Accessibility Guidelines.  
- SR: screen reader.  
- RAG: Red/Amber/Green status.


## Przykłady użycia

- Ustalenie wymagań a11y przed redesignem aplikacji.  
- Raport zgodności dla kontraktu enterprise.  
- Mapowanie kryteriów na nowe komponenty design systemu.


## Ryzyka i ograniczenia

- Brak mapowania → luki a11y w komponentach.  
- Nieudokumentowane wyjątki → ryzyko prawne.  
- Tylko automaty → niewykryte problemy.  
- Brak przeglądów → regresje.


## Decyzje i uzasadnienia

- Poziom WCAG i ewentualne wyjątki.  
- Zakres SR/narzędzi w testach.  
- Kadencja raportów.  
- Odpowiedzialność za utrzymanie tabeli.


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

- Kryteria ↔ Komponenty ↔ Testy.  
- Wyjątki ↔ Uzasadnienie ↔ Plan napraw.  
- Raporty ↔ Audyty ↔ Roadmapa.


## Struktura sekcji

1) Poziom WCAG i kontekst prawny  
2) Tabela kryteriów i mapowanie na komponenty/widoki  
3) Wyjątki i uzasadnienia  
4) Testy i narzędzia (manual + automaty + SR)  
5) Raportowanie zgodności i przeglądy  
6) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Tabela kryteriów (ID, opis, poziom, zastosowanie, test)  
- Lista komponentów z przypisanymi kryteriami.  
- Wyjątki i ryzyka z planem kompensacji.  
- Szablon raportu zgodności.  
- Kadencja przeglądów i aktualizacji.


## Wymagane streszczenia

- Executive summary: poziom, główne ryzyka/wyjątki.  
- Skrót statusu zgodności (RAG).


## Guidance (skrót)

- Preferuj poziom AA jako domyślny; udokumentuj wyjątki.  
- Mapuj kryteria na komponenty już na etapie design.  
- Testuj SR/klawiaturą; automaty są uzupełnieniem.  
- Utrzymuj tabelę kryteriów w repo; aktualizuj po zmianach.  
- Raportuj status regularnie; integruj z accessibility_improvement_plan.


## Checklisty Definition of Ready (DoR)

- [ ] Poziom WCAG ustalony; kontekst prawny znany.  
- [ ] Lista komponentów/widoków dostępna.  
- [ ] Narzędzia testowe i SR dostępne.  
- [ ] Tabela kryteriów rozpoczęta.  
- [ ] Plan raportowania ustalony.


## Checklisty Definition of Done (DoD)

- [ ] Tabela kryteriów kompletna i zmapowana.  
- [ ] Wyjątki udokumentowane; plany kompensacji opisane.  
- [ ] Testy/narzędzia przypisane; raportowanie działa.  
- [ ] linkage_index zaktualizowany; brak krytycznych luk.  
- [ ] Kadencja przeglądów zaplanowana.

