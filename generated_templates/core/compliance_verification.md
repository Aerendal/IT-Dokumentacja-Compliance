---
title: Compliance Verification
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Compliance Verification


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać, jak weryfikujemy zgodność systemu/projektu z wymaganiami (regulacyjnymi, standardami, politykami): kontrole, testy, dowody, wyniki i plan remediacji.


## Zakres i granice

- Obejmuje: standardy/zakres, metody weryfikacji (kontrole automatyczne, przeglądy, testy), artefakty/dowody, status (pass/partial/fail/RAG), plan remediacji i waivery z sunset.
- Poza zakresem: definicja samych wymagań i projektowanie kontroli (opisane w politykach/standardach).


## Użytkownicy i interesariusze
- Legal/Compliance, Security/Privacy, Product/Engineering, Audit, TPRM/Vendor Mgmt.
## Wejścia i wyjścia

- Wejścia: katalog wymagań/kontroli, standardy (SOC2/ISO/PCI/HIPAA/GDPR/… lub wewnętrzne), wyniki skanów/testów, logi audytu, polityki/procedury, lista właścicieli kontroli.
- Wyjścia: raport weryfikacji (status, dowody), lista braków i plan remediacji (owner/ETA), waivery z sunset, decyzje go/conditional/no‑go, aktualizacje risk register.


## Założenia
- Legal/Compliance zapewnia interpretację; dane/flow są aktualne; istnieją polityki security/privacy.
## Otwarte pytania
- Jakie raporty regulacyjne (format/SLA/kanał) są wymagane? 
- Czy istnieją dodatkowe wymogi sektorowe (fin/health/public/ot)?
## Powiązania (meta)

- Key Documents: compliance_monitoring_runbook, compliance_monitoring_tools, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference, data_privacy_compliance.
- Key Document Structures: wymagania/kontrole, metody/testy, dowody, status, remediacja/waivery.
- Document Dependencies: SIEM/logi, CI/CD/IaC scans, DLP, CMDB/IAM, ticketing, katalog kontroli.


## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia

- Przygotowanie: zakres/standardy, lista kontroli i dowodów, właściciele.  
- Wykonanie: testy/skany/przeglądy, zbieranie dowodów.  
- Ocena: status RAG, brakujące kontrole, waivery.  
- Remediacja i follow‑up: action items, retesty, aktualizacja risk register.



## Struktura sekcji (szkielet)
1. Dane i zgody (lawful basis, PII, retencja, anonimizacja).
2. Dokumentacja modeli (model card, dane treningowe, metryki, ograniczenia).
3. Monitorowanie i audyt (bias/drift, logging decyzji, reproducibility).
4. Bezpieczeństwo i dostęp (mode registry, podpisy, kontrola wersji).
5. Regulacje/specjalne wymagania branż (med/fin/public), AI Act gdy dotyczy.
## Szybkie powiązania

- linkage_index.jsonl (compliance/verification)
- compliance_monitoring_runbook, compliance_monitoring_tools, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference, data_privacy_compliance


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
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

1. Zdefiniuj zakres/standardy i listę kontroli/dowodów.  
2. Przeprowadź testy/przeglądy/skany, zbierz dowody i wypełnij tabelę statusów.  
3. Dodaj plan remediacji/waivery i decyzje; zaktualizuj linkage_index/checklisty.


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

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

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

- [ ] Każda kontrola ma metodę, dowód, status i ownera; waivery mają sunset.  
- [ ] Plan remediacji powiązany z brakami; retesty zaplanowane.  
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Tabela kontroli/statusów, raporty skanów/testów, logi audytu, repo dowodów, action items, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Legal/Compliance → Security/Privacy → Product/Engineering → Audit/Owner sign‑off.
## Metryki jakości

- % kontroli pass, liczba waiverów i czas sunset, czas zamknięcia braków, pokrycie dowodów, terminowość retestów.

## Kryteria ukończenia

- [ ] Status RAG i plan remediacji opublikowane; dowody kompletne; dokument w linkage_index; wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Wymagania/zakres → Metody/testy → Dowody → Status → Remediacja/waivery → Raport.


## Struktura sekcji

1) Zakres i standardy (framework, systemy, daty, ownerzy)  
2) Metody weryfikacji (kontrole auto, przeglądy, testy; narzędzia, częstotliwość)  
3) Artefakty i dowody (lokalizacja, format, wymagania audytu)  
4) Wyniki i status (pass/partial/fail/RAG, tabela kontroli)  
5) Plan remediacji i waivery (owner, ETA, sunset, kompensacje)  
6) Decyzje i komunikacja (go/conditional/no‑go, eskalacje, raport odbiorcy)  
7) Załączniki (export kontroli, logi, raporty skanów/testów)


## Wymagane rozwinięcia

- Tabela kontroli: wymaganie, metoda, dowód, status, owner, ETA, waiver (tak/nie, sunset).  
- Kryteria RAG/pass/fail; progi dla automatycznych testów/skanów.  
- Plan retestów i częstotliwość przeglądów; repo dowodów.


## Wymagane streszczenia

- Executive: zakres/standard, status RAG, top braki/waivery, plan remediacji z ETA.


## Guidance (skrót)

- Mapuj wymagania→kontrole→dowody; bez dowodu kontrola = fail.  
- Automatyzuj testy/skany tam, gdzie możliwe; taguj dowody lokalizacją.  
- Każdy brak → action item z owner/ETA; każdy waiver → sunset/kompensacja.  
- Aktualizuj risk register, jeśli brak dotyka ryzyka.


## Checklisty Definition of Ready (DoR)

- [ ] Zakres/standardy i katalog kontroli dostępne; właściciele kontroli wskazani.  
- [ ] Repo dowodów i narzędzia testów/skanów gotowe; progi RAG wstępnie ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Kontrole ocenione; dowody zebrane/podlinkowane; status RAG zapisany.  
- [ ] Braki → action items; waivery z sunset/kompensacją; risk register zaktualizowany; dokument w linkage_index; metadane aktualne.

