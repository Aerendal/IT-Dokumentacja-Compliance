---
title: Harmonogram implementacji IAM
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Harmonogram implementacji IAM


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan wdrożenia IAM: IdP/SSO, provisioning (SCIM/JIT), role RBAC/ABAC, MFA, logi/audyt, recertyfikacje, komunikacja i change management.


## Zakres i granice

- Obejmuje: etapy (przygotowanie IdP/SCIM, pilotaż, rollout, recertyfikacje), zadania i daty (integracje aplikacji, MFA, RBAC/ABAC, logi/audyt, szkolenia), priorytetyzację aplikacji/zasobów, dependency map, ryzyka/mitigacje/fallback/rollback, komunikację i change management.  
- Poza zakresem: projekt modelu ról (oddzielne dokumenty RBAC/ABAC) – tu harmonogram wdrożeń.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: lista aplikacji/zasobów, polityki IAM/SoD, IdP/SSO/SCIM zdolności, wymagania regulatora, on-call/contact, change policy, szkolenia.  
- Wyjścia: harmonogram fal (pilot→rollout), priorytet aplikacji, plan MFA/RBAC/ABAC, logi/audyt/recerts harmonogram, plan komunikacji, ryzyka i rollback, RACI.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: access_control_matrix_design/reference, rbac_design, abac_design, multi_factor_authentication_design, access_control_testing, logging_and_audit_trail, incident_response_playbook, communication_plan, change_management_plan, risk_register.
- Key Document Structures: etapy, zadania, priorytety, ryzyka, komunikacja.
- Document Dependencies: IdP/SSO/SCIM, HRIS (JML), CMDB, ticketing/change, SIEM/logi, training platform.



## Zależności dokumentu

- Konsumuje: [dokumenty wejściowe — co musi istnieć zanim ten dokument powstanie]
- Dostarcza do: [dokumenty wyjściowe — co korzysta z tego dokumentu]

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

- Cele i zakres
- Kamienie milowe i terminy
- Zasoby i odpowiedzialności
- Zależności
- Ryzyka
- Status i postęp

## Szybkie powiązania

- linkage_index.jsonl (iam/implementation_schedule)
- access_control_matrix_design/reference, rbac_design, abac_design, multi_factor_authentication_design, access_control_testing, logging_and_audit_trail, incident_response_playbook, communication_plan, change_management_plan, risk_register


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
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

1. Ustal fale i priorytety app; wpisz daty/ownerów i zależności.  
2. Dodaj plan MFA/SCIM/logów/recerts i komunikację/CAB; przygotuj rollback.  
3. Aktualizuj postęp, ryzyka i decyzje; zamknij DoR/DoD i linkage_index.


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

- [ ] Priorytety i zależności uwzględnione; MFA/SSO/SCIM/logi/recerts dostarczone; rollback opisany.  
- [ ] Komunikacja/CAB prowadzona; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Gantt/CSV/board, lista app, plan MFA/SCIM/logi, checklisty testów AC, recert schedule, contact list, rollback plan, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % app na SSO/MFA/SCIM, liczba rollbacków/stopów, czas zamknięcia fali, liczba waiverów i czas sunset, zgodność recertyfikacji z planem.

## Kryteria ukończenia

- [ ] Harmonogram IAM wykonany lub zaktualizowany; decyzje i ryzyka udokumentowane; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Etapy i fale (przygotowanie, pilotaż, rollout, recertyfikacje) z datami/ownerami  
2) Zadania per fala (integracje app, MFA, RBAC/ABAC, logi/audyt, szkolenia)  
3) Priorytetyzacja aplikacji/zasobów i dependency map  
4) Ryzyka/mitigacje, fallback/rollback (plan na stop)  
5) Komunikacja i change management (kanały, cadence, CAB, szablony)  
6) Załączniki (Gantt/CSV/board, contact list, checklisty)


## Wymagane rozwinięcia

- Lista aplikacji z priorytetem, kryteriami gotowości i właścicielami.  
- Plan MFA (kto, kiedy, metody), SCIM/JIT provisioning, logi/audyt i SIEM.  
- Plan recertyfikacji (cadence, zakres) i testy AC.  
- Ścieżka rollback/stop i kryteria go/conditional/no‑go.


## Wymagane streszczenia

- Executive: status fal, % app z MFA/SSO/SCIM, główne ryzyka i plan rollback, nadchodzące recertyfikacje.


## Guidance (skrót)

- Zacznij od app krytycznych i z wysokim ryzykiem; pilot przed pełnym rolloutem.  
- Wymagaj MFA i logów; SCIM/JIT gdzie to możliwe; testuj RBAC/ABAC.  
- Zawsze plan rollback/stop i komunikacja; loguj decyzje i zmiany.  
- Recertyfikacje ustaw od razu z cadence; integruj z HRIS (JML).


## Checklisty Definition of Ready (DoR)

- [ ] Lista app/zasobów z priorytetem; IdP/SSO/SCIM gotowe; polityki IAM/SoD znane.  
- [ ] Ownerzy fal i CAB/komunikacja wstępnie ustalone; rollback plan nakreślony.


## Checklisty Definition of Done (DoD)

- [ ] Fale wdrożone; MFA/SSO/SCIM/logi/recerts zgodnie z planem; ryzyka/waivery z sunset; komunikacja i CAB decyzje zapisane; dokument w linkage_index; metadane aktualne.

