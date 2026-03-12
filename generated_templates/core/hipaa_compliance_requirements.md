---
title: HIPAA Compliance Requirements
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# HIPAA Compliance Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zapewnić i raportować zgodność z regulacjami sektorowymi (HIPAA/PCI/FERPA) poprzez kontrolki techniczne/procesowe.


## Zakres i granice

- Obejmuje: zakres danych chronionych, kontrolki (dostęp, audyt, retencja, IR), szkolenia, audyty/raporty.
- Poza zakresem: szczegółowy kod usług.


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

- Kontekst i zakres danych
- Kontrolki i właściciele
- Audyty/raporty
- Szkolenia/świadomość
- Incydenty/IR
- Ryzyka


## Szybkie powiązania
- hipaa-compliance
- compliance-requirements
- regulatory-compliance-requirements
- legal-compliance-requirements
- hipaa-compliance-training

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **HL7 FHIR** — Standard Wymiany Danych w Ochronie Zdrowia
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
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

- Wypełnij sekcje według szkieletu; jeśli sekcja N/A, uzasadnij.
- Dodaj quick-links i uzupełnij checklisty DoR/DoD w reports/checklist_atomic.jsonl.
- Po review zaktualizuj metadane, artefakty i status.


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
- Rejestr regulacji, mapping wymaganie→kontrolka→dowód, waivery, raporty.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Legal/Compliance → Security/Privacy → Product/Engineering → Audit/Owner sign‑off.
## Metryki jakości
- Liczba/istotność luk, terminowość SLA/dowodów, liczba/ważność waiver, wynik audytów, czas reakcji na zmiany regulacyjne.
## Kryteria ukończenia
- [ ] Wymagania, kontrolki, luki/waivery opisane; plan monitoringu zmian istnieje.
- [ ] Dokument w linkage_index/checklistach; wersja/data/właściciel aktualne.
## Wejścia

- Regulacje/standard
- Mapa danych chronionych
- Polityki i kontrolki
- Incydenty/audyty


## Wyjścia

- Plan/raport zgodności
- Lista kontrolek i właścicieli
- Szkolenia/świadomość
- Powiązania do logowania/IR



## Szybkie powiązania (uzupełnij)

- [ ] hipaa_compliance.md
- [ ] compliance_requirements.md
- [ ] security_compliance_matrix.md
- [ ] logging_and_audit_trail.md
- [ ] data_privacy_compliance.md
- [ ] security_policy_design.md


## Wymagane rozwinięcia / streszczenia

- Streszczenie kluczowych wymagań/ryzyk; rozwinięcia planu/raportu.


## Wymagane powiązania

- Dokumenty privacy/security/logging/audyt; runbooki incydentów; szkolenia.


## Kryteria DoR

- [ ] Zakres danych i regulacji zebrany
- [ ] Kontrolki/właściciele zmapowani
- [ ] Źródła logów/dowodów dostępne
- [ ] Plan audytu/raportowania uzgodniony


## Kryteria DoD

- [ ] Plan/raport wypełniony
- [ ] Kontrolki/szkolenia opisane
- [ ] Powiązania/quick-links dodane
- [ ] Metadane/DoR/DoD zaktualizowane


## Artefakty do załączenia

- Plan/raport
- Lista kontrolek/dowodów
- Szkolenia
- Raporty audytów


## Walidacja / testy

- Sprawdź kompletność dowodów/logów; sanity planu audytu/raportu.


## Metryki monitorowane

- Znaleziska audytu High/Med
- On-time raportowanie
- Incydenty regulatory
- Szkolenia ukończone (%)


## Utrzymanie i aktualizacje

- Przegląd wg cyklu audytów/regulacji; aktualizacja quick-links/checklist.


## Zakończenie

Po spełnieniu DoD zaktualizuj status, podlinkuj artefakty/quick-links i odhacz checklistę w reports/checklist_atomic.jsonl.
