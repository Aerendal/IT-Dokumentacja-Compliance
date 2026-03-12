---
title: Hyperautomation Metrics
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Hyperautomation Metrics


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje metryki, KPI/KRI i sposób pomiaru skuteczności programów hyperautomation (RPA + workflow + AI/ML + integracje). Ma umożliwić śledzenie wartości biznesowej, stabilności technicznej, ryzyk oraz zgodności.


## Zakres i granice

- Obejmuje: metryki biznesowe (oszczędność czasu/kosztu, SLA), operacyjne (awarie botów, retraje, lead time), jakościowe (defekt rate, accuracy ML), zgodności (audit trail, segregacja obowiązków), bezpieczeństwa (uprzywilejowane dane/dostępy), adopcji i zmian (liczba procesów włączonych, satysfakcja użytkowników).
- Poza zakresem: szczegółowe procedury budowy botów/procesów, pełne modele finansowe.


## Użytkownicy i interesariusze

- Automation CoE, Ops/SRE, Business Owners, Security/Compliance, Finance/FinOps.


## Wejścia i wyjścia

- Wejścia: katalog procesów z automatyzacją, definicje SLA/KPI biznesowych, logi RPA/orkiestratora, monitoring ML, dane kosztowe, polityki compliance (SoD, audyt), dane o incydentach.
- Wyjścia: zestaw metryk/KPI/KRI, definicje źródeł danych, dashboardy, progi/alerty, raporty cykliczne, kryteria go/hold dla nowych automatyzacji.


## Założenia

- Orkiestrator/logi dostępne; dane kosztowe z FinOps/ERP.
- Polityka SoD i audytu jest zdefiniowana.


## Otwarte pytania

- Czy mierzymy efekty uboczne (shadow IT, manual overrides)?
- Jak często rewizja progów i dashboardów?


## Powiązania (meta)

- Key Documents: automation_strategy, rpa_governance, ml_ops, security_baseline, change_management.
- Key Document Structures: katalog procesów, metryki, progi, alerty, raportowanie.
- Document Dependencies: monitoring/observability, CMDB procesów, IAM/SoD, koszt/FinOps.


## Zależności dokumentu

Wymaga aktualnego katalogu procesów i ich właścicieli, źródeł logów (orkiestrator, ML, API), kosztów (licencje, infra), wymagań SoD/audytu i polityki danych. Brak danych blokuje DoR.


## Fazy cyklu życia

- Planowanie: wybór metryk/KPI, progi, źródła danych.
- Implementacja: instrumentacja logów, zasilenie dashboardów, alerty.
- Operacje: monitoring ciągły, raporty cykliczne, aktualizacja progów.
- Retrospektywa: analiza trendów, decyzje o rozbudowie/wycofaniu automatyzacji.



## Struktura sekcji (szkielet)

- Podsumowanie wykonawcze
- Kluczowe metryki i KPI
- Trendy i analiza
- Problemy i rekomendacje
- Kolejne kroki

## Szybkie powiązania

- linkage_index.jsonl (automation/metrics)
- rpa_governance, ml_ops, security_baseline, change_management, finops


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

1. Zbierz katalog procesów i dane źródłowe metryk.
2. Zdefiniuj KPI/KRI, progi i alerty; przypisz właścicieli.
3. Skonfiguruj dashboardy/widoki; opisz raportowanie cykliczne.
4. Wypełnij DoR/DoD; aktualizuj przy każdej większej zmianie automatyzacji.


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

- Throughput botów, Retry rate, Bot MTTR, Automation SLA, Drift ML, SoD hit.


## Przykłady użycia

- Raport miesięczny value i awaryjności dla zarządu.
- Alert: wzrost retraje > próg → analiza przyczyny i rollback wersji bota.


## Ryzyka i ograniczenia

- Metryki bez spójnych źródeł lub definicji → mylne decyzje.
- Brak SoD/audytu → ryzyko naruszeń compliance.


## Decyzje i uzasadnienia
- Wybór metryk/SLO na dashboardzie.  
- Progi i kanały eskalacji.  
- Layout (kolejność, grupowanie).  
- Retencja i wersjonowanie zmian.
## Powiązania z innymi dokumentami

- Automation Strategy, RPA Governance, ML Ops Runbook, Security Baseline, Change Mgmt.


## Powiązania z sekcjami innych dokumentów

- ML Ops → accuracy/drift; Security/SoD → access metrics; FinOps → cost/value.


## Słownik pojęć w dokumencie

- KPI/KRI, SLA/SLO, Drift, Retry, MTTR, SoD, Audit trail.


## Wymagane odwołania do standardów

- Polityki SoD, audyt (np. SOC2/ISO), wymagania prywatności danych procesów.


## Mapa relacji sekcja→sekcja

- Procesy → Metryki → Progi/alerty → Dashboardy → Decyzje → Action plan.


## Mapa relacji dokument→dokument

- Hyperautomation Metrics → Automation Strategy → Change/Release → Audit/Compliance.


## Ścieżki informacji

- Logi/monitoring → Agregacja → Dashboardy/alerty → Decyzje → Retrospektywa.


## Weryfikacja spójności

- [ ] Metryki mają źródła, wzory, właścicieli i progi.
- [ ] Widoki exec/ops/audit spójne; brak sprzecznych definicji.
- [ ] KRI pokrywają główne ryzyka (SoD, dane wrażliwe, awaryjność).


## Lista kontrolna spójności relacji

- [ ] Każdy proces ma metryki biznes/ops/quality lub N/A z uzasadnieniem.
- [ ] Każdy alert ma próg i właściciela reakcji.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Dashboardy (BI/observability), raporty cykliczne, definicje metryk, konfiguracje alertów.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Automation CoE → Security/Compliance → Business Owners → Exec sign‑off.


## Metryki jakości

- Coverage procesów (% z metrykami), alert fidelity (false positive/negative), aktualność danych, czas reakcji na alert, wartość biznesowa (czas/koszt saved), MTTR botów, drift ML.

## Kryteria ukończenia

- [ ] Metryki/progi/alerty działają i są raportowane.
- [ ] Dashboardy dostępne dla interesariuszy; instrukcje widoków opisane.
- [ ] Dokument powiązany w linkage_index i checklistach.


## Powiązania sekcja↔sekcja

- Katalog procesów → Metryki biznesowe/operacyjne → Dashboardy → Decyzje go/hold.
- ML accuracy → Jakość/defekty → Retrain/mitigacje.
- SoD/Access → Ryzyka/alerty → Audyt/raportowanie.


## Struktura sekcji

1) Katalog procesów i właściciele  
2) Metryki biznesowe (czas/koszt/SLA/value)  
3) Metryki operacyjne (stabilność botów, retraje, lead time, queue time)  
4) Metryki jakości (defekt rate, accuracy/precision/recall dla ML)  
5) Metryki bezpieczeństwa/compliance (SoD, uprzywilejowane dane, audit trail)  
6) Metryki adopcji UX (NPS, satysfakcja, usage)  
7) Progi/alerty i eskalacje  
8) Dashboardy i raportowanie (widoki exec/ops/audit)  
9) Ryzyka, decyzje, action plan  


## Wymagane rozwinięcia

- Definicje metryk (wzory, okna czasowe, źródła danych, sampling).
- Progi/alerty i właściciele reakcji.
- Mapowanie proces → metryki → cel biznesowy.


## Wymagane streszczenia

- Top KPI dla zarządu (np. czas/cost saved, SLA, awaryjność, compliance hits).
- Najważniejsze ryzyka/KRI i ich progi.


## Guidance (skrót)

- Ustal minimalny zestaw core KPI (biznes, operacje, jakość, compliance, bezpieczeństwo).
- Zapewnij dane z jednego źródła prawdy (orkiestrator/monitoring/FinOps).
- Dla ML dodaj drift/accuracy i plan retrain; dla RPA stabilność i retraje.
- Oddziel widoki exec (value/ryzyka) od ops (alerty, defekty).
- Dokumentuj progi i właścicieli reakcji; automatyzuj alerty.


## Checklisty Definition of Ready (DoR)

- [ ] Katalog procesów i właściciele zebrani.
- [ ] Źródła danych/metryk dostępne; polityka danych uzgodniona.
- [ ] Metryki wstępnie zdefiniowane; brakujące oznaczone N/A.
- [ ] Progi/alerty i role reakcji uzgodnione wstępnie.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Metryki zdefiniowane ze źródłami, wzorami, oknami czasowymi.
- [ ] Progi/alerty skonfigurowane; właściciele reakcji przypisani.
- [ ] Dashboardy/raporty opisane i dostępne; linki działają.
- [ ] Ryzyka/KRI opisane; decyzje i action plan zapisane.
- [ ] Wersja/data/właściciel zaktualizowane; dokument w linkage_index.

