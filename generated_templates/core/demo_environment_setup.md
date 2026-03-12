---
title: Demo Environment Setup
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Demo Environment Setup


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przygotować powtarzalne środowisko demo/pre‑sales z danymi i scenariuszami pokazującymi kluczowe wartości produktu, przy minimalnym ryzyku bezpieczeństwa i łatwym odświeżaniu.


## Zakres i granice

- Obejmuje: top scenariusze demo, dane syntetyczne/anonymizowane, provisioning środowiska (IaaS/PaaS/SaaS), konfiguracje i feature flags, konta/demo users, integracje mock/stub, reset/odświeżanie, bezpieczeństwo (brak PII/sekretów), monitoring, instrukcje dla prezenterów.  
- Poza zakresem: pełne środowiska produkcyjne, realne dane klientów.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: lista scenariuszy sprzedażowych, wymagania funkcjonalne, dane demo, budżet kosztowy, szablony infra, listy kont i ról, ograniczenia bezpieczeństwa.  
- Wyjścia: gotowe środowisko demo, playbook uruchomienia i resetu, checklisty DoR/DoD, obrazy/backupy baz, instrukcje dla prezenterów i FAQ.


## Założenia

- Dostępne są narzędzia IaC i monitoring.  
- Dane syntetyczne pokrywają kluczowe przypadki.  
- Prezenterzy mają dostęp i instrukcje.


## Otwarte pytania

- Czy potrzebne są warianty językowe/regionalne demo?  
- Jak obsłużyć demo w trybie offline?  
- Jak długo trzymać logi demo i koszty referencyjne?

## Powiązania (meta)

- Key Documents: security_controls_reference, data_protection_compliance, rollback_runbook, test_data_strategy, feature_flags_policy, monitoring_strategy_document.  
- Key Document Structures: scenariusze, dane, provisioning, bezpieczeństwo, reset, instrukcje.  
- Document Dependencies: IaC/CI-CD, secrets manager, logging/monitoring, mock services, CDN/assets.


## Zależności dokumentu

Wymaga: zatwierdzonych scenariuszy demo, danych syntetycznych/anonymizowanych, szablonów infra/IaC, kont/feature flags, polityk bezpieczeństwa danych, budżetu kosztowego. Brak = brak DoR.


## Fazy cyklu życia

- Definicja scenariuszy i danych.  
- Provisioning i konfiguracja.  
- Walidacja demo (run-through).  
- Utrzymanie/resety i monitoring.  
- Aktualizacje pod nowe featury.



## Struktura sekcji (szkielet)
- Cel i definicja sukcesu (KPI)
- Zakres, założenia i ograniczenia
- Interesariusze i role/RACI
- Kamienie milowe i daty
- Plan fal/sprintów z deliverables
- Zależności i ryzyka oraz plan mitigacji
- Budżet/zasoby i obłożenie
- Plan komunikacji i raportowania
- Kryteria akceptacji/go-live i plan rewizji
## Szybkie powiązania

- linkage_index.jsonl (demo/environment/setup)  
- test_data_strategy, feature_flags_policy, rollback_runbook


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

1. Wybierz scenariusze i dane; uruchom provisioning IaC.  
2. Skonfiguruj feature flags, konta i mocki; wykonaj run-through.  
3. Użyj środowiska na demo; po wydarzeniu wykonaj reset/destroy.  
4. Zbieraj feedback, aktualizuj dokument i linkage_index.


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

- Demo run-through: pełne przejście scenariuszy przed prezentacją.  
- IaC: Infrastructure as Code.  
- Mock service: zastępczy serwis do demonstrowania integracji.


## Przykłady użycia

- Demo SaaS z włączonymi premium feature’ami na feature flags.  
- Prezentacja integracji API z mockowanym ERP.  
- Showcase analityki na syntetycznym zestawie danych klientów.


## Ryzyka i ograniczenia

- Ujawnienie sekretów/PII → incydent bezpieczeństwa.  
- Niespójne dane demo → słaba prezentacja.  
- Brak resetu → dryf stanu i koszty.  
- Zależność od łączy/serwisów zewnętrznych → awaria w trakcie demo.


## Decyzje i uzasadnienia

- Zakres scenariuszy vs koszt utrzymania.  
- Stopień realizmu danych vs bezpieczeństwo.  
- Częstotliwość odświeżania/niszczenia.  
- Zakres monitoringu i budżet alarmów.


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

- Scenariusze ↔ Dane ↔ Feature flags.  
- Provisioning ↔ Bezpieczeństwo ↔ Monitoring.  
- Reset/odświeżanie ↔ Koszt ↔ Dostępność.


## Struktura sekcji

1) Scenariusze demo i value props  
2) Dane demo (synthetic/anonymized) i generatory  
3) Provisioning (IaC, obrazy, konfiguracje, feature flags)  
4) Bezpieczeństwo i sekretów brak/rotacja  
5) Walidacja i checklisty run-through  
6) Reset/odświeżanie, backupy/obrazy  
7) Monitoring/koszt i odpowiedzialności  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Playbook provisioning (komendy/IaC) i czas tworzenia.  
- Lista kont/ ról demo + automaty resetu haseł.  
- Generatory danych demo i sposób anonimizacji.  
- Checklista run-through przed prezentacją.  
- Plan kosztów i harmonogram odświeżeń.  
- Procedura wyłączania i niszczenia środowiska.


## Wymagane streszczenia

- Executive summary: co pokazujemy, dostępność, koszt.  
- Skrót bezpieczeństwa: brak PII, sekretów, rotacja haseł.


## Guidance (skrót)

- Używaj w pełni syntetycznych danych; nigdy PII.  
- Automatyzuj provisioning i reset; trzymaj obrazy gotowe.  
- Włącz feature flags pod scenariusze; izoluj od prod.  
- Monitoruj koszt i wygaszaj nieużywane środowiska.  
- Testuj demo przed każdym użyciem; miej plan awaryjny.  
- Aktualizuj linkage_index po zmianach scenariuszy.


## Checklisty Definition of Ready (DoR)

- [ ] Scenariusze i dane demo zatwierdzone.  
- [ ] IaC/szablony gotowe; konta/feature flags przygotowane.  
- [ ] Polityki bezpieczeństwa (brak PII/sekretów) potwierdzone.  
- [ ] Budżet kosztowy i monitoring ustawione.  
- [ ] Plan reset/destroy opisany.


## Checklisty Definition of Done (DoD)

- [ ] Środowisko utworzone i zweryfikowane (run-through OK).  
- [ ] Brak PII/sekretów; logi i monitoring działają.  
- [ ] Reset/destroy wykonane po demo (jeśli wymagane).  
- [ ] Dokumentacja i linkage_index zaktualizowane; koszty w normie.  
- [ ] Feedback/prezentacja odnotowane; otwarte zadania zapisane.

