---
title: Search Audit Logging
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Search Audit Logging


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Określić zasady audytowania zapytań wyszukiwania, aby zapewnić rozliczalność, bezpieczeństwo i zgodność z prywatnością: co logować, jak maskować PII, retencja, dostęp i raportowanie nadużyć.


## Zakres i granice

- Obejmuje: pola audit logów search (zapytanie, user/session id, czas, źródło, wynik/stan, latency), PII/maskowanie/anonimizacja, retencję i storage, dostęp/RBAC i przeglądy nadużyć, raportowanie (metryki nadużyć, incydenty), zgodność privacy/security.  
- Poza zakresem: produktowa analityka usage (osobne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania privacy/security, klasyfikacja danych, architektura search, polityki retencji, wymagania regulatora/klienta.  
- Wyjścia: specyfikacja pól audytowych, zasady maskowania/anonimizacji, plan retencji i dostępu, procedura przeglądów nadużyć/raportów.


## Założenia
- Sync czasu działa.  
- SIEM/log pipeline dostępne.  
- Zespoły dev/ops współpracują.
## Otwarte pytania
- Jak długo przechowywać logi specyficzne (np. admin DB)?  
- Czy potrzebne jest podpisywanie logów kluczem HSM?  
- Jak często testować odtwarzanie i integralność?
## Powiązania (meta)

- Key Documents: privacy_policy, data_classification, logging_and_audit_trail, security_requirements, incident_response_playbook, breach_notification_procedure, data_retention_policy.
- Key Document Structures: pola logów, PII/maskowanie, retencja/storage, dostęp/przeglądy, raportowanie.
- Document Dependencies: search platform, IAM/RBAC, SIEM/log storage, masking/anonymization tools, ticketing/IR.



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

- linkage_index.jsonl (search/audit_logging)
- privacy_policy, data_classification, logging_and_audit_trail, security_requirements, incident_response_playbook, breach_notification_procedure, data_retention_policy


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

1. Zdefiniuj pola logów i maskowanie; ustaw retencję/storage.  
2. Skonfiguruj RBAC i przeglądy nadużyć; podłącz alerty/raporty.  
3. Aktualizuj po zmianach architektury/retencji/regulacji; zamknij DoR/DoD i linkage_index.


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

- [ ] PII zminimalizowane/maskowane; retencja i dostęp zgodne z politykami; alerty raportują nadużycia; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Schemat logów, mask rules, storage/retention config, RBAC listy, raporty nadużyć, alert configs, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % logów spełniających schemat, liczba naruszeń maskowania, terminowość przeglądów dostępu, czas reakcji na alert nadużyć, liczba waiverów i czas sunset.

## Kryteria ukończenia

- [ ] Audyt logowania wyszukiwań wdrożony zgodnie z politykami; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres i pola audytowe zapytań (co logujemy/nie logujemy; format)  
2) PII i maskowanie/anonimizacja (reguły dla query/user/session/fields)  
3) Retencja i przechowywanie (lokalizacja, szyfrowanie, czas, legal hold)  
4) Dostęp i przeglądy (RBAC, przeglądy nadużyć, audyt dostępu)  
5) Raportowanie i alerty (metryki nadużyć, incydenty, procedura IR)  
6) Ryzyka i waivery (sunset/kompensacje)  
7) Załączniki (schemat logu, przykłady, mask rules, checklisty)


## Wymagane rozwinięcia

- Schemat logu (pola obowiązkowe/zakazane), reguły maskowania/anonimizacji.  
- Retencja: czasy, legal hold, szyfrowanie, lokalizacja; log rotation.  
- Dostęp: role, przeglądy okresowe, audyt; procedura analizy nadużyć i eskalacji IR.


## Wymagane streszczenia

- Executive: jakie pola logujemy, retencja, maskowanie, kto ma dostęp, jak raportujemy nadużycia.


## Guidance (skrót)

- Minimalizuj PII; maskuj/anonymizuj zapytania i identyfikatory gdzie możliwe.  
- Logi szyfruj, trzymaj z retencją i audytem dostępu; przeglądy okresowe.  
- Alertuj na wzorce nadużyć; integruj z IR/Breach procedurami.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania privacy/security i klasyfikacja danych znane; architektura search opisana.  
- [ ] Narzędzia logowania/maskowania i storage dostępne; właściciele wskazani.


## Checklisty Definition of Done (DoD)

- [ ] Schemat logów i maskowanie zdefiniowane; retencja i RBAC ustawione; alerty/raporty działają; dokument w linkage_index; metadane aktualne.

