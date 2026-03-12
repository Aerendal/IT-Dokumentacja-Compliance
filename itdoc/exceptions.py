"""itdoc.exceptions — hierarchia wyjątków pakietu."""


class ItDocError(Exception):
    """Bazowy wyjątek pakietu itdoc."""


class SchemaError(ItDocError):
    """Błąd schematu DB — brakująca tabela, brak wymaganych kolumn."""


class TemplateError(ItDocError):
    """Błąd szablonu — niepoprawny frontmatter, brak wymaganych sekcji."""


class QueryError(ItDocError):
    """Błąd zapytania — nieznany kod standardu/regulacji, niepoprawny doc_uid."""
