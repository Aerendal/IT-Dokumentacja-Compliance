---
title: BIM User Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# BIM User Training


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przygotować plan szkoleń użytkowników BIM (projektanci, koordynatorzy, wykonawcy) obejmujący narzędzia, standardy, procesy i kontrolę jakości, aby zwiększyć produktywność i spójność modeli.


## Zakres i granice

- Obejmuje: onboarding do CDE, standardy modelowania (LOD/LOI), naming conventions, struktura plików, praca współbieżna/koordynacja, clash detection, QA/QC, eksporty/IFC, wersjonowanie, bezpieczeństwo dostępu, role i uprawnienia, checklisty.  
- Poza zakresem: szkolenia CAD 2D bez BIM, kontrakty prawne (osobne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: standardy BIM organizacji (BEP, EIR), wymagania projektu, role i matryca uprawnień, narzędzia (Revit/Archicad/Navisworks/IFC), lista typowych błędów, harmonogram projektu.  
- Wyjścia: program szkolenia (moduły/agenda), materiały (prezentacje, ćwiczenia, checklisty), plan egzaminu/walidacji, listy obecności, ocena skuteczności, DoR/DoD.


## Założenia

- Standardy i CDE są stabilne.  
- Uczestnicy mają podstawy CAD/BIM.  
- Dostępny jest trener lub SME dla specjalistycznych tematów.


## Otwarte pytania

- Jakie KPI szkolenia (np. spadek clashy o X%)?  
- Jak długo utrzymywać nagrania i materiały?  
- Czy potrzebne są ścieżki dla ról specjalnych (MEP, konstrukcja)?

## Powiązania (meta)

- Key Documents: bim_model_validation, document_management_system, access_control_policy, qa_engineer_onboarding, project_execution_plan, clash_detection_guidelines.  
- Key Document Structures: moduły szkoleniowe, ćwiczenia, walidacja, uprawnienia, QA/QC.  
- Document Dependencies: CDE, licencje narzędzi, konta użytkowników, repo standardów, system SSO/IAM.


## Zależności dokumentu

Wymaga: aktualnych standardów BIM (BEP/EIR), listy uczestników i ról, dostępów do CDE i licencji, harmonogramu projektu, wymagań QA/QC. Braki = brak DoR.


## Fazy cyklu życia

- Planowanie i przygotowanie materiałów.  
- Szkolenia (teoria + praktyka).  
- Walidacja umiejętności i korekty.  
- Utrwalenie (przypomnienia, QA/QC na projekcie).  
- Retrospektywa i ulepszenia.



## Struktura sekcji (szkielet)

- Opis stanowiska / roli
- Wymagania wstępne
- Zasoby i dostępy
- Ścieżka nauki (dzień 1/30/90)
- Pierwsze zadania
- Kontakty i eskalacja

## Szybkie powiązania

- linkage_index.jsonl (bim/user/training)  
- bim_model_validation, clash_detection_guidelines, document_management_system


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
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

1. Przygotuj listę ról i dostępów, materiały i środowisko CDE.  
2. Przeprowadź moduły teoretyczne i ćwiczenia.  
3. Zweryfikuj umiejętności (quiz/zadanie), daj feedback.  
4. Monitoruj jakość modeli w projekcie; aktualizuj plan i linkage_index.


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

- CDE: Common Data Environment do współdzielenia modeli.  
- BEP: BIM Execution Plan.  
- LOD/LOI: poziom szczegółowości geometrycznej/informacyjnej.


## Przykłady użycia

- Szkolenie nowego zespołu projektantów przed fazą koordynacji.  
- Ujednolicenie praktyk BIM między firmami w JV.  
- Refresh dla wykonawców przed startem budowy.


## Ryzyka i ograniczenia

- Brak dostępu/licencji → opóźnienie szkoleń.  
- Zbyt ogólne ćwiczenia → słaba transferowalność.  
- Brak walidacji → brak poprawy jakości modeli.  
- Nieaktualne standardy → chaos w CDE.


## Decyzje i uzasadnienia

- Zakres modułów i głębokość (pod projekt/rolę).  
- Kryteria zaliczenia i progi quizu.  
- Narzędzia i wersje wspierane.  
- Kadencja szkoleń odświeżających.


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

- Standardy i naming ↔ QA/QC ↔ Clash detection.  
- Role/uprawnienia ↔ CDE ↔ Bezpieczeństwo dostępu.  
- Ćwiczenia ↔ Walidacja ↔ Ocena skuteczności.


## Struktura sekcji

1) Kontekst projektu i standardy BIM  
2) Moduły szkoleniowe (CDE, modelowanie, koordynacja, QA/QC, bezpieczeństwo)  
3) Ćwiczenia praktyczne i scenariusze  
4) Walidacja/egzamin i kryteria zaliczenia  
5) Materiały i wsparcie (FAQ, runbooki)  
6) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Agenda modułów z czasem i trenerem.  
- Ćwiczenia: tworzenie modelu, eksport IFC, clash detection, wersjonowanie.  
- Checklisty QA/QC i naming conventions.  
- Plan walidacji (quiz + zadanie praktyczne).  
- Plan utrwalenia (micro‑learning, office hours).  
- Matryca uprawnień i dostępów w CDE.


## Wymagane streszczenia

- Executive summary: zakres szkolenia, grupy docelowe, daty.  
- Skrót wymagań BEP/EIR i kluczowych standardów.


## Guidance (skrót)

- Używaj przykładów z aktualnego projektu; ćwicz na tym samym CDE.  
- Wymuś naming/structuring na ćwiczeniach; weryfikuj QA/QC.  
- Zaplanuj powtórki i wsparcie po szkoleniu.  
- Mierz skuteczność (quiz, jakość modeli, liczba clashy).  
- Zapewnij dostęp/SSO przed szkoleniem, by nie tracić czasu.  
- Aktualizuj materiały po każdej iteracji i w linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Standardy BEP/EIR i naming dostępne.  
- [ ] Lista uczestników i role z uprawnieniami w CDE.  
- [ ] Licencje/narzędzia i konta skonfigurowane.  
- [ ] Materiały/ćwiczenia przygotowane.  
- [ ] Harmonogram sesji uzgodniony.


## Checklisty Definition of Done (DoD)

- [ ] Sesje zrealizowane; frekwencja i materiały udostępnione.  
- [ ] Egzamin/walidacja zaliczona przez uczestników.  
- [ ] Checklisty QA/QC stosowane w projektach.  
- [ ] Linkage_index i repo materiałów zaktualizowane.  
- [ ] Feedback zebrany; plan poprawek zapisany.

