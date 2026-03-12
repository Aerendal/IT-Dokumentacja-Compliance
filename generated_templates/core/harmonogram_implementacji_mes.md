---
title: Harmonogram implementacji MES
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Harmonogram implementacji MES


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaplanować wdrożenie MES: etapy i kolejność linii/zakładów, integracje OT/IT, testy/UAT, szkolenia, cutover/rollback oraz komunikację z produkcją.


## Zakres i granice

- Obejmuje: zakres linii/obszarów i modułów MES, etapy (pilot → linia 1 → kolejne linie), integracje (SCADA/PLC, ERP, QMS, WMS), testy/UAT/validacja danych, szkolenia operatorów, cutover/okna produkcyjne, rollback, ryzyka/mitigacje, komunikację.  
- Poza zakresem: projekt szczegółowy MES (osobne specy) i modernizacja sprzętu OT.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: lista linii/zakładów i modułów MES, stan integracji SCADA/PLC/ERP/QMS/WMS, okna produkcyjne, zasoby projektowe, polityki jakości/bezpieczeństwa, plan zmian, ryzyka OT.  
- Wyjścia: harmonogram fal rollout, mapa integracji i zależności, plan testów/UAT, plan szkoleń, plan cutover/rollback, plan komunikacji, lista ryzyk i mitigacji.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: mes_architecture, scada_integration_plan, erp_integration_plan, qms_integration_plan, wms_integration_plan, change_management_plan, communication_plan, risk_register, disaster_recovery_plan (ot), safety_guidelines.
- Key Document Structures: etapy/fale, integracje, testy/UAT, szkolenia, cutover/rollback, ryzyka/komunikacja.
- Document Dependencies: SCADA/PLC, ERP/QMS/WMS, OT network, historians, data quality, training resources, on-site windows.



## Zależności dokumentu

- Konsumuje: [dokumenty wejściowe — co musi istnieć zanim ten dokument powstanie]
- Dostarcza do: [dokumenty wyjściowe — co korzysta z tego dokumentu]

## Fazy cyklu życia

- Faza 1: Koncepcja i Wizja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 2: Analiza Wymagań: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 3: Projekt / Design: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 4: Planowanie: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 5: Implementacja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 6: Testowanie / QA: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 7: Bezpieczeństwo / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 8: Wdrożenie / Deployment: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 9: Operacje / Maintenance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)

- Cele i zakres
- Kamienie milowe i terminy
- Zasoby i odpowiedzialności
- Zależności
- Ryzyka
- Status i postęp

## Szybkie powiązania

- linkage_index.jsonl (mes/implementation_schedule)
- mes_architecture, scada_integration_plan, erp_integration_plan, qms_integration_plan, wms_integration_plan, change_management_plan, communication_plan, risk_register, disaster_recovery_plan (ot), safety_guidelines


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

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

1. Wypisz fale rollout, integracje i readiness; przypisz daty/ownerów.  
2. Zaplanuj testy/UAT, szkolenia, cutover/rollback i komunikację.  
3. Aktualizuj postęp, ryzyka i decyzje go/conditional/no‑go; zamknij DoR/DoD i linkage_index.


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

- [ ] Priorytety i zależności uwzględnione; kryteria go/rollback opisane; komunikacja prowadzona.  
- [ ] Testy/UAT/szkolenia wykonane przed go-live; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Gantt/CSV, readiness checklist, integracje mapy, test/UAT plan, training plan, cutover/rollback runbook, komunikacja, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % linii uruchomionych, powodzenie integracji/testów, liczba rollbacków, liczba waiverów i czas sunset, czas przestoju podczas cutover.

## Kryteria ukończenia

- [ ] Harmonogram MES wykonany/aktualny, decyzje i ryzyka udokumentowane; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres linii/obszarów i modułów MES; kolejność rollout (fale)  
2) Etapy i daty (pilot, linia 1, kolejne linie/zakłady) z ownerami  
3) Integracje (SCADA/PLC, ERP, QMS, WMS), zależności i readiness checklist  
4) Testy/UAT/validacja danych, szkolenia operatorów i SOP aktualizacje  
5) Cutover i okna produkcyjne; rollback/plan B; kryteria go/conditional/no‑go  
6) Ryzyka i mitigacje; komunikacja z produkcją i change management  
7) Załączniki (Gantt/CSV, readiness checklist, test/UAT plan, training plan, cutover/rollback runbook)


## Wymagane rozwinięcia

- Lista linii/zakładów z priorytetem; readiness SCADA/PLC/ERP/QMS/WMS; okna produkcyjne.  
- Kryteria go/no‑go per fala; plan cutover/rollback; plan testów/UAT i danych.  
- Plan szkoleń (kto, kiedy, materiały, SOP) i komunikacja z produkcją.


## Wymagane streszczenia

- Executive: status fal, kluczowe integracje i ryzyka OT, najbliższe cutover, plan rollback.


## Guidance (skrót)

- Pilot na jednej linii, potem rollout falami; każda fala ma readiness checklist.  
- Integracje OT/IT są krytyczne: weryfikuj SCADA/PLC readiness i dane.  
- Plan cutover/rollback i okna produkcyjne uzgodnij z produkcją i bezpieczeństwem.  
- Szkolenia operatorów i aktualizacja SOP obowiązkowe przed go-live.


## Checklisty Definition of Ready (DoR)

- [ ] Lista linii/zakładów i modułów; readiness integracji wstępnie oceniona; okna prod znane.  
- [ ] Plan testów/UAT i szkoleń zarysowany; cutover/rollback szkic; komunikacja ustalona.


## Checklisty Definition of Done (DoD)

- [ ] Fale rollout wykonane; integracje/testy/UAT/szkolenia zrealizowane; cutover/rollback przeprowadzone lub gotowe; ryzyka i waivery z sunset; dokument w linkage_index; metadane aktualne.

