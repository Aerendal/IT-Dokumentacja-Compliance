---
title: Podstawy teorii kwantowej
status: needs_content
aligned: true
aligned_rev: 8
aligned_at: 2026-02-09
aligned_by: codex
---
# Podstawy teorii kwantowej


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Dać skrót kluczowych pojęć teorii kwantowej dla zespołów technicznych/produktowych pracujących z technologiami kwantowymi: stan/przestrzeń, operacje, ograniczenia fizyczne i modele obliczeń.


## Zakres i granice

- Obejmuje: postulaty/pojęcia (przestrzeń Hilberta, stan, pomiar, superpozycja, splątanie), operacje (bramy, unitarność, pomiar, kompozycja obwodów), różnice kubit vs klasyka, zasoby/ograniczenia (decoherence, T1/T2, fidelity, błędy, zarys QEC), modele obliczeń (obwodowy, adiabatyczny/annealing, variational/hybrid), słownik i źródła.  
- Poza zakresem: szczegółowe dowody matematyczne i implementacje sprzętowe (osobne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: potrzeby zespołów produkt/tech, materiały edukacyjne.  
- Wyjścia: skrót pojęć, słownik, lista źródeł do pogłębienia.



## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
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
1. Problem i algorytmy: opis, złożoność klasyczna vs kwantowa, algorytm kwantowy użyty.
2. Benchmarki: klasyczny baseline (HW/alg), kwantowy backend (sim/QPU), metryki (czas/jakość/koszt).
3. Warunki i ograniczenia: liczba kubitów, głębokość, błędy, noise, skalowalność.
4. Wyniki: porównanie metryk, wariancja, confidence; czy przewaga występuje.
5. Ryzyka/bariery: hardware availability, error rates, dane, koszty.
6. Wnioski i rekomendacje: Go/continue research/stop, roadmapa optymalizacji.
## Szybkie powiązania

- linkage_index.jsonl (quantum/basics)
- quantum_device_topology, calibration_runbook, transpilation_strategy, quantum_observability


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Użyj jako skrót/słownik dla zespołów; dodaj linki do materiałów firmowych.  
2. Aktualizuj, gdy zmieniasz stack sprzętowy lub gdy dochodzą nowe materiały szkoleniowe.


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
- **Spike/Soak** — krótki skok vs długi test stabilności.
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

- [ ] Pojęcia zdefiniowane jasno; ograniczenia i modele opisane; linki działają.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Słownik, one-pager PDF/MD, linki do kursów/książek, ADR (jeśli używany do decyzji).


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Użycie dokumentu (odsłony/odwołania), feedback zespołów, kompletność słownika.

## Kryteria ukończenia

- [ ] Skrót opublikowany, słownik/źródła dostępne; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Postulaty i pojęcia (przestrzeń Hilberta, stan, pomiar, superpozycja, splątanie)  
2) Operacje (bramy, unitarność, pomiar, kompozycja obwodów)  
3) Kubyty vs klasyka (superpozycja vs mieszanki, pomiar, korelacje)  
4) Zasoby i ograniczenia (decoherence, T1/T2, fidelity, błędy, zarys QEC)  
5) Modele obliczeń (obwodowy, adiabatyczny/annealing, variational/hybrid)  
6) Słownik i źródła (definicje, linki do kursów/książek)  
7) Ryzyka/uwagi (np. klasyczny koszt symulacji, skalowalność, szum)


## Wymagane rozwinięcia

- Krótkie definicje każdego pojęcia; przykłady bram i ich macierzy.  
- Zwięzłe opisy ograniczeń (czas koherencji, błędy) i dlaczego mają znaczenie dla algorytmów.  
- Porównanie modeli obliczeń i typowe przypadki użycia.


## Wymagane streszczenia

- One-pager: kluczowe pojęcia, ograniczenia, modele, linki do nauki.


## Guidance (skrót)

- Utrzymuj prosty język; linkuj do źródeł dla pogłębienia.  
- Podawaj intuicję + minimalną formułę; unikaj przeciążania matematycznego.  
- Podkreśl ograniczenia fizyczne i ich wpływ na projekt/algorytmy.


## Checklisty Definition of Ready (DoR)

- [ ] Zakres pojęć uzgodniony; źródła edukacyjne zebrane.


## Checklisty Definition of Done (DoD)

- [ ] Definicje i źródła dodane; słownik i one-pager gotowe; dokument w linkage_index; metadane aktualne.

