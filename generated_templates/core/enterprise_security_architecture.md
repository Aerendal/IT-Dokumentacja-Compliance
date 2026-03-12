---
title: Enterprise Security Architecture
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Enterprise Security Architecture


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Określić docelową architekturę bezpieczeństwa dla całej organizacji: zasady, wzorce, capability map, governance i roadmapę.


## Zakres i granice

- Obejmuje: zasady/pryncypia bezpieczeństwa, capability map (identity, sieć, dane, aplikacje, endpoint, SOC/IR, GRC), wzorce referencyjne, integracje między domenami, governance, metryki i roadmapę.
- Poza zakresem: konfiguracje systemów operacyjnych i pojedynczych usług (opisane w dokumentach domenowych).


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia
- Wejścia: strategia biznesowa i produktowa, mapy procesów i capability, as-is architektura i CMDB, backlog inicjatyw, ograniczenia regulacyjne/techniczne/finansowe, istniejące ADR/standardy, dane referencyjne i integracje, plany sourcingu/partnerstw.
- Wyjścia: target i interim architektura przedsiębiorstwa (diagramy kontekst/warstwy/domeny/linie danych), zasady/guardrails, decyzje architektoniczne z uzasadnieniem, roadmapa transformacji z kamieniami i zależnościami, plan migracji danych i integracji, kryteria go/no-go, lista ryzyk/założeń.
## Założenia
- Dostępne są zespoły compliance/kliniczne do akceptacji.  
- Narzędzia IAM, SIEM/SOAR, katalog danych i iPaaS są dostępne.  
- Budżet na testy DR/BCP i laboratoria integracyjne.
## Otwarte pytania
- Czy partnerzy zewnętrzni wymagają dedykowanych stref integracji?  
- Jakie są lokalne wymogi prawne (kraje) dot. lokalizacji danych medycznych?  
- Jak wygląda proces rotacji kluczy/secretów dla urządzeń IoMT?
## Powiązania (meta)
- Key Documents: business_strategy, product_strategy_document, technology_strategy, data_strategy, security_architecture_vision, integration_strategy, operating_model, sourcing_strategy, cost_model/FinOps, risk_register.
- Key Document Structures: domena/capability → usługi/aplikacje → dane → interfejsy → bezpieczeństwo/compliance → operacje.
- Document Dependencies: polityki/regulacje (np. GDPR/PCI/ISO), standardy architektoniczne organizacji, katalog usług wspólnych, umowy z dostawcami/partnerami.
- RACI: Enterprise Architect (owner), Domain/Capability Architects, Security, Data, Infra/Cloud, Product, Ops, Finance/Procurement.
- Standardy/compliance: architektura referencyjna, standardy API/event/IaC, klasyfikacja danych, IAM/segregacja, DR/BCP, FinOps/GreenOps.
## Zależności dokumentu
- Upstream: strategia i portfel inicjatyw, decyzje korporacyjne (cloud, buy vs build, vendor lock-in), dane o bieżących systemach/umowach, regulacje.
- Downstream: architektury domenowe, projekty produktów, backlog epik/roadmap, plany danych/integracji, standardy implementacyjne, budżety i kontrakty.
- Zewnętrzne: dostawcy chmurowi/SaaS, integracje partnerskie, wymogi regulatorów (lokalizacja danych, audyt), zależności łańcucha dostaw.
## Fazy cyklu życia
- Discovery: inwentaryzacja as-is, mapy capability/domen, problemy i ryzyka.
- Target/Interim Design: warianty, ADR, model danych i integracji, standardy/guardrails.
- Review: board (arch/security/compliance/finanse), koszty/TCO/FinOps, performance i dostępność, ryzyka/regulacje.
- Implementation & Test: zgodność implementacji z target/interim, testy NFR, walidacja integracji i danych.
- Rollout & Ops: migracje etapowe, monitoring/SLO, DR/BCP, governance zmian, postmortems i iteracje.
## Struktura sekcji (szkielet)

- Kontekst i pryncypia bezpieczeństwa
- Capability map (identity/network/data/app/endpoint/SOC/GRC)
- Wzorce referencyjne i minimalne kontrolki
- Integracje między domenami i zależności
- Governance, role i fora decyzyjne
- Metryki/KPI i raportowanie
- Roadmapa i priorytety
- Ryzyka i wyjątki


## Szybkie powiązania
- security-architecture
- security-architecture-review
- security-architecture-reference
- security-architecture-document
- network-security-architecture

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
- **UoR-PL** — Ustawa o Rachunkowości

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

- Zdefiniuj pryncypia i capability map; podłącz wzorce referencyjne i minimalne kontrolki; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Ustal roadmapę i fora governance; synchronizuj z planami domenowymi.


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
- Capability — zdolność biznesowa realizowana przez procesy, dane i systemy.
- Domain — spójny obszar funkcjonalny z jasno określonym właścicielem i interfejsami.
- Guardrails — zasady ograniczające wybory architektoniczne/technologiczne (np. dozwolone chmury, standardy API/IaC).
## Przykłady użycia
- Transformacja platformy płatniczej: segmentacja domen (Payments, Risk/Fraud, Ledger), event-driven integracje, multi-region, PCI/DR/BCP, plan migracji danych i cutover.
- Konsolidacja aplikacji front-office: target composable architecture, API gateway + event mesh, wspólne capability (identity/catalog), redukcja duplikatów, roadmapa fazowa.
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
- Mapy capability/domen, CMDB/system inventory, diagramy C4/layered, ADR log, macierz NFR/SLO, plan migracji danych, katalog API/event, RACI, FinOps/GreenOps modele kosztów.
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

- Strategia firmy/IT, apetyt na ryzyko, regulacje.
- Architektury domenowe (cloud, sieć, tożsamość, dane), wyniki audytów/incydentów.
- Benchmarki/ramy (TOGAF/SABSA/ISO), lessons learned.


## Wyjścia

- Dokument pryncypiów i capability map.
- Wzorce referencyjne i minimalne kontrolki per capability.
- Roadmapa inicjatyw i zależności między domenami.
- Governance (fora, odpowiedzialności) i metryki.



## Szybkie powiązania (uzupełnij)

- security_architecture_reference.md
- security_strategy.md
- security_roadmap.md
- security_compliance_matrix.md
- risk_management_framework.md
- security_status_report.md


## Wymagane rozwinięcia / streszczenia

- Capability map z przypisanymi usługami/produktami.
- Streszczenie pryncypiów i top inicjatyw.


## Wymagane powiązania

- Strategia, roadmapa, compliance matrix, rejestr ryzyk, architektury domenowe.


## Kryteria DoR

- [ ] Strategia/ryzyka/regulacje zebrane.
- [ ] Architektury domenowe dostępne.
- [ ] Właściciele domen i governance ustalone.


## Kryteria DoD

- [ ] Pryncypia i capability map opisane.
- [ ] Wzorce/minimalne kontrolki podane; roadmapa i governance wpisane.
- [ ] Quick-links/checklisty zaktualizowane, metadane bieżące.


## Artefakty do załączenia

- Capability map, diagramy domenowe.
- Wzorce referencyjne i checklisty minimalne.
- Roadmapa inicjatyw i kalendarz governance.


## Walidacja / testy

- Peer review z właścicielami domen i ryzyka.
- Sprawdzenie spójności z regulacjami i strategiami IT.


## Metryki monitorowane

- Postęp inicjatyw w roadmapie; adopcja wzorców.
- Trend zgodności i ryzyk krytycznych.
- Udział w forach governance (frekwencja, decyzje na czas).


## Utrzymanie i aktualizacje

- Przegląd półroczny/roczny lub po istotnych zmianach strategii/regulacji.
- Aktualizuj capability map i roadmapę wraz z inicjatywami domenowymi.


## Zakończenie

Po spełnieniu DoD opublikuj dokument, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i zsynchronizuj z planami domen.
