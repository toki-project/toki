"""Common variables and functions."""
from toki import operations as ops

INT_TYPES = ('int8', 'int16', 'int32', 'int64')
FLOAT_TYPES = ('float16', 'float16', 'float64')
NUMBER_TYPES = INT_TYPES + FLOAT_TYPES

numeric_ops_map = {
    'add': ops.Add,
    # 'divmod': ops.DivideModulus,
    # 'eq': ops.Equals,
    'ge': ops.GreaterEqual,
    'gt': ops.GreaterThan,
    'le': ops.LessEqual,
    'lt': ops.LessThan,
    'ne': ops.NotEquals,
    'mod': ops.Modulus,
    'mul': ops.Multiply,
    'pow': ops.Power,
    'radd': ops.Add,
    # 'rdivmod': ops.DivideModulus,
    'rmod': ops.Modulus,
    'rmul': ops.Multiply,
    'rpow': ops.Power,
    'rsub': ops.Subtract,
    'sub': ops.Subtract,
}
