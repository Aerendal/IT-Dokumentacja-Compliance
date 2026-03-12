---
title: Feature Prioritization Matrix
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Feature Prioritization Matrix


## Metadane

- Właściciel: Product Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Zdefiniować metodę priorytetyzacji funkcji/backlogu (np. RICE/WSJF/MoSCoW), aby podejmować transparentne decyzje produktowe.


## Zakres i granice

- Obejmuje: kryteria i wagi (impact/reach/effort/risk/value/time criticality), scoring, proces zbierania danych, rolę interesariuszy, wizualizację i publikację wyników, przeglądy i rewalidację, mapowanie na roadmapę.
- Poza zakresem: szczegółowy opis każdej funkcji (w backlogu), zarządzanie portfelem projektów (osobne jeśli istnieje).


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: backlog funkcji/epik, dane o użytkowaniu i wartości, estymaty effort, ryzyka/techniczne długi, terminy/regulacje, zasoby.
- Wyjścia: macierz scoringu, ranking funkcji, rekomendacje do roadmapy, log decyzji, harmonogram przeglądów.


## Założenia
- Platforma analytics/monitoring dostępna.  
- Feature flagi zaimplementowane.  
- Zespół gotowy reagować na alerty.
## Otwarte pytania
- Jak długo monitorować po rollout?  
- Jak łączyć metryki jakości z doświadczeniem użytkownika (NPS/CSAT)?  
- Jak zarządzać wersjonowaniem eventów przy iteracjach?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: narzędzia backlogu/analytics, źródła danych value/effort, polityki governance produktu, cykl przeglądów, komunikacja do zespołów; brak – odnotuj.


## Fazy cyklu życia

Definicja kryteriów → Zbieranie danych → Scoring → Review → Roadmap update → Rewizje.



## Struktura sekcji (szkielet)

- Kryteria i wagi (definicje, źródła danych).
- Proces scoringu i zatwierdzania.
- Macierz i ranking (tabele/wykresy).
- Publikacja i komunikacja (PM/engineering/stakeholders).
- Przeglądy i rekalibracja (częstotliwość, zdarzenia trigger).
- Ryzyka i mitigacje (bias, dane niepełne).


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


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

- Ustal kryteria/wagi; zbierz dane; policz scoring; opublikuj ranking; aktualizuj w przeglądach.


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
- Adopcja: % użytkowników korzystających z funkcji.  
- Data completeness: odsetek oczekiwanych eventów.  
- Feature flag: przełącznik pozwalający sterować rolloutem.
## Przykłady użycia
- Monitoring nowego checkout flow.  
- Weryfikacja skuteczności rekomendacji.  
- Ocena nowej funkcji wyszukiwania.
## Ryzyka i ograniczenia
- Brak eventów → brak obserwowalności.  
- Złe progi → szum alertów.  
- Brak data quality → błędne wnioski.  
- Rollout bez flag → trudny rollback.
## Decyzje i uzasadnienia
- Progi KPI i alertów.  
- Strategia rollout/rollback i A/B.  
- Zakres data quality testów.  
- Kadencja raportów post-launch.
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

Kryteria → scoring; scoring → ranking; ranking → roadmap; przeglądy → rekalibracja wag.


## Wymagane rozwinięcia

- Szablon macierzy i instrukcja scoringu.
- Przykład policzonego zestawu funkcji.


## Wymagane streszczenia

- Jednostronicowy ranking top N z uzasadnieniem.


## Guidance

Cel: transparentna priorytetyzacja. DoR: backlog i dane value/effort; governance/role; kryteria. DoD: kryteria/wagi, macierz, ranking, publikacja, przeglądy; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Backlog + dane value/effort; [ ] Role/governance; [ ] Narzędzie macierzy.
- DoD: [ ] Kryteria/wagi/macierz/ranking/publikacja; [ ] Przeglądy; [ ] Sekcje N/A uzasadnione; metadane aktualne.
