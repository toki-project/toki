"""Data types definition."""
from __future__ import annotations

from typing import Union

import metadsl

from toki.types import Expr

# datatype classes


class DataType(Expr):
    """Main data type class."""


class Boolean(DataType):
    """Boolean data type expression."""


class Number(DataType):
    """Number data type expression."""

    @metadsl.expression
    def __add__(self, other: Union[Number, int, float]) -> Number:
        """Define ``add`` expression."""

    @metadsl.expression
    def __div__(self, other: Union[Number, int, float]) -> Number:
        """Define ``div`` expression."""

    @metadsl.expression
    def __divmod__(self, other: Union[Number, int, float]) -> Number:
        """Define ``divmod`` expression."""

    # note: maybe other should be Union[Number, int, float]
    @metadsl.expression
    def __eq__(self, other: Number) -> Number:
        """Define ``eq`` expression."""

    @metadsl.expression
    def __floordiv__(self, other: Union[Number, int, float]) -> Number:
        """Define ``floordiv`` expression."""

    @metadsl.expression
    def __ge__(  # type: ignore
        self, other: Union[Number, int, float]
    ) -> Boolean:
        """Define ``ge`` expression."""

    @metadsl.expression
    def __gt__(  # type: ignore
        self, other: Union[Number, int, float]
    ) -> Boolean:
        """Define ``gt`` expression."""

    @metadsl.expression
    def __le__(self, other: Union[Number, int, float]) -> Boolean:
        """Define ``le`` expression."""

    @metadsl.expression
    def __lt__(self, other: Union[Number, int, float]) -> Boolean:
        """Define ``lt`` expression."""

    @metadsl.expression
    def __mod__(self, other: Union[Number, int, float]) -> Number:
        """Define ``mod`` expression."""

    @metadsl.expression
    def __mul__(self, other: Union[Number, int, float]) -> Number:
        """Define ``mul`` expression."""

    @metadsl.expression
    def __pow__(self, other: Union[Number, int, float]) -> Number:
        """Define ``pow`` expression."""

    @metadsl.expression
    def __radd__(self, other: Union[Number, int, float]) -> Number:
        """Define ``radd`` expression."""

    @metadsl.expression
    def __rdivmod__(self, other: Union[Number, int, float]) -> Number:
        """Define ``rdivmod`` expression."""

    @metadsl.expression
    def __rmod__(self, other: Union[Number, int, float]) -> Number:
        """Define ``rmod`` expression."""

    @metadsl.expression
    def __rmul__(self, other: Union[Number, int, float]) -> Number:
        """Define ``rmul`` expression."""

    @metadsl.expression
    def __rpow__(self, other: Union[Number, int, float]) -> Number:
        """Define ``rpow`` expression."""

    @metadsl.expression
    def __rsub__(  # type: ignore
        self, other: Union[Number, int, float]
    ) -> Number:
        """Define ``rsub`` expression."""

    @metadsl.expression
    def __sub__(self, other: Union[Number, int, float]) -> Number:
        """Define ``sub`` expression."""

    @metadsl.expression
    def __truediv__(self, other: Union[Number, int, float]) -> Number:
        """Define ``truediv`` expression."""


class Integer(Number):
    """Integer number data type expression."""


class SignedInteger(Integer):
    """Signed integer number data type expression."""


class Int8(SignedInteger):
    """Int8 data type expression."""


class Int16(SignedInteger):
    """Int16 data type expression."""


class Int32(SignedInteger):
    """Int32 data type expression."""


class Int64(SignedInteger):
    """Int64 data type expression."""


class Floating(Number):
    """Floating number data type expression."""


class Float16(Floating):
    """Float16 data type expression."""


class Float32(Floating):
    """Float32 data type expression."""


class Float64(Floating):
    """Float64 data type expression."""


# datatype function


@metadsl.expression
def int8(x: int) -> Int8:
    """
    Define int8 expression.

    Parameters
    ----------
    x : int

    Returns
    -------
    Int8
    """


@metadsl.expression
def int16(x: int) -> Int16:
    """
    Define int16 expression.

    Parameters
    ----------
    x : int

    Returns
    -------
    Int16
    """


@metadsl.expression
def int32(x: int) -> Int32:
    """
    Define int32 expression.

    Parameters
    ----------
    x : int

    Returns
    -------
    Int32
    """


@metadsl.expression
def int64(x: int) -> Int64:
    """
    Define int64 expression.

    Parameters
    ----------
    x : int

    Returns
    -------
    Int64
    """


@metadsl.expression
def float16(x: Union[int, float]) -> Float16:
    """
    Define float16 expression.

    Parameters
    ----------
    x : Union[int, float]

    Returns
    -------
    Float16
    """


@metadsl.expression
def float32(x: Union[int, float]) -> Float32:
    """
    Define float32 expression.

    Parameters
    ----------
    x : Union[int, float]

    Returns
    -------
    Float32
    """


@metadsl.expression
def float64(x: Union[int, float]) -> Float64:
    """
    Define float64 expression.

    Parameters
    ----------
    x : Union[int, float]

    Returns
    -------
    Float64
    """
