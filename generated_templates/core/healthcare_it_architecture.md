---
title: Healthcare IT Architecture
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Healthcare IT Architecture


## Metadane

- Właściciel: Solution Architect
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje referencyjną architekturę IT dla organizacji ochrony zdrowia: systemy kliniczne/administracyjne, integracje, bezpieczeństwo i zgodność (HIPAA/RODO), dane pacjenta, interoperacyjność i ciągłość działania. Ma być podstawą projektów i audytów.


## Zakres i granice

- Obejmuje: EHR/EMR, LIS/RIS/PACS, HIS/ERP/HR, systemy rejestracji i billing, portale pacjenta/telemedycyna, integracje (HL7 FHIR/DICOM/API), zarządzanie tożsamością, prywatność i zgody, bezpieczeństwo kliniczne, dane analityczne i raportowanie, ciągłość działania/DR, sieć i segmentacja, urządzenia medyczne IoMT.
- Poza zakresem: szczegółowe projekty kliniczne urządzeń, polityki personalne, kontrakty dostawców (oddzielne dokumenty).


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

- linkage_index.jsonl (healthcare/it/architecture)  
- privacy_and_consent_policy, data_governance_healthcare, security_baseline_healthcare, interoperability_plan, dr_plan_clinical_it, iot_medical_device_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **HL7 FHIR** — Standard Wymiany Danych w Ochronie Zdrowia
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
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

1. Zmapuj systemy/procesy i interfejsy, uzupełnij dane/zgody/segmentację.  
2. Zdefiniuj integracje (FHIR/HL7/DICOM) i wymagania bezpieczeństwa/DR.  
3. Zaplanuj wdrożenia/migracje i testy; aktualizuj DoR/DoD i linkage_index.


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

## Powiązania sekcja↔sekcja

- Procesy kliniczne → Systemy → Integracje/standardy → Bezpieczeństwo/prywatność → DR/BCP.  
- Dane pacjenta → Zgody/privacy → Dostęp/segmentacja → Audyt/raportowanie.  
- IoMT → Sieć/segmentacja → Monitoring/patching.


## Struktura sekcji

1) Kontekst i cele kliniczne/biznesowe  
2) Domeny systemów (kliniczne, administracyjne, pacjent) i mapy procesów  
3) Integracje i interoperacyjność (FHIR/HL7/DICOM/API, ESB/iPaaS)  
4) Dane i słowniki (PHI/PII, master data, terminologia kliniczna)  
5) Bezpieczeństwo/prywatność i zgody (IAM, MFA, segmentacja, audyt, RODO/HIPAA)  
6) IoMT i sieć (segmentacja, NAC, patch/firmware, monitoring)  
7) Ciągłość działania/DR (RPO/RTO kliniczne, archiwizacja obrazów, testy)  
8) Analityka i raportowanie (DWH/lake, BI kliniczne, quality measures)  
9) Operacje i zarządzanie konfiguracją (CMDB/CMMS, change, patching)  
10) Roadmapa, decyzje, ryzyka, otwarte pytania


## Wymagane rozwinięcia

- Katalog interfejsów (HL7/FHIR/DICOM/API) z właścicielami.  
- Segmentacja sieci klinicznej (VLAN/NAC/ZTNA) i zasady dostępu do PHI.  
- Plan DR/BCP dla systemów krytycznych (EHR/PACS) z testami.  
- Słownik danych pacjenta i mapowanie terminologii (LOINC/SNOMED/ICD).


## Wymagane streszczenia

- Executive view: główne systemy, integracje, ryzyka compliance, gotowość DR.  
- Jednostronicowa mapa integracji i segmentacji dla audytu.


## Guidance (skrót)

- Projektuj „privacy by design”: zgody, minimalny dostęp, audyt, szyfrowanie.  
- Standaryzuj integracje na FHIR/HL7/DICOM; unikaj ad‑hoc CSV/API bez kontraktów.  
- Kliniczne SLA > techniczne SLA — priorytetyzuj RTO/RPO dla EHR/PACS.  
- IoMT to najsłabsze ogniwo: segmentacja, NAC, patch/firmware, monitoring anomalii.  
- Testuj DR/BCP regularnie, łącznie z odtwarzaniem obrazów i danych klinicznych.


## Checklisty Definition of Ready (DoR)

- [ ] Inwentarz systemów i interfejsów HL7/FHIR/DICOM zebrany.  
- [ ] Polityki zgód/privacy i wymagania SLA kliniczne dostępne.  
- [ ] Założenia segmentacji sieci/IoMT i bezpieczeństwa uzgodnione.  
- [ ] Wymagania DR/BCP dla krytycznych systemów określone.  
- [ ] Zespół właścicieli domen wyznaczony (kliniczne/IT/security).


## Checklisty Definition of Done (DoD)

- [ ] Architektura opisana, mapy integracji/segmentacji dołączone.  
- [ ] Standardy FHIR/HL7/DICOM i kontrakty API zdefiniowane.  
- [ ] Plan DR/BCP i testy uzgodnione; status/wersja/data zaktualizowane.  
- [ ] Zgody/privacy, IAM/MFA, audyt i logging PHI opisane.  
- [ ] Powiązania w linkage_index i katalog danych uzupełnione.

