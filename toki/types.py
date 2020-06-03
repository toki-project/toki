"""Type expressions definition."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

import metadsl

# Expressions definition


class Expr(metadsl.Expression):
    """Base expression class."""

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def _display_name(self) -> str:
        return self.__class__.__name__


class DatabaseExpr(Expr):
    """Database expression."""


class DatabaseSchemaExpr(Expr):
    """Database schema expression."""


@dataclass
class TableSchemaExpr(Expr):
    """Table schema expression."""

    @property
    def structure(self) -> dict:
        return self.args[0]

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        output = '{}\n'.format(self._display_name)
        for k, v in self.structure.items():
            output += '  {}: {}({})\n'.format(
                k, v['type'], 'nullale' if v['nullable'] else 'non-nullable'
            )
        return output


@dataclass
class TableExpr(Expr):
    """Table expression class."""

    @property
    def name(self) -> str:
        return self.args[0]

    @property
    def schema(self) -> TableSchemaExpr:
        return self.args[1]

    @property
    def database_name(self) -> Optional[str]:
        return self.args[2]

    @property
    def database_schema_name(self) -> Optional[str]:
        return self.args[3]

    @metadsl.expression
    def __getitem__(self, key: Union[str, List[str]]) -> SelectionExpr:
        """
        Get item from TableExpr.

        Parameters
        ----------
        key : Union[str, list[str]]
            The key could be a string or a list of keys.

        Returns
        -------
        SelectionExpr
        """

    @property
    def _display_name(self) -> str:
        return '{}{}{}'.format(
            '{}.'.format(self.database_name) if self.database_name else '',
            '{}.'.format(self.database_schema_name)
            if self.database_schema_name
            else '',
            self.name,
        )

    def __repr__(self) -> str:
        output = '{}: {}\n'.format(self._display_name, self.__class__.__name__)
        for k, v in self.schema.structure.items():
            output += '  {}: {}({})\n'.format(
                k, v['type'], 'nullale' if v['nullable'] else 'non-nullable'
            )
        return output


class SelectionExpr(TableExpr):
    """Collection of columns expression"""

    @property
    def source(self) -> TableExpr:
        return self.args[0]

    @property
    def projection(self) -> Union[str, List[str]]:
        return self.args[1]

    @property
    def _display_name(self) -> str:
        return self.__class__.__name__

    def __repr__(self) -> str:
        output = '{}[{}]\n'.format(self._display_name, str(self.projection))
        for l in repr(self.source).split('\n'):
            output += '  {}\n'.format(l)
        return output


class ValueExpr(Expr):
    """Column expression."""


class ColumnExpr(ValueExpr):
    """Column expression."""


class ScalarExpr(ValueExpr):
    """Column expression."""


class AnyValue(ValueExpr):
    """Any value expression."""


class AnyScalar(ScalarExpr, AnyValue):
    """Any scalar expression."""


class AnyColumn(ColumnExpr, AnyValue):
    """Any column expression."""


# expression factory


@metadsl.expression
def table_schema(structure: Dict[str, Dict[str, Any]]) -> TableSchemaExpr:
    """
    Create a table schema expression from a dictionary.

    Parameters
    ----------
    structure : dict

    Returns
    -------
    TableSchemaExpr
    """


@metadsl.expression
def table(
    name: str,
    schema: TableSchemaExpr,
    database_name: Optional[str] = None,
    database_schema_name: Optional[str] = None,
) -> TableExpr:
    """
    Create a table expression from a schema.

    Parameters
    ----------
    name : str
    schema : SchemaExpr
    database_name : str, optional, default None
    database_schema_name : str, optional, default None

    Returns
    -------
    TableExpr
    """
