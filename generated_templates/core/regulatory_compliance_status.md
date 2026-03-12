---
title: Regulatory Compliance Status
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Regulatory Compliance Status


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Raport statusu prac regulacyjnych: produkty/rynki w scope, wymagania i dowody, status RAG, ryzyka/blokery, plan działań i kamienie, nadchodzące audyty/recertyfikacje.


## Zakres i granice

- Obejmuje: produkty/rynki, wymagania i status (spełnione/otwarte/RAG), dowody (dokumenty/testy/certyfikaty z datami), ryzyka i blokery, plan działań i kamienie milowe, terminy audytów/przeglądów/recertyfikacji, komunikację do kierownictwa/regulatora.  
- Poza zakresem: szczegółowe mapowanie kontroli (osobne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: katalog wymagań/SoA, repo dowodów, raporty audytów/testów, risk register, harmonogram audytów, status prac projektowych.  
- Wyjścia: status RAG per wymaganie/produkt, lista ryzyk i blockerów, plan działań (owner/ETA), kamienie milowe, kalendarz audytów/recertyfikacji, raport dla kierownictwa/regulatora.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: compliance_verification, compliance_with_regulations, regulatory_compliance_review, mapowanie_compliance, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan.
- Key Document Structures: produkty/rynki, wymagania/status, dowody, ryzyka/blokery, plan działań, audyty/przeglądy.
- Document Dependencies: repo dowodów, GRC/ticketing, SIEM/logi, skany/testy, właściciele kontroli.



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
- Cel i zakres polityki
- Zakres obowiązywania i wyjątki
- Role i odpowiedzialności
- Wymagania/kontrole (techniczne/procesowe)
- Proces zarządzania zmianą i wyjątkami
- Dowody/audyt, metryki zgodności
- Komunikacja/szkolenia i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (compliance/status)
- compliance_verification, compliance_with_regulations, regulatory_compliance_review, mapowanie_compliance, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan


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

1. Uzupełnij scope, tabelę statusów i dowody.  
2. Dodaj ryzyka/blokery i plan działań; zsynchronizuj audyty/przeglądy.  
3. Przygotuj raport dla kierownictwa/regulatora; zaktualizuj linkage_index/checklisty.


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

- [ ] Każde wymaganie ma dowód, status i ownera; luki mają plan.  
- [ ] Kalendarz audytów/przeglądów zgodny z planem działań; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Tabela statusu/CSV, repo dowodów, raporty testów/audytów, kalendarz audytów, plan działań, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % wymagań z dowodem, liczba luk/waiverów i czas sunset, terminowość audytów/recertyfikacji, czas zamknięcia działań, dokładność dat dowodów.

## Kryteria ukończenia

- [ ] Raport statusu aktualny, plan działań ustawiony, audyty zsynchronizowane; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Produkty/rynki objęte (scope, daty, właściciele)  
2) Wymagania i status (RAG, dowody/linki, data dowodu)  
3) Ryzyka i blokery (impact, prawdopodobieństwo, powiązanie z risk register)  
4) Plan działań i kamienie (owner, ETA, priorytet)  
5) Audyty/przeglądy/recertyfikacje (daty, zakres, przygotowanie)  
6) Komunikacja i odbiorcy (kierownictwo, regulator/klienci)  
7) Załączniki (export statusu, raporty testów, kalendarz audytów)


## Wymagane rozwinięcia

- Tabela statusu: wymaganie → dowód → data → status RAG → owner → następny krok.  
- Plan działań dla luk/ryzyk; harmonogram audytów/przeglądów.  
- Szablon raportu dla kierownictwa/regulatora.


## Wymagane streszczenia

- Executive: status RAG per produkt, top ryzyka/blokery, plan działań i ETA, najbliższe audyty/recertyfikacje.


## Guidance (skrót)

- Brak dowodu = status czerwony; aktualizuj daty dowodów.  
- Ryzyka/blokery muszą mieć właściciela i plan; aktualizuj risk register.  
- Synchronizuj kalendarz audytów z planem działań; komunikuj zmiany.


## Checklisty Definition of Ready (DoR)

- [ ] Katalog wymagań/SoA i repo dowodów dostępne; harmonogram audytów znany.  
- [ ] Właściciele kontroli/produktów wskazani; kryteria RAG ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Statusy RAG i dowody wpisane; ryzyka/blokery i plan działań z owner/ETA; audyty zaplanowane.  
- [ ] Raport przygotowany/udostępniony; dokument w linkage_index; metadane aktualne.

