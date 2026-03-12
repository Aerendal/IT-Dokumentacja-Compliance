---
title: AI Model Governance
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# AI Model Governance


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Ustanawia zasady governance dla modeli AI/ML: cykl życia, odpowiedzialności, ryzyko, zgodność, audytowalność i etyka. Ma zapewnić bezpieczne i zgodne użycie modeli.


## Zakres i granice

- Obejmuje: role (owner/steward/validator), rejestr modeli, krytyczność/ryzyko, proces approval/release, dokumentacja (model card, data sheet), dane i privacy, bias/fairness, monitorowanie jakości/drift, bezpieczeństwo modeli (supply chain, skany, signing), audyt/ślady decyzji, incident response ML, retencja i decommission, zgodność (regulacje AI, branżowe).
- Poza zakresem: trening i tuning konkretnych modeli (oddzielne plany), architektura serving (link).


## Użytkownicy i interesariusze

- Data/ML, Security/Privacy, Legal/Compliance, Risk, Product/Business.


## Wejścia i wyjścia

- Wejścia: strategia AI, katalog modeli, polityki privacy/security, standardy dokumentacji, rejestr danych, wymagania regulacyjne (AI Act/sector), ryzyka biznesowe, narzędzia registry/CI/CD/monitoring.
- Wyjścia: polityki governance, RACI, procesy approval/release/decommission, wymagania dokumentacji (model card/data sheet), kryteria risk tiering, wymagania bezpieczeństwa, monitoring i audyt, plan IR ML.


## Założenia

- Narzędzia registry/monitoring istnieją; polityki privacy/security obowiązują.


## Otwarte pytania

- Jakie regulacje (AI Act/branżowe) musimy spełnić? 
- Jaki cykl przeglądów i re‑approval?


## Powiązania (meta)

- Key Documents: model_card, data_sheet, model_registry_policy, observability_ml, data_quality_policy, security_baseline_ml, incident_response_ml, privacy_policy, risk_management_plan.
- Key Document Structures: role, procesy, risk tiering, dokumentacja, monitoring, audyt.
- Document Dependencies: model registry, CI/CD, monitoring/drift, signing/SBOM, data lineage, access control, legal/regulatory register.


## Zależności dokumentu

Wymaga katalogu modeli i ryzyk, polityk privacy/security, narzędzi registry/monitoring, wymagań regulacyjnych. Bez tego DoR otwarte.


## Fazy cyklu życia

- Rejestracja modelu i risk tiering.
- Approval i dokumentacja; kontrolki bezpieczeństwa.
- Release i monitorowanie; audyt i IR.
- Decommission i archiwizacja.



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

- linkage_index.jsonl (ml/governance)
- model_card, data_sheet, model_registry_policy, observability_ml, data_quality_policy, security_baseline_ml, incident_response_ml, privacy_policy, risk_management_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

1. Zarejestruj model i wykonaj risk tiering; przygotuj dokumentację.
2. Zastosuj kontrolki security/approval; podpisz/skanuj obrazy.
3. Ustaw monitoring/drift/bias i IR ML; audytuj decyzje.
4. Przeglądaj cyklicznie regulacje i aktualizuj; domknij DoR/DoD i linkage_index.


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

- Risk tier, Model card, Data sheet, SBOM, Drift, Bias, IR ML.


## Przykłady użycia

- Model scoring kredytowy (wysoki tier): approval z Legal/Privacy, explainability, monitor bias, IR ML.
- Chatbot (średni tier): SBOM/sign, monitoring quality/drift, periodic review.


## Ryzyka i ograniczenia

- Brak governance → ryzyko prawne/etyczne; brak monitoringu → degradacja/bias; brak security → supply chain.


## Decyzje i uzasadnienia

- [Decyzja] Kryteria tiering i kontrolki — uzasadnienie ryzyka/regulacji.
- [Decyzja] Zakres dokumentacji i evidence — uzasadnienie audytu.


## Powiązania z innymi dokumentami

- Model Card, Data Sheet, Registry Policy, Observability ML, Data Quality, Security Baseline ML, Incident Response ML, Privacy, Risk Mgmt.


## Powiązania z sekcjami innych dokumentów

- Privacy → dane/DSR; Security → SBOM/sign/scan; Observability → drift/quality.


## Słownik pojęć w dokumencie

- Risk tier, Model card, Data sheet, SBOM, Drift, Bias, IR ML.


## Wymagane odwołania do standardów

- AI Act (jeśli dot.), ISO/IEC AI wytyczne, privacy (RODO/CCPA), security supply chain.


## Mapa relacji sekcja→sekcja

- Tiering → Kontrolki → Dokumentacja → Monitoring → IR/Decommission.


## Mapa relacji dokument→dokument

- AI Model Governance → Privacy/Security/Observability → IR/Risk → Audit/Compliance.


## Ścieżki informacji

- Rejestracja → Tiering → Approval → Release → Monitoring → IR/Audit → Decommission.


## Weryfikacja spójności

- [ ] Tiering/kontrolki/dokumentacja zdefiniowane; security/monitoring wpięte; relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy model ma tier, dokumentację, kontrolki security i monitoring.
- [ ] Każdy alert/incident ma IR ML ścieżkę i audyt.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Rejestr modeli, model cards, data sheets, SBOM/scan/sign raporty, monitoring/drift dashboardy, IR ML playbook.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Data/ML Governance → Security/Privacy → Legal/Compliance → Owner sign‑off.


## Metryki jakości

- % modeli z tier/dokumentacją/monitoringiem, czas approval, liczba incydentów ML, zgodność z regulacjami, kompletność SBOM/scan.

## Kryteria ukończenia

- [ ] Governance opisane; monitoring/IR/tiers/dokumentacja zdefiniowane; dokument w linkage_index; wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Risk tiering → Approval/controls → Monitoring/audyt.
- Dokumentacja (model card/data sheet) → Release/registry → Monitoring/IR.


## Struktura sekcji

1) Role i RACI (owner, steward, validator, security, privacy)  
2) Rejestr modeli i risk tiering (krytyczność, wpływ, dane)  
3) Dokumentacja (model card, data sheet, decyzje, explainability)  
4) Bezpieczeństwo modeli (supply chain, signing/SBOM, scanning, access)  
5) Approval/release/deployment (gates, evidence, change)  
6) Monitoring/drift/bias i alerty (metryki, progi, runbook)  
7) Incident response ML i audit trail  
8) Decommission/retencja i archiwizacja  
9) Zgodność/regulacje i przeglądy  
10) Ryzyka, decyzje, open issues


## Wymagane rozwinięcia

- Kryteria risk tiering i kontrolki per tier; proces approval/gates.
- Wymagania dokumentacji (model card, data sheet) i evidence.
- Wymagania security (SBOM/signing/scans) i monitoring (drift/bias/quality).


## Wymagane streszczenia

- Risk tiering, główne kontrolki, wymagania dokumentacji, monitoring i IR.


## Guidance (skrót)

- Zrób risk tiering; wyższy tier → mocniejsze kontrolki (approval, explainability, IR).
- Wymagaj model card/data sheet i evidence; podpisuj obrazy, SBOM, skanuj.
- Monitoruj drift/bias i jakość; miej runbook IR ML i audit trail decyzji.
- Przeglądaj cyklicznie zgodność z regulacjami (np. AI Act) i privacy.


## Checklisty Definition of Ready (DoR)

- [ ] Katalog modeli i dane/ryzyka dostępne; polityki privacy/security znane.
- [ ] Narzędzia registry/CI/CD/monitoring dostępne; struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Risk tiering i kontrolki opisane; dokumentacja wymagana zdefiniowana.
- [ ] Security (SBOM/sign/scan) i monitoring/drift/bias opisane; IR ML wpięty.
- [ ] Dokument w linkage_index; wersja/data/właściciel aktualne.

