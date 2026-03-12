---
title: Incident Response Playbook
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Incident Response Playbook


## Metadane

- Właściciel: Security Officer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Praktyczny playbook reagowania na incydenty (security/availability), skracający MTTR i ograniczający wpływ biznesowy.


## Zakres i granice

- Obejmuje: klasyfikację incydentów (SEV1/2/3; security vs availability), ogólny runbook (detekcja → triage → containment → eradication → recovery → postmortem), scenariusze wysokiego ryzyka (ransomware, DDoS, data leak, credential theft, major outage), komunikację wewn./zewn., artefakty i narzędzia, after-action/CAPA.  
- Poza zakresem: szczegółowe runbooki systemowe (per usługa) – linkowane oddzielnie; DR testy pełne (osobny dokument).


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia

- Wejścia: polityka bezpieczeństwa, SLO/SLA, architektura usług, lista kontaktów i ról, kanały komunikacji, narzędzia IR/forensics, wymagania regulatorów.  
- Wyjścia: procedury per SEV, scenariusze wysokiego ryzyka, szablony komunikatów, checklisty triage/forensics, plan postmortem/CAPA, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: incident_response_plan, crisis_communication, audit_logging, logging_strategy, obsluga_incydentow_rate_limit, postmortem_incydentow_produkcyjnych.  
- Key Document Structures: klasyfikacja, runbook ogólny, scenariusze, komunikacja, artefakty/narzędzia, after-action.  
- Document Dependencies: SIEM/APM, paging/alerting, ticketing, status page, legal/PR contacts, DR/backup.



## Zależności dokumentu
- Konsumuje: Incident classification/severity matrix, On-call rota, Runbooki techniczne, BCP/DR, Comms plan.
- Dostarcza do: Post-Incident Review, Lessons Learned, aktualizacji Runbooków/monitoringu, Change/Release (jeśli wymagane poprawki).
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
- Faza 10: Incident Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 11: Monitoring / Observability: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 12: Dokumentacja referencyjna: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 13: Szkolenie / Onboarding: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 14: Komunikacja stakeholders: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 15: Knowledge Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 16: Postmortem / Retrospektywa: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 17: Budżetowanie / Cost Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 18: Vendor Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 19: Governance / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 20: Decommission / Sunset: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 21: DR / BCP: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 22: Change Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 23: Capacity Planning: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)
- Cel i zakres stosowania planu
- Klasyfikacja i priorytety (severity, wpływ, SLA reakcji)
- Role i RACI w czasie incydentu
- Przebieg procesu: wykrycie → triage → containment → eradication → recovery → closure
- Komunikacja: wewnętrzna/zewnętrzna, szablony komunikatów, częstotliwość
- Narzędzia i artefakty: tabele kontaktów, kanały, system ticketów, log template
- Kryteria zamknięcia i przekazania do PIR/postmortem
## Szybkie powiązania

- linkage_index.jsonl (security/incident_response_playbook)  
- crisis_communication, audit_logging, logging_strategy, postmortem_incydentow_produkcyjnych


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

1. Określ SEV i uruchom odpowiedni tor eskalacji.  
2. Postępuj wg runbooka ogólnego i scenariusza; prowadź log działań.  
3. Komunikuj, zamknij incydent, wykonaj postmortem/CAPA; zaktualizuj linkage_index i checklists.


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

- [ ] SEV i eskalacja działają; runbook ma pełny ciąg detekcja→postmortem.  
- [ ] Scenariusze wysokiego ryzyka mają pre-approved kroki i komunikację.  
- [ ] Linkage_index uzupełniony; CAPA/lessons learned proces opisany.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Tabela SEV, ścieżka eskalacji, szablony komunikatów, checklisty triage/containment, log działań, raport postmortem, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- MTTR/MTTA per SEV, liczba incydentów z kompletnym postmortem, czas publikacji initial/closure comms, liczba powtórek z tej samej przyczyny, realizacja CAPA (% on-time).

## Kryteria ukończenia

- [ ] Playbook gotowy do użycia (klasyfikacja, runbook, scenariusze, komunikacja, artefakty) i osadzony w linkage_index.


## Struktura sekcji

1) Klasyfikacja incydentów i eskalacja (SEV, kryteria, on-call, SLA reakcji)  
2) Runbook ogólny (detekcja, triage, containment, eradication, recovery, handoff do postmortem)  
3) Scenariusze wysokiego ryzyka (ransomware, DDoS, data leak/PII, credential theft, major outage) – kroki i decyzje pre-approved  
4) Komunikacja (kanały, szablony: initial/update/closure, odbiorcy, PR/legal/regulator)  
5) Artefakty i narzędzia (checklisty, formularze, forensics, logi/trace, ścieżka eskalacji)  
6) After-action (postmortem, CAPA, aktualizacja runbooków/monitoringu/szkoleń, tabletop/chaos)  
7) Załączniki (szablony komunikatów, checklisty, ADR/waiver log)


## Wymagane rozwinięcia

- Tabela SEV z kryteriami, SLA reakcji i ownerami; ścieżka eskalacji.  
- Checklisty triage/containment per scenariusz; pre-approved bloki (np. blokada kont, cutover).  
- Szablony komunikacji (wewn., klient, regulator) i zasady aprobat (PR/legal).  
- Lista narzędzi forensics i lokalizacji logów/artefaktów; procedura dowodowa.  
- Plan postmortem/CAPA z terminami i ownerami; harmonogram ćwiczeń tabletop.


## Wymagane streszczenia

- Executive: ostatnie SEV1/2, czas reakcji/MTTR, status CAPA, główne ryzyka i luki.


## Guidance (skrót)

- „Contain first”: ogranicz wpływ zanim szukasz pełnej przyczyny; zabezpieczaj dowody.  
- Eskaluj wg SEV i timebox triage; dokumentuj decyzje/akcje.  
- Komunikuj często i jasno; używaj status page dla wpływu na klientów.  
- Każdy incydent kończy się postmortem z CAPA i aktualizacją monitoringu/runbooków.  
- Aktualizuj linkage_index i checklisty po zmianach.


## Checklisty Definition of Ready (DoR)

- [ ] Tabela SEV/eskalacji i kontakty on-call dostępne; kanały komunikacji działają.  
- [ ] Narzędzia SIEM/APM/forensics dostępne; szablony komunikatów przygotowane.


## Checklisty Definition of Done (DoD)

- [ ] Scenariusze i runbook ogólny opisane; SEV/eskalacja jasna; linkage_index zaktualizowany.  
- [ ] Postmortem/CAPA proces opisany; status/metadane aktualne; checklisty DoR/DoD odhaczone.  
- [ ] Szablony komunikacji i artefakty dołączone.

