---
title: Compliance with Regulations
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Compliance with Regulations


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zebrać i potwierdzić zgodność systemu/projektu z kluczowymi regulacjami/standardami (np. GDPR/RODO, PCI, ISO, SOC, branżowe), mapując wymagania na kontrolki i dowody, wskazując status i plan remediacji.


## Zakres i granice

- Obejmuje: listę regulacji/standardów i zakres systemu, mapowanie wymaganie→kontrola→dowód, status (spełnione/luka/RAG), ryzyka, plan remediacji i waivery z sunset, cykliczne przeglądy/aktualizacje.
- Poza zakresem: szczegółowy audyt techniczny i projektowanie nowych kontrolek (osobne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: Statement of Applicability/katalog wymagań, polityki i standardy, wyniki skanów/testów/audytów, logi dowodów, właściciele kontroli, wymagania klienta/regulatora.
- Wyjścia: tabela wymagań→kontrole→dowody→status, lista luk i waivery, plan remediacji (owner/ETA), decyzje go/conditional/no‑go, aktualizacje risk register.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: compliance_verification, compliance_monitoring_runbook, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference, data_privacy_compliance.
- Key Document Structures: wymagania, kontrole, dowody, status, remediacja/waivery.
- Document Dependencies: katalog kontroli, repo dowodów, SIEM/logi, skany/testy, GRC/ticketing.



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
- Cel i zakres polityki
- Zakres obowiązywania i wyjątki
- Role i odpowiedzialności
- Wymagania/kontrole (techniczne/procesowe)
- Proces zarządzania zmianą i wyjątkami
- Dowody/audyt, metryki zgodności
- Komunikacja/szkolenia i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (compliance/regulations)
- compliance_verification, compliance_monitoring_runbook, compliance_metrics_dashboard, compliance_audit_report, risk_register, change_management_plan, security_controls_reference, data_privacy_compliance


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

1. Wypisz regulacje i zakres; zmapuj wymagania na kontrole i dowody.  
2. Oceń status RAG, wskaż luki/waivery, dodaj plan remediacji i ETA.  
3. Zaplanuj przeglądy i odświeżanie dowodów; aktualizuj linkage_index/checklisty.


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

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

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

- [ ] Każde wymaganie ma kontrolę, dowód, status i ownera; waivery mają sunset.  
- [ ] Luki mają plan remediacji/ETA; RAG spójny z dowodami; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Tabela wymagań/kontroli/dowodów/statusów, repo dowodów, raporty skanów/testów, waiver log, risk register, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % wymagań z dowodem, % pass vs luki, liczba waiverów i czas sunset, czas zamknięcia luk, terminowość przeglądów/dowodów.

## Kryteria ukończenia

- [ ] Status RAG i plan remediacji opublikowane; dowody kompletne; dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Regulacje/standardy i zakres systemu (SoA, systemy, dane, jurysdykcje)  
2) Mapowanie wymaganie → kontrola → dowód (lokalizacja, owner)  
3) Status i ryzyka (RAG, luki, wpływ, powiązanie z risk register)  
4) Plan remediacji i waivery (owner, ETA, sunset, kompensacje)  
5) Przegląd cykliczny/aktualizacja (cadence, odpowiedzialni)  
6) Załączniki (export mapowania, raporty skanów/testów, log dowodów)


## Wymagane rozwinięcia

- Tabela wymagań z kontrolą, dowodem, statusem, ownerem, ETA; waivery i sunset.  
- Kryteria RAG i decyzji go/conditional/no‑go; priorytety luk.  
- Harmonogram przeglądów i odświeżania dowodów; repo dowodów.


## Wymagane streszczenia

- Executive: regulacje w scope, status RAG, top luki/waivery, plan remediacji i ETA.


## Guidance (skrót)

- Każde wymaganie musi mieć kontrolę i dowód; brak dowodu = luka.  
- Status opieraj na dowodach z datą; aktualizuj po audytach/testach/zmianach.  
- Waivery wymagają sunset i kompensacji; aktualizuj risk register dla luk.  
- Planuj przeglądy/odświeżanie dowodów w cyklu (np. m-c/kw.).


## Checklisty Definition of Ready (DoR)

- [ ] Regulacje/standardy i SoA dostępne; zakres systemu określony.  
- [ ] Repo dowodów i właściciele kontroli znani; wstępne RAG kryteria ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Mapowanie wymaganie→kontrola→dowód→status kompletne; luki/waivery opisane.  
- [ ] Plan remediacji z owner/ETA; risk register zaktualizowany; dokument w linkage_index; metadane aktualne.

