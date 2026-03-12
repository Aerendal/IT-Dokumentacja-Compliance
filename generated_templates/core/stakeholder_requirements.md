---
title: Stakeholder Requirements
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Stakeholder Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zebrać i ustrukturyzować wymagania interesariuszy (wewnętrznych i zewnętrznych), zapewniając spójność, priorytetyzację, śledzenie decyzji i zgodność z celami biznesowymi.


## Zakres i granice

- Obejmuje: identyfikację interesariuszy, persony/role, potrzeby i problemy, wymagania funkcjonalne/niefunkcjonalne, priorytety (MoSCoW/RICE), zależności, ryzyka, akceptacje, mapowanie na backlog/roadmapę.  
- Poza zakresem: szczegółowe specyfikacje techniczne (oddzielne dokumenty), plan testów.


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: wywiady, warsztaty, analizy danych, obowiązki prawne, SLA, ograniczenia techniczne, feedback klientów, strategia produktu.  
- Wyjścia: katalog wymagań z priorytetami, macierz interesariusz↔wymaganie, akceptacje/odrzucenia z uzasadnieniem, DoR/DoD, decyzje i zależności, aktualizacja backlogu/roadmapy.


## Założenia

- Dostępni są kluczowi interesariusze.  
- Istnieje narzędzie backlog/traceability.  
- Dane do decyzji (ryzyka, koszty) są dostępne.


## Otwarte pytania

- Jak obsłużyć konflikt priorytetów między działami?  
- Jak wersjonować wymagania w dużych zmianach?  
- Jak mapować wymagania na SLA/OKR?

## Powiązania (meta)

- Key Documents: business_objectives_document, change_impact_assessment, quality_assurance_plan, non_functional_requirements_nfr, risk_assessment, communication_plan.  
- Key Document Structures: interesariusze, potrzeby, wymagania, priorytety, akceptacje, traceability.  
- Document Dependencies: backlog tool, requirements repo, RACI, CMDB usług (dla zależności).


## Zależności dokumentu

Wymaga: listy interesariuszy, strategii produktu, ograniczeń prawnych/technicznych, dostępnego narzędzia traceability, kryteriów priorytetyzacji. Brak = brak DoR.


## Fazy cyklu życia

- Identyfikacja interesariuszy i potrzeb.  
- Formułowanie wymagań i priorytetyzacja.  
- Akceptacje i traceability do backlogu.  
- Przeglądy okresowe i aktualizacje.



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

- linkage_index.jsonl (stakeholder/requirements)  
- business_objectives_document, non_functional_requirements_nfr


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

1. Zmapuj interesariuszy i potrzeby.  
2. Zapisz wymagania z priorytetem; powiąż z backlogiem.  
3. Uzyskaj akceptacje; loguj decyzje.  
4. Przeglądaj cyklicznie; aktualizuj dokument i linkage_index.


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

- RACI: Responsible/Accountable/Consulted/Informed.  
- MoSCoW/RICE: techniki priorytetyzacji.  
- Traceability: powiązanie wymagania z implementacją/testami.


## Przykłady użycia

- Warsztaty z działem sprzedaży i wsparcia.  
- Dokumentacja wymagań regulatora.  
- Priorytetyzacja funkcji dla release kwartalnego.


## Ryzyka i ograniczenia

- Rozmyte wymagania → scope creep.  
- Brak akceptacji → konflikty później.  
- Brak traceability → trudny audyt/regresja.  
- Nadmiar priorytetów „wysokich” → brak fokus.


## Decyzje i uzasadnienia

- Wybrane kryteria priorytetyzacji.  
- Zakres i kadencja przeglądów.  
- Zakres udziału poszczególnych interesariuszy.  
- Poziom szczegółowości wymaganych artefaktów.


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

- Interesariusze ↔ Potrzeby ↔ Priorytety.  
- Wymagania ↔ Zależności ↔ Akceptacje.  
- Decyzje ↔ Traceability ↔ Backlog.


## Struktura sekcji

1) Interesariusze, role, RACI  
2) Potrzeby/problem statements  
3) Wymagania (F/NF) z priorytetami  
4) Zależności, ryzyka, decyzje  
5) Akceptacje/odrzucenia i uzasadnienia  
6) Traceability do epików/backlogu  
7) DoR/DoD, pytania


## Wymagane rozwinięcia

- Katalog wymagań z ID, owner, priorytetem, źródłem.  
- Macierz interesariusz ↔ wymaganie ↔ status.  
- Kryteria priorytetyzacji (MoSCoW/RICE) i scoring.  
- Szablon akceptacji i log decyzji.  
- Plan przeglądów (kadencja).  
- Traceability do epików/user stories.


## Wymagane streszczenia

- Executive summary: top potrzeby, priorytety, kluczowe ryzyka.  
- Skrót akceptacji/odrzuceń (z uzasadnieniem).


## Guidance (skrót)

- Oddziel potrzeby od rozwiązań; zapisuj problem statements.  
- Priorytetyzuj jawnie z interesariuszami; unikaj „wszystko wysokie”.  
- Utrzymuj traceability do backlogu i decyzji.  
- Aktualizuj po każdym przeglądzie; wersjonuj zmiany.  
- Dokumentuj odrzucenia i przyczyny; zmniejsza powroty.  
- Aktualizuj linkage_index po zmianach.


## Checklisty Definition of Ready (DoR)

- [ ] Lista interesariuszy i ról potwierdzona.  
- [ ] Kryteria priorytetyzacji uzgodnione.  
- [ ] Źródła danych/wywiadów zebrane.  
- [ ] Narzędzie traceability dostępne.  
- [ ] Wstępny backlog/epiki zmapowane.


## Checklisty Definition of Done (DoD)

- [ ] Wymagania z priorytetami i akceptacjami zapisane.  
- [ ] Traceability do backlogu/epików pełne.  
- [ ] Decyzje i odrzucenia udokumentowane.  
- [ ] linkage_index zaktualizowany.  
- [ ] Plan kolejnego przeglądu ustalony.

