---
title: ITSM Process Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# ITSM Process Training


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Przygotować program szkoleniowy z procesów ITSM (Incident, Problem, Change, Request, CMDB, SLA), aby zespoły stosowały spójne procedury, narzędzia i metryki.


## Zakres i granice

- Obejmuje: cele procesów, role i RACI, przepływy (Incident/Problem/Change/Request/Knowledge/CMDB), SLA/OLA, narzędzia (ITSM tool), formularze, standardy jakości, raportowanie, ćwiczenia praktyczne, certyfikacja wewnętrzna.
- Poza zakresem: wdrożenie samego narzędzia ITSM (osobne), polityki HR.


## Użytkownicy i interesariusze

- [Rola] — [potrzeby/odpowiedzialności]
- [Rola] — [potrzeby/odpowiedzialności]


## Wejścia i wyjścia

- Wejścia: polityki ITSM, katalog usług, SLA/OLA, konfiguracja narzędzia, raporty audytowe, lista typowych błędów.
- Wyjścia: sylabus, materiały (prezentacje/runbooki), laboratoria w narzędziu, checklisty DoR/DoD per proces, quiz/ocena, harmonogram sesji, metryki skuteczności (adopcja, poprawność danych, SLA).


## Założenia

- [Założenie 1]
- [Założenie 2]


## Otwarte pytania

- [Pytanie 1]
- [Pytanie 2]


## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: procesy ITSM, konfigurację narzędzia, katalog usług, CMDB, SLA/OLA, polityki bezpieczeństwa danych; brak – odnotuj.


## Fazy cyklu życia

Plan → Przygotowanie materiałów/labów → Sesje → Ocena → Aktualizacja programu.



## Struktura sekcji (szkielet)

- Cele i KPI szkolenia (adopcja, poprawność danych, SLA adherence).
- Zakres procesów i RACI.
- Narzędzia i konfiguracja (widoki, formularze, kody kategorii).
- Ćwiczenia praktyczne (Incident, Problem, Change, Request, Knowledge, CMDB updates).
- Raportowanie i metryki.
- Ocena i certyfikacja (quiz, praktyka).
- Plan utrzymania programu.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO 20000-1** — System Zarządzania Usługami IT (SMS)
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

### Polskie normy i regulacje
- **PN-EN-ISO-9001** — PN-EN ISO 9001:2015-10 — Systemy Zarządzania Jakością
- **PN-EN-ISO-IEC-20000-1** — PN-EN ISO/IEC 20000-1:2019 — Zarządzanie Usługami IT
- **PN-ISO/IEC-27001** — PN-ISO/IEC 27001:2023-09 — Systemy Zarządzania Bezpieczeństwem Informacji

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

- Dostosuj sylabus do ról; przygotuj laby; przeprowadź sesje; oceń; monitoruj metryki adopcji; aktualizuj program.


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

- [Termin 1]
- [Termin 2]
- [Termin 3]


## Przykłady użycia

- [Przykład 1]
- [Przykład 2]


## Ryzyka i ograniczenia

- [Ryzyko 1]
- [Ryzyko 2]


## Decyzje i uzasadnienia

- [Decyzja 1]
- [Decyzja 2]


## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód]
- [Dokument Z → Sekcja W] — [powód]


## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1]
- [Standard 2]


## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ]
- [Sekcja C] -> [Sekcja D] : [typ]


## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ]
- [Dokument C] -> [Dokument D] : [typ]


## Ścieżki informacji

- [Wejście] → [Źródło] → [Rozwinięcie] → [Wyjście]
- [Wejście] → [Źródło] → [Streszczenie] → [Wyjście]


## Weryfikacja spójności

- [ ] Ścieżki informacji zamknięte
- [ ] Brak sprzecznych relacji
- [ ] Sekcje krytyczne mają źródła


## Lista kontrolna spójności relacji

- [ ] Relacje mają sekcje źródłowe
- [ ] Relacje nie są sprzeczne
- [ ] Cross-doc uzasadnione
- [ ] Rozwinięcia/streszczenia odnotowane


## Artefakty powiązane

- [Artefakt 1]
- [Artefakt 2]


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]


## Ścieżka akceptacji

1. Autor przygotowuje wersję roboczą i przeprowadza samorecenzję.
2. Recenzent techniczny (Tech Lead / BA) weryfikuje merytorycznie.
3. Właściciel procesu zatwierdza treść i zakres.
4. PM / Scrum Master aktualizuje metadata (wersja, data, status).
5. Dokument trafia do repozytorium i jest linkowany w Szybkie powiązania.

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

Proces → rola → narzędzie → raportowanie; SLA → ćwiczenia; CMDB → Request/Change.


## Wymagane rozwinięcia

- Ćwiczenia → szczegółowe scenariusze i dane.
- Raporty → szablony w narzędziu.


## Wymagane streszczenia

- One-pager: procesy, role, SLA, narzędzie, zasady jakości danych.


## Guidance

Cel: spójne stosowanie ITSM. DoR: polityki, SLA, konfiguracja narzędzia, katalog usług dostępne. DoD: sylabus/ćwiczenia/raporty/ocena gotowe; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Polityki ITSM, SLA/OLA, konfiguracja narzędzia zebrane; [ ] Katalog usług/CMDB dostępny.
- DoD: [ ] Sylabus/ćwiczenia/quizy gotowe; [ ] Raporty/metryki zdefiniowane; [ ] Sekcje N/A uzasadnione; metadane aktualne.

