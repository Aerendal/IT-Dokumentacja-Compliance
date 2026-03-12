---
title: Public Records Requirements
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Public Records Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Określić wymagania dotyczące dokumentów i danych podlegających udostępnieniu jako public records (ustawy FOIA/UDIP/GD), zapewniając zgodność, właściwe przechowywanie, anonimizację i ścieżki dostępu.


## Zakres i granice

- Obejmuje: identyfikację kategorii public records, klasyfikację danych, zasady retencji/usuwania, procedury udostępniania (request handling), anonimizację/redaction, wyjątki (np. dane wrażliwe), formaty udostępniania, audyt/logi, role i odpowiedzialności, SLA na odpowiedź, opłaty (jeśli dopuszczone).  
- Poza zakresem: polityka wewnętrzna dokumentów poufnych (osobny dokument), marketing/PR.


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: przepisy lokalne/narodowe, rejestr dokumentów, klasyfikacja danych, polityka retencji, narzędzia DMS, zgłoszenia publiczne, wzory odpowiedzi.  
- Wyjścia: katalog public records i wyjątków, procedura obsługi wniosków, checklisty DoR/DoD, szablony odpowiedzi, plan anonimizacji, matryca ról, raporty SLA/audyt.


## Założenia

- DMS i ticketing działają.  
- Prawne wymagania zebrane.  
- Zespół ma narzędzia redaction.


## Otwarte pytania

- Jak długo przechowywać logi i odpowiedzi?  
- Jak obsłużyć wnioski wielojęzyczne?  
- Czy udostępniać API do danych publicznych?

## Powiązania (meta)

- Key Documents: data_protection_compliance, document_management_system, regulatory_document_management, security_controls_reference, logging_and_audit_trail.  
- Key Document Structures: kategorie, retencja, wnioski, anonimizacja, audyt.  
- Document Dependencies: DMS/ECM, ticketing/requests, redaction tools, IAM, legal registry.


## Zależności dokumentu

Wymaga: listy dokumentów i klasyfikacji, wymogów prawnych (FOIA/UDIP), polityk retencji, narzędzi do redakcji/anonimizacji, kanałów wniosków i SLA. Brak = brak DoR.


## Fazy cyklu życia

- Identyfikacja i klasyfikacja public records.  
- Ustanowienie procedur wniosków i anonimizacji.  
- Operacje i audyt.  
- Przeglądy i aktualizacje zgodności.



## Struktura sekcji (szkielet)
- Cel i zakres polityki
- Zakres obowiązywania i wyjątki
- Role i odpowiedzialności
- Wymagania/kontrole (techniczne/procesowe)
- Proces zarządzania zmianą i wyjątkami
- Dowody/audyt, metryki zgodności
- Komunikacja/szkolenia i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (public/records/requirements)  
- document_management_system, data_protection_compliance


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

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

1. Utwórz katalog public records i wyłączeń.  
2. Ustal procedurę wniosków, SLA i szablony.  
3. Wdroż narzędzia redaction i logowanie.  
4. Raportuj SLA/audyt; aktualizuj dokument i linkage_index.


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

- FOIA/UDIP: prawo do informacji publicznej.  
- Redaction: usunięcie/ukrycie fragmentów danych.  
- SLA: czas na odpowiedź/realizację wniosku.


## Przykłady użycia

- Udostępnienie raportu finansowego organowi publicznemu.  
- Odpowiedź na wniosek obywatela o dane projektów.  
- Publikacja zestawu danych po anonimizacji.


## Ryzyka i ograniczenia

- Ujawnienie danych osobowych → ryzyko prawne.  
- Opóźnienia SLA → kary lub utrata zaufania.  
- Nieaktualny rejestr → chaos w audycie.  
- Brak spójnych szablonów → niespójne odpowiedzi.


## Decyzje i uzasadnienia

- Zakres public records i wyłączeń.  
- Format udostępniania (PDF/CSV/API).  
- SLA i opłaty (jeśli dozwolone).  
- Retencja logów i dokumentów.


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

- Katalog ↔ Retencja ↔ Udostępnianie.  
- Anonimizacja ↔ Wyjątki ↔ Audyt.  
- SLA ↔ Ticketing ↔ Raporty.


## Struktura sekcji

1) Zakres prawny i kategorie public records  
2) Retencja/usuwanie i klasyfikacja  
3) Procedura wniosków (SLA, kanały, opłaty)  
4) Anonimizacja/redaction i wyjątki  
5) Format udostępniania i dostęp  
6) Audyt/logi i raportowanie  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Rejestr public records i wyłączeń.  
- Szablony odpowiedzi (grant/deny/partial) i checklisty.  
- Procedura anonimizacji/redaction (narzędzia, kroki).  
- Matryca ról i odpowiedzialności.  
- SLA na odpowiedź i raporty.  
- Plan przeglądów prawnych.


## Wymagane streszczenia

- Executive summary: obowiązki, główne kategorie i SLA.  
- Skrót wyjątków prawnych.


## Guidance (skrót)

- Zawsze klasyfikuj dane; wątpliwe traktuj jako wrażliwe.  
- Stosuj redaction/anonimizację przed publikacją; loguj.  
- Utrzymuj rejestr wniosków i SLA; audytuj.  
- Zgodność z RODO/PII: usuń/ukryj dane osobowe jeśli nie wymagane.  
- Aktualizuj linkage_index po zmianach procedur.


## Checklisty Definition of Ready (DoR)

- [ ] Wymogi prawne i kategorie zebrane.  
- [ ] Polityka retencji i klasyfikacja dostępne.  
- [ ] Narzędzia redaction/anonimizacji gotowe.  
- [ ] Kanały wniosków i ticketing skonfigurowane.  
- [ ] Role/odpowiedzialności przypisane.


## Checklisty Definition of Done (DoD)

- [ ] Procedura działa; wnioski obsługiwane w SLA.  
- [ ] Anonimizacja/redaction stosowana; logi kompletne.  
- [ ] Rejestr public records aktualny; linkage_index zaktualizowany.  
- [ ] Raporty/audyt przeprowadzone; brak krytycznych niezgodności.  
- [ ] Szablony/wyjątki zaktualizowane po przeglądzie.

