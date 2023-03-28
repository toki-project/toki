"""Type expressions definition."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Union

import metadsl

# Expressions definition


def constructor(fn: Callable):
    """Decorator for expression constructor."""

    def _fn(*args, **kwargs):
        fn.__qualname__ = fn.__qualname__.split('.')[0]
        return metadsl.expression(fn)(*args, **kwargs)

    return _fn


@dataclass
class Expr(metadsl.Expression):
    """Base expression class."""

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        fn_name = (
            self.function.__name__
            if not str(self.function) == 'expr'
            else self._display_name
        )

        output = '{}({})'.format(fn_name, self.args)
        return output

    @property
    def _display_name(self) -> str:
        return self.__class__.__name__

    @staticmethod
    def expr(*args, **kwargs):
        """Create an expression with the given value."""
        raise NotImplementedError('Operation not supported yet.')


class Database(Expr):
    """Database expression."""


class DatabaseSchema(Expr):
    """Database schema expression."""


class TableSchema(Expr):
    """Table schema expression."""

    @staticmethod
    @constructor
    def expr(structure: Dict[str, Dict[str, Any]]) -> TableSchema:
        """
        Create a table schema expression from a dictionary.

        Parameters
        ----------
        structure : dict

        Returns
        -------
        TableSchema
        """

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


class TableBase(Expr):
    """Table base expression class."""

    def __getitem__(
        self, key: Union[str, List[str]]
    ) -> Union[Column, Projection]:
        """
        Get item from Table.

        Parameters
        ----------
        key : Union[str, list[str]]
            The key could be a string or a list of keys.

        Returns
        -------
        Projection or Column
            if the given ``key`` is a string, return is a Column
            if the given ``key`` is a list of string, return a Projection
        """
        if isinstance(key, str):
            if key not in self.schema.structure:
                raise TypeError('Column ``{}`` not found.'.format(key))
            _col_type = COLUMN_TYPE_MAP[self.schema.structure[key]['type']]
            # TODO: check a way to normalize this problem
            expr = _col_type.expr(self, key)  # type: ignore
        else:
            cols_not_found = []
            for k in key:
                if k not in self.schema.structure:
                    cols_not_found += [k]
            if cols_not_found:
                raise TypeError(
                    'Columns {} not found.\n'.format(str(cols_not_found))
                )
            expr = self._get_columns(key)
        return expr

    @metadsl.expression
    def _get_columns(self: TableBase, keys: List[str]) -> Projection:
        """
        Get columns projection for the given keys.

        Parameters
        ----------
        keys : list[str]

        Returns
        -------
        Projection
        """

    @metadsl.expression
    def __add__(self, other: Union[int, float]) -> TableBase:
        """
        Add a number to a table expression.

        Parameters
        ----------
        other : int or float

        Returns
        -------
        TableBase
        """

    @metadsl.expression
    def __truediv__(self, other: Union[int, float]) -> TableBase:
        """
        Divide a table expression by a given number.

        Parameters
        ----------
        other : int or float

        Returns
        -------
        TableBase
        """

    @metadsl.expression
    def __floordiv__(self, other: Union[int, float]) -> TableBase:
        """
        Divide a table expression by a given number.

        The result should be truncated to the integer value.

        Parameters
        ----------
        other : int or float

        Returns
        -------
        TableBase
        """

    @metadsl.expression
    def __mod__(self, other: Union[int, float]) -> TableBase:
        """
        Calculate the modulus of table expression by a number.

        Parameters
        ----------
        other : int or float

        Returns
        -------
        TableBase
        """

    @metadsl.expression
    def __mul__(self, other: Union[int, float]) -> TableBase:
        """
        Multiply a number to a table expression.

        Parameters
        ----------
        other : int or float

        Returns
        -------
        TableBase
        """

    @metadsl.expression
    def __sub__(self, other: Union[int, float]) -> TableBase:
        """
        Subtract a number from a table expression.

        Parameters
        ----------
        other : int or float

        Returns
        -------
        TableBase
        """

    @metadsl.expression
    def __pow__(self, other: Union[int, float]) -> TableBase:
        """
        Calculate the power of the table expression to the given number.

        Parameters
        ----------
        other : int or float

        Returns
        -------
        TableBase
        """


class Table(TableBase):
    """Table expression class."""

    @staticmethod
    @constructor
    def expr(
        name: str,
        schema: TableSchema,
        database_name: Optional[str] = None,
        database_schema_name: Optional[str] = None,
    ) -> Table:
        """
        Create a table expression from a schema.

        Parameters
        ----------
        name : str
        schema : Schema
        database_name : str, optional, default None
        database_schema_name : str, optional, default None

        Returns
        -------
        Table
        """

    @property
    def name(self) -> str:
        return self.args[0]

    @property
    def schema(self) -> TableSchema:
        return self.args[1]

    @property
    def database_name(self) -> Optional[str]:
        return self.args[2]

    @property
    def database_schema_name(self) -> Optional[str]:
        return self.args[3]

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


class Projection(TableBase):
    """Collection of columns expression"""

    @staticmethod
    @constructor
    def expr(source: TableBase, columns: List[str],) -> Projection:
        """
        Create a projection expression for given table and columns name.

        Parameters
        ----------
        source : TableBase
        columns : list[str]

        Returns
        -------
        Projection
        """

    @property
    def source(self) -> Table:
        return self.args[0]

    @property
    def columns(self) -> Union[str, List[str]]:
        return self.args[1]

    @property
    def _display_name(self) -> str:
        return '{}[{}]'.format(self.__class__.__name__, str(self.columns))

    def __repr__(self) -> str:
        output = '{}\n'.format(self._display_name)
        for l in repr(self.source).split('\n'):
            output += '  {}\n'.format(l)
        return output


class Value(Expr):
    """Column expression."""

    @classmethod
    def expr(cls, input: Expr) -> Value:  # type: ignore
        """
        Create a value expression for given input.

        Parameters
        ----------
        input : Expr

        Returns
        -------
        Value
        """

        def _expr(input: Expr):
            ...

        _expr.__annotations__['return'] = cls.__name__
        _expr.__doc__ = cls.expr.__doc__
        _expr.__qualname__ = 'expr'
        _expr.__name__ = 'expr'
        _expr = constructor(_expr)

        return _expr(input)


class Column(Projection, Value):
    """Column expression."""

    rename: Optional[str] = None

    @staticmethod
    @constructor
    def expr(source: TableBase, column: str) -> Column:
        """
        Create a column projection expression for given table and column name.

        Parameters
        ----------
        source : TableBase
        column : str

        Returns
        -------
        Column
        """

    @property
    def _display_name(self) -> str:
        result = '{}[{}]'.format(self.__class__.__name__, str(self.columns))
        if self.rename:
            result += '(as {})'.format(self.rename)
        return result

    def name(self, name: str) -> Column:
        self.rename = name
        return self


class Scalar(Value):
    """Column expression."""


class AnyValue(Value):
    """Any value expression."""


class AnyScalar(Scalar, AnyValue):
    """Any scalar expression."""


class AnyColumn(Column, AnyValue):
    """Any column expression."""


class NumericValue(Value):
    """Numeric value expression."""


class NumericScalar(Scalar, NumericValue):
    """Numeric scalar expression."""


class NumericColumn(Column, NumericValue):
    """Numeric column expression."""


class BooleanValue(NumericValue):
    """Boolean value expression."""


class BooleanScalar(Scalar, BooleanValue):
    """Boolean scalar expression."""


class BooleanColumn(Column, BooleanValue):
    """Boolean column expression."""


class IntegerValue(NumericValue):
    """Integer value expression."""


class IntegerScalar(Scalar, IntegerValue):
    """Integer scalar expression."""


class IntegerColumn(Column, IntegerValue):
    """Integer column expression."""

    @staticmethod
    @constructor
    def expr(source: TableBase, column: str) -> IntegerColumn:
        """
        Create an integer column projection expression.

        Parameters
        ----------
        source : TableBase
        column : str

        Returns
        -------
        IntegerColumn
        """


class FloatingValue(NumericValue):
    """Floating value expression."""


class FloatingScalar(Scalar, FloatingValue):
    """Floating scalar expression."""


class FloatingColumn(Column, FloatingValue):
    """Floating column expression."""


class DecimalValue(NumericValue):
    """Decimal value expression."""


class DecimalScalar(Scalar, DecimalValue):
    """Decimal scalar expression."""


class DecimalColumn(Column, DecimalValue):
    """Decimal column expression."""


class StringValue(Value):
    """String value expression."""


class StringScalar(Scalar, StringValue):
    """String scalar expression."""


class StringColumn(Column, StringValue):
    """String column expression."""


class TemporalValue(Value):
    """Temporal value expression."""


class TemporalScalar(Scalar, TemporalValue):
    """Temporal scalar expression."""


class TemporalColumn(Column, TemporalValue):
    """Temporal column expression."""


class DateValue(TemporalValue):
    """Date value expression."""


class DateScalar(Scalar, DateValue):
    """Date scalar expression."""


class DateColumn(Column, DateValue):
    """Date column expression."""


class TimeValue(TemporalValue):
    """Time value expression."""


class TimeScalar(Scalar, TimeValue):
    """Time scalar expression."""


class TimeColumn(Column, TimeValue):
    """Time column expression."""


class TimestampValue(TemporalValue):
    """Timestamp value expression."""


class TimestampScalar(Scalar, TimestampValue):
    """Timestamp scalar expression."""


class TimestampColumn(Column, TimestampValue):
    """Timestamp column expression."""


class PseudoColumn(Column):
    """Pseudo column expression."""


class RowID(PseudoColumn):
    """RowID pseudocolumn expression."""


# maps

COLUMN_TYPE_MAP = {
    # numerical
    'bool': BooleanColumn,
    'int': IntegerColumn,
    'int8': IntegerColumn,
    'int16': IntegerColumn,
    'int32': IntegerColumn,
    'int64': IntegerColumn,
    'float16': FloatingColumn,
    'float32': FloatingColumn,
    'float64': FloatingColumn,
    'decimal': DecimalColumn,
    # date and time
    'date': DateColumn,
    'time': TimeColumn,
    'timestamp': TimestampColumn,
    # pseudocolumn
    'rowid': RowID,
}
