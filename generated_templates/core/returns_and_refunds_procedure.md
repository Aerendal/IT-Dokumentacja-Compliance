---
title: Returns and Refunds Procedure
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Returns and Refunds Procedure


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje procedurę zwrotów i refundacji: zgłoszenie, weryfikacja, logistyka, decyzje, płatność i komunikacja. Ma zapewnić zgodność, szybkość i dobrą obsługę klienta.


## Zakres i granice

- Obejmuje: kanały zgłoszeń (web/app/support), typy zwrotów (defekt, odstąpienie, SLA), polityki czasu/warunków, weryfikację dowodów, autoryzację RMA, logistykę (etykiety, pickup, magazyn), inspekcję, decyzję (refund/replacement/store credit), metody refundacji i terminy, komunikację z klientem, fraud checks, księgowanie i audyt, metryki (cycle time, NPS/CSAT, koszt).  
- Poza zakresem: polityka cen/promocji; chargebacky kartowe (link do osobnego runbooka).


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia

- Wejścia: polityka zwrotów, warunki prawne (konsumenckie), dane zamówienia/płatności, dowody (zdjęcia, logi), SLA logistyczne, reguły fraud, dane magazynu.  
- Wyjścia: decyzja zwrotu, etykieta/pickup, statusy i komunikaty, zlecenie refundacji, noty księgowe, raporty KPI i wyjątki, checklisty DoR/DoD.


## Założenia

- Integracje z PSP/WMS/CRM działają.  
- Polityka zwrotów zgodna z prawem lokalnym.  
- Zespół support/warehouse dostępny.


## Otwarte pytania

- Jak obsłużyć cross‑border VAT/cła w zwrotach?  
- Jakie progi alertów przy spike zwrotów?  
- Czy oferować instant refund/store credit?


## Powiązania (meta)

- Key Documents: return_policy, payment_reliability_runbook, warehouse_intake_procedure, fraud_detection_strategy, customer_communication_templates, accounting_policy.  
- Key Document Structures: zgłoszenie, weryfikacja, logistyka, decyzja, refundacja, raporty.  
- Document Dependencies: order system, payments/PSP, warehouse/WMS, ticketing/CRM, fraud engine, accounting/ERP.


## Zależności dokumentu

Wymaga: polityki zwrotów i warunków prawnych, danych zamówienia/płatności, integracji z PSP/WMS, szablonów komunikacji, reguł fraud i SLA logistycznych. Braki = DoR otwarte.


## Fazy cyklu życia

- Przyjęcie zgłoszenia i wstępna weryfikacja.  
- Autoryzacja RMA i logistyka zwrotu.  
- Inspekcja i decyzja.  
- Refundacja/wykonanie, księgowanie i raport.  
- Retro i ulepszenia procesu.



## Struktura sekcji (szkielet)
- Cel, zakres i definicje sukcesu
- Trigger/scenariusze i preconditions
- Role, uprawnienia i narzędzia
- Kroki operacyjne (checklista) z walidacją
- Monitoring i dowody wykonania
- Rollback/contingency oraz komunikacja/escalacja
- Rejestr zmian runbooka
## Szybkie powiązania

- linkage_index.jsonl (returns/and/refunds/procedure)  
- return_policy, payment_reliability_runbook, warehouse_intake_procedure, fraud_detection_strategy


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

1. Przyjmij zgłoszenie, wykonaj weryfikację/fraud; nadaj RMA.  
2. Zorganizuj logistykę i inspekcję; podejmij decyzję.  
3. Zrealizuj refundację/replacement, wyślij komunikaty; raportuj KPI; aktualizuj DoR/DoD i linkage_index.


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

- RMA: autoryzacja zwrotu.  
- Chargeback: spór kartowy (osobny proces).  
- Cycle time: czas od zgłoszenia do refundacji.


## Przykłady użycia

- Zwrot z powodu defektu i wymiana.  
- Odstąpienie w ciągu 14/30 dni i refundacja.  
- Zwrot flagowany przez fraud engine.


## Ryzyka i ograniczenia

- Nadużycia (fraud, friendly fraud).  
- Opóźnienia logistyczne → niezadowolenie.  
- Niepełne logi → problemy audytowe.


## Decyzje i uzasadnienia

- Warunki kwalifikacji zwrotów.  
- Priorytety decyzji refund/credit/replacement.  
- SLA i kanały komunikacji.


## Powiązania z innymi dokumentami

- return_policy — warunki.  
- payment_reliability_runbook — kanały refundacji.  
- warehouse_intake_procedure — inspekcja i logistyczne przyjęcie.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Prawo konsumenckie lokalne, polityki księgowe i podatkowe.  
- Wewnętrzne standardy bezpieczeństwa danych klientów.

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

- Zgłoszenie → Weryfikacja → Decyzja → Refundacja.  
- Logistyka → Inspekcja → Decyzja.  
- Fraud checks → Decyzja/wyjątki → Raporty.


## Struktura sekcji

1) Zakres i warunki zwrotów (czas, typy, wyjątki)  
2) Proces zgłoszenia i weryfikacji (dowody, fraud, SLA)  
3) Autoryzacja i logistyka (RMA, etykiety, pickup/ship)  
4) Inspekcja i decyzja (refund/replacement/credit)  
5) Płatność/refundacja (metody, terminy, statusy)  
6) Komunikacja z klientem (szablony, kanały, SLA)  
7) Raportowanie i metryki (cycle time, CSAT/NPS, koszt, wyjątki)  
8) Compliance i audyt (dane, księgowość, prawo konsumenckie)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Flow dla głównych typów zwrotów; SLA per etap.  
- Szablony komunikacji i statusy.  
- Tabela metod refundacji i terminy.  
- Checklisty inspekcji i fraud checks.


## Wymagane streszczenia

- Executive snapshot: liczba zwrotów, cycle time, top przyczyny, koszt.  
- Karta SLA/komunikacja dla supportu.


## Guidance (skrót)

- Jasno komunikuj warunki i statusy; redukuj kontakt do supportu.  
- Ustal SLA per etap; automatyzuj etykiety i statusy.  
- Spójne kryteria inspekcji i fraud checks.  
- Refunduj tym samym kanałem gdy możliwe; loguj wszystko dla audytu.  
- Analizuj przyczyny zwrotów i usprawniaj produkt/logistykę.


## Checklisty Definition of Ready (DoR)

- [ ] Zamówienie/płatność zweryfikowane; warunki spełnione.  
- [ ] Fraudy/reguły i wymagane dowody sprawdzone.  
- [ ] Kanał refundacji i SLA znane.  
- [ ] Etykieta/pickup zorganizowane.  
- [ ] Komunikacja i statusy przygotowane.


## Checklisty Definition of Done (DoD)

- [ ] Zwrot/inspekcja zakończone; decyzja udokumentowana.  
- [ ] Refundacja/wykonanie rozliczone; status/wersja/data uzupełnione.  
- [ ] Komunikaty wysłane; księgowość i audyt zaktualizowane.  
- [ ] Raport KPI/wyjątki opublikowany; linkage_index uzupełniony.  
- [ ] Lessons learned i przyczyny zwrotów odnotowane.

