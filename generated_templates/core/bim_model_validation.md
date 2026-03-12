---
title: BIM Model Validation
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# BIM Model Validation


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zdefiniować procedury walidacji modeli BIM, aby zapewnić zgodność ze standardami (LOD/LOI, BEP/EIR), poprawność geometryczną i informacyjną, oraz gotowość do koordynacji/wykonawstwa.


## Zakres i granice

- Obejmuje: kontrolę geometrii (topologia, kolizje), LOI/LOD, naming i struktury plików, klasyfikację (IFC/Uniclass/OmniClass), atrybuty i parametry, zgodność z BEP/EIR, clash detection, QA/QC checklisty, raporty i komunikację błędów, wersjonowanie i audyt.  
- Poza zakresem: projektowanie nowych elementów (odniesienie do standardów modelowania), renderowanie/VR.


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: BEP/EIR, standardy naming/klasyfikacji, modele dyscyplin, dane referencyjne (siatki, poziomy), listy kontrolne QA/QC, narzędzia (Revit/Navisworks/IFC checker).  
- Wyjścia: raport walidacji z defektami i priorytetami, listy kolizji, checklisty DoR/DoD, status zgodności LOD/LOI, rekomendacje napraw, zaktualizowane modele/repo.


## Założenia

- Dostępny CDE i narzędzia checkerów.  
- Standardy BEP/EIR są zatwierdzone.  
- Zespół zna procedury QA/QC BIM.


## Otwarte pytania

- Jak często wykonywać pełną walidację (tydzień/sprint)?  
- Jakie formaty eksportu są wymagane przez kontrakt?  
- Jak raportować metryki jakości BIM (np. % modeli spełniających LOD)?

## Powiązania (meta)

- Key Documents: bim_user_training, document_management_system, clash_detection_guidelines, qa_engineer_onboarding, access_control_policy.  
- Key Document Structures: geometra, atrybuty/LOD/LOI, naming/klasyfikacja, kolizje, raporty.  
- Document Dependencies: CDE, IFC checker, clash detection tools, CMDB projektów, repo wersji.


## Zależności dokumentu

Wymaga: aktualnych standardów (BEP/EIR), listy modeli dyscyplin, narzędzi checker/clash, zasad wersjonowania i naming, dostępu do CDE. Brak = brak DoR.


## Fazy cyklu życia

- Przygotowanie standardów i checklist.  
- Walidacja modeli i kolizji.  
- Raportowanie i komunikacja napraw.  
- Retesty i potwierdzenie DoD.  
- Audyt okresowy i ulepszenia.



## Struktura sekcji (szkielet)
- Streszczenie i cele biznesowe
- Zakres, założenia, ograniczenia
- Kontekst domenowy i interesariusze
- Wymagania funkcjonalne i niefunkcjonalne
- Architektura/komponenty i integracje
- Model danych i przepływy informacji
- Bezpieczeństwo, prywatność i compliance
- Plan wdrożenia/migracji i kryteria go/no-go
- Monitoring/operacje oraz ryzyka i mitigacje
- Decyzje i uzasadnienia, pytania otwarte
## Szybkie powiązania

- linkage_index.jsonl (bim/model/validation)  
- clash_detection_guidelines, bim_user_training, document_management_system


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

1. Przygotuj standardy i checklisty; pobierz modele z CDE.  
2. Uruchom walidacje geometrii/atrybutów i clash detection.  
3. Sporządź raport z defektami i priorytetami; przypisz właścicieli.  
4. Po poprawkach wykonaj retest; odhacz DoD i zaktualizuj dokument.


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

- LOD/LOI: poziom szczegółowości geometrycznej/informacyjnej.  
- Clash: kolizja między elementami modeli.  
- CDE: Common Data Environment.


## Przykłady użycia

- Walidacja modelu MEP przed koordynacją.  
- Sprawdzenie LOD/LOI dla etapu wykonawczego.  
- Raport kolizji dla instalacji HVAC vs konstrukcja.


## Ryzyka i ograniczenia

- Niekompletne standardy → niespójność modeli.  
- Brak retestu → powracające kolizje.  
- Nadpisywanie modeli bez wersji → utrata audytu.  
- Niewłaściwe priorytety → opóźnienia budowy.


## Decyzje i uzasadnienia

- Kryteria priorytetyzacji kolizji.  
- Zakres LOD/LOI na etapy.  
- Narzędzia checker/clash i formaty wymiany.  
- Kadencja walidacji/audytu.


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

- Naming/klasyfikacja ↔ Atrybuty/LOD/LOI ↔ Raporty.  
- Clash detection ↔ Geometria ↔ Koordynacja.  
- Wersjonowanie ↔ Audyt ↔ Komunikacja błędów.


## Struktura sekcji

1) Standardy i wymagania (BEP/EIR, LOD/LOI, naming)  
2) Walidacja geometrii i topologii  
3) Walidacja atrybutów/klasyfikacji/LOD/LOI  
4) Clash detection i raportowanie kolizji  
5) Raporty QA/QC i priorytety defektów  
6) Wersjonowanie, audyt i komunikacja  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Checklisty walidacji (geometria, atrybuty, naming, klasyfikacja).  
- Reguły LOD/LOI na etapy projektu.  
- Szablon raportu kolizji (kategorie, priorytety, właściciele).  
- Polityka wersjonowania i naming plików/modeli.  
- Matryca narzędzi i eksportów (IFC, NWD, BCF).  
- Procedura retestu i zamykania defektów.


## Wymagane streszczenia

- Executive summary: status zgodności i główne defekty.  
- Skrót LOD/LOI i kolizji krytycznych.


## Guidance (skrót)

- Używaj checklist i automaty checkerów; wszystko dokumentuj w CDE.  
- Priorytetyzuj kolizje krytyczne wpływające na konstrukcję/instalacje.  
- Utrzymuj spójne naming/klasyfikacje – automatyczne walidatory.  
- Wersjonuj modele; nie nadpisuj bez historii.  
- Komunikuj defekty z właścicielami; śledź status w jednym narzędziu.  
- Aktualizuj linkage_index po każdej walidacji.


## Checklisty Definition of Ready (DoR)

- [ ] Standardy BEP/EIR i naming dostępne.  
- [ ] Modele dyscyplin aktualne; eksporty przygotowane.  
- [ ] Narzędzia checker/clash działają.  
- [ ] Checklisty walidacji zatwierdzone.  
- [ ] Dostęp do CDE i repo wersji.


## Checklisty Definition of Done (DoD)

- [ ] Walidacje wykonane; defekty sklasyfikowane i przypisane.  
- [ ] Kolizje krytyczne rozwiązane lub plan napraw.  
- [ ] Raporty i wersje modeli zaktualizowane w CDE.  
- [ ] linkage_index zaktualizowany; audyt/ślad zapisany.  
- [ ] Retest zakończony; brak otwartych krytycznych defektów.

