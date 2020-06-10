"""Strategy rules mechanism module."""
from typing import Callable

import metadsl
import metadsl_rewrite
from metadsl_core.strategies import register_core


class RegisterStrategy:
    """Registrer Strategy class for metadsl strategy."""

    _inner_strategy: list = []

    def register(self, fn: Callable):
        """
        Register a strategy.

        Parameters
        ----------
        fn : Callable
        """
        self._inner_strategy.append(fn)

    def get_rules(self) -> metadsl_rewrite.StrategyRepeat:
        """
        Get a set of registered rules.

        Returns
        -------
        metadsl_rewrite.StrategyRepeat
        """
        inner_strategy = metadsl_rewrite.StrategySequence(
            *self._inner_strategy
        )
        return metadsl_rewrite.StrategyRepeat(
            metadsl_rewrite.StrategyFold(inner_strategy)
        )


def register(
    name: str,
    klass: metadsl.Expression,
    f_source_name: str,
    f_target: Callable,
):
    """
    Register a function expression.

    Parameters
    ----------
    name : str
    klass : metadsl.Expression
    f_source_name : str
    f_target : Callable
    """
    f_target.__qualname__ = name
    setattr(klass, f_source_name, metadsl.expression(f_target))


def rewrite(fn: Callable):
    """
    Register a function expression.

    Parameters
    ----------
    fn : Callable
    """
    register_core(metadsl_rewrite.rule(fn))
