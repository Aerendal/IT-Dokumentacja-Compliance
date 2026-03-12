---
title: Delivery Performance Review
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Delivery Performance Review


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Ocenić realizację dostarczania projektów/usług: tempo, jakość, koszty, ryzyka i satysfakcję interesariuszy, aby wprowadzać usprawnienia i decyzje o priorytetach.


## Zakres i granice

- Obejmuje: przegląd KPI (delivery velocity, predictability, scope change, quality/defect rate, SLA), status kamieni milowych, ryzyka i problemy, budżet i zużycie, satysfakcję interesariuszy, działania korygujące i decyzje.  
- Poza zakresem: szczegółowe retrospektywy zespołów (osobne spotkania), plan produktu długoterminowy.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: roadmapa/kamienie, status zadań (Jira itp.), KPI, budżet vs plan, ryzyka/issues, feedback klientów/użytkowników, SLA raporty.  
- Wyjścia: raport przeglądu, decyzje i akcje, zaktualizowany plan/roadmapa, checklisty DoR/DoD, aktualizacja ryzyk i KPI.


## Założenia

- Dostępne są wiarygodne dane z narzędzi.  
- Interesariusze uczestniczą i akceptują decyzje.  
- Istnieje kanał publikacji raportów.


## Otwarte pytania

- Jak mierzyć wpływ zmian zakresu na KPI?  
- Jaka minimalna częstotliwość przeglądów?  
- Jak długo przechowywać raporty przeglądów?

## Powiązania (meta)

- Key Documents: project_execution_plan, risk_assessment, change_management, quality_assurance_plan, program_management_requirements, release_readiness_statement.  
- Key Document Structures: KPI, kamienie, ryzyka, decyzje, akcje, komunikacja.  
- Document Dependencies: PM tool, finance/budget system, SLA/monitoring, risk/issues log.


## Zależności dokumentu

Wymaga: aktualnych KPI i statusu kamieni, danych budżetowych, listy ryzyk/issues, feedbacku interesariuszy, narzędzi raportowych. Brak = brak DoR.


## Fazy cyklu życia

- Przygotowanie danych i agendy.  
- Przegląd/spotkanie i decyzje.  
- Publikacja raportu i akcji.  
- Follow-up i monitorowanie.  
- Iteracyjne ulepszenia.



## Struktura sekcji (szkielet)
- Zakres modeli i wersji objętych przeglądem.
- Metryki jakości i stabilności vs baseline/SLO.
- Drift danych i konceptu; feature health.
- Bias/fairness i compliance (AI Act/RODO, dane wrażliwe).
- Bezpieczeństwo (adversarial, model stealing/leakage).
- Koszty i wydajność (latency, throughput, koszt inferencji, zużycie GPU/CPU/RAM).
- Incydenty/alerty i ich status.
- Decyzje i plan działań (retrain, tuning, thresholds, rollback, eksperymenty).
- Ryzyka i akceptacje/waivery.
## Szybkie powiązania

- linkage_index.jsonl (delivery/performance/review)  
- program_management_requirements, risk_assessment


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

1. Zbierz KPI/statusy i przygotuj agendę.  
2. Poprowadź przegląd, zanotuj decyzje/akcje.  
3. Opublikuj raport; śledź realizację akcji.  
4. Aktualizuj dokument/linkage_index; powtarzaj cyklicznie.


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

- Predictability: stosunek zaplanowanego do zrealizowanego w sprincie/iteracji.  
- RAG: status Red/Amber/Green.  
- Scope creep: niekontrolowany wzrost zakresu.


## Przykłady użycia

- Przegląd kwartalny programu transformacji IT.  
- Ocena delivery feature setu przed releasem.  
- Raport dla zarządu o stanie projektu strategicznego.


## Ryzyka i ograniczenia

- Nieaktualne dane → złe decyzje.  
- Brak follow-up → powtarzające się problemy.  
- Zbyt szczegółowe KPI → rozmycie priorytetów.  
- Brak transparentności budżetu → zaskoczenia finansowe.


## Decyzje i uzasadnienia

- Zakres KPI i kadencja przeglądu.  
- Kryteria RAG i eskalacje.  
- Priorytety akcji i alokacja zasobów.  
- Aktualizacja roadmapy/scope po przeglądzie.


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

- KPI ↔ Kamienie ↔ Decyzje.  
- Ryzyka/issues ↔ Akcje ↔ Follow-up.  
- Budżet ↔ Zakres ↔ Priorytety.


## Struktura sekcji

1) KPI i trend (velocity, predictability, quality, SLA)  
2) Status kamieni i zakresu (zmiany, scope creep)  
3) Budżet vs plan, zasoby  
4) Ryzyka/issues i działania korygujące  
5) Feedback interesariuszy i satysfakcja  
6) Decyzje, akcje, właściciele, terminy  
7) DoR/DoD, pytania, kolejne spotkanie


## Wymagane rozwinięcia

- Tabela KPI z targetami i trendami.  
- Lista kamieni z datami i wskaźnikiem on-track/at-risk.  
- Log ryzyk/issues z priorytetami i planem.  
- Template raportu i komunikacji.  
- Plan follow-up i SLA na akcje.  
- Dashboard referencyjny.


## Wymagane streszczenia

- Executive summary: status (RAG), top ryzyka, kluczowe decyzje.  
- Skrót budżet vs plan.


## Guidance (skrót)

- Skup się na decyzjach i akcjach, nie na samych statusach.  
- Miej jeden dashboard danych; unikaj dyskusji o źródłach.  
- Eskaluj ryzyka wcześnie; przypisz właścicieli i terminy.  
- Rewiduj KPI przy zmianach zakresu.  
- Dokumentuj decyzje; aktualizuj linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] KPI i status kamieni aktualne.  
- [ ] Budżet vs plan przygotowany.  
- [ ] Lista ryzyk/issues zaktualizowana.  
- [ ] Feedback interesariuszy zebrany.  
- [ ] Agenda i uczestnicy potwierdzeni.


## Checklisty Definition of Done (DoD)

- [ ] Raport opublikowany; decyzje/akcje przypisane.  
- [ ] KPI/ryzyka uaktualnione; linkage_index zaktualizowany.  
- [ ] Follow-up zaplanowany; terminy ustawione.  
- [ ] Brak otwartych krytycznych pytań z przeglądu.  
- [ ] Dokumentacja dostępna w repo.

