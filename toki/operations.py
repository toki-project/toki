from __future__ import annotations

from toki import datatypes as dts
from toki import types as tps


class OperationExpr(tps.Expr):
    """Operation expression."""


class BinaryOp(OperationExpr):
    """Binary base operation."""

    @property
    def left(self) -> dts.DataType:
        return self.args[0]

    @property
    def right(self) -> dts.DataType:
        return self.args[1]

    @staticmethod
    @tps.constructor
    def expr(left: dts.DataType, right: dts.DataType) -> Add:
        """Create an Add expression for the given parameters."""


class Add(BinaryOp):
    """Addition operation."""


class Subtract(BinaryOp):
    """Subtraction operation."""


class Multiply(BinaryOp):
    """Multiplication operation."""


class Divide(BinaryOp):
    """Division operation."""


class FloorDivide(BinaryOp):
    """Floor division operation."""


class Power(BinaryOp):
    """Power operation."""


class Modulus(BinaryOp):
    """Division operation."""
