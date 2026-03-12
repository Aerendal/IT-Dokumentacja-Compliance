---
title: Record of Processing Activities (RoPA)
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-03-09
aligned_by: codex
---

# Record of Processing Activities (RoPA)

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Prowadzić Rejestr Czynności Przetwarzania danych osobowych wymagany przez Art. 30 RODO/GDPR. Każdy wpis opisuje: cel przetwarzania, kategorie danych osobowych, kategorie osób, odbiorców danych, przekazania do krajów trzecich, terminy usunięcia danych oraz techniczne i organizacyjne środki bezpieczeństwa. Rejestr jest obowiązkowym dokumentem audytowym okazywanym organowi nadzorczemu na żądanie.

## Zakres i granice
- Obejmuje: wszystkie operacje przetwarzania danych osobowych w organizacji (Art. 30 ust. 1 RODO dla administratorów, Art. 30 ust. 2 dla podmiotów przetwarzających), dane kontaktowe administratora i DPO, podstawy prawne przetwarzania, opis kategorii danych i podmiotów, kraje trzecie i gwarancje, planowane terminy usunięcia, opis środków bezpieczeństwa.
- Poza zakresem: treść Polityki Prywatności (oddzielny dok.), formularze zgody, DPIA (oddzielny dok.).

## Wejścia i wyjścia
- Wejścia: inwentaryzacja systemów i procesów przetwarzania danych, dane kontaktowe administratora/DPO, umowy z podmiotami przetwarzającymi (DPA), polityki retencji, oceny ryzyka bezpieczeństwa.
- Wyjścia: kompletny rejestr czynności przetwarzania (format tabela lub Excel/DB), gotowy do okazania UODO/organowi nadzorczemu, podstawa do DPIA, audytów i ocen zgodności.

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- Data Protection Impact Assessment (DPIA) — wpisy wysokiego ryzyka wymagają DPIA.
- Data Processing Agreement (DPA) — każdy podmiot przetwarzający musi mieć DPA.
- Privacy Policy / Notice — informacje przekazywane osobom na podstawie rejestru.
- Information Security Risk Assessment — środki bezpieczeństwa odniesione do oceny ryzyka.

## Struktura rejestru (Art. 30 RODO)

Każda czynność przetwarzania zawiera pola:

| Pole | Opis |
|------|------|
| ID czynności | Unikalny identyfikator |
| Nazwa czynności | Np. "Obsługa rekrutacji", "Marketing e-mail" |
| Cel przetwarzania | Konkretny cel biznesowy |
| Podstawa prawna | Art. 6 (1) lit. a/b/c/d/e/f lub Art. 9 |
| Kategorie osób | Pracownicy / klienci / kandydaci / itp. |
| Kategorie danych | Dane zwykłe / szczególne kategorie (Art. 9) |
| Odbiorcy | Wewnętrzni + zewnętrzni (nazwy lub kategorie) |
| Kraje trzecie | Kraj + gwarancje (SCC / BCR / decyzja adekwatności) |
| Termin usunięcia | Okres retencji lub kryteria usunięcia |
| Środki bezpieczeństwa | Opis tech./org. środków ochrony |

## Odpowiedzialność i przegląd

- **Administrator** odpowiada za prowadzenie i aktualność rejestru.
- **DPO** nadzoruje kompletność i zgodność z RODO.
- Przegląd: min. raz w roku lub przy każdej nowej czynności przetwarzania.
