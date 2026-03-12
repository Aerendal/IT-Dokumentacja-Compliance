---
title: Harmonogram implementacji
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Harmonogram implementacji


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaplanować implementację rozwiązania: fazy, zadania, kamienie milowe, zależności, ryzyka, bufory, komunikację i kryteria akceptacji, aby dowieźć zakres w czasie i bez kolizji.


## Zakres i granice

- Obejmuje: fazy (analiza/design/dev/test/deploy), zadania i kamienie, zależności/krytyczna ścieżka, ryzyka i plan B, bufory, komunikację/statusy, kryteria akceptacji per faza.
- Poza zakresem: szczegółowe specyfikacje techniczne (linkowane), runbooki wdrożeniowe (oddzielne).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: zakres/projekt, wymagania, architektura, zależności systemowe, dostępność zespołu, kalendarze blackoutów, ryzyka.  
- Wyjścia: harmonogram faz i kamieni, lista zależności/krytyczna ścieżka, plan komunikacji/statusów, lista ryzyk i mitigacji, kryteria akceptacji.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: project_plan, release_plan, change_management_plan, risk_register, communication_plan, deployment_schedule, testing_plan_schedule, non_functional_requirements.
- Key Document Structures: fazy, kamienie, zależności, komunikacja, kryteria akceptacji.
- Document Dependencies: ticketing/board, CI/CD, kalendarze zespołów, CAB/Change, environment readiness.



## Zależności dokumentu

- Konsumuje: [dokumenty wejściowe — co musi istnieć zanim ten dokument powstanie]
- Dostarcza do: [dokumenty wyjściowe — co korzysta z tego dokumentu]

## Fazy cyklu życia

- Faza 1: Koncepcja i Wizja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 2: Analiza Wymagań: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 3: Projekt / Design: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 4: Planowanie: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 5: Implementacja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 6: Testowanie / QA: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 7: Bezpieczeństwo / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 8: Wdrożenie / Deployment: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 9: Operacje / Maintenance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)

- Cele i zakres
- Kamienie milowe i terminy
- Zasoby i odpowiedzialności
- Zależności
- Ryzyka
- Status i postęp

## Szybkie powiązania

- linkage_index.jsonl (project/implementation_schedule)
- project_plan, release_plan, change_management_plan, risk_register, communication_plan, deployment_schedule, testing_plan_schedule, non_functional_requirements


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

1. Ustal fazy/kamienie, zależności i blackouty; wpisz do tabeli/kalendarza.  
2. Dodaj ryzyka/bufory/plan B i komunikację; ustaw kryteria akceptacji.  
3. Aktualizuj statusy i linkage_index; raportuj wg cadence.


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

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

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

- [ ] Zależności i blackouty uwzględnione; krytyczna ścieżka jasno opisana.  
- [ ] Bufory/plan B przypisane; ryzyka mają właścicieli i mitigację.  
- [ ] Kryteria akceptacji spójne z fazami i testami/deploy; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Gantt/CSV, board/tickety, matryca zależności, kalendarze blackoutów, raporty statusów, CAB decyzje, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Terminowość kamieni, liczba przesunięć krytycznej ścieżki, zużycie buforów, liczba eskalacji, % faz z kompletnym DoD.

## Kryteria ukończenia

- [ ] Harmonogram aktualny, ryzyka/waivery opisane, komunikacja działa; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Fazy i kamienie (analiza/design/dev/test/deploy) z datami/ownerami  
2) Zadania, zależności i krytyczna ścieżka (Gantt/CSV/link do boardu)  
3) Ryzyka i plan B (bufory, trigger na plan B, owner/ETA)  
4) Bufory i założenia (czas, zasoby, środowiska)  
5) Plan komunikacji i statusów (cadence, kanały, odbiorcy, szablony)  
6) Kryteria akceptacji per faza (DoR/DoD, wejścia/wyjścia)  
7) Załączniki (board, Gantt, kalendarze blackoutów, CAB decyzje)


## Wymagane rozwinięcia

- Kamienie milowe i daty; właściciele.  
- Matryca zależności i krytyczna ścieżka; identyfikacja blackoutów.  
- Kryteria akceptacji i DoR/DoD per faza; powiązania z testami/deploy.  
- Plan komunikacji (status weekly/daily, szablony, eskalacje).


## Wymagane streszczenia

- Executive: timeline, krytyczna ścieżka, top ryzyka, bufory, decyzje CAB/go-no-go.


## Guidance (skrót)

- Planuj od końca (data release) wstecz; zaznacz blackouty i zależności.  
- Bufory dla krytycznych integracji/środowisk; definiuj trigger na plan B.  
- Aktualizuj harmonogram po zmianach zakresu; komunikuj statusy regularnie.  
- Ustal jasne kryteria go/conditional/no‑go na koniec każdej fazy.


## Checklisty Definition of Ready (DoR)

- [ ] Zakres i wymagania zatwierdzone; główne zależności i blackouty zidentyfikowane.  
- [ ] Ownerzy faz/kamieni wyznaczeni; board/kalendarze dostępne.  
- [ ] Kryteria akceptacji per faza wstępnie spisane.


## Checklisty Definition of Done (DoD)

- [ ] Harmonogram opublikowany; krytyczna ścieżka i ryzyka/bufory opisane; komunikacja działa.  
- [ ] Kryteria akceptacji per faza spełnione lub waiver z sunset; dokument w linkage_index; metadane aktualne.

