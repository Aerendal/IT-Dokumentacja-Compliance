---
title: Profiling Tools Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Profiling Tools Training


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Program szkolenia z narzędzi profilowania (CPU/Memory/IO/Network) dla deweloperów i SRE, aby szybciej diagnozować i usuwać problemy wydajnościowe.


## Zakres i granice

- Obejmuje: listę narzędzi (perf, flamegraphs, eBPF, pprof, JFR, Chrome DevTools, DB profilers), scenariusze użycia, środowiska (local/stage/prod-safe), metryki i artefakty, best practices (sampling vs tracing), bezpieczeństwo/PII, checklisty ćwiczeń, materiały i ewaluację.  
- Poza zakresem: pełne szkolenie z optymalizacji algorytmów (oddzielny kurs).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: katalog usług/stacków, standardy performance, narzędzia dostępne w org, przykładowe incydenty, polityki dostępu do prod, budżet czasowy szkolenia.  
- Wyjścia: sylabus i laboratoria, instrukcje „how-to”, scenariusze ćwiczeń, checklisty DoR/DoD, wyniki ewaluacji (quiz/praktyka), lista usprawnień narzędzi.


## Założenia

- Środowiska lab/stage dostępne i zbliżone do prod.  
- Organizacja ma polityki prod-safe/PII.  
- Zespoły mają czas na udział w szkoleniu.


## Otwarte pytania

- Czy potrzebna certyfikacja formalna?  
- Jak często odświeżać szkolenie?  
- Jak mierzyć wpływ szkolenia na MTTR/performance?


## Powiązania (meta)

- Key Documents: performance_engineering_guidelines, observability_plan, incident_response_runbook, security_requirements, onboarding_engineer.  
- Key Document Structures: narzędzia, scenariusze, ćwiczenia, bezpieczeństwo, ewaluacja.  
- Document Dependencies: dostęp do środowisk, uprawnienia, próbki aplikacji, monitoring/logi.


## Zależności dokumentu

Wymaga: listy narzędzi dostępnych w org, polityk dostępu do prod, przykładów incydentów performance, mentorów/trenerów, środowisk lab/stage. Braki = DoR otwarte.


## Fazy cyklu życia

- Przygotowanie sylabusa i labów.  
- Przeprowadzenie szkoleń/cykli.  
- Ewaluacja i doskonalenie materiałów.  
- Odświeżenie przy zmianie stacku/narzędzi.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (profiling/tools/training)  
- performance_engineering_guidelines, observability_plan, incident_response_runbook, onboarding_engineer


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

1. Wybierz narzędzia i scenariusze dla danego stacku.  
2. Przeprowadź laby i ewaluację; zbierz feedback.  
3. Aktualizuj materiały, DoR/DoD i linkage_index po każdym cyklu szkolenia.


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

- Flamegraph: wizualizacja stosu CPU/Wall/Memory.  
- Prod-safe: zasady minimalizujące wpływ na produkcję.  
- Profiling sampling vs tracing: kompromis obciążenie vs szczegół.


## Przykłady użycia

- Warsztat „GC pause” dla JVM.  
- Profiling API latency (pprof) w Go.  
- Chrome DevTools dla front-end TTI/LCP.


## Ryzyka i ograniczenia

- Profiling na prod może degradować usługę.  
- Brak kompetencji → błędne wnioski z profili.  
- PII w zrzutach/profilach.


## Decyzje i uzasadnienia

- Które narzędzia standardowe w org na dany stack.  
- Poziom dostępu do prod dla uczestników.  
- Kryteria certyfikacji/zaliczenia.


## Powiązania z innymi dokumentami

- incident_response_runbook — profilowanie w incydentach.  
- performance_engineering_guidelines — zasady optymalizacji.  
- onboarding_engineer — plan dla nowych osób.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Wewnętrzne polityki prod access/PII.  
- Standardy językowe/stackowe dla narzędzi profilujących.

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

- Narzędzia → Scenariusze → Ćwiczenia → Ewaluacja.  
- Bezpieczeństwo/PII → Uprawnienia → Środowiska.


## Struktura sekcji

1) Cel i grupa docelowa  
2) Narzędzia i wymagania (stack, OS, języki)  
3) Scenariusze i laboratoria (CPU, memory, IO, DB, front-end)  
4) Instrukcje „how-to” i best practices (sampling, flamegraph, traces)  
5) Bezpieczeństwo/PII i dostęp do środowisk (prod-safe)  
6) Ewaluacja i certyfikacja (quiz, zadania praktyczne)  
7) Materiały i wsparcie (runbooks, cheatsheets)  
8) Harmonogram i logistyka  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Lista narzędzi z wersjami i wsparciem per język/OS.  
- Scenariusze labów z danymi i oczekiwanym wynikiem (np. memory leak, GC pause, slow query).  
- Checklisty bezpieczeństwa dla pracy na prod/stage (PII, performance impact).  
- Szablony cheat‑sheet i runbooków.


## Wymagane streszczenia

- Executive snapshot: pokrycie zespołów, wyniki ewaluacji, top potrzebne narzędzia.  
- Krótki plan zajęć (agenda) na 1‑2 dni szkolenia.


## Guidance (skrót)

- Zaczynaj od obserwowalności (metryki/logi) przed głębokim profilingiem.  
- Używaj sampling gdy to możliwe; tracing/flamegraphs dla pinpointu.  
- Miej prod‑safe zasady: throttle, ogranicz czas, testuj na stage gdy się da.  
- Dokumentuj wyniki profilowania i poprawki; włącz do post‑incident reviews.  
- Aktualizuj materiały wraz ze zmianą stacku/narzędzi.


## Checklisty Definition of Ready (DoR)

- [ ] Lista narzędzi i dostępów przygotowana.  
- [ ] Scenariusze labów i dane testowe gotowe.  
- [ ] Polityki prod-safe/PII zdefiniowane.  
- [ ] Trenerzy i harmonogram ustalone.  
- [ ] Materiały wstępne (cheatsheet/runbook) przygotowane.


## Checklisty Definition of Done (DoD)

- [ ] Szkolenie przeprowadzone; wyniki ewaluacji zebrane.  
- [ ] Feedback wprowadzony; materiały zaktualizowane; status/wersja/data uzupełnione.  
- [ ] Dostępy i środowiska posprzątane; PII usunięte.  
- [ ] Linkage_index i repo wiedzy uzupełnione o lekcje.  
- [ ] Lista usprawnień narzędzi/praktyk przekazana ownerom.

