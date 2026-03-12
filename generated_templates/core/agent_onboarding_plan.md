---
title: Agent Onboarding Plan
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Agent Onboarding Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan wdrożenia nowych agentów (np. contact center/support): szkolenia, narzędzia, procesy, KPI i certyfikacja. Ma skrócić czas do produktywności i zapewnić jakość obsługi.


## Zakres i granice

- Obejmuje: proces onboarding (preboarding, dostęp, konta, sprzęt), szkolenia (produkt, proces, narzędzia, bezpieczeństwo/PII), shadowing, checklisty, certyfikacja, KPI (AHT, CSAT, FCR, adherence), coaching/feedback, harmonogram, compliance (RODO/PCI jeśli dot.), komunikację i wsparcie.
- Poza zakresem: polityki HR ogólne (link), wynagrodzenia.


## Użytkownicy i interesariusze

- Support/Contact Center, Training, Security/Privacy, HR/IT, QA Program, Product.


## Wejścia i wyjścia

- Wejścia: profile ról, materiały szkoleniowe, systemy (CRM/CCaaS/KB), polityki bezpieczeństwa/PII, listy dostępów, KPI docelowe, trenerzy/mentorzy, harmonogram szkoleń.
- Wyjścia: plan onboarding, checklisty, harmonogram, certyfikacja, przypisanie mentorów, raport postępu, KPI po wdrożeniu.


## Założenia

- Systemy i materiały dostępne; mentorzy mają czas; polityki PII/security obowiązują.


## Otwarte pytania

- Jak długo monitorujemy KPI po starcie? 
- Czy wymagany re‑cert co rok?


## Powiązania (meta)

- Key Documents: support_playbook, knowledge_base_guidelines, security_pii_policy, quality_assurance_program, training_materials, access_management.
- Key Document Structures: proces, szkolenia, dostępy, KPI, raporty.
- Document Dependencies: systemy CCaaS/CRM/KB, access/IAM, trenerzy/mentors, materiały szkoleniowe, polityki security/PII.


## Zależności dokumentu

Wymaga: ról/profili, listy systemów/dostępów, materiałów szkoleniowych, polityk PII/security, KPI docelowych, trenerów/mentorów. Bez tego DoR otwarte.


## Fazy cyklu życia

- Preboarding: sprzęt, konta, dostępy.
- Szkolenia teoretyczne/praktyczne i shadowing.
- Certyfikacja i start produkcyjny.
- Monitoring KPI i coaching; retro po okresie próbnym.



## Struktura sekcji (szkielet)
- Narzędzia i dostęp
- SLA/kanały i procedury
- Tone of voice i makra/playbooki
- Bezpieczeństwo/prywatność (PII/PCI)
- Eskalacje i komunikacja
- QA i metryki jakości
- Zadania praktyczne i kryteria ukończenia
## Szybkie powiązania

- linkage_index.jsonl (support/agent_onboarding)
- support_playbook, knowledge_base_guidelines, security_pii_policy, quality_assurance_program, training_materials, access_management


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

1. Zdefiniuj role/KPI; przygotuj dostępy i materiały.
2. Zaplanuj harmonogram szkoleń/shadowing; przypisz mentorów.
3. Certyfikuj; monitoruj KPI i feedback; raportuj postęp.


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

- AHT, CSAT, FCR, Adherence, PII, PCI.


## Przykłady użycia

- Onboarding nowej fali agentów: 2 tyg. szkolenia, shadowing 5 dni, certyfikacja, KPI monitorowane 30 dni.


## Ryzyka i ograniczenia

- Brak dostępu/sprzętu opóźnia start; brak PII szkolenia → ryzyko compliance; brak KPI/feedback → niska jakość.


## Decyzje i uzasadnienia

- [Decyzja] Kryteria certyfikacji — uzasadnienie jakości; [Decyzja] KPI startowe — uzasadnienie celów.


## Powiązania z innymi dokumentami

- Support Playbook, KB Guidelines, Security/PII Policy, QA Program, Training Materials, Access Mgmt.


## Powiązania z sekcjami innych dokumentów

- Access Mgmt → dostępy; QA Program → KPI; PII Policy → szkolenia.


## Słownik pojęć w dokumencie

- AHT, CSAT, FCR, Adherence, PII, PCI.


## Wymagane odwołania do standardów

- PII/PCI wytyczne, polityki bezpieczeństwa, regulacje branżowe jeśli dot.


## Mapa relacji sekcja→sekcja

- Dostępy/Szkolenia → Shadowing → Certyfikacja → KPI/Coaching.


## Mapa relacji dokument→dokument

- Onboarding Plan → Support Playbook/KB/PII/QA → KPI/Raporty.


## Ścieżki informacji

- Preboarding → Szkolenia → Shadowing → Certyfikacja → KPI/Feedback → Raport.


## Weryfikacja spójności

- [ ] Dostępy/szkolenia/mentoring/certyfikacja opisane; KPI i raporty ustawione; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy agent ma checklistę, szkolenia, certyfikację, KPI i feedback.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Checklisty dostępu, materiały szkoleniowe, harmonogram, certyfikacja, raport KPI, feedback log.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- Support/Training → Security/Privacy → Product/QA → Owner sign‑off.


## Metryki jakości

- Czas do produktywności, zdawalność certyfikacji, AHT/CSAT/FCR po starcie, błędy PII, retencja po okresie próbnym.

## Kryteria ukończenia

- [ ] Onboarding przeprowadzony, KPI/feedback raportowane; dokument w linkage_index; wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Dostępy → Szkolenia → Shadowing → Certyfikacja → KPI.
- Feedback/coaching → KPI → Plan poprawy.


## Struktura sekcji

1) Zakres ról i cele onboarding (KPI startowe)  
2) Harmonogram i etapy (preboarding, szkolenia, shadowing, certyfikacja)  
3) Dostępy/systemy/sprzęt (IAM, PII/PCI zasady)  
4) Szkolenia i materiały (produkt/proces/narzędzia/security/PII)  
5) Shadowing i praktyka (czas, kryteria)  
6) Certyfikacja i kryteria zaliczenia  
7) KPI i monitoring (AHT, CSAT, FCR, adherence)  
8) Coaching/feedback i plan poprawy  
9) Raportowanie postępu i ryzyka


## Wymagane rozwinięcia

- Checklisty dostępu/sprzętu; plan szkoleń; kryteria certyfikacji; KPI startowe.
- Mentorzy/trenerzy i cadence feedback; raport postępu.


## Wymagane streszczenia

- Timeline, systemy/dostępy, kluczowe szkolenia, KPI startowe, kryteria certyfikacji.


## Guidance (skrót)

- Zapewnij dostępy i sprzęt przed dniem 1; zacznij od bezpieczeństwa/PII.
- Łącz teorię + shadowing + praktykę; mierz KPI od startu.
- Ustal jasne kryteria certyfikacji; dawaj szybki feedback i coaching.


## Checklisty Definition of Ready (DoR)

- [ ] Role/KPI zdefiniowane; materiały i systemy dostępne; polityki PII/security znane.
- [ ] Harmonogram i mentorzy przygotowani; struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Onboarding wykonany; certyfikacja zakończona; KPI i raporty dostępne.
- [ ] Feedback/coaching udokumentowane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.

