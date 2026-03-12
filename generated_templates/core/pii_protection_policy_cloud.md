---
title: PII Protection Policy Cloud
status: needs_content
aligned: true
aligned_rev: 1
aligned_by: codex
aligned_at: 2026-03-09
---

# PII Protection Policy Cloud

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Opisać Politykę Ochrony Danych Osobowych (PII) w Środowisku Chmurowym zgodnie z ISO/IEC 27018:2019. Polityka określa obowiązki podmiotu przetwarzającego PII (PII processor) w chmurze: zasady minimalizacji i ograniczenia celu, kontrola dostępu, szyfrowanie, powiadamianie o incydentach, prawa podmiotów danych, zakaz wykorzystania PII w celach marketingowych, zasady przechowywania i usuwania PII oraz przejrzystość wobec klientów-administratorów.

## Zakres i granice
- Obejmuje: zasady przetwarzania PII przez dostawcę usług chmurowych (CSP) lub podmiot korzystający z chmury, kontrole ochrony PII specyficzne dla chmury (rozszerzenie ISO/IEC 27002 dla chmury), zgoda i cel przetwarzania PII, szyfrowanie PII w spoczynku i w tranzycie, kontrola dostępu do PII w chmurze, powiadamianie administratora o incydentach PII, zakaz wtórnego wykorzystania PII bez zgody, usuwanie PII po zakończeniu umowy.
- Poza zakresem: ogólna polityka bezpieczeństwa informacji (ISO 27001), Privacy Policy skierowana do osób fizycznych (GDPR Art. 13/14).

## Wejścia i wyjścia
- Wejścia: umowy z klientami-administratorami PII, inwentaryzacja danych PII w chmurze, wymagania ISO/IEC 27018, wymagania GDPR/RODO (gdy PII to dane osobowe), certyfikacja ISO/IEC 27001 jako podstawa.
- Wyjścia: polityka ochrony PII w chmurze (udokumentowana informacja), klauzule ochrony PII w umowach z klientami, instrukcje bezpieczeństwa dla pracowników mających dostęp do PII, dowody certyfikacji (ISO 27018 lub SOC 2 z kryterium prywatności).

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- Cloud Security Policy (ISO/IEC 27017) — polityka PII rozszerza ogólną cloud security policy.
- Information Security Policy (ISO/IEC 27001) — nadrzędna polityka bezpieczeństwa.
- Data Processing Agreement (DPA/GDPR) — polityka jest implementacją wymagań DPA.
- PII Incident Notification Procedure — procedura powiadamiania wynikająca z tej polityki.

## Treść polityki

### 1. Zakres i cel
Polityka dotyczy wszystkich systemów, usług i pracowników przetwarzających Dane Osobowe (PII) w środowiskach chmurowych (IaaS / PaaS / SaaS) organizacji.

### 2. Zasady przetwarzania PII w chmurze (ISO/IEC 27018 Annex A)

#### 2.1 Zgoda i cel (A.1)
- PII przetwarza się wyłącznie w celach określonych przez administratora (controller)
- Zakaz wykorzystania PII do celów marketingowych bez wyraźnej zgody
- Cel przetwarzania dokumentuje się w Rejestrze PII

#### 2.2 Minimalizacja danych (A.2)
- Zbierane i przechowywane jest tylko PII niezbędne do realizacji usługi
- Regularne przeglądy wolumenu PII i usuwanie zbędnych danych

#### 2.3 Ograniczenie geograficzne (A.3)
- Lokalizacje przetwarzania PII są ujawniane klientom-administratorom
- Przekazywanie PII poza EOG: wyłącznie z odpowiednimi gwarancjami (SCC/BCR)

#### 2.4 Prawa podmiotów danych (A.4)
- Procedury realizacji żądań dostępu, sprostowania, usunięcia i przeniesienia PII
- Termin odpowiedzi: [X dni roboczych]

#### 2.5 Kontrola dostępu (A.5)
- Dostęp do PII: wyłącznie autoryzowany personel z uzasadnioną potrzebą
- Uwierzytelnianie wieloskładnikowe (MFA) dla dostępu do systemów z PII
- Logowanie wszystkich dostępów do PII

#### 2.6 Szyfrowanie (A.6)
- PII w spoczynku: szyfrowanie AES-256 lub równoważne
- PII w tranzycie: TLS 1.2+ obowiązkowe
- Zarządzanie kluczami: zgodnie z polityką kryptografii

#### 2.7 Powiadamianie o incydentach (A.7)
- Naruszenia dotyczące PII: powiadomienie klienta-administratora w ciągu [X godzin]
- Zawartość powiadomienia: opis incydentu, zakres PII, podjęte działania

#### 2.8 Usuwanie PII (A.8)
- Po zakończeniu umowy: bezpieczne usunięcie lub zwrot PII w ciągu [X dni]
- Dowód usunięcia: certyfikat zniszczenia danych

### 3. Odpowiedzialność i audyt
- Właściciel polityki: [CISO / Privacy Officer]
- Audyt zgodności: [raz w roku lub po istotnych zmianach]
- Certyfikacja ISO/IEC 27018: [status certyfikacji]
