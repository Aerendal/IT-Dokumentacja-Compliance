---
title: Claims Processing Procedure
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Claims Processing Procedure


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać standardowy proces obsługi roszczeń (insurance/fintech/serwis), zapewniając zgodność, szybkość, jakość decyzji i dobrą komunikację z klientem.


## Zakres i granice

- Obejmuje: przyjęcie zgłoszenia (kanały), weryfikację danych i tożsamości, triage/prioritization, ocena i decyzja, wymagane dokumenty, fraud checks, kalkulację/wycenę, wypłatę/rozliczenie, odwołania, SLA/OLA, komunikację i statusy, audyt i raporty.  
- Poza zakresem: projekt produktowy polis (oddzielne dokumenty), pricing aktuaryjny.


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia

- Wejścia: dane zgłoszenia, dokumenty klienta, polis/umowa, reguły biznesowe, wyniki fraud/score, SLA, limity, kanały komunikacji.  
- Wyjścia: decyzja (approve/deny/partial), kwota i uzasadnienie, komunikaty do klienta, lista wyjątków/escalacji, checklisty DoR/DoD, log/audyt, raporty KPI.


## Założenia

- System claims, KYC i płatności dostępne.  
- Polityki danych i RODO/HIPAA przestrzegane.  
- Zespół ma zasoby do obsługi odwołań.


## Otwarte pytania

- Jak często kalibrować scoring fraud?  
- Jak raportować odwołania i wygrane/utracone?  
- Jak długo przechowywać dokumenty roszczeń?

## Powiązania (meta)

- Key Documents: risk_assessment, fraud_detection_playbook, data_protection_compliance, customer_communication_standards, sla_catalog, rollback_runbook (dla błędnych wypłat).  
- Key Document Structures: intake, weryfikacja, decyzja, wypłata, komunikacja, audyt.  
- Document Dependencies: claims system, KYC/identity, fraud/scoring, payment system, DMS, ticketing.


## Zależności dokumentu

Wymaga: reguł biznesowych i limitów, polityk fraud/KYC, dostępnych kanałów zgłoszeń, systemu claims, integracji płatności, wzorów komunikatów, SLA. Brak = brak DoR.


## Fazy cyklu życia

- Przyjęcie i rejestracja zgłoszenia.  
- Weryfikacja danych/identity i fraud checks.  
- Ocena/wycena i decyzja.  
- Wypłata/rozliczenie i komunikacja.  
- Odwołania i audyt/raporty.



## Struktura sekcji (szkielet)
- Cel i zakres
- Definicje i role/RACI
- Standardy/zasady i narzędzia
- Kroki procesu / checklisty
- Kryteria jakości/DoD i wyjątki
- Komunikacja i eskalacje
- Rejestr zmian i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (claims/processing/procedure)  
- fraud_detection_playbook, customer_communication_standards


## Mające zastosowanie standardy i normy


### Polskie normy i regulacje
- **KNF-REKOM-IT** — Rekomendacje KNF dot. systemów IT w sektorze finansowym
- **SOLVENCY2-PL** — Solvency II — Wymogi IT dla Ubezpieczycieli (implementacja PL)

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

1. Zdefiniuj wymagane dane i kanały intake.  
2. Skonfiguruj weryfikacje KYC/fraud; ustal reguły decyzji.  
3. Wdrażaj workflow w systemie claims; ustaw SLA i komunikaty.  
4. Monitoruj KPI, obsługuj odwołania; aktualizuj dokument i linkage_index.


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

- Intake: przyjęcie i rejestracja zgłoszenia.  
- 4-eyes: zasada podwójnej autoryzacji wypłat.  
- Time-to-decision: czas od zgłoszenia do decyzji.


## Przykłady użycia

- Roszczenia ubezpieczeń komunikacyjnych.  
- Zwroty w e-commerce z weryfikacją fraud.  
- Reklamacje serwisowe z wypłatą/kredytem.


## Ryzyka i ograniczenia

- Niekompletne dane → opóźnienia.  
- Fraud → straty finansowe.  
- Błędne wypłaty → chargebacks i niezadowolenie.  
- Brak audytu → ryzyko regulacyjne.


## Decyzje i uzasadnienia

- Progi fraud i eskalacji.  
- SLA i priorytety zgłoszeń.  
- Poziom automatyzacji decyzji.  
- Retencja logów i dokumentów.


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

- Intake ↔ Weryfikacja ↔ Decyzja ↔ Wypłata.  
- Fraud/KYC ↔ Decyzja ↔ Audyt.  
- SLA ↔ Komunikacja ↔ KPI.


## Struktura sekcji

1) Intake i kanały + wymagane dane  
2) Weryfikacja/KYC/fraud  
3) Ocena/wycena i reguły decyzji  
4) Wypłata/rozliczenie i kontrole  
5) Komunikacja/statusy i SLA  
6) Odwołania/escalacje  
7) Audyt, raporty, DoR/DoD  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Checklista danych i dokumentów na wejściu.  
- Reguły fraud i scoring; kiedy eskalować.  
- Szablony decyzji i komunikatów (approve/deny/partial).  
- Kontrole wypłaty (limity, 4-eyes, rollback).  
- KPI i raporty (time-to-decision, approval rate, NPS).  
- Procedura odwołań i SLA.


## Wymagane streszczenia

- Executive summary: SLA, top ryzyka, zmiany procesowe.  
- Skrót decyzji i odwołań (wolumen, przyczyny).


## Guidance (skrót)

- Zbieraj komplet danych na starcie; automatyzuj walidacje.  
- Oddziel decyzję od wypłaty; stosuj kontrole fraud.  
- Komunikuj statusy proaktywnie; jasne uzasadnienia decyzji.  
- Monitoruj KPI i wyjątki; ucz się z odwołań.  
- Dokumentuj i audytuj; aktualizuj linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Reguły biznesowe/limity i SLA dostępne.  
- [ ] Integracje KYC/fraud i płatności gotowe.  
- [ ] Szablony komunikatów i decyzji zatwierdzone.  
- [ ] Kanały intake skonfigurowane/testowane.  
- [ ] Procedura odwołań ustalona.


## Checklisty Definition of Done (DoD)

- [ ] Workflow działa end-to-end; testy i KPI w normie.  
- [ ] Komunikaty i logi/audyt kompletne.  
- [ ] Kontrole fraud/wypłat aktywne; wyjątki obsłużone.  
- [ ] Raporty uruchomione; linkage_index zaktualizowany.  
- [ ] Brak krytycznych defektów w procesie.

