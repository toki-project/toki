"""Public API definition."""
from typing import List, Union

from toki import datatypes as dts
from toki import operations as ops
from toki import rules as rls
from toki import types as tps

# from toki import types as tps

# table


def _projection_col(key: str) -> tps.Column:
    """Dispatch for getitem for a given string key."""


def _projection_cols(key: List[str]) -> tps.Projection:
    """Dispatch for getitem for a given string key."""


rls.register('Column', tps.TableBase, '__getitem__', _projection_col)
rls.register('Projection', tps.TableBase, '__getitem__', _projection_cols)

# number


def _binop(name):
    def _op(
        x: Union[int, float, dts.Number], y: Union[int, float, dts.Number]
    ) -> ops.Add:
        """Dispatch for ``{}`` between two numbers."""

    _op.__qualname__ = name.lower()
    _op.__name__ = name
    _op.__doc__ = _op.__doc__.format(name)
    return _op


rls.register('Add', dts.Number, '__add__', _binop('Add'))
rls.register('Subtract', dts.Number, '__sub__', _binop('Subtract'))
rls.register('Muliply', dts.Number, '__mul__', _binop('Multiply'))
rls.register('Divide', dts.Number, '__truediv__', _binop('Divide'))
rls.register('FloorDivide', dts.Number, '__floordiv__', _binop('FloorDivide'))
rls.register('Power', dts.Number, '__pow__', _binop('Power'))
rls.register('Modulus', dts.Number, '__mod__', _binop('Modulus'))
