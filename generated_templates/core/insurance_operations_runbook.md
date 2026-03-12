---
title: Insurance Operations Runbook
status: needs_content
aligned: true
aligned_rev: 3
aligned_at: 2026-02-09
aligned_by: codex
---

# Insurance Operations Runbook

## Metadane
- Właściciel: DevOps Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Insurance Operations Runbook daje operacyjny, krok-po-kroku opis działań z jasnymi warunkami start/stop i eskalacją.


## Zakres i granice
- Obejmuje: warunki wejścia, przygotowanie, kroki operacyjne, walidację wyników, rollback, monitoring, eskalacje/komunikację.
- Poza zakresem: decyzje produktowe/architektoniczne; długofalowa strategia.



## Wejścia i wyjścia
- Wejścia: definicja triggera/scenariusza, wymagane uprawnienia/narzędzia, dane wejściowe, RACI i kontakty.
- Wyjścia: wykonane kroki z timestamp, dowody/artefakty, status (sukces/niepowodzenie), decyzje i eskalacje.



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



## Powiązania sekcja↔sekcja
- Trigger → Kroki przygotowawcze → Wykonanie → Walidacja → Komunikacja/Eskalacja.
- Runbook ↔ Monitoring/Alerting ↔ Incident/Problem mgmt.



## Fazy cyklu życia
- Przygotowanie runbooka: wersja, właściciel, testowane ścieżki.
- Egzekucja: krokowo z dowodami.
- Postmortem: usprawnienia runbooka i monitoringu.




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
## Struktura sekcji (szkielet)
- Cel, zakres i definicje sukcesu
- Trigger/scenariusze i preconditions
- Role, uprawnienia i narzędzia
- Kroki operacyjne (checklista) z walidacją
- Monitoring i dowody wykonania
- Rollback/contingency oraz komunikacja/escalacja
- Rejestr zmian runbooka



## Wymagane rozwinięcia
- Checklisty z komendami/API, ścieżki alternatywne, limity czasowe.



## Wymagane streszczenia
- Krótka karta operacyjna: kiedy użyć, główne kroki, numery kontaktowe.



## Guidance
DoR: zweryfikowany trigger, dostępne uprawnienia/narzędzia, owner on-call.
DoD: kroki przetestowane, rollback opisany, dowody i komunikacja zdefiniowane, metadane aktualne.



## Szybkie powiązania
- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies

## Mające zastosowanie standardy i normy

### Polskie normy i regulacje
- **KNF-REKOM-IT** — Rekomendacje KNF dot. systemów IT w sektorze finansowym
- **SOLVENCY2-PL** — Solvency II — Wymogi IT dla Ubezpieczycieli (implementacja PL)

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty jakości
- [ ] Czy cel dokumentu jest jednoznaczny?
- [ ] Czy zakres i granice są jasno określone?
- [ ] Czy wszystkie zależności są opisane?
- [ ] Czy wskazano wymagane rozwinięcia i streszczenia?
- [ ] Czy powiązania sekcja↔sekcja są spójne?

## Definicje robocze
- Downtime clinical — praca offline; kroki powrotu i walidacja kliniczna.
- RTO/RPO — czas przywrócenia / utrata danych akceptowalna.
## Przykłady użycia
- Awaria EHR: przełączenie na tryb downtime, komunikaty do kliniki, powrót i rekonsyliacja.
- Patch krytyczny: CAB, okno serwisowe, test po wdrożeniu, walidacja kliniczna.
## Ryzyka i ograniczenia
- Naruszenie HIPAA/RODO (logi, dostęp, dane w komunikatach).
- Brak walidacji klinicznej po incydencie/patchu → ryzyko kliniczne.
## Decyzje i uzasadnienia
- Kadencja raportów (tydzień/kwartał).  
- Kryteria go/no-go i required evidence.  
- Standard kanałów komunikacji (statuspage, e-mail, in-app).
## Założenia
- Dostępne są runbooki vendorów i aktualne listy kontaktów.
- Monitoring i backup są wdrożone w środowisku docelowym.
## Otwarte pytania
- Czy wszystkie integracje HL7/FHIR mają testy conformance?
- Jakie są lokalne wymagania prawne poza HIPAA/RODO?
## Powiązania z innymi dokumentami
- Incident Response Playbook (kliniczny/IT), Change Management, Backup & DR.
- IAM/Privileged Access Policy, Audit/Compliance plan.
## Powiązania z sekcjami innych dokumentów
- Privacy/Security → IAM/logi/szyfrowanie.
- HL7/FHIR Integration → Monitoring i testy interface’ów.
## Słownik pojęć w dokumencie
- EHR/EMR, PACS, LIS, RIS, HL7, FHIR, CAB, RTO/RPO.
## Wymagane odwołania do standardów
- HIPAA/RODO, lokalne przepisy zdrowotne, HL7/FHIR conformance, ISO 27799 (health infosec).
## Mapa relacji sekcja→sekcja
- Inwentarz → Monitoring/Backup/DR → Incydenty/Downtime → Audyt.
## Mapa relacji dokument→dokument
- Healthcare IT Ops Runbook → Incident Response → Change Mgmt → Audit/Compliance.
## Ścieżki informacji
- Alert/Incydent → Triage/Eskalacja → Komunikacja → Mitigacja → Walidacja kliniczna → Postmortem.
- Zmiana/Patch → CAB → Wdrożenie → Walidacja → Dokumentacja/audyt.
## Weryfikacja spójności
- [ ] Czy wszystkie ścieżki informacji są zamknięte?
- [ ] Czy istnieją pętle lub sprzeczne relacje?
- [ ] Czy sekcje krytyczne mają wskazane źródła i rozwinięcia?

## Lista kontrolna spójności relacji
- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań (np. wzajemne wykluczanie)?
- [ ] Czy relacje cross‑doc mają uzasadnienie i są zgodne z fazą?
- [ ] Czy relacje wymagają rozwinięć lub streszczeń są odnotowane?

## Artefakty powiązane
- Dashboardy, harmonogramy patch/backup, szablony komunikatów, listy kontaktów, logi audytu.
## Ścieżka decyzji
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]

## Użytkownicy i interesariusze
- IT Ops/SRE, Security/Compliance, Klinicyści/SME, Vendorzy, Service Desk.
## Ścieżka akceptacji
- IT Ops → Security/Compliance → Klinika → CAB/Owner sign‑off.
## Kryteria ukończenia
- [ ] Harmonogramy, playbooki i kontakty kompletne.
- [ ] Dowody backup/DR/testów dostępne.
- [ ] Dokument powiązany w linkage_index.jsonl i checklistach.
## Metryki jakości
- Dostępność (SLA), liczba incydentów klinicznych, czas reakcji/naprawy, sukces testów DR, wskaźniki audytu (log completeness, access recertification), defekty po patchach.
## Monitoring i utrzymanie
- [Co monitorujemy] — [narzędzie / częstotliwość]
- [Kto utrzymuje] — [rola]

## Kontrola zmian
- [Zmiana] — [powód] — [data] — [akceptacja]

## Wymogi prawne i regulacyjne
- [Wymóg 1] — [źródło / akt prawny / standard]
- [Wymóg 2] — [źródło / akt prawny / standard]

## Zasady bezpieczeństwa informacji
- [Zasada 1] — [opis i wpływ na dokument]
- [Zasada 2] — [opis i wpływ na dokument]

## Ochrona danych i prywatność
- [Wymaganie 1] — [opis i sekcja docelowa]
- [Wymaganie 2] — [opis i sekcja docelowa]

## Wersjonowanie treści
- [Wersja] — [zmiana] — [autor] — [data]
- [Wersja] — [zmiana] — [autor] — [data]

## Historia zmian sekcji
- [Sekcja] — [zmiana] — [data]
- [Sekcja] — [zmiana] — [data]

## Wymagane aktualizacje
- [Sekcja] — [powód aktualizacji] — [termin]
- [Sekcja] — [powód aktualizacji] — [termin]

## Integracje i interfejsy
- [System / API] — [zakres integracji] — [wymagania]
- [System / API] — [zakres integracji] — [wymagania]

## Wymagania danych
- [Dane wejściowe] — [format] — [walidacja]
- [Dane wyjściowe] — [format] — [walidacja]

## Logowanie i audyt
- [Zdarzenie] — [poziom] — [retencja]
- [Zdarzenie] — [poziom] — [retencja]

## Utrzymanie i operacje
- [Procedura] — [cel] — [częstotliwość]
- [Procedura] — [cel] — [częstotliwość]

## KPI i SLA
- [KPI] — [cel] — [pomiar]
- [SLA] — [cel] — [pomiar]

## Scenariusze awaryjne
- [Scenariusz] — [objawy] — [reakcja]
- [Scenariusz] — [objawy] — [reakcja]

## Wpływ na inne systemy
- [System] — [rodzaj wpływu] — [ryzyko]
- [System] — [rodzaj wpływu] — [ryzyko]

## Zależności danych między systemami
- [Źródło danych] → [Odbiorca] — [opis]
- [Źródło danych] → [Odbiorca] — [opis]

## Harmonogram przeglądów
- [Obszar] — [częstotliwość] — [właściciel]
- [Obszar] — [częstotliwość] — [właściciel]

## Wymagania wydajnościowe
- [Wymaganie] — [metryka] — [próg]
- [Wymaganie] — [metryka] — [próg]

## Wymagania dostępnościowe
- [Wymaganie] — [SLA] — [metoda pomiaru]
- [Wymaganie] — [SLA] — [metoda pomiaru]

## Wymagania skalowalności
- [Wymaganie] — [cel] — [warunki]
- [Wymaganie] — [cel] — [warunki]

## Wymagania dostępności danych
- [Dane] — [częstotliwość dostępu] — [SLA]
- [Dane] — [częstotliwość dostępu] — [SLA]

## Retencja i archiwizacja
- [Dane] — [retencja] — [archiwizacja]
- [Dane] — [retencja] — [archiwizacja]

## Dostępność w sytuacjach awaryjnych
- [Scenariusz] — [zachowanie] — [priorytet]
- [Scenariusz] — [zachowanie] — [priorytet]

## Testy i weryfikacja
- [Test] — [cel] — [wynik oczekiwany]
- [Test] — [cel] — [wynik oczekiwany]

## Walidacja zgodności
- [Wymóg] — [metoda weryfikacji]
- [Wymóg] — [metoda weryfikacji]

## Audyty i przeglądy
- [Audyty] — [częstotliwość] — [odpowiedzialny]
- [Audyty] — [częstotliwość] — [odpowiedzialny]