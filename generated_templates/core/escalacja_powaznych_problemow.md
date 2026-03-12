---
title: Eskalacja poważnych problemów
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Eskalacja poważnych problemów


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać procedurę eskalacji krytycznych incydentów: kryteria/severity, ścieżki i kontakty, SLA reakcji/rezolucji, komunikacja, dokumentacja i post-incident RCA/action items.


## Zakres i granice

- Obejmuje: definicje severity/priorytetów i kryteria eskalacji, ścieżki on-call (L1/L2/L3/leadership/security/PR), SLA reakcji/rezolucji, komunikację (kanały, częstotliwość, status page/klienci), dokumentację incydentu (timeline, decyzje), RCA/post-incident i action items, przegląd procesu.  
- Poza zakresem: szczegółowe runbooki techniczne (linkowane), pełny IR playbook (osobny dokument).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: policy sev/priority, contact lists, on-call schedule, IR/BCP/DR plans, status page/playbooks, risk register.  
- Wyjścia: procedura eskalacji, matryca sev→ścieżka/SLA, szablony komunikacji, log incydentu (timeline/decyzje), action items i RCA, plan przeglądu procesu.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: incident_response_playbook, incident_notifications, postmortem_analysis, communication_plan, risk_register, change_management_plan, disaster_recovery_plan, business_continuity_plan.
- Key Document Structures: severity/criteria, ścieżki i kontakty, SLA/reakcja, komunikacja, dokumentacja, RCA/action items.
- Document Dependencies: on-call schedule, contact DB, ticketing/IM tool, status page, IR/BCP/DR, PR/Legal.



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
1. Kategorie: dostęp/SSO, wydajność, dane, UX, bezpieczeństwo, operacje.
2. Format wpisu: symptom, wpływ, przyczyna, link do runbook/rozwiązania, priorytet.
3. Tagowanie: systemy, domeny, zespoły, krytyczność.
4. Szybkie filtry: „najczęstsze”, „wysoki wpływ”, „regresje”.
5. Wersjonowanie i review: kto dodaje/aktualizuje, przeglądy okresowe.
6. Integracja: linki do ticketów, KB, runbooków, katalogów problemów szczegółowych.
## Szybkie powiązania

- linkage_index.jsonl (incident/escalation)
- incident_response_playbook, incident_notifications, postmortem_analysis, communication_plan, risk_register, change_management_plan, disaster_recovery_plan, business_continuity_plan


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Zdefiniuj sev/kryteria i matrycę eskalacji; uzupełnij contact list i SLA.  
2. Ustaw szablony komunikacji i kanały; przygotuj log incydentu.  
3. Po incydencie wypełnij log/RCA/action items; zaktualizuj linkage_index/checklisty.


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

- [ ] Sev/kryteria i ścieżki spójne; SLA zgodne z IR/BCP/DR; komunikacja gotowa.  
- [ ] Log/RCA/action items prowadzone; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Matryca sev→SLA, contact list, szablony komunikacji, log incydentu, RCA, action plan, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- MTTA/MTTR vs SLA dla P0/P1, liczba opóźnionych eskalacji, liczba action items otwartych/zamkniętych, terminowość komunikacji, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Procedura eskalacji gotowa, komunikacja i kontakty aktualne; wersja/data/właściciel aktualne; dokument w linkage_index.


## Struktura sekcji

1) Definicje severity/priorytetów i kryteria eskalacji  
2) Ścieżki i kontakty (on-call L1/L2/L3, Security, PR/Legal, Leadership)  
3) SLA reakcji/rezolucji i czasy eskalacji (matryca sev→SLA)  
4) Komunikacja (kanały, częstotliwość update, status page, klienci, szablony)  
5) Dokumentacja incydentu (timeline, decyzje, właściciele, log)  
6) Post-incident: RCA, action items, follow-up, przegląd procesu  
7) Załączniki (contact list, szablony komunikatów, log incydentu, matryca sev→SLA)


## Wymagane rozwinięcia

- Matryca sev→kryteria→SLA reakcji/rezolucji; ścieżki eskalacji i kanały.  
- Szablony komunikacji (wew/klienci/status page), contact list i rotacje on-call.  
- Wymogi dokumentacji (timeline, decyzje) i RCA/action items z właścicielami/ETA.


## Wymagane streszczenia

- Executive: ostatnie P0/P1, czas reakcji/rezolucji vs SLA, otwarte action items/ETA.


## Guidance (skrót)

- Eskaluj wg kryteriów, nie uznaniowo; loguj każdą decyzję i czas.  
- Komunikacja regularna, single source (status page/ticket/IM); szablony gotowe.  
- RCA i action items obowiązkowe; zamykaj z retestem, włącz w postmortem.


## Checklisty Definition of Ready (DoR)

- [ ] Sev/kryteria i contact list gotowe; on-call schedule aktualny; kanały komunikacji ustalone.  
- [ ] Matryca sev→SLA wstępnie uzgodniona; szablony komunikatów przygotowane.


## Checklisty Definition of Done (DoD)

- [ ] Matryca eskalacji i komunikacja opisane; log/RCA/action items z owner/ETA; dokument w linkage_index; metadane aktualne.

