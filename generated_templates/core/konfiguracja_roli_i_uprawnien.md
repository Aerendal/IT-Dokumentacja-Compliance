---
title: Konfiguracja ról i uprawnień
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Konfiguracja ról i uprawnień


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Zdefiniować i wdrożyć model ról/uprawnień dla systemu, zgodny z zasadą najmniejszych uprawnień i łatwy w audycie.


## Zakres i granice
- Obejmuje: cele i KPI, zakres prac, kamienie milowe, kryteria akceptacji, zasoby/budżet, ryzyka i zależności, sposób raportowania.
- Poza zakresem: szczegółowe instrukcje implementacyjne; bieżące operacje poza objętym okresem.
## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: cele biznesowe, backlog/zakres, dostępne zasoby i budżet, zależności, ograniczenia kalendarzowe/regulacyjne.
- Wyjścia: plan fal/sprintów, milestones z datami, RACI, ryzyka z planem mitigacji, plan komunikacji i raportowania.
## Założenia
- IdP/IAM/CMDB/HRIS dostępne; zespoły Security/IAM mają zasoby; polityki AC/SoD obowiązują.
## Otwarte pytania
- Jakie systemy wymagają bardziej granularnych ról/atrybutów?  
- Jakie raporty audytu są wymagane przez regulatora/klientów?
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

1. Model: RBAC/ABAC, domeny uprawnień, separacja obowiązków, role bazowe vs. rozszerzenia.
2. Słownik ról: opis, zakres dostępu, typ użytkowników, ograniczenia środowiskowe.
3. Mapping: role → uprawnienia, grupy, polityki; dziedziczenie, wyjątki.
4. Procesy: nadawanie/zmiana/odbieranie, JIT/JEA, recertyfikacje, least privilege reviews.
5. Techniczne wdrożenie: katalog (AD/IAM), system docelowy, integracje SSO, logowanie dostępu.
6. Audyt i zgodność: logi, raporty, alerty zmian, testy uprawnień, ścieżki zgód.


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

## Standardy i compliance
### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

## RACI i role

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie dokumentu | DEV / BA | PM | BA / ARCH | OPS / SM |
| Przegląd i zatwierdzenie | PM / BA | PM | Tech Lead | OPS |
| Aktualizacja | DEV / BA | PM | BA | OPS |
| Archiwizacja | OPS | PM | BA | SM |

## Jak używać dokumentu

- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.



## Checklisty jakości

- [ ] Role opisane wraz z zakresem i ograniczeniami.
- [ ] Mapping ról do uprawnień/grup/polityk udokumentowany.
- [ ] Proces nadawania/odbierania i recertyfikacji zdefiniowany.
- [ ] Logi/audyt dostępów włączone; testy uprawnień wykonywane okresowo.

## Definicje robocze

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia
- Nadmiarowe uprawnienia, brak SoD, brak recerts/logów → ryzyko audytowe; brak waiver sunset → dług bezpieczeństwa.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- access_control_goals, access_control_matrix_design/reference, role_based_access_control_rbac_design, attribute_based_access_control_abac_design, access_control_patterns, access_control_testing, multi_factor_authentication_design, data_classification, security_controls_reference, risk_register.
## Powiązania z sekcjami innych dokumentów
- Data classification → SoD i uprawnienia; IAM/MFA → integracje; Risk Register → wpisy ryzyka; AC Testing → walidacja macierzy.
## Słownik pojęć w dokumencie
- RBAC, ABAC, SoD, JML, JIT, Recertyfikacja, Waiver, Sunset, IdP, IAM.
## Wymagane odwołania do standardów
- Polityki AC/IAM/SoD organizacji; wymogi audytowe/regulatora (SOX/ISO/PCI itp., jeśli dotyczy).
## Mapa relacji sekcja→sekcja
- Model/SoD → Macierz → JML/JIT → Recertyfikacje → Audyt/testy → Waivery.
## Mapa relacji dokument→dokument
- Konfiguracja ról i uprawnień ↔ AC goals/matrix/RBAC/ABAC/testing/MFA/risk_register.
## Ścieżki informacji
- SoD/klasyfikacja → Macierz → Provisioning → Recertyfikacje → Audyt/testy → Waivery → Aktualizacje.
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
- Macierz CSV/JSON, SoD rules, waiver log, workflow JML/JIT/recerts, raporty audytu/logów, testy AC, ADR log.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości
- % ról po recertyfikacji w terminie, liczba waiverów i czas sunset, pokrycie testów AC, liczba nadmiarowych uprawnień wykrytych, czas provision/deprovision.
## Kryteria ukończenia
- [ ] Macierz i procesy AC opisane; testy/audyt/waivery zdefiniowane; dokument w linkage_index; metadane aktualne.
