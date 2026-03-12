---
title: Map Styling Reference
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Map Styling Reference


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Referencja stylowania map (vector/raster): palety, warstwy, etykiety, zoomy i zasady czytelności. Ma zapewnić spójny wygląd i użyteczność map w produkcie.


## Zakres i granice

- Obejmuje: palety kolorów, typografie etykiet, hierarchię warstw (drogi/POI/teren), style ikon, grubości linii, zoom/LOD rules, tryby (light/dark/high-contrast), lokalizację/języki, fallbacki, performance (tile size, sprites), A11y (kontrast, czytelność), testy wizualne.  
- Poza zakresem: rendering engine implementation (osobne).


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia

- Wejścia: brand guidelines, wymagania map/produktowe, target urządzenia, dane źródłowe (tiles/POI), A11y/wymogi kontrastu, lokalizacja.  
- Wyjścia: pliki stylu (JSON/Mapbox/GL), zasady warstw i zoom, palety i tokeny, wytyczne ikon/etykiet, checklisty DoR/DoD.


## Założenia

- Dostępne dane i fonty/sprites.  
- Narzędzia do stylów/visual diff.  
- Zespół ma dostęp do device lab.


## Otwarte pytania

- Jak obsłużyć custom POI/brandowane warstwy?  
- Czy wymagany osobny styl offline?  
- Jak zarządzać aktualizacją danych/warstw?


## Powiązania (meta)

- Key Documents: design_system_guidelines, accessibility_compliance, localization_guidelines, performance_budget, map_data_sources.  
- Key Document Structures: palety, typografia, warstwy, zoom rules, tryby, A11y.  
- Document Dependencies: tile server/style JSON, sprites/icons, fonty, QA visual diff tools.


## Zależności dokumentu

Wymaga: brand palette/fonts, dane map (tiles/POI), wymagania kontrastu, lokalizacje językowe, target urządzeń/rozmiary ekranów. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja stylu i tokenów.  
- Implementacja i testy wizualne.  
- Rollout i iteracje na feedback/analytics.



## Struktura sekcji (szkielet)
- Cel i zakres zbioru
- Taksonomia i definicje
- Standardy/wytyczne
- Szablony/wzorce z przykładami
- Kryteria jakości i walidacja
- Utrzymanie i sposób zgłaszania zmian
## Szybkie powiązania

- linkage_index.jsonl (map/styling/reference)  
- design_system_guidelines, performance_budget, accessibility_compliance


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

1. Ustal palety/typografię i hierarchię warstw; zbuduj plik stylu.  
2. Przeprowadź testy wizualne/kontrast/locale; popraw.  
3. Rollout w produkcie; monitoruj feedback; aktualizuj DoR/DoD i linkage_index.


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

- LOD: Level of Detail.  
- Sprite atlas: połączone ikony dla performance.  
- WCAG kontrast: ratio tekst/tło.


## Przykłady użycia

- Styl mapy dla aplikacji mobilnej (light/dark).  
- High-contrast map dla dostępności.  
- Lokalizacja etykiet dla wielu języków.


## Ryzyka i ograniczenia

- Zbyt dużo detalu na niskich zoomach → szum.  
- Niski kontrast → nieczytelne.  
- Duże sprites/tile → performance.


## Decyzje i uzasadnienia

- Priorytety warstw i widoczność per zoom.  
- Palety kontrastowe i typografia.  
- Budżet performance (tile/sprites).


## Powiązania z innymi dokumentami

- design_system_guidelines — kolor/typografia.  
- map_data_sources — źródła.  
- accessibility_compliance — A11y.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- WCAG kontrast, wewnętrzne standardy brand/performance.  
- Wytyczne platform (iOS/Android/web) dla map i typografii.

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

- Palety/typografia → Warstwy/etykiety → A11y/kontrast.  
- Zoom rules → Performance → Czytelność.  
- Lokalizacja → Etykiety → Kerning/layout.


## Struktura sekcji

1) Palety i tokeny (light/dark/high-contrast)  
2) Typografia i etykiety (font, rozmiar, kerning, locale)  
3) Warstwy i hierarchia (drogi, POI, teren, granice)  
4) Ikony i sprites (rozmiar, kolor, states)  
5) Zoom/LOD rules (widoczność, generalizacja, min/max zoom)  
6) Kontrast i A11y (WCAG, tryb high-contrast)  
7) Performance (tile size, sprites atlas, caching)  
8) Testy i QA (visual diff, urządzenia, locale)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Plik stylu (JSON) z tokenami; lista warstw i zoom.  
- Tabela kontrastu i zgodności WCAG.  
- Visual diff checklist i scenariusze.  
- Guidelines ikon/etykiet (locale/RTL).


## Wymagane streszczenia

- One‑pager: palety/typografia/zoom rules.  
- Snapshot kontrastów i zgodności A11y.


## Guidance (skrót)

- Utrzymuj hierarchię: ważniejsze warstwy wyróżnione; redukuj szum na niższych zoomach.  
- Zapewnij kontrast i czytelność etykiet; testuj locale/RTL.  
- Optymalizuj performance: sprites, caching, mniejsze tile.  
- Testuj wizualnie na docelowych urządzeniach i zoomach.  
- Aktualizuj styl wraz z brand i feedbackiem.


## Checklisty Definition of Ready (DoR)

- [ ] Brand palette/fonts i wymagania A11y zebrane.  
- [ ] Dane map/warstw znane; target urządzeń określony.  
- [ ] Plan testów wizualnych/locale przygotowany.  
- [ ] Performance budget ustalony.  
- [ ] Narzędzia (style JSON, diff) dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Plik stylu i tokeny opublikowane; status/wersja/data uzupełnione.  
- [ ] Testy wizualne/kontrast/locale zaliczone; wyjątki opisane.  
- [ ] Performance w budżecie; monitoring ustawiony.  
- [ ] Dokumentacja/Linkage_index zaktualizowana.  
- [ ] Ryzyka/feedback zapisane.

