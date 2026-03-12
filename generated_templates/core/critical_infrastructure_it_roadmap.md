---
title: Critical Infrastructure IT Roadmap
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Critical Infrastructure IT Roadmap


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan rozwoju IT dla infrastruktury krytycznej (energy/water/transport/health): bezpieczeństwo, niezawodność, modernizacja i zgodność. Ma zapewnić ciągłość działania, odporność i zgodność regulacyjną.


## Zakres i granice

- Obejmuje: stan obecny, ryzyka i luki, priorytety modernizacji (OT/IT/SCADA/ICS), segmentację sieci, zero trust, monitoring/OT SOC, patch/asset mgmt, backup/DR, zgodność (NIS2/ISA/IEC 62443/ISO 27001), projekty modernizacji (edge/cloud), harmonogram i CAPEX/OPEX, personel i szkolenia, ćwiczenia cyber/DR.  
- Poza zakresem: szczegółowe projekty systemów pojedynczych (oddzielne).


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: ocena ryzyka i audyty, mapy systemów OT/IT, inwentarz assetów i krytyczności, wymagania regulatorów, budżet, SLO/RTO/RPO, incydenty historyczne, plany biznesowe.  
- Wyjścia: roadmapa (kwartały/lata), pakiety projektów i priorytety, zależności, CAPEX/OPEX, KPI (incydenty, compliance score, MTTR), decyzje architektoniczne, plan szkoleń i ćwiczeń.


## Założenia

- Wsparcie zarządu i finansowania.  
- Dostępność zespołów OT/IT/security.  
- Aktualne dane o infrastrukturze.


## Otwarte pytania

- Jak włączyć dostawców/partnerów w model access?  
- Jakie SLA/KPI wymagają regulatorzy?  
- Jak mierzyć poprawę bezpieczeństwa w czasie?


## Powiązania (meta)

- Key Documents: risk_register, security_requirements, dr_plan, business_continuity_plan, network_segmentation_design, identity_and_access_strategy, training_plan_security.  
- Key Document Structures: stan obecny, ryzyka, projekty, bezpieczeństwo, DR/BCP, harmonogram, KPI.  
- Document Dependencies: CMDB/asset inventory, OT/IT network diagrams, SOC/SIEM, backup/DR, IAM, vendor contracts.


## Zależności dokumentu

Wymaga: aktualnej oceny ryzyka, inwentarza assetów, wymagań regulacyjnych, danych budżetowych, map sieci OT/IT, planów DR/BCP. Braki = DoR otwarte.


## Fazy cyklu życia

- Ocena i priorytetyzacja.  
- Planowanie i zabezpieczenie finansowania.  
- Wykonanie projektów i ćwiczenia.  
- Przeglądy roczne, audyty i aktualizacje.



## Struktura sekcji (szkielet)
- Cel i definicja sukcesu (KPI)
- Zakres, założenia i ograniczenia
- Interesariusze i role/RACI
- Kamienie milowe i daty
- Plan fal/sprintów z deliverables
- Zależności i ryzyka oraz plan mitigacji
- Budżet/zasoby i obłożenie
- Plan komunikacji i raportowania
- Kryteria akceptacji/go-live i plan rewizji
## Szybkie powiązania

- linkage_index.jsonl (critical/infrastructure/it/roadmap)  
- network_segmentation_design, dr_plan, security_requirements, business_continuity_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **SCRUM Guide** — Przewodnik Scrum

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

1. Zbierz ryzyka i assety; zdefiniuj cele/KPI.  
2. Ułóż projekty i harmonogram; zabezpiecz budżet.  
3. Realizuj, monitoruj KPI i zgodność; aktualizuj DoR/DoD i linkage_index.


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

- NIS2: dyrektywa UE dot. bezpieczeństwa podmiotów kluczowych.  
- IEC 62443: standard bezpieczeństwa systemów przemysłowych.  
- DMZ: strefa izolacji między OT a IT.


## Przykłady użycia

- Roadmapa modernizacji SCADA/OT z segmentacją.  
- Przygotowanie do audytu NIS2/IEC 62443.  
- Plan zwiększenia odporności energetyki/transportu.


## Ryzyka i ograniczenia

- Opóźnione projekty → ryzyko regulatora/bezpieczeństwa.  
- Brak asset inventory → fałszywe priorytety.  
- Niedoszacowany OPEX SOC/monitoring.


## Decyzje i uzasadnienia

- Kolejność projektów (risk vs koszt).  
- Modele operacyjne SOC/monitoring (in‑house vs MSSP).  
- Zakres segmentacji/zero trust vs budżet.


## Powiązania z innymi dokumentami

- business_continuity_plan — BCP.  
- dr_plan — DR.  
- network_segmentation_design — segmentacja.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- NIS2, IEC 62443, ISO 27001, lokalne przepisy sektorowe.  
- Wewnętrzne polityki bezpieczeństwa/DR.

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

- [Artefakt 1, np. diagram architektury] — [opis i relacja do tego dokumentu]
- [Artefakt 2, np. schemat bazy danych] — [opis i relacja do tego dokumentu]

## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

- Ryzyka → Projekty → Harmonogram → KPI.  
- Segmentacja/zero trust → Monitoring/SOC → Incydenty/MTTR.  
- DR/BCP → RTO/RPO → Projekty backup/replication.


## Struktura sekcji

1) Kontekst i cele (regulacje, krytyczność)  
2) Stan obecny i ryzyka (asset criticality, luki)  
3) Projekty i inicjatywy (modernizacja, security, reliability)  
4) Sieć/segmentacja i zero trust (OT/IT/DMZ)  
5) Monitoring/SOC i incident response (OT + IT)  
6) Backup/DR/BCP (RTO/RPO, testy)  
7) Zgodność i audyty (NIS2/IEC 62443/ISO 27001, lokalne)  
8) Harmonogram i budżet (CAPEX/OPEX)  
9) KPI/metryki sukcesu (incydenty, compliance score, MTTR, uptime)  
10) Szkolenia i ćwiczenia (cyber/DR)  
11) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Macierz ryzyk i projektów z priorytetami.  
- Harmonogram (roadmapa) i budżet.  
- Plan segmentacji i zero trust OT/IT.  
- Plan ćwiczeń cyber/DR i audytów.


## Wymagane streszczenia

- Executive snapshot: top ryzyka, projekty w toku, budżet, KPI.  
- Karta zgodności (status NIS2/IEC 62443/ISO 27001).


## Guidance (skrót)

- Najpierw asset inventory i risk assessment; potem projekty.  
- Segmentacja OT/IT + zero trust to fundament.  
- Regularne ćwiczenia cyber/DR i testy backupu.  
- Plan finansowy musi obejmować OPEX (SOC/monitoring).  
- Uzgodnij KPI z regulatorami/zarządem.


## Checklisty Definition of Ready (DoR)

- [ ] Ocena ryzyka i inwentarz assetów dostępne.  
- [ ] Wymagania regulacyjne i RTO/RPO znane.  
- [ ] Dane budżetowe i priorytety biznesowe zebrane.  
- [ ] Mapy sieci OT/IT i zależności gotowe.  
- [ ] Plan DR/BCP dostępny.


## Checklisty Definition of Done (DoD)

- [ ] Roadmapa i projekty opisane; status/wersja/data uzupełnione.  
- [ ] Budżet i KPI ustalone; raport dla zarządu/regulatora przygotowany.  
- [ ] Segmentacja/zero trust/monitoring/DR projekty zaplanowane/uruchomione.  
- [ ] Linkage_index zaktualizowany; ryzyka i decyzje udokumentowane.  
- [ ] Plan przeglądów rocznych/audytów zapisany.

