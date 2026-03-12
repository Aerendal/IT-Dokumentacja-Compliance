---
title: Emergency Response Testing
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Emergency Response Testing


## Metadane

- Właściciel: QA Lead
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Planować i wykonywać testy reakcji na sytuacje awaryjne (IT/OT/obiekty): scenariusze, cele/KPI, kryteria sukcesu, wykonanie, obserwacje, luki i doskonalenie.


## Zakres i granice

- Obejmuje: scenariusze (awaria DC, ransomware, pożar/ewakuacja, OT outage, łączność), cele (RTO/RPO, bezpieczeństwo ludzi, komunikacja), plan testu (zakres, role, harmonogram, dane/snapshoty, środowisko), wykonanie (timeline, decyzje), wyniki/luki/akcje naprawcze, raport i plan kolejnych ćwiczeń.
- Poza zakresem: pełny plan DR/BCP (osobne dokumenty) – tutaj testy/ćwiczenia.


## Użytkownicy i interesariusze
- **QA Lead / Test Manager** — planuje strategię testowania i zarządza procesem QA
- **QA Engineer** — projektuje i wykonuje przypadki testowe
- **Development Team** — naprawia defekty i dostarcza testowalny kod
- **Product Owner** — definiuje kryteria akceptacji i priorytetyzuje defekty

## Wejścia i wyjścia

- Wejścia: scenariusze z DR/BCP, RTO/RPO, inwentarz systemów/OT/obiektów, runbooki IR/BCP/DR, plany ewakuacji/safety, kontakt listy, dane do testu (kopie/anonimizacja), harmonogram.  
- Wyjścia: plan testu, protokół wykonania (timeline, decyzje), wyniki i luki, action items z owner/ETA, raport z rekomendacjami, plan kolejnych ćwiczeń.


## Założenia
- AIS/VHF/GMDSS działają.  
- Zasoby ratunkowe są utrzymywane i dostępne.  
- Zespoły przeszkolone i PPE dostępne.
## Otwarte pytania
- Jak integrować dane AIS/pogoda do wczesnego ostrzegania?  
- Jakie są lokalne wymagania raportowe (czasy, format)?  
- Jak często aktualizować scenariusze ćwiczeń?
## Powiązania (meta)

- Key Documents: disaster_recovery_plan, business_continuity_plan, incident_response_playbook, incident_notifications, backup_and_recovery_testing, emergency_response_plan, safety_guidelines, risk_register.
- Key Document Structures: scenariusze, cele/kryteria, plan testu, wykonanie, wyniki/luki, follow‑up.
- Document Dependencies: systemy IT/OT, safety procedures, komunikacja, backup/snapshots, SIEM/monitoring, ticketing.



## Zależności dokumentu
Wymaga: aktualnych kontaktów i list zasobów, map stref, procedur łączności, list pasażerów/crew i planów ładunków, polityk bezpieczeństwa, wymogów regulatorów. Braki = DoR otwarte.
## Fazy cyklu życia
- Przygotowanie (listy kontaktów, zasoby, training).  
- Reakcja (alarmowanie, łączność, akcja, raporty).  
- Po zdarzeniu (debrief, raporty, aktualizacje).  
- Ćwiczenia okresowe.
## Struktura sekcji (szkielet)
- Scenariusze i role.
- Kanały i eskalacje (progi, redundancja, kolejność).
- Integracje (HR/IDP/CMDB/location services).
- Szablony komunikatów i wielojęzyczność.
- Bezpieczeństwo/prywatność (PII, logging, retention).
- Dostępność/DR (redundancja, fallback, testy failover).
- Runbooki i testy/ćwiczenia.
- Monitoring SLA i raporty po incydencie.
- Ryzyka i mitigacje.
## Szybkie powiązania

- linkage_index.jsonl (dr/emergency_testing)
- disaster_recovery_plan, business_continuity_plan, incident_response_playbook, incident_notifications, backup_and_recovery_testing, emergency_response_plan, safety_guidelines, risk_register


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

1. Wybierz scenariusze, cele i kryteria; przygotuj plan i zasoby.  
2. Przeprowadź test, notuj timeline i decyzje; zbierz logi/dowody.  
3. Spisz wyniki i luki; przypisz action items; zaplanuj retest; zaktualizuj linkage_index/checklisty.


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
- SAR: Search and Rescue.  
- MRCC: Maritime Rescue Coordination Centre.  
- MRO: Mass Rescue Operations.
## Przykłady użycia
- Pożar na statku w porcie; koordynacja z strażą pożarną i holownikami.  
- Wyciek paliwa; deploy booms/sorbent, zawiadomienie regulatora.  
- Kolizja jednostek; SAR, medyczne, clearing toru wodnego.
## Ryzyka i ograniczenia
- Brak łączności lub przestarzałe kontakty → opóźnienia.  
- Zła pogoda ogranicza zasoby (helikoptery).  
- Brak ćwiczeń → chaos w realnym zdarzeniu.
## Decyzje i uzasadnienia
- Priorytety zasobów przy zdarzeniach równoległych.  
- Kanały alternatywne łączności.  
- Kiedy angażować regulator/wojsko/partnerów.
## Powiązania z innymi dokumentami
- safety_compliance — zgodność i bezpieczeństwo.  
- port_operations_plan — koordynacja operacji.  
- incident_response_runbook — procesy ogólne.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- SOLAS/GMDSS, lokalne przepisy SAR, przepisy środowiskowe (wycieki).  
- Wewnętrzne polityki bezpieczeństwa.
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

- [ ] Scenariusze pokrywają kluczowe ryzyka; kryteria sukcesu jasno opisane.  
- [ ] Action items mają owner/ETA; retesty zaplanowane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Checklisty scenariuszy, logi/test reports, komunikacja (status/alerty), backup/snapshot dowody, zdjęcia/raporty, action plan, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Osiągnięcie RTO/RPO, czas ewakuacji/reakcji, liczba luk i czas ich zamknięcia, liczba retestów, bezpieczeństwo podczas ćwiczeń (incydenty=0), terminowość raportu.

## Kryteria ukończenia

- [ ] Testy przeprowadzone, wyniki i luki opisane, plan retestów ustawiony; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Scenariusze testowe (DC outage, ransomware, pożar/ewakuacja, OT outage, łączność)  
2) Cele i kryteria sukcesu (RTO/RPO, komunikacja, bezpieczeństwo ludzi, SLA)  
3) Plan testu (zakres, role, harmonogram, dane/snapshoty, środowisko, pre-reqs)  
4) Wykonanie i obserwacje (timeline, decyzje, problemy)  
5) Wyniki, luki i akcje naprawcze (owner, ETA, priorytet)  
6) Raport i plan kolejnych ćwiczeń (cadence, doskonalenie, retest)  
7) Załączniki (checklisty, kontakt listy, runbooki, logi, zdjęcia/raporty)


## Wymagane rozwinięcia

- Matryca scenariusz→cel/KPI→kryteria sukcesu; dane/snapshoty do testu; plan komunikacji (kanały, szablony).  
- Tabela action items z owner/ETA; plan retestów; log decyzji.


## Wymagane streszczenia

- Executive: scenariusze przećwiczone, osiągnięcie RTO/RPO/bezpieczeństwa, główne luki i plan retestów.


## Guidance (skrót)

- Testuj jak najbliżej realiów: komunikacja, ewakuacja, backup/snapshots, ręczne procedury.  
- Dokumentuj timeline i decyzje; luki → action items z datą; retest po remediacji.  
- Zadbaj o bezpieczeństwo ludzi podczas ćwiczeń; zatwierdź z Safety/Facility.


## Checklisty Definition of Ready (DoR)

- [ ] Scenariusze/RTO/RPO i role ustalone; dane/snapshoty dostępne; zgody Safety.  
- [ ] Plan komunikacji i runbooki gotowe; środowisko testowe lub kontrolowany prod okno.


## Checklisty Definition of Done (DoD)

- [ ] Test wykonany; RTO/RPO i bezpieczeństwo ocenione; luki i action items zapisane.  
- [ ] Raport i plan retestów opublikowane; dokument w linkage_index; metadane aktualne.

