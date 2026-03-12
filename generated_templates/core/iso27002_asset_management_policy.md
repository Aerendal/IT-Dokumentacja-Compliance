---
title: "Asset Management Policy"
status: aktywny
aligned: ISO/IEC 27002
---

## Cel dokumentu
Zdefiniować politykę zarządzania aktywami informacyjnymi zgodnie z ISO/IEC 27002:2022 temat 5 (Organizational Controls) — kontrole 5.9 (Inventory of Information and Other Assets), 5.10 (Acceptable Use of Assets) i 5.11 (Return of Assets). Polityka ustanawia wymóg inwentaryzacji wszystkich aktywów, przypisania właścicielstwa, klasyfikacji aktywów informacyjnych i zasad dopuszczalnego użytkowania — zapewniając że aktywa są chronione proporcjonalnie do ich wartości i klasyfikacji przez cały cykl życia (od nabycia do bezpiecznego usunięcia).

## Zakres i granice
Polityka obejmuje wszystkie aktywa informacyjne organizacji: sprzęt (serwery, urządzenia końcowe, urządzenia sieciowe), oprogramowanie (licencje, aplikacje), dane (bazy danych, dokumenty, backupy), usługi (SaaS, chmura) i aktywa niematerialne (własność intelektualna, know-how).

## Wejścia i wyjścia
**Wejścia:**
- Inwentarz aktywów (hardware, software, data, services)
- Schemat klasyfikacji informacji organizacji
- Wyniki Risk Assessment w zakresie aktywów
- Wymagania ISO/IEC 27001 Annex A 5.9–5.11

**Wyjścia:**
- Zatwierdzona polityka zarządzania aktywami
- Rejestr aktywów (Asset Inventory) z właścicielami
- Klasyfikacja aktywów i etykietowanie

## Zasady zarządzania aktywami

### 1. Inwentaryzacja aktywów (ISO/IEC 27002 5.9)
- Wszystkie aktywa informacyjne muszą być zidentyfikowane i zarejestrowane w centralnym rejestrze
- Rejestr zawiera: identyfikator, opis, właściciela, lokalizację, klasyfikację, status
- Inwentarz jest przeglądany i aktualizowany co najmniej raz na rok i przy każdej istotnej zmianie
- Aktywa w chmurze są objęte inwentaryzacją (Cloud Asset Inventory)

### 2. Właścicielstwo aktywów
Każdy aktyw musi mieć przypisanego **Właściciela Aktywa** odpowiedzialnego za:
- Klasyfikację aktywa i utrzymanie właściwego poziomu ochrony
- Autoryzację dostępu do aktywa
- Przegląd uprawnień dostępu (minimum raz w roku)
- Zapewnienie bezpiecznego usunięcia aktywa po zakończeniu jego cyklu życia

### 3. Klasyfikacja aktywów informacyjnych
| Klasa | Opis | Przykłady | Wymagania ochrony |
|-------|------|-----------|------------------|
| **Tajne** | Najwyższa wrażliwość | Klucze kryptograficzne, dane biometryczne, sekrety biznesowe | Szyfrowanie AES-256, dostęp ograniczony, logging |
| **Poufne** | Wrażliwe dane biznesowe | Dane osobowe, dokumenty umów, dane finansowe | Szyfrowanie, kontrola dostępu RBAC |
| **Wewnętrzne** | Użytek wewnętrzny | Dokumentacja techniczna, procedury, korespondencja | Kontrola dostępu, nieudostępnianie zewnętrznym |
| **Publiczne** | Dozwolone do ujawnienia | Materiały marketingowe, dokumenty publiczne | Integralność |

### 4. Dopuszczalne użytkowanie aktywów (ISO/IEC 27002 5.10)
- Aktywa organizacji mogą być używane wyłącznie w celach służbowych i zgodnie z politykami bezpieczeństwa
- Zakazane: instalowanie nieautoryzowanego oprogramowania, kopiowanie danych na nieautoryzowane nośniki, obejście kontroli bezpieczeństwa
- Używanie prywatnych urządzeń do przetwarzania danych organizacji wymaga zatwierdzenia (BYOD Policy)
- Monitoring użytkowania aktywów może być prowadzony zgodnie z prawem pracy i polityką prywatności

### 5. Zwrot aktywów (ISO/IEC 27002 5.11)
Przy rozwiązaniu umowy lub zmianie stanowiska pracownik/wykonawca musi zwrócić:
- Wszystkie urządzenia (laptop, telefon, tokeny, karty dostępu)
- Dokumenty i nośniki zawierające dane organizacji
- Dostępy (hasła, klucze, certyfikaty) muszą być unieważnione (Offboarding Checklist)

### 6. Bezpieczne usunięcie aktywów
- Nośniki danych przed utylizacją: bezpieczne wyczyszczenie (NIST SP 800-88: Clear/Purge/Destroy)
- Sprzęt: certyfikat zniszczenia danych od certyfikowanego recyklera IT
- Oprogramowanie: dezaktywacja licencji przed usunięciem

## Rejestr aktywów — szablon
| ID | Nazwa aktywa | Typ | Właściciel | Lokalizacja | Klasyfikacja | Data aktualizacji |
|----|-------------|-----|-----------|-------------|--------------|-----------------|
| A001 | [Serwer produkcyjny X] | Sprzęt | [IT Ops] | [DC-01] | Poufne | [Data] |
| A002 | [System ERP] | Oprogramowanie | [CIO] | [SaaS] | Poufne | [Data] |

## Powiązania (meta)
- standardy-i-compliance: ISO/IEC 27002:2022 kontrole 5.9/5.10/5.11, ISO/IEC 27001 Annex A 5.9-5.11, NIST SP 800-53 CM-8
- raci-i-role: CISO (Owner/Approver), Asset Owners (Responsible), IT Ops (Consulted), pracownicy (Informed)
