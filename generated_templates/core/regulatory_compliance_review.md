---
title: Regulatory Compliance Review
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Regulatory Compliance Review


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Procedura cyklicznego przeglądu zgodności: zakres produktów/rynków, checklista wymagań i dowodów, wyniki, wyjątki i działania korygujące, raportowanie i follow‑up.


## Zakres i granice

- Obejmuje: zakres przeglądu (produkty/rynek), checklistę wymagań/dowodów, wyniki (zgodne/niezgodne/RAG), wyjątki/waivery z sunset, działania korygujące (owner/ETA), raportowanie do interesariuszy/regulatora, harmonogram przeglądów/follow‑up.  
- Poza zakresem: projektowanie kontrolek (w politykach) i pełne audyty certyfikacyjne (oddzielne).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: katalog wymagań/SoA, repo dowodów, wyniki audytów/testów/skanów, risk register, poprzednie przeglądy.  
- Wyjścia: wypełniona checklista, raport RAG, lista wyjątków/waiverów i działań korygujących (owner/ETA), plan follow‑up/retestów, komunikacja do interesariuszy/regulatora.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: compliance_verification, compliance_with_regulations, mapowanie_compliance, compliance_monitoring_runbook/tools, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan.
- Key Document Structures: zakres, checklista/dowody, wyniki, wyjątki/waivery, działania, raport/follow‑up.
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

- linkage_index.jsonl (compliance/regulatory_review)
- compliance_verification, compliance_with_regulations, mapowanie_compliance, compliance_monitoring_runbook/tools, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
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

1. Zdefiniuj zakres i właścicieli; wypełnij checklistę wymagania→dowody→status.  
2. Zapisz wyjątki/waivery i działania korygujące; przygotuj raport i odbiorców.  
3. Zaplanuj follow‑up/retesty; zaktualizuj linkage_index/checklisty.


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

- [ ] Wymagania mają dowody/status/owner; waivery mają sunset.  
- [ ] Działania korygujące i retesty zaplanowane; raport dostarczony.  
- [ ] Dokument w linkage_index; relacje cross‑doc opisane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Checklista/CSV, raport, repo dowodów, waiver log, plan działań/retestów, risk register wpisy, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % wymagań z dowodem, liczba wyjątków i czas sunset, czas zamknięcia działań korygujących, terminowość raportów i retestów.

## Kryteria ukończenia

- [ ] Przegląd zakończony, raport i plan działań opublikowane; follow‑up ustawiony; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres przeglądu (produkty/rynek, daty, właściciele)  
2) Checklista wymagań i dowodów (status RAG, lokalizacja dowodów)  
3) Wyniki i wyjątki/waivery (sunset, kompensacje)  
4) Działania korygujące (owner, ETA, priorytet)  
5) Raportowanie (odbiorcy, format, terminy; regulator/klienci jeśli dotyczy)  
6) Follow‑up i przeglądy (retesty, audyt, cadence)  
7) Załączniki (checklista/CSV, raport, waiver log, plan działań)


## Wymagane rozwinięcia

- Kryteria RAG i akceptacji; szablon raportu.  
- Lista interesariuszy/regulatorów i wymagane formaty/termine raportów.  
- Harmonogram retestów i przeglądów; ścieżka eskalacji.


## Wymagane streszczenia

- Executive: status RAG, top wyjątki/waivery, plan działań z ETA, najbliższy retest/audyt.


## Guidance (skrót)

- Brak dowodu = niezgodne; status opieraj na dowodach z datą.  
- Wyjątki/waivery zawsze z sunset/kompensacją; aktualizuj risk register.  
- Ustal jasny plan follow‑up i terminy raportów; komunikuj wyniki wcześnie.


## Checklisty Definition of Ready (DoR)

- [ ] Katalog wymagań/SoA i repo dowodów dostępne; kryteria RAG ustalone.  
- [ ] Ownerzy kontroli i interesariusze raportu wskazani.


## Checklisty Definition of Done (DoD)

- [ ] Checklista wypełniona; raport RAG i wyjątki/waivery opisane; działania korygujące z owner/ETA; follow‑up zaplanowany; dokument w linkage_index; metadane aktualne.

