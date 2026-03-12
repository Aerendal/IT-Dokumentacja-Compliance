---
title: Harmonogram POC/pilota
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Harmonogram POC/pilota


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaplanować Proof of Concept / pilota: zakres i cele, kryteria sukcesu (go/conditional/no‑go), etapy/kamienie, zadania i zależności, ryzyka/mitigacje, metryki i raportowanie.


## Zakres i granice

- Obejmuje: zakres i cele POC/pilota, kryteria sukcesu, etapy/kamienie z datami i właścicielami, zadania i zależności, dane/testy/środowiska, ryzyka/mitigacje/plan awaryjny, metryki i raportowanie.  
- Poza zakresem: pełne rollouty produkcyjne (osobne plany).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: problem statement, hipotezy, wymagania success criteria, dane/testy, środowiska, zespoły i dostępność, ryzyka.  
- Wyjścia: harmonogram POC/pilota (etapy/kamienie), lista zadań i zależności, kryteria go/conditional/no‑go, plan ryzyk/mitigacji/awaryjny, metryki i raporty.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: experimentation_plan, risk_register, change_management_plan, monitoring_strategy_document, rollout_plan, communication_plan.
- Key Document Structures: cele/kryteria, etapy/kamienie, zadania/zależności, ryzyka, metryki/raporty.
- Document Dependencies: dane/testy, środowiska, dostępność zespołu, ticketing/board, monitoring/analytics.



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

- linkage_index.jsonl (project/poc_schedule)
- experimentation_plan, risk_register, change_management_plan, monitoring_strategy_document, rollout_plan, communication_plan


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

1. Ustal cele/kryteria i etapy/kamienie; wypełnij zadania/zależności.  
2. Przygotuj dane/testy/środowiska; zaplanuj ryzyka i plan awaryjny.  
3. Monitoruj metryki; raportuj postęp; zaktualizuj linkage_index/checklisty.


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

- [ ] Kamienie/cele spójne z kryteriami; metryki dostępne; zależności uwzględnione.  
- [ ] Plan awaryjny/rollback istnieje; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Gantt/board, checklists, metryki/raporty, dane/testy, log decyzji, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Terminowość kamieni, spełnienie kryteriów sukcesu, liczba rollbacków/awaryjnych stopów, czas decyzji go/no-go, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] POC/pilot wykonany, kryteria ocenione, decyzja i log; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres i cele POC/pilota; kryteria sukcesu (go/conditional/no‑go)  
2) Etapy i kamienie milowe z datami/właścicielami  
3) Zadania i zależności; dane/testy; środowiska  
4) Ryzyka i mitigacje; plan awaryjny/rollback  
5) Metryki i raportowanie postępu (cadence, odbiorcy)  
6) Załączniki (Gantt/board, checklisty, template raportu)


## Wymagane rozwinięcia

- Kryteria sukcesu i go/conditional/no‑go; definicja hipotez i metryk.  
- Plan danych/testów i środowisk; zależności (API, integracje).  
- Ryzyka/mitigacje i plan awaryjny (cofnięcie, fallback).


## Wymagane streszczenia

- Executive: cele, kryteria sukcesu, status kamieni, top ryzyka, data decyzji.


## Guidance (skrót)

- Jasne kryteria go/conditional/no‑go z metrykami; brak = brak decyzji.  
- Ustal etapy i kamienie z datami; realnie szacuj dostępność zespołów.  
- Przygotuj dane/testy i środowiska wcześniej; monitoruj postęp metrykami.  
- Miej plan rollback/awaryjny; dokumentuj ryzyka i decyzje.


## Checklisty Definition of Ready (DoR)

- [ ] Cele i kryteria sukcesu zdefiniowane; dane/testy/środowiska dostępne.  
- [ ] Etapy/kamienie/zależności opisane; ownerzy i komunikacja ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Etapy i kamienie zrealizowane; metryki ocenione vs kryteria; decyzja go/conditional/no‑go zapisana.  
- [ ] Ryzyka/mitigacje zaktualizowane; dokument w linkage_index; metadane aktualne.

