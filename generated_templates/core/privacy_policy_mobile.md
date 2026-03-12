---
title: Privacy Policy Mobile
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Privacy Policy Mobile


## Metadane

- Właściciel: Mobile Developer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Przygotować politykę prywatności dla aplikacji mobilnej zgodną z wymogami sklepów i regulacjami.



## Zakres i granice
- Obejmuje: zakres procesu, role/RACI, kroki, checklisty, standardy/normy, wyjątki i eskalacje.
- Poza zakresem: decyzje strategiczne lub tematy niezwiązane z procesem.
## Użytkownicy i interesariusze
- **Mobile Developer (iOS/Android)** — projektuje i implementuje funkcje aplikacji mobilnej
- **UX/UI Designer** — dostarcza projekty interfejsu dopasowane do platform
- **QA Engineer** — testuje na urządzeniach docelowych
- **Product Owner** — definiuje wymagania funkcjonalne aplikacji

## Wejścia i wyjścia
- Wejścia: polityki/standardy, narzędzia, dane wejściowe, role.
- Wyjścia: wykonany proces z dowodami, metryki jakości, decyzje/eskalacje.
## Założenia
- Backend booking/schedule dostępny.  
- Payment provider zgodny z PCI.  
- Zespół ma proces release mobilnych.
## Otwarte pytania
- Jak obsłużyć zwroty i zmiany rezerwacji w offline?  
- Jak długo przechowywać dane biletów i telemetry?  
- Jak wspierać multi-tenant/regionalne różnice treści?
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
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)

1. Zakres danych: jakie dane zbierane (konto, urządzenie, lokalizacja, usage), cel przetwarzania, legal basis.
2. Udostępnianie: komu i po co (partnerzy/analityka/reklama), linki do ich polityk.
3. Bezpieczeństwo i retencja: przechowywanie, szyfrowanie, retencja, prawa użytkownika (access/delete/opt-out).
4. Tracking/SDK: identyfikatory, reklama, analityka; ustawienia zgód/ATT (iOS), opt-out.
5. Dzieci/limity: COPPA/rodzice, wiek, ograniczenia.
6. Kontakt/zmiany: dane kontaktowe, zmiany polityki, ostatnia aktualizacja.


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **ISO/IEC 27018** — Ochrona Danych Osobowych w Chmurze (PII)
- **ISO/IEC 27701** — Zarządzanie Informacjami o Prywatności (PIMS)

### Polskie normy i regulacje
- **UODO-PL** — Ustawa o Ochronie Danych Osobowych (implementacja RODO)

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

- [ ] Jasno opisano dane/cel/udostępnianie i prawa użytkownika.
- [ ] Retencja/bezpieczeństwo i procedura zgód/opt-out podane; ATT (iOS) ujęte.
- [ ] Sekcja partnerów/SDK z linkami do polityk; ograniczenia dla dzieci uwzględnione.
- [ ] Kontakt i data ostatniej aktualizacji dodane.

## Definicje robocze
- Boarding pass: elektroniczny dokument wejścia na pokład.  
- Staged rollout: stopniowe udostępnianie wersji użytkownikom.  
- Offline-first: kluczowe dane dostępne bez połączenia.
## Przykłady użycia
- Aplikacja linii lotniczej z boarding pass i status flight.  
- Aplikacja kolejowa z biletami i mapą stacji offline.  
- Aplikacja komunikacji miejskiej z opóźnieniami i płatnościami.
## Ryzyka i ograniczenia
- Brak offline → utrata dostępu do biletów.  
- Opóźnione notyfikacje → frustracja użytkowników.  
- Błędy płatności → utrata przychodu.  
- Luka bezpieczeństwa → wycieki PII/płatności.
## Decyzje i uzasadnienia
- Model offline/cache i TTL.  
- Metody płatności i provider.  
- Priorytety notyfikacji i częstotliwość.  
- Strategie rollout i monitoring KPI.
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
