---
title: Audit Trail
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Audit Trail


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zdefiniować wymagania i standard dla ścieżki audytu (audit trail) w systemach: co logować, jak przechowywać, jak zapewnić nienaruszalność i dostępność na potrzeby zgodności i dochodzeń.


## Zakres i granice

- Obejmuje: zdarzenia do logowania (auth, zmiany danych, konfiguracje, admin, integracje), format logów, znaczniki czasu/korelacja, nienaruszalność (WORM/signed), retencję, dostęp/RO, maskowanie PII, monitoring anomalii, eksport/raporty dla audytorów, testy i weryfikacje.
- Poza zakresem: logowanie telemetryczne nieaudytowe (osobne dokumenty observability).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: polityki compliance, wymagania audytu (ISO/SOC/PCI/RODO), inwentarz systemów, mapy danych i PII, limity kosztowe, narzędzia logowania/siem, klasyfikacja zdarzeń.  
- Wyjścia: katalog logów i pól obowiązkowych, konfiguracja retencji/archiwum, kontrola dostępu, procedury przeglądów i testów, raporty zgodności, checklisty DoR/DoD.
## Założenia
- Sync czasu działa.  
- SIEM/log pipeline dostępne.  
- Zespoły dev/ops współpracują.
## Otwarte pytania
- Jak długo przechowywać logi specyficzne (np. admin DB)?  
- Czy potrzebne jest podpisywanie logów kluczem HSM?  
- Jak często testować odtwarzanie i integralność?
## Powiązania (meta)
- Key Documents: security_requirements, incident_response_runbook, data_retention_policy, logging_standards, siem_playbook, access_control_policy.  
- Key Document Structures: źródła, pola, retencja, bezpieczeństwo, przeglądy, raporty.  
- Document Dependencies: SIEM/log pipeline, IAM, time sync, storage (WORM/immutable), CMDB.
## Zależności dokumentu
Wymaga: wymagań regulacyjnych, inwentarza systemów/logów, czasu zsynchronizowanego, narzędzi SIEM/ETL, polityk PII/retencji, kontroli dostępu. Braki = DoR otwarte.
## Fazy cyklu życia
- Planowanie logów i retencji.  
- Wdrożenie i monitorowanie pipeline.  
- Przeglądy okresowe i testy odtwarzania.  
- Audyty i ulepszenia.
## Struktura sekcji (szkielet)

- Wymogi regulacyjne i zakres zdarzeń
- Format logów i korelacja (trace-id, user-id)
- Bezpieczeństwo i nienaruszalność (WORM, podpisy, checksum)
- Retencja i archiwizacja
- Dostęp i maskowanie PII, role
- Monitoring/anomalie i alerty
- Eksport/raporty dla audytorów
- Testy i walidacja audit trail


## Szybkie powiązania

- Security Logging, Privacy, Data Retention, Incident Response, Compliance (SOX/PCI/GxP).


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
1. Zidentyfikuj źródła/pola i ustaw retencję; skonfiguruj pipeline.  
2. Zabezpiecz logi (RBAC, WORM, maskowanie); monitoruj i alertuj.  
3. Wykonuj przeglądy/testy; raportuj zgodność; aktualizuj DoR/DoD i linkage_index.
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

## Wejścia

- Wymogi regulacyjne (SOX/PCI/GxP/RODO), polityki bezpieczeństwa, architektura systemu, katalog zdarzeń, wymagania audytu zewnętrznego.


## Wyjścia

- Specyfikacja audit trail: zdarzenia, format, retencja, kontrole integralności, procedury dostępu/eksportu, checklisty testów.



## Jak używać (checklista)

- Określ wymagane zdarzenia i format; włącz korelację trace/user.
- Skonfiguruj WORM/podpisy; ustaw retencję i role dostępu RO.
- Zaimplementuj alerty anomalii; przygotuj procedury eksportu i testy.


## Wymagane rozwinięcia / powiązania

- Tabela zdarzeń i pól, schemat logu, procedura eksportu, matryca ról, test nienaruszalności, wzory raportów audytowych.


## Kryteria DoR

- Wymogi regulacyjne znane; katalog zdarzeń wstępnie zebrany; architektura logowania dostępna.


## Kryteria DoD

- Audit trail skonfigurowany, zabezpieczony, retencja ustawiona; testy integralności/eksportu wykonane; procedury udokumentowane.


## Artefakty

- Spec audit trail, konfiguracje logów, wyniki testów, procedury eksportu, raporty audytowe.


## Walidacja

- Test WORM/podpisów, próby eksportu i odtwarzania, audyt próbki logów; kontrola dostępów.


## Metryki

- Pokrycie zdarzeń audytowych, czas na znalezienie zdarzenia, incydenty naruszenia integralności, sukces testów eksportu.


## Utrzymanie

- Przegląd półroczny zdarzeń/pól/retencji; test integralności; aktualizacja wraz z wymaganiami regulacyjnymi.


## Zakończenie

Solidny audit trail wspiera zgodność i dochodzenia; utrzymuj go z zabezpieczeniami, retencją i testami.

