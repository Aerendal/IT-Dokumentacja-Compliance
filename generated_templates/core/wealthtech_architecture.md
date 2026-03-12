---
title: WealthTech Architecture
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# WealthTech Architecture


## Metadane

- Właściciel: Solution Architect
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zaprojektować architekturę platformy WealthTech (doradztwo inwestycyjne, portfele, trading) uwzględniając zgodność, bezpieczeństwo i skalowalność.


## Zakres i granice

- Obejmuje: moduły (KYC/AML, profile inwestorów, risk engine, portfolio mgmt/rebalancing, trading/OMS, dane rynkowe, raporty regulacyjne, klient B2C/B2B), integracje (broker, custodian, płatności), bezpieczeństwo/prywatność (PII/fin dane), zgodność (MiFID/SEC/KNF, Suitability), audyt, SLA, observability, DR.
- Poza zakresem: szczegółowe strategie inwestycyjne (osobne dokumenty) i UI design.


## Użytkownicy i interesariusze
- **Solution / Enterprise Architect** — projektuje i zatwierdza architekturę
- **Tech Lead** — odpowiada za spójność techniczną implementacji
- **Product Owner** — definiuje wymagania biznesowe wchodzące na wejście
- **Development Team** — implementuje na podstawie projektu

## Wejścia i wyjścia
- Wejścia: wymagania kliniczne i regulacyjne, mapa procesów (kliniczne/administracyjne), inwentarz systemów i interfejsów, profile danych pacjenta, polityki zgód/RODO/HIPAA, wymagania bezpieczeństwa, SLA kliniczne, ograniczenia sprzętowe IoMT, budżet i roadmapa.
- Wyjścia: model architektury (logiczny/fizyczny), segmentacja sieci i bezpieczeństwa, standardy integracji (FHIR/HL7/DICOM/API), katalog danych i słownik terminów klinicznych, plan interoperacyjności, wymagania DR/BCP, decyzje technologiczne, RACI i harmonogram wdrożeń.
## Założenia
- Dostępne są zespoły compliance/kliniczne do akceptacji.  
- Narzędzia IAM, SIEM/SOAR, katalog danych i iPaaS są dostępne.  
- Budżet na testy DR/BCP i laboratoria integracyjne.
## Otwarte pytania
- Czy partnerzy zewnętrzni wymagają dedykowanych stref integracji?  
- Jakie są lokalne wymogi prawne (kraje) dot. lokalizacji danych medycznych?  
- Jak wygląda proces rotacji kluczy/secretów dla urządzeń IoMT?
## Powiązania (meta)
- Key Documents: clinical_process_map, interoperability_plan, data_governance_healthcare, privacy_and_consent_policy, security_baseline_healthcare, dr_plan_clinical_it, iot_medical_device_policy.
- Key Document Structures: domeny kliniczne, dane pacjenta, integracje, bezpieczeństwo/prywatność, ciągłość działania, analityka/raportowanie.
- Document Dependencies: IAM/SSO/consent, HSM/PKI, sieć/segmentacja, katalog interfejsów HL7/FHIR/DICOM, CMMS/CMDB urządzeń medycznych, SIEM/SOAR, backup/archiwum obrazów.
## Zależności dokumentu
Wymaga: listy systemów i interfejsów, polityk zgód i prywatności, wymagań SLA klinicznych, standardów bezpieczeństwa/segmentacji, mapy urządzeń IoMT. Braki = DoR otwarte.
## Fazy cyklu życia
- Definicja architektury referencyjnej.  
- Plan i projekt integracji/segmentacji.  
- Wdrożenia i migracje systemów/urzadzeń.  
- Operacje, audyty regulacyjne, aktualizacje i modernizacje.
## Struktura sekcji (szkielet)

- Domeny i moduły funkcjonalne
- Integracje (broker/custodian/dane/płatności)
- Dane i model (PII, transakcyjne, ryzyko)
- Bezpieczeństwo/zgodność (KYC/AML, Suitability, audyt)
- NFR: wydajność, dostępność, DR
- Observability i operacje
- Plan wdrożenia/migracji


## Szybkie powiązania

- Financial Data Security, KYC/AML Compliance, Audit Trail, Incident/DR, Performance/SLAs.


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
- PHI (Protected Health Information): dane identyfikujące pacjenta i jego historię.  
- Interoperacyjność: bezpieczna wymiana danych klinicznych między systemami/partnerami.  
- NAC: Network Access Control dla urządzeń/IoMT.
## Przykłady użycia
- Modernizacja EHR z integracją FHIR i PACS.  
- Budowa telemedycyny z dostępem do danych pacjenta i billingiem.  
- Segmentacja sieci klinicznej i IoMT dla audytu bezpieczeństwa.
## Ryzyka i ograniczenia
- Naruszenie prywatności/RODO/HIPAA.  
- Przestoje systemów klinicznych wpływające na opiekę pacjenta.  
- Luki w IoMT/firmware i brak patchy.
## Decyzje i uzasadnienia
- Wybór standardu integracji (FHIR/HL7) dla nowych usług.  
- Poziomy segmentacji i dostępu do PHI.  
- Architektura DR (aktywny/aktywny vs aktywny/pasywny) dla EHR/PACS.
## Powiązania z innymi dokumentami
- privacy_and_consent_policy — zasady zgód i PII/PHI.  
- interoperability_plan — szczegóły integracji i testów.  
- dr_plan_clinical_it — ciągłość działania i testy DR.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- HIPAA / RODO, normy lokalne (np. HL7 PL), FHIR/HL7/DICOM.  
- Wewnętrzne standardy bezpieczeństwa i segmentacji klinicznej.
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

## Wejścia

- Wymagania regulacyjne i biznesowe, profile klientów, wolumeny transakcyjne, dostawcy danych/brokerzy, polityki bezpieczeństwa, SLA.


## Wyjścia

- Architektura referencyjna, diagramy, model danych, integracje, wymagania niefunkcjonalne, plan bezpieczeństwa/regulacji, runbooki operacyjne.



## Jak używać (checklista)

- Zmapuj moduły i integracje; zdefiniuj NFR i zgodność.
- Zaprojektuj model danych i bezpieczeństwo/PII; ustal audyt i logging.
- Przygotuj diagramy i plan wdrożenia; zdefiniuj SLA i DR.


## Wymagane rozwinięcia / powiązania

- Diagramy architektury, matryca regulacyjna, model danych, SLA/DR, runbooki ops, lista integracji/dostawców.


## Kryteria DoR

- Wymagania biznes/regulacyjne zebrane; dostawcy danych/brokerzy znani.


## Kryteria DoD

- Architektura zatwierdzona; NFR/zgodność opisane; integracje i dane zmapowane; plan wdrożenia gotowy.


## Artefakty

- Dokument architektury, diagramy, model danych, matryca zgodności, SLA/DR, runbooki.


## Walidacja

- Przegląd architektury/secu/regulacyjny; testy POC z brokerem/danymi; weryfikacja audytu/logów.


## Metryki

- SLA fulfillment, latency trading/quotes, błędy integracji, incydenty bezpieczeństwa/regulacyjne.


## Utrzymanie

- Przegląd roczny/regulacyjny; aktualizacja przy zmianach dostawców/reguł; audyty okresowe.


## Zakończenie

Architektura WealthTech musi łączyć zgodność, bezpieczeństwo i wydajność; utrzymuj ją z audytami i SLA.

