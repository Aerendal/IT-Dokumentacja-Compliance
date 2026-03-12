---
title: PCI DSS Self-Assessment Questionnaire (SAQ)
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-03-09
aligned_by: codex
---

# PCI DSS Self-Assessment Questionnaire (SAQ)

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Przeprowadzić i udokumentować Kwestionariusz Samooceny PCI DSS (SAQ) dla organizacji niepodlegającej obowiązkowemu audytowi przez Qualified Security Assessor (QSA). SAQ jest narzędziem do oceny zgodności z PCI DSS v4.0 i dokumentuje spełnienie wymagań bezpieczeństwa dla środowiska danych posiadacza karty (CDE). Wynik SAQ jest przekazywany do banku-acquirera lub sieci kartowej.

## Zakres i granice
- Obejmuje: określenie właściwego typu SAQ (A/A-EP/B/B-IP/C/C-VT/D/P2PE), opis zakresu CDE i metody przetwarzania kart, ocenę spełnienia wymagań PCI DSS per typ SAQ, Attestation of Compliance (AOC), plan naprawczy dla niezgodności (jeśli dotyczy).
- Poza zakresem: pełny raport QSA (Report on Compliance — RoC), skanowanie zewnętrzne ASV (oddzielny raport), testy penetracyjne (oddzielny raport).

## Wejścia i wyjścia
- Wejścia: diagram CDE i przepływów danych kart, inwentaryzacja systemów w zakresie, wyniki skanowania ASV, polityki bezpieczeństwa organizacji, dowody implementacji kontroli PCI DSS.
- Wyjścia: wypełniony SAQ (właściwy typ), Attestation of Compliance (AOC), lista niezgodności z datami naprawy, plan naprawczy (Remediation Plan).

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- Cardholder Data Environment (CDE) Diagram — zakres SAQ zdefiniowany przez CDE.
- Network Diagram (PCI DSS) — wymagany jako dowód dla Wymagania 1.
- Vulnerability Scan Report (ASV) — wymagany dla wszystkich SAQ z zewnętrznym dostępem.
- Penetration Test Report — wymagany dla SAQ D i wybranych typów.
- Information Security Policy (PCI DSS) — dowód dla Wymagania 12.

## Typy SAQ PCI DSS v4.0

| Typ SAQ | Kiedy stosować |
|---------|---------------|
| SAQ A | Sprzedawcy e-commerce z pełnym outsourcingiem płatności |
| SAQ A-EP | E-commerce z przekierowaniem do zewnętrznego IFrame |
| SAQ B | Terminale fizyczne (imprinters / standalone POS bez IP) |
| SAQ B-IP | Terminale POS z połączeniem IP |
| SAQ C | Systemy POS z połączeniem internetowym |
| SAQ C-VT | Wirtualne terminale przez przeglądarkę |
| SAQ D | Wszystkie pozostałe sprzedawcy i usługodawcy |
| SAQ P2PE | Terminale zatwierdzone w programie P2PE PCI |

## Struktura samooceny (SAQ D — pełny zakres)

### Sekcja 1 — Informacje o organizacji
- Nazwa, adres, kontakt
- Typ działalności i kanały płatności
- Wolumen transakcji kartowych rocznie
- Typ SAQ i uzasadnienie wyboru

### Sekcja 2 — Zakres CDE
- Opis systemów w CDE
- Metody segmentacji sieci
- Opis przepływów danych posiadacza karty

### Sekcja 3 — Ocena wymagań PCI DSS
Dla każdego wymagania (1–12 + Req. A1/A2/A3):
- Status: Tak (Y) / Nie (N) / Nie dotyczy (N/A)
- Odpowiedzialna osoba/system
- Dowody (numer polityki, wynik skanu, itp.)

### Sekcja 4 — Plan naprawczy
| Wymaganie | Opis niezgodności | Planowane działanie | Termin | Właściciel |
|-----------|------------------|--------------------|---------| -----------|

### Sekcja 5 — Attestation of Compliance (AOC)
- Podpis Dyrektora Wykonawczego lub upoważnionej osoby
- Data oceny
- Oświadczenie o zgodności lub niezgodności
