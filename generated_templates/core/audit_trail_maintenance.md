---
title: Audit Trail Maintenance
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Audit Trail Maintenance


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje zasady utrzymania ścieżek audytu: zakres logów, retencja, bezpieczeństwo, integralność i dostęp. Ma zapewnić zgodność (ISO/SOC/PCI/RODO), wsparcie dochodzeń i minimalizację ryzyka.


## Zakres i granice

- Obejmuje: źródła logów (aplikacje, DB, admin, IAM, sieć), formaty i korelację, identyfikację użytkowników/akcji, stemplowanie czasu, integralność (hash/immutable storage/WORM), retencję i archiwizację, bezpieczeństwo (szyfrowanie, kontrola dostępu), monitoring log pipeline, testy odtwarzania, raporty zgodności, procedury przeglądu.  
- Poza zakresem: pełne runbooki IR (linkowane).


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

- linkage_index.jsonl (audit/trail/maintenance)  
- logging_standards, data_retention_policy, siem_playbook, access_control_policy


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

## Powiązania sekcja↔sekcja

- Źródła/pola → Retencja/bezpieczeństwo → Raporty/przeglądy.  
- Integralność → Dochodzenia/audyt → Testy odtwarzania.  
- Access control → PII → Zgodność.


## Struktura sekcji

1) Zakres logów i obowiązkowe pola (kto/co/kiedy/skąd)  
2) Źródła i pipeline (kolekcja, korelacja, time sync)  
3) Integralność i bezpieczeństwo (hash, WORM, szyfrowanie, RBAC)  
4) Retencja/archiwizacja i koszty (policy per typ zdarzeń)  
5) Dostęp do logów (least privilege, break-glass, PII masking)  
6) Monitoring/alerty pipeline (opóźnienia, drop, błędy)  
7) Testy odtwarzania i gotowości audytowej  
8) Raporty i przeglądy okresowe (ISO/SOC/PCI/RODO)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Macierz źródeł logów i pól; SLA na dostarczenie.  
- Polityki retencji/archiwum per typ logu.  
- Procedura testów integralności/odtwarzania.  
- Plan przeglądów i raportów zgodności.


## Wymagane streszczenia

- Executive snapshot: pokrycie logów, status retencji, incydenty pipeline.  
- Krótka karta „obowiązkowe pola” dla zespołów dev.


## Guidance (skrót)

- Zbieraj „kto/co/kiedy/skąd” i koreluj request-ID/session.  
- Używaj czasu zsynchronizowanego (NTP) i WORM/immutable dla krytycznych logów.  
- Maskuj PII; kontroluj dostęp (RBAC, break-glass).  
- Monitoruj pipeline; testuj odtwarzanie i integralność.  
- Aktualizuj retencję zgodnie z regulacjami i kosztami.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania compliance i pola obowiązkowe znane.  
- [ ] Źródła logów i dostęp do nich zidentyfikowane.  
- [ ] Time sync i narzędzia SIEM/pipeline dostępne.  
- [ ] Polityki retencji/PII określone.  
- [ ] Role i uprawnienia do logów uzgodnione.


## Checklisty Definition of Done (DoD)

- [ ] Logi zbierane i zabezpieczone; status/wersja/data uzupełnione.  
- [ ] Retencja/archiwum wdrożone; testy odtwarzania wykonane.  
- [ ] Raporty/przeglądy zgodności przygotowane; wyjątki opisane.  
- [ ] Monitoring pipeline działa; alerty skonfigurowane.  
- [ ] Linkage_index i risk register zaktualizowane.

