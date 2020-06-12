"""Tests for `toki.datatypes` module."""
import pytest

from toki import datatypes as dtypes
from toki.backends.sql_standard import SQLStandard

from .common import NUMBER_TYPES

common_number_ops = [
    'add',
    'divmod',
    # 'eq',
    'ge',
    'gt',
    'le',
    'lt',
    'mod',
    'mul',
    'pow',
    'radd',
    'rdivmod',
    'rmod',
    'rmul',
    'rpow',
    'rsub',
    'sub',
]


@pytest.fixture
def con():
    return SQLStandard()


@pytest.mark.parametrize('tp_x', NUMBER_TYPES)
@pytest.mark.parametrize('tp_y', NUMBER_TYPES)
def test_compile(con, tp_x, tp_y):
    _dtype_x = getattr(dtypes, tp_x)
    _dtype_primitive_x = int if tp_x.startswith('int') else float
    x = _dtype_primitive_x(1)
    x_expr = _dtype_x(x)

    _dtype_y = getattr(dtypes, tp_y)
    _dtype_primitive_y = int if tp_y.startswith('int') else float

    y = _dtype_primitive_y(2)
    y_expr = _dtype_y(y)

    # import pdb; pdb.set_trace()

    assert con.compile(x_expr + y_expr) == '{} + {}'.format(x, y)
    assert con.compile(x_expr - y_expr) == '{} - {}'.format(x, y)
    assert con.compile(x_expr * y_expr) == '{} * {}'.format(x, y)
    assert con.compile(x_expr / y_expr) == '{} / {}'.format(x, y)
    assert con.compile(x_expr // y_expr) == '{} // {}'.format(x, y)
    assert con.compile(x_expr ** y_expr) == '{} ** {}'.format(x, y)
    assert con.compile(x_expr % y_expr) == '{} % {}'.format(x, y)
