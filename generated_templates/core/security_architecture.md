---
title: Security Architecture
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Architecture


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zdefiniować architekturę bezpieczeństwa systemu: warstwy i kontrolki, przepływy danych, integracje, odpowiedzialności i zgodność.


## Zakres i granice

- Obejmuje: warstwy/konrolki (identity, sieć, dane, aplikacja, endpoint, monitoring), trust boundaries, zależności, zgodność/regulacje, ryzyka i rekomendacje.
- Poza zakresem: szczegółowe konfiguracje per usługa (opisywane w dokumentach technicznych/runbookach).


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

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

- Kontekst i zakres
- Warstwy i kontrolki (identity/network/data/app/endpoint/obs)
- Przepływy danych, trust boundaries i zależności
- Monitoring/logging/audyt i observability
- Zgodność i ryzyka
- Rekomendacje i plan działań


## Szybkie powiązania
- security-architecture-review
- security-architecture-reference
- security-architecture-document
- network-security-architecture
- mlops-security-architecture

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa

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

- Opisz kontekst, dodaj diagram i tabelę kontrolek z właścicielami; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Po review podlinkuj artefakty i zaktualizuj status.


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

- Architektura systemu i DFD, mapa danych/wrażliwości.
- Polityki/regulacje, wymagania NFR/SLO/SLA.
- Rejestr ryzyk, incydenty, wyniki audytów/testów.


## Wyjścia

- Opis i diagram architektury bezpieczeństwa.
- Lista kontrolek z właścicielami i coverage.
- Rekomendacje i plan działań.
- Powiązania do monitoringu/testów/compliance.



## Szybkie powiązania (uzupełnij)

- security_architecture_review.md
- security_architecture_reference.md
- security_policy_design.md
- security_compliance_matrix.md
- security_monitoring_strategy.md
- logging_and_audit_trail.md


## Wymagane rozwinięcia / streszczenia

- Diagram(y) architektury i trust boundaries.
- Tabela kontrolek: warstwa → kontrolka → właściciel → dowód/monitoring.
- Streszczenie ryzyk i rekomendacji.


## Wymagane powiązania

- Polityki/standardy, compliance matrix, monitoring/logging, runbooki IR, oceny bezpieczeństwa.
- Rejestr ryzyk i backlog defektów bezpieczeństwa.


## Kryteria DoR

- [ ] Architektura/DFD i mapa danych dostępne.
- [ ] Polityki/regulacje i wymagania NFR zebrane.
- [ ] Ownerzy bezpieczeństwa i architektury potwierdzeni.


## Kryteria DoD

- [ ] Diagram/Opis uzupełniony, kontrolek i właścicieli wpisane.
- [ ] Ryzyka i rekomendacje opisane, plan działań dodany.
- [ ] Quick-links/checklisty zaktualizowane, metadane bieżące.


## Artefakty do załączenia

- Diagramy architektury/trust boundaries.
- Tabela kontrolek/właścicieli.
- Plan działań i linki do monitoringu/testów.


## Walidacja / testy

- Peer review architektury; sanity trust boundaries.
- Sprawdzenie mapowania kontrolek do ryzyk/DFD.


## Metryki monitorowane

- Pokrycie kontrolek per warstwa/asset.
- Liczba wyjątków i ich wiek.
- Trend ryzyk i niezgodności architektonicznych.


## Utrzymanie i aktualizacje

- Przegląd co release/kwartał lub po zmianach architektury/incydencie.
- Aktualizuj diagramy i kontrole po zmianach systemu lub standardów.


## Zakończenie

Po spełnieniu DoD podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i zakomunikuj zmiany interesariuszom.
