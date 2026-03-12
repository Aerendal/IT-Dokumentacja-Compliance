---
title: Asset Update Procedure
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Asset Update Procedure


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać bezpieczny i kontrolowany proces aktualizacji assetów (pliki, media, modele, konfiguracje) w środowiskach produkcyjnych/stage, z naciskiem na wersjonowanie, walidację, publikację, rollback i audyt.


## Zakres i granice

- Obejmuje: zgłoszenie/plan aktualizacji, wersjonowanie i naming, walidację/QA (checksum, skan, testy smoke), publikację na kanałach (repo/CDN/API), propagację cache, kompatybilność wstecz, komunikację i status, monitoring i rollback.  
- Poza zakresem: tworzenie nowych assetów (produkcja), zmiany kodu aplikacji (osobne procedury release).


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia

- Wejścia: opis zmiany assetu, wersja źródłowa i docelowa, wyniki QA/testów, kanały dystrybucji, lista zależnych systemów, wymagania zgodności/licencji, okno publikacji.  
- Wyjścia: zaktualizowany asset z wersją, log zmian, dowody QA, status publikacji, plan rollback, aktualizacja linkage_index, checklisty DoR/DoD.


## Założenia

- Dostępne repo/CDN i monitoring.  
- Zespół ma prawa do publikacji i rollbacku.  
- QA i skan narzędzia działają.


## Otwarte pytania

- Jak długo przechowywać poprzednie wersje?  
- Czy wymagane są podpisy cyfrowe dla wszystkich typów assetów?  
- Jak audytować pobrania/instalacje po aktualizacji?  
- Jak obsłużyć klientów offline/air‑gapped?

## Powiązania (meta)

- Key Documents: asset_delivery_strategy, content_delivery_network_cdn_design, rollback_runbook, quality_assurance_plan, change_management, security_controls_reference.  
- Key Document Structures: wersje, QA, publikacja, rollback, komunikacja, monitoring.  
- Document Dependencies: repo/CDN, CI/CD, skaner AV/licencji, monitoring, cache/edge, CMDB assetów.


## Zależności dokumentu

Wymaga: źródła prawdy assetu, narzędzi QA (skan/checksum), kanałów publikacji, polityk wersjonowania/naming, planu rollback, okna publikacji i zainteresowanych stron. Braki = brak DoR.


## Fazy cyklu życia

- Przygotowanie (zgłoszenie, wersja, QA).  
- Publikacja i propagacja.  
- Walidacja post‑release i monitoring.  
- Rollback (jeśli potrzebny) i zamknięcie.  
- Dokumentacja i retrospektywa.



## Struktura sekcji (szkielet)
- Cel, zakres i definicje sukcesu
- Trigger/scenariusze i preconditions
- Role, uprawnienia i narzędzia
- Kroki operacyjne (checklista) z walidacją
- Monitoring i dowody wykonania
- Rollback/contingency oraz komunikacja/escalacja
- Rejestr zmian runbooka
## Szybkie powiązania

- linkage_index.jsonl (asset/update/procedure)  
- asset_delivery_strategy, rollback_runbook, quality_assurance_plan


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

1. Utwórz zgłoszenie z opisem, wersją i ryzykiem.  
2. Wykonaj QA i testy; przygotuj kanały publikacji.  
3. Opublikuj, monitoruj i waliduj; komunikuj status.  
4. Jeśli problemy – wykonaj rollback; zaktualizuj dokumentację i linkage_index.


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

- Smoke test: szybka weryfikacja podstawowej funkcji po publikacji.  
- Cache purge: wymuszenie odświeżenia assetów w CDN.  
- Source of truth: repozytorium referencyjne danego assetu.


## Przykłady użycia

- Aktualizacja modeli ML w CDN dla inference edge.  
- Zmiana plików konfiguracyjnych dla klientów on‑prem.  
- Podmiana zestawu ikon/grafik w aplikacji web.


## Ryzyka i ograniczenia

- Brak kompatybilności wstecz → błędy klientów.  
- Niespójność cache → różne wersje u użytkowników.  
- Brak rollback → długi outage.  
- Niesprawdzony podpis → ryzyko bezpieczeństwa.


## Decyzje i uzasadnienia

- Wybór kanałów publikacji i TTL.  
- Kryteria stop/rollback.  
- Zakres smoke i testów regresji.  
- Polityka komunikacji (kto, kiedy, gdzie).


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

- Wersjonowanie ↔ QA ↔ Publikacja ↔ Monitoring ↔ Rollback.  
- Zależności systemów ↔ Kompatybilność ↔ Komunikacja.


## Struktura sekcji

1) Opis aktualizacji i wersje  
2) QA/validacja (skan, checksum, testy smoke)  
3) Publikacja i propagacja (repo/CDN/API/cache)  
4) Kompatybilność i zależności  
5) Monitoring i kryteria akceptacji  
6) Rollback i komunikacja  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Polityka wersjonowania (semver/naming) i etykiety release.  
- Lista testów smoke per typ assetu.  
- Kroki publikacji per kanał (repo/CDN/API) i czyszczenie cache.  
- Progi metryk i alertów po publikacji.  
- Procedura rollback z poprzednią wersją i walidacją.  
- Szablony komunikacji do interesariuszy.


## Wymagane streszczenia

- Executive summary: co/po co/kiedy wersja.  
- Skrót kompatybilności i zależności.


## Guidance (skrót)

- Zawsze weryfikuj checksum/podpis i wykonuj smoke przed publikacją.  
- Publikuj w oknach o niskim ruchu; monitoruj metryki i błędy.  
- Minimalizuj cache inconsistency (ETag/TTL, purge).  
- Miej gotowy rollback; trzymaj poprzednią wersję łatwo dostępnie.  
- Loguj wszystkie kroki; aktualizuj linkage_index i changelog.  
- Komunikuj zmiany do zespołów zależnych.


## Checklisty Definition of Ready (DoR)

- [ ] Opis zmiany i wersja docelowa dostępne.  
- [ ] QA/skan/checksum wykonane; testy smoke gotowe.  
- [ ] Kanały publikacji i okno uzgodnione.  
- [ ] Plan rollback i poprzednia wersja dostępne.  
- [ ] Interesariusze poinformowani.


## Checklisty Definition of Done (DoD)

- [ ] Asset opublikowany; metryki/monitoring w normie.  
- [ ] Brak krytycznych defektów; fallback/rollback niewykonany lub zakończony.  
- [ ] Changelog/linkage_index zaktualizowane.  
- [ ] Dowody QA i komunikacja zarchiwizowane.  
- [ ] Post‑release review wykonane; lekcje zapisane.

