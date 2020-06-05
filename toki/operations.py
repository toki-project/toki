from __future__ import annotations

from toki import datatypes as dts
from toki import types as tps


class OperationExpr(tps.Expr):
    """Operation expression."""


class Add(OperationExpr):
    """Binary ``add`` operation."""

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
