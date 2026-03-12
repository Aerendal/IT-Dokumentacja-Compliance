---
title: Ad Spend Monitoring
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Ad Spend Monitoring


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Określa sposób monitorowania i kontroli wydatków reklamowych (digital/offline), aby wykrywać odchylenia, oszustwa, nieefektywne kampanie oraz zapewnić zgodność budżetową. Dostarcza metryki, alerty, raporty i procedury reakcji.


## Zakres i granice

- Obejmuje: kanały digital (search, social, display, video, programmatic), podstawowe offline (OOH/print jeśli raportowane), metryki finansowe i wydajnościowe, budżety/limity, harmonogram raportów, alerty odchyleń, wykrywanie fraudu (click fraud, bot traffic), zgodność tagowania/utm, integracje z narzędziami (ad platforms, analytics, BI, antifraud).
- Poza zakresem: strategia mediowa i kreacje (opis w planach kampanii), negocjacje stawek z dostawcami.


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: budżety/konta/kampanie, dane kosztów z platform (API), dane wynikowe (konwersje/attribution), benchmarki KPI, limity dzienne/miesięczne, reguły antyfraud, kalendarz kampanii, kursy walut (jeśli multi‑currency).
- Wyjścia: dashboardy i alerty, raporty cykliczne, lista odchyleń i działań korygujących, log audytowy zmian budżetów, rekomendacje optymalizacji.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: marketing_plan, attribution_model, antifraud_policy, data_governance, finops/budget_policy.
- Key Document Structures: budżety/limity, metryki, alerty, raporty, działania korygujące.
- Document Dependencies: dostępy do API platform, DWH/BI, antifraud, kursy walut, zgody privacy/cookies.


## Zależności dokumentu

Wymaga aktualnych budżetów/limitów i mapy kont/kampanii, dostępów do API oraz polityki tagowania/attribution. Bez nich DoR pozostaje otwarte.


## Fazy cyklu życia

- Planowanie: import budżetów, limity, KPI, mapowanie kont.
- Operacje bieżące: monitoring kosztów/KPI, alerty, reagowanie.
- Optymalizacja: rekomendacje i przeniesienia budżetu.
- Audyt/Compliance: log zmian, zgodność tagowania i polityk wydatków.



## Struktura sekcji (szkielet)
- SLO i device matrix.
- Sceny referencyjne i testy syntetyczne.
- Instrumentacja i eventy (FPS/frametime/stutter, HW metrics).
- Telemetria prod (sampling, priv), storage i koszty.
- Dashboardy i alerty (progi, kanały, runbook).
- Raporty wersja/build → FPS.
- Ryzyka i mitigacje.
## Szybkie powiązania
- vm-performance-monitoring
- transaction-monitoring
- throughput-monitoring
- synthetic-monitoring
- session-monitoring

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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
- Zdefiniuj SLO i sceny; zainstrumentuj; ustaw sampling/alerty; monitoruj; raportuj regresje; iteruj optymalizacje.
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

- Budżety/limity → Metryki/alerty → Raporty → Działania korygujące.
- Tagowanie/attribution → Metryki wydajności → Rekomendacje.
- Antifraud → Alerty odchyleń → Eskalacje/budżet stop.


## Struktura sekcji

1) Budżety i limity (miesięczne/dzienne, per kanał/kampania/konto)  
2) Metryki i KPI (koszt, CPC/CPM/CPL/CPA/ROAS, viewability, fraud, pacing)  
3) Źródła danych i integracje (platformy, DWH/BI, antifraud, waluty)  
4) Alerty i progi (pacing, koszt vs. plan, fraud, brak danych/tagów)  
5) Raportowanie (częstotliwość, odbiorcy, format, widoki exec/ops)  
6) Działania korygujące i eskalacje (stop, przeniesienie budżetu, zmiana stawek)  
7) Zgodność i audyt (log zmian, dostępy, privacy/tagging)

