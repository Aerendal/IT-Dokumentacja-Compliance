---
title: Procedury cutover
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Procedury cutover


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać standardowe kroki cutover między systemami/wersjami, by ograniczyć downtime i ryzyko oraz zapewnić gotowy rollback.


## Zakres i granice

- Obejmuje: przygotowanie (freeze, backup, walidacja środowisk, komunikacja), wykonanie (sekwencja kroków, role, Go/No-Go, okna zmian), walidację po (smoke/regresja, sanity danych, monitoring), rollback (warunki, kroki, czas decyzji), komunikację/koordynację (war room, status updates), dokumentację/log działań i lessons learned.  
- Poza zakresem: szczegółowe kroki specyficzne dla pojedynczej aplikacji (odsyłane do runbooków serwisowych).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: plan zmiany, lista systemów/wersji, okna zmian, backup/restore plan, testy pre-cutover, kontakty/role, status page/komunikacja.  
- Wyjścia: wykonany cutover lub rollback, log działań, wyniki walidacji, lessons learned/CAPA, aktualizacje runbooków, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: runbook_monitorowania, checklist_gotowosci_do_go_live, incident_response_playbook, backup_and_disaster_recovery, change_management_policy.  
- Key Document Structures: przygotowanie, wykonanie, walidacja, rollback, komunikacja, dokumentacja.  
- Document Dependencies: ticketing/CAB, status page, monitoring/APM, backup system, runbooki serwisowe.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Przygotowanie: cele, zakres, założenia.
- Planowanie: sekwencja prac, zasoby, daty.
- Realizacja: monitoring postępu, decyzje go/stop.
- Zamknięcie: retrospektywa, aktualizacja planów.
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

- linkage_index.jsonl (operations/cutover_procedure)  
- runbook_monitorowania, checklist_gotowosci_do_go_live, backup_and_disaster_recovery


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

1. Wypełnij przygotowanie i checkliste pre-cutover; uzyskaj zgody/okno zmian.  
2. Wykonaj kroki cutover z logiem działań; przeprowadź walidację i decyzję Go/No-Go.  
3. Jeśli rollback – wykonaj wg sekcji; po zakończeniu zrób lessons learned, zaktualizuj linkage_index.


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

- [ ] Backup/freeze i test rollback wykonane przed startem.  
- [ ] Go/No-Go kryteria spełnione lub rollback; komunikacja prowadzona.  
- [ ] Log działań i lessons learned uzupełnione; linkage_index aktualne.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Plan cutover, log działań, backup/restore evidencje, test rollback, wyniki walidacji, komunikaty, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Sukces cutover bez rollback, czas okna vs plan, liczba incydentów po cutover, czas decyzji Go/No-Go, % checklist pre/post wypełnionych, czas publikacji komunikatów.

## Kryteria ukończenia

- [ ] Cutover bezpiecznie przeprowadzony lub rollback, z kompletną walidacją i dokumentacją, powiązany w linkage_index.


## Struktura sekcji

1) Przygotowanie (freeze, backup, walidacja środowisk, checklista, komunikacja)  
2) Wykonanie (sekwencja kroków, role, Go/No-Go, okno zmian, timebox)  
3) Walidacja po (smoke/regresja, sanity danych, monitoring, kryteria akceptacji)  
4) Rollback (warunki, kroki, czas na decyzję, komunikacja, test rollback)  
5) Komunikacja i koordynacja (war room, status page, odbiorcy, częstotliwość update)  
6) Dokumentacja (log działań, timeline, wyniki, lessons learned, CAPA)  
7) Załączniki (checklisty pre/post, szablony komunikacji, ADR/waiver log)


## Wymagane rozwinięcia

- Szczegółowa checklista pre-cutover (backup/freeze/health checks) i post-cutover (smoke/regresja).  
- Matryca Go/No-Go z kryteriami i właścicielami decyzji; timebox na decyzję rollback.  
- Szablony komunikacji (start/update/closure, rollback) i lista odbiorców.  
- Procedura testu rollback przed oknem zmian; log działań + timestampy.  
- Plan CAPA i lessons learned po cutover.


## Wymagane streszczenia

- Executive: zakres cutover, ryzyka/mitigacje, plan rollback, okno zmian, status po walidacji.


## Guidance (skrót)

- Bez backup/freeze i przetestowanego rollbacku cutover nie startuje.  
- Ustal jasne Go/No-Go i timebox na decyzję; prowadź log działań w czasie rzeczywistym.  
- Walidacja: smoke + sanity danych + monitoring; jeśli wątpliwości – rollback.  
- Komunikuj cyklicznie (war room + status page); aktualizuj linkage_index po fakcie.


## Checklisty Definition of Ready (DoR)

- [ ] Backup/restore plan i test rollback dostępne; okno zmian i role potwierdzone.  
- [ ] Checklisty pre/post przygotowane; komunikacja/status page gotowe.


## Checklisty Definition of Done (DoD)

- [ ] Cutover/rollback wykonany, walidacja i log działań zakończone; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Lessons learned/CAPA spisane; checklisty DoR/DoD odhaczone.

