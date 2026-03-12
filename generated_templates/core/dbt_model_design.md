---
title: dbt Model Design
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# dbt Model Design


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Standard projektowania modeli dbt: warstwy, nazewnictwo, materializacje, testy, dokumentacja, performance i review, aby zapewnić spójność i utrzymywalność hurtowni.


## Zakres i granice

- Obejmuje: konwencje nazw (sources/stg/int/fct/marts), kontrakty i schematy, materializacje i partitioning, dependency/lineage, testy (unikalność, not null, relacje, custom), dokumentację i opis kolumn, performance (COST/CLUSTER/SORT keys), polityki review.  
- Poza zakresem: orkiestracja (Airflow/CI) i monitoring produkcyjny (osobne dokumenty), polityki dostępu danych (w design_abac/row level security).


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: wymagania biznesowe, model koncepcyjny, źródła danych (contracts), volumetria/SLI, limity kosztów, standardy nazewnictwa domen, polityki jakości danych.  
- Wyjścia: szablony modeli i schematy YAML, decyzje materializacji/partycji, testy i dokumentacja kolumn, checklisty review, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: dbt_project_guide, dbt_test_specification, data_contracts, lineage_strategy, cost_optimization, data_quality_policy, design_abac.  
- Key Document Structures: warstwy, nazewnictwo, materializacje, testy, dokumentacja, performance, review.  
- Document Dependencies: warehouse platform (BigQuery/Snowflake/Redshift), Git/CI, data contracts, observability (freshness), permissions model.



## Zależności dokumentu
Jeżeli brak danych w bazie: wypisz znane zależności (dokumenty, kontrakty, usługi), wskaż właścicieli i wpływ na kolejność prac; gdy brak zależności – zapisz to wprost.
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
- Faza 10: Incident Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 11: Monitoring / Observability: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 12: Dokumentacja referencyjna: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 13: Szkolenie / Onboarding: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 14: Komunikacja stakeholders: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 15: Knowledge Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 16: Postmortem / Retrospektywa: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 17: Budżetowanie / Cost Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 18: Vendor Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 19: Governance / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 20: Decommission / Sunset: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 21: DR / BCP: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 22: Change Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 23: Capacity Planning: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)
- Rola i kontekst: hero/prop/filler, dystans oglądu, czytelność gameplay.
- Styl i język form: realizm/stylizacja, shape language, proporcje, silhouette tests.
- Skala i jednostki: wymiary docelowe, pivot/origin, orientacja.
- Podziały materiałowe i kolor: liczba materiałów, break-up, maski vertex/texture, warianty kolorystyczne.
- Poziom detalu: target LOD0 (detal, bevel), stany (clean/dirty/damaged/destroyed).
- Punkty interakcji i attach: uchwyty, sloty, punkty VFX/SFX, collision intent.
- Wymagania techniczne: mapy PBR potrzebne, texel density, LOD count, collider typ, naming.
- Referencje: moodboard, zdjęcia, wcześniejsze assety do reuse.
## Szybkie powiązania

- linkage_index.jsonl (data/dbt_model_design)  
- dbt_project_guide, dbt_test_specification, data_quality_policy, design_abac


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

1. Zmapuj wymagania na warstwy; wybierz nazwy i materializacje zgodnie z tabelą konwencji.  
2. Dodaj schemat YAML z kontraktem kolumn i testami; opisz kolumny i exposures.  
3. Upewnij się, że PR spełnia checklistę i linki w linkage_index są dodane.


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

- [ ] Klucz modelu unikalny i testowany; lineage bez cykli; brak SELECT *.  
- [ ] Materializacja dobrana do wolumetrii; testy i dokumentacja kompletne; meta zawiera owner/PII/SLA.  
- [ ] Linkage_index i ADR odzwierciedlają decyzje.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Pliki model.sql i schema.yml, tabela konwencji nazw, makra materializacji, wyniki testów, raport kosztu/czasu kompilacji, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Pokrycie testami (% modeli/kolumn), czas budowy i koszt per model, liczba rollbacków, liczba naruszeń konwencji nazw, wskaźnik brakujących meta/dokumentacji.

## Kryteria ukończenia

- [ ] Model spełnia standardy warstw, testów, dokumentacji i wydajności i jest gotowy do produkcji.


## Struktura sekcji

1) Warstwy i nazewnictwo (sources, stg_, int_, dim/fct, marts, shared seeds, macros)  
2) Kontrakty i schematy (sources + models, kolumny, typy, constraints)  
3) Materializacje i wydajność (view/table/incremental, partition/cluster, merge strategy, late‑arriving)  
4) Testy jakości (built‑in, relationships, accepted_values, custom, data tests, freshness)  
5) Dokumentacja i opis kolumn (docs blocks, exposures, meta tags)  
6) Lineage i dependency (ref/source, naming, DAG hygiene, fan‑out/fan‑in)  
7) Code review i standardy stylu (SQL style, macros, PR checklist)  
8) Załączniki (przykłady, makra, ADR, waiver log)


## Wymagane rozwinięcia

- Tabela konwencji nazw i prefiksów per warstwa/domena.  
- Wytyczne materializacji: kiedy incremental/merge + klucz naturalny/techniczny, strategie deduplikacji, okna czasowe.  
- Testy minimalne i rozszerzone per warstwa; kryteria dla accepted_values.  
- Zasady dokumentowania kolumn i exposures; wymagane meta (owner, SLA, PII).  
- PR checklist (schema diff, performance, security/PII, tests run).


## Wymagane streszczenia

- Executive: pokrycie warstw i testów, zasady materializacji, główne ryzyka kosztowe/perf.


## Guidance (skrót)

- Utrzymuj cienkie warstwy: stg do czyszczenia, int do logiki łączeń, dim/fct do prezentacji.  
- Domyślnie incremental+merge z kluczem deterministycznym; unikaj fan‑out bez potrzeb.  
- Każdy model musi mieć testy not null/unique na klucz oraz relację do źródeł.  
- Dokumentacja i meta są wymagane przy tworzeniu/zmianie modelu; PR bez testów jest blokowany.  
- Mierz koszt i czas kompilacji; stosuj cluster/partition, ogranicz SELECT *.


## Checklisty Definition of Ready (DoR)

- [ ] Źródła i klucze biznesowe zidentyfikowane; volumetria/SLI znane.  
- [ ] Wybrane warstwy i materializacja; uzgodnione PII i polityka dostępu.  
- [ ] Wymagania testów i dokumentacji zaakceptowane.


## Checklisty Definition of Done (DoD)

- [ ] Model posiada kontrakt, testy, dokumentację kolumn, meta; DAG i lineage czyste.  
- [ ] Materializacja/partycje zoptymalizowane, koszty zaakceptowane; PR checklist spełniona; linkage_index zaktualizowany.  
- [ ] Status/metadane aktualne; checklisty DoR/DoD odhaczone.

