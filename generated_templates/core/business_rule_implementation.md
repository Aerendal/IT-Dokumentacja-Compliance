---
title: Business Rule Implementation
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Business Rule Implementation


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje, jak implementować i utrzymywać reguły biznesowe: źródła prawdy, modele decyzji, silniki reguł, testy i governance. Minimalizuje rozbieżności między zespołami i ułatwia zmiany/regresje.


## Zakres i granice

- Obejmuje: identyfikację źródeł wymagań, modelowanie reguł (DMN/DSL/kod), silniki (rules engine, feature flags, policy-as-code), dane wejściowe/wyjściowe, wersjonowanie, testy (unit/property/contract), walidacje i monitoring decyzji, bezpieczeństwo/PII, audyt/traceability, rollout/backout.  
- Poza zakresem: definicje polityk biznesowych (BRD) — tu skupiamy się na implementacji i eksploatacji.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: BRD/user stories, modele domenowe, dane wejściowe/źródła, polityki compliance, wzorce decyzji, strategie wersjonowania/deploy, narzędzia rules engine/policy-as-code, profile ruchu.  
- Wyjścia: artefakty reguł (DSL/DMN/kod), kontrakty danych, testy i wyniki, decyzje architektoniczne, plan rollout/backout, monitorowanie skutków, RACI.


## Założenia

- Dostępne repo i CI/CD dla reguł.  
- Monitoring/observability wspiera logi decyzji.  
- Zespół ma kompetencje w modelowaniu decyzji.


## Otwarte pytania

- Czy potrzebne są wyjaśnienia (XAI) dla decyzji?  
- Jakie są wymagania regulatora dla danej domeny?  
- Czy reguły muszą być lokalizowane/parametryzowane per rynek?


## Powiązania (meta)

- Key Documents: decision_model, data_contract_standard, testing_strategy, observability_plan, change_management_request, rollback_plan.  
- Key Document Structures: modele decyzji, reguły, dane, testy, wersjonowanie, monitoring, governance.  
- Document Dependencies: źródła danych, rules engine/feature flags, CI/CD, logging/tracing, audit store.


## Zależności dokumentu

Wymaga: zatwierdzonych reguł biznesowych (lub ich modelu), zdefiniowanych danych wejściowych/wyjściowych i kontraktów, narzędzia wykonawczego (engine/DSL), wymagań audytu/traceability, strategii rollout/backout. Braki = DoR otwarte.


## Fazy cyklu życia

- Modelowanie i implementacja.  
- Testy i weryfikacja.  
- Rollout i monitoring wpływu.  
- Utrzymanie, wersjonowanie, deprecjacje.



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

- linkage_index.jsonl (business/rule/implementation)  
- decision_model, data_contract_standard, testing_strategy, observability_plan, change_management_request


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

1. Zamodeluj reguły i dane; ustal engine/DSL i kontrakty.  
2. Przygotuj testy i monitoring; skonfiguruj rollout/backout.  
3. Publikuj zmiany z wersjonowaniem i audytem; aktualizuj DoR/DoD i linkage_index.


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

- DMN: standard modelowania decyzji/reguł.  
- Policy-as-code: reguły w kodzie z automatycznym egzekwowaniem.  
- Traceability: możliwość odtworzenia, która reguła i wersja podjęła decyzję.


## Przykłady użycia

- Wdrożenie reguł scoringu ryzyka kredytowego.  
- Reguły cenowe/promocyjne w e‑commerce.  
- Polityki uprawnień w systemie dostępu (ABAC/RBAC) jako policy-as-code.


## Ryzyka i ograniczenia

- Rozbieżne źródła reguł → niespójność decyzji.  
- Brak audytu/traceability → trudne RCA i compliance.  
- Bias w danych → niesprawiedliwe decyzje.


## Decyzje i uzasadnienia

- Wybór engine/DSL vs kod własny.  
- Poziom logowania i retencji dla reguł z PII.  
- Strategia rollout (flags vs wersje) i testy A/B.


## Powiązania z innymi dokumentami

- decision_model — źródło logiki.  
- testing_strategy — pokrycie testowe.  
- rollback_plan — cofnięcie wersji reguł.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Regulacje branżowe (fin/health), RODO/PII, polityki audytu.  
- Wewnętrzne standardy jakości kodu i policy-as-code.

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

- Dane i kontrakty → Reguły → Testy → Monitoring.  
- Wersjonowanie → Rollout/backout → Audyt/traceability.  
- Bezpieczeństwo/PII → Dane → Logi/audyt.


## Struktura sekcji

1) Kontekst i cele reguł (wartość, KPI)  
2) Model decyzji i zakres (DMN/diagram, domain model)  
3) Dane wejściowe/wyjściowe i kontrakty (typy, walidacje, PII)  
4) Implementacja reguł (engine/DSL/kod, zasady kodowania)  
5) Wersjonowanie i deployment (branching, feature flags, migracje)  
6) Testy i walidacja (unit/property/contract/A-B, dane testowe)  
7) Monitoring i audyt (metryki skutków, logi decyzji, explainability)  
8) Bezpieczeństwo i zgodność (dostępy, PII, audyt)  
9) Rollout/backout i utrzymanie (runbook, deprecjacje)  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Tabela reguł z wersjami i właścicielami; źródła danych i walidacje.  
- Strategia testów (szczególnie property-based i kontraktowe) oraz dane testowe.  
- Plan rollout/backout z kontrolą zgodności danych i traceability.


## Wymagane streszczenia

- Snapshot decyzji: kluczowe reguły, wersje, wpływ na KPI, ryzyka.  
- Krótki „change note” przy każdej nowej wersji.


## Guidance (skrót)

- Jedno źródło prawdy dla reguł; unikaj duplikacji w kodzie.  
- Reguły traktuj jak kod: wersjonuj, testuj, review, monitoruj.  
- Loguj decyzje i dane wejściowe (z maskowaniem PII) dla audytu/RCA.  
- Oddziel definicję reguł od implementacji UI/API; wspieraj rollout flagami.  
- Regularnie weryfikuj wpływ reguł na KPI i bias.


## Checklisty Definition of Ready (DoR)

- [ ] Model decyzji/reguł i dane wejściowe/wyjściowe opisane.  
- [ ] Engine/DSL wybrany; zasady wersjonowania ustalone.  
- [ ] Dane testowe i strategia testów przygotowane.  
- [ ] Wymagania audytu/PII/traceability zidentyfikowane.  
- [ ] Plan rollout/backout uzgodniony.


## Checklisty Definition of Done (DoD)

- [ ] Reguły zaimplementowane i zreviewowane; testy przeszły.  
- [ ] Logi/audyt/monitoring decyzji aktywne; status/wersja/data uzupełnione.  
- [ ] Rollout/backout przetestowany; deprecjacje opisane.  
- [ ] Kontrakty danych i linkage_index zaktualizowane.  
- [ ] Wpływ na KPI/bias oceniony lub zaplanowany do pomiaru.

