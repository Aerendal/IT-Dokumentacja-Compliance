---
title: Wytyczne best practices hospitality tech
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Wytyczne best practices hospitality tech


## Metadane

- Właściciel: Clinical Lead
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Best practices technologiczne dla hospitality: integracje PMS/POS/CRM, bezpieczeństwo danych gości, niezawodność/SLA, UX gościa (mobile key), monitoring/compliance, incident/DR.


## Zakres i granice

- Obejmuje: integracje PMS/POS/CRM (rezerwacje, billing, lojalność), bezpieczeństwo danych gości (PII/payment, tokenizacja, PCI, privacy), niezawodność i SLA (check-in/out, płatności, klucze), UX gościa (mobile key/app, kioski), monitoring i compliance (PCI/RODO), incident/DR (konta/lockout, awarie kart/kluczy, fallback offline).  
- Poza zakresem: projekt sprzętu zamków i sieci Wi-Fi gości (osobne dokumenty).


## Użytkownicy i interesariusze
- **Clinical Lead / Chief Medical Officer** — definiuje wymagania kliniczne i waliduje
- **Integration Architect** — projektuje integracje z systemami szpitalnymi
- **Security / Privacy Officer** — zapewnia zgodność z HIPAA, RODO, ustawa o ochronie zdrowia
- **Development Team** — implementuje funkcjonalności kliniczne

## Wejścia i wyjścia

- Wejścia: wymagania biznesowe hotelu, integracje PMS/POS/CRM, polityki PCI/privacy, architektura sieci, SLA partnerów, feedback gości.  
- Wyjścia: checklisty integracji i bezpieczeństwa, praktyki UX, plan monitoring/incident/DR, metryki i SLA.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: privacy_policy, pci_dss_compliance, security_requirements, incident_response_playbook, disaster_recovery_plan, monitoring_strategy_document, customer_experience_strategy, mobile_app_security.
- Key Document Structures: integracje, bezpieczeństwo, SLA, UX/mobile key, monitoring/compliance, incident/DR.
- Document Dependencies: PMS/POS/CRM API, płatności, zamki/mobile key, sieć gości, SIEM/monitoring, ticketing.



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
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (hospitality/best_practices)
- privacy_policy, pci_dss_compliance, security_requirements, incident_response_playbook, disaster_recovery_plan, monitoring_strategy_document, customer_experience_strategy, mobile_app_security


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **HL7 FHIR** — Standard Wymiany Danych w Ochronie Zdrowia
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)

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

1. Uzupełnij integracje, bezpieczeństwo/PCI/privacy, SLA/UX.  
2. Dodaj monitoring/compliance i playbooki incident/DR; linkuj checklisty.  
3. Aktualizuj po zmianach partnerów/produktów; zamknij DoR/DoD i linkage_index.


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

- [ ] Integracje i SLA opisane; bezpieczeństwo/PCI/privacy uwzględnione; monitoring/incident przygotowane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Checklisty integracji/testów, polityki PII/payment/tokenizacja, SLA/fallback, monitoring dashboards, playbooki incident/DR, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Uptime check-in/out/płatności, czas lockout gościa, QoE mobile key, liczba incydentów PCI/privacy, czas reakcji na incydenty.

## Kryteria ukończenia

- [ ] Best practices opisane, checklisty gotowe, metryki/alerty działają; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Integracje PMS/POS/CRM (zakres, dane, SLA, testy)  
2) Bezpieczeństwo danych gości (PII/payment, PCI/tokenizacja, privacy, access control)  
3) Niezawodność i SLA (check-in/out, płatności, klucze, kioski; redundant paths)  
4) UX gościa i mobile key (journey, offline, fallback)  
5) Monitoring i compliance (metryki, PCI/RODO, audyt, alerty)  
6) Incident i DR (scenariusze: lockout, awarie kart/kluczy, POS/PMS down; fallback/BCP)  
7) Załączniki (checklisty, szablony testów, contact list partnerów)


## Wymagane rozwinięcia

- Checklisty integracji/testów; polityki PII/payment/tokenizacja; SLA i fallback offline; playbooki incident/DR.  
- Metryki: uptime check-in/out/płatności, czas lockout, QoE mobile key, incydenty PCI/privacy.


## Wymagane streszczenia

- Executive: status integracji, bezpieczeństwo/PCI/privacy, SLA krytyczne, główne ryzyka i plany DR.


## Guidance (skrót)

- Priorytet: bezpieczny check-in/out i płatność; tokenizuj dane; trzymaj fallback offline.  
- Testuj mobile key/kioski w sieci gości; monitoruj SLA i QoE.  
- Ustal jasne playbooki dla lockout/POS/PMS down; audytuj PCI/privacy.


## Checklisty Definition of Ready (DoR)

- [ ] Integracje PMS/POS/CRM i polityki PCI/privacy zebrane; SLA partnerów znane.  
- [ ] Ownerzy sekcji i kanały komunikacji z partnerami ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Checklisty integracji/bezpieczeństwa/UX/monitoringu/incident gotowe; metryki i SLA opisane; dokument w linkage_index; metadane aktualne.

