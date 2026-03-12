---
title: Property Management Architecture
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Property Management Architecture


## Metadane

- Właściciel: Solution Architect
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje architekturę systemu zarządzania nieruchomościami (Property Management): moduły, dane, integracje, bezpieczeństwo, zgodność i operacje. Celem jest spójność i skalowalność platformy dla portfela nieruchomości.


## Zakres i granice

- Obejmuje: moduły (portfolio, najemcy, czynsze, faktury, utrzymanie/CMMS, inspekcje, raporty finansowe), kanały (portal najemcy/właściciela/mobilne), integracje (ERP/księgowość, płatności, GIS, IoT/utility meters, CRM, e‑signature), dane (umowy, płatności, zużycie mediów, zgłoszenia), bezpieczeństwo/PII (dane najemców), zgodność (RODO, lokalne przepisy najmu), SLA i dostępność, raportowanie i analitykę, zarządzanie dokumentami, audyt, DR/BCP.  
- Poza zakresem: polityki cenowe i strategie inwestycyjne (oddzielne dokumenty).


## Użytkownicy i interesariusze
- **Solution / Enterprise Architect** — projektuje i zatwierdza architekturę
- **Tech Lead** — odpowiada za spójność techniczną implementacji
- **Product Owner** — definiuje wymagania biznesowe wchodzące na wejście
- **Development Team** — implementuje na podstawie projektu

## Wejścia i wyjścia

- Wejścia: wymagania biznesowe (leasing, utrzymanie, rozliczenia mediów), mapy procesów operacyjnych, dane referencyjne nieruchomości, integracje wymagane, wymagania bezpieczeństwa/privacy, przepisy lokalne (czynsze/depozyty), profile ruchu, budżet/FinOps.  
- Wyjścia: model architektury (logiczny/fizyczny), kontrakty API/eventów, katalog integracji, wymagania bezpieczeństwa/PII, plan DR/BCP, SLA/SLO, decyzje architektoniczne i roadmapa.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: tenancy_lifecycle_process, payments_integration, maintenance_work_order_flow, document_management_policy, data_privacy_assessment, dr_plan, observability_plan.  
- Key Document Structures: moduły, integracje, dane, bezpieczeństwo, DR/BCP, raportowanie.  
- Document Dependencies: IAM/SSO, ERP/accounting, payment gateway, GIS/IoT, CMMS, document store, logging/monitoring.


## Zależności dokumentu

Wymaga: map procesów najmu/utrzymania, listy integracji i danych, wymagań bezpieczeństwa/PII, przepisów lokalnych, architektury referencyjnej IT, dostępności IAM/monitoringu/DR. Braki = DoR otwarte.


## Fazy cyklu życia

- Projekt i wybór architektury (cloud/on‑prem/hybrid).  
- Implementacja modułów i integracji.  
- Operacje/utrzymanie, audyty, DR testy.  
- Modernizacja i skalowanie.



## Struktura sekcji (szkielet)
- Streszczenie i cele biznesowe
- Zakres, założenia, ograniczenia
- Kontekst domenowy i interesariusze
- Wymagania funkcjonalne i niefunkcjonalne
- Architektura/komponenty i integracje
- Model danych i przepływy informacji
- Bezpieczeństwo, prywatność i compliance
- Plan wdrożenia/migracji i kryteria go/no-go
- Monitoring/operacje oraz ryzyka i mitigacje
- Decyzje i uzasadnienia, pytania otwarte
## Szybkie powiązania
- property-management-system-architecture
- risk-management-architecture
- property-listing-management
- property-management-system-vision
- property-management-system-requirements

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
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.
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

- Moduły/dane → Integracje → Raporty → SLA.  
- Bezpieczeństwo/PII → IAM/dokumenty → Audyt/zgodność.  
- DR/BCP → SLA → Architektura i hosting (cloud/on‑prem/hybrid).


## Struktura sekcji

1) Kontekst i cele biznesowe  
2) Moduły i domeny (leasing, utrzymanie, płatności, dokumenty, raporty)  
3) Architektura logiczna/fizyczna i hosting  
4) Integracje (ERP, płatności, GIS/IoT, CRM, e‑signature)  
5) Dane i model informacji (umowy, najemcy, obiekty, media)  
6) Bezpieczeństwo/PII i zgodność (RODO, dostęp, szyfrowanie, audyt)  
7) SLA/SLO i operacje (monitoring, support, CMMS)  
8) DR/BCP (RTO/RPO, backup, testy)  
9) Raportowanie/analityka (finansowe, operacyjne, ESG)  
10) Roadmapa, ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Diagramy architektury i integracji; katalog API/eventów.  
- Model danych (kluczowe encje) i zasady PII/retencji.  
- Plan DR/BCP i testy; SLA/SLO dla kluczowych modułów.  
- Standardy dokumentów (umowy, zgłoszenia) i repozytorium.


## Wymagane streszczenia

- Executive snapshot: architektura, integracje, SLA, top ryzyka.  
- Krótka karta PII/bezpieczeństwo dla compliance.


## Guidance (skrót)

- Standaryzuj kontrakty API/eventów i dokumenty.  
- Integracje z ERP/płatności to krytyczne ścieżki — zapewnij wysokie SLA.  
- IoT/meters mogą generować duże wolumeny — planuj storage/stream.  
- Zaplanuj offline/field (mobile) i synchronizację.  
- Regularnie testuj DR/BCP i backup dokumentów.

