# SECURITY.md

## Cel dokumentu

Ten dokument opisuje sposób zgłaszania problemów bezpieczeństwa oraz granice bezpieczeństwa repo.

---

# 1. Jak zgłaszać problemy bezpieczeństwa

Nie zgłaszaj wrażliwych problemów bezpieczeństwa przez publiczny issue tracker, jeśli:
- problem dotyczy sekretów,
- problem umożliwia nieautoryzowany dostęp,
- problem dotyczy ujawnienia wrażliwych danych,
- problem dotyczy prywatnych assets runtime.

Zamiast tego użyj prywatnego kanału zgłoszenia.

## Kanał zgłoszenia

Problemy bezpieczeństwa proszę zgłaszać prywatnie przez dedykowany kanał kontaktu z maintainerem repo.

---

# 2. Co traktujemy jako problem bezpieczeństwa

Za problem bezpieczeństwa uznajemy w szczególności:

- obecność sekretów w repo,
- wyciek danych w runtime assets,
- ujawnienie prywatnych ścieżek lub danych operacyjnych,
- możliwość nieautoryzowanego dostępu do danych runtime,
- niekontrolowane wykonywanie kodu z niejawnych wejść,
- niebezpieczne założenia w bootstrapie lub pipeline.

---

# 3. Co nie jest problemem bezpieczeństwa

Za problem bezpieczeństwa nie uznajemy automatycznie:

- zwykłego błędu logicznego bez wpływu na bezpieczeństwo,
- regresji testów,
- braku assetów runtime,
- niezgodności dokumentacji z uruchomieniem,
- problemów z lokalnym środowiskiem bez wpływu na dane lub dostęp.

---

# 4. Zasady pracy z assets runtime

Assets runtime mogą mieć status:
- publiczny,
- lokalny,
- zewnętrzny,
- organizacyjny.

Nie należy:
- publikować prywatnych assets w repo bez jawnej decyzji,
- commitować lokalnych backupów runtime DB,
- publikować danych, których status nie został ustalony.

Status assets powinien być zgodny z:
- `docs/RUNTIME_BOOTSTRAP.md`
- `docs/OPEN_DECISIONS.md`

---

# 5. Sekrety i skany

Przed pokazaniem repo na zewnątrz należy sprawdzić:
- brak tokenów,
- brak haseł,
- brak sekretów w skryptach i konfiguracji,
- brak prywatnych ścieżek użytkownika.

Rekomendowane jest użycie skanera sekretów, np.:
- `gitleaks`
- `trufflehog`

---

# 6. Oczekiwania wobec zgłoszenia

Dobre zgłoszenie bezpieczeństwa powinno zawierać:
- krótki opis problemu,
- zakres wpływu,
- warunki odtworzenia,
- informację, czy problem wymaga prywatnych assets,
- propozycję ograniczenia skutków, jeśli jest znana.

---

# 7. Zakres odpowiedzialności

Repo jest utrzymywane z naciskiem na:
- audytowalność,
- jawny kontrakt runtime,
- ograniczanie ukrytych zależności,
- przewidywalność procesu.

Nie oznacza to automatycznie pełnej odporności na wszystkie klasy zagrożeń.  
Granice bezpieczeństwa repo należy czytać razem z dokumentacją runtime i onboardingową.
