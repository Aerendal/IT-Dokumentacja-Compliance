---
title: Business Value Proposition
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Business Value Proposition


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Precyzuje wartość biznesową oferowaną klientom/segmentom: problem, rozwiązanie, korzyści, dowody i wyróżniki. Ma być bazą dla roadmapy, pricingu i komunikacji.


## Zakres i granice

- Obejmuje: segmenty/ICP, problemy/pain points, rozwiązanie/produkty, korzyści mierzalne (KPI, ROI, TCO), wyróżniki vs alternatywy, dowody (case, dane), ryzyka/adopcję, założenia i hipotezy, wymagania do delivery (funkcje, jakość, wsparcie), metryki sukcesu.  
- Poza zakresem: szczegółowy plan marketingu/sprzedaży (oddzielne), backlog funkcji.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: badania rynku/klientów, dane użycia, konkurencja, koszty i pricing, benchmarki, wyniki eksperymentów, feedback sales/CS.  
- Wyjścia: karta value proposition, mapy problem→korzyść→dowód, priorytety funkcji, metryki sukcesu, lista hipotez do testów, komunikacja (one-liner/UVP), aktualizacje DoR/DoD.


## Założenia

- Dostęp do danych rynkowych i klientów.  
- Możliwość wykonywania eksperymentów.  
- Spójny przekaz w organizacji.


## Otwarte pytania

- Czy segmenty wymagają lokalizacji/regulacji specyficznych?  
- Jakie progi ROI musimy spełnić?  
- Jak często aktualizować value prop?


## Powiązania (meta)

- Key Documents: product_strategy, pricing_model, customer_research, go_to_market_plan, experiment_results, success_metrics.  
- Key Document Structures: segmenty, problem, korzyści, dowody, wyróżniki, metryki.  
- Document Dependencies: dane rynku/klientów, analizy konkurencji, wyniki badań/eksperymentów, koszty/pricing.


## Zależności dokumentu

Wymaga: zweryfikowanych danych rynkowych, listy segmentów/ICP, wyników badań/eksperymentów, wstępnego modelu kosztów/pricingu, feedbacku sales/CS. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja i weryfikacja (badania/eksperymenty).  
- Publikacja i użycie w roadmapie/pricingu/GTM.  
- Przeglądy okresowe na podstawie danych i konkurencji.



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

- linkage_index.jsonl (business/value/proposition)  
- product_strategy, pricing_model, customer_research, experiment_results, success_metrics


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

1. Wypełnij segmenty/problemy/korzyści i dowody; oblicz ROI/TCO.  
2. Zweryfikuj hipotezy eksperymentami; zaktualizuj messaging i roadmapę.  
3. Monitoruj metryki sukcesu; aktualizuj DoR/DoD i linkage_index.


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

- ICP: Ideal Customer Profile.  
- UVP: Unique Value Proposition.  
- ROI/TCO: zwrot/całkowity koszt.


## Przykłady użycia

- Nowy produkt B2B SaaS: value prop dla CTO/CFO.  
- Pivot funkcji po testach A/B.  
- Odświeżenie messagingu po wejściu nowego konkurenta.


## Ryzyka i ograniczenia

- Korzyści bez liczb → mała wiarygodność.  
- Brak dowodów → słaba sprzedaż/adopcje.  
- Nieaktualizacja po zmianie rynku → utrata dopasowania.


## Decyzje i uzasadnienia

- Które segmenty priorytetowe.  
- Jakie metryki sukcesu mierzyć (np. win rate, NRR).  
- Strategia pricingu vs wartości.


## Powiązania z innymi dokumentami

- product_strategy — kierunek.  
- pricing_model — monetizacja.  
- customer_research — dane jakościowe/ilościowe.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Brak formalnych standardów; stosuj wewnętrzne wytyczne strategii/brandingu.

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

- Segmenty/problemy → Korzyści/UVP → Dowody → Metryki sukcesu.  
- Hipotezy → Eksperymenty → Aktualizacja value prop.  
- Wyróżniki → Pricing/GTM → Roadmapa.


## Struktura sekcji

1) Segmenty/ICP i problemy  
2) Rozwiązanie/produkt (kluczowe funkcje)  
3) Korzyści i wartość (ROI/TCO/KPI)  
4) Wyróżniki vs alternatywy/konkurencja  
5) Dowody (case studies, dane, referencje)  
6) Hipotezy i ryzyka; plan testów/eksperymentów  
7) Metryki sukcesu i monitorowanie  
8) Komunikacja (one-liner, messaging)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Tabela problem→korzyść→dowód per segment.  
- ROI/TCO kalkulacje z założeniami.  
- Lista hipotez i plan eksperymentów/validacji.  
- Messaging/UVP w 1–2 zdaniach.


## Wymagane streszczenia

- Jednostronicowa karta value prop (segment, problem, rozwiązanie, korzyść, dowód).  
- Executive snapshot: top 3 korzyści, wyróżniki, metryki sukcesu.


## Guidance (skrót)

- Korzyści kwantyfikuj (czas, koszt, przychód, ryzyko); unikaj ogólników.  
- Porównuj z alternatywami (build/manual/konkurencja).  
- Weryfikuj hipotezy eksperymentami; aktualizuj po danych.  
- Zachowaj spójność messagingu w produkt/marketing/sales.  
- Utrzymuj value prop żywe: przeglądy kwartalne.


## Checklisty Definition of Ready (DoR)

- [ ] Segmenty/ICP i problemy zbadane.  
- [ ] Dane/dowody dostępne; hipotezy spisane.  
- [ ] Wstępny pricing/koszt policzony.  
- [ ] Plan eksperymentów i metryki sukcesu ustalone.  
- [ ] Messaging draft przygotowany.


## Checklisty Definition of Done (DoD)

- [ ] Karta value prop uzupełniona; dowody i liczby dodane.  
- [ ] Hipotezy zweryfikowane lub plan kolejnych testów; status/wersja/data uzupełnione.  
- [ ] Messaging uzgodniony z GTM; roadmapa/pricing zaktualizowane.  
- [ ] Linkage_index i success metrics dashboard zaktualizowane.  
- [ ] Ryzyka i decyzje zapisane.

