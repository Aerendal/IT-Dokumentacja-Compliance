---
title: Audit Logging
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Audit Logging


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Spójne zasady rejestrowania zdarzeń audytowych zapewniające rozliczalność działań użytkowników i systemów oraz spełnienie wymogów bezpieczeństwa i compliance.


## Zakres i granice

- Obejmuje: katalog zdarzeń audytowych, pola obowiązkowe, synchronizację czasu, identyfikację użytkownika/usługi, integralność i retencję logów, kontrolę dostępu, walidację kompletności, raportowanie i przeglądy.  
- Poza zakresem: pełna architektura pipelines logowania (observability), SIEM tuning, runbooki IR (oddzielne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania compliance (SOX/PCI/ISO/RODO), lista krytycznych operacji biznesowych/administracyjnych, katalog ról i tożsamości, topologie systemów, źródła czasu (NTP), polityki retencji.  
- Wyjścia: specyfikacja pól audytowych, lista zdarzeń per system/usługa, zasady retencji i dostępu, plan walidacji i raportowania, linki w linkage_index.


## Założenia
- Sync czasu działa.  
- SIEM/log pipeline dostępne.  
- Zespoły dev/ops współpracują.
## Otwarte pytania
- Jak długo przechowywać logi specyficzne (np. admin DB)?  
- Czy potrzebne jest podpisywanie logów kluczem HSM?  
- Jak często testować odtwarzanie i integralność?
## Powiązania (meta)

- Key Documents: access_control_matrix_reference, api_security_audit, logging_strategy, siem_onboarding, incident_response_runbook, privacy_policy, retention_policy.  
- Key Document Structures: zdarzenia, pola, czas, przechowywanie/retencja, walidacja, dostęp/przeglądy.  
- Document Dependencies: NTP/chrony, IdP/SSO, correlation/trace id, CMDB źródeł logów, klucze/signing, magazyn WORM/S3 with Object Lock.



## Zależności dokumentu
Wymaga: wymagań regulacyjnych, inwentarza systemów/logów, czasu zsynchronizowanego, narzędzi SIEM/ETL, polityk PII/retencji, kontroli dostępu. Braki = DoR otwarte.
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
- Kontekst i cele
- Zakres zdarzeń i format
- PII/maskowanie/anonimizacja
- Retencja i dostęp
- Integracja SIEM/alerty
- Testy i weryfikacja
- Ryzyka
## Szybkie powiązania

- linkage_index.jsonl (security/audit_logging)  
- logging_strategy, siem_onboarding, retention_policy, access_control_matrix_reference, privacy_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
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

1. Określ wymagania regulacyjne i krytyczne operacje; zmapuj źródła logów.  
2. Wybierz/potwierdź schemat pól, źródło czasu i zabezpieczenia; zaprojektuj retencję.  
3. Ustal testy kompletności/integralności, raporty i przeglądy; dodaj powiązania w linkage_index.


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
- WORM: Write Once Read Many storage.  
- Break-glass: awaryjny dostęp pod kontrolą.  
- Audit trail: zapis działań użytkownika/systemu z kontekstem.
## Przykłady użycia
- Przygotowanie do audytu SOC2/PCI.  
- Śledzenie incydentu bezpieczeństwa.  
- Wymogi regulatora (RODO) na retencję logów.
## Ryzyka i ograniczenia
- Brak integralności → logi niewiarygodne.  
- Nadmiar PII → ryzyko privacy.  
- Pipeline drop/outage → luka w audycie.
## Decyzje i uzasadnienia
- Retencja per typ logu i lokalizacja storage.  
- Poziomy dostępu i break-glass.  
- Budżet na storage vs potrzeby compliance.
## Powiązania z innymi dokumentami
- incident_response_runbook — użycie logów.  
- siem_playbook — analiza.  
- data_retention_policy — retencja.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- ISO 27001/SOC2/PCI/RODO wymagania logów i retencji.  
- Wewnętrzne polityki bezpieczeństwa i PII.
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

- [ ] Każde krytyczne zdarzenie ma źródło logu, pola obowiązkowe i trace id.  
- [ ] Retencja zgodna z regulacjami; logi zabezpieczone (immutability, szyfrowanie, RBAC).  
- [ ] Walidacja kompletności/integralności i alerty są aktywne; przeglądy cykliczne zaplanowane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Schemat JSON/Avro logu audytowego, mapa źródeł logów, polityka retencji, konfiguracja WORM/Object Lock, raporty z testów kompletności, ADR/waiver log, dashboardy/alerty.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Pokrycie krytycznych operacji (%), liczba braków logów per okres, czas detekcji braków, wskaźnik integralności (hash chain ok), liczba nieautoryzowanych dostępów do logów, zgodność retencji.

## Kryteria ukończenia

- [ ] Dokument pozwala wdrożyć i utrzymać audytowalne logi (zakres, schemat, retencja, testy, dostęp) i jest powiązany w linkage_index.


## Struktura sekcji

1) Zakres zdarzeń audytowych (authN/authZ, zmiany danych, konfiguracja, uprawnienia, administracja, eksporty)  
2) Format i pola obowiązkowe (kto/co/kiedy/skąd/jaki wynik, correlation/trace id, tenant, wersja schematu, signature)  
3) Czas i synchronizacja (NTP, strefy, tolerancje, monotonic time, drift)  
4) Przechowywanie i retencja (WORM/immutability, szyfrowanie, cykl życia, klasy storage)  
5) Bezpieczeństwo i dostęp (least privilege, separation of duties, break‑glass, audyt dostępu)  
6) Walidacja i testy (coverage completeness, integrity checks, sampling, chaos tests)  
7) Raportowanie i przeglądy (dashboards, okresowe raporty, alerty na braki, procedury review)  
8) Załączniki (mapa źródeł logów, schemat JSON, ADR/waivery)


## Wymagane rozwinięcia

- Lista krytycznych zdarzeń per domena (data change, privilege change, config change, access to PII/export).  
- Schemat logu (JSON/Avro) z polami obowiązkowymi i wersjonowaniem; zasady correlation id.  
- Zabezpieczenia: podpisy, hash chain, WORM, szyfrowanie at-rest/in-transit, RBAC do logów.  
- Retencja: okresy per regulacja, procedura legal hold.  
- Testy kompletności/integralności i alerty na brak logów.


## Wymagane streszczenia

- Executive: zakres pokrycia, status retencji/immutability, główne ryzyka i plan ich mitigacji.


## Guidance (skrót)

- Zawsze używaj czasu z NTP i wersjonuj schematy logów; dodaj trace/correlation id.  
- Logi audytowe oddziel od aplikacyjnych; stosuj WORM lub S3 Object Lock + podpisy.  
- Automatyzuj walidację kompletności (missing logs, gap detection) i alertuj na brak zdarzeń kluczowych.  
- Dostęp do logów tylko read‑only, audytowany; regularne przeglądy uprawnień.  
- Każda zmiana schematu lub zakresu logowania wymaga ADR/waiver i aktualizacji linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Lista krytycznych operacji i wymagań compliance zebrana; źródła czasu uzgodnione.  
- [ ] Zidentyfikowano wszystkie systemy generujące logi audytowe i ich właścicieli.  
- [ ] Ustalony magazyn z opcją immutability oraz wstępna polityka retencji.


## Checklisty Definition of Done (DoD)

- [ ] Schemat/log format zatwierdzony; lista zdarzeń per system kompletna; linkage_index zaktualizowany.  
- [ ] Retencja i zabezpieczenia wdrożone; testy kompletności/integralności działają; raporty/przeglądy mają właścicieli.  
- [ ] Status/metadane aktualne; checklisty DoR/DoD odhaczone.

