---
title: Camera Configuration Reference
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Camera Configuration Reference


## Metadane

- Właściciel: Technical Writer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Referencja konfiguracji kamer (CCTV/AV): ustawienia, sieć, bezpieczeństwo i utrzymanie. Ma zapewnić spójność, jakość obrazu i zgodność z politykami bezpieczeństwa/prywatności.


## Zakres i granice

- Obejmuje: typy kamer, rozdzielczość/FPS/codec, bitrate, WDR/IR, PoE/zasilanie, sieć (VLAN, QoS), storage/retencję, dostęp (IAM, hasła, certyfikaty), szyfrowanie/RTSP/HTTPS, integrację z VMS/NVR, polityki prywatności (maskowanie, retention), monitoring zdrowia (uptime, temperatura), procedury update/patch, hardening (UPnP off, default creds), testy i checklisty.  
- Poza zakresem: projekt fizycznego rozmieszczenia kamer (oddzielny dokument).


## Użytkownicy i interesariusze
- **Technical Writer / Documentation Owner** — tworzy i utrzymuje dokumentację
- **Subject Matter Expert (SME)** — dostarcza merytoryczne treści i weryfikuje poprawność
- **Development Team** — recenzuje dokumentację techniczną
- **End Users** — korzystają z dokumentacji i zgłaszają nieścisłości

## Wejścia i wyjścia

- Wejścia: wymagania bezpieczeństwa/prywatności, sieć/VLAN, VMS/NVR spec, polityki retencji, modele kamer, środowisko (światło), SLA.  
- Wyjścia: standard config (profile), checklisty wdrożenia i audytu, matryca ustawień per scenariusz (lobby/parking/biuro), plan aktualizacji/patch, DoR/DoD.


## Założenia

- Sieć/VLAN/QoS dostępne.  
- VMS/NVR wspiera wymagane protokoły.  
- Polityki prywatności obowiązują.


## Otwarte pytania

- Jakie są lokalne wymogi prawne dot. monitoringu?  
- Jakie są limity storage/bandwidth?  
- Czy potrzebna redundancja storage/cluster VMS?


## Powiązania (meta)

- Key Documents: security_requirements, privacy_policy, network_segmentation_design, retention_policy, incident_response_runbook, vendor_hardening_guides.  
- Key Document Structures: wideo, sieć, bezpieczeństwo, retencja, monitoring, patching.  
- Document Dependencies: VMS/NVR, sieć (switch/PoE), storage, IAM, certyfikaty, monitoring.


## Zależności dokumentu

Wymaga: polityk bezpieczeństwa/prywatności, sieci VLAN/QoS, spec VMS/NVR, listy kamer i modeli, wymagań retencji, narzędzi monitoringu. Braki = DoR otwarte.


## Fazy cyklu życia

- Przygotowanie profili i standardów.  
- Wdrożenie i testy.  
- Operacje/monitoring i patching.  
- Audyty i aktualizacje.



## Struktura sekcji (szkielet)
1. Zakres (które usługi/aplikacje, środowiska).
2. Tabela parametrów: nazwa, opis, typ, default, dozwolone wartości, wpływ, środowisko.
3. Zasady zmian (kto może, proces, walidacja, rollout).
4. Bezpieczeństwo (sekrety vs konfiguracja jawna, maskowanie).
5. Testy i walidacja (smoke po zmianie, feature flags).
## Szybkie powiązania

- linkage_index.jsonl (camera/configuration/reference)  
- network_segmentation_design, retention_policy, security_requirements, vendor_hardening_guides


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

1. Wybierz profil dla scenariusza; ustaw w kamerze/VMS.  
2. Skonfiguruj sieć/VLAN/QoS, access i szyfrowanie; wykonaj checklistę hardeningu.  
3. Monitoruj i patchuj; aktualizuj DoR/DoD i linkage_index.


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

- VMS: Video Management System.  
- ONVIF: standard interoperacyjności kamer.  
- WORM: write-once-read-many (storage).


## Przykłady użycia

- Konfiguracja kamer w biurze/parkingu.  
- Audyt bezpieczeństwa istniejącej instalacji.  
- Przygotowanie do inspekcji regulatora prywatności.


## Ryzyka i ograniczenia

- Brak hardeningu → przejęcie kamer.  
- Zbyt wysoki bitrate → brak storage/QoS.  
- Nieaktualne patchy → podatności.


## Decyzje i uzasadnienia

- Profile bitrate/FPS per scenariusz.  
- Poziom szyfrowania i cert (self‑signed vs CA).  
- Retencja vs koszt storage.


## Powiązania z innymi dokumentami

- retention_policy — retencja.  
- security_requirements — hardening.  
- incident_response_runbook — incydenty.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Lokalne przepisy monitoringu/wideo, RODO/PII.  
- Wewnętrzne standardy bezpieczeństwa sieci.

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

- Ustawienia video → Storage/retencja → Sieć/QoS.  
- Dostęp/IAM → Hardening/patch → Bezpieczeństwo/prywatność.  
- Monitoring → Incident response → Patching.


## Struktura sekcji

1) Standardy wideo (rozdzielczość/FPS/codec/bitrate)  
2) Sieć i zasilanie (VLAN, QoS, PoE, izolacja)  
3) Bezpieczeństwo i dostęp (IAM, cert, szyfrowanie, hardening)  
4) Storage/retencja (NVR/VMS, retention, backup)  
5) Integracje (VMS/NVR, RTSP/ONVIF, alerty)  
6) Monitoring zdrowia (uptime, temperatura, lost frames)  
7) Patching/updates i lifecycle (firmware, testy)  
8) Checklists i audyt konfiguracji  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Profile ustawień per scenariusz i tabela bitrate/storage.  
- Checklista hardeningu i dostępu.  
- Plan patch/firmware z oknami i rollback.  
- Polityka maskowania prywatności i retencji.


## Wymagane streszczenia

- Executive snapshot: profile, retencja, status patchy, top ryzyka.  
- Karta szybkiej konfiguracji dla nowych instalacji.


## Guidance (skrót)

- Wyłącz UPnP/default creds; wymuś silne hasła/certy.  
- Oddziel kamery VLAN/PoE; QoS dla wideo krytycznego.  
- Kalibruj bitrate/FPS do sceny; monitoruj storage.  
- Aktualizuj firmware regularnie; testuj na kilku sztukach.  
- Przestrzegaj prywatności: maski, retencja, dostęp.


## Checklisty Definition of Ready (DoR)

- [ ] Polityki bezpieczeństwa/prywatności i retencji zebrane.  
- [ ] Spec sieci/VLAN/QoS i VMS/NVR znane.  
- [ ] Modele kamer i firmware zidentyfikowane.  
- [ ] Certyfikaty/IAM przygotowane.  
- [ ] Narzędzia monitoringu dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Profile konfiguracji zastosowane; status/wersja/data uzupełnione.  
- [ ] Hardening/iam/szyfrowanie wdrożone; testy nagrań i storage.  
- [ ] Monitoring zdrowia działa; alerty ustawione.  
- [ ] Plan patchy wdrożony; exceptions udokumentowane.  
- [ ] Linkage_index zaktualizowany; ryzyka/dec. zapisane.

