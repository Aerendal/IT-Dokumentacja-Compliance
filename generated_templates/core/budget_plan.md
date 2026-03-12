---
title: Budget Plan
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Budget Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Przygotować plan budżetu (OPEX/CAPEX) dla projektu/portfolio, obejmujący założenia, przydziały, harmonogram wydatków, ryzyka i ścieżkę zatwierdzeń, tak aby zapewnić przejrzystość i kontrolę kosztów.


## Zakres i granice

- Obejmuje: założenia finansowe, kategorie kosztów (ludzie, licencje, infra, vendorzy, podróże, rezerwy), CAPEX vs OPEX, harmonogram wydatków, scenariusze i wrażliwość, kursy walut, amortyzację, KPI finansowe (TCO, ROI), proces zatwierdzeń i limitów, monitorowanie wykonania.
- Poza zakresem: szczegółowe faktury i księgowania (system finansowy), polityki zakupowe (linkowane).


## Użytkownicy i interesariusze

- [Rola] — [potrzeby/odpowiedzialności]
- [Rola] — [potrzeby/odpowiedzialności]


## Wejścia i wyjścia

- Wejścia: backlog/plan projektów, stawki i cenniki, kontrakty, headcount plan, kursy FX, polityki zakupowe, historyczne wydatki, cele KPI.
- Wyjścia: arkusz budżetu (plan vs miesiące/kwartały), założenia i scenariusze, rezerwy i ryzyka, ścieżka akceptacji, plan raportowania (burn rate, odchylenia), wersjonowanie zmian.


## Założenia

- [Założenie 1]
- [Założenie 2]


## Otwarte pytania

- [Pytanie 1]
- [Pytanie 2]


## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: dane finansowe, kontrakty, polityki zakupowe, kursy FX, backlog projektów; brak – odnotuj.


## Fazy cyklu życia

Planowanie → Zatwierdzenie → Wykonanie/monitoring → Korekty → Zamknięcie/retrospektywa.



## Struktura sekcji (szkielet)

- Założenia i scenariusze (bazowy/pesymistyczny/optymistyczny).
- Kategorie kosztów (tabela) i CAPEX/OPEX.
- Harmonogram wydatków (miesiące/kwartały, FX jeśli).
- Rezerwy i ryzyka kosztowe.
- KPI finansowe (TCO/ROI/IRR) i metryki operacyjne (burn, run rate).
- Ścieżka akceptacji i limity wydatków.
- Monitoring i raportowanie odchyleń.
- Zmiany i wersjonowanie (changelog).


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **DORA** — Ustawa o Cyfrowej Odporności Operacyjnej (UE)

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

- Wypełnij założenia, kategorie i harmonogram; uzyskaj akceptacje; monitoruj odchylenia i aktualizuj plan.


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
- **CAPEX/OPEX** — wydatki inwestycyjne vs operacyjne.
- **Czułość** — jak wynik zmienia się przy zmianie kluczowych założeń.
## Przykłady użycia

- [Przykład 1]
- [Przykład 2]


## Ryzyka i ograniczenia

- [Ryzyko 1]
- [Ryzyko 2]


## Decyzje i uzasadnienia

- [Decyzja 1]
- [Decyzja 2]


## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód]
- [Dokument Z → Sekcja W] — [powód]


## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1]
- [Standard 2]


## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ]
- [Sekcja C] -> [Sekcja D] : [typ]


## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ]
- [Dokument C] -> [Dokument D] : [typ]


## Ścieżki informacji

- [Wejście] → [Źródło] → [Rozwinięcie] → [Wyjście]
- [Wejście] → [Źródło] → [Streszczenie] → [Wyjście]


## Weryfikacja spójności

- [ ] Ścieżki informacji zamknięte
- [ ] Brak sprzecznych relacji
- [ ] Sekcje krytyczne mają źródła


## Lista kontrolna spójności relacji

- [ ] Relacje mają sekcje źródłowe
- [ ] Relacje nie są sprzeczne
- [ ] Cross-doc uzasadnione
- [ ] Rozwinięcia/streszczenia odnotowane


## Artefakty powiązane

- [Artefakt 1]
- [Artefakt 2]


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]


## Ścieżka akceptacji

1. Autor przygotowuje wersję roboczą i przeprowadza samorecenzję.
2. Recenzent techniczny (Tech Lead / BA) weryfikuje merytorycznie.
3. Właściciel procesu zatwierdza treść i zakres.
4. PM / Scrum Master aktualizuje metadata (wersja, data, status).
5. Dokument trafia do repozytorium i jest linkowany w Szybkie powiązania.

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

Np. założenia → scenariusze; kategorie kosztów → harmonogram; ryzyka → rezerwy; KPI → monitorowanie.


## Wymagane rozwinięcia

- Tabele kosztów → źródła stawek/kontraktów.
- FX → źródła kursów i częstotliwość aktualizacji.


## Wymagane streszczenia

- Jednostronicowy snapshot: suma CAPEX/OPEX, rezerwy, KPI, kluczowe ryzyka.


## Guidance

Cel: jasny, śledzalny plan kosztów. DoR: backlog, stawki, kontrakty, polityki zakupowe zebrane. DoD: tabele kosztów, harmonogram, rezerwy, KPI, akceptacje i monitoring opisane; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Backlog i stawki/kontrakty dostępne; [ ] Polityki zakupowe i kursy FX znane; [ ] Owner finansowy/PM przypisany.
- DoD: [ ] Tabele kosztów/harmonogram/KPI gotowe; [ ] Rezerwy/ryzyka opisane; [ ] Ścieżka akceptacji i monitoring dodane; sekcje N/A uzasadnione; metadane aktualne.

