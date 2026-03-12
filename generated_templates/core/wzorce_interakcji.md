---
title: Wzorce Interakcji
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Wzorce Interakcji


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Branża / produkt: [np. aplikacja web, kiosk, mobile]
- Kontakt eksperta UX: [osoba/rola/link]


## Cel dokumentu

Katalog i standaryzacja wzorców interakcji UX/UI (nawigacja, formularze, listy, komunikaty, dostępność) wraz z zasadami użycia i przykładami.


## Zakres i granice

- Zakres: interakcje użytkownika z interfejsem (web/mobile/embedded), w tym copy UX, mikroanimacje, wzorce dostępności.
- Poza zakresem: brand design (kolory/typografia), architektura informacji makro, logika domenowa backend.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

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

1. Nawigacja i hierarchie (globalna, lokalna, breadcrumbs, header, menu boczne).
2. Formularze i walidacje (polityka błędów, inline vs po submit, maski, stany edge).
3. Listy / tabele (sort, filtr, paginacja, infinite scroll, puste stany).
4. Komunikaty i feedback (toast/dialog/inline, sukces/błąd/info, loading/skeleton, retry).
5. Dostępność (kontrast, focus, kolejność TAB, ARIA, klawiatura, screen reader).
6. Wzorce dla mobile/touch (gesty, hit area, stan offline, haptics).
7. Przykłady referencyjne i anty‑przykłady.
8. Harmonogram aktualizacji i właścicielstwo.


## Szybkie powiązania
- wzorce-us-ug-obywatelskich
- wzorce-rekrutacyjne
- wzorce-omnichannel
- wzorce-zarzadzania-uprawami
- wzorce-smart-city

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

- Zweryfikuj, czy zakres pokrywa Twój produkt; jeśli nie, dopisz wyjątki w „Zakres i granice”.
- Dla każdej sekcji wypełnij: „kiedy używać”, „jak wygląda”, „warianty”, „anty‑przykłady”, „ograniczenia dostępności”.
- Podlinkuj do komponentów UI i ticketów wdrożeniowych; uaktualnij quick links w tym pliku i w `linkage_index.jsonl`.
- Oznacz spełnienie checklist DoR/DoD (poniżej) w `reports/checklist_atomic.jsonl`.


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

- Brief produktu / persony / journeys.
- Heurystyki i standardy WCAG/ARIA.
- Dane z badań użyteczności lub analityki (heatmapy, drop-off).


## Wyjścia

- Zestaw wzorców z opisem kiedy stosować, przykładami, wariantami i ograniczeniami.
- Mapowanie wzorców do komponentów design systemu / bibliotek UI.
- Lista otwartych pytań i uzupełnień do badań.



## Szybkie powiązania (uzupełnij po zlinkowaniu)

- [ ] Powiązanie z design system: `linkage_index.jsonl` → komponenty (`aria_patterns_library.md`, `component_library_docs.md`).
- [ ] Powiązanie z accessibility: `linkage_index.jsonl` → WCAG/ARIA (`wcag_level_requirements.md`, `accessibility_monitoring_runbook.md`).
- [ ] Powiązanie z analityką zachowań: `linkage_index.jsonl` → metryki (`user_engagement_metrics.md`, `conversion_monitoring.md`).


## Wymagane rozwinięcia / streszczenia

- Dołącz 1–3 zrzuty lub diagramy dla kluczowych wzorców (desktop + mobile).
- Dodaj skróconą tabelę decyzji: wzorzec → stosować gdy → nie stosować gdy → komponent DS.
- Streszczij wyniki ostatniego audytu dostępności (max 5 punktów).


## Wymagane powiązania

- Komponenty DS / biblioteki UI (np. Storybook, Figma).
- Standardy WCAG/ARIA, lokalne polityki dostępności.
- Metryki produktu (CTR, completion rate, time-on-task, error rate).
- Bilety utrzymaniowe dla refaktoryzacji wzorców (linki do narzędzia PM).


## Kryteria DoR (Definition of Ready)

- [ ] Zdefiniowane persony / scenariusze.
- [ ] Wskazane komponenty lub brakujące komponenty DS.
- [ ] Zebrane dane z błędów UX lub badań (jeśli istnieją).
- [ ] Uzgodnione scope/wyłączenia.


## Kryteria DoD (Definition of Done)

- [ ] Każdy wzorzec ma opis „kiedy używać / kiedy nie”, warianty i anty‑przykłady.
- [ ] Dostępność: wymagania klawiatury, screen reader, focus, kontrast, haptics.
- [ ] Linki do komponentów i tickety wdrożeniowe są aktualne.
- [ ] Metryki monitorowane i raportowane (dashboard lub SQL/graf).
- [ ] Plan przeglądu cyklicznego (np. co kwartał) zapisany w sekcji „Harmonogram”.


## Artefakty do załączenia

- Zrzuty ekranów / makiety (desktop, mobile).
- Tabele porównawcze wariantów (np. modal vs sheet vs toast).
- Przykładowe treści mikrocopy (PL/EN).
- Linki do prototypów Figma / Storybook / repo komponentów.


## Walidacja / testy

- Testy dostępności (WCAG 2.1 AA): klawiatura, czytniki ekranu, kontrast.
- Testy heurystyczne (Nielsen, Shneiderman) i szybkie badania 5‑user.
- A/B lub feature flag metrics: konwersja, czas realizacji zadania, błędy formularza.
- QA: regresja UI na głównych viewportach + dark mode (jeśli dotyczy).


## Metryki monitorowane

- Completion rate danego wzorca (np. formularz rejestracji).
- Error rate i abandon rate.
- Czas do pierwszej akcji (TTFA) i time-on-task.
- Liczba zgłoszeń helpdesk dotyczących interakcji.


## Utrzymanie i aktualizacje

- Przegląd kwartalny wzorców (UX + właściciel produktu).
- Sync z design system co wydanie major.
- Rejestr zmian w `reports/change_log.jsonl` (dodaj wpis przy każdej istotnej zmianie).


## Zakończenie

Po spełnieniu DoD zaktualizuj status w sekcji Metadane, odhacz checklisty, uzupełnij quick links i zarejestruj wynik walidacji w `reports/checklist_atomic.jsonl`.
