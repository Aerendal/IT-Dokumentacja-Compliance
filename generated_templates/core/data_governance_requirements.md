---
title: Data Governance Requirements
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Data Governance Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.3
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zdefiniować wymagania ładu danych: role i odpowiedzialności, polityki (klasyfikacja, dostęp, jakość, privacy, retencja), procesy zmian i kontroli, metryki/SLO jakości danych, narzędzia (catalog/lineage/DQ/DLP), audyt i raportowanie. Celem jest spójne, bezpieczne, zgodne i dostępne dane.


## Zakres i granice

- Obejmuje: role (Owner/Steward/Custodian/Consumer), katalog i linię danych, klasyfikację i polityki quality/privacy/security/retention, SoD i kontrolę dostępu, metryki jakości (completeness/accuracy/timeliness), standardy definicji danych, procesy zmian/zgód/sharing, TPRM dostawców danych, audyt/monitoring/raportowanie, narzędzia (catalog, lineage, DQ, DLP, audit).
- Poza zakresem: szczegółowe modele danych per domena (oddzielne specyfikacje), implementacja konkretnych pipeline (osobne dokumenty techniczne).


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: strategia danych, klasyfikacja danych, polityki privacy/security/retencji, rejestr systemów/pipeline, wymagania regulacyjne (GDPR/CCPA/PCI/HIPAA/branżowe), katalog danych, metryki jakości, rejestr TPRM dostawców.
- Wyjścia: zestaw wymagań governance (role, procesy, polityki), katalog kontrolny (quality/access/privacy/retention), metryki i SLO/KPI danych, plan narzędzi (catalog/lineage/DQ/DLP), wymagania audytu i raportów, RACI i plan wdrożenia.


## Założenia

- Dostępne są polityki i rejestry systemów; istnieje sponsor governance; narzędzia mogą być skonfigurowane.


## Otwarte pytania

- Jakie dodatkowe wymogi branżowe (np. finansowe/medyczne/energetyczne)?  
- Jakie SLA raportowania jakości i kto je odbiera (exec/ops/audit)?


## Powiązania (meta)

- Key Documents: data_strategy, data_classification, privacy_policy, security_baseline, access_control_sod, data_quality_policy, retention_policy, tprm_policy, lineage_standards.
- Key Document Structures: role, polityki, metryki, procesy, audyt.
- Document Dependencies: IdP/IAM, catalog/lineage tools, DQ tools, DLP, logging/audit, TPRM register.


## Zależności dokumentu

Wymaga: strategii danych, klasyfikacji, polityk privacy/security/retencji, rejestru systemów/pipeline, wymagań regulacyjnych, narzędzi catalog/lineage/DQ/DLP, rejestru TPRM. Bez tego DoR pozostaje otwarte.


## Fazy cyklu życia

- Definicja (role, polityki, metryki, narzędzia).
- Implementacja (catalog/lineage/DQ/DLP, access/SoD, metryki).
- Operacje i monitorowanie (raporty jakości, audyt, incydenty danych).
- Przeglądy okresowe i doskonalenie (lekcje, aktualizacje polityk/metryk).



## Struktura sekcji (szkielet)
- Cel i kontekst biznesowy
- Interesariusze, persony i scenariusze
- Wymagania funkcjonalne (priorytety, reguły, wyjątki)
- Wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo, zgodność)
- Dane i integracje
- Kryteria akceptacji i miary sukcesu
- Zależności, ryzyka i założenia
- Śledzenie (traceability) do epik/testów
## Szybkie powiązania

- linkage_index.jsonl (data/governance_requirements)
- data_strategy, data_classification, privacy_policy, security_baseline, access_control_sod, data_quality_policy, retention_policy, tprm_policy, lineage_standards


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 20546** — Technologie Informacyjne — Big Data
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
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

1. Uzupełnij role, klasyfikację i polityki; zdefiniuj metryki/SLO.  
2. Opisz procesy (change/sharing/exception/access review) i narzędzia.  
3. Dodaj TPRM, audyt/raportowanie, plan wdrożenia; zamknij DoR/DoD i wpisz do linkage_index.


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

- Brak klasyfikacji/rol → niespójne dostępy; brak metryk → brak kontroli jakości; brak SoD/access review → ryzyko nadużyć; brak audit trail → ryzyko compliance.


## Decyzje i uzasadnienia

- [Decyzja] Zestaw metryk/SLO i progi; [Decyzja] Narzędzia i integracje; [Decyzja] Cykl przeglądów/audytów; [Decyzja] Waivery i sunset.


## Powiązania z innymi dokumentami

- data_strategy, data_classification, privacy_policy, security_baseline, access_control_sod, data_quality_policy, retention_policy, tprm_policy, lineage_standards.


## Powiązania z sekcjami innych dokumentów

- Access Control/SoD → polityki dostępu; Retention → polityki retencji; DQ → metryki; TPRM → dostawcy danych; Security/Privacy → kontrole.


## Słownik pojęć w dokumencie

- Data Owner/Steward/Custodian, SoD, Lineage, DQ, DLP, SLO, KPI/KRI, Waiver, Sunset.


## Wymagane odwołania do standardów

- GDPR/CCPA, PCI/HIPAA/branżowe jeśli dotyczy; firmowe polityki danych/bezpieczeństwa/audytu.


## Mapa relacji sekcja→sekcja

- Klasyfikacja/role → Polityki → Metryki/SLO → Procesy → Narzędzia → Audyt → Waivery.


## Mapa relacji dokument→dokument

- Data Governance Requirements ↔ data_strategy/data_classification/privacy/security/retention/tprm/access_control_sod/lineage_standards.


## Ścieżki informacji

- Strategia/klasyfikacja → Polityki → Metryki → Procesy → Narzędzia → Raporty/Audyt → Przeglądy → Aktualizacje.


## Weryfikacja spójności

- [ ] Klasyfikacja spójna z politykami i access/SoD; metryki mają źródła i progi.  
- [ ] Procesy mają SLA/dowody; wyjątki mają sunset/kompensacje.  
- [ ] Narzędzia i integracje pokrywają wymagania; raporty/audyt zaplanowane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- RACI, matryca klasyfikacji, polityki (access/privacy/retention/sharing), definicje metryk/SLO, procesy i checklisty, katalog/lineage/DQ/DLP wymagania, TPRM rejestr, dashboard KPI/KRI, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Coverage klasyfikacji, % systemów w katalogu/lineage, SLO jakości spełnione, czas zamykania incydentów danych, liczba waiverów i ich sunset, status audytów.

## Kryteria ukończenia

- [ ] Wymagania governance opisane i powiązane z metrykami/procesami/narzędziami; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Role/klasyfikacja → Polityki → Metryki/SLO → Procesy zmian/sharing → Narzędzia → Audyt/raportowanie → Waivery.


## Struktura sekcji

1) Streszczenie i zakres (domeny, jurysdykcje, ryzyka)  
2) Role i odpowiedzialności (Owner/Steward/Custodian/Consumer, RACI)  
3) Klasyfikacja danych i polityki (access, privacy, retention, sharing/consent)  
4) Standardy jakości danych i metryki/SLO (definicje, progi, źródła)  
5) Procesy i kontrole (change mgmt dla danych, SoD, access reviews, data sharing, exception/waiver)  
6) Narzędzia i integracje (catalog, lineage, DQ, DLP, IAM, logging/audit)  
7) TPRM i dostawcy danych (oceny, umowy, due diligence)  
8) Audyt, monitoring, raportowanie (cykl, dashboardy, KPI/KRI)  
9) Plan wdrożenia i harmonogram przeglądów  
10) Załączniki (słownik definicji danych, wzory raportów, checklisty)


## Wymagane rozwinięcia

- RACI ról governance; matryca klasyfikacji i polityki na klasy.  
- Definicje metryk (completeness/accuracy/timeliness/consistency/uniqueness) i progi/SLO; źródła danych metryk.  
- Proces change/sharing/exception z krokami, SLA i dowodami; access review/SoD cykl.  
- Wymagania narzędzi (catalog/lineage/DQ/DLP) i integracje z IAM/CI/CD.  
- Plan audytów/raportów (kto, kiedy, KPI/KRI, odbiorcy).


## Wymagane streszczenia

- Executive: role, top polityki, top metryki/SLO, kluczowe ryzyka i plan wdrożenia.  
- One-pager: mapa polityk na klasy danych, cykl przeglądów, narzędzia i raporty.


## Guidance (skrót)

- Zacznij od klasyfikacji i ról; bez tego polityki i metryki są niespójne.  
- Ustal mierzalne SLO jakości i źródła danych; raportuj regularnie.  
- Zapewnij SoD i access review cyklicznie; wyjątki muszą mieć sunset/kompensacje.  
- Automatyzuj katalog/lineage/DQ gdzie to możliwe; integruj z IAM i CI/CD.  
- TPRM: wymagaj dowodów zgodności i jakości danych od dostawców; utrzymuj audyt.


## Checklisty Definition of Ready (DoR)

- [ ] Strategia danych/klasyfikacja/polityki privacy-security-retention dostępne.  
- [ ] Rejestr systemów/pipeline i wymagania regulacyjne zebrane.  
- [ ] Narzędzia catalog/lineage/DQ/DLP/IAM zidentyfikowane; ownerzy ról wskazani.


## Checklisty Definition of Done (DoD)

- [ ] Role/RACI, polityki i metryki/SLO opisane; procesy change/sharing/exception/access review zdefiniowane.  
- [ ] Wymagania narzędzi i integracje zapisane; audyt/raportowanie zaplanowane.  
- [ ] TPRM i waivery z sunset/kompensacjami udokumentowane; dokument w linkage_index.

