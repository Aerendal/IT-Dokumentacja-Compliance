---
title: Shader Compilation
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Shader Compilation


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zdefiniować proces kompilacji shaderów (offline/online), zarządzanie wariantami i cache, aby minimalizować czasy kompilacji oraz błędy kompatybilności.


## Zakres i granice

- Obejmuje: pipeline kompilacji (CI/offline/at-runtime), profile/targety (SM/feature levels), zarządzanie defines/variant explosion, cache (disk/in-memory/distribution), PSO, walidację i debug.
- Poza zakresem: treść pojedynczych shaderów i asset pipeline.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: cele biznesowe, backlog/epiki, wymagania niefunkcjonalne, ograniczenia prawne/techniczne, istniejące systemy/dane.
- Wyjścia: zaakceptowana wersja dokumentu, decyzje architektoniczne/procesowe, action items z właścicielami i terminami.
## Założenia
- Dostępne są zespoły compliance/kliniczne do akceptacji.  
- Narzędzia IAM, SIEM/SOAR, katalog danych i iPaaS są dostępne.  
- Budżet na testy DR/BCP i laboratoria integracyjne.
## Otwarte pytania
- Czy partnerzy zewnętrzni wymagają dedykowanych stref integracji?  
- Jakie są lokalne wymogi prawne (kraje) dot. lokalizacji danych medycznych?  
- Jak wygląda proces rotacji kluczy/secretów dla urządzeń IoMT?
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
- Profile/targety shaderów
- Proces kompilacji (offline/online/CI)
- Warianty/defines i limitowanie eksplozji
- Cache/PSO i invalidacja
- Walidacja/debug i telemetry
- Ryzyka i decyzje


## Szybkie powiązania
- shader-testing
- shader-documentation
- shader-development
- shader-architecture
- shader-security-review

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
- PHI (Protected Health Information): dane identyfikujące pacjenta i jego historię.  
- Interoperacyjność: bezpieczna wymiana danych klinicznych między systemami/partnerami.  
- NAC: Network Access Control dla urządzeń/IoMT.
## Przykłady użycia
- Modernizacja EHR z integracją FHIR i PACS.  
- Budowa telemedycyny z dostępem do danych pacjenta i billingiem.  
- Segmentacja sieci klinicznej i IoMT dla audytu bezpieczeństwa.
## Ryzyka i ograniczenia
- Naruszenie prywatności/RODO/HIPAA.  
- Przestoje systemów klinicznych wpływające na opiekę pacjenta.  
- Luki w IoMT/firmware i brak patchy.
## Decyzje i uzasadnienia
- Wybór standardu integracji (FHIR/HL7) dla nowych usług.  
- Poziomy segmentacji i dostępu do PHI.  
- Architektura DR (aktywny/aktywny vs aktywny/pasywny) dla EHR/PACS.
## Powiązania z innymi dokumentami
- privacy_and_consent_policy — zasady zgód i PII/PHI.  
- interoperability_plan — szczegóły integracji i testów.  
- dr_plan_clinical_it — ciągłość działania i testy DR.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- HIPAA / RODO, normy lokalne (np. HL7 PL), FHIR/HL7/DICOM.  
- Wewnętrzne standardy bezpieczeństwa i segmentacji klinicznej.
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

- Lista platform/API i targetów shader model
- Wymagania efektów/materialów (liczba wariantów)
- Budżet czasu kompilacji (CI/build/runtime)
- Narzędzia kompilacji (DXC/GLSL/Vulkan/Metal) i walidacji


## Wyjścia

- Proces kompilacji i walidacji (kroki, narzędzia)
- Strategia wariantów/defines i ograniczania ich liczby
- Zasady cache/PSO (lokalny/centralny, invalidacja)
- Checklisty DoR/DoD + punkty telemetry



## Szybkie powiązania (uzupełnij)

- [ ] shader_architecture.md
- [ ] shader_testing.md
- [ ] shader_optimization_patterns.md
- [ ] rendering_pipeline_design.md
- [ ] graphics_best_practices.md
- [ ] graphics_architecture_reference.md


## Wymagane rozwinięcia / streszczenia

- Rozwinięcia kluczowych decyzji/ryzyk; krótkie streszczenie wymagań i wyników testów.


## Wymagane powiązania

- Rendering/shader/LOD/streaming dokumenty, narzędzia profilingu/diffów, polityki jakości.


## Kryteria DoR

- [ ] Platformy/API i targety SM wybrane
- [ ] Lista efektów/materialów i wariantów zebrana
- [ ] Budżet czasu kompilacji ustalony
- [ ] Narzędzia kompilacji dostępne


## Kryteria DoD

- [ ] Proces kompilacji/cache opisany
- [ ] Warianty i limitacje zdefiniowane
- [ ] Walidacja/debug i telemetry ujęte
- [ ] Quick-links/checklisty uzupełnione


## Artefakty do załączenia

- Skrypty kompilacji/CI
- Tabela wariantów/defines
- Raporty czasu kompilacji
- Logi/raporty walidacji


## Walidacja / testy

- Testy perf i stabilności na scenach referencyjnych / ruchu reprezentatywnym.
- Testy regresji wizualnej i funkcjonalnej na platformach/urządzeniach.


## Metryki monitorowane

- Czas kompilacji (CI/runtime)
- Cache hit-rate PSO/shader
- Liczba wariantów na materiał/efekt
- Defekty kompilacji na build


## Utrzymanie i aktualizacje

- Przegląd co release lub przy większych zmianach pipeline/shader/streaming.
- Aktualizacja quick-links, checklist i artefaktów po każdej istotnej zmianie.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, podlinkuj artefakty/quick-links i odhacz checklistę w reports/checklist_atomic.jsonl.
