---
title: Network Operations Training
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Network Operations Training


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przygotować zespół NOC/NetOps do skutecznej obsługi i utrzymania sieci: monitorowanie, incident response, change/maintenance, bezpieczeństwo, narzędzia i procedury, aby skrócić MTTR i utrzymać SLA.


## Zakres i granice

- Obejmuje: monitoring i alertowanie (NMS, telemetry), procedury incydentowe, triage i eskalacje, podstawy routingu/switchingu, change management, maintenance windows, bezpieczeństwo (ACL, DDoS, access), dokumentację i runbooki, raportowanie KPI NOC.  
- Poza zakresem: zaawansowana architektura sieci (oddzielne szkolenia), SOC/IR szczegółowy (oddzielny playbook).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: architektura sieci, narzędzia NMS/telemetry, runbooki incydentów, polityki change, listy ról i kontaktów, SLA/OLA, historia incydentów, polityki bezpieczeństwa.  
- Wyjścia: program szkolenia (moduły), materiały (prezentacje, laby), checklisty DoR/DoD, wyniki egzaminu/weryfikacji, zaktualizowane runbooki, plan on-call/roty.


## Założenia

- Dostęp do środowisk testowych i narzędzi.  
- Zespół ma podstawy sieci.  
- Czas na ćwiczenia jest zabezpieczony.


## Otwarte pytania

- Jak mierzyć długofalowy efekt szkolenia na MTTR/change rate?  
- Jak często aktualizować progi alertów?  
- Czy potrzebne są ścieżki specjalistyczne (wireless, DC, cloud)?

## Powiązania (meta)

- Key Documents: network_outage_response, maintenance_windows_schedule, change_management, ddos_protection_plan, logging_and_audit_trail, access_control_policy.  
- Key Document Structures: monitoring, incident response, change, bezpieczeństwo, dokumentacja/runbooki, KPI.  
- Document Dependencies: NMS/telemetry, ticketing, CMDB, access management, comms tools, lab/test env.


## Zależności dokumentu

Wymaga: aktualnych runbooków i architektury, dostępu do NMS/telemetry i labu, listy kontaktów/escalation, polityk change/security, przeglądu historii incydentów i SLA. Braki = brak DoR.


## Fazy cyklu życia

- Planowanie i przygotowanie materiałów/labu.  
- Szkolenie teoretyczne + ćwiczenia (symulacje incydentów).  
- Walidacja umiejętności (quiz/lab).  
- Onboarding do on-call i shadowing.  
- Przegląd i iteracje materiałów.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (network/operations/training)  
- network_outage_response, maintenance_windows_schedule, change_management


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

### Polskie normy i regulacje
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa
- **PT-PL** — Prawo Telekomunikacyjne (Ustawa o komunikacji elektronicznej)
- **UKE-WYTYCZNE** — Wytyczne UKE dot. bezpieczeństwa sieci telekomunikacyjnych

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

1. Przygotuj materiały i lab; zaktualizuj runbooki.  
2. Przeprowadź moduły i ćwiczenia; zbierz wyniki.  
3. Waliduj umiejętności; przypisz on-call/shadowing.  
4. Monitoruj KPI i aktualizuj plan szkolenia i linkage_index.


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

- MTTR: średni czas przywrócenia.  
- Change success rate: % zmian bez incydentów.  
- Shadowing: dołączenie do dyżuru w trybie obserwatora.


## Przykłady użycia

- Szkolenie nowego zespołu NOC po wdrożeniu nowej sieci WAN.  
- Ćwiczenia DDoS z udziałem SOC i NOC.  
- Ujednolicenie praktyk change w rozproszonym zespole.


## Ryzyka i ograniczenia

- Brak labu → teoria bez praktyki.  
- Nieaktualne runbooki → błędne działania.  
- Za mało ćwiczeń → długi MTTR.  
- Słabe progi alertów → fałszywe alarmy i wypalenie.


## Decyzje i uzasadnienia

- Zakres modułów i głębokość (L2/L3).  
- Narzędzia NMS/telemetry preferowane.  
- Kadencja szkoleń i refreshy.  
- Progi KPI docelowe.


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

- Monitoring ↔ Alerty ↔ Incident response.  
- Change ↔ Maintenance ↔ Rollback.  
- Bezpieczeństwo ↔ Dostępy ↔ Audyt.  
- KPI ↔ Raporty ↔ Ulepszenia.


## Struktura sekcji

1) Architektura i narzędzia NOC  
2) Monitoring/alerty i triage  
3) Procedury incydentów (outage, degradacja, DDoS)  
4) Change/maintenance, CAB, rollback  
5) Bezpieczeństwo dostępu (jump hosts, least privilege)  
6) Dokumentacja/runbooki i raporty KPI  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Agenda modułów i labów (BGP/OSPF, link failure, DDoS drill).  
- Checklista triage (warstwa 1/2/3, ACL, DNS, WAN).  
- Procedury komunikacji (status, eskalacje, klient).  
- Plan on-call i shadowing, kryteria gotowości.  
- KPI: MTTR, liczba incydentów, false positives, change success rate.  
- Materiały bezpieczeństwa (dostępy, MFA, logowanie).


## Wymagane streszczenia

- Executive summary: zakres szkolenia, daty, grupy.  
- Skrót KPI NOC i targetów.


## Guidance (skrót)

- Ćwicz na labie z realnymi scenariuszami; rób post‑mortem po ćwiczeniach.  
- Używaj standardowych runbooków; aktualizuj je po każdym incydencie.  
- Monitoring bez triage to szum: kalibruj progi, redukuj false positives.  
- Zawsze planuj rollback dla change; trzymaj okna maintenance.  
- Audytuj dostępy i działania; używaj jump hostów/MFA.  
- Mierz skuteczność szkolenia: KPI przed/po, błędy w labach.


## Checklisty Definition of Ready (DoR)

- [ ] Architektura/runbooki aktualne; narzędzia NMS dostępne.  
- [ ] Lab i dane testowe przygotowane.  
- [ ] Lista uczestników/rol i kontakty eskalacji gotowe.  
- [ ] Polityki change/security znane.  
- [ ] KPI i cele szkolenia ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Szkolenie zrealizowane; uczestnicy zaliczyli walidację.  
- [ ] Runbooki zaktualizowane na podstawie ćwiczeń.  
- [ ] KPI poprawione lub plan działań korygujących.  
- [ ] linkage_index/CMDB zaktualizowane.  
- [ ] Feedback zebrany i zaplanowane iteracje.

