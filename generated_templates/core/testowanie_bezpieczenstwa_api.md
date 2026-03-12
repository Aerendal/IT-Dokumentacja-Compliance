---
title: Testowanie bezpieczeństwa API
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Testowanie bezpieczeństwa API


## Metadane

- Właściciel: QA Lead
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan i standard testów bezpieczeństwa API (manualnych i automatycznych) obejmujących OWASP API Top 10, ochronę przed nadużyciami, integralność danych i zgodność z wymaganiami bezpieczeństwa.


## Zakres i granice

- Obejmuje: zakres testów (AuthN/AuthZ, rate limit/abuse, input validation/schema, injection, BOLA, SSRF, IDOR, replay, storage/transport security), fuzzing i DAST/SAST dla kontraktu API, środowiska i dane testowe, raportowanie i klasyfikację incydentów, retesty i SLA napraw, automatyzację w CI/CD.  
- Poza zakresem: pełny pentest sieciowy, monitoring produkcyjny (osobne runbooki).


## Użytkownicy i interesariusze
- **QA Lead / Test Manager** — planuje strategię testowania i zarządza procesem QA
- **QA Engineer** — projektuje i wykonuje przypadki testowe
- **Development Team** — naprawia defekty i dostarcza testowalny kod
- **Product Owner** — definiuje kryteria akceptacji i priorytetyzuje defekty

## Wejścia i wyjścia

- Wejścia: kontrakt API (OpenAPI/AsyncAPI), model uprawnień, profile ruchu/limity, dane wrażliwe/PII, polityka bezpieczeństwa, narzędzia (fuzzer, DAST, SCA, SAST), środowiska testowe.  
- Wyjścia: plan testów, scenariusze i checklisty, konfiguracje narzędzi (fuzz/DAST), raport z wynikami i severity, bilety na naprawy z SLA, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: design_bezpieczenstwa_api, specyfikacja_wymagan_api, strategia_wersjonowania_api, logging_strategy, audit_logging, rate_limiting_requirements.  
- Key Document Structures: zakres testów, narzędzia/automatyzacja, środowiska/dane, raportowanie/severity, retesty/SLA.  
- Document Dependencies: CI/CD pipeline, secret management, test data management, gateway/WAF config, SIEM.



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

- Zakres testów i kryteria akceptacji
- Przypadki testowe (TC)
- Środowisko testowe
- Dane testowe
- Wyniki i raporty
- Defekty i status

## Szybkie powiązania

- linkage_index.jsonl (security/api_security_testing)  
- design_bezpieczenstwa_api, specyfikacja_wymagan_api, logging_strategy


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

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa

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

1. Zbierz kontrakt i mapuj OWASP na endpointy; ustal priorytety.  
2. Skonfiguruj narzędzia i dane testowe; uruchom automaty w CI/CD i manuale na ryzykownych ścieżkach.  
3. Raportuj severity, otwieraj bilety z SLA, retestuj; zaktualizuj linkage_index i checklisty.


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

- [ ] Zakres OWASP API Top 10 pokryty; abuse cases przetestowane.  
- [ ] Dane testowe bez PII; wyniki włączone w CI/CD gates; severity/SLA stosowane.  
- [ ] Linkage_index zawiera dokument; retesty potwierdzają naprawy.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Raporty fuzz/DAST, listy scenariuszy, dane testowe, bilety z SLA, logi/trace, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Liczba krytycznych/High na iterację, średni czas naprawy (MTTR) dla defektów bezpieczeństwa, pokrycie OWASP, odsetek buildów zablokowanych przez testy, odsetek waiverów wygasłych.

## Kryteria ukończenia

- [ ] Plan testów bezpieczeństwa API zaimplementowany (zakres, narzędzia, raportowanie, SLA) i powiązany w linkage_index.


## Struktura sekcji

1) Zakres i priorytety (OWASP API Top 10, abuse cases, AuthN/AuthZ, rate limit)  
2) Narzędzia i automatyzacja (fuzzing, contract-based DAST, SAST/SCA, replay protection tests)  
3) Środowiska i dane testowe (separacja, masking/synthetic data, test accounts, keys)  
4) Scenariusze i checklisty (manual + automaty, happy/sad/abuse paths, BOLA/IDOR)  
5) Raportowanie i severity (CVSS/OWASP risk, bilety, exploitability, evidence)  
6) Retesty i SLA (czas napraw, gate w CI/CD, waiver process)  
7) Załączniki (skrypty, config narzędzi, ADR/waiver log)


## Wymagane rozwinięcia

- Mapowanie OWASP API Top 10 do konkretnych endpointów i scenariuszy.  
- Polityka danych testowych (masking, synthetic, klucze/sekrety).  
- Definicje severity i SLA napraw; kryteria blokujące release.  
- Integracja z CI/CD: kiedy uruchamiamy (PR, nightly, pre‑prod), jak raportujemy.  
- Procedura waiver i retestu po fixie.


## Wymagane streszczenia

- Executive: stan testów bezpieczeństwa, liczba krytycznych/lub blockerów, plan napraw i ryzyka.


## Guidance (skrót)

- Zawsze uruchamiaj testy kontraktowe i fuzzing na zmodyfikowanych endpointach; pełny pakiet cyklicznie.  
- Autoryzacja: testuj BOLA/IDOR osobno; używaj wielu ról/tenantów.  
- Dane testowe nie mogą zawierać produkcyjnych PII; klucze testowe rotuj.  
- Fail‑the‑build dla krytycznych findings bez waiver; retest musi potwierdzić fix.  
- Loguj dowody (request/response, trace id) i koreluj z audit logs.


## Checklisty Definition of Ready (DoR)

- [ ] Kontrakt i role/tenanty dostępne; środowisko testowe gotowe; dane testowe zmaskowane/synthetic.  
- [ ] Narzędzia fuzz/DAST/SAST/SCA skonfigurowane; polityka severity/SLA uzgodniona.


## Checklisty Definition of Done (DoD)

- [ ] Testy uruchomione, wyniki zseverityowane, bilety utworzone; linkage_index zaktualizowany.  
- [ ] Krytyczne/High naprawione lub z waiver + plan; retesty zaplanowane/wykonane; status/metadane aktualne.  
- [ ] Checklisty DoR/DoD odhaczone.

