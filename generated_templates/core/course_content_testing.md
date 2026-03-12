---
title: Course Content Testing
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Course Content Testing


## Metadane

- Właściciel: QA Lead
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnić, że treści kursów (e‑learning/instrukcje) działają poprawnie, są zgodne z celami dydaktycznymi i dostępnościowymi, zanim trafią do uczestników.


## Zakres i granice

- Obejmuje: weryfikację treści merytorycznej, SCORM/xAPI pakiety, multimedia (audio/wideo/quizy), ścieżki nawigacji, dostępność (WCAG), kompatybilność urządzeń/przeglądarek, dane śledzenia (LMS/LRS), testy lokalizacji, regresję po aktualizacjach.  
- Poza zakresem: projekt dydaktyczny (osobny dokument), polityka HR szkoleniowa.


## Użytkownicy i interesariusze
- **QA Lead / Test Manager** — planuje strategię testowania i zarządza procesem QA
- **QA Engineer** — projektuje i wykonuje przypadki testowe
- **Development Team** — naprawia defekty i dostarcza testowalny kod
- **Product Owner** — definiuje kryteria akceptacji i priorytetyzuje defekty

## Wejścia i wyjścia

- Wejścia: pakiet kursu (SCORM/xAPI/HTML), scenariusze edukacyjne, checklisty QA, wymagania dostępności, lista urządzeń/przeglądarek, języki lokalizacji, dane testowe w LMS.  
- Wyjścia: raport testów z defektami, checklisty DoR/DoD, lista urządzeń/przeglądarek zaliczonych, wyniki quizów testowych, rekomendacje poprawek.


## Założenia

- LMS/LRS wspiera SCORM/xAPI.  
- Zespół ma dostęp do device lab/testów a11y.  
- Polityki dostępności firmy obowiązują.


## Otwarte pytania

- Jak długo przechowywać dane testowe w LMS?  
- Czy potrzebne są nagrania w wielu językach?  
- Jak raportować skuteczność szkolenia po publikacji?

## Powiązania (meta)

- Key Documents: ui_test_strategy, accessibility_improvement_plan, documentation_roadmap, localization_guidelines, error_handling_standards.  
- Key Document Structures: treść, multimedia, nawigacja, dostępność, śledzenie, lokalizacja.  
- Document Dependencies: LMS/LRS, SCORM/xAPI validator, narzędzia dostępności, device lab, analytics.


## Zależności dokumentu

Wymaga: pakietu kursu, checklist QA i dostępności, środowiska LMS/LRS testowego, listy urządzeń/przeglądarek, danych testowych, wytycznych lokalizacji. Brak = brak DoR.


## Fazy cyklu życia

- Przygotowanie testów i środowiska LMS.  
- Testy funkcjonalne/dostępności/multimedia/lokalizacja.  
- Raport i poprawki.  
- Retesty/regresja i akceptacja.  
- Publikacja i monitoring feedbacku.



## Struktura sekcji (szkielet)
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (course/content/testing)  
- ui_test_strategy, accessibility_improvement_plan


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

1. Załaduj pakiet na LMS test; przygotuj checklisty.  
2. Wykonaj testy funkcji/dostępności/multimedia/lokalizacja.  
3. Zgłoś defekty; po poprawkach zrób regresję.  
4. Odhacz DoD; opublikuj kurs; zaktualizuj linkage_index.


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

- SCORM/xAPI: standardy śledzenia aktywności e‑learning.  
- LRS: Learning Record Store.  
- DoD: Definition of Done dla publikacji kursu.


## Przykłady użycia

- Test kursu onboardingowego z quizami i certyfikatem.  
- Weryfikacja tłumaczenia kursu na nowe języki.  
- Regresja po aktualizacji wideo lub quizu.


## Ryzyka i ograniczenia

- Błędy śledzenia → brak raportów postępów.  
- Brak dostępności → niezgodność i wykluczenie.  
- Problemy na urządzeniach mobilnych → niska adopcja.  
- Zmiany bez regresji → powracające defekty.


## Decyzje i uzasadnienia

- Zakres urządzeń/przeglądarek.  
- Poziom WCAG i priorytety poprawek.  
- Kadencja regresji.  
- Format raportowania do L&D.


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

- Treść ↔ Multimedia ↔ Dostępność.  
- Nawigacja ↔ Śledzenie danych ↔ Raporty LMS.  
- Lokalizacja ↔ Testy urządzeń ↔ Defekty.


## Struktura sekcji

1) Zakres kursu i wymagania  
2) Testy funkcjonalne/nawigacja/quizy  
3) Testy dostępności (WCAG)  
4) Multimedia i wydajność (audio/wideo)  
5) Śledzenie danych (SCORM/xAPI, LRS)  
6) Lokalizacja i urządzenia/przeglądarki  
7) Raport, DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Checklisty: funkcjonalność, dostępność, multimedia, lokalizacja.  
- Matryca urządzeń/przeglądarek i wyników.  
- Walidacja SCORM/xAPI i eventów LRS.  
- Szablon raportu defektów i priorytetów.  
- Procedura regresji po poprawkach.  
- Kryteria akceptacji (DoD) przed publikacją.


## Wymagane streszczenia

- Executive summary: status kursu, krytyczne defekty, akceptacja.  
- Skrót wyników na urządzeniach/przeglądarkach.


## Guidance (skrót)

- Testuj w LMS zbliżonym do produkcji; weryfikuj tracking.  
- Sprawdzaj WCAG: klawiatura, kontrast, napisy, ARIA.  
- Waliduj quizy/oceny i przejścia modułów.  
- Utrzymuj matrycę urządzeń; priorytetyzuj najczęstsze.  
- Dokumentuj i powtarzaj regresję po każdej poprawce.  
- Aktualizuj linkage_index po publikacji.


## Checklisty Definition of Ready (DoR)

- [ ] Pakiet kursu i scenariusze dostępne.  
- [ ] Środowisko LMS/LRS gotowe; dane testowe wgrane.  
- [ ] Checklisty QA i dostępności zatwierdzone.  
- [ ] Lista urządzeń/przeglądarek i języków określona.  
- [ ] Kryteria akceptacji ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Testy zakończone; krytyczne defekty zamknięte.  
- [ ] Tracking SCORM/xAPI działa; raporty poprawne.  
- [ ] Dostępność (WCAG) zweryfikowana; wyjątki udokumentowane.  
- [ ] Matryca urządzeń/przeglądarek zaliczona.  
- [ ] Dokumentacja/linkage_index zaktualizowane.

