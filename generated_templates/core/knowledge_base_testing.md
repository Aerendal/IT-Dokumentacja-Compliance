---
title: Knowledge Base Testing
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Knowledge Base Testing


## Metadane

- Właściciel: QA Lead
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Zakres systemów: [link do KB/portal]


## Cel dokumentu

Zdefiniować strategię i zakres testów bazy wiedzy (portal/FAQ/artykuły), wraz z kryteriami akceptacji, raportowaniem defektów i planem regresji, aby zapewnić aktualność, kompletność i użyteczność treści.


## Zakres i granice

- Zakres: funkcjonalność wyszukiwania i nawigacji, poprawność treści, linki/odnośniki, tagowanie/kategorie, uprawnienia, wydajność (search latency), dostępność (WCAG/A11y), SEO/schematy, lokalizacja, dane strukturalne, monitorowanie jakości i feedback użytkowników.
- Poza zakresem: publikacja nowych artykułów i workflow redakcyjny (opisane w procedurach contentowych), testy UI end‑to‑end specyficzne dla aplikacji niezwiązanych z KB.


## Użytkownicy i interesariusze
- **QA Lead / Test Manager** — planuje strategię testowania i zarządza procesem QA
- **QA Engineer** — projektuje i wykonuje przypadki testowe
- **Development Team** — naprawia defekty i dostarcza testowalny kod
- **Product Owner** — definiuje kryteria akceptacji i priorytetyzuje defekty

## Wejścia i wyjścia
- Wejścia: cele biznesowe, backlog/epiki, wymagania niefunkcjonalne, ograniczenia prawne/techniczne, istniejące systemy/dane.
- Wyjścia: zaakceptowana wersja dokumentu, decyzje architektoniczne/procesowe, action items z właścicielami i terminami.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)

1. Cel i zakres testów (funkcjonalny/A11y/SEO/wydajność/uprawnienia).
2. Założenia, ryzyka i priorytety (np. krytyczne ścieżki: search, artykuł, kontakt).
3. Typy testów i macierz pokrycia (funkcjonalne, A11y, i18n/l10n, SEO, wydajność, bezpieczeństwo podstawowe).
4. Dane testowe i środowiska (zestaw artykułów, tagi, role, indeksy).
5. Scenariusze i automatyzacja (testy ręczne/automaty; kryteria pass/fail).
6. Kryteria akceptacji i go/no‑go (defekty blokujące, SLO search, A11y minimum).
7. Raportowanie defektów i wskaźniki (CVSS/NFR, P1–P4, MTTR, coverage).
8. Plan regresji i utrzymania (kiedy powtarzać, trigger po wydaniu treści/indeksu).


## Szybkie powiązania
- knowledge-base
- knowledge-base-requirements
- knowledge-base-creation
- technical-wiki-knowledge-base
- knowledge-base-structure-design

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

- W sekcji 1–3 określ zakres i pokrycie; w 4–5 przygotuj dane/środowiska i scenariusze/automaty.
- Zdefiniuj kryteria go/no‑go (sekcja 6) i sposób raportowania (sekcja 7).
- Po testach wypełnij wyniki, uzupełnij quick links i checklisty w `reports/checklist_atomic.jsonl`.


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

## Wejścia

- Wymagania funkcjonalne/NFR KB, architektura wyszukiwarki/indeksu, dane testowe (artykuły, tagi, multimedia), wytyczne SEO/Schema, wytyczne A11y (WCAG), definicje ról/uprawnień, metryki jakości treści.


## Wyjścia

- Plan i scenariusze testów (funkcjonalne, niefunkcjonalne, A11y, wydajność, lokalizacja).
- Wyniki i defekty z priorytetami, raport go/no‑go, lista rekomendacji i plan regresji.
- Linki do dashboardów/monitoringu jakości oraz wpisy w `linkage_index.jsonl`.



## Szybkie powiązania (uzupełnij po zlinkowaniu)

- [ ] `linkage_index.jsonl` → `design_struktury_faq.md`, `design_systemu_faq.md`
- [ ] `linkage_index.jsonl` → `logging_strategy.md`, `monitoring_strategy_document.md`
- [ ] `linkage_index.jsonl` → A11y/SEO: `wcag_level_requirements.md`, `aria_patterns_library.md`


## Wymagane rozwinięcia / streszczenia

- Macierz pokrycia: obszar (search/nawigacja/treść/A11y/SEO/wydajność/uprawnienia) → typ testu → narzędzie → właściciel → status.
- Streszczenie wyników: defekty krytyczne, spełnienie SLO (np. search p95), status go/no‑go, plan regresji.


## Wymagane powiązania

- Silnik wyszukiwania/indeksu i konfiguracja, wytyczne A11y/SEO, zestaw danych testowych, dashboardy jakości treści, ticketing do defektów.


## Kryteria DoR (Definition of Ready)

- [ ] Zakres obszarów i krytyczne ścieżki zdefiniowane.
- [ ] Dane testowe (artykuły, tagi, role) przygotowane; środowisko dostępne.
- [ ] Narzędzia do A11y/SEO/wydajności uzgodnione; role/ownerzy testów przypisani.


## Kryteria DoD (Definition of Done)

- [ ] Testy wykonane zgodnie z macierzą; defekty sklasyfikowane i przekazane.
- [ ] Kryteria go/no‑go ocenione; plan regresji zapisany; quick links/status zaktualizowane.
- [ ] Checklisty DoR/DoD odhaczone; metadane aktualne.


## Artefakty do załączenia

- Plan testów, macierz pokrycia, zestaw danych testowych, logi/raporty z narzędzi (A11y/SEO/wydajność), raport końcowy go/no‑go, bilety defektów.


## Walidacja / testy

- Testy funkcjonalne (search, nawigacja, linki, multimedia), A11y (WCAG 2.1 AA), SEO/Schema, wydajność wyszukiwarki (p95), uprawnienia/role, i18n/l10n.
- Retesty po poprawkach; sanity po aktualizacji indeksu/treści.


## Metryki monitorowane

- Coverage testów, liczba defektów P1/P2, MTTR defektów, SLO search (p95), A11y issue rate, broken link rate, feedback CSAT na artykuły.


## Utrzymanie i aktualizacje

- Testy regresji po każdej większej aktualizacji treści lub silnika wyszukiwania; przegląd kwartalny zakresu i metryk; rejestr zmian w `reports/change_log.jsonl`.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, odhacz checklisty, dodaj powiązania w `linkage_index.jsonl` oraz wpis w `reports/checklist_atomic.jsonl`.
