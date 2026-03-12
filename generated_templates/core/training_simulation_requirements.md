---
title: Training Simulation Requirements
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Training Simulation Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Określić wymagania dla symulacji szkoleniowych (VR/desktop/web): cele dydaktyczne, scenariusze, technologia, metryki i zgodność, aby zapewnić realizm, bezpieczeństwo i mierzalną efektywność.


## Zakres i granice

- Obejmuje: scenariusze i role, cele learning outcomes, poziom realizmu, interakcje, ocena/score, dane telemetryczne, wymagania techniczne (sprzęt/VR/latencja), dostępność, bezpieczeństwo danych, integracje (LMS/LRS), raportowanie, testy i walidacja.  
- Poza zakresem: pełny design graficzny (oddzielne specyfikacje), rekrutacja uczestników.


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: cele szkolenia, profile użytkowników, ograniczenia sprzętu, polityki bezpieczeństwa, standardy SCORM/xAPI, budżet, wymagania regulatora/branży.  
- Wyjścia: specyfikacja scenariuszy i interakcji, metryki oceny, wymagania techniczne, plan testów/akceptacji, checklisty DoR/DoD, integracje z LMS/LRS, plan utrzymania treści.


## Założenia

- Dostępne środowisko dev/test i sprzęt.  
- Użytkownicy testowi są dostępni.  
- Organizacja akceptuje wymagania RODO i bezpieczeństwa.


## Otwarte pytania

- Jak mierzyć transfer wiedzy po szkoleniu?  
- Jaki minimalny fps/latencja dla VR w tym use-case?  
- Jak obsłużyć lokalizacje wielojęzyczne?

## Powiązania (meta)

- Key Documents: course_content_testing, performance_testing_plan, accessibility_improvement_plan, data_protection_compliance, lms_integration_guide (jeśli istnieje), documentation_roadmap.  
- Key Document Structures: scenariusze, interakcje, metryki, technologia, testy, integracje.  
- Document Dependencies: silnik/symulator, hardware VR/PC, LMS/LRS, analytics, storage.


## Zależności dokumentu

Wymaga: zdefiniowanych celów nauki, profili użytkowników, budżetu i sprzętu, standardów raportowania (xAPI/SCORM), polityk bezpieczeństwa danych, dostępu do narzędzi dev/test. Brak = brak DoR.


## Fazy cyklu życia

- Definicja celów i scenariuszy.  
- Wymagania techniczne i projekt interakcji.  
- Implementacja/prototyp i testy.  
- Walidacja/akceptacja i rollout.  
- Utrzymanie/aktualizacje i raporty.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (training/simulation/requirements)  
- course_content_testing, performance_testing_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

1. Zdefiniuj cele i scenariusze; przypisz metryki.  
2. Określ wymagania techniczne i dostępności; zaplanuj testy.  
3. Implementuj/prototypuj; waliduj na użytkownikach testowych.  
4. Rollout; raportuj wyniki; aktualizuj dokument/linkage_index.


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

- xAPI/SCORM: standardy śledzenia aktywności szkoleniowych.  
- VR sickness: dyskomfort przy niskim fps/latencji.  
- Branching scenario: wiele ścieżek zależnych od decyzji użytkownika.


## Przykłady użycia

- Symulacja BHP w VR dla pracowników produkcji.  
- Trening obsługi klienta z branching dialogami.  
- Symulator procedur technicznych na desktop/web.


## Ryzyka i ograniczenia

- Niska wydajność → złe doświadczenie/VR sickness.  
- Brak metryk → brak oceny skuteczności.  
- Niepewność prawna danych użytkownika → ryzyko RODO.  
- Brak dostępności → wykluczenie części użytkowników.


## Decyzje i uzasadnienia

- Wybór silnika/technologii i sprzętu.  
- Zakres telemetry i raportów.  
- Poziom realizmu vs koszt.  
- Kadencja aktualizacji treści.


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

- Cele ↔ Scenariusze ↔ Metryki oceny.  
- Technologia ↔ Wydajność/latencja ↔ Dostępność.  
- Integracje ↔ Dane/raportowanie ↔ Bezpieczeństwo.


## Struktura sekcji

1) Cele i użytkownicy (learning outcomes, role)  
2) Scenariusze i interakcje (poziomy, ścieżki, branching)  
3) Metryki oceny i telemetry (score, czas, błędy)  
4) Technologia (sprzęt, engine, grafika, audio, latency)  
5) Dostępność i bezpieczeństwo danych  
6) Integracje LMS/LRS, raportowanie  
7) Plan testów (funkcjonalne, perf, a11y, device)  
8) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Lista scenariuszy z celami i kryteriami zaliczenia.  
- Metryki i eventy xAPI/SCORM; schemat danych.  
- Wymagania sprzętowe (VR/PC/mobile), minimalne fps/latencja.  
- Plan testów urządzeń i dostępności (napisy/audio).  
- Polityka danych: anonimizacja/retencja.  
- Plan aktualizacji treści i wersjonowania.


## Wymagane streszczenia

- Executive summary: cele, kluczowe scenariusze, wymagania sprzętowe.  
- Skrót metryk oceny i raportowania.


## Guidance (skrót)

- Zacznij od celów edukacyjnych, a nie od technologii.  
- Zbieraj telemetry; ocena musi być mierzalna i powtarzalna.  
- Testuj wydajność i komfort (fps/latency/VR sickness).  
- Zapewnij dostępność: napisy, alternatywy wejścia, kontrast.  
- Integruj z LMS/LRS; waliduj xAPI/SCORM.  
- Aktualizuj linkage_index po releasach.


## Checklisty Definition of Ready (DoR)

- [ ] Cele nauki i scenariusze spisane.  
- [ ] Wymagania sprzętowe i budżet potwierdzone.  
- [ ] Standardy xAPI/SCORM i eventy zdefiniowane.  
- [ ] Plan testów (funkcja, perf, a11y, urządzenia) gotowy.  
- [ ] Polityki danych/bezpieczeństwa zatwierdzone.


## Checklisty Definition of Done (DoD)

- [ ] Scenariusze działają; metryki zbierane poprawnie.  
- [ ] Wydajność/latencja spełnia minimalne progi.  
- [ ] Dostępność zweryfikowana; wyjątki udokumentowane.  
- [ ] Integracje LMS/LRS działają; raporty generowane.  
- [ ] linkage_index i dokumentacja zaktualizowane; feedback zebrany.

