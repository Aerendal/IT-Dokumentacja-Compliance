---
title: Reagowanie na problemy z BOPIS
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Reagowanie na problemy z BOPIS


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Szybko rozwiązywać problemy z usługą BOPIS (Buy Online, Pick-up In Store) minimalizując wpływ na klientów i sklepy.


## Zakres i granice

- Obejmuje: detekcję błędów zamówień/opóźnień/braków stocku, triage per kanał/sklep/status, stabilizację (rezerwacje manualne, alternatywne sklepy, komunikaty), naprawę (sync stock/płatności/powiadomienia), komunikację (klienci/sklepy/support), postmortem i poprawki procesowe/IT.  
- Poza zakresem: pełny design BOPIS (osobny dokument), polityki zwrotów (osobno).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: alerty/order error rate, logi OMS/POS/WMS, status kanałów, stany magazynowe, płatności/refundy, powiadomienia, SLA lead time.  
- Wyjścia: decyzje stabilizacyjne, lista zamówień dotkniętych i akcje (manual/alternatywa/refund), komunikaty do klientów/sklepów, root cause i CAPA, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: obsluga_incydentow_rate_limit, api_rate_limiting_requirements, logging_strategy, checklist_gotowosci_do_go_live, incident_response_playbook.  
- Key Document Structures: detekcja, triage, stabilizacja, naprawa, komunikacja, postmortem.  
- Document Dependencies: OMS/OMS API, POS, WMS, payment gateway, notification service, status page.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (retail/bopis_response)  
- incident_response_playbook, logging_strategy, api_rate_limiting_requirements


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

1. Zidentyfikuj zakres problemu (kanał/sklep/status); włącz checklistę stabilizacji.  
2. Napraw przyczyny (sync/płatności/powiadomienia); komunikuj do klientów/sklepów.  
3. Wykonaj postmortem/CAPA; zaktualizuj linkage_index i checklisty.


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

- [ ] Zamówienia zabezpieczone (manual/alternatywa/refund); sync/płatności/powiadomienia działają.  
- [ ] Komunikacja do klientów/sklepów wykonana; linkage_index uzupełniony.  
- [ ] CAPA z ownerami/terminami; testy/regresje potwierdzają fix.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Raport zamówień dotkniętych, logi OMS/POS/WMS, szablony komunikacji, CAPA lista, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Liczba zamówień dotkniętych, czas stabilizacji, czas do komunikacji do klienta, sukces rate retry płatności/sync, liczba powtórzeń tego samego problemu.

## Kryteria ukończenia

- [ ] Runbook reakcji na problemy BOPIS gotowy do użycia i powiązany w linkage_index.


## Struktura sekcji

1) Detekcja (metryki: order error rate, SLA pickup, brak stock; alerty)  
2) Triage (kanał, sklep, status zamówień, segment VIP, wpływ)  
3) Stabilizacja (manual reserve, alternatywny sklep, throttling/kolejka, komunikaty ETA)  
4) Naprawa (sync stock, retry płatności, ponowne powiadomienia, fix integracji)  
5) Komunikacja (klienci: ETA/refund; sklepy: instrukcje; support: FAQ)  
6) Postmortem i korekty (root cause, CAPA, testy/regresje, update runbooków)  
7) Załączniki (checklisty, szablony komunikatów, ADR/waiver log)


## Wymagane rozwinięcia

- Progi alertów i routing (on-call retail/OMS).  
- Checklisty stabilizacji (manual reserve, alternatywny sklep, refund/kupon).  
- Szablony komunikacji (SMS/email/push/status page).  
- Matryca RCA (stock sync, płatność, powiadomienia, integracje).  
- Plan testów/regresji po poprawkach.


## Wymagane streszczenia

- Executive: wpływ (liczba zamówień, sklepy, kanały), root cause, podjęte akcje, CAPA i terminy.


## Guidance (skrót)

- Najpierw zabezpiecz zamówienia klientów (manual/alternatywa) i komunikuj ETA; potem napraw integracje.  
- Monitoruj sync stock i płatności; zapewnij idempotencję i retry.  
- Utrzymuj szablony komunikacji gotowe; aktualizuj linkage_index i runbooki po incydencie.


## Checklisty Definition of Ready (DoR)

- [ ] Alerty/metryki BOPIS działają; logi OMS/POS/WMS dostępne.  
- [ ] Szablony komunikacji i procedury manual reserve przygotowane.


## Checklisty Definition of Done (DoD)

- [ ] Stabilizacja wykonana; przyczyna usunięta; komunikacja zrobiona; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] CAPA i testy/regresje zaplanowane/wykonane; checklisty DoR/DoD odhaczone.

