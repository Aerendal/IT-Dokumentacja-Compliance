"""itdoc — biblioteka IT Dokumentacja.

Eksportuje publiczne API pakietu.

Przykład użycia:
    from itdoc.db import get_connection, validate_schema
    from itdoc.query import find_by_standard, get_contract
    from itdoc.template import load_template, validate_template
    from itdoc.anchor import to_anchor
"""

from itdoc.anchor import to_anchor
from itdoc.db import check_link_resolution_coverage, get_connection, validate_schema
from itdoc.exceptions import ItDocError, QueryError, SchemaError, TemplateError
from itdoc.query import (
    find_by_regulation,
    find_by_standard,
    get_contract,
    rhythm_downstream,
    rhythm_upstream,
)
from itdoc.template import get_required_sections, load_template, validate_template

__version__ = "0.1.0"

__all__ = [
    # anchor
    "to_anchor",
    # db
    "get_connection",
    "validate_schema",
    "check_link_resolution_coverage",
    # exceptions
    "ItDocError",
    "SchemaError",
    "TemplateError",
    "QueryError",
    # query
    "find_by_standard",
    "find_by_regulation",
    "get_contract",
    "rhythm_upstream",
    "rhythm_downstream",
    # template
    "load_template",
    "validate_template",
    "get_required_sections",
]
