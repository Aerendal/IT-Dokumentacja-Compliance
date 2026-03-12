---
title: Unit Training Rollout
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Unit Training Rollout


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan wdrożenia szkolenia jednostek/zespołów: zakres, harmonogram, materiały, trenerzy, ewaluacja i komunikacja. Ma zapewnić spójne przeszkolenie i mierzalne efekty.


## Zakres i granice

- Obejmuje: cele szkolenia, grupy docelowe, sylabus, formaty (online/offline/blended), harmonogram, zasoby (trenerzy, sale, narzędzia), komunikację, prerekwizyty, materiały, ćwiczenia, oceny (quiz/praktyka), certyfikację/badge, śledzenie frekwencji, feedback i ciągłe doskonalenie.  
- Poza zakresem: polityka wynagrodzeń/HR (oddzielne).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: potrzeby kompetencyjne, sylabus, dostępność trenerów i uczestników, narzędzia LMS, materiały szkoleniowe, plan komunikacji, budżet.  
- Wyjścia: harmonogram i sesje, listy uczestników, materiały i linki, oceny i certyfikaty, raport frekwencji/ocen, checklisty DoR/DoD.


## Założenia

- Narzędzia LMS i sale/online dostępne.  
- Budżet na trenerów/materiały.  
- Uczestnicy mają czas i zgodę na udział.


## Otwarte pytania

- Jakie minimalne KPI (frekwencja/zdawalność/NPS)?  
- Czy potrzebna akredytacja zewnętrzna?  
- Jak długo przechowywać dane o wynikach?


## Powiązania (meta)

- Key Documents: competency_matrix, training_materials, lms_setup, communication_plan, evaluation_rubric, certification_policy.  
- Key Document Structures: cele, grupy, harmonogram, materiały, oceny, komunikacja, ewaluacja.  
- Document Dependencies: LMS, kalendarze, sale/narzędzia, ankiety/quiz tools, śledzenie frekwencji.


## Zależności dokumentu

Wymaga: zatwierdzonego sylabusa, dostępnych trenerów i zasobów, list uczestników, skonfigurowanego LMS, materiałów i planu komunikacji. Braki = DoR otwarte.


## Fazy cyklu życia

- Przygotowanie (sylabus, materiały, LMS, komunikacja).  
- Realizacja sesji i ocen.  
- Raportowanie wyników i certyfikacja.  
- Retro i aktualizacje materiałów.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (unit/training/rollout)  
- competency_matrix, training_materials, lms_setup, evaluation_rubric, certification_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
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

1. Ustal cele/sylabus i zasoby; przygotuj harmonogram i materiały.  
2. Przeprowadź sesje i oceny; śledź frekwencję i wyniki.  
3. Raportuj, certyfikuj, zbierz feedback; aktualizuj DoR/DoD i linkage_index.


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

- LMS: Learning Management System.  
- Rubryka oceny: kryteria i wagi do oceny zadań.  
- NPS: Net Promoter Score szkolenia.


## Przykłady użycia

- Rollout szkolenia bezpieczeństwa/ESD w fabryce.  
- Program onboardingu nowego zespołu inżynierów.  
- Cykl szkoleń produktowych dla działu sprzedaży.


## Ryzyka i ograniczenia

- Niska frekwencja → brak efektu.  
- Brak prerekwizytów → niska zdawalność.  
- Brak danych w LMS → trudne raportowanie.


## Decyzje i uzasadnienia

- Format (online vs blended) i długość modułów.  
- Kryteria zaliczenia i certyfikacji.  
- Kadencja odświeżeń materiałów.


## Powiązania z innymi dokumentami

- training_materials — treści.  
- evaluation_rubric — oceny.  
- communication_plan — komunikacja.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Wewnętrzne polityki szkoleń i ochrony danych uczestników.  
- Ewentualne normy branżowe dla certyfikacji.

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

- Cele → Sylabus → Materiały/oceny → Ewaluacja.  
- Harmonogram → Frekwencja → Raport → Doskonalenie.  
- Komunikacja → Uczestnicy → Feedback.


## Struktura sekcji

1) Cele i zakres szkolenia  
2) Grupy docelowe i prerekwizyty  
3) Sylabus i format (moduły, ćwiczenia)  
4) Harmonogram i logistyka (terminy, sale/online, trenerzy)  
5) Materiały i narzędzia (LMS, linki, sprzęt)  
6) Oceny i certyfikacja (quiz/praktyka, progi, badge)  
7) Frekwencja i śledzenie postępów  
8) Komunikacja i onboarding uczestników  
9) Feedback, ewaluacja i doskonalenie  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Kalendarz sesji i obsady trenerów.  
- Lista materiałów (slajdy, ćwiczenia, labs) i dostępów.  
- Rubryka oceny i progi zaliczenia.  
- Plan komunikacji (zaproszenia, przypomnienia, follow-up).


## Wymagane streszczenia

- One‑pager: cele, terminy, wymagania, kontakt.  
- Snapshot wyników: frekwencja, zdawalność, NPS/feedback.


## Guidance (skrót)

- Dopasuj format do grup (blended/online); uwzględnij strefy czasowe.  
- Zadbaj o prerekwizyty i dostęp do narzędzi przed startem.  
- Mierz nie tylko frekwencję, ale i mastery (oceny/praktyka).  
- Zbieraj feedback każdej sesji; iteruj materiały.  
- Zapewnij ścieżkę certyfikacji/badge i śledzenie w LMS.


## Checklisty Definition of Ready (DoR)

- [ ] Sylabus i materiały gotowe; LMS skonfigurowany.  
- [ ] Trenerzy i terminy potwierdzeni; listy uczestników.  
- [ ] Prerekwizyty i dostęp do narzędzi zakomunikowane.  
- [ ] Rubryka ocen i progi ustalone.  
- [ ] Plan komunikacji przygotowany.


## Checklisty Definition of Done (DoD)

- [ ] Sesje zrealizowane; frekwencja i wyniki zapisane; status/wersja/data uzupełnione.  
- [ ] Certyfikaty/badge przyznane; wyjątki opisane.  
- [ ] Feedback zebrany i wprowadzony; materiały zaktualizowane.  
- [ ] Raport (frekwencja/zdawalność/NPS) opublikowany; linkage_index uzupełniony.  
- [ ] Ryzyka/decyzje odnotowane; plan ulepszeń dodany.

