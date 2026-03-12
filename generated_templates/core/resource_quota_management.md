---
title: Resource Quota Management
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Resource Quota Management


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zdefiniować zasady przydziału i egzekwowania kwot zasobów (CPU/mem/storage/network/API) dla zespołów/usług, by zapobiegać nadużyciom i zapewnić przewidywalność.


## Zakres i granice

- Obejmuje: polityki limitów/requests (k8s), storage quotas, rate limiting API, priorytety/tiers, proces request/approval, monitoring i raportowanie zużycia, automatyczne egzekwowanie i alerty, FinOps/showback.
- Poza zakresem: szczegółowe konfiguracje billingowe (osobne dokumenty), projekt architektury usług.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: cele biznesowe, backlog/zakres, dostępne zasoby i budżet, zależności, ograniczenia kalendarzowe/regulacyjne.
- Wyjścia: plan fal/sprintów, milestones z datami, RACI, ryzyka z planem mitigacji, plan komunikacji i raportowania.
## Założenia
- Dane master produktów/rynków są aktualne.  
- DMS wspiera e‑signature i audyt zgodny z regulacjami.  
- Zespół compliance nadzoruje proces.
## Otwarte pytania
- Czy regulator wymaga dostępu on‑line czy tylko submission?  
- Jak długo przechowywać wersje robocze?  
- Jak obsłużyć lokalne wymagania (język, format) dla wielu rynków?  
- Jak audytować komunikację e‑mail/portale regulatorów?
## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Przygotowanie: cele, zakres, założenia.
- Planowanie: sekwencja prac, zasoby, daty.
- Realizacja: monitoring postępu, decyzje go/stop.
- Zamknięcie: retrospektywa, aktualizacja planów.
## Struktura sekcji (szkielet)

- Zakres i podział na tiers/namespace’y
- Polityki limitów/requests i storage/network/API
- Proces wnioskowania/approval/recertyfikacji
- Monitoring i alerty zużycia
- Raportowanie kosztów/showback
- Eskalacje i wyjątki
- Utrzymanie i przeglądy


## Szybkie powiązania

- Capacity Planning, FinOps, SLO/SLA, Security (abuse), Change Management, Incident Response (quota breach).


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

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
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.
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
- Submission: zgłoszenie/dossier do regulatora.  
- Variation: zmiana zatwierdzonego dossier.  
- PSUR/CSR/DSUR: przykłady raportów okresowych w farmacji.
## Przykłady użycia
- Zarządzanie dossier medycznym na wielu rynkach UE/US.  
- Obsługa variation po zmianie produkcji.  
- Przygotowanie raportów okresowych bezpieczeństwa.
## Ryzyka i ograniczenia
- Brak legal hold → ryzyko prawne.  
- Niespójne metadane → trudne audyty i wyszukiwanie.  
- Niepełny audyt → niezgodność regulacyjna.  
- Brak kalendarza → spóźnione raporty.
## Decyzje i uzasadnienia
- Wybór taksonomii i narzędzi DMS/ECM.  
- Poziom dostępu regulatora (viewer?).  
- Zakres audytu i retencji.  
- Automatyzacja alertów i integracji.
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

## Wejścia

- Inwentarz usług/namespace’ów, profile obciążenia, SLO, budżety kosztowe, ryzyka współdzielenia, dane zużycia historycznego.


## Wyjścia

- Polityka kwot, tabela limitów/tiers, proces przydziału/zmian, dashboard zużycia, alerty i raporty showback.



## Jak używać (checklista)

- Określ tiers i wartości domyślne; przypisz do zespołów/usług.
- Skonfiguruj limity/requests w k8s/API/storage; ustaw alerty.
- Ustal proces wniosków i recertyfikacji; raportuj zużycie i koszty.
- Monitoruj wyjątki i incydenty; dostosuj limity przy zmianach SLO.


## Wymagane rozwinięcia / powiązania

- Tabela limitów per tier, szablon wniosku, dashboard zużycia, procedura wyjątków.


## Kryteria DoR

- Dane zużycia historycznego, inwentarz usług, budżety/tier’y zatwierdzone.


## Kryteria DoD

- Polityka i limity wdrożone; monitoring i raporty działają; proces wniosków aktywny.


## Artefakty

- Polityka kwot, konfiguracje k8s/API/storage, dashboardy, raporty showback, rejestr wniosków.


## Walidacja

- Testy limitów (synthetic), weryfikacja alertów, przegląd raportów vs billing.


## Metryki

- % usług z poprawnie ustawionymi limitami, liczba przekroczeń/alertów, czas decyzji dla wniosku, koszt per tier.


## Utrzymanie

- Przegląd kwartalny limitów/tiers, korekta po zmianach obciążenia/budżetu; audyt wniosków/wyjątków.


## Zakończenie

Zarządzanie kwotami stabilizuje środowisko i koszty; utrzymuj politykę wraz z monitoringiem i procesem wniosków.
