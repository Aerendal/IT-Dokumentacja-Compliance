---
title: Patient Data Privacy (HIPAA, GDPR)
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Patient Data Privacy (HIPAA, GDPR)


## Metadane

- Właściciel: Clinical Lead
- Wersja: v0.3
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnić opis środków ochrony danych pacjentów (PHI/PII) zgodnych z HIPAA i GDPR: obowiązki prawne, środki techniczne/organizacyjne, umowy i transfery, prawa osób/DSAR, retencja/usuwanie/deidentyfikacja, bezpieczeństwo (safeguards/art.32), monitorowanie i dowody zgodności.


## Zakres i granice

- Obejmuje: kategorie danych pacjenta (PHI/PII), role (CE/BA), notice/zgody/podstawy prawne, rejestry (ROP/DPIA), prawa osób (DSAR, access/amendment), retencja/deidentyfikacja/usuwanie, transfery i umowy (BAA/DPA/SCC/BCR), bezpieczeństwo (administrative/technical/physical safeguards), audyt/monitoring/szkolenia, breach/notification (odnośnik do runbooka IR/Breach).
- Poza zakresem: szczegółowe DPIA dla pojedynczych systemów, publiczna polityka prywatności (oddzielny dokument).


## Użytkownicy i interesariusze
- **Clinical Lead / Chief Medical Officer** — definiuje wymagania kliniczne i waliduje
- **Integration Architect** — projektuje integracje z systemami szpitalnymi
- **Security / Privacy Officer** — zapewnia zgodność z HIPAA, RODO, ustawa o ochronie zdrowia
- **Development Team** — implementuje funkcjonalności kliniczne

## Wejścia i wyjścia

- Wejścia: inventory systemów/PHI/PII, ROP/DPIA, HIPAA risk analysis, BAA/DPA/SCC/BCR, polityki retencji/bezpieczeństwa, DSAR/consent narzędzia i logi, rejestry incydentów/breach, wymagania kliniczne/regulatora.
- Wyjścia: tabela obowiązki→środki/dowody, lista umów/transferów, plan audytów/testów/szkoleń, waivery z sunset/kompensacjami, raport zgodności, aktualizacje rejestrów i klauzul.


## Założenia

- Systemy i dane są zinwentaryzowane; narzędzia DSAR/consent i logi dostępne; zespół kliniczny zaangażowany.


## Otwarte pytania

- Czy są dodatkowe jurysdykcje (stanowe/krajowe) z wymaganiami specyficznymi?  
- Jakie są SLA na DSAR/notice w kontraktach z klinikami/payerami?


## Powiązania (meta)

- Key Documents: data_privacy_hipaa_gdpr, records_of_processing, data_privacy_assessment, data_retention_policy, security_requirements, vendor_risk_assessment, incident_response_runbook, breach_notification_procedure, access_control_policy, risk_register.
- Key Document Structures: obowiązki, środki/dowody, umowy/transfery, retencja, prawa osób, bezpieczeństwo, audyt/monitoring, waivery.
- Document Dependencies: CMDB/inventory, data classification, consent/DSAR tooling, BAA/DPA/SCC/BCR, DLP/logging/audit, szkolenia kliniczne.


## Zależności dokumentu

- Upstream: inventory/ROP/DPIA, HIPAA risk analysis, umowy (BAA/DPA/SCC/BCR), polityki retencji/bezpieczeństwa, mechanizmy DSAR/consent.
- Downstream: audyty/testy, plan działań compliance, szkolenia kliniczne, aktualizacje rejestrów/klauzul.
- Zewnętrzne: procesorzy/BA, organy nadzorcze, klienci/placówki medyczne.


## Fazy cyklu życia

- Identyfikacja/zakres (PHI/PII, role CE/BA, jurysdykcje).
- Wdrożenie środków/umów i zapis w rejestrach.
- Monitorowanie/audyt/szkolenia; testy bezpieczeństwa.
- Przeglądy po zmianach/incidentach/breach; aktualizacja rejestrów/umów.



## Struktura sekcji (szkielet)

- Cel i zakres dokumentu
- Główne sekcje merytoryczne
- Powiązania z innymi dokumentami
- Wymagane zatwierdzenia i przeglądy
- Historia zmian

## Szybkie powiązania

- linkage_index.jsonl (privacy/patient)
- data_privacy_hipaa_gdpr, records_of_processing, data_privacy_assessment, data_retention_policy, security_requirements, vendor_risk_assessment, incident_response_runbook, breach_notification_procedure, access_control_policy, risk_register


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

- [Decyzja] Zakres i role CE/BA; [Decyzja] Środki i priorytety; [Decyzja] Waivery i sunset; [Decyzja] Plan audytów/szkoleń.


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

- [ ] Obowiązki HIPAA/GDPR pokryte środkami/dowodami; role CE/BA i transfery są jasne; umowy aktualne.
- [ ] DSAR/notice/retencja i bezpieczeństwo mają SLA/logi/dowody; waivery mają sunset/kompensacje.
- [ ] Breach/notification odniesiony do runbooka IR; audyty/monitoring/szkolenia zaplanowane; KPI/KRI mierzone.


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

- Zakres danych/rol → Obowiązki → Środki/dowody → Umowy/transfery → Retencja/deidentyfikacja → Prawa osób/DSAR → Bezpieczeństwo → Audyt/monitoring → Waivery/breach.


## Struktura sekcji

1) Streszczenie (scope PHI/PII, role CE/BA, top ryzyka, status)  
2) Zakres danych/systemów i ról (CE/BA, jurysdykcje)  
3) Obowiązki HIPAA/GDPR (notice/zgody/podstawy, prawa osób, dokumentacja)  
4) Rejestry i oceny (ROP, DPIA, HIPAA risk analysis)  
5) Umowy i transfery (BAA/DPA/SCC/BCR, lokalizacja)  
6) Retencja/usuwanie/deidentyfikacja (dowody, harmonogram)  
7) Bezpieczeństwo danych (admin/technical/physical safeguards, IAM, szyfrowanie, DLP, audyt)  
8) Prawa osób/DSAR (SLA, narzędzia, dowody)  
9) Monitorowanie/audyt i szkolenia kliniczne  
10) Waivery/wyjątki i ryzyka; decyzje (ADR)  
11) Breach/notification (link do runbooka IR/Breach)


## Wymagane rozwinięcia

- Tabela obowiązki→środki/dowody z ownerem i KPI/KRI; HIPAA safeguards i art.32.
- Lista umów (BAA/DPA/SCC/BCR) i transferów (lokalizacje, podmioty).
- Retencja/deidentyfikacja/depers z dowodami i harmonogramem przeglądów.
- DSAR/consent/notice: SLA, narzędzia, logi; training kliniczne i audyty.
- Waivery/wyjątki z sunset/kompensacjami; plan audytów/testów.


## Wymagane streszczenia

- Executive: scope PHI/PII, role CE/BA, top ryzyka, środki, status audytów/breach.
- One-pager: kluczowe obowiązki, środki, umowy/transfery, KPI/KRI.


## Guidance (skrót)

- DoR: inventory PHI/PII, ROP/DPIA, HIPAA risk analysis, BAA/DPA/SCC/BCR, polityki retencji/bezpieczeństwa, narzędzia DSAR/consent, ownerzy domen.  
- DoD: środki wdrożone i udokumentowane; rejestry/umowy aktualne; DSAR/consent działają; audyty/monitoring/szkolenia zaplanowane; waivery z sunset; breach runbook podlinkowany; dokument w linkage_index.  
- Spójność: każde wymaganie ma środek/dowód/owner; transfery i umowy pokryte; DSAR/notice/retencja/testy bezpieczeństwa mają SLA i dowody; breach odniesiony do runbooka.


## Checklisty Definition of Ready (DoR)

- [ ] Inventory PHI/PII/systemów i role CE/BA zebrane; ROP/DPIA i HIPAA risk analysis dostępne; BAA/DPA/SCC/BCR dostępne.
- [ ] Ownerzy domen/processów i narzędzia DSAR/consent wskazani; polityki retencji/bezpieczeństwa znane.


## Checklisty Definition of Done (DoD)

- [ ] Środki i dowody wdrożone; rejestry/umowy aktualne; DSAR/consent działają; audyty/monitoring/szkolenia zaplanowane; waivery z sunset; breach runbook powiązany; dokument w linkage_index.

