---
title: Documentation Maintenance Schedule
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Documentation Maintenance Schedule


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Ustala harmonogram przeglądów i aktualizacji dokumentacji (technicznej, operacyjnej, compliance), aby była aktualna, spójna i audytowalna. Ma zmniejszyć ryzyko pracy na nieaktualnych procedurach i ułatwić zgodność.


## Zakres i granice

- Obejmuje: katalog dokumentów (runbooki, polityki, procedury, architektura), częstotliwości przeglądów, właścicieli, checklisty jakości, wersjonowanie, ścieżkę zatwierdzania, raportowanie statusu, archiwizację/retencję, powiązania z release/zmianą.
- Poza zakresem: tworzenie nowych dokumentów (oddzielne guideline), repozytorium narzędziowe (link).


## Użytkownicy i interesariusze

- Tech Writing, PMO, Security/Compliance, Engineering/Operations, Audit.


## Wejścia i wyjścia

- Wejścia: lista dokumentów i właścicieli, krytyczność, wymagania compliance (np. roczne przeglądy), kalendarz release/changes, standardy jakości, narzędzia repo/CI, statusy obecne.
- Wyjścia: plan/przeglądy (kalendarz), przypisania owner/reviewer, checklisty, raporty statusu, lista zaległych dokumentów, archiwizacja/retencja.


## Założenia

- Repo dokumentacji i narzędzia CI/lint dostępne; ownerzy przypisani.


## Otwarte pytania

- Jakie raporty dla leadership/audytu? 
- Czy archiwizujemy wersje w dedykowanym repo lub systemie DMS?


## Powiązania (meta)

- Key Documents: documentation_standards, change_management, release_plan, compliance_calendar, audit_logging, versioning_guidelines.
- Key Document Structures: katalog, harmonogram, właściciele, checklisty, raporty.
- Document Dependencies: repo dokumentacji (git/wiki), CI/lint, narzędzia status/raporty, kalendarz release/changes, compliance calendar.


## Zależności dokumentu

Wymaga katalogu dokumentów z właścicielami i krytycznością, wymagań compliance, kalendarza release/changes, narzędzi repo/status. Bez tego DoR otwarte.


## Fazy cyklu życia

- Inwentaryzacja dokumentów i właścicieli.
- Ustalenie częstotliwości i kalendarza (compliance/release/ryzyko).
- Przeglądy/aktualizacje i zatwierdzenia.
- Raportowanie statusu i archiwizacja.
- Ciągłe doskonalenie (retro po audytach/incydentach).



## Struktura sekcji (szkielet)
- Cel i definicja sukcesu (KPI)
- Zakres, założenia i ograniczenia
- Interesariusze i role/RACI
- Kamienie milowe i daty
- Plan fal/sprintów z deliverables
- Zależności i ryzyka oraz plan mitigacji
- Budżet/zasoby i obłożenie
- Plan komunikacji i raportowania
- Kryteria akceptacji/go-live i plan rewizji
## Szybkie powiązania

- linkage_index.jsonl (docs/maintenance)
- documentation_standards, change_management, release_plan, compliance_calendar, audit_logging, versioning_guidelines


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

1. Uzupełnij katalog dokumentów, krytyczność, właścicieli i daty.
2. Zbuduj kalendarz przeglądów (cykliczny + triggery release/changes/compliance).
3. Włącz checklisty/CI/lint do procesu review; raportuj status.
4. Aktualizuj harmonogram po zmianach; domykaj DoR/DoD; dodaj do linkage_index.


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

- [Decyzja] Częstotliwości i krytyczność — uzasadnienie ryzyka/compliance.
- [Decyzja] Narzędzia/CI/lint — uzasadnienie automatyzacji i jakości.


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

- [ ] Katalog i daty aktualne; workflow opisany; raporty działają; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy dokument ma właściciela, datę kolejnego review, status.
- [ ] Każda overdue ma plan; relacje cross‑doc opisane.


## Artefakty powiązane

- Katalog, kalendarz, checklisty, raporty status, reguły CI/lint, archiwum.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Tech Writing/PMO → Security/Compliance → Owners → Audit/Owner sign‑off.


## Metryki jakości

- % dokumentów aktualnych, średnie overdue, czas review, liczba znalezionych błędów w review, zgodność z compliance (audyt).

## Kryteria ukończenia

- [ ] Harmonogram i procesy opisane; raportowanie/archiwizacja działa; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Katalog → Harmonogram/przypisania → Checklisty → Raporty/archiwizacja.
- Release/changes → Trigger przeglądów → Aktualizacja dokumentów.


## Struktura sekcji

1) Katalog dokumentów (typ, krytyczność, właściciel, ostatnia aktualizacja)  
2) Harmonogram przeglądów (częstotliwość, kalendarz, triggery release/changes/compliance)  
3) Role i odpowiedzialności (owner, reviewer, approver)  
4) Checklisty jakości i standardy (format, aktualność, linki, powiązania)  
5) Proces przeglądu/aktualizacji (workflow, narzędzia, CI/lint)  
6) Raportowanie statusu i eskalacje (zaległości, ryzyko)  
7) Archiwizacja/retencja i wersjonowanie  
8) Ryzyka, decyzje, open issues


## Wymagane rozwinięcia

- Katalog z krytycznością i datami przeglądu; kalendarz compliance/release.
- Checklisty jakości i definicja „aktualny” (data, linki, powiązania, testy/próby).
- Workflow przeglądu (owner→reviewer→approver), narzędzia (PR/CI/lint), raporty status.


## Wymagane streszczenia

- Podsumowanie krytycznych dokumentów i ich terminów, liczba zaległych, plan na najbliższy okres.


## Guidance (skrót)

- Trzymaj katalog i daty w jednym źródle; automatyzuj przypomnienia.
- Wiąż przeglądy z release/changes i compliance calendar.
- Używaj checklist i CI/lint do weryfikacji format/linków.
- Raportuj zaległości i ryzyko; eskaluj krytyczne dokumenty.


## Checklisty Definition of Ready (DoR)

- [ ] Katalog dokumentów i właściciele dostępni; wymagania compliance znane.
- [ ] Narzędzia repo/CI/lint i raportowania dostępne.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Harmonogram i role ustawione; checklisty i workflow opisane.
- [ ] Raportowanie/eskalacje i archiwizacja/wersjonowanie zdefiniowane.
- [ ] Dokument w linkage_index; wersja/data/właściciel aktualne.

