---
title: PLM User Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# PLM User Training


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przygotować szkolenia użytkowników systemu PLM (Product Lifecycle Management): procesy, role, dane, wersjonowanie, change control i integracje, aby zapewnić poprawne użycie i jakość danych produktu.


## Zakres i granice

- Obejmuje: onboarding do PLM, role i uprawnienia, struktury danych (BOM, specyfikacje, dokumenty), wersjonowanie i change control, workflow zatwierdzeń, integracje (CAD, ERP, QMS), standardy nazewnictwa i klasyfikacji, raportowanie, dobre praktyki i typowe błędy.  
- Poza zakresem: szczegółowa konfiguracja PLM (oddzielna dokumentacja systemowa).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: procesy PLM, RACI, standardy danych, matryca uprawnień, lista integracji, przykładowe produkty/BOM, harmonogram szkolenia, narzędzia (LMS).  
- Wyjścia: program szkolenia (moduły/agenda), materiały (deck/ćwiczenia), checklisty DoR/DoD, test wiedzy, rejestr uczestników, ocena skuteczności, aktualizacja runbooków.


## Założenia

- PLM i integracje dostępne.  
- Użytkownicy mają podstawy domenowe.  
- Menedżerowie wspierają udział w szkoleniach.


## Otwarte pytania

- Jak mierzyć poprawę jakości danych po szkoleniach?  
- Jak często odświeżać moduły przy zmianach procesów?  
- Czy włączać partnerów/dostawców do szkoleń?

## Powiązania (meta)

- Key Documents: document_management_system, change_management, quality_assurance_plan, data_quality_playbook, access_control_policy, cad_integration_guidelines (jeśli istnieje).  
- Key Document Structures: role/uprawnienia, dane produktu, change control, integracje, QA danych, szkolenia.  
- Document Dependencies: PLM system, CAD/ERP integracje, LMS, CMDB produktów.


## Zależności dokumentu

Wymaga: aktualnych procesów PLM, standardów danych (BOM, naming), matrycy ról/uprawnień, dostępów do środowisk szkoleniowych, integracji CAD/ERP, materiałów przykładowych. Brak = brak DoR.


## Fazy cyklu życia

- Planowanie i przygotowanie materiałów.  
- Szkolenia (teoria + ćwiczenia).  
- Walidacja umiejętności (test/ćwiczenia).  
- Utrwalenie i wsparcie (FAQ, office hours).  
- Retrospektywa i ulepszenia.



## Struktura sekcji (szkielet)

- Opis stanowiska / roli
- Wymagania wstępne
- Zasoby i dostępy
- Ścieżka nauki (dzień 1/30/90)
- Pierwsze zadania
- Kontakty i eskalacja

## Szybkie powiązania

- linkage_index.jsonl (plm/user/training)  
- change_management, data_quality_playbook


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

1. Zbierz procesy PLM i standardy; przygotuj materiały/środowisko.  
2. Przeprowadź moduły i ćwiczenia; zbierz wyniki testu.  
3. Monitoruj jakość danych po szkoleniu; aktualizuj materiały.  
4. Uzupełnij linkage_index i rejestry szkoleniowe.


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

- BOM: Bill of Materials.  
- Change control: proces nadawania/akceptacji zmian w danych produktu.  
- PLM: system zarządzania cyklem życia produktu.


## Przykłady użycia

- Onboarding projektantów CAD do PLM.  
- Szkolenie produkcji/logistyki z wersjonowania BOM.  
- Wspólna praca R&D i jakości na jednym workflow.


## Ryzyka i ograniczenia

- Niepoprawne dane → błędne produkcje/zamówienia.  
- Brak wersjonowania → konflikty zmian.  
- Zła integracja CAD/ERP → niespójne BOM.  
- Niska adopcja → powrót do arkuszy i shadow IT.


## Decyzje i uzasadnienia

- Zakres obowiązkowych modułów i testów.  
- Poziom szczegółu naming/klasyfikacji.  
- Kto zatwierdza change control.  
- Narzędzia do monitorowania jakości danych.


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

- Dane produktu ↔ Wersjonowanie ↔ Change control.  
- Role/uprawnienia ↔ Workflow ↔ QA danych.  
- Integracje ↔ Nazewnictwo/klasyfikacja ↔ Raportowanie.


## Struktura sekcji

1) Role i uprawnienia w PLM  
2) Struktury danych (BOM/specyfikacje/dokumenty)  
3) Wersjonowanie i change control (workflow)  
4) Integracje CAD/ERP/QMS i dobre praktyki danych  
5) Raportowanie i audyt danych  
6) Szkolenia, testy, DoR/DoD  
7) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Agenda modułów i ćwiczeń (np. tworzenie BOM, zmiana wersji).  
- Checklista QA danych i naming.  
- Przykłady change request i approvali.  
- Instrukcje integracji CAD (import/ekspport) i ERP (synchronizacja).  
- Test wiedzy + kryteria zaliczenia.  
- Plan refresh szkoleń i utrwalenia.


## Wymagane streszczenia

- Executive summary: zakres szkolenia i kluczowe ryzyka danych.  
- Skrót najczęstszych błędów i jak ich unikać.


## Guidance (skrót)

- Ucz użytkowników na realnych przykładach produktów.  
- Podkreśl wersjonowanie i change control – źródło błędów danych.  
- Utrzymuj spójne nazewnictwo/klasyfikację; waliduj w PLM.  
- Monitoruj jakość danych po szkoleniu; szybkie feedback.  
- Aktualizuj materiały po zmianach procesów/integ.  
- Dokumentuj w linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Procesy PLM i standardy danych zaktualizowane.  
- [ ] Środowisko szkoleniowe i konta gotowe.  
- [ ] Materiały i ćwiczenia przygotowane.  
- [ ] Matryca ról/uprawnień dostępna.  
- [ ] Plan testu i kryteria zaliczenia zdefiniowane.


## Checklisty Definition of Done (DoD)

- [ ] Szkolenie przeprowadzone; testy zaliczone.  
- [ ] Materiały zaktualizowane po feedbacku.  
- [ ] Jakość danych monitorowana; działania korygujące zapisane.  
- [ ] linkage_index i rejestry uzupełnione.  
- [ ] Plan refresher ustalony.

