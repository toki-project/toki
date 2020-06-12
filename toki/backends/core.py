"""Define the public toki API."""
from typing import Any, Protocol, Union

import pandas as pd

import toki


class Backend(Protocol):
    """Backend protocol."""

    def connect(self) -> None:
        """Connect to the backend."""

    def compile(self, expr: toki.types.Expr) -> Union[str, Any]:
        """
        Compile a toki expression.

        Parameters
        ----------
        expr : toki.types.Expr

        Returns
        -------
        Union[str, Any]
        """

    def execute(
        self, expr: toki.types.Expr
    ) -> Union[pd.DataFrame, str, int, float, bool, Any]:
        """
        Execute a toki expression.

        Parameters
        ----------
        expr : toki.types.Expr

        Returns
        -------
        Union[pd.DataFrame, str, int, float, bool, Any]
        """


class BackendTranslator(Protocol):
    """Backend translator protocol."""

    def translate(self, expr: toki.types.Expr) -> Union[str, Any]:
        """
        Translate a toki expression.

        Parameters
        ----------
        expr : toki.types.Expr

        Returns
        -------
        Union[str, Any]
        """
