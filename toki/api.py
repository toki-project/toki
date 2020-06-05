"""Public API definition."""
from typing import Union

from toki import datatypes as dts
from toki import operations as ops

# from toki import types as tps


def _number_add(
    x: Union[int, float, dts.Number], y: Union[int, float, dts.Number]
) -> ops.Add:
    """Dispatch for addition between two numbers."""


# tps.register('Add', dts.Number, '__add__', _number_add)
