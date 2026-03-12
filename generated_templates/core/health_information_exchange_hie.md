---
title: Health Information Exchange (HIE)
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Health Information Exchange (HIE)


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Określić wymagania i architekturę wymiany informacji zdrowotnej (HIE) pomiędzy podmiotami medycznymi, z zachowaniem interoperacyjności, bezpieczeństwa i zgodności regulacyjnej.


## Zakres i granice

- Obejmuje: standardy i formaty (HL7 v2/FHIR/CDA), identyfikację pacjenta (MPI/PI), consent management, profile IHE, transport (REST/Direct), bezpieczeństwo (TLS/mTLS/OAuth2, audyt), zgodność (HIPAA/RODO, krajowe), rejestrowanie dostępu, walidację danych, jakość i kompletność, monitoring i SLA.
- Poza zakresem: aplikacje kliniczne UI (opisane w oddzielnych dokumentach), analityka wtórna.


## Użytkownicy i interesariusze

- [Rola] — [potrzeby/odpowiedzialności]
- [Rola] — [potrzeby/odpowiedzialności]


## Wejścia i wyjścia

- Wejścia: wymagania kliniczne/operacyjne, przepisy lokalne, obecne systemy (EHR/EMR/LIS/RIS/PACS), identyfikatory pacjentów, polityki zgód, rejestry usług, profile IHE.
- Wyjścia: architektura HIE, model danych/transformacji, polityki consent/audyt, integracje systemów źródłowych, plan testów interoperacyjności, SLA/OLA, runbook operacyjny.


## Założenia

- [Założenie 1]
- [Założenie 2]


## Otwarte pytania

- [Pytanie 1]
- [Pytanie 2]


## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: katalog systemów medycznych, polityki zgód i prywatności, rejestr identyfikatorów, integracje istniejące, profile IHE, wymagania krajowe; brak – odnotuj.


## Fazy cyklu życia

- Discovery: wymagania kliniczne/regulacyjne, inwentaryzacja systemów.
- Design: model danych, identyfikacja, transport, bezpieczeństwo, consent, audyt.
- Implementacja: integracje, transformacje, rejestry, audyt.
- Testy: interoperacyjność (IHE), bezpieczeństwo, wydajność, zgodność.
- Operacje: monitoring, inspekcje audytowe, update standardów, reagowanie na incydenty.



## Struktura sekcji (szkielet)

- Use-case i wymagania kliniczne.
- Standardy i profile (HL7/FHIR/IHE, krajowe).
- Identyfikacja pacjenta i MPI.
- Consent management i prywatność (RODO/HIPAA, rejestrowanie zgód/dostępu).
- Transport i bezpieczeństwo (REST/Direct, TLS/mTLS/OAuth2, audyt/logi).
- Transformacje i walidacja danych (mapowanie, kodowanie, słowniki, ICD/SNOMED/LOINC).
- Integracje z systemami źródłowymi (EHR/EMR/LIS/RIS/PACS).
- SLA/OLA i monitoring (dostępność, latency, błędy, kompletność).
- Testy interoperacyjności i zgodności (IHE Connectathon-style).
- Ryzyka i mitigacje.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **HL7 FHIR** — Standard Wymiany Danych w Ochronie Zdrowia
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)

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

- Zbierz wymagania i przepisy; dobierz standardy/profile; zaprojektuj identyfikację, consent, bezpieczeństwo i transport; zaplanuj testy interoperacyjności; wdrażaj i monitoruj.


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

- [Termin 1]
- [Termin 2]
- [Termin 3]


## Przykłady użycia

- [Przykład 1]
- [Przykład 2]


## Ryzyka i ograniczenia

- [Ryzyko 1]
- [Ryzyko 2]


## Decyzje i uzasadnienia

- [Decyzja 1]
- [Decyzja 2]


## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód]
- [Dokument Z → Sekcja W] — [powód]


## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1]
- [Standard 2]


## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ]
- [Sekcja C] -> [Sekcja D] : [typ]


## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ]
- [Dokument C] -> [Dokument D] : [typ]


## Ścieżki informacji

- [Wejście] → [Źródło] → [Rozwinięcie] → [Wyjście]
- [Wejście] → [Źródło] → [Streszczenie] → [Wyjście]


## Weryfikacja spójności

- [ ] Ścieżki informacji zamknięte
- [ ] Brak sprzecznych relacji
- [ ] Sekcje krytyczne mają źródła


## Lista kontrolna spójności relacji

- [ ] Relacje mają sekcje źródłowe
- [ ] Relacje nie są sprzeczne
- [ ] Cross-doc uzasadnione
- [ ] Rozwinięcia/streszczenia odnotowane


## Artefakty powiązane

- [Artefakt 1]
- [Artefakt 2]


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]


## Ścieżka akceptacji

1. Autor przygotowuje wersję roboczą i przeprowadza samorecenzję.
2. Recenzent techniczny (Tech Lead / BA) weryfikuje merytorycznie.
3. Właściciel procesu zatwierdza treść i zakres.
4. PM / Scrum Master aktualizuje metadata (wersja, data, status).
5. Dokument trafia do repozytorium i jest linkowany w Szybkie powiązania.

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

Consent → dostęp/udostępnianie; identyfikacja pacjenta → matching i bezpieczeństwo; standardy → transformacje; SLA → monitoring.


## Wymagane rozwinięcia

- Consent/privacy → polityki prawne lokalne; wzory zgód.
- Transformacje → mapping pól i słowników kodów.
- Monitoring → dashboardy KPI/SLA.


## Wymagane streszczenia

- Tabela standardów/profile + decyzje architektoniczne; mapa systemów i integracji.


## Guidance

Cel: bezpieczna, interoperacyjna wymiana danych medycznych. DoR: use-case, przepisy, systemy zidentyfikowane; polityki zgód znane. DoD: model danych/transportu/bezpieczeństwa/consent/SLA opisane; testy zaplanowane; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Use-case i regulacje; [ ] Systemy źródłowe i identyfikacja; [ ] Polityki zgód i bezpieczeństwa.
- DoD: [ ] Architektura/model danych/bezpieczeństwo/consent opisane; [ ] Testy interoperacyjności i monitoring zaplanowane; [ ] Sekcje N/A uzasadnione; metadane aktualne.

