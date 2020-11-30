"""Tests for `toki.datatypes` module."""
import pytest

from toki import datatypes as dtypes

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


INT_TYPES = ('int8', 'int16', 'int32', 'int64')
FLOAT_TYPES = ('float16', 'float16', 'float64')
NUMBER_TYPES = INT_TYPES + FLOAT_TYPES


@pytest.mark.parametrize(
    'n1', [dtypes.int8(1), dtypes.int16(1), dtypes.int32(1), dtypes.int64(1)]
)
@pytest.mark.parametrize('n2', [None, 1])
@pytest.mark.parametrize(
    'op',
    common_number_ops,
)
def test_int_ops(con, n1, n2, op):
    if n2 is None:
        n2 = n1

    result = getattr(n1, '__{}__'.format(op))(n2)
    assert isinstance(result, dtypes.DataType)
    con.compile


@pytest.mark.parametrize(
    'n1_type',
    [dtypes.float16, dtypes.float32, dtypes.float64],
)
@pytest.mark.parametrize(
    'n1_value',
    [1, 1.0],
)
@pytest.mark.parametrize('n2', [None, 1])
@pytest.mark.parametrize(
    'op',
    common_number_ops,
)
def test_float_ops(n1_type, n1_value, n2, op):
    n1 = n1_type(n1_value)

    if n2 is None:
        n2 = n1

    result = getattr(n1, '__{}__'.format(op))(n2)
    assert isinstance(result, dtypes.DataType)


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

    assert con.compile(x_expr + y_expr) == '{} + {}'.format(x, y)
    assert con.compile(x_expr - y_expr) == '{} - {}'.format(x, y)
    assert con.compile(x_expr * y_expr) == '{} * {}'.format(x, y)
    assert con.compile(x_expr / y_expr) == '{} / {}'.format(x, y)
    assert con.compile(x_expr // y_expr) == '{} // {}'.format(x, y)
    assert con.compile(x_expr ** y_expr) == '{} ** {}'.format(x, y)
    assert con.compile(x_expr % y_expr) == '{} % {}'.format(x, y)
