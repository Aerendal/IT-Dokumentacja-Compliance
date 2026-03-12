---
title: Post-mortem incydentu HD
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Post-mortem incydentu HD


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Przeanalizować incydent w Help Desk/Service Desk, znaleźć przyczyny i usprawnić procesy/ narzędzia wsparcia.



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
- Zasoby DC dostępne; łączność stabilna.  
- Dostęp do licencji vendorów.  
- Zespół ma kompetencje w NFV/SDN.
## Otwarte pytania
- Jak obsłużyć compliance (np. 3GPP/ETSI) w audytach?  
- Jakie są limity licencyjne i CAPEX/OPEX na skalowanie?  
- Czy wymagane są profile k8s dla CNF (CPU pinning/hugepages)?  
- Jak testować SFC/latencję end-to-end?
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

1. Podsumowanie: czas, wpływ (SLA/CSAT/volumen zgłoszeń), kanały dotknięte.
2. Timeline: zdarzenia, alerty, eskalacje, komunikacja.
3. Root cause: ludzie/procesy/narzędzia; czynniki współwystępujące.
4. CAPA: działania naprawcze/prewencyjne, właściciele, terminy, status.
5. Usprawnienia: zmiany w routing/KB/automatyzacji/szkoleniach/monitoringu.
6. Follow-up: retest, QA odpowiedzi, aktualizacja runbooków, informacja do agentów/klientów.


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

- [ ] Timeline fact-based; root cause uzgodnione.
- [ ] CAPA z właścicielami/terminami wpisane.
- [ ] Usprawnienia procesów/narzędzi/szkoleń określone.
- [ ] Follow-up i komunikacja do zespołu/klientów wykonane.

## Definicje robocze
- NFVI: infrastruktura uruchamiająca funkcje sieciowe.  
- MANO: orkiestracja i zarządzanie VNF/CNF.  
- SR-IOV/DPDK: techniki przyspieszania I/O sieciowego.
## Przykłady użycia
- Wdrożenie core 5G jako CNF na klastrze Kubernetes + SDN.  
- Wirtualizacja firewall/load balancer z akceleracją DPDK.  
- Skalowanie VNF EPC na nowe regiony z MANO.
## Ryzyka i ograniczenia
- Brak akceleracji → niespełnienie SLA latency.  
- Złożoność MANO/SDN → ryzyko błędów.  
- Brak testów HA → dłuższe outage.  
- Licencje vendorów ograniczające skalowanie.
## Decyzje i uzasadnienia
- Wybór platformy NFVI/SDN i MANO.  
- Które VNF/CNF akcelerować i jak.  
- Model segmentacji i bezpieczeństwa.  
- Parametry scale-out i alarmów.
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
- Raport metryk, demo, feedback, logi, ADR, action plan, waiver log (jeśli wyjątki), lessons repository.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości
- Czas od końca POC do decyzji, % kryteriów osiągniętych, liczba action items otwartych/zamkniętych, czas do rollout/iteracji (jeśli Go), jakość lessons (feedback).
## Kryteria ukończenia
- [ ] Post-mortem POC kompletne; decyzja i plan zapisane; wersja/data/właściciel aktualne.
