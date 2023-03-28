"""Public API definition."""
from typing import Union

from toki import datatypes as dts
from toki import operations as ops
from toki import rules as rls
from toki import types as tps

# binary operations

int_types = [
    tps.IntegerValue,
    tps.IntegerColumn,
]

floating_types = [
    tps.FloatingValue,
    tps.FloatingColumn,
]

number_types = [dts.Number, tps.NumericValue] + int_types + floating_types
logical_types = [dts.Boolean, tps.BooleanValue]

REVERSIBLE_OPS = [
    'add',
    'and',
    'floordiv',
    'mod',
    'mul',
    'or' 'pow',
    'sub',
    'truediv',
    'xor',
]

generic_bin_ops = {
    # 'Equals': 'eq',
    'NotEquals': 'ne',
}

numeric_bin_ops = {
    'Add': 'add',
    'Subtract': 'sub',
    'Multiply': 'mul',
    'Divide': 'truediv',
    'FloorDivide': 'floordiv',
    'Power': 'pow',
    'Modulus': 'mod',
    'GreaterEqual': 'ge',
    'GreaterThan': 'gt',
    'LessEqual': 'le',
    'LessThan': 'lt',
}

logical_bin_ops = {'And': 'and', 'Or': 'or', 'Xor': 'Xor'}


def _binop_prepare(op_method, name):
    op_method.__qualname__ = name.lower()
    op_method.__name__ = name
    op_method.__doc__ = op_method.__doc__.format(name)
    return op_method


def _define_type_bin_methods(type_ref, ops_map, op_method):
    for tp in type_ref:
        for class_name, method_name in ops_map.items():
            op_modifies = ['']
            if method_name in REVERSIBLE_OPS:
                op_modifies = ['', 'r']

            for modify in op_modifies:
                rls.register(
                    class_name,
                    tp,
                    '__{}{}__'.format(modify, method_name),
                    op_method(class_name),
                )


def _create_bin_op_numeric(name):
    T = getattr(ops, name)

    def _op(
        x: Union[int, float, dts.Number, tps.NumericValue],
        y: Union[int, float, dts.Number, tps.NumericValue],
    ) -> T:
        """Dispatch for ``{}`` between two numbers."""

    return _binop_prepare(_op, name)


def _create_bin_op_logical(name):
    T = getattr(ops, name)

    def _op(
        x: Union[bool, dts.Boolean, tps.BooleanValue],
        y: Union[bool, dts.Boolean, tps.BooleanValue],
    ) -> T:
        """Dispatch for ``{}`` between two logical values."""

    return _binop_prepare(_op, name)


_define_type_bin_methods(number_types, numeric_bin_ops, _create_bin_op_numeric)
_define_type_bin_methods(
    logical_types, logical_bin_ops, _create_bin_op_logical
)
