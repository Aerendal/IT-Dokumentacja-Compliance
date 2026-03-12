---
title: Venue Utilization Report
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Venue Utilization Report


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Raportować wykorzystanie obiektu (sale, strefy, zasoby) w zadanym okresie, aby optymalizować przychody, harmonogramy i koszty operacyjne.


## Zakres i granice

- Obejmuje: wskaźniki obłożenia (occupancy, utilization rate), przychody per strefa/czas, harmonogram rezerwacji, no-show/cancel, przepustowość wejść, zużycie zasobów (media, personel), anomalie, rekomendacje optymalizacji.
- Poza zakresem: pełne planowanie eventów (osobne), marketing.


## Użytkownicy i interesariusze
- SRE/Infra, FinOps, Security/Compliance, Product/Teams właściciele danych, Leadership.
## Wejścia i wyjścia

- Wejścia: kalendarz rezerwacji, system biletowy, dane wejść/wyjść, POS, koszt mediów/personelu, SLA obiektu, dane pogodowe jeśli istotne.
- Wyjścia: raport (sekcje poniżej), metryki KPI, wykresy obłożenia i przychodów, lista rekomendacji i action items.


## Założenia
- Dostępne metryki i billing; tagowanie działa; polityki retencji/bezpieczeństwa obowiązują.
## Otwarte pytania
- Jaka częstotliwość raportu i kto jest ownerem?  
- Czy wymagane są raporty per klient/tenant?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: system rezerwacji/biletów, dane wejść, POS, koszty mediów/personelu, SLA; brak – odnotuj.


## Fazy cyklu życia

Zbieranie danych → Analiza → Raport → Rekomendacje → Follow-up.



## Struktura sekcji (szkielet)

- Zakres okresu i stref.
- KPI: occupancy/utilization, przychód per m2/godz., no-show/cancel, throughput wejść.
- Analiza przychodów i kosztów (media, personel, sprzątanie).
- Anomalie i insighty (szczyty/dole, overbooking, puste okna).
- Rekomendacje (zmiana cenników, grafiku, layoutu, staffing).
- Action items (owner, termin, status).


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

- Zbierz dane, policz KPI, wskaż anomalie, dodaj rekomendacje, przypisz akcje, śledź follow-up.


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
- Hot/Warm/Cold, Tiering, Lifecycle, Cost/GB, Capacity %, Public exposure.
## Przykłady użycia
- Raport m-c: growth 8%, hot 40% → rekomendacja tiering + cleanup orphaned buckets.  
- Anomalia kosztów: spike w regionie X → analiza tagów → restrykcja public access.
## Ryzyka i ograniczenia
- Brak tagów/właścicieli → brak odpowiedzialności; brak retencji → ryzyko compliance; brak alertów → overflow/koszty.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- FinOps Policy, Data Lifecycle, Backup & Retention, Security Baseline (storage), Tagging Standards, Capacity Planning.
## Powiązania z sekcjami innych dokumentów
- Tagging → właściciele; Lifecycle → retencja/tiering; Security → public access/szyfrowanie.
## Słownik pojęć w dokumencie
- Hot/Warm/Cold, Tiering, Lifecycle, Cost/GB, Capacity %, Public exposure.
## Wymagane odwołania do standardów
- Polityki retencji/bezpieczeństwa/FinOps, wymogi regulatorów dot. danych (jeśli dotyczy).
## Mapa relacji sekcja→sekcja
- Metryki/KPI → Ryzyka → Rekomendacje → Plan działań → Follow‑up.
## Mapa relacji dokument→dokument
- Storage Report → FinOps/Lifecycle/Security → Capacity/DR → Audit/Compliance.
## Ścieżki informacji
- Metryki/billing → Analiza → Rekomendacje → Plan → Follow‑up → Kolejny raport.
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
- Dashboardy storage/billing, surowe dane, listy tagów/owners, plan działań, raport PDF/BI.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- SRE/Infra → FinOps → Security/Compliance → Leadership/Owner sign‑off.
## Metryki jakości
- Dokładność danych vs billing, tempo realizacji rekomendacji, zmiana kosztów/pojemności, liczba otwartych wyjątków, public exposure findings.
## Kryteria ukończenia
- [ ] Raport opublikowany; rekomendacje/owner/ETA zapisane; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

Obłożenie → przychody/koszty → rekomendacje; no-show → harmonogram; anomalie → action items.


## Wymagane rozwinięcia

- KPI definicje i źródła.
- Dane kosztowe → format i częstotliwość.


## Wymagane streszczenia

- 1-stronicowe podsumowanie KPI + 3 najważniejsze rekomendacje.


## Guidance

Cel: lepsze wykorzystanie obiektu. DoR: dane rezerwacji/pos/wejść/kosztów. DoD: KPI/analiza/rekomendacje/action; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Dane rezerwacji/wejść/POS/kosztów; [ ] Zakres okresu/stref; [ ] SLA/cele.
- DoD: [ ] KPI i analiza; [ ] Rekomendacje i action items; [ ] Sekcje N/A uzasadnione; metadane aktualne.
