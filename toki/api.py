"""Public API definition."""
from typing import Union

from toki import datatypes as dts
from toki import operations as ops
from toki import rules as rls
from toki import types as tps

# number


def _binop(name):
    T = getattr(ops, name)

    def _op(
        x: Union[int, float, dts.Number, tps.NumericValue],
        y: Union[int, float, dts.Number, tps.NumericValue],
    ) -> T:
        """Dispatch for ``{}`` between two numbers."""

    _op.__qualname__ = name.lower()
    _op.__name__ = name
    _op.__doc__ = _op.__doc__.format(name)
    return _op


int_types = [
    tps.IntegerValue,
    tps.IntegerColumn,
]

floating_types = [
    tps.FloatingValue,
    tps.FloatingColumn,
]

number_types = [dts.Number, tps.NumericValue] + int_types + floating_types


bin_op_maps = {
    'Add': 'add',
    'Subtract': 'sub',
    'Multiply': 'mul',
    'Divide': 'truediv',
    'FloorDivide': 'floordiv',
    'Power': 'pow',
    'Modulus': 'mod',
    # 'Equals': 'eq',
    'GreaterEqual': 'ge',
    'GreaterThan': 'gt',
    'LessEqual': 'le',
    'LessThan': 'lt',
    'NotEquals': 'ne',
}

reverble_ops = [
    'add',
    'sub',
    'mul',
    'truediv',
    'floordiv',
    'pow',
    'mod',
]

for tp in number_types:
    for class_name, method_name in bin_op_maps.items():
        op_modifies = ['']
        if method_name in reverble_ops:
            op_modifies = ['', 'r']

        for modify in op_modifies:
            rls.register(
                class_name,
                tp,
                '__{}{}__'.format(modify, method_name),
                _binop(class_name),
            )
