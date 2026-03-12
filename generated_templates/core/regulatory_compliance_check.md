---
title: Regulatory Compliance Check
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Regulatory Compliance Check


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Checklista weryfikacji zgodności regulacyjnej: zakres regulacji/produktów, wymagania i dowody, luki i plan działań, akceptacje i cykliczne przeglądy.


## Zakres i granice

- Obejmuje: regulacje/standardy w scope, wymagania obligatoryjne/opcjonalne, dowody (dokumenty/testy/certyfikaty), status (pass/partial/fail/RAG), luki i plan działań, akceptacje właścicieli, harmonogram przeglądów.  
- Poza zakresem: projektowanie nowych kontrolek (w politykach), pełne audyty (oddzielne raporty).


## Użytkownicy i interesariusze
- Legal/Compliance, Security/Privacy, Product/Engineering, Audit, TPRM/Vendor Mgmt.
## Wejścia i wyjścia

- Wejścia: katalog wymagań/SoA, polityki/standardy, raporty testów/skanów, certyfikaty, repo dowodów, właściciele kontroli.  
- Wyjścia: wypełniona checklista, status RAG, lista luk i plan remediacji (owner/ETA), akceptacje, harmonogram przeglądów, wpisy do risk register.


## Założenia
- Legal/Compliance zapewnia interpretację; dane/flow są aktualne; istnieją polityki security/privacy.
## Otwarte pytania
- Jakie raporty regulacyjne (format/SLA/kanał) są wymagane? 
- Czy istnieją dodatkowe wymogi sektorowe (fin/health/public/ot)?
## Powiązania (meta)

- Key Documents: compliance_verification, compliance_with_regulations, compliance_monitoring_runbook/tools, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference.
- Key Document Structures: wymagania, dowody, status, luki/remediacja, akceptacja, przeglądy.
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
- Cel i zakres polityki
- Zakres obowiązywania i wyjątki
- Role i odpowiedzialności
- Wymagania/kontrole (techniczne/procesowe)
- Proces zarządzania zmianą i wyjątkami
- Dowody/audyt, metryki zgodności
- Komunikacja/szkolenia i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (compliance/regulatory_check)
- compliance_verification, compliance_with_regulations, compliance_monitoring_runbook/tools, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference


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

1. Wpisz regulacje w scope, wymagania i dowody; nadaj status RAG.  
2. Zidentyfikuj luki/waivery i plan działań; dodaj akceptacje.  
3. Zaplanuj przeglądy; aktualizuj linkage_index/checklisty.


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

- [ ] Każde wymaganie ma dowód, status i ownera; waivery mają sunset.  
- [ ] Luki mają plan i ETA; przeglądy zaplanowane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Checklista/CSV, repo dowodów, raporty testów/certyfikaty, waiver log, risk register wpisy, harmonogram przeglądów.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Legal/Compliance → Security/Privacy → Product/Engineering → Audit/Owner sign‑off.
## Metryki jakości

- % wymagań z dowodem, liczba luk i czas ich zamknięcia, liczba waiverów i czas sunset, terminowość przeglądów.

## Kryteria ukończenia

- [ ] Status i plan działań opublikowane; akceptacje zapisane; dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres regulacji/produktów (lista, wersje, systemy/dane w scope)  
2) Wymagania i status (obligatoryjne/opcjonalne, dowody, RAG)  
3) Luki i plan działań (owner, ETA, koszt/ryzyko, waivery z sunset)  
4) Akceptacja (właściciel, data, wersja, komentarze)  
5) Harmonogram przeglądów i monitorowanie zmian regulacji  
6) Załączniki (checklista/CSV, raporty testów/certyfikaty, repo dowodów, waiver log)


## Wymagane rozwinięcia

- Tabela wymagań z dowodami, statusem i ownerem; kryteria RAG.  
- Plan remediacji/waivery; harmonogram przeglądów (np. kwartalnie/po zmianach).  
- Ścieżka akceptacji (kto podpisuje, gdzie zapis).


## Wymagane streszczenia

- Executive: status RAG, top luki/waivery, plan działań i ETA, najbliższy przegląd.


## Guidance (skrót)

- Brak dowodu = luka; status musi opierać się na dowodach z datą.  
- Waivery z sunset/kompensacją; aktualizuj risk register.  
- Przeglądaj checklistę po audytach/zmianach regulacji/systemu.


## Checklisty Definition of Ready (DoR)

- [ ] Regulacje/standardy i katalog wymagań dostępne; repo dowodów wskazane.  
- [ ] Właściciele kontroli zidentyfikowani; kryteria RAG wstępnie ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Checklista wypełniona; dowody podlinkowane; status RAG zapisany.  
- [ ] Luki/waivery z planem działań; akceptacje podpisane; harmonogram przeglądów ustawiony; dokument w linkage_index; metadane aktualne.

