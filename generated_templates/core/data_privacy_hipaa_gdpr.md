---
title: Data Privacy (HIPAA, GDPR)
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Data Privacy (HIPAA, GDPR)


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Opisuje, jak organizacja spełnia wymagania prywatności dla danych zdrowotnych i osobowych w kontekście HIPAA i GDPR: obowiązki, środki, procesy, dowody zgodności i monitorowanie.


## Zakres i granice

- Obejmuje: kategorie danych (PHI/PII), role (covered entity, business associate), podstawy prawne/zgody, notice/BAA/DPA, prawa osób (DSAR, access/amendment), ROP/DPIA, retencję/usuwanie, transfery (SCC/BCR), bezpieczeństwo (HIPAA Safeguards, GDPR art. 32), rejestrowanie/monitoring, audyty, waivery/wyjątki.
- Poza zakresem: szczegółowe DPIA/PIA per system (osobne dokumenty), pełne polityki publiczne (osobny dokument).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: inventory PHI/PII i systemów, ROP/DPIA, BAA/DPA/SCC/BCR, polityki retencji/bezpieczeństwa, DSAR/consent mechanizmy, HIPAA risk analysis, rejestry incydentów/breach, wymagania klientów/regulatora.
- Wyjścia: opis zgodności HIPAA/GDPR, środki techn./org., lista umów/transferów, plan audytów/testów, waivery z sunset/kompensacjami, raporty statusu.


## Założenia
- Systemy i dane są zinwentaryzowane; narzędzia DSAR/consent i logi dostępne; zespół kliniczny zaangażowany.
## Otwarte pytania
- Czy są dodatkowe jurysdykcje (stanowe/krajowe) z wymaganiami specyficznymi?  
- Jakie są SLA na DSAR/notice w kontraktach z klinikami/payerami?
## Powiązania (meta)

- Key Documents: records_of_processing, data_privacy_assessment, data_privacy_compliance_plan, data_retention_policy, security_requirements, vendor_risk_assessment, incident_response_runbook, breach_notification_procedure, access_control_policy.
- Dependencies: CMDB/system inventory, data classification, consent/DSAR tools, BAA/DPA/SCC/BCR, DLP/logging/audit, training/awareness, HIPAA safeguards.


## Zależności dokumentu

- Upstream: inventory/ROP/DPIA, risk analysis (HIPAA), BAA/DPA/SCC/BCR, polityki retencji/bezpieczeństwa, DSAR/consent.
- Downstream: audyty, raporty zgodności, plan działań z compliance planu, szkolenia, aktualizacje rejestrów i klauzul.
- Zewnętrzne: procesorzy/BA, organy nadzorcze, klienci.


## Fazy cyklu życia

- Identyfikacja/zakres (PHI/PII, role, jurysdykcje).  
- Wdrożenie środków i umów.  
- Monitorowanie/audyt i raportowanie.  
- Przeglądy po zmianach/incidentach.



## Struktura sekcji (szkielet)

- Cel i zakres dokumentu
- Główne sekcje merytoryczne
- Powiązania z innymi dokumentami
- Wymagane zatwierdzenia i przeglądy
- Historia zmian

## Szybkie powiązania

- patient-data-privacy-hipaa-gdpr
- guest-data-privacy-gdpr
- employee-data-privacy-gdpr
- tenant-data-privacy-gdpr-ccpa
- user-data-privacy

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **HL7 FHIR** — Standard Wymiany Danych w Ochronie Zdrowia
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
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

- Obowiązki (HIPAA/GDPR) → środki → dowody → audyt/monitoring → waivery.


## Struktura sekcji

1) Streszczenie (PHI/PII scope, role, top ryzyka, plan)  
2) Zakres danych/systemów i ról (covered entity/BA, jurysdykcje)  
3) Obowiązki HIPAA (Safeguards/BAA/notice/breach) i GDPR (podstawy, notice, prawa osób)  
4) Rejestry i oceny (ROP, DPIA, HIPAA risk analysis)  
5) Umowy i transfery (BAA/DPA/SCC/BCR, lokalizacja)  
6) Retencja/usuwanie/deidentyfikacja (policy, implementacja, dowody)  
7) Bezpieczeństwo (administracyjne/fizyczne/techniczne; IAM, szyfrowanie, DLP, audyt)  
8) DSAR/prawa osób i proces (SLA, narzędzia, dowody)  
9) Monitorowanie, audyty, szkolenia (cadence, KPI/KRI)  
10) Waivery/wyjątki i ryzyka; decyzje (ADR)  


## Wymagane rozwinięcia

- Tabela obowiązki→środki/dowody (HIPAA/GDPR), owner/termin; BAA/DPA/SCC/BCR lista; retencja/depers dowody; log DSAR/consent; plan audytów/szkoleń.


## Wymagane streszczenia

- Executive summary: PHI/PII w scope, role (CE/BA), top ryzyka, środki, status audytów.
- One-pager: obowiązki kluczowe, środki, umowy/transfery, KPI/KRI.


## Guidance (skrót)

- DoR: inventory PHI/PII i role (CE/BA), ROP/DPIA i HIPAA risk analysis, BAA/DPA/SCC/BCR, polityki retencji/bezpieczeństwa, DSAR/consent narzędzia, ownerzy domen.
- DoD: środki wdrożone i udokumentowane; rejestry/umowy aktualne; DSAR/consent działają; audyty/monitoring zaplanowane; waivery z sunset; metadane aktualne; dokument w linkage_index.
- Spójność: każde wymaganie HIPAA/GDPR ma środek/dowód/owner; transfery i umowy są pokryte; DSAR/notice/retencja/testy bezpieczeństwa mają SLA i dowody.

