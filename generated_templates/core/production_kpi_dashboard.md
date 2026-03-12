---
title: Production KPI Dashboard
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Production KPI Dashboard


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaprojektować dashboard KPI dla środowiska produkcyjnego: kluczowe metryki, źródła danych, standardy wizualizacji, alerty i governance, aby umożliwić szybkie decyzje operacyjne i produktowe.


## Zakres i granice

- Obejmuje: definicje KPI (biznesowe i techniczne), źródła danych (DB, eventy, monitoring), SLA/SLO, segmentacje (region, kanał, plan), wizualizacje i layout, progi alertów, odświeżanie/replikacja, kontrolę dostępu, wersjonowanie/zmiany, dokumentację definicji.  
- Poza zakresem: implementacja ETL/ELT (osobne dokumenty), szczegółowy design narzędzia BI (stylistyka).


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: katalog KPI, definicje metryk, źródła danych, wymagania interesariuszy, polityka dostępu, standardy wizualizacji, SLA raportowania.  
- Wyjścia: specyfikacja dashboardu (karty, filtry, layout), słownik metryk, plan danych i odświeżania, matryca dostępu, alerty, checklisty DoR/DoD, changelog.


## Założenia

- Dane źródłowe są wiarygodne; istnieje metrics layer lub definicje.  
- Użytkownicy mają SSO.  
- Zespół jest w stanie utrzymać SLA danych/alertów.


## Otwarte pytania

- Jak wersjonować definicje KPI?  
- Jak długo trzymać historię alertów?  
- Czy potrzebne są warianty dashboardu per region/segment?

## Powiązania (meta)

- Key Documents: performance_metrics_dashboard, monitoring_strategy_document, data_governance_requirements, access_control_policy, data_quality_playbook, release_readiness_statement.  
- Key Document Structures: metryki, dane, wizualizacje, alerty, dostęp, governance.  
- Document Dependencies: BI tool, data warehouse/lake, metrics layer, IAM/SSO, monitoring/alerting.


## Zależności dokumentu

Wymaga: zatwierdzonej listy KPI i definicji, dostępności danych w DWH/metrics layer, wymagań od interesariuszy, polityki dostępu i standardów wizualizacji, narzędzia BI. Brak = brak DoR.


## Fazy cyklu życia

- Definicja metryk i wymagań.  
- Projekt layoutu i dostępu.  
- Implementacja i testy danych/alertów.  
- Publikacja i przeglądy.  
- Utrzymanie i zmiany.



## Struktura sekcji (szkielet)
- Zakres raportu i okres
- Definicje metryk/KPI i źródła danych
- Wyniki z trendami i wizualizacjami
- Insighty i obserwacje
- Ryzyka/odchylenia i ich wpływ
- Rekomendacje i plan działań z właścicielami
- Załączniki/metodologia
## Szybkie powiązania

- linkage_index.jsonl (production/kpi/dashboard)  
- data_governance_requirements, monitoring_strategy_document


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum
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

1. Zbierz wymagania i definicje KPI; uzupełnij słownik.  
2. Zaprojektuj layout i dostęp; skonfiguruj dane/odświeżanie.  
3. Ustaw alerty; przetestuj dane i wydajność.  
4. Publikuj dashboard; monitoruj i aktualizuj przy zmianach KPI.


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

- KPI: kluczowy miernik celu.  
- SLO: target poziomu usługi.  
- Metrics layer: warstwa semantyczna nad danymi.


## Przykłady użycia

- Dashboard produktowy: aktywność użytkowników, retencja, churn.  
- Dashboard operacyjny: SLA incydentów, dostępność, błędy API.  
- Dashboard finansowy: przychód, marża, koszty infra.


## Ryzyka i ograniczenia

- Niespójne definicje KPI → błędne decyzje.  
- Opóźnione odświeżanie → stare dane.  
- Brak kontroli dostępu → wycieki danych.  
- Zbyt wiele kart → brak skupienia.


## Decyzje i uzasadnienia

- Wybór narzędzia BI i metrics layer.  
- Częstotliwość odświeżania i progi alertów.  
- Układ kart i priorytety KPI.  
- Zakres dostępu i audytu.


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

- KPI/definicje ↔ Źródła ↔ Dane/odświeżanie.  
- Wizualizacje ↔ Alerty ↔ Dostęp.  
- Governance ↔ Changelog ↔ Audyt.


## Struktura sekcji

1) Cele i użytkownicy dashboardu  
2) Lista KPI + definicje (wzory, źródła, segmenty)  
3) Projekt wizualizacji (karty, drill-down, filtry)  
4) Dane i odświeżanie (harmonogram, latency, quality)  
5) Alerty i SLO (progi, kanały, eskalacje)  
6) Dostęp i bezpieczeństwo  
7) Governance: zmiany, wersjonowanie, audyt  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Słownik KPI (nazwa, definicja, wzór, źródło, segment, właściciel).  
- Makieta layoutu z grupowaniem kart i filtrami.  
- Plan odświeżania (częstotliwość, SLA, latency).  
- Progi alertów i kanały (email/Slack/Pager).  
- Matryca dostępu (role → uprawnienia).  
- Changelog i procedura wprowadzania zmian.


## Wymagane streszczenia

- Executive summary: top KPI, główne źródła, SLA dashboardu.  
- Skrót alertów i kanałów.


## Guidance (skrót)

- Definicje KPI utrzymuj w jednym słowniku; unikaj „shadow metrics”.  
- Projektuj czytelnie: 3–5 grup, niewiele kolorów, jasne filtry.  
- Mierz i alertuj na dane, nie na wykresy (quality + latency).  
- Ogranicz dostęp do wrażliwych KPI (PII/finanse).  
- Aktualizuj changelog i komunikuj zmiany użytkownikom.  
- Waliduj wartości z interesariuszami przed publikacją.


## Checklisty Definition of Ready (DoR)

- [ ] Lista KPI i definicji zatwierdzona.  
- [ ] Źródła danych dostępne; odświeżanie możliwe.  
- [ ] Standardy wizualizacji i polityka dostępu uzgodnione.  
- [ ] Narzędzie BI dostępne; role zdefiniowane.  
- [ ] Wymagania alertów i SLA spisane.


## Checklisty Definition of Done (DoD)

- [ ] Dashboard opublikowany; dane poprawne i odświeżają się wg SLA.  
- [ ] Słownik KPI i changelog zaktualizowane.  
- [ ] Alerty działają; brak krytycznych błędów.  
- [ ] Dostępy sprawdzone; audyt/wersjonowanie zapisane.  
- [ ] Feedback zebrany; plan iteracji zapisany.

