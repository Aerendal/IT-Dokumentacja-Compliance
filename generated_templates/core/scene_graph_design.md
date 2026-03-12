---
title: Scene Graph Design
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Scene Graph Design


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link do silnika / sceny]


## Cel dokumentu

Zaprojektować i utrzymywać scene graph (hierarchie, komponenty, aktualizacje) tak, aby był wydajny, spójny i łatwy do rozszerzania w grach/aplikacjach 3D/AR/VR.


## Zakres i granice

- Zakres: model danych (node/component/ECS), transformacje i dziedziczenie, porządek aktualizacji (tick/event), culling/LOD, instancjonowanie i streaming, warstwy (render/physics/UI), synchronizacja z fizyką/animacją, serializacja/persistencja, debug/inspekcja, wątki i bezpieczeństwo.
- Poza zakresem: asset pipeline, szczegóły render pipeline i shaderów (opisane w innych dokumentach).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: use cases/persony, backlog epik, ograniczenia techniczne/prawne, decyzje zależne (ADR), dane i systemy źródłowe.
- Wyjścia: zaakceptowany projekt, diagramy (kontekst, komponenty, sekwencje, dane), lista decyzji z uzasadnieniem, plan wdrożenia/migracji.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Wymaga odniesienia do: Key Documents, Key Document Structures, Document Dependencies, RACI i role, Standardy i compliance.


## Zależności dokumentu

Architektura renderingu/fizyki/animacji, budżety perf, formaty assetów, wymagania edytora/tools, system scripting/ECS; brak → odnotuj i zaplanuj uzupełnienie.


## Fazy cyklu życia

Discovery → Design → Prototyp → Review → Implementacja → Testy perf/stability → Utrzymanie.



## Struktura sekcji (szkielet)

1. Kontekst produktu i budżety perf/stability.
2. Model danych: node vs component/ECS, hierarchie, ID/naming, ownership.
3. Aktualizacja: tick/event, dependency ordering, wątki/lockless, przerwania.
4. Transformacje: dziedziczenie macierzy, dirty flags, space conversions.
5. Culling i LOD: view-frustum/occlusion/distance/importance; polityki per warstwa.
6. Instancjonowanie, prefaby, streaming sceny i lifecycle obiektów.
7. Warstwy: render/physics/UI i synchronizacja z animacją/fizyką.
8. Serializacja/persistencja: format, versioning, backward compatibility, save/load.
9. Debug/inspekcja/profiling: overlay, capture, trace, walidatory.
10. Ryzyka i ograniczenia; decyzje architektoniczne.


## Szybkie powiązania
- world-scene-architecture-design
- wan-design
- vm-design-patterns
- visualization-design
- ui-ux-design-document

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

- Wypełnij sekcje 1–3 na podstawie wymagań i architektury render/fizyka/anim.
- Zdefiniuj strategie culling/LOD i streaming (sekcje 4–6) oraz serializację (8).
- Dodaj quick-links do zależnych dokumentów; odhacz DoR/DoD w checklistach.
- Po review uzupełnij metryki, artefakty i zaktualizuj status w Metadane.


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

- Wymagania produktu (typ doświadczenia, target platformy, budżety perf).
- Architektura renderingu, fizyki i animacji; ograniczenia pamięci/WASM/konsola/mobile.
- Decyzja co do modelu danych (ECS vs klasy), potrzeby edytora/tools, polityki wątków.
- Wymagania dot. serializacji/save-load, streaming świata, wielkość sceny.


## Wyjścia

- Specyfikacja scene graph: struktury danych, API, zasady ownership/naming/ID.
- Strategie aktualizacji i synchronizacji (render/physics/UI), kolejność i priorytety.
- Zasady LOD/culling/instancjonowania/streamingu; polityki lifetime obiektów.
- Format i wersjonowanie serializacji, wymagania debug/inspekcji/profilingu.
- Checklisty zgodności i metryki dla perf/stability.


## Powiązania sekcja↔sekcja

Model danych → aktualizacja/culling; LOD → instancjonowanie; serializacja → edytor/save/load; wątki → bezpieczeństwo aktualizacji.


## Szybkie powiązania (uzupełnij)

- [ ] Rendering architecture / pipeline overview
- [ ] Physics integration guide
- [ ] Tools/editor requirements
- [ ] Performance budget / profiling playbook
- [ ] Asset/scene serialization format spec


## Wymagane rozwinięcia / streszczenia

- Aktualizacja/wątki → kolejność, lockless/locks, hazardy i strategie rollback.
- Serializacja → format, versioning, test zgodności wstecznej.
- Debug → zestaw narzędzi edytora/overlay + przykładowe checklisty perf.
- Streszczenie wizualne: diagram scene graph + tabela zasad aktualizacji/LOD.


## Wymagane powiązania

- Architektura renderingu / fizyki / animacji.
- Standardy naming/ID oraz zasady ownership obiektów.
- Linie produktowe: wymagania edytora, pipeline buildów, polityki pamięci.


## Kryteria DoR

- [ ] Budżety perf i target platformy ustalone.
- [ ] Architektura render/fizyka/anim znana; dostęp do API integracyjnych.
- [ ] Wybrany model danych (node/component/ECS) i polityka wątków.
- [ ] Wymagania serializacji/save-load zebrane.


## Kryteria DoD

- [ ] Sekcje 2–9 opisane lub oznaczone N/A z uzasadnieniem.
- [ ] Zdefiniowane kolejności aktualizacji i polityki wątków.
- [ ] Culling/LOD/streaming mają reguły i metryki akceptacji.
- [ ] Serializacja ma format i test kompatybilności; opisany debug/profiling.
- [ ] Metadane aktualne; quick-links i checklisty zaktualizowane.


## Artefakty do załączenia

- Diagram scene graph, tabela update-order/priority, przykładowe reguły LOD.
- Plik wzorcowy serializacji + test kompatybilności.
- Zrzuty z narzędzi debug/profiling, logi z testów perf.


## Walidacja / testy

- Testy perf: FPS/frametime, stutter, GC; profilowanie CPU/GPU.
- Testy poprawności: dziedziczenie transformacji, cycle detection, determinism.
- Testy zgodności serializacji: load/save across wersje, różne platformy.


## Metryki monitorowane

- Frametime (p50/p95), liczba draw calls, liczba nodeów aktywnych vs culled.
- Czas aktualizacji sceny (ms) i udział w budżecie klatki.
- Sukces/porazka testów kompatybilności serializacji.


## Utrzymanie i aktualizacje

- Przegląd co release lub przy zmianie pipeline’u render/physics/anim.
- Synchronizacja z zespołem tools/editor i zespół perf; rejestr zmian w DB.


## Zakończenie

Po spełnieniu DoD zaktualizuj status w Metadane, podlinkuj quick-links i artefakty, a checklistę odhacz w `reports/checklist_atomic.jsonl`.
