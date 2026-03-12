---
title: Exploratory Data Analysis Report
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Exploratory Data Analysis (EDA) Report


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Podsumować wnioski z wstępnej analizy danych: jakość, rozkłady, korelacje, potencjalne cechy i ryzyka.



## Zakres i granice
- Obejmuje: zakres okresu/obiektu raportowania, metryki/KPI, źródła danych, obserwacje, ryzyka, rekomendacje, akcje follow-up.
- Poza zakresem: zmiana procesu/systemu poza rekomendacjami; implementacja poprawek.
## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: definicje metryk, źródła danych, okres raportowania, limity/targety, wcześniejsze raporty.
- Wyjścia: sekcja wyników z wizualizacjami, wnioski, rekomendacje i przypisane zadania.
## Założenia
- Dostępne narzędzia DQ i katalog danych.  
- Dostęp do systemów źródłowych/wyciągów.  
- Wspólne definicje KPI/metryk obowiązują.
## Otwarte pytania
- Czy potrzebne są dodatkowe źródła zewnętrzne?  
- Czy istnieją ograniczenia prawne (jurysdykcje) dla wybranych danych?  
- Jakie są limity kosztów pozyskania/przetwarzania?
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
- Zbieranie danych i walidacja.
- Analiza i interpretacja.
- Rekomendacje i plan działań.
- Follow-up i przegląd wyników.
## Struktura sekcji (szkielet)

1. Dane źródłowe: opis tabel/kolumn, zakres czasowy, liczność, sampling.
2. Jakość danych: brakujące, duplikaty, outliers, spójność typów, data drift.
3. Rozkłady i statystyki opisowe (top kolumny, korelacje).
4. Wizualizacje kluczowe (hist/box/scatter/heatmap).
5. Potencjalne feature/hipotezy; ryzyka (leakage, bias).
6. Rekomendacje: czyszczenie, transformacje, kolejne kroki.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)

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

- [ ] Opis źródeł i jakości danych spisany.
- [ ] Rozkłady/wykresy i korelacje przedstawione.
- [ ] Ryzyka (leakage/bias/drift) zidentyfikowane.
- [ ] Rekomendacje i next steps zapisane.

## Definicje robocze
- Świeżość: maks. opóźnienie dostarczenia danych vs SLA.  
- Kompletność: odsetek brakujących wierszy/pól.  
- Dokładność: zgodność z systemem źródłowym lub ground truth.
## Przykłady użycia
- Specyfikacja danych do analizy churn.  
- Wymagania danych do budowy modelu rekomendacji.  
- Dane do audytu kosztów i marży per segment.
## Ryzyka i ograniczenia
- Bias w danych (niedoreprezentowane segmenty).  
- Braki PII/zgód mogą zablokować użycie danych.  
- Niska jakość danych wydłuża czas analizy lub fałszuje wyniki.
## Decyzje i uzasadnienia
- Zakres czasowy/segmenty vs koszt i czas pozyskania.  
- Poziom agregacji vs granularność wymagana przez KPI.  
- Tolerancje DQ vs harmonogram analizy.
## Powiązania z innymi dokumentami
- data_contract_standard — wymagania kontraktowe.  
- privacy_and_pii_handling — reguły PII.  
- data_quality_playbook — testy i progi DQ.
## Powiązania z sekcjami innych dokumentów
- Access Control/SoD → polityki dostępu; Retention → polityki retencji; DQ → metryki; TPRM → dostawcy danych; Security/Privacy → kontrole.
## Słownik pojęć w dokumencie
- Data Owner/Steward/Custodian, SoD, Lineage, DQ, DLP, SLO, KPI/KRI, Waiver, Sunset.
## Wymagane odwołania do standardów
- RODO/PII i wewnętrzne polityki danych.  
- Standardy jakości danych i katalogowania obowiązujące w organizacji.
## Mapa relacji sekcja→sekcja
- Klasyfikacja/role → Polityki → Metryki/SLO → Procesy → Narzędzia → Audyt → Waivery.
## Mapa relacji dokument→dokument
- Data Governance Requirements ↔ data_strategy/data_classification/privacy/security/retention/tprm/access_control_sod/lineage_standards.
## Ścieżki informacji
- Strategia/klasyfikacja → Polityki → Metryki → Procesy → Narzędzia → Raporty/Audyt → Przeglądy → Aktualizacje.
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
- RACI, matryca klasyfikacji, polityki (access/privacy/retention/sharing), definicje metryk/SLO, procesy i checklisty, katalog/lineage/DQ/DLP wymagania, TPRM rejestr, dashboard KPI/KRI, waiver log, ADR log.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości
- Coverage klasyfikacji, % systemów w katalogu/lineage, SLO jakości spełnione, czas zamykania incydentów danych, liczba waiverów i ich sunset, status audytów.
## Kryteria ukończenia
- [ ] Wymagania governance opisane i powiązane z metrykami/procesami/narzędziami; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.
