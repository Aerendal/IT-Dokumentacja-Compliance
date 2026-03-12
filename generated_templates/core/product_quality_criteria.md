---
title: Product Quality Criteria
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Product Quality Criteria


## Metadane

- Właściciel: Product Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Zdefiniować mierzalne kryteria jakości produktu (funkcjonalne i niefunkcjonalne), aby kierować developmentem, testami i decyzjami go/no-go.


## Zakres i granice

- Obejmuje: kryteria funkcjonalne, użyteczność/UX, wydajność, niezawodność/dostępność, bezpieczeństwo/prywatność, zgodność/regulacje, dostępność (a11y), lokalizacja, obsługę błędów, analitykę i telemetry, maintainability/observability, dokumentację.
- Poza zakresem: szczegółowe test cases (osobne), roadmapa funkcji.


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: wymagania biznesowe, SLO/SLA, regulacje, standardy org (security/a11y), dane z badań UX, metryki prod.
- Wyjścia: lista kryteriów z metrykami/progami, mapping do wymagań/us stories, powiązanie z SLO i testami, szablon oceny release, checklisty QA.


## Założenia
- Dostępne środowiska i dane testowe.  
- CI/CD uruchamia testy i zbiera logi/metryki.  
- Zespół ma standard DoR/DoD dla user story.
## Otwarte pytania
- Czy wymagane są dodatkowe testy zgodności (regulatory)?  
- Jakie są minimalne progi dla A11y/bezpieczeństwa?  
- Kto akceptuje wyjątki od NFR?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: SLO/SLA, standardy security/a11y/privacy, wymagania regulacyjne, dane UX/telemetry, backlog/test plan; brak – odnotuj.


## Fazy cyklu życia

Definicja → Review → Aktualizacje per release → Ewaluacja.



## Struktura sekcji (szkielet)

- Kategorie jakości i ich kryteria.
- Metryki/progi i sposób pomiaru.
- Mapowanie do wymagań/us stories i testów.
- Ocena release (go/conditional/no-go) i raport.
- Utrzymanie i rewizje kryteriów.
- Ryzyka i mitigacje.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum

### Polskie normy i regulacje
- **PN-EN-ISO-9001** — PN-EN ISO 9001:2015-10 — Systemy Zarządzania Jakością
- **PN-EN-ISO-IEC-20000-1** — PN-EN ISO/IEC 20000-1:2019 — Zarządzanie Usługami IT
- **PN-ISO/IEC-27001** — PN-ISO/IEC 27001:2023-09 — Systemy Zarządzania Bezpieczeństwem Informacji

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

- Zdefiniuj kryteria/metryki; zmapuj na wymagania/testy; używaj w review release; aktualizuj na podstawie danych prod.


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

Kryteria → metryki/testy; SLO → wydajność/dostępność; bezpieczeństwo → prywatność; UX → a11y.


## Wymagane rozwinięcia

- Tabele kryteriów z progami i SLI.
- Szablon oceny release.


## Wymagane streszczenia

- One-pager: top kryteria i progi + link do testów/SLO.


## Guidance

Cel: wspólny język jakości. DoR: SLO, standardy, wymagania, dane UX. DoD: kryteria/metyki/mapowanie/testy/ocena; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] SLO/SLA; [ ] Standardy security/a11y/privacy; [ ] Wymagania/regulacje; [ ] Dane UX/telemetry.
- DoD: [ ] Kryteria/metryki/mapowanie/ocena opisane; [ ] Sekcje N/A uzasadnione; metadane aktualne.
