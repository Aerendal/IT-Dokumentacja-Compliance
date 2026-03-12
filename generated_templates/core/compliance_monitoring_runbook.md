---
title: Compliance Monitoring Runbook
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Compliance Monitoring Runbook


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnić operacyjne monitorowanie kontroli compliance (np. GDPR, SOC2, ISO, PCI, HIPAA), wykrywać odchylenia, prowadzić triage/escalation i dostarczać dowody dla audytów.


## Zakres i granice

- Obejmuje: źródła danych/kontrole, dashboardy/alerty i progi, triage/escalacje, działania korygujące, logi przeglądów i raporty audytowe, utrzymanie i tuning kontroli/alertów.
- Poza zakresem: projekt samych kontroli/polityk (opisane w politykach/standardach).


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: katalog kontroli, wymagania audytowe, SLO compliance, źródła danych (SIEM/IAM/CMDB/CI-CD/IaC scans/DLP), harmonogram przeglądów, lista właścicieli kontroli.
- Wyjścia: alerty i tickety compliance, log przeglądów, raporty audytowe, plan działań korygujących z owner/ETA, status RAG.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: compliance_monitoring_tools, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference, data_privacy_compliance.
- Key Document Structures: kontrole/metryki, alerty/progi, triage/escalacja, raporty/dowody, działania korygujące.
- Document Dependencies: SIEM/logi, CMDB/IAM, IaC/policy scans, DLP, ticketing, katalog kontroli.


## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia

- Konfiguracja źródeł/alertów i progów.
- Operacje: monitoring, triage, eskalacje, tickety.
- Raportowanie i audyt; działania korygujące.
- Przeglądy okresowe i tuning.



## Struktura sekcji (szkielet)
- Kontekst i scope
- Metryki/status kontrolek
- Dowody i źródła
- Alerty i dashboardy
- Przeglądy/raporty
- Ryzyka
## Szybkie powiązania

- linkage_index.jsonl (compliance/monitoring_runbook)
- compliance_monitoring_tools, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference, data_privacy_compliance


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

1. Uzupełnij mapę kontroli→metryki→progi→właścicieli.  
2. Skonfiguruj dashboardy/alerty, triage/escalacje i ticketing.  
3. Raportuj, gromadź dowody, prowadź tuning i aktualizuj linkage_index/checklisty.


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

- [ ] Kontrole mają metryki/progi/ownerów; alerty i SLA działają.  
- [ ] Działania korygujące powiązane z odchyleniami; dowody w repo.  
- [ ] Tuning/false positives odnotowane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Mapa kontroli→metryk/progów, dashboardy, konfiguracje alertów, log triage, tickety, raporty audytowe, tuning log, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Czas reakcji/rozwiązania odchylenia, liczba false positives, pokrycie kontroli w monitoringu, terminowość raportów audytowych, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Monitoring i triage działają, raporty i dowody gotowe; action items zamknięte lub w toku z planem; dokument w linkage_index; metadane aktualne.


## Powiązania sekcja↔sekcja

- Źródła/metryki → Alerty/progi → Triage/escalacja → Działania korygujące → Raporty/audyt → Tuning.


## Struktura sekcji

1) Zakres i kontrolki w monitoringu (framework, lista kontroli, właściciele)  
2) Źródła danych i metryki (SIEM/IAM/CMDB/IaC/DLP, definicje KPI/KRI)  
3) Dashboardy i alerty (progi, RAG, kanały, odpowiedzialni)  
4) Triage i eskalacja (kryteria, SLA reakcji, ścieżki)  
5) Działania korygujące i follow‑up (owner, ETA, dowody)  
6) Raportowanie i dowody dla audytów (cadence, format, repo)  
7) Utrzymanie i tuning (przeglądy progów, false positives, testy kontroli)  
8) Załączniki (mapa kontroli→metryk, szablony raportów, linki do dashboardów/ticketów)


## Wymagane rozwinięcia

- Mapowanie kontroli na metryki/źródła i progi; kanały alertów.  
- Kryteria triage (severity/RAG), SLA reakcji i eskalacje; runbook decyzji.  
- Szablon raportu audytowego i lokalizacja dowodów; częstotliwość przeglądów.  
- Proces tuning (false positives, testy kontroli, zmiany progów).


## Wymagane streszczenia

- Executive: status RAG, top 5 odchyleń, plan działań i ETA, zmiany progów.


## Guidance (skrót)

- Trzymaj jedną mapę: kontrola → metryka → próg → właściciel.  
- Definiuj SLA na triage i zamknięcie ticketów; loguj decyzje.  
- Minimalizuj false positives tuningiem progów i poprawą jakości danych.  
- Utrzymuj repo dowodów audytowych; raportuj cyklicznie KPI/KRI.


## Checklisty Definition of Ready (DoR)

- [ ] Katalog kontroli i wymagania audytu dostępne; źródła danych zidentyfikowane.  
- [ ] Ownerzy kontroli, kanały alertów i SLA reakcji wstępnie ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Mapy kontroli/metryk/progów wypełnione; alerty działają; triage/escalacje opisane.  
- [ ] Raportowanie i repo dowodów działają; działania korygujące z owner/ETA; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.

