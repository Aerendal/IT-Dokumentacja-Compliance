"""
itdoc._batch — profesjonalny wzorzec dla przetwarzania wsadowego (batch processing).

Problem z gołym ``except: pass``
---------------------------------
Cichy wyjątek w pętli batch jest często celowy (jeden zły rekord nie powinien
zatrzymywać całego przebiegu), ale:

* utrudnia debugowanie — nie wiesz co zostało pominięte ani dlaczego,
* może maskować regresje — test nie wykryje nowego wyjątku bo jest połykany,
* CodeQL/Bandit zgłaszają go jako problem jakości kodu.

Rozwiązanie: ``batch_continue()``
-----------------------------------
Kontekst managerowy który:

1. **Normalnie** — loguje pominięty wyjątek na poziomie DEBUG (cichy w produkcji).
2. **ITDOC_STRICT=1** — re-raise'uje każdy wyjątek (tryb debugowania).
3. **Testowalny** — zachowanie jest udokumentowane testami, nie "zgadywane".

Użycie::

    from itdoc._batch import batch_continue

    for f in files:
        with batch_continue(f"reading {f.name}"):
            data = f.read_text()
            process(data)

    # Zamiast:
    for f in files:
        try:
            data = f.read_text()
            process(data)
        except Exception:
            pass  # <- połyka błąd niewidzialnie

Tryb debugowania::

    ITDOC_STRICT=1 python scripts/compliance_check.py

    # Spowoduje re-raise wszystkich wyjątków które normalnie byłyby pominięte.
    # Zobaczysz pełny traceback zamiast ciszy.

Konfiguracja przez zmienną środowiskową::

    ITDOC_STRICT=1    — re-raise wszystkich wyjątków batch_continue
    ITDOC_STRICT=0    — (domyślnie) tryb normalny, loguj DEBUG i kontynuuj
"""

from __future__ import annotations

import logging
import os
from collections.abc import Generator
from contextlib import contextmanager

_DEFAULT_LOGGER = logging.getLogger(__name__)


def _strict_mode() -> bool:
    """Return True if ITDOC_STRICT=1 is set in the environment."""
    return os.environ.get("ITDOC_STRICT", "0").strip() == "1"


@contextmanager
def batch_continue(
    context: str,
    *,
    logger: logging.Logger | None = None,
    reraise: tuple[type[BaseException], ...] = (),
) -> Generator[None, None, None]:
    """Context manager for batch processing: log-and-continue on exception.

    Zamiast gołego ``except: pass`` używaj tego kontekstu. Zachowanie:

    * Normalnie: łapie ``Exception``, loguje na DEBUG, kontynuuje pętlę.
    * ``ITDOC_STRICT=1``: re-raise (pełny traceback — tryb debugowania).
    * ``reraise``: typy wyjątków które *zawsze* są re-raise'owane niezależnie
      od ITDOC_STRICT (np. ``KeyboardInterrupt``, ``SystemExit``).

    Args:
        context: Opis co było przetwarzane (pojawi się w logu i traceback).
                 Powinien jednoznacznie identyfikować element — np. nazwa pliku,
                 ID rekordu, URL.
        logger:  Logger do użycia. Domyślnie ``logging.getLogger('itdoc._batch')``.
        reraise: Tuple typów wyjątków które zawsze są propagowane.

    Examples:
        Podstawowe użycie::

            for path in all_paths:
                with batch_continue(f"parse {path.name}"):
                    result = parse_template(path)
                    results.append(result)

        Z niestandardowym loggerem::

            _log = logging.getLogger(__name__)
            for row in db_rows:
                with batch_continue(f"row id={row['id']}", logger=_log):
                    process_row(row)

        Zawsze re-raise dla konkretnych typów::

            for item in items:
                with batch_continue("item", reraise=(MemoryError,)):
                    process(item)
    """
    _log = logger or _DEFAULT_LOGGER
    try:
        yield
    except reraise:
        raise
    except Exception as exc:
        if _strict_mode():
            raise RuntimeError(
                f"batch_continue: exception in [{context}] (re-raised because ITDOC_STRICT=1)"
            ) from exc
        _log.debug(
            "batch_continue: skipped [%s] — %s: %s",
            context,
            type(exc).__name__,
            exc,
        )
