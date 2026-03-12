---
title: Product Knowledge Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Product Knowledge Training


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaprojektować i realizować szkolenia z wiedzy produktowej dla sprzedaży, wsparcia i partnerów, tak aby komunikacja wartości, funkcji i ograniczeń była spójna i skuteczna.


## Zakres i granice

- Obejmuje: materiały produktowe (wartość, use‑cases, persony), demo flow, pricing/licencje na wysokim poziomie, roadmapa publiczna, FAQ i obiekcje, konkurencja, procedury aktualizacji treści, testy wiedzy, lokalizacja.  
- Poza zakresem: negocjacje cenowe, szczegółowe kontrakty prawne.


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: aktualne funkcje i release notes, segmenty klientów, obiekcje z rynku, polityki cen/licencji, materiały marketing, feedback z supportu, plan roadmapy publicznej.  
- Wyjścia: program szkolenia, decki/handouty, demo scripts, FAQ, quiz/test, rejestr uczestników, harmonogram refresher, checklisty DoR/DoD.


## Założenia

- Produkt ma release notes; demo environment dostępne.  
- Pricing/licencje utrzymywane w jednym źródle.  
- LMS dostępny do rejestru/testów.


## Otwarte pytania

- Jak mierzyć wpływ szkolenia na wyniki sprzedaży?  
- Czy potrzebne wersje językowe materiałów?  
- Jak długo przechowywać nagrania szkoleń?

## Powiązania (meta)

- Key Documents: demo_environment_setup, documentation_roadmap, change_impact_assessment, communication_playbook, partner_onboarding_policy.  
- Key Document Structures: materiały, demo, FAQ/obiekcje, testy, aktualizacje.  
- Document Dependencies: LMS, CMS/knowledge base, status page/roadmap, pricing source, analytics z supportu.


## Zależności dokumentu

Wymaga: aktualnych informacji produktowych, kanału „source of truth” dla pricing/licencji, dostępu do demo environment, danych o obiekcjach i konkurencji, narzędzi szkoleniowych/LMS. Brak = brak DoR.


## Fazy cyklu życia

- Planowanie i przygotowanie materiałów/demo.  
- Szkolenie i testy wiedzy.  
- Zbiór feedbacku i aktualizacje.  
- Refresher po releasach.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (product/knowledge/training)  
- demo_environment_setup, communication_playbook


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum

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

1. Przygotuj materiały i demo; zdefiniuj quiz.  
2. Przeprowadź szkolenie; zbierz wyniki w LMS.  
3. Aktualizuj materiały po releasach; odśwież FAQ.  
4. Zaktualizuj linkage_index i rejestry.


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

- Source of truth: główny kanał aktualnych info produktowych.  
- Refresher: cykliczne, krótkie szkolenie po releasie.


## Przykłady użycia

- Onboarding nowego zespołu sales.  
- Aktualizacja partnerów po wprowadzeniu nowej funkcji.  
- Refresher po zmianie pricingu.


## Ryzyka i ograniczenia

- Nieaktualne materiały → błędne obietnice klientom.  
- Brak demo lub zepsute dane → słabe szkolenie.  
- Brak testu → brak weryfikacji wiedzy.  
- Chaos w źródłach prawdy → niespójne przekazy.


## Decyzje i uzasadnienia

- Cadence refresher i release sync.  
- Zakres quizu i progi.  
- Jakie segmenty mają dedykowane materiały.  
- Kto zatwierdza zmiany w materiale.


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

- Materiały ↔ Demo ↔ FAQ/obiekcje.  
- Roadmapa ↔ Aktualizacje treści ↔ Testy/refresher.


## Struktura sekcji

1) Profil odbiorców i cele szkolenia  
2) Materiały produktowe (wartość, use‑cases, konkurencja)  
3) Demo scripts i środowisko  
4) FAQ/obiekcje i odpowiedzi  
5) Testy/quiz i kryteria zaliczenia  
6) Aktualizacje (release cadence, owners)  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Deck i one‑pagers per segment.  
- Demo flow + checklisty (co pokazać, dane, fallback).  
- FAQ/obiekcje z odpowiedziami; konkurencja i różnice.  
- Szablon quizu; progi zaliczenia.  
- Plan aktualizacji po releasach i komunikacja.  
- Rejestr uczestników w LMS.


## Wymagane streszczenia

- Executive summary: kluczowe wartości produktu.  
- Skrót najczęstszych obiekcji i odpowiedzi.


## Guidance (skrót)

- Utrzymuj jedno źródło prawdy (CMS); synchronizuj z release notes.  
- Trenuj na demo environment; sprawdzaj aktualność danych.  
- Aktualizuj FAQ po feedbacku z rynku/supportu.  
- Mierz skuteczność testem/quizem; planuj refresher co releas(e).  
- Dokumentuj zmiany w linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Aktualne materiały i release notes.  
- [ ] Dostęp do demo environment.  
- [ ] Pricing/licencje potwierdzone.  
- [ ] FAQ/obiekcje zebrane.  
- [ ] LMS i quiz przygotowane.


## Checklisty Definition of Done (DoD)

- [ ] Szkolenie wykonane; wyniki w LMS.  
- [ ] Materiały i FAQ zaktualizowane; demo zweryfikowane.  
- [ ] Feedback zebrany; plan poprawek zapisany.  
- [ ] linkage_index uzupełniony; brak krytycznych braków treści.  
- [ ] Zaplanowany następny refresher.

