---
title: Common GIS Issues
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Common GIS Issues


## Metadane

- Właściciel: Document Owner
- Wersja: v0.3
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Typowe problemy w systemach GIS (dane, usługi, wydajność, wizualizacja) oraz standardowe procedury diagnostyki i naprawy, aby skrócić MTTR i poprawić jakość map/analiz.


## Zakres i granice

- Obejmuje: dane/CRS/projekcje, topologię, wydajność renderingu/tilingu, błędy usług WMS/WFS/WMTS/Vector Tiles, synchronizację baz (PostGIS/GeoServer), cache/CDN, uprawnienia/ACL, jakość styli/legend.  
- Poza zakresem: polityka pozyskiwania nowych danych (osobny dokument), projektowanie map (map_styling_reference), ogólne bezpieczeństwo sieci.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: logi serwerów map, CRS/układy odniesienia warstw, parametry kafelkowania, statystyki wydajności, zgłoszenia użytkowników, konfiguracje styli, parametry cache/CDN.  
- Wyjścia: katalog issue→diagnoza→mitigacja, checklisty diagnostyczne, matryca szybkich poprawek, rekomendacje optymalizacji, linki do narzędzi testowych i linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: map_styling_reference, gis_operations_runbook, data_quality_playbook, performance_tuning_tips, access_control_policy, cache_management_guidelines.  
- Key Document Structures: dane/CRS, usługi, wydajność/cache, uprawnienia, wizualizacja, runbooki.  
- Document Dependencies: GeoServer/MapServer, PostGIS, CDN/cache, monitoring, CRS katalog, CMDB usług.



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

- linkage_index.jsonl (gis/issues/common)  
- map_styling_reference, gis_operations_runbook, performance_tuning_tips


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

1. Wybierz kategorię problemu, wykonaj checklistę diagnostyczną.  
2. Zastosuj kroki naprawcze/rollback; zweryfikuj metryki.  
3. Zaktualizuj runbook/checklistę i linkage_index; poinformuj zgłaszającego.


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

- [ ] Każdy typowy problem ma diagnozę i mitigację; CRS/topologia poprawne.  
- [ ] Cache/CDN i usługi map mają monitoring i alerty; style/versioning udokumentowane.  
- [ ] Linkage_index uzupełniony; checklists zaktualizowane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Logi/trace usług map, konfiguracje styli, CRS/reprojection rules, cache settings, raporty topologii, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- MTTR incydentów GIS, cache hit ratio, czas renderu vs SLO, liczba incydentów CRS mismatch/topologia, liczba rollbacków styli/warstw.

## Kryteria ukończenia

- [ ] Dokument skraca MTTR dla incydentów GIS i jest powiązany w linkage_index.


## Struktura sekcji

1) Kategorie problemów i symptomy  
2) Checklisty diagnostyczne per kategoria (CRS/topologia/usługi/cache/ACL/styl)  
3) Kroki naprawcze i fallbacki (reprojekcja, fix topologii, regen cache, rollback stylu)  
4) Narzędzia testowe (QGIS, ogrinfo, curl GetCapabilities, tiles debug)  
5) Alerty i metryki (czas renderu, 4xx/5xx usług map, cache hit/miss)  
6) Ryzyka, decyzje, pytania otwarte  
7) Załączniki (szablon checklisty, przykłady logów, ADR/waiver log)


## Wymagane rozwinięcia

- Lista najczęstszych CRS i reguł reprojekcji; typowe błędy „EPSG mismatch”.  
- Szablon checklisty dla WMS/WFS/WMTS błędów i dla Vector Tiles.  
- Procedura czyszczenia/regeneracji cache (warstwa/region/czas).  
- Typowe problemy topologii (self‑intersections, gaps) i sposoby naprawy.  
- Scenariusze wydajności (za duże kafle, brak min/max zoom, złe simplification).


## Wymagane streszczenia

- Executive: top 5 problemów i szybkie fixy; skrót CRS/reguł organizacyjnych.


## Guidance (skrót)

- Najpierw potwierdź CRS i reprojekcję; debug zaczynaj od GetCapabilities/HealthCheck.  
- Waliduj dane i style przy publikacji; wersjonuj warstwy i style.  
- Monitoruj czas renderu i 4xx/5xx; cache invaliduj celowanie, nie globalnie.  
- Dokumentuj fixy i aktualizuj checklisty oraz linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Logi i metryki danej usługi dostępne; znany CRS/warstwa/zakres.  
- [ ] Reprodukcja problemu lub zrzut zapytania; wersje danych/styli zidentyfikowane.  
- [ ] Dostęp do serwera map/cache potwierdzony.


## Checklisty Definition of Done (DoD)

- [ ] Problem usunięty, test/regresja OK; metryki/alerty w normie.  
- [ ] Runbook/checklista zaktualizowane; użytkownik poinformowany; linkage_index/CMDB zaktualizowane, status/metadane aktualne.  
- [ ] checklisty DoR/DoD odhaczone.

