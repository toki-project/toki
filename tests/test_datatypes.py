"""Tests for `toki.datatypes` module."""
import pytest

from toki import datatypes as dtypes

from .common import numeric_ops_map


@pytest.mark.parametrize(
    'n1', [dtypes.int8(1), dtypes.int16(1), dtypes.int32(1), dtypes.int64(1)]
)
@pytest.mark.parametrize('n2', [None, 1])
@pytest.mark.parametrize(
    'op', numeric_ops_map.items(),
)
def test_int_ops(n1, n2, op):
    op_name, op_class = op

    if n2 is None:
        n2 = n1

    result = getattr(n1, '__{}__'.format(op_name))(n2)
    assert isinstance(result, op_class)


@pytest.mark.parametrize(
    'n1_type', [dtypes.float16, dtypes.float32, dtypes.float64],
)
@pytest.mark.parametrize(
    'n1_value', [1, 1.0],
)
@pytest.mark.parametrize('n2', [None, 1])
@pytest.mark.parametrize(
    'op', numeric_ops_map.items(),
)
def test_float_ops(n1_type, n1_value, n2, op):
    op_name, op_class = op
    n1 = n1_type(n1_value)

    if n2 is None:
        n2 = n1

    result = getattr(n1, '__{}__'.format(op_name))(n2)
    assert isinstance(result, op_class)
