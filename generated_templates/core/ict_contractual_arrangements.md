---
title: ICT Contractual Arrangements
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-03-09
aligned_by: codex
---

# ICT Contractual Arrangements

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Opisać wymagania i szablon dla Umów Kontraktowych z Dostawcami Usług ICT zgodnie z Art. 30 DORA (Digital Operational Resilience Act). Każda umowa z dostawcą ICT wspierającym funkcje krytyczne lub istotne musi zawierać obowiązkowe klauzule dotyczące: opisu usług, poziomów usług, bezpieczeństwa danych, lokalizacji przetwarzania, prawa audytu, prawa wyjścia i planu wyjścia, podwykonawstwa oraz dostępności w sytuacjach kryzysowych.

## Zakres i granice
- Obejmuje: wymagane klauzule Art. 30 DORA (ust. 2 a–j), wzorzec klauzul do wbudowania w umowy z dostawcami ICT, wymagania dotyczące SLA dla krytycznych funkcji, klauzule audytu i inspekcji, klauzule exit plan i prawo wypowiedzenia, podwykonawstwo ICT, klauzule dotyczące lokalizacji danych i bezpieczeństwa.
- Poza zakresem: treść pełnej umowy handlowej (kontekst biznesowy), negocjacje komercyjne, ocena finansowa dostawcy.

## Wejścia i wyjścia
- Wejścia: ICT Third-Party Provider Register, klasyfikacja funkcji krytycznych/istotnych, wymagania bezpieczeństwa organizacji, ramy prawne (DORA, GDPR, przepisy sektorowe), wyniki due diligence dostawcy.
- Wyjścia: klauzule kontraktowe zgodne z Art. 30 DORA, umowa (lub aneks) z dostawcą ICT, klauzule audit rights, exit plan jako załącznik do umowy.

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- ICT Third-Party Provider Register — umowy odnoszą się do zarejestrowanych dostawców.
- ICT Risk Management Framework — wymagania bezpieczeństwa w umowach z frameworku.
- Data Processing Agreement (DPA) — gdy dostawca przetwarza dane osobowe, DPA jest częścią umowy.
- Business Continuity Plan — klauzule ciągłości usług muszą być spójne z BCP.

## Obowiązkowe klauzule kontraktowe (Art. 30 DORA)

### 1. Opis usług ICT (Art. 30 ust. 2 a)
- Pełny opis funkcji i usług ICT objętych umową
- Lokalizacje świadczenia usług i przetwarzania danych
- Podwykonawcy ICT — lista i zasady subdelegacji

### 2. Poziomy usług — SLA (Art. 30 ust. 2 b)
- Mierniki jakości, dostępności i wydajności
- Procedury raportowania incydentów
- Kary umowne za naruszenie SLA

### 3. Bezpieczeństwo informacji (Art. 30 ust. 2 c)
- Wymagania bezpieczeństwa minimalnego (szyfrowanie, IAM, logi)
- Obowiązki w zakresie zarządzania incydentami
- Prawo do testów penetracyjnych i audytów bezpieczeństwa

### 4. Dostępność, ciągłość i odtwarzanie (Art. 30 ust. 2 d)
- Wymagania RTO/RPO dla funkcji krytycznych
- Procedury ciągłości usługi i plan odtwarzania dostawcy
- Obowiązki dostawcy w sytuacji incydentu wpływającego na klienta

### 5. Prawo audytu i inspekcji (Art. 30 ust. 2 e)
- Prawo do audytów przez klienta lub audytora zewnętrznego
- Obowiązek dostarczania wyników audytów na żądanie
- Zakres dostępu do dokumentacji i systemów

### 6. Prawo wyjścia i exit plan (Art. 30 ust. 2 f–g)
- Warunki i przesłanki wypowiedzenia umowy
- Minimalne okresy wypowiedzenia
- Plan migracji danych i przejście do innego dostawcy

### 7. Lokalizacja danych (Art. 30 ust. 2 h)
- Kraje przechowywania i przetwarzania danych
- Ograniczenia jurysdykcyjne

### 8. Podwykonawstwo (Art. 30 ust. 2 i)
- Zasady subdelegacji — wymóg zgody lub powiadomienia
- Obowiązek stosowania tych samych standardów przez podwykonawców

### 9. Współpraca z organami nadzoru (Art. 30 ust. 2 j)
- Obowiązek dostarczania informacji na żądanie organu nadzoru
- Prawo organów do inspekcji u dostawcy
