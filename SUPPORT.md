# SUPPORT.md

## Zakres wsparcia

Repo jest utrzymywane w modelu best-effort.

To oznacza, że:
- zgłoszenia techniczne mogą być analizowane,
- poprawki mogą być przyjmowane selektywnie,
- wsparcie nie jest gwarantowane w czasie SLA,
- priorytet mają problemy związane z kontraktem runtime, odtwarzalnością i stabilnością.

---

# Co warto zgłaszać

Najbardziej wartościowe są zgłoszenia dotyczące:

- problemów z bootstrapem,
- problemów z doctorem,
- błędów build current,
- regresji w fast / integration,
- problemów z pipeline,
- rozjazdu między dokumentacją a rzeczywistym zachowaniem repo,
- problemów z minimal mode / onboardingiem.

---

# Co powinno zawierać zgłoszenie

Dobre zgłoszenie powinno zawierać:

1. wersję / commit / tag repo,
2. system i wersję Pythona,
3. sposób uruchomienia,
4. pełny komunikat błędu,
5. informację, czy problem dotyczy minimal mode czy full runtime.

Jeżeli to możliwe, dołącz:
- wynik `python3 scripts/doctor.py --strict`,
- wynik `pip check`,
- wynik odpowiedniego poziomu testów.

---

# Ograniczenia wsparcia

Wsparcie może być ograniczone dla problemów wynikających z:

- prywatnych lub niedostępnych assets runtime,
- lokalnych modyfikacji niezgodnych z dokumentacją,
- niejawnych zmian środowiska poza wspieranym workflow,
- niestandardowego użycia repo nieopisanego w docs.

---

# Priorytety obsługi

Najwyższy priorytet mają:
1. problemy z odtwarzalnością,
2. problemy z kontraktem runtime,
3. regresje pipeline / integration,
4. błędy w docs prowadzące do złego uruchomienia.

Niższy priorytet mają:
- pytania ogólne,
- kosmetyka,
- sugestie niepowiązane z aktualnym zakresem repo.

---

# Kontakt / ścieżka zgłoszeń

Zgłoszenia techniczne proszę kierować przez Issues wraz z logami z `doctor --strict` i właściwego poziomu testów.
