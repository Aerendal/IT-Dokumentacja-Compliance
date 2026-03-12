---
title: Donation Tracking
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Donation Tracking


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje, jak zbierać, rejestrować i raportować darowizny: źródła, waluty, kanały, compliance, przejrzystość dla darczyńców i audytów. Ma minimalizować ryzyko błędów, fraudu i niespójności raportów.


## Zakres i granice

- Obejmuje: kanały darowizn (online/offline/partners), waluty i kursy, identyfikację darczyńców (anonimowi vs KYC), przypisanie celów/funduszy, metadane (kampania, źródło), płatności i potwierdzenia, reconciliację z PSP/banami, podatki/ulgi, raporty (finansowe, donors, regulatorzy), RODO/PII, kontrolę fraud.  
- Poza zakresem: plan kampanii fundraising (osobny dokument), zarządzanie grantami (oddzielne).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: źródła danych (PSP/bank CSV/API), formularze darczyńców, kursy walut, listy kampanii i funduszy, polityki RODO/AML/KYC, konfiguracja potwierdzeń, wymagania audytu/podatków.  
- Wyjścia: znormalizowany rejestr darowizn, raporty (dzienny/miesięczny/roczny), potwierdzenia/rachunki, pliki dla księgowości/podatków, alerty anomalii, checklisty DoR/DoD.


## Założenia

- Dostępne API/eksporty PSP/bank.  
- Polityki AML/RODO obowiązują.  
- Zespół finansów współpracuje z IT.


## Otwarte pytania

- Jak obsłużyć chargeback/refund darowizn?  
- Czy wymagane są certyfikaty darowizn w formie papierowej?  
- Jak długo przechowywać PII darczyńców?


## Powiązania (meta)

- Key Documents: fundraising_policy, aml_kyc_policy, privacy_policy, reconciliation_runbook, tax_receipt_template, donor_communication_plan.  
- Key Document Structures: kanały, waluty, KYC, reconciliacja, raporty, bezpieczeństwo, komunikacja.  
- Document Dependencies: PSP/bank API, CRM/donor DB, accounting/ERP, FX rates, email service, antifraud tools.


## Zależności dokumentu

Wymaga: dostępów do PSP/bank danych, list kampanii/funduszy, polityk KYC/RODO/AML, wzorców potwierdzeń podatkowych, harmonogramu raportów. Braki = DoR otwarte.


## Fazy cyklu życia

- Ustalenie źródeł/kanałów i modeli danych.  
- Implementacja rejestru i reconciliacji.  
- Operacje i raportowanie; audyty.  
- Ulepszenia (fraud, komunikacja, raporty).



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

- linkage_index.jsonl (donation/tracking)  
- fundraising_policy, aml_kyc_policy, reconciliation_runbook, tax_receipt_template


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

1. Zbierz kanały/źródła i skonfiguruj rejestr; zdefiniuj model danych.  
2. Ustaw reconciliację, potwierdzenia i raporty; uruchom monitoring anomalii.  
3. Prowadź raporty i audyty; aktualizuj DoR/DoD i linkage_index.


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

- Reconciliacja: uzgadnianie zapisów systemu z PSP/bank.  
- Donor ID: identyfikator darczyńcy (może być anonimowy).  
- AML/KYC: obowiązki przeciwdziałania praniu pieniędzy i weryfikacji darczyńców.


## Przykłady użycia

- Kampania online multi‑currency.  
- Darowizny offline z późniejszym importem i reconciliacją.  
- Alert na duże/niecodzienne darowizny (AML).


## Ryzyka i ograniczenia

- Rozbieżności PSP/bank → brak zaufania/raporty błędne.  
- Brak KYC/AML → ryzyko prawne.  
- Ujawnienie PII → naruszenia privacy.


## Decyzje i uzasadnienia

- Poziom agregacji raportów (fundusz/kampania/rynek).  
- Częstotliwość reconciliacji i alertów.  
- Zakres danych donorów (minimalizacja).


## Powiązania z innymi dokumentami

- aml_kyc_policy — KYC/AML.  
- reconciliation_runbook — uzgodnienia.  
- tax_receipt_template — potwierdzenia.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Regulacje AML/KYC, RODO/PII, lokalne przepisy podatkowe dot. darowizn.  
- Wewnętrzne polityki bezpieczeństwa danych i finansów.

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

- Kanały/waluty → Rejestr → Reconciliacja → Raporty.  
- KYC/AML → Identyfikacja → Raporty regulatora.  
- Anomalie → Alerty → Korekty/antifraud.


## Struktura sekcji

1) Zakres i cele (przejrzystość, compliance)  
2) Kanały i dane wejściowe (PSP/bank/offline, waluty, kampanie)  
3) Model danych darowizn i identyfikacja darczyńcy (PII/KYC/anonim)  
4) Rejestr i reconciliacja (PSP/bank → system)  
5) Potwierdzenia/rachunki i komunikacja (e‑mail/pdf, donor care)  
6) Raportowanie i podatki (finanse, donors, regulator)  
7) Bezpieczeństwo/RODO/AML/KYC i antifraud  
8) Alerty i monitoring anomalii  
9) Operacje i przeglądy (harmonogram, SLA, audyt)  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Schemat rejestru darowizn (pola, waluty, kampania, fundusz, donor ID).  
- Procedura reconciliacji (źródło → system) i wzorce niezgodności.  
- Szablony potwierdzeń/rachunków i polityka czasu wysyłki.  
- Raporty obowiązkowe (regulator/podatki/donors) i harmonogram.


## Wymagane streszczenia

- Executive snapshot: kwoty per fundusz/kampania, anon vs KYC, anomalie.  
- Krótki raport reconciliacji (zgodności/rozbieżności).


## Guidance (skrót)

- Normalizuj waluty i pola; trzymaj jedną prawdę o darowiźnie.  
- Reconciliuj regularnie; automatyzuj alerty anomalii.  
- Szanuj privacy: minimalizuj PII, szyfruj, stosuj retencję.  
- Utrzymuj transparentność dla darczyńców (potwierdzenia, raporty).  
- Dokumentuj wyjątki i korekty.


## Checklisty Definition of Ready (DoR)

- [ ] Dostępy do PSP/bank i listy kampanii/funduszy.  
- [ ] Polityki AML/KYC/RODO i szablony potwierdzeń dostępne.  
- [ ] Model danych darowizn uzgodniony.  
- [ ] Harmonogram raportów i wymogi regulatora znane.  
- [ ] Narzędzia antyfraud/alerty dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Rejestr darowizn działa; reconciliacja przechodzi.  
- [ ] Potwierdzenia/rachunki wysyłane; PII zabezpieczone.  
- [ ] Raporty finansowe/donor/regulator opublikowane; status/wersja/data uzupełnione.  
- [ ] Alerty anomalii aktywne; korekty udokumentowane.  
- [ ] Linkage_index i risk register zaktualizowane.

