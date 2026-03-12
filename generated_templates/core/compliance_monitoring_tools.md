---
title: Compliance Monitoring Tools
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Compliance Monitoring Tools


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać narzędzia i procesy monitorowania zgodności: jakie regulacje/standardy i systemy są objęte, jakie kontrole są automatyzowane, jakie dowody zbieramy, jak alertujemy, raportujemy i prowadzimy remediację.


## Zakres i granice

- Obejmuje: zakres regulacji/standardów (ISO/SOC/PCI/HIPAA/GDPR/NIS2/…), systemy w scope, narzędzia/źródła dowodów (SIEM/SOAR, CSPM/KSPM, skanery konfig/łatek, IaC drift, IAM recertyfikacje, DLP, GRC), mapę kontroli→narzędzie→alert/raport, progi i krytyczność, runbooki remediacji, raporty/dashboardy, integracje z audytem/recertyfikacjami.
- Poza zakresem: definicja wymagań/standardów (polityki), szczegółowe audyty manualne (osobne raporty).


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: katalog kontroli/SoA, wymagania audytowe, lista systemów w scope, właściciele kontroli, narzędzia i ich konfiguracje, SLA na alerty, harmonogram raportów.
- Wyjścia: mapa kontrola→narzędzie→alert/raport, konfiguracje alertów/progów, lista runbooków remediacji, harmonogram raportów/dashboardów, plan tuningu/false positives, log dowodów.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: compliance_monitoring_runbook, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference, data_privacy_compliance.
- Key Document Structures: kontrole, narzędzia/źródła, alerty/progi, raporty, remediacja, tuning.
- Document Dependencies: SIEM/logi, CSPM/KSPM, skanery konfig/łatek, IaC scans, DLP, IAM recerts, ticketing/GRC.


## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia

- Konfiguracja narzędzi i mapy kontrola→alert/raport.
- Operacje: monitoring, alerty, triage i remediacja.
- Raportowanie i dowody audytowe.
- Tuning (false positives) i przeglądy okresowe.



## Struktura sekcji (szkielet)
- Kontekst i scope
- Metryki/status kontrolek
- Dowody i źródła
- Alerty i dashboardy
- Przeglądy/raporty
- Ryzyka
## Szybkie powiązania

- linkage_index.jsonl (compliance/monitoring_tools)
- compliance_monitoring_runbook, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference, data_privacy_compliance


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
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

1. Zdefiniuj scope, narzędzia i mapę kontroli; wypełnij tabelę z progami/SLA/runbookami.  
2. Skonfiguruj alerty/raporty; ustaw repo dowodów; dodaj tuning/FP procedurę.  
3. Utrzymuj dokument i linkage_index; aktualizuj po audytach lub zmianach narzędzi.


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

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ relacji: rozszerza/streszcza/wymaga/wyklucza]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji

- [Wejście] -> [Sekcja źródłowa] -> [Sekcja rozwinięcia] -> [Wyjście]
- [Wejście] -> [Sekcja źródłowa] -> [Sekcja streszczenia] -> [Wyjście]

## Weryfikacja spójności

- [ ] Kontrole mają narzędzie, próg, SLA, ownera i runbook; dowody podlinkowane.  
- [ ] Alerty krytyczne działają; tuning/FP proces aktywny; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Lista narzędzi, mapa kontroli, konfiguracje alertów, runbooki remediacji, repo dowodów, raporty/dashboardy, tuning log, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Pokrycie kontroli w narzędziach, % alertów z runbookiem i SLA, liczba false positives i czas tuningu, terminowość raportów, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Monitoring narzędziowy spójny z katalogiem kontroli, alerty i raporty działają; metadane aktualne.


## Powiązania sekcja↔sekcja

- Zakres/standardy → Kontrole/narzędzia → Alerty/progi → Runbooki → Raporty → Tuning.


## Struktura sekcji

1) Zakres regulacji/standardów i systemów w scope  
2) Narzędzia i źródła dowodów (SIEM/SOAR, CSPM/KSPM, IaC drift, skanery, IAM recerts, DLP, GRC)  
3) Mapowanie kontroli (kontrola → narzędzie/źródło → typ dowodu/alertu → próg/SLA → właściciel)  
4) Alerty i runbooki (progi, krytyczność, kanały, eskalacje, CAPA)  
5) Raporty i dashboardy (częstotliwość, odbiorcy, repo dowodów)  
6) Integracje z audytem/recertyfikacjami (SoA, access recerts, wyniki skanów)  
7) Tuning i przeglądy (false positives, zmiany progów, testy kontrolne)  
8) Załączniki (lista narzędzi, konfiguracje, mapa kontroli, szablony raportów)


## Wymagane rozwinięcia

- Tabela kontroli z narzędziami, progami, SLA, właścicielem, dowodem i runbookiem.  
- Kryteria krytyczności/priorytetów alertów i SLA reakcji.  
- Lokalizacja repo dowodów i ścieżka audytu; harmonogram raportów.  
- Proces tuningu i testów kontrolnych; plan przeglądów okresowych.


## Wymagane streszczenia

- Executive: scope, krytyczne alerty/SLA, top odchylenia, plan tuningu/remediacji.


## Guidance (skrót)

- Jedna mapa: wymaganie/standard → kontrola → narzędzie/źródło → alert/raport → runbook.  
- SLA i priorytety muszą być uzgodnione z właścicielami kontroli.  
- Ogranicz false positives tuningu progów i jakości danych; loguj zmiany.  
- Repo dowodów i raporty muszą być łatwo dostępne dla audytu.


## Checklisty Definition of Ready (DoR)

- [ ] Zakres regulacji/standardów i systemów znany; katalog kontroli/SoA dostępny.  
- [ ] Narzędzia/źródła i ownerzy kontroli zidentyfikowani; wstępne SLA/pr progi uzgodnione.


## Checklisty Definition of Done (DoD)

- [ ] Mapa kontrola→narzędzie→alert/raport kompletna; alerty/runbooki działają.  
- [ ] Repo dowodów i harmonogram raportów działa; tuning/FP proces opisany.  
- [ ] Dokument w linkage_index; wersja/data/właściciel aktualne.

