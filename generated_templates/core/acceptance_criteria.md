---
title: Acceptance Criteria
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Acceptance Criteria


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Ustala jednoznaczne kryteria akceptacji dla user story/feature/zmiany: kiedy uznajemy pracę za ukończoną, zgodną z wymaganiami, bezpieczną i gotową do release. Redukuje ryzyko niedomówień i zwrotów.


## Zakres i granice

- Obejmuje: kryteria funkcjonalne, niefunkcjonalne (wydajność, bezpieczeństwo, dostępność), dane/testy, UX/A11y, zgodność prawna, monitoring/telemetria, regresję/feature flags, kryteria rollout/backout, dowody (testy, logi, screeny).  
- Poza zakresem: pełny plan testów (osobny dokument), decyzje biznesowe o priorytecie backlogu.


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: user story/BRD, definicje Done, wymagania NFR, makiety/UX, dane testowe, polityki bezpieczeństwa/privacy, standardy A11y, dependency list, risk assessment.  
- Wyjścia: lista kryteriów akceptacji, dane testowe i dowody, status spełnienia (checklisty), decyzja go/no‑go dla release, aktualizacja JIRA/ALM i DoD.


## Założenia

- Dostępne środowiska i dane testowe.  
- CI/CD uruchamia testy i zbiera logi/metryki.  
- Zespół ma standard DoR/DoD dla user story.


## Otwarte pytania

- Czy wymagane są dodatkowe testy zgodności (regulatory)?  
- Jakie są minimalne progi dla A11y/bezpieczeństwa?  
- Kto akceptuje wyjątki od NFR?


## Powiązania (meta)

- Key Documents: qa_strategy_document, testing_vision_statement, non_functional_requirements, security_requirements, accessibility_compliance, release_checklist.  
- Key Document Structures: kryteria funkcjonalne, NFR, dane/testy, bezpieczeństwo/A11y, rollout/backout, dowody.  
- Document Dependencies: system testów (CI/CD), dane testowe, feature flags, monitoring/logi, ticketing.


## Zależności dokumentu

Wymaga: kompletnego opisu user story/feature, zdefiniowanych NFR, dostępnych danych testowych lub sposobu ich pozyskania, ustalonego środowiska i narzędzi testowych, uzgodnionych wymagań bezpieczeństwa/A11y. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja kryteriów (refinement).  
- Weryfikacja w trakcie implementacji/testów.  
- Akceptacja przed release; ewentualny backout/roll-forward.  
- Retrospektywa i aktualizacja wzorców kryteriów.



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

- linkage_index.jsonl (acceptance/criteria)  
- qa_strategy_document, testing_vision_statement, non_functional_requirements, release_checklist, security_requirements


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

1. Zdefiniuj kryteria (funkcjonalne + NFR) wraz z danymi i dowodami.  
2. W trakcie testów odhaczaj spełnienie; zbieraj dowody.  
3. Przed release wypełnij snapshot, podejmij decyzję go/no‑go, zaktualizuj DoD.


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

- Acceptance Criteria: warunki uznania user story/feature za ukończone.  
- Backout: procedura powrotu do poprzedniej wersji, gdy kryteria nie są spełnione po deployu.  
- Evidence: obiektywny dowód spełnienia (testy, logi, metryki).


## Przykłady użycia

- Feature płatności: kryteria funkcjonalne + PCI + latency + A11y checkout.  
- API: kryteria kontraktowe (schema), error handling, rate limiting, observability.  
- Mobile: kryteria UX/A11y, wydajność na niskiej klasy urządzeniach.


## Ryzyka i ograniczenia

- Niejasne kryteria → zwroty i opóźnienia.  
- Brak danych testowych → fałszywe akceptacje.  
- Pominięte NFR → regresje wydajności/bezpieczeństwa/A11y.


## Decyzje i uzasadnienia

- Format kryteriów (Given/When/Then vs checklista) zależnie od zespołu.  
- Poziom dowodów wymagany dla produkcji vs testów wewnętrznych.  
- Warunki backout i czas obserwacji po deployu.


## Powiązania z innymi dokumentami

- non_functional_requirements — progi i wskaźniki.  
- release_checklist — kroki i dowody.  
- security_requirements — kontrole security.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- WCAG/EN/ADA (A11y), polityki bezpieczeństwa i prywatności.  
- Wewnętrzne standardy jakości i testów.

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

- Kryteria funkcjonalne + NFR → Testy/Dowody → Decyzja go/no‑go.  
- Dane testowe → Wyniki testów → Akceptacja.  
- Rollout/Backout → Monitoring → Stabilizacja.


## Struktura sekcji

1) Kontekst i zakres user story/feature  
2) Kryteria funkcjonalne (given/when/then, edge cases)  
3) Kryteria niefunkcjonalne (wydajność, bezpieczeństwo, A11y, UX, dane)  
4) Dane i środowiska testowe (źródła, maskowanie, seed)  
5) Dowody i metryki (testy auto/manual, logi, screeny, metryki SLI)  
6) Rollout/feature flags i warunki backout  
7) Otwarte ryzyka/pytania, decyzja go/no‑go


## Wymagane rozwinięcia

- Lista kryteriów w formie Gherkin lub checklist.  
- Progi NFR (np. p95<300 ms, WCAG 2.1 AA, brak high/critical security issues).  
- Plan danych testowych (maskowanie, generowanie) i metody weryfikacji.


## Wymagane streszczenia

- Jednostronicowy snapshot do akceptacji: spełnione/niespełnione, ryzyka, zalecenie go/no‑go.  
- Krótka lista krytycznych edge cases.


## Guidance (skrót)

- Kryteria pisz z perspektywy użytkownika, ale sprawdzaj pokrycie NFR.  
- Wymagaj dowodów: link do testów, zrzuty, logi, metryki.  
- Ustal jasne progi go/no‑go i warunki backout.  
- Dopasuj dane testowe do scenariuszy krytycznych i ryzyk.  
- Synchronizuj z DoR/DoD i ticketami w ALM.


## Checklisty Definition of Ready (DoR)

- [ ] User story/feature opisane; scope i zależności znane.  
- [ ] NFR i wymagania bezpieczeństwa/A11y zdefiniowane.  
- [ ] Dane testowe zidentyfikowane, sposób pozyskania uzgodniony.  
- [ ] Środowiska i narzędzia testowe dostępne.  
- [ ] Zdefiniowane warunki backout/rollout (feature flags).


## Checklisty Definition of Done (DoD)

- [ ] Wszystkie kryteria odhaczone; dowody dołączone.  
- [ ] NFR spełnione lub wyjątki zaakceptowane.  
- [ ] Rollout/backout i monitoring zaplanowane; status/wersja/data uzupełnione.  
- [ ] Ticket/ALM zaktualizowany, linkage_index uzupełniony.  
- [ ] Lessons learned/edge cases dopisane do repo wiedzy.

