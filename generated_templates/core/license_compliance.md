---
title: License Compliance
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# License Compliance


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnić zgodność licencyjną oprogramowania (OSS/proprietary) w projekcie/produkcie: polityka licencji, SBOM, proces zatwierdzania zależności, zobowiązania (NOTICE/attribution/src), ryzyka i remediacja, audyt.


## Zakres i granice

- Obejmuje: komponenty OSS/proprietary, politykę licencji (dozwolone/zakazane/warunkowe, copyleft, dual licensing), SBOM, proces skanów/approvals/wyjątków, zobowiązania (NOTICE/ACK/source offer), ryzyka (konflikty, EOL, podatności), raporty/audyt.
- Poza zakresem: pełna ocena podatności (oddzielne), negocjacje komercyjnych umów (Legal prowadzi).


## Użytkownicy i interesariusze
- Legal/Compliance, Security/Privacy, Product/Engineering, Audit, TPRM/Vendor Mgmt.
## Wejścia i wyjścia

- Wejścia: lista zależności, SBOM narzędzia/raporty, polityka licencyjna, lista dozwolonych/zakazanych, wyniki skanów SCA, umowy komercyjne, wymagania klienta/regulatora.
- Wyjścia: SBOM i raport zgodności, decyzje dot. zależności (approve/deny/exception), lista zobowiązań (NOTICE/attribution/source offer), log wyjątków i sunset, plan remediacji konfliktów.


## Założenia
- Legal/Compliance zapewnia interpretację; dane/flow są aktualne; istnieją polityki security/privacy.
## Otwarte pytania
- Jakie raporty regulacyjne (format/SLA/kanał) są wymagane? 
- Czy istnieją dodatkowe wymogi sektorowe (fin/health/public/ot)?
## Powiązania (meta)

- Key Documents: open_source_policy, third_party_software_policy, security_requirements, vulnerability_management_procedure, change_management_plan, risk_register.
- Key Document Structures: polityka, SBOM, proces approvals, zobowiązania, ryzyka/remediacja, raporty.
- Document Dependencies: SCA/SBOM narzędzia, repo/CI, ticketing/GRC, Legal/Procurement.



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

- linkage_index.jsonl (compliance/license)
- open_source_policy, third_party_software_policy, security_requirements, vulnerability_management_procedure, change_management_plan, risk_register


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

1. Opisz politykę licencji i listę dozwolone/zakazane/warunkowe.  
2. Zdefiniuj proces skanów/approvals/SBOM i zobowiązania (NOTICE/src).  
3. Dodaj ryzyka/remediację i raporty; aktualizuj linkage_index/checklisty.


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

- [ ] Każda zależność ma licencję, decyzję i (jeśli potrzeba) zobowiązanie; waivery mają sunset.  
- [ ] SBOM aktualne; raporty i NOTICE zgodne; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- SBOM export, raport SCA, lista licencji policy, log approvals/waiverów, NOTICE/attribution, source-offer, raporty zgodności, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Legal/Compliance → Security/Privacy → Product/Engineering → Audit/Owner sign‑off.
## Metryki jakości

- % zależności z pełną metadany licencji, liczba waiverów i czas sunset, czas reakcji na zależność zakazaną, aktualność SBOM, liczba EOL zależności otwartych.

## Kryteria ukończenia

- [ ] Polityka/licencje/procesy opisane; SBOM/raporty/NOTICE aktualne; dokument w linkage_index; metadane aktualne.


## Struktura sekcji

1) Zakres i komponenty (OSS/proprietary, języki, platformy, źródła SBOM)  
2) Polityka licencji (dozwolone/zakazane/warunkowe, copyleft/dual licensing)  
3) Proces: skanowanie SBOM/SCA, approvals nowych zależności, wyjątki/waivery, aktualizacje/EOL  
4) Zobowiązania (NOTICE/ACK/source offer, attribution) i lokalizacja artefaktów  
5) Ryzyka i remediacja (konflikty licencyjne, podatności licenc. w SCA, wersje EOL)  
6) Raporty i audyt (SBOM repo, log decyzji, raporty zgodności, częstotliwość przeglądów)  
7) Załączniki (SBOM export, lista licencji, log wyjątków, szablon NOTICE)


## Wymagane rozwinięcia

- Lista licencji dozwolonych/zakazanych/warunkowych i kryteria decyzji.  
- Procedura approve/deny z rolami (Engineering, Legal, Security) i SLA.  
- Szablon NOTICE/attribution, source-offer dla copyleft; repo lokalizacji.  
- Plan przeglądu SBOM i aktualizacji zależności/EOL; waivery z sunset.


## Wymagane streszczenia

- Executive: status SBOM, zależności ryzykowne (copyleft/EOL), wyjątki/waivery, plan remediacji.


## Guidance (skrót)

- Generuj SBOM w CI; blokuj buildy z licencjami zakazanymi lub brakiem NOTICE.  
- Copyleft/dual licensing → konsultacja Legal; dokumentuj source-offer.  
- Waivery mają sunset i kompensacje; trackuj w GRC/ticketach.  
- Aktualizuj SBOM przy każdej zmianie zależności; raportuj cyklicznie.


## Checklisty Definition of Ready (DoR)

- [ ] Polityka licencji i lista licencji dostępne; narzędzia SBOM/SCA gotowe.  
- [ ] Role approvals (Eng/Legal/Sec) i repo SBOM wskazane; wstępne SLA uzgodnione.


## Checklisty Definition of Done (DoD)

- [ ] SBOM i raport zgodności wygenerowane; decyzje/wyjątki zapisane; NOTICE/attribution/source-offer gotowe.  
- [ ] Ryzyka/remediacja zaplanowane; dokument w linkage_index; wersja/data/właściciel aktualne.

