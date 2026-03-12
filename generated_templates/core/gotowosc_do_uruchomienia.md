---
title: Gotowość do uruchomienia
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Gotowość do uruchomienia


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Lista kontrolna, czy system/produkt jest gotowy do startu produkcyjnego.



## Zakres i granice
Obejmuje: [główne obszary i komponenty]. Nie obejmuje: [wyraźnie wykluczone obszary — w tym ich dokumenty].
## Użytkownicy i interesariusze
- QA, PM/Release, Dev, Security/Perf, Product/Business.
## Wejścia i wyjścia

- Wejścia: wymagania projektowe, zakres i cel projektu, zatwierdzone decyzje architektoniczne, polityki organizacyjne, zależności od innych dokumentów.
- Wyjścia: wypełniony dokument gotowy do przeglądu i zatwierdzenia, zaktualizowane wpisy w systemach zarządzania dokumentacją.

## Założenia
- Dostępne są środowiska, dane i narzędzia testowe; zespoły mają czas na runy.
## Otwarte pytania
- Jakie dodatkowe testy wymagane przez regulatorów/klientów?  
- Czy potrzebne testy prod-shadow / canary?
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

- Faza 1: Koncepcja i Wizja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 2: Analiza Wymagań: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 3: Projekt / Design: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 4: Planowanie: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 5: Implementacja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 6: Testowanie / QA: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 7: Bezpieczeństwo / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 8: Wdrożenie / Deployment: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 9: Operacje / Maintenance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)

- Funkcjonalność: AC spełnione, krytyczne bugi=0.
- Testy: unit/integration/e2e/perf/security/UAT zakończone.
- Bezpieczeństwo: sekrety, TLS, access review, compliance.
- Observability: logi/metryki/trace, alerty, runbooki.
- Operacje: backup/DR, capacity, on-call, status page.
- Release: plan deploy/rollback, komunikacja, approvals.
- Wsparcie: KB/FAQ, support readiness, monitoring UX.


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


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

- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.



## Checklisty jakości

- [ ] AC/testy/bezpieczeństwo przejrzane.
- [ ] Observability/runbooki i on-call gotowe.
- [ ] Deploy/rollback/status page zaplanowane.
- [ ] Support/KB i komunikacja przygotowane.

## Definicje robocze

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia
- Release: smoke → regression → perf → security smoke → UAT; decyzja go/conditional/no‑go na podstawie kryteriów.  
- Hotfix: skrócony plan (smoke + targeted regression) z klarownym go/conditional/no‑go.
## Ryzyka i ograniczenia
- Brak gotowości środowisk/danych → poślizgi; niejasne kryteria go/conditional/no‑go → spory; flakiness maskuje defekty.
## Decyzje i uzasadnienia
- Progi istotności/efektu.  
- Zakres testów DQ/sanity vs czas.  
- Kiedy wymagany niezależny reviewer.
## Powiązania z innymi dokumentami
- QA Strategy, Test Data Preparation, Release Plan, Risk Mgmt Plan, Change Mgmt, Security/Perf Testing Plans.
## Powiązania z sekcjami innych dokumentów
- Test Data → dane/środowiska; Release Plan → harmonogram/go-no-go; Risk → priorytety.
## Słownik pojęć w dokumencie
- Go/Conditional/No‑go, Defect leakage, Flakiness, Entry/Exit criteria, Regression, Smoke.
## Wymagane odwołania do standardów
- Polityki QA, bezpieczeństwa i wydajności; wymagania klienta/regulatora jeśli dotyczy.
## Mapa relacji sekcja→sekcja
- Zakres/Ryzyka → Typy testów → Harmonogram → Runy → Raporty → Decyzje → Retro.
## Mapa relacji dokument→dokument
- Testing Plan → QA/Release/Risk → Change/Incident → Lessons Learned.
## Ścieżki informacji
- Wymagania/ryzyka → Plan → Runy → Raporty → Decyzje → Retro → Aktualizacja planu.
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
- Matryca fal/kryteriów, dashboardy, alert configs, feature flag plan, rollout log, komunikaty, waiver log, ADR log.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- QA/PM → Security/Perf (jeśli dotyczy) → Product/Business → Release/CAB.
## Metryki jakości
- Czas rollout, liczba pauz/stopów, MTTR przy rollback, wpływ na KPI/błędy, liczba waiverów i czas sunset.
## Kryteria ukończenia
- [ ] Rollout zamknięty (sukces/stop) z decyzjami i logami; wersja/data/właściciel aktualne.
