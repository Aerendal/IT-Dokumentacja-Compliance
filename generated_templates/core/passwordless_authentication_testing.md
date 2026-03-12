---
title: Passwordless Authentication Testing
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Passwordless Authentication Testing


## Metadane

- Właściciel: QA Lead
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zdefiniować zakres i procedury testów dla wdrożeń passwordless (WebAuthn/FIDO2, magic links, passkeys), aby zapewnić bezpieczeństwo, użyteczność i zgodność z wymaganiami.


## Zakres i granice

- Obejmuje: scenariusze rejestracji/uwierzytelniania/recovery, multi-device, roaming keys, device binding, step-up, phishing-resistance, fallback, UX na różnych platformach/przeglądarkach, bezpieczeństwo (anti-replay, origin binding), logowanie i audyt.  
- Poza zakresem: pełny projekt MFA (opisany w multi_factor_authentication_design).


## Użytkownicy i interesariusze
- **QA Lead / Test Manager** — planuje strategię testowania i zarządza procesem QA
- **QA Engineer** — projektuje i wykonuje przypadki testowe
- **Development Team** — naprawia defekty i dostarcza testowalny kod
- **Product Owner** — definiuje kryteria akceptacji i priorytetyzuje defekty

## Wejścia i wyjścia

- Wejścia: wymagania security/UX, obsługiwane metody passwordless, listy urządzeń/przeglądarek, polityki recovery/fallback, integracje IdP/SSO, test accounts.  
- Wyjścia: plan testów, checklisty DoR/DoD, wyniki i defekty, raport zgodności (phishing-resistance), rekomendacje poprawy UX/bezpieczeństwa.


## Założenia

- IdP/SSO wspiera WebAuthn/passkeys.  
- Dostępne device lab i SIEM.  
- Zespół może zautomatyzować regresję.


## Otwarte pytania

- Jak często powtarzać testy phishing?  
- Czy wymagać passkeys mandatory dla adminów?  
- Jak raportować coverage do audytu?

## Powiązania (meta)

- Key Documents: multi_factor_authentication_design, access_control_policy, logging_and_audit_trail, security_controls_reference, api_security_testing.  
- Key Document Structures: scenariusze, urządzenia, bezpieczeństwo, UX, recovery, logi.  
- Document Dependencies: IdP/SSO, WebAuthn/FIDO2 provider, device lab, SIEM.


## Zależności dokumentu

Wymaga: wdrożonych metod passwordless, listy urządzeń/przeglądarek, polityk recovery, integracji IdP/SSO, narzędzi do logów i monitoringu. Brak = brak DoR.


## Fazy cyklu życia

- Planowanie scenariuszy i urządzeń.  
- Testy bezpieczeństwa i UX.  
- Raportowanie i defekty.  
- Retesty i akceptacja.  
- Monitoring i regresja.



## Struktura sekcji (szkielet)
- Prereqs (IDP, certy, platformy, feature flags).
- Konfiguracja IDP/IAM i RP (WebAuthn params, attestation policy).
- Front/back flows (registration/auth, fallback, step-up).
- Recovery/fallback (backup codes, support procesy).
- Testy (functional, security, a11y, UX, device matrix).
- Rollout (pilot, procent/region, komunikacja, metrics freeze).
- Monitoring/KPI (success rate, drop-off, fraud, latency).
- Wsparcie i runbooki (FAQ, escalation).
## Szybkie powiązania

- linkage_index.jsonl (passwordless/authentication/testing)  
- multi_factor_authentication_design, api_security_testing


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

1. Zdefiniuj metody i urządzenia testowe; przygotuj konta.  
2. Uruchom scenariusze bezpieczeństwa i UX; loguj wyniki.  
3. Zgłoś defekty; retest po poprawkach.  
4. Raportuj pokrycie i rekomendacje; zaktualizuj dokument/linkage_index.


## Checklisty jakości

### Kompletność
- **Kryterium:** Wszystkie wymagane sekcje i pola są wypełnione
- **Metryka:** Odsetek wypełnionych sekcji do wymaganych
- **Próg OK:** 90%
- **Narzędzie:** template_auditor.py, checklist_atomic.jsonl

### Dokładność
- **Kryterium:** Informacje są poprawne merytorycznie i aktualne
- **Metryka:** Przegląd ekspercki; data ostatniej aktualizacji
- **Próg OK:** Przegląd co 3 mies.
- **Narzędzie:** regulation_updater.py

### Spójność
- **Kryterium:** Terminologia i struktura są spójne w całej bibliotece
- **Metryka:** Liczba niespójności terminologicznych i strukturalnych
- **Próg OK:** 0 niespójności
- **Narzędzie:** bulk_section_patcher.py

### Śledzalność
- **Kryterium:** Każda sekcja ma źródło (standard, regulacja, decyzja)
- **Metryka:** Odsetek sekcji z wypełnionymi standards_refs
- **Próg OK:** 80%
- **Narzędzie:** impact_analyzer.py

### Aktualność
- **Kryterium:** Dokument jest aktualny względem obowiązujących regulacji
- **Metryka:** Czas od ostatniej aktualizacji vs. częstotliwość przeglądów
- **Próg OK:** < 6 mies.
- **Narzędzie:** changelog_tracker.py

### Użyteczność
- **Kryterium:** Użytkownik końcowy może efektywnie wypełnić dokument na podstawie guidance
- **Metryka:** Ocena guidance (score z template_auditor); feedback użytkowników
- **Próg OK:** Score >= 70
- **Narzędzie:** template_auditor.py

## Definicje robocze

- WebAuthn: standard uwierzytelniania bez haseł (FIDO2).  
- Passkey: klucz sprzętowy/biometryczny powiązany z kontem.  
- Origin binding: powiązanie uwierzytelnienia z domeną.


## Przykłady użycia

- Test passkey na iOS/Android i desktop.  
- Symulacja phishingu z podmienionym origin.  
- Recovery po utracie telefonu z TOTP/passkey.


## Ryzyka i ograniczenia

- Słabe fallbacki → kompromitacja.  
- Brak logów → trudna forensics.  
- Brak kompatybilności na platformach → zła adopcja.  
- Brak testów phishing → fałszywe poczucie bezpieczeństwa.


## Decyzje i uzasadnienia

- Akceptowane metody/fallbacki.  
- Platformy obowiązkowe do testów.  
- Poziom logowania i retencja.  
- Kryteria akceptacji phishing-resistance.


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

## Powiązania sekcja↔sekcja

- Scenariusze ↔ Urządzenia ↔ Bezpieczeństwo/UX.  
- Recovery/fallback ↔ Phishing-resistance ↔ Audyt.  
- Logi ↔ Incydenty ↔ Raporty.


## Struktura sekcji

1) Metody passwordless i wymagania  
2) Scenariusze testowe (register/auth/recover/step-up)  
3) Urządzenia/przeglądarki i kompatybilność  
4) Bezpieczeństwo: phishing-resistance, origin, anti-replay  
5) UX i dostępność (a11y, fallback)  
6) Logi/audyt i alerty  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Macierz scenariusz × urządzenie/przeglądarka × wynik.  
- Testy phishing (origin mismatch, fake RP).  
- Recovery/fallback test cases (lost device, new device).  
- Performance (time to auth) i UX ankiety.  
- Logi i korelacja w SIEM.  
- Kryteria akceptacji i raport szablon.


## Wymagane streszczenia

- Executive summary: pokrycie scenariuszy, defekty krytyczne.  
- Skrót phishing-resistance i recovery wyników.


## Guidance (skrót)

- Testuj na różnych platformach (desktop/mobile) i przeglądarkach.  
- Wymuś origin binding i odrzucaj słabe fallbacki.  
- Recovery musi być bezpieczne; unikaj e-mail bez dodatkowych kroków.  
- Loguj kluczowe zdarzenia (register/auth/recover/fail) z correlation ID.  
- Automatyzuj regresję; integruj z CI.  
- Aktualizuj linkage_index po cyklu testów.


## Checklisty Definition of Ready (DoR)

- [ ] Metody passwordless wdrożone; polityka recovery zdefiniowana.  
- [ ] Lista urządzeń/przeglądarek gotowa.  
- [ ] Narzędzia logów/SIEM dostępne.  
- [ ] Konta testowe i dane przygotowane.  
- [ ] Kryteria akceptacji uzgodnione.


## Checklisty Definition of Done (DoD)

- [ ] Testy wykonane; krytyczne defekty zamknięte.  
- [ ] Raport i linkage_index zaktualizowane.  
- [ ] Logi/audyt kompletne; alerty skonfigurowane.  
- [ ] Recovery/fallback zweryfikowane; phishing tests zaliczone.  
- [ ] Plan regresji w CI uruchomiony.

