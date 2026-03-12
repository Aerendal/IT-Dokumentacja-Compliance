---
title: Data Masking Specification
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Data Masking Specification


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Określić zasady maskowania danych wrażliwych (PII/PHI/PCI) w środowiskach produkcyjnych i nieprodukcyjnych.



## Zakres i granice
- Obejmuje: persony/use cases, funkcje, wyjątki, reguły biznesowe, NFR (wydajność, dostępność, bezpieczeństwo, zgodność).
- Poza zakresem: szczegółowy projekt techniczny i implementacja.
## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: cele biznesowe, brief produktowy, regulacje, istniejące procesy/systemy, dane referencyjne.
- Wyjścia: uporządkowana lista wymagań z priorytetami, kryteriami akceptacji i powiązaniem z testami/architekturą.
## Założenia
- Dostępne są polityki i rejestry systemów; istnieje sponsor governance; narzędzia mogą być skonfigurowane.
## Otwarte pytania
- Jakie dodatkowe wymogi branżowe (np. finansowe/medyczne/energetyczne)?  
- Jakie SLA raportowania jakości i kto je odbiera (exec/ops/audit)?
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
- Elicytacja i warsztaty.
- Konsolidacja i priorytetyzacja.
- Walidacja z interesariuszami (biznes/arch/security/legal).
- Traceability do backlogu/testów.
## Struktura sekcji (szkielet)

1. Zakres danych do maskowania (pola, tabele, logi, kopie).
2. Poziomy maskowania (pełne, częściowe, tokenizacja, anonimizacja).
3. Techniki i narzędzia (on-the-fly, ETL, DB functions).
4. Środowiska i separacja (prod vs test/dev, refresh danych).
5. Weryfikacja i audyt (testy maskowania, logi, zgodność).
6. Role i odpowiedzialności.


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


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

- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.



## Checklisty jakości

- [ ] Lista pól/zasobów wrażliwych z maskowaniem.
- [ ] Technika maskowania per pole zdefiniowana.
- [ ] Proces eksportu do nie-proda z maskowaniem.
- [ ] Testy/audyt maskowania wykonywane.

## Definicje robocze

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia
- Brak klasyfikacji/rol → niespójne dostępy; brak metryk → brak kontroli jakości; brak SoD/access review → ryzyko nadużyć; brak audit trail → ryzyko compliance.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- data_strategy, data_classification, privacy_policy, security_baseline, access_control_sod, data_quality_policy, retention_policy, tprm_policy, lineage_standards.
## Powiązania z sekcjami innych dokumentów
- Access Control/SoD → polityki dostępu; Retention → polityki retencji; DQ → metryki; TPRM → dostawcy danych; Security/Privacy → kontrole.
## Słownik pojęć w dokumencie
- Data Owner/Steward/Custodian, SoD, Lineage, DQ, DLP, SLO, KPI/KRI, Waiver, Sunset.
## Wymagane odwołania do standardów
- GDPR/CCPA, PCI/HIPAA/branżowe jeśli dotyczy; firmowe polityki danych/bezpieczeństwa/audytu.
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
## Guidance

Cel: skrócone wskazówki do wypełniania szablonów dokumentów (core/satellite).

- Cel dokumentu: 2–3 zdania o decyzjach, ryzykach i wartości dokumentu.
- Zakres i granice: co obejmuje (systemy/procesy/zespoły) i czego nie obejmuje; zaznacz granice odpowiedzialności.
- Wejścia: dane, wymagania, standardy, zależności potrzebne przed startem.
- Wyjścia: artefakty/rezultaty, kto je konsumuje, format (link/plik).
- Zależności dokumentu: wymagane dokumenty lub decyzje; właściciel; wpływ na kolejność prac.
- Powiązania sekcja↔sekcja: które sekcje się rozwijają/streszczają; podaj uzasadnienie.
- Struktura sekcji: utrzymuj układ logiczny; sekcje bez treści oznacz jako N/A z krótkim uzasadnieniem.
- Fazy cyklu życia: zaznacz, w których fazach dokument powstaje/aktualizuje się/archiwizuje; kto odpowiada.
- DoR (Definition of Ready): zakres, wejścia, role, zależności, kryteria akceptacji gotowe.
- DoD (Definition of Done): sekcje uzupełnione lub N/A, powiązania wpisane, checklisty jakości sprawdzone, wersja/data/właściciel, linki/artefakty działają.
- Język: polski; nazwy własne pozostają bez zmian; liczby w nazwach plików usunięte już w szablonach.
- Filozofia: optymalizuj przez rozwój, nie ucinanie — dodawaj, nie kasuj; elementy „satelitarne” zostają.

oprawność.

