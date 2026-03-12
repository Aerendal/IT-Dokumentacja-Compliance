---
title: Donor CRM Design
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Donor CRM Design


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaprojektować CRM dla darczyńców: pozyskanie, segmentacja, komunikacja, obsługa płatności i zgodność, aby zwiększyć retencję i wartość darowizn przy pełnej audytowalności.


## Zakres i granice

- Obejmuje: model danych darczyńców i darowizn, wielokanałowe touchpointy (email/SMS/telefon/event), płatności i rozliczenia (jednorazowe/subscription), segmentację i scoring, kampanie i automatyzacje, raporty KPI (LTV, churn, conversion), integracje (payment gateway, marketing, księgowość), zgodność (RODO/PCI), bezpieczeństwo i dostęp.  
- Poza zakresem: strategia fundraisingu (osobny dokument), szczegółowe treści kampanii.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania fundraisingu, polityki RODO/PCI, listy kanałów, schematy płatności, raporty KPI, integracje istniejące, role i uprawnienia.  
- Wyjścia: architektura CRM, model danych, integracje i API, plan migracji danych, konfiguracja kampanii i automatyzacji, checklisty DoR/DoD, runbooki operacyjne.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: data_protection_compliance, payment_card_security_pci_dss, marketing_automation_playbook, access_control_policy, rollback_runbook, incident_response_for_customers.  
- Key Document Structures: dane, płatności, segmentacja, kampanie, raporty, bezpieczeństwo.  
- Document Dependencies: payment gateway, email/SMS provider, data warehouse/BI, accounting/ERP, marketing tools.


## Zależności dokumentu

Wymaga: zatwierdzonych kanałów i procesów płatności, polityk RODO/PCI, integracji z płatnościami i mailingiem, listy ról/uprawnień, planu migracji danych. Brak = brak DoR.


## Fazy cyklu życia

- Analiza i model danych.  
- Projekt integracji i płatności.  
- Konfiguracja kampanii i automatyzacji.  
- Migracja danych i testy.  
- Operacje/monitoring i ulepszenia.



## Struktura sekcji (szkielet)
- Cel i zakres
- Definicje i role/RACI
- Standardy/zasady i narzędzia
- Kroki procesu / checklisty
- Kryteria jakości/DoD i wyjątki
- Komunikacja i eskalacje
- Rejestr zmian i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (donor/crm/design)  
- payment_card_security_pci_dss, marketing_automation_playbook


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

1. Zbierz wymagania i dane; zaprojektuj model i płatności.  
2. Skonfiguruj integracje i kampanie; przygotuj migrację.  
3. Wdróż, przetestuj (płatności, RODO/PCI, raporty).  
4. Uruchom operacje; monitoruj KPI; aktualizuj dokument/linkage_index.


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

- Dane ↔ Płatności ↔ Raporty KPI.  
- Segmentacja ↔ Kampanie ↔ Automatyzacja.  
- Bezpieczeństwo ↔ Dostęp ↔ Zgodność.


## Struktura sekcji

1) Model danych (darczyńca, darowizna, kampania, zgody)  
2) Płatności i rozliczenia (jednorazowe/subscription, PCI)  
3) Segmentacja i scoring (RFM/LTV)  
4) Kampanie i automatyzacja (journeys, trigger)  
5) Raporty/KPI i dashboardy  
6) Bezpieczeństwo/RODO/PCI, role i dostęp  
7) Migracja danych i testy  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Schemat danych i API (darczyńcy, transakcje, zgody).  
- Flow płatności i wyjątki (chargeback, refund, nieudane).  
- Definicje segmentów i scoringu; reguły automatyzacji.  
- Szablony raportów (LTV, churn, conversion, retention).  
- Matryca ról i uprawnień; logi audytowe.  
- Plan migracji danych i walidacja jakości.


## Wymagane streszczenia

- Executive summary: zakres, kanały, płatności, ryzyka.  
- Skrót KPI i definicji segmentów.


## Guidance (skrót)

- Projektuj RODO/PCI-first: minimalizuj PII, szyfruj, tokenizuj płatności.  
- Wymuś unikalny donor ID; konsoliduj duplikaty.  
- Automatyzuj kampanie na podstawie segmentów i scoringu.  
- Monitoruj LTV, churn, conversion; iteruj kampanie.  
- Loguj audyt i anomalie płatności; miej rollback plan.  
- Aktualizuj linkage_index po releasach.


## Checklisty Definition of Ready (DoR)

- [ ] Polityki RODO/PCI i kanały płatności zatwierdzone.  
- [ ] Model danych i unikalny donor ID zdefiniowane.  
***
