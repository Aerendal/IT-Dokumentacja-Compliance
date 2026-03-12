---
title: Operating Model
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Operating Model


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Definiuje, jak organizacja dostarcza wartość na co dzień: struktura ról i odpowiedzialności, procesy end‑to‑end, governance, mierzenie wyników, narzędzia i rytuały operacyjne.


## Zakres i granice

- Obejmuje: model ról i RACI, procesy kluczowe i rytuały (cadence), kanały decyzyjne, governance i fora, mierniki operacyjne (KPI/KRI), narzędzia i integracje, komunikację i eskalacje, kontrolki compliance/audyt, ciągłe doskonalenie.
- Poza zakresem: szczegółowe instrukcje zadaniowe (SOP-y) oraz playbooki IR/BCP (osobne dokumenty).


## Użytkownicy i interesariusze
- ML Platform, DevOps/SRE, Security, Product/Owners modeli, FinOps.
## Wejścia i wyjścia

- Wejścia: strategia firmy/produktów, architektura (biznes/dane/IT), regulacje, dostępne role/zespoły, narzędzia, KPI historyczne, budżet.
- Wyjścia: opis modelu operacyjnego (role, procesy, rytuały, governance), RACI, kalendarz/fora, zestaw KPI/KRI i sposób pomiaru, mapa narzędzi, zasady eskalacji/komunikacji, plan doskonalenia.


## Założenia
- Registry, scanning, signing, SBOM narzędzia dostępne; model registry działa.
## Otwarte pytania
- Jak często patchować base i rescanujemy obrazy? 
- Czy wymagane warianty CPU/GPU/AVX?
## Powiązania (meta)

- Key Documents: business_architecture_vision, enterprise_architecture_vision, product_strategy_document, go_to_market_strategy, risk_register, incident_response_playbook, change_management_process, data_governance_model.
- Key Document Structures: rola → proces → narzędzie → metryka → decyzja → eskalacja.
- Document Dependencies: polityki bezpieczeństwa/compliance, regulacje HR/finanse, katalog usług/narzędzi, CMDB/ITSM.
- RACI: COO/Operations (owner), Product/Engineering, Support/Success, Security/Compliance, Finance, HR/Learning, Data/Analytics.


## Zależności dokumentu

- Upstream: strategia, architektury, regulacje, budżet i headcount, portfel inicjatyw.
- Downstream: SOP-y, runbooki, plany szkoleń, OKR/KPI dashboardy, kontrakty SLA/OLA, plany audytów.
- Zewnętrzne: dostawcy narzędzi, partnerzy BPO, regulatorzy/audytorzy.


## Fazy cyklu życia

- Zaprojektowanie modelu (rola/proces/rytuał/KPI).
- Pilotaż i dostrojenie (metryki, obciążenie, UX zespołów).
- Rollout i skalowanie (szkolenia, komunikacja, automatyzacje).
- Ciągłe doskonalenie (retrospektywy, audyty, rebalans zasobów).


## Struktura sekcji (szkielet)

1) Streszczenie i cele operacyjne (KPI/KRI)
2) Zakres i założenia (obszar, zespoły, regulacje)
3) Role i odpowiedzialności (RACI, org model, delegacje)
4) Procesy i rytuały (cadence, wejścia/wyjścia, definicje gotowości/ukończenia)
5) Governance i fora decyzyjne (agenda, uczestnicy, wejścia/wyjścia)
6) Narzędzia i integracje (ITSM/CRM/DevOps/Data/Comms), standardy danych/etkietowania
7) KPI/KRI i pomiar (dashboardy, właściciele, częstotliwość, progi)
8) Komunikacja i eskalacje (kanały, SLA/OLA, on-call, runbooki referencyjne)
9) Compliance i ryzyka (kontrolki, audyty, rejestr ryzyk, plan remediacji)
10) Szkolenia i onboarding (plan, wymagane certyfikacje, materiały)
11) Plan doskonalenia (retrospektywy, eksperymenty, automatyzacje)
12) Decyzje (ADR) i otwarte pytania


## Szybkie powiązania

- business_architecture_vision, enterprise_architecture_vision, product_strategy_document, go_to_market_strategy, risk_register, incident_response_playbook, change_management_process, data_governance_model


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów

## Standardy i compliance
### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

## RACI i role

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie dokumentu | DEV / BA | PM | BA / ARCH | OPS / SM |
| Przegląd i zatwierdzenie | PM / BA | PM | Tech Lead | OPS |
| Aktualizacja | DEV / BA | PM | BA | OPS |
| Archiwizacja | OPS | PM | BA | SM |

## Jak używać dokumentu
1. Wybierz base i zbuduj obraz wg szablonu; dodaj deps.
2. Dodaj security (SBOM/sign/scan) i observability; ustaw resources/perf.
3. W CI: build/test/scan/sign/push; rollout z canary; monitoruj metryki.
4. Patchuj base i rescanuj okresowo; aktualizuj dokument i linkage_index.
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

- System of Record — system przechowujący źródłowe dane referencyjne.
- System of Engagement — system do codziennej pracy i interakcji z klientem/użytkownikiem.
- OLA — Operational Level Agreement między zespołami wewnętrznymi.


## Przykłady użycia

- Model operacyjny dla produktu SaaS: role (PM/Eng/CS/Support), fora (triage, CAB, QBR), narzędzia (Jira/ITSM/CRM/BI), KPI (NRR, uptime, MTTR, CSAT), eskalacje on-call.
- Model dla organizacji usługowej: value stream Lead→Delivery→Support, RACI, cadence (standup/ops review/retro), KPI (utilization, on-time, NPS), kontrolki compliance.


## Ryzyka i ograniczenia
- Brak scanning/signing → ryzyko supply chain; duży obraz → wolne deploy/cold start; brak observability → trudne incydenty.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- Model Serving Architecture, Observability ML, Security Baseline Containers, SBOM Policy, CI/CD Pipeline ML, Cost Optimization ML, Data Privacy Policy.
## Powiązania z sekcjami innych dokumentów
- Security Baseline → rootless/scan/sign; Observability → metrics; Serving → rollout.
## Słownik pojęć w dokumencie
- SBOM, Signing, Rootless, Cold start, BLAS, Canary, HPA.
## Wymagane odwołania do standardów
- Polityki security kontenerów, SBOM i signing; licencje base/dep; privacy (PII) jeśli dane w obrazie.
## Mapa relacji sekcja→sekcja
- Base/deps → Security/size → Perf → Observability → Rollout.
## Mapa relacji dokument→dokument
- Model Containerization → Serving/Security/Observability/CI-CD → Release/Cost.
## Ścieżki informacji
- Artefakty → Build/Scan/Sign → Deploy → Monitor → Patch/Rescan.
## Weryfikacja spójności

- [ ] Role/procesy/fora mają właścicieli i wejścia/wyjścia.
- [ ] KPI/KRI mają źródła, progi i częstotliwość; eskalacje mają SLA/OLA.
- [ ] Narzędzia są przypisane do procesów i mają standardy danych/tagowania; plan audytów/szkoleń istnieje.

## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- RACI, kalendarz forów, runbooki referencyjne, katalog narzędzi, dashboard KPI/KRI, plan szkoleń, plan audytów, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- ML Platform/DevOps → Security → Observability/FinOps → Owner sign‑off.
## Metryki jakości
- Rozmiar obrazu, cold start p95, liczba obrazów bez SBOM/scan, czas build/scan, liczba rollbacków z powodu obrazu, koszt storage/transfer.
## Kryteria ukończenia
- [ ] Standard obrazu wdrożony; scan/sign/SBOM; perf/observability/resource opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

- Rola/RACI → Procesy/Rytuały → Narzędzia → KPI/KRI → Eskalacje/fora → Doskonalenie.
- Compliance/ryzyka → Kontrolki → Monitoring → Audyt.


## Wymagane rozwinięcia

- RACI map, kalendarz forów i rytuałów (z wejściami/wyjściami), definicje eskalacji i runbooki referencyjne.
- Zestaw KPI/KRI z progami, właścicielami i metodą pomiaru; dashboardy.
- Mapa narzędzi (system-of-record vs system-of-engagement) i integracji, standardy danych/tagowania.
- Plan szkoleń/onboardingu oraz plan audytów/compliance.


## Wymagane streszczenia

- Executive summary: cele, główne role/fora, kluczowe KPI/KRI, kalendarz operacyjny.
- One-pager: kto/co/kiedy/jak mierzone, eskalacje i kanały.


## Guidance (skrót)

- DoR: zdefiniowane cele operacyjne/KPI, zakres zespołów, znane regulacje i narzędzia bazowe, wstępny RACI i lista forów.
- DoD: role/procesy/rytuały opisane; governance/fora i eskalacje zdefiniowane; KPI/KRI z progami; narzędzia i integracje przypisane; plan szkoleń/audytów; dokument w linkage_index.
- Spójność: każde wejście ma właściciela i kanał; każde KPI ma źródło i częstotliwość; eskalacje mają SLA/OLA i runbook referencyjny.


## Checklisty Definition of Ready (DoR)

- [ ] Cele operacyjne/KPI i zakres zespołów uzgodnione; regulacje/ograniczenia znane.
- [ ] Wstępny RACI, lista forów i narzędzi bazowych zidentyfikowane.


## Checklisty Definition of Done (DoD)

- [ ] Opisany model ról/procesów/rytuałów/governance; KPI/KRI z progami i właścicielami.
- [ ] Kalendarz forów/escalacji, mapa narzędzi, plan szkoleń i audytów; dokument w linkage_index.

