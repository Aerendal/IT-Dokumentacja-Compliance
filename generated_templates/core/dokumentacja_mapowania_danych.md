---
title: Dokumentacja mapowania danych
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Dokumentacja mapowania danych


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać odwzorowanie danych między źródłami a systemem docelowym: kolumny, transformacje, walidacje, deduplikacja, wersjonowanie i artefakty testowe.


## Zakres i granice

- Obejmuje: źródła i model docelowy (tabele/kolumny/typy), mapowanie kolumna↔kolumna, transformacje (jednostki/kodowania/reguły), walidacje jakości (null/domain/referencyjne), matching/deduplikację, wersjonowanie/changelog, próbki i testy mapowania.  
- Poza zakresem: definicja modeli domenowych (osobne specy) i pipeline’ów ETL (osobne runbooki/ IaC).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: schematy źródeł i docelowe, słownik danych, reguły biznesowe, jednostki/kodowania, polityki jakości danych, przykłady danych, wymagania zgodności.  
- Wyjścia: tabela mapowania, reguły transformacji i walidacji, definicje dedupe/matching, changelog, zestaw testów i próbek.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: data_model, data_dictionary, data_quality_policy, data_governance_requirements, lineage_standards, etl_pipeline_spec, data_retention_policy.
- Key Document Structures: mapowanie, transformacje, walidacje, dedupe, wersjonowanie, próbki/testy.
- Document Dependencies: źródła (DB/files/APIs), docelowy DWH/lake, ETL/ELT narzędzia, DQ narzędzia, lineage/catalog.



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

- Cel i zakres dokumentu
- Główne sekcje merytoryczne
- Powiązania z innymi dokumentami
- Wymagane zatwierdzenia i przeglądy
- Historia zmian

## Szybkie powiązania

- linkage_index.jsonl (data/mapping_docs)
- data_model, data_dictionary, data_quality_policy, data_governance_requirements, lineage_standards, etl_pipeline_spec, data_retention_policy


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **ISO 20000-1** — System Zarządzania Usługami IT (SMS)
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

1. Wypełnij tabelę mapowania i transformacje; dodaj walidacje i dedupe.  
2. Dodaj testy/próbki i changelog; podlinkuj do lineage/catalog.  
3. Aktualizuj po zmianach schematu; zamknij DoR/DoD i linkage_index.


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

- [ ] Każde pole ma mapowanie/regułę i walidację; dedupe/matching opisane.  
- [ ] Testy pokrywają krytyczne pola/reguły; changelog aktualny; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Arkusze mapowania, reguły transformacji, test cases, sample data, changelog, lineage links, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % pól z walidacją/testem, liczba błędów mapowania, czas aktualizacji mapy po zmianie schematu, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Mapa aktualna, testy przechodzą, walidacje zdefiniowane; dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Źródła i model docelowy (tabele/kolumny/typy, słownik)  
2) Mapowanie kolumna↔kolumna i transformacje (jednostki, kodowania, reguły)  
3) Walidacje jakości (null/domain/referencyjne), matching/deduplikacja  
4) Wersjonowanie i zmiany (changelog, zakres zmian, wersja mapy)  
5) Próbki i testy mapowania (sample data, test cases, asercje)  
6) Ryzyka i waivery (sunset/kompensacje)  
7) Załączniki (arkusze map, pliki testów, słownik, lineage)


## Wymagane rozwinięcia

- Tabela mapowania z regułami; jednostki/kodowania; konwersje czasu/stref.  
- Walidacje: null/domain/PK/FK, zakresy, referencje, jakościowe (dup, uniqueness).  
- Reguły dedupe/matching (klucze, fuzzy, progi) i kolejność aplikacji.  
- Changelog wersji map; zestaw testów (input→expected), próbki danych.


## Wymagane streszczenia

- Executive: status mapy, główne zmiany w wersji, top ryzyka jakości, wyniki testów.


## Guidance (skrót)

- Trzymaj mapę w repo (CSV/JSON) z wersjonowaniem; każde pole ma regułę i właściciela.  
- Wymuszaj walidacje i testy automatyczne w ETL/CI; brak testu = luka.  
- Jednostki/kodowania zawsze explicite; loguj zmiany w changelogu.  
- Dedupe/matching definiuj z progami i kolejnością; zapisuj decyzje/waivery.


## Checklisty Definition of Ready (DoR)

- [ ] Schematy źródeł/docelowy i słownik dostępne; reguły biznesowe znane.  
- [ ] Narzędzia ETL/DQ i repo mapy przygotowane; właściciele zidentyfikowani.


## Checklisty Definition of Done (DoD)

- [ ] Mapowanie/transformacje/walidacje/dedupe opisane; testy/próbki i changelog dodane.  
- [ ] Waivery (jeśli) z sunset; dokument w linkage_index; metadane aktualne.

