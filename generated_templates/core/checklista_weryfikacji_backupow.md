---
title: Checklista weryfikacji backupów
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Checklista weryfikacji backupów


## Metadane

- Właściciel: Document Owner
- Wersja: v0.3
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Lista kontrolna regularnej weryfikacji backupów, aby potwierdzić ich kompletność, odtwarzalność oraz zgodność z wymaganiami RPO/RTO i audytem.


## Zakres i granice

- Obejmuje: istnienie i świeżość backupów, testy restore (full/partial/PITR), integralność danych, zabezpieczenie kluczy, monitorowanie/alerty, dowody i action items.
- Poza zakresem: projekt architektury backup/DR (oddzielne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: harmonogram/plan backupów, cele RPO/RTO, lista systemów/danych krytycznych, procedury restore, klucze KMS/HSM, logi backup/monitoring.
- Wyjścia: wypełniona checklista, dowody z testów, lista braków/action items z owner/ETA, decyzja go/conditional/no‑go dla wzorca backupu.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: backup_and_recovery_design, backup_and_recovery_procedure, backup_and_recovery_testing, backup_and_recovery_reference, disaster_recovery_plan, business_continuity_plan.
- Key Document Structures: zakres, scenariusze testów, metryki RPO/RTO, dowody, action items.
- Document Dependencies: inwentarz systemów/danych, klucze KMS/HSM, plan retencji, runbook restore, monitoring/logi.


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
- Cel i zakres
- Definicje i role/RACI
- Standardy/zasady i narzędzia
- Kroki procesu / checklisty
- Kryteria jakości/DoD i wyjątki
- Komunikacja i eskalacje
- Rejestr zmian i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (backup/verification)
- backup_and_recovery_design, backup_and_recovery_procedure, backup_and_recovery_testing, disaster_recovery_plan, business_continuity_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO 22301** — System Zarządzania Ciągłością Działania (BCMS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Przygotuj plan backup/RPO/RTO, scenariusze i środowisko.  
2. Wykonaj testy restore, wypełnij checklistę i zapisz dowody.  
3. Utwórz action items/waivery, zaplanuj retest i follow‑up; zaktualizuj linkage_index.


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

- Zakres/RPO/RTO → Testy → Dowody → Action items/waivery → Retesty.


## Mapa relacji dokument→dokument

- Checklista weryfikacji backupów → Backup/DR/BCP → Audit/Compliance.


## Ścieżki informacji

- Plan backup → Testy → Dowody → Action items → Retesty → Audyt.


## Weryfikacja spójności

- [ ] RPO/RTO i retencja spójne z wynikami; dowody kompletne.  
- [ ] Action items/waivery mają właścicieli i daty; follow‑up zaplanowany; relacje cross‑doc opisane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Logi/raporty restore, checksums, screenshoty, ticket audytowy, lista action items, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Spełnienie RPO/RTO, czas odtwarzania, % testów z dowodami, liczba waiverów i czas ich zamknięcia, liczba krytycznych action items otwartych.

## Kryteria ukończenia

- [ ] Testy wykonane, dowody zapisane, RPO/RTO ocenione, braki/action items rozpisane.  
- [ ] Dokument w linkage_index; wersja/data/właściciel aktualne.


## Punkty kontroli

- [ ] Backupy istnieją dla wszystkich systemów/krytycznych danych; retencja/lokalizacje zgodne z planem.  
- [ ] Świeżość zgodna z harmonogramem; RPO spełnione.  
- [ ] Test restore wykonany (full/partial/PITR); scenariusz ransomware/tampering uwzględniony.  
- [ ] Integralność danych po restore (checksum, spójność aplikacyjna/DB).  
- [ ] Czas odtwarzania zmierzony i ≤ RTO; RPO potwierdzone.  
- [ ] Dokumentacja restore aktualna; ścieżka do kluczy KMS/HSM sprawdzona.  
- [ ] Dostępy do backupów/kluczy zabezpieczone (IAM/least privilege); audyt logów.  
- [ ] Monitorowanie/alerty backupu działają; brakujące alerty zapisane.  
- [ ] Dowody z testu zapisane (logi, checksumy, zrzuty, ticket); lokalizacja wskazana.  
- [ ] Braki/action items mają ownera i termin; follow‑up zaplanowany; waiver (jeśli RPO/RTO niespełnione) z sunset/kompensacją.


## Wymagane rozwinięcia

- Progi RPO/RTO per system, format dowodów, scenariusze testów i częstotliwość retestów.



## Wymagane streszczenia

- Podsumowanie: spełnienie RPO/RTO, główne braki, action items i terminy.


## Guidance (skrót)

- Testuj na izolowanym środowisku prod‑like; zawsze zapisuj dowody.  
- Brak dowodu = test niezaliczony; brak spełnienia RPO/RTO → waiver z sunset.  
- Utrzymuj listę action items i follow‑up po każdym teście.


## Checklisty Definition of Ready (DoR)

- [ ] Plan backup/retencji i cele RPO/RTO dostępne; lista systemów/danych krytycznych gotowa.  
- [ ] Procedury restore i scenariusze testowe opisane; klucze KMS/HSM dostępne.  
- [ ] Miejsce na dowody i ticket audytowy ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Checklist wypełniona; RPO/RTO zmierzone; integralność potwierdzona.  
- [ ] Dowody zapisane i podlinkowane; action items/waivery z owner/ETA; follow‑up ustawiony.  
- [ ] Dokument w linkage_index/checklistach; metadane aktualne.

