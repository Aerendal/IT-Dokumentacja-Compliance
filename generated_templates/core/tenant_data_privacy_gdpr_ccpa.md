---
title: Tenant Data Privacy (GDPR/CCPA)
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Tenant Data Privacy (GDPR/CCPA)


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Opisuje, jak dane tenantów (klientów B2B/SaaS) są przetwarzane i chronione zgodnie z GDPR/CCPA: obowiązki, środki, umowy i dowody zgodności.


## Zakres i granice

- Obejmuje: dane tenantów (PII + dane biznesowe), role (controller/processor), podstawy prawne/notice, DPA/SCC/BCR, prawa osób (DSAR), retencję/usuwanie, transfery, bezpieczeństwo (IAM, szyfrowanie, DLP, audyt), podział danych między tenantami (izolacja), logi/monitoring, audyty i waivery.
- Poza zakresem: polityka prywatności publiczna; szczegółowe DPIA per feature.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: inventory danych tenantów, ROP/DPIA, DPA/SCC/BCR, polityki retencji/bezpieczeństwa, mechanizmy DSAR/notice, architektura izolacji tenantów, rejestry incydentów, wymagania klientów/regulatora.
- Wyjścia: opis środków i dowodów, lista umów/transferów, plan audytów/testów, waivery z sunset/kompensacjami, raport statusu, guidance dla zespołów produkt/eng.


## Założenia
- Systemy i dane są zinwentaryzowane; narzędzia DSAR/consent i logi dostępne; zespół kliniczny zaangażowany.
## Otwarte pytania
- Czy są dodatkowe jurysdykcje (stanowe/krajowe) z wymaganiami specyficznymi?  
- Jakie są SLA na DSAR/notice w kontraktach z klinikami/payerami?
## Powiązania (meta)

- Key Documents: data_privacy_assessment, data_privacy_compliance_plan, data_privacy_compliance, data_retention_policy, security_requirements, vendor_risk_assessment, incident_response_runbook, breach_notification_procedure, access_control_policy.
- Dependencies: multi-tenant architecture/isolacja, IdP/IAM, DPA/SCC/BCR, DSAR/consent tools, data classification, logging/audit, training.


## Zależności dokumentu

- Upstream: inventory/ROP/DPIA, DPA/SCC/BCR, architektura multi-tenant, polityki retencji/bezpieczeństwa, DSAR/notice.
- Downstream: audyty, plany działań, komunikacja z klientami, aktualizacje rejestrów/klauzul, guidance dla dev/ops.
- Zewnętrzne: klienci (DPA/uzgodnienia), procesorzy, organy nadzorcze.


## Fazy cyklu życia

- Identyfikacja/zakres (dane tenantów, role, jurysdykcje, izolacja).  
- Wdrożenie środków/umów.  
- Monitorowanie/audyt i raportowanie.  
- Przeglądy po zmianach/incidentach.



## Struktura sekcji (szkielet)

- Cel i zakres dokumentu
- Główne sekcje merytoryczne
- Powiązania z innymi dokumentami
- Wymagane zatwierdzenia i przeglądy
- Historia zmian

## Szybkie powiązania

- guest-data-privacy-gdpr
- employee-data-privacy-gdpr
- data-privacy-hipaa-gdpr
- patient-data-privacy-hipaa-gdpr
- zgodno-gdpr-ccpa

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **ISO/IEC 27018** — Ochrona Danych Osobowych w Chmurze (PII)
- **ISO/IEC 27701** — Zarządzanie Informacjami o Prywatności (PIMS)

### Polskie normy i regulacje
- **UODO-PL** — Ustawa o Ochronie Danych Osobowych (implementacja RODO)

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
1. Uzupełnij scope, role, obowiązki i rejestry (ROP/DPIA/HIPAA risk analysis).  
2. Dodaj środki/dowody, umowy/transfery, retencję/deidentyfikację, DSAR/consent.  
3. Opisz bezpieczeństwo, audyt/monitoring/szkolenia, waivery i powiąż z runbookiem breach; zamknij DoR/DoD i wpisz do linkage_index.
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
- Niepełny inventory/ROP → luka compliance; brak DSAR/consent dowodów → ryzyko regulacyjne; brak BAA/SCC → transfer risk; brak sunset dla waiverów → trwały debt.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- data_privacy_hipaa_gdpr, records_of_processing, data_privacy_assessment, data_retention_policy, security_requirements, vendor_risk_assessment, incident_response_runbook, breach_notification_procedure, access_control_policy, risk_register.
## Powiązania z sekcjami innych dokumentów
- Security Requirements → safeguards; Data Retention → retencja/depers; IR/Breach → reakcja; Vendor Risk → umowy/transfery.
## Słownik pojęć w dokumencie
- PHI, PII, CE/BA, BAA, DPA, SCC/BCR, ROP, DPIA, DSAR, De‑identification, Depersonalizacja, Safeguards.
## Wymagane odwołania do standardów
- HIPAA (Privacy/Security Rule), GDPR (art. 5, 6, 9, 28, 30, 32, 33/34), ewentualnie lokalne przepisy medyczne; standardy branżowe (NIST/HITRUST) jeśli stosowane.
## Mapa relacji sekcja→sekcja
- Zakres/role → Obowiązki → Środki/dowody → Umowy/transfery → Retencja/deidentyfikacja → DSAR → Bezpieczeństwo → Audyt/monitoring → Waivery/Breach.
## Mapa relacji dokument→dokument
- Patient Data Privacy ↔ data_privacy_hipaa_gdpr/records_of_processing/data_retention_policy/security/IR/Breach.
## Ścieżki informacji
- Inventory/ROP/DPIA → Środki/dowody → Umowy/transfery → Retencja/DSAR → Audyt/monitoring → Breach → Aktualizacje rejestrów.
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
- Tabela obowiązki→środki/dowody, ROP, DPIA, HIPAA risk analysis, BAA/DPA/SCC/BCR, log DSAR/consent, retencja/depers dowody, audyt/szkolenia plany, waiver log, ADR log, breach notification runbook link.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości
- SLA DSAR/notice, kompletność ROP/DPIA, liczba/miejsce waiverów, coverage safeguards vs. HIPAA/GDPR, audyt findings, incydenty/breach, zgodność retencji.
## Kryteria ukończenia
- [ ] Obowiązki HIPAA/GDPR opisane i pokryte środkami/dowodami; umowy/transfery/retencja/DSAR opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

- Obowiązki → środki/izolacja → dowody → audyt/monitoring → waivery.


## Struktura sekcji

1) Streszczenie (scope, role, top ryzyka, plan)  
2) Dane tenantów i role (controller/processor, izolacja)  
3) Podstawy prawne, notice/zgody, prawa osób (DSAR)  
4) Rejestry i oceny (ROP, DPIA)  
5) Umowy i transfery (DPA/SCC/BCR, podmiot trzeci, lokalizacja)  
6) Retencja/usuwanie (policy, implementacja, dowody)  
7) Bezpieczeństwo i izolacja tenantów (IAM, szyfrowanie, segmentacja, DLP, audyt)  
8) Logi/monitoring i audyty (KPI/KRI, cadence)  
9) Waivery/wyjątki i ryzyka; decyzje (ADR)  


## Wymagane rozwinięcia

- Tabela obowiązki→środki/dowody; architektura izolacji tenantów; DPA/SCC/BCR lista; retencja/depers dowody; DSAR/logi.


## Wymagane streszczenia

- Executive summary: scope, role, top ryzyka, środki, status audytów.
- One-pager: obowiązki, środki, umowy/transfery, KPI/KRI.


## Guidance (skrót)

- DoR: inventory/ROP/DPIA, architektura izolacji, DPA/SCC/BCR, polityki retencji/bezpieczeństwa, DSAR/notice narzędzia; ownerzy domen.
- DoD: środki wdrożone i udokumentowane; rejestry/umowy aktualne; izolacja tenantów opisana/testy; audyty/monitoring zaplanowane; waivery z sunset; metadane aktualne; dokument w linkage_index.
- Spójność: izolacja tenantów zdefiniowana (dane, metadane, logi); każda umowa/transfer pokryta; DSAR/notice/retencja mają SLA/logi; bezpieczeństwo (IAM/szyfrowanie/audyt) ma dowody.

