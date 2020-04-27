"""Tests for `toki.datatypes` module."""
import pytest

from toki import datatypes as dtypes

common_number_ops = [
    'add',
    'divmod',
    'eq',
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


@pytest.mark.parametrize(
    'n1', [dtypes.int8(1), dtypes.int16(1), dtypes.int32(1), dtypes.int64(1)]
)
@pytest.mark.parametrize('n2', [None, 1])
@pytest.mark.parametrize(
    'op', common_number_ops,
)
def test_int_ops(n1, n2, op):
    if n2 is None:
        n2 = n1

    result = getattr(n1, '__{}__'.format(op))(n2)
    assert isinstance(result, dtypes.DataType)


@pytest.mark.parametrize(
    'n1_type', [dtypes.float16, dtypes.float32, dtypes.float64],
)
@pytest.mark.parametrize(
    'n1_value', [1, 1.0],
)
@pytest.mark.parametrize('n2', [None, 1])
@pytest.mark.parametrize(
    'op', common_number_ops,
)
def test_float_ops(n1_type, n1_value, n2, op):
    n1 = n1_type(n1_value)

    if n2 is None:
        n2 = n1

    result = getattr(n1, '__{}__'.format(op))(n2)
    assert isinstance(result, dtypes.DataType)
