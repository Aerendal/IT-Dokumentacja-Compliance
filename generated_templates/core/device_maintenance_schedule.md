---
title: Device Maintenance Schedule
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Device Maintenance Schedule


## Metadane

- Właściciel: Project Manager
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Ustalić harmonogram i zakres utrzymania urządzeń (IT/IoT/produkcyjne), aby zapewnić dostępność, bezpieczeństwo i zgodność z gwarancjami/regulacjami.


## Zakres i granice

- Obejmuje: inwentarz urządzeń, klasy krytyczności, czynności serwisowe (FW/OS/patch, kalibracje, czyszczenie, części), cykle (dzienny/tyg./mies./kwart./roczny), okna serwisowe, odpowiedzialności, części zamienne, bezpieczeństwo (backup/konfiguracje), dokumentowanie prac, SLA/OLA.
- Poza zakresem: projekt nowych urządzeń (osobne), naprawy awaryjne poza planem (odnotować ale nie planować tu).


## Użytkownicy i interesariusze
- Tech Writing, PMO, Security/Compliance, Engineering/Operations, Audit.
## Wejścia i wyjścia

- Wejścia: CMDB/inwentarz, instrukcje producentów, gwarancje, regulacje branżowe, historia awarii, dostępność części, okna serwisowe.
- Wyjścia: kalendarz prac, checklisty per klasa urządzeń, lista części/wersji FW, plan backup/konfiguracji, rejestr wykonanych prac, metryki (MTBF/MTTR/overdue).


## Założenia
- Repo dokumentacji i narzędzia CI/lint dostępne; ownerzy przypisani.
## Otwarte pytania
- Jakie raporty dla leadership/audytu? 
- Czy archiwizujemy wersje w dedykowanym repo lub systemie DMS?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: CMDB, manuale producentów, polityki patchingu, regulacje (np. medyczne/lotnicze), umowy serwisowe, magazyn części; brak – odnotuj.


## Fazy cyklu życia

Planowanie → Przygotowanie części/okien → Wykonanie → Weryfikacja → Raport/Audyt → Korekty.



## Struktura sekcji (szkielet)

- Klasy urządzeń i krytyczność; zakres czynności.
- Kalendarz prac i okna serwisowe.
- Checklisty czynności per klasa (patch/FW, kalibracja, czyszczenie, testy).
- Backup/konfiguracje przed/po.
- Części zamienne i magazyn.
- Dokumentacja prac (rejestr, podpisy, dowody).
- Metryki i raportowanie (MTBF, MTTR, overdue, audyty).
- Ryzyka i mitigacje.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów

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

- Skategoryzuj urządzenia; zaplanuj kalendarz; przygotuj części i backup; wykonaj czynności; udokumentuj; monitoruj wskaźniki.


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
- Dokument krytyczny, Review due, Overdue, Archiwizacja, Retencja.
## Przykłady użycia
- Harmonogram rocznych przeglądów polityk bezpieczeństwa; kwartalne runbooki; powiązanie z release major.
## Ryzyka i ograniczenia
- Przeterminowane dokumenty → błędy operacyjne/audytowe; brak katalogu → brak odpowiedzialności.
## Decyzje i uzasadnienia

- [Decyzja 1]
- [Decyzja 2]


## Powiązania z innymi dokumentami
- Documentation Standards, Change Mgmt, Release Plan, Compliance Calendar, Audit Logging, Versioning Guidelines.
## Powiązania z sekcjami innych dokumentów
- Change/Release → trigger przeglądów; Compliance → terminy; Versioning → archiwizacja.
## Słownik pojęć w dokumencie
- Dokument krytyczny, Review due, Overdue, Archiwizacja, Retencja.
## Wymagane odwołania do standardów
- Polityki compliance i audytu, standardy dokumentacji wewnętrznej.
## Mapa relacji sekcja→sekcja
- Katalog → Harmonogram → Review → Raport → Archiwizacja.
## Mapa relacji dokument→dokument
- Maintenance Schedule → Docs Standards/Change/Release/Compliance → Audit.
## Ścieżki informacji
- Katalog → Kalendarz → Review → Raport → Eskalacja/Archiwizacja.
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
- Katalog, kalendarz, checklisty, raporty status, reguły CI/lint, archiwum.
## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]


## Ścieżka akceptacji
- Tech Writing/PMO → Security/Compliance → Owners → Audit/Owner sign‑off.
## Metryki jakości
- % dokumentów aktualnych, średnie overdue, czas review, liczba znalezionych błędów w review, zgodność z compliance (audyt).
## Kryteria ukończenia
- [ ] Harmonogram i procesy opisane; raportowanie/archiwizacja działa; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

Inwentarz → kalendarz → części; krytyczność → częstotliwość; backup → patching; dokumentacja → audyt.


## Wymagane rozwinięcia

- Checklisty → szczegóły z manuali.
- Backup → procedury i lokalizacje.


## Wymagane streszczenia

- Tabela klas urządzeń → częstotliwość → właściciel → okno.


## Guidance

Cel: przewidywalne utrzymanie z minimalnym downtime. DoR: inwentarz, manuale, SLA, okna dostępne. DoD: kalendarz/checklisty/metryki gotowe; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Inwentarz i krytyczność; [ ] Manuale/regulacje; [ ] Okna i zasoby; [ ] Backup dostępny.
- DoD: [ ] Kalendarz i checklisty uzupełnione; [ ] Prace udokumentowane; [ ] Metryki/raportowanie opisane; sekcje N/A uzasadnione; metadane aktualne.

