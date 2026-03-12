---
title: Dokument przydziału zadań
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Dokument przydziału zadań


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przypisać zadania do osób/zespołów z zakresem, terminami, zależnościami i kryteriami akceptacji, aby zapewnić przejrzystość i wykonanie planu.


## Zakres i granice

- Obejmuje: listę zadań (ID, opis, owner, due, priorytet), zależności/blokery, Definition of Done, status/aktualizacje, ryzyka, kanały komunikacji/escalacji.
- Poza zakresem: szczegółowe instrukcje techniczne dla zadań (linkowane).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: backlog/plan, zależności projektowe, dostępność zespołu, kryteria jakości, ryzyka.
- Wyjścia: aktualny przydział zadań, status i ryzyka, lista blockerów, plan komunikacji i eskalacji.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: project_plan, release_plan, risk_register, communication_plan, change_management_plan.
- Key Document Structures: zadania, zależności, DoD, status, komunikacja.
- Document Dependencies: ticketing/board, RACI, SLA wewnętrzne.


## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (project/task_assignment)
- project_plan, release_plan, risk_register, communication_plan, change_management_plan


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

## Standardy i compliance
### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

## RACI i role

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie dokumentu | DEV / BA | PM | BA / ARCH | OPS / SM |
| Przegląd i zatwierdzenie | PM / BA | PM | Tech Lead | OPS |
| Aktualizacja | DEV / BA | PM | BA | OPS |
| Archiwizacja | OPS | PM | BA | SM |

## Jak używać dokumentu

1. Wypełnij tabelę zadań i zależności; ustaw DoD i priorytety.  
2. Dodaj komunikację/escalacje i aktualizuj statusy; utrzymuj linkage_index.  
3. Raportuj snapshot postępu; zarządzaj ryzykami i blockerami.


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

- [ ] Każde zadanie ma owner/due/DoD; zależności i blokery są oznaczone.  
- [ ] Statusy aktualne; ryzyka mają plan mitigacji; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Board/ticket list, raporty postępu, log komunikacji, lista blockerów/ryzyk, waiver log (jeśli akceptujemy opóźnienia), ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % zadań z owner/due/DoD, cykl aktualizacji statusu, liczba otwartych blockerów, terminowość realizacji, liczba eskalacji.

## Kryteria ukończenia

- [ ] Przydział aktualny, blokery/ryzyka rozpisane, komunikacja działa; metadane aktualne.


## Struktura sekcji

1) Lista zadań (ID, opis, owner, due, priorytet, DoD, status)  
2) Zależności i blokery (zadanie→zadanie/system, wymagane decyzje)  
3) Kryteria akceptacji/DoD i wymagane artefakty/dowody  
4) Status/aktualizacje (data, kto, komentarz)  
5) Ryzyka i plan mitigacji (owner/ETA)  
6) Komunikacja i eskalacja (kanały, cadence, on-call)  
7) Załączniki (linki do ticketów/boardów, szablony raportów)


## Wymagane rozwinięcia

- Format tabeli zadań i pola obowiązkowe; priorytety i SLA; kolumna ryzyka/blokera.  
- Reguły aktualizacji statusu i częstotliwość raportów.  
- Lista osób do eskalacji i kanałów (chat/mail/standup/CAB).


## Wymagane streszczenia

- Snapshot: postęp (% ukończonych), kluczowe blokery, nadchodzące terminy, ryzyka.


## Guidance (skrót)

- Każde zadanie musi mieć ownera, due i DoD; brak = nieplanowalne.  
- Utrzymuj zależności i blokery w jednej tabeli; aktualizuj status na bieżąco.  
- Raportuj regularnie snapshot z blockerami i ryzykami; eskaluj wg zasad.


## Checklisty Definition of Ready (DoR)

- [ ] Zadania mają opis, ownera, due, priorytet, wstępny DoD.  
- [ ] Zależności i blokery zidentyfikowane; kanały komunikacji określone.


## Checklisty Definition of Done (DoD)

- [ ] Zadania ukończone wg DoD i udokumentowane; statusy zaktualizowane.  
- [ ] Blokery rozwiązane lub przeniesione; snapshot/raport zaktualizowany; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.

