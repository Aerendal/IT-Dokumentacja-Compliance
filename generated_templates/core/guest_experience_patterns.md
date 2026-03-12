---
title: Guest Experience Patterns
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Guest Experience Patterns


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zebrać i ustandaryzować wzorce doświadczeń gościa (hotels/resorts/cruise/events): podróż gościa end-to-end, kluczowe momenty prawdy, integracje i standardy, aby podnieść satysfakcję i spójność usług.


## Zakres i granice

- Obejmuje: pre-arrival (rezerwacja, preferencje), check-in/out (mobile/kiosk/front desk), pobyt (usługi, housekeeping, F&B, spa), komunikację (app/SMS/chat), personalizację (profil/loyalty), płatności/napiwki, feedback/NPS, eskalacje, dostępność (ADA/WCAG), bezpieczeństwo danych/PCI.  
- Poza zakresem: operacje zaplecza kuchni/maintenance (oddzielne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: journey map, persona gościa, standardy marki, systemy PMS/POS/loyalty, kanały komunikacji, KPI (NPS, CSAT, upsell), polityki RODO/PCI.  
- Wyjścia: katalog wzorców i flow, wymagania systemowe/integracyjne, checklisty DoR/DoD, scenariusze szkoleniowe, KPI i metryki monitoringu.


## Założenia

- Systemy PMS/POS/loyalty dostępne i integrowalne.  
- Goście mają urządzenia mobilne dla kluczowych touchpointów.  
- Zespół obsługi jest szkolony.


## Otwarte pytania

- Jak obsłużyć gości bez smartfonów?  
- Jak długo przechowywać preferencje i historię?  
- Czy wymagane są lokalne regulacje dla komunikacji marketingowej?

## Powiązania (meta)

- Key Documents: customer_service_training, payment_card_security_pci_dss, accessibility_improvement_plan, marketing_automation_playbook, incident_response_for_customers.  
- Key Document Structures: journey, touchpoints, personalizacja, płatności, komunikacja, feedback.  
- Document Dependencies: PMS, POS, loyalty/CRM, messaging platform, analytics, access control.


## Zależności dokumentu

Wymaga: mapy podróży gościa, standardów marki, dostępnych integracji (PMS/POS/loyalty), polityk RODO/PCI, planu komunikacji i dostępności. Brak = brak DoR.


## Fazy cyklu życia

- Definicja journey i touchpointów.  
- Projekt wzorców i wymagań systemowych.  
- Implementacja i szkolenia.  
- Monitoring KPI i poprawki.  
- Retrospektywy i aktualizacja wzorców.



## Struktura sekcji (szkielet)
- Streszczenie i wizja
- Diagnoza stanu i kontekst
- Cele i KPI
- Filar/priorytety i inicjatywy
- Horyzonty/roadmapa i zależności
- Ryzyka i założenia
- Governance, finansowanie i raportowanie
## Szybkie powiązania

- linkage_index.jsonl (guest/experience/patterns)  
- customer_service_training, payment_card_security_pci_dss


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

1. Zmapuj journey i priorytetowe touchpointy.  
2. Wybierz wzorce i wymagania systemowe; zapisz w backlogu.  
3. Wdroż i przeszkol obsługę; monitoruj KPI.  
4. Zbieraj feedback; aktualizuj wzorce i linkage_index.


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

- PMS: Property Management System.  
- NPS/CSAT: metryki satysfakcji.  
- Touchpoint: punkt styku gościa z usługą.


## Przykłady użycia

- Wzorzec mobile check-in z cyfrowym kluczem.  
- Pre-arrival upsell (pokój wyższej kategorii, spa).  
- Feedback po wymeldowaniu z eskalacją negatywnych opinii.


## Ryzyka i ograniczenia

- Silosy danych → niespójna personalizacja.  
- Brak dostępności → wykluczenie gości.  
- Problemy płatności → straty i niezadowolenie.  
- Brak feedback loop → brak ulepszeń.


## Decyzje i uzasadnienia

- Kanały komunikacji i opt-in.  
- Zakres personalizacji vs prywatność.  
- KPI priorytetowe i progi alertów.  
- Standardy dostępności dla aplikacji i kiosków.


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

- Journey ↔ Touchpoints ↔ Komunikacja.  
- Personalizacja ↔ Systemy (PMS/POS/loyalty) ↔ Płatności.  
- Feedback ↔ KPI ↔ Usprawnienia.


## Struktura sekcji

1) Journey i persony gości  
2) Wzorce touchpointów (pre-arrival, check-in/out, pobyt)  
3) Komunikacja i personalizacja (app/chat/loyalty)  
4) Płatności/PCI i napiwki  
5) Feedback/NPS i eskalacje  
6) Dostępność (ADA/WCAG) i bezpieczeństwo danych  
7) KPI i monitoring  
8) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Szablony flow dla pre-arrival/check-in/out.  
- Reguły personalizacji (preferencje, upsell).  
- Polityki komunikacji i SLA odpowiedzi.  
- Checklisty dostępności (mobile/web/kiosk).  
- Raporty KPI (NPS, CSAT, upsell, response time).  
- Scenariusze szkoleniowe dla obsługi.


## Wymagane streszczenia

- Executive summary: kluczowe wzorce i KPI.  
- Skrót polityk komunikacji i dostępności.


## Guidance (skrót)

- Utrzymuj jeden profil gościa; synchronizuj PMS/POS/loyalty.  
- Zapewnij bezproblemowy check-in/out (mobile/kiosk).  
- Komunikuj proaktywnie (opóźnienia, oferty) z jasnym opt-in.  
- Chroń dane i płatności (PCI, minimalizacja PII).  
- Mierz NPS/CSAT po kluczowych touchpointach; iteruj.  
- Aktualizuj linkage_index po zmianach wzorców.


## Checklisty Definition of Ready (DoR)

- [ ] Journey map i persony gotowe.  
- [ ] Integracje PMS/POS/loyalty dostępne.  
- [ ] Polityki RODO/PCI i dostępności znane.  
- [ ] KPI i sposób pomiaru ustalone.  
- [ ] Materiały szkoleniowe przygotowane.


## Checklisty Definition of Done (DoD)

- [ ] Wzorce wdrożone; KPI w normie lub plan działań.  
- [ ] Komunikacja działa; opt-in/opt-out obsłużone.  
- [ ] Dostępność zweryfikowana; wyjątki zatwierdzone.  
- [ ] Raport KPI opublikowany; linkage_index zaktualizowany.  
- [ ] Feedback przeanalizowany; backlog zaktualizowany.

