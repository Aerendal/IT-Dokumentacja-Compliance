---
title: Access Control Review
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Access Control Review


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Definiuje przeglądy kontroli dostępu (recertyfikacje) dla ról/uprawnień/SoD: zakres, częstotliwość, właścicieli, kryteria i dowody, aby utrzymać least privilege i zgodność (SOX/PCI/RODO).


## Zakres i granice

- Obejmuje: typy przeglądów (rola/user/access/SoD), częstotliwości, zakres systemów/danych, właścicieli i approverów, procedurę przeglądu, wyjątki/waivery z sunset, dowody i raporty, integracje z IAM/CMDB/ticketing.
- Poza zakresem: projekt macierzy AC (osobno) i operacyjne nadania (JML workflow).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: macierze ról/uprawnień, SoD rules, listy użytkowników i dostępów, CMDB/asset, wymagania audyt/regulator, harmonogram JML/zmian, wcześniejsze odchylenia.
- Wyjścia: decyzje keep/remove/adjust, waivery z sunset/kompensacjami, raport przeglądu, action items (owner/ETA), metryki (completion, violations, findings), dowody dla audytu.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: access_control_matrix_design, access_control_policy, access_control_improvement_plan, multi_factor_authentication_design, logging_and_audit_trail, security_controls_reference, risk_register.
- Dependencies: IdP/IAM, CMDB/asset, HR/JML, ticketing/workflow, SIEM/logi, SoD rules, audyt schedule.


## Zależności dokumentu

- Upstream: macierze ról, SoD rules, listy access, wymagania audyt/regulator, harmonogram JML/zmian.
- Downstream: zmiany access (remove/adjust), waivery, raporty audytowe, risk register aktualizacje, improvement backlog.
- Zewnętrzne: audytorzy/regulatorzy.


## Fazy cyklu życia

- Planowanie (zakres, częstotliwość, ownerzy).
- Wykonanie przeglądu.
- Decyzje i wdrożenie zmian (remove/adjust/waiver).
- Raportowanie i retrospektywa.



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

- access_control_matrix_design, access_control_improvement_plan, access_control_policy, multi_factor_authentication_design, logging_and_audit_trail, security_controls_reference, risk_register


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.
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

- [ ] Każdy dostęp/rola w scope ma decyzję (keep/remove/adjust/waiver) i dowód.
- [ ] Waivery mają sunset/kompensacje; KPI (completion, violations, time-to-close) obliczone.
- [ ] Raport zawiera dowody i jest zgodny z wymaganiami audytu/regulatora.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Harmonogram i raport przeglądów, exporty access/SoD, waiver log, ticket log, KPI dashboard, ADR log.


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

- Zakres/frequency → procedura → decyzje → waivery/action items → raport/KPI.


## Struktura sekcji

1) Streszczenie (zakres, completion, violations, top findings)  
2) Zakres i częstotliwość przeglądów (systemy, role, SoD, user access)  
3) Procedura przeglądu (dane wejściowe, narzędzia, kroki, SLA)  
4) Rola/owner/approver, podział obowiązków (SoD)  
5) Decyzje i egzekucja (remove/adjust/waiver, ticketing, ETA)  
6) Waivery/wyjątki (powód, kompensacje, sunset, przegląd)  
7) Raportowanie i dowody (audyt, KPI: completion, violations, time-to-close)  
8) Ryzyka i zależności; decyzje (ADR) i otwarte pytania  


## Wymagane rozwinięcia

- Harmonogram przeglądów; wzór raportu; lista ownerów/approverów; procedura SoD; log waivers; checklisty recertyfikacji.
- Integracja z IAM/CMDB/ticketing; dowody (exporty, podpisy, logi).


## Wymagane streszczenia

- Executive summary: completion, violations, top findings, waivery, rekomendacje.
- One-pager: zakres, wyniki, waivery, terminy zamknięcia.


## Guidance (skrót)

- DoR: zakres/systemy/role/SoD zebrane; ownerzy/approverzy znani; narzędzia IAM/CMDB/ticketing dostępne; SLA i wymagania audytu/regulatora znane.
- DoD: przegląd wykonany; decyzje i zmiany w ticketingu; waivery z sunset; raport/KPI; metadane aktualne; dokument w linkage_index.
- Spójność: każde uprawnienie ma decyzję; waivery mają sunset/kompensacje; raport zawiera dowody i KPI.


## Checklisty Definition of Ready (DoR)

- [ ] Zakres/systemy/role/SoD i ownerzy/approverzy zebrani; narzędzia IAM/CMDB/ticketing dostępne; SLA/requirement audytu znane.


## Checklisty Definition of Done (DoD)

- [ ] Przegląd wykonany; decyzje wdrożone; waivery z sunset/kompensacjami; raport/KPI/dowody gotowe; dokument w linkage_index.

