---
title: Design systemu bezpieczeństwa publicznego
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Design systemu bezpieczeństwa publicznego


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaprojektować system bezpieczeństwa publicznego (monitoring, alarmy, łączność): architektura, integracje, bezpieczeństwo/prywatność i ciągłość działania, zgodnie z prawem i wymaganiami operacyjnymi.


## Zakres i granice

- Obejmuje: monitoring wideo/audio/IoT, alarmy, łączność (radio/LTE/5G), centrum operacyjne/PSAP, integracje GIS/dispatch/sensory, analitykę wideo (VA), alerting publiczny, bezpieczeństwo/prywatność, obserwowalność, DR/BCP, retencję danych.
- Poza zakresem: szczegółowe procedury operacyjne służb (osobne SOP/runbooki).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania operacyjne i prawne (lokalne/regionalne), mapy GIS, inwentarz sensorów/urządzeń, polityki retencji/prywatności, wymagania łączności (coverage/SLA), budżet i ograniczenia.
- Wyjścia: architektura high-level (edge/cloud), projekt sieci/segmentacji/redundancji, plan integracji (GIS/dispatch/VA/sensory), bezpieczeństwo/prywatność (szyfrowanie, RBAC/ABAC, audyt, anonimizacja), observability i DR (failover/testy alarmów), plan retencji/dostępu do danych, lista ryzyk i plan mitigacji.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: security_requirements, data_retention_policy, access_control_policy, incident_response_runbook, disaster_recovery_plan, business_continuity_plan, privacy_impact_assessment, integration_architecture, network_architecture.
- Key Document Structures: architektura, integracje, bezpieczeństwo/prywatność, łączność, DR/BCP, retencja.
- Document Dependencies: GIS/dispatch system, sensor inventory, network/telecom providers, IAM/IdP, SIEM, storage/retention systems, legal/privacy counsel.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia

- Faza 1: Koncepcja i Wizja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 2: Analiza Wymagań: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 3: Projekt / Design: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 4: Planowanie: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 5: Implementacja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 6: Testowanie / QA: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 7: Bezpieczeństwo / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 8: Wdrożenie / Deployment: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 9: Operacje / Maintenance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)
1. Zakres: typy zadań/zasobów, ograniczenia (czas, zależności, okna).
2. Algorytmy/heurystyki (priority, fair share, cron, DAG, SLAs).
3. Model danych: job/task, queue, dependencies, retries.
4. Planowanie i ekzekucja: dispatcher, workers, preemption, autoscale.
5. Observability: kolejki, latencja, SLA hit/miss, backlog, alerty.
6. Bezpieczeństwo: authZ do kolejek, izolacja tenantów, rate limits.
7. Change/ops: config as code, release/rollback, maintenance windows.
## Szybkie powiązania

- linkage_index.jsonl (public_safety/design)
- security_requirements, data_retention_policy, access_control_policy, incident_response_runbook, disaster_recovery_plan, business_continuity_plan, privacy_impact_assessment, integration_architecture, network_architecture


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa

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

1. Zbierz wymagania prawne/operacyjne i inwentarz sensorów/systemów.  
2. Opracuj architekturę, integracje i łączność; dodaj bezpieczeństwo/prywatność i DR/BCP.  
3. Ustal testy alarmów/failover i retencję; zaktualizuj linkage_index/checklisty.


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

- [ ] Architektura spełnia coverage/SLA; segmentacja i redundancja opisane.  
- [ ] Bezpieczeństwo/prywatność i retencja zgodne z prawem; logi/audyt opisane.  
- [ ] Testy alarmów/failover zaplanowane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Diagramy architektury/sieci, inwentarz sensorów, matryca integracji, polityki retencji/prywatności, konfiguracje bezpieczeństwa, runbooki testów/DR, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Dostępność systemu (SLA), czas detekcji/reakcji na alarm, sukces testów alarmów/failover, zgodność retencji z prawem, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Projekt HLD gotowy, bezpieczeństwo/prywatność/retencja/DR uwzględnione; dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres i wymagania (operacyjne/prawne, coverage, SLA)  
2) Architektura (edge vs cloud, storage/retencja, segmentacja sieci, redundancja)  
3) Integracje (dispatch/PSAP, GIS, sensory: pożar/środowisko, VA/analytics, public alerting)  
4) Łączność i niezawodność (radio/LTE/5G, QoS, fallback, powielone ścieżki)  
5) Bezpieczeństwo i prywatność (szyfrowanie w tranzycie/spoczynku, RBAC/ABAC, audyt/logi, anonimizacja/masking, zgodność prawna)  
6) Observability i DR/BCP (monitoring, testy alarmów, failover, backup/retencja, RPO/RTO)  
7) Ryzyka i ograniczenia (techniczne/prawne/operacyjne) oraz plan mitigacji  
8) Załączniki (diagramy, inwentarz sensorów, polityki retencji, mapy GIS, runbooki testów)


## Wymagane rozwinięcia

- Diagramy architektury i segmentacji; profile redundancji i QoS.  
- Matryca integracji (system→interfejs→protokół→SLA).  
- Polityki retencji/prywatności i logowania; procedury anonimizacji.  
- Plan testów alarmów i failover (częstotliwość, kryteria sukcesu).


## Wymagane streszczenia

- Executive: zakres, architektura HLD, top ryzyka, plan DR/BCP, retencja/prywatność.


## Guidance (skrót)

- Priorytet: niezawodność/bezpieczeństwo/prywatność; projektuj „fail secure & fail operational”.  
- Stosuj segmentację i zero trust między domenami (OT/IT/VA).  
- Retencja danych zgodna z prawem; minimalizuj PII, stosuj anonimizację tam, gdzie można.  
- Testuj alarmy i failover cyklicznie; utrzymuj logi/audyt centralnie.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania prawne/operacyjne i inwentarz sensorów/systemów zebrane; coverage/SLA znane.  
- [ ] Polityki retencji/prywatności dostępne; ownerzy domen wskazani.


## Checklisty Definition of Done (DoD)

- [ ] Architektura/integracje/łączność opisane; bezpieczeństwo/prywatność i retencja uwzględnione; testy alarmów/DR zaplanowane.  
- [ ] Ryzyka/waivery z sunset opisane; dokument w linkage_index; metadane aktualne.

