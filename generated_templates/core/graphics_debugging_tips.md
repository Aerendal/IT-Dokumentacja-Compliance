---
title: Graphics Debugging Tips
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Graphics Debugging Tips


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zebrać praktyczne techniki debugowania grafiki (artefakty, perf, crash), aby skrócić czas diagnozy i zmniejszyć ryzyko regresji.


## Zakres i granice

- Obejmuje: repro i capture (RenderDoc/PIX/NSight), warstwy walidacji, diffy wizualne, debug LOD/streaming, synchronizację CPU/GPU, typowe artefakty, checklisty.
- Poza zakresem: szczegółowy design shaderów/pipeline.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: cele biznesowe, backlog/epiki, wymagania niefunkcjonalne, ograniczenia prawne/techniczne, istniejące systemy/dane.
- Wyjścia: zaakceptowana wersja dokumentu, decyzje architektoniczne/procesowe, action items z właścicielami i terminami.
## Założenia
- Laboratoria i sprzęt są dostępne i zgodne z BHP.  
- Zespoły mają czas na szkolenie.  
- Dostępne są licencje/sterowniki narzędzi.
## Otwarte pytania
- Jak często powtarzać szkolenie?  
- Czy wymagane są certyfikaty/odznaki po szkoleniu?  
- Jak archiwizować logi i wyniki labów?
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

- Kontekst i cele
- Setup narzędzi (capture/validation)
- Typowe artefakty i ścieżki diagnozy
- Perf i synchronizacja (CPU/GPU)
- LOD/streaming debug
- Checklista i przykłady
- Ryzyka i wyjątki


## Szybkie powiązania
- debugging-tips-and-tricks
- 3d-graphics-vision
- 3d-graphics-architecture
- test-automation-tips
- seasonal-farming-tips

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

- Wypełnij sekcje w kolejności: kontekst → wymagania → decyzje → testy/metryki.
- Dodaj quick-links do dokumentów zależnych; uzupełnij checklisty DoR/DoD w reports/checklist_atomic.jsonl.
- Po review zaktualizuj artefakty/metryki i status w Metadane.


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
- ESD: Electrostatic Discharge.  
- Boundary scan: test IEEE 1149.x.  
- Logic analyzer: narzędzie do analizy cyfrowych przebiegów.
## Przykłady użycia
- Szkolenie nowych inżynierów hardware.  
- Warsztat z debugowania prototypu z SoC + DDR.  
- Scenariusz naprawy niedziałającego portu komunikacyjnego.
## Ryzyka i ograniczenia
- Uszkodzenie sprzętu przy błędnych pomiarach/flashu.  
- Brak ESD → sporadyczne, trudne do powtórzenia błędy.  
- Brak logów → utrata wiedzy i czasu.
## Decyzje i uzasadnienia
- Zakres scenariuszy w zależności od produktów/SoC.  
- Wybór narzędzi (open-source vs vendor).  
- Standard logów/ticketów (format danych pomiarowych).
## Powiązania z innymi dokumentami
- board_bringup_checklist — debug prototypów.  
- firmware_recovery_guide — flash/recovery.  
- logging_standards_embedded — format logów.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Zasady BHP/ESD labów.  
- IEEE 1149.x (boundary scan) gdzie stosowalne.
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

- Zgłoszenia/artefakty i sceny repro
- Narzędzia capture/profiling dostępne
- Wersje build/driver/API
- Cele jakości/perf


## Wyjścia

- Lista technik/debug steps
- Checklisty dla artefaktów i crashy
- Linki do narzędzi i konfiguracji
- Powiązania do runbooków i testów



## Szybkie powiązania (uzupełnij)

- [ ] visual_artifact_resolution.md
- [ ] visual_regression_test_specification.md
- [ ] shader_testing.md
- [ ] rendering_failure_response.md
- [ ] graphics_best_practices.md
- [ ] gpu_utilization_monitoring.md


## Wymagane rozwinięcia / streszczenia

- Rozwinięcia kluczowych decyzji/ryzyk; krótkie streszczenie wyników/fixów.


## Wymagane powiązania

- Rendering/shader/QA dokumenty powiązane; narzędzia profilujące/diff; polityki jakości.


## Kryteria DoR

- [ ] Scena repro i opis artefaktu
- [ ] Narzędzia capture/validation dostępne
- [ ] Wersje build/driver znane
- [ ] Cele jakości/perf zebrane


## Kryteria DoD

- [ ] Checklisty i techniki wypełnione
- [ ] Przykłady z capture/diff dodane
- [ ] Quick-links/checklisty uzupełnione
- [ ] Metadane zaktualizowane


## Artefakty do załączenia

- Capture sesje (rdc/pix/nsight)
- Checklisty debug
- Przykłady przed/po
- Logi/raporty z debug


## Walidacja / testy

- Testy perf/stabilności na scenach referencyjnych.
- Testy regresji wizualnej na platformach/ustawieniach docelowych.


## Metryki monitorowane

- Czas diagnozy artefaktu
- Liczba powtórnych wystąpień
- Udział zgłoszeń rozwiązanych z tym runbookiem
- False positive rate w diffach


## Utrzymanie i aktualizacje

- Przegląd co release lub po istotnych zmianach shader/pipeline/streaming.
- Aktualizacja quick-links, checklist i artefaktów po każdej istotnej zmianie.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, podlinkuj artefakty/quick-links i odhacz checklistę w reports/checklist_atomic.jsonl.
