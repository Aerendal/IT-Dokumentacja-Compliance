---
title: Legal Compliance Requirements
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Legal Compliance Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zbiera wymagania prawne i regulacyjne dla produktu/usługi (jurysdykcje, branże), przekłada je na wymagania funkcjonalne/niefunkcjonalne i kontrolki techniczne/organizacyjne. Ma zapewnić zgodność, audytowalność i zmniejszyć ryzyko prawne.


## Zakres i granice

- Obejmuje: identyfikację jurysdykcji i regulacji (privacy, sektorowe, finansowe, zdrowie, bezpieczeństwo), wymagania danych (retencja, lokalizacja, DSR), bezpieczeństwo (IAM, logi, szyfrowanie), dostępność/UX (np. ADA/WCAG), sprawozdawczość i dowody, TPRM/umowy, proces zmian i monitoringu regulacji.
- Poza zakresem: interpretacja prawna w szczegółach (prowadzi Legal) – tutaj wymagania dla IT/produkt.


## Użytkownicy i interesariusze

- Legal/Compliance, Security/Privacy, Product/Engineering, Audit, TPRM/Vendor Mgmt.


## Wejścia i wyjścia

- Wejścia: lista jurysdykcji/rynków, regulacje (RODO/CCPA/DORA/NIS2/PCI/HIPAA/sector), kontrakty/SLA, dane/flow, modele biznesowe, polityki privacy/security, TPRM, risk register.
- Wyjścia: katalog wymagań legal/compliance (funkcyjne/niefunkcyjne), mapowanie na kontrolki/artefakty, właściciele i SLA, plan wdrożenia, lista luk i waivers z datami, plan monitoringu zmian regulacyjnych.


## Założenia

- Legal/Compliance zapewnia interpretację; dane/flow są aktualne; istnieją polityki security/privacy.


## Otwarte pytania

- Jakie raporty regulacyjne (format/SLA/kanał) są wymagane? 
- Czy istnieją dodatkowe wymogi sektorowe (fin/health/public/ot)?


## Powiązania (meta)

- Key Documents: privacy_policy, data_classification, key_management_policy, audit_logging, tprm_policy, accessibility_standards, security_baseline, incident_response_plan, drp_bcp, regulatory_reporting.
- Key Document Structures: regulacje, wymagania, kontrolki, luki, plan.
- Document Dependencies: CMDB/data flows, IAM/KMS/logging, monitoring, change mgmt, legal registry, TPRM register.


## Zależności dokumentu

Wymaga: listy regulacji/jurysdykcji, danych/flow, polityk security/privacy, rejestru TPRM, właścicieli domen. Bez tego DoR otwarte.


## Fazy cyklu życia

- Identyfikacja regulacji/jurysdykcji i zakresu.
- Mapowanie wymagań na kontrolki/artefakty (w IT/produkt/procesy).
- Ocena luk i plan działań; waivery z datą.
- Monitorowanie i przeglądy cykliczne; aktualizacja.



## Struktura sekcji (szkielet)
1. Dane i zgody (lawful basis, PII, retencja, anonimizacja).
2. Dokumentacja modeli (model card, dane treningowe, metryki, ograniczenia).
3. Monitorowanie i audyt (bias/drift, logging decyzji, reproducibility).
4. Bezpieczeństwo i dostęp (mode registry, podpisy, kontrola wersji).
5. Regulacje/specjalne wymagania branż (med/fin/public), AI Act gdy dotyczy.
## Szybkie powiązania

- linkage_index.jsonl (compliance/legal_requirements)
- privacy_policy, data_classification, key_management_policy, audit_logging, tprm_policy, accessibility_standards, security_baseline, incident_response_plan, drp_bcp, regulatory_reporting


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
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

1. Zbierz regulacje/jurysdykcje i dane/flow; wypełnij sekcje wymagań.
2. Mapuj wymagania na kontrolki/artefakty i właścicieli; wpisz SLA i dowody.
3. Zidentyfikuj luki/waivery i plan działań; ustaw monitoring zmian.
4. Zamknij DoR/DoD; dodaj dokument do linkage_index.


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

- Jurysdykcja, Waiver, DSR, AOC, Accessibility (WCAG), Regulatory reporting.


## Przykłady użycia

- Nowy rynek UE: RODO/DSR, lokalizacja danych, accessibility, AOC dostawców.
- Produkt finansowy: PCI DSS + raporty regulacyjne, SoD, logi/audyt.


## Ryzyka i ograniczenia

- Niepełne mapowanie → kary; waivery bez dat → trwałe ryzyko; brak dowodów → audyt niezaliczony.


## Decyzje i uzasadnienia

- [Decyzja] Zakres regulacji i priorytety — uzasadnienie ryzyka/rynku.
- [Decyzja] SLA/dowody i właściciele — uzasadnienie audytu/compliance.


## Powiązania z innymi dokumentami

- Privacy Policy, Data Classification, Key Management, Audit Logging, TPRM, Accessibility Standards, Security Baseline, Incident Response, DRP/BCP, Regulatory Reporting.


## Powiązania z sekcjami innych dokumentów

- Privacy → DSR/retencja; Security → IAM/crypto/logi; TPRM → umowy.


## Słownik pojęć w dokumencie

- Jurysdykcja, Waiver, DSR, AOC, Accessibility, Regulatory reporting.


## Wymagane odwołania do standardów

- RODO/CCPA, PCI, HIPAA/sector, DORA/NIS2 jeśli dotyczy, WCAG.


## Mapa relacji sekcja→sekcja

- Regulacje → Wymagania → Kontrolki → Luki/Waivery → Plan/Monitoring.


## Mapa relacji dokument→dokument

- Legal Requirements → Privacy/Security/Accessibility/TPRM → Audit/Reporting.


## Ścieżki informacji

- Regulacje → Wymagania/Kontrolki → Dowody → Raporty → Monitorowanie zmian.


## Weryfikacja spójności

- [ ] Wymagania mają kontrolki/właścicieli/SLA; dowody i waivery opisane.
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każde wymaganie ma kontrolkę, owner, SLA, dowód; waivery mają datę i kompensację.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Rejestr regulacji, mapping wymaganie→kontrolka→dowód, waivery, raporty.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Legal/Compliance → Security/Privacy → Product/Engineering → Audit/Owner sign‑off.


## Metryki jakości

- Liczba/istotność luk, terminowość SLA/dowodów, liczba/ważność waiver, wynik audytów, czas reakcji na zmiany regulacyjne.

## Kryteria ukończenia

- [ ] Wymagania, kontrolki, luki/waivery opisane; plan monitoringu zmian istnieje.
- [ ] Dokument w linkage_index/checklistach; wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Regulacje → Wymagania → Kontrolki/artefakty → Luki/waivery → Plan i monitoring.
- Dane/flow → Lokalizacja/retencja/DSR → Kontrolki.


## Struktura sekcji

1) Jurysdykcje i regulacje (lista, zakres, obowiązki)  
2) Wymagania i kontrolki (funkcyjne/niefunkcyjne, artefakty, właściciele, SLA)  
3) Dane i przepływy (lokalizacja, retencja, DSR, privacy by design)  
4) Dostępność/UX i dostępność cyfrowa (np. WCAG/ADA)  
5) Bezpieczeństwo i logowanie/audyt (IAM, szyfrowanie, logi, monitoring)  
6) Raportowanie/regulatory reporting (SLA, formaty, kanały)  
7) TPRM/umowy (AOC/SOC2/PCI, licencje, zobowiązania kontraktowe)  
8) Luki i waivery (kompensacje, daty przeglądów)  
9) Plan działań i monitoring zmian regulacyjnych  
10) Ryzyka, decyzje, open issues


## Wymagane rozwinięcia

- Mapowanie regulacji → kontrolki/artefakty i właściciele; SLA/Due dates.
- Lista danych/flow i wymagania lokalizacji/retencji/DSR; privacy by design.
- Rejestr luk/waiver z datą końca i kompensacją; plan przeglądów.


## Wymagane streszczenia

- Kluczowe regulacje i wymagania, top luki/waivery, plan działań i SLA.


## Guidance (skrót)

- Zacznij od jurysdykcji i danych/flow; mapuj regulacje na kontrolki IT/produkt.
- Ustal właścicieli i SLA dla wymagań; dokumentuj dowody (audit trail).
- Używaj privacy by design i accessibility by design; aktualizuj przy zmianach produktu/rynków.
- Monitoruj zmiany regulacyjne; przeglądy cykliczne i waivery z datą.


## Checklisty Definition of Ready (DoR)

- [ ] Lista regulacji/jurysdykcji i dane/flow dostępne; właściciele domen znani.
- [ ] Polityki security/privacy/accessibility dostępne; TPRM rejestr.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Wymagania i kontrolki opisane; właściciele/SLA i dowody zdefiniowane.
- [ ] Luki/waivery z datami i kompensacją; plan monitoringu zmian.
- [ ] Dokument w linkage_index; wersja/data/właściciel aktualne.

