---
title: Program Management Requirements
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Program Management Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zdefiniować wymagania i standardy dla zarządzania programami (zestaw powiązanych projektów), aby zapewnić spójne planowanie, governance, ryzyka, raportowanie i osiąganie celów biznesowych.


## Zakres i granice

- Obejmuje: cele programu i KPI, strukturę governance (steering, RACI), plan i harmonogram, zarządzanie zakresem/benefitami, budżet/koszty, ryzyka i zależności między projektami, standardy raportowania, narzędzia i procesy decyzyjne, zmiany/program change control.  
- Poza zakresem: szczegółowe plany pojedynczych projektów (oddzielne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: business case, backlog/roadmap, budżet, lista projektów, interesariusze, polityki organizacji, ryzyka strategiczne, zasoby.  
- Wyjścia: karta programu, governance i RACI, harmonogram high-level, matryca zależności, plan benefitów, standard raportów, DoR/DoD, decyzje i tolerancje.


## Założenia

- Dostępne są dane finansowe i statusy projektów.  
- Sponsoring i governance mają mandat decyzyjny.  
- Zespoły akceptują wspólne standardy raportowania.


## Otwarte pytania

- Jak mierzyć realizację benefitów w czasie?  
- Jak mapować zależności na plan capacity?  
- Czy potrzebne jest narzędzie PPM dedykowane?

## Powiązania (meta)

- Key Documents: project_execution_plan, risk_assessment, change_management, delivery_performance_review, business_objectives_document, communication_plan.  
- Key Document Structures: cele/KPI, governance, plan, zależności, ryzyka, raporty.  
- Document Dependencies: PMO narzędzia, budżet/finance, CMDB usług, portfolio kanban.


## Zależności dokumentu

Wymaga: zatwierdzonego business case, listy projektów i sponsorów, polityk governance, budżetu i KPI, narzędzi raportowania. Brak = brak DoR.


## Fazy cyklu życia

- Inicjacja programu.  
- Planowanie i ustanowienie governance.  
- Realizacja i monitorowanie.  
- Kontrola zmian i benefitów.  
- Zamknięcie i ewaluacja.



## Struktura sekcji (szkielet)
- Cel i kontekst biznesowy
- Interesariusze, persony i scenariusze
- Wymagania funkcjonalne (priorytety, reguły, wyjątki)
- Wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo, zgodność)
- Dane i integracje
- Kryteria akceptacji i miary sukcesu
- Zależności, ryzyka i założenia
- Śledzenie (traceability) do epik/testów
## Szybkie powiązania

- linkage_index.jsonl (program/management/requirements)  
- delivery_performance_review, change_management


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

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

1. Utwórz kartę programu, cele/KPI i RACI.  
2. Zbuduj plan i matrycę zależności; uzgodnij budżet.  
3. Ustal raporty, tolerancje i change control.  
4. Monitoruj, raportuj, eskaluj; aktualizuj dokument/linkage_index.


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

- Tolerancja: zakres odchyleń bez eskalacji.  
- Benefit realization: osiągnięcie zdefiniowanej wartości biznesowej.  
- RAG: Red/Amber/Green status.


## Przykłady użycia

- Program migracji do chmury.  
- Program modernizacji platformy omnichannel.  
- Program zgodności regulacyjnej.


## Ryzyka i ograniczenia

- Brak jasnych tolerancji → opóźnione eskalacje.  
- Niespójne raporty → dezinformacja.  
- Zależności między projektami → opóźnienia, jeśli niezarządzane.  
- Benefity nieprzypisane → brak realizacji wartości.


## Decyzje i uzasadnienia

- Kadencja raportów i przeglądów.  
- Zakres tolerancji czasu/kosztu/zakresu.  
- Priorytety projektów w programie.  
- Narzędzia raportowania i governance.


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

- Cele/KPI ↔ Plan ↔ Raporty.  
- Governance ↔ Zmiany ↔ Eskalacje.  
- Zależności ↔ Ryzyka ↔ Decyzje.


## Struktura sekcji

1) Cele, KPI i scope programu  
2) Governance, role, RACI i tolerancje  
3) Plan high-level i harmonogram, zależności między projektami  
4) Budżet i zarządzanie benefitami  
5) Ryzyka i zmiany (program change control)  
6) Raportowanie i komunikacja  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Karta programu i KPI (baseline/target).  
- RACI i komitety (steering, architektura, ryzyko).  
- Matryca zależności i tolerancje (czas/koszt/zakres).  
- Szablon raportu programu (RAG, finanse, ryzyka).  
- Proces change control i escalation.  
- Plan benefit realization i mierniki.


## Wymagane streszczenia

- Executive summary: cele, status RAG, główne ryzyka.  
- Skrót zależności i budżetu.


## Guidance (skrót)

- Ustal jasne tolerancje i ścieżki eskalacji.  
- Mapuj zależności wcześnie; aktualizuj przy każdej zmianie.  
- Standardyzuj raporty; jedno źródło prawdy.  
- Zarządzaj benefitami jak wymaganiami – z właścicielami i KPI.  
- Eskaluj ryzyka ponad tolerancje szybko.  
- Aktualizuj linkage_index po przeglądach.


## Checklisty Definition of Ready (DoR)

- [ ] Business case i sponsor potwierdzeni.  
- [ ] Cele/KPI i scope zdefiniowane.  
- [ ] RACI i governance uzgodnione.  
- [ ] Budżet wstępny i narzędzia raportowe dostępne.  
- [ ] Lista projektów i zależności znana.


## Checklisty Definition of Done (DoD)

- [ ] Raporty i governance działają; RAG aktualne.  
- [ ] Tolerancje i eskalacje przestrzegane.  
- [ ] Benefity zmapowane i monitorowane.  
- [ ] linkage_index zaktualizowany.  
- [ ] Lessons learned i plan następnych przeglądów zapisany.

