---
title: Mapowanie compliance
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Mapowanie compliance


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zmapować wymagania regulacyjne/standardów (GDPR/RODO, ISO, SOC, PCI, branżowe) na kontrolki, właścicieli i artefakty dowodowe w organizacji, wskazać luki, priorytety i plan remediacji.


## Zakres i granice

- Obejmuje: listę standardów/regulacji i wersji, obszary (bezpieczeństwo/dane/dostępność), tabelę wymagań → kontrolki/procesy → właściciele → dowody → status, luki/priorytety/plan remediacji, ścieżkę audytu (repo dowodów), cykl przeglądów i aktualizacji, eksport/komunikację.  
- Poza zakresem: definiowanie nowych kontrolek (w politykach/standardach) i pełne audyty techniczne (oddzielne raporty).


## Użytkownicy i interesariusze
- Legal/Compliance, Security/Privacy, Product/Engineering, Audit, TPRM/Vendor Mgmt.
## Wejścia i wyjścia

- Wejścia: SoA/katalog wymagań, polityki/standardy, wyniki audytów/testów, repo dowodów, właściciele kontroli, wymagania klienta/regulatora.  
- Wyjścia: tabela mapowania z RAG, lista luk i plan remediacji (owner/ETA), waivery z sunset, eksport dla audytu/klientów, harmonogram przeglądów.


## Założenia
- Legal/Compliance zapewnia interpretację; dane/flow są aktualne; istnieją polityki security/privacy.
## Otwarte pytania
- Jakie raporty regulacyjne (format/SLA/kanał) są wymagane? 
- Czy istnieją dodatkowe wymogi sektorowe (fin/health/public/ot)?
## Powiązania (meta)

- Key Documents: compliance_with_regulations, compliance_verification, compliance_monitoring_runbook/tools, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference, data_privacy_compliance.
- Key Document Structures: wymagania, kontrolki, dowody, status, luki/remediacja, audyt/eksport.
- Document Dependencies: repo dowodów, GRC/ticketing, SIEM/logi, skany/testy, właściciele kontroli.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)
1. Dane i zgody (lawful basis, PII, retencja, anonimizacja).
2. Dokumentacja modeli (model card, dane treningowe, metryki, ograniczenia).
3. Monitorowanie i audyt (bias/drift, logging decyzji, reproducibility).
4. Bezpieczeństwo i dostęp (mode registry, podpisy, kontrola wersji).
5. Regulacje/specjalne wymagania branż (med/fin/public), AI Act gdy dotyczy.
## Szybkie powiązania

- linkage_index.jsonl (compliance/mapping)
- compliance_with_regulations, compliance_verification, compliance_monitoring_runbook/tools, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference, data_privacy_compliance


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
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

1. Wypisz standardy i zakres; zbuduj tabelę wymagań→kontroli→dowodów→statusów.  
2. Oznacz luki/waivery i plan remediacji; podlinkuj repo dowodów.  
3. Ustal cadence przeglądów i eksportów; zaktualizuj linkage_index/checklisty.


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

- [ ] Każde wymaganie ma kontrolę/dowód/status; waivery mają sunset.  
- [ ] Luki mają plan remediacji; repo dowodów aktualne; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Tabela mapowania, repo dowodów, raporty skanów/testów, waiver log, risk register wpisy, eksporty CSV/JSON/PDF, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Legal/Compliance → Security/Privacy → Product/Engineering → Audit/Owner sign‑off.
## Metryki jakości

- % wymagań z dowodem, liczba luk i czas zamknięcia, liczba waiverów i czas sunset, terminowość przeglądów, kompletność eksportów.

## Kryteria ukończenia

- [ ] Mapowanie aktualne, luki/waivery opisane, eksporty gotowe; wersja/data/właściciel aktualne; dokument w linkage_index.


## Struktura sekcji

1) Zakres standardów/regulacji (lista, wersje, obszary, systemy/dane w scope)  
2) Tabela mapowania: wymaganie → kontrola/proces → właściciel → dowód (lokalizacja) → status (RAG)  
3) Luki, priorytety i plan remediacji (owner, ETA, koszt/ryzyko, waivery z sunset)  
4) Ścieżka audytu i repo dowodów (lokalizacja, wersjonowanie, dostęp)  
5) Monitoring i aktualizacje (cadence, trigger na zmiany regulacji, zmiany architektury)  
6) Komunikacja i eksport (odbiorcy: audyt, klienci, zarząd; formaty: CSV/JSON/PDF)  
7) Załączniki (export tabeli, raporty skanów/testów, waiver log)


## Wymagane rozwinięcia

- Tabela mapowania z RAG, ownerami, dowodami i linkami; kryteria statusu.  
- Priorytetyzacja luk (ryzyko/impact) i plan remediacji; waivery z sunset/kompensacjami.  
- Repo dowodów i zasady wersjonowania/dostępu; harmonogram przeglądów.


## Wymagane streszczenia

- Executive: status RAG, top luki/waivery, plan remediacji i ETA, zakres standardów w scope.


## Guidance (skrót)

- Każde wymaganie musi mieć kontrolę i dowód; brak dowodu = luka.  
- Ustal kryteria RAG i aktualizuj po audytach/testach/zmianach regulacji.  
- Waivery zawsze z sunset i kompensacją; aktualizuj risk register.  
- Eksport/komunikacja: przygotuj widoki dla audytu/klientów/zarządu.


## Checklisty Definition of Ready (DoR)

- [ ] SoA/katalog wymagań dostępny; repo dowodów wskazane; ownerzy kontroli znani.  
- [ ] Kryteria RAG ustalone; format tabeli/eksportu uzgodniony.


## Checklisty Definition of Done (DoD)

- [ ] Tabela mapowania kompletna; luki/waivery opisane z owner/ETA/sunset; repo dowodów zaktualizowane.  
- [ ] Plan remediacji i eksport przygotowane; dokument w linkage_index; metadane aktualne.

