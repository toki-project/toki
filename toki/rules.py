from typing import Callable

import metadsl_rewrite


class RegisterStrategy:
    """Registrer Strategy class for metadsl strategy."""

    _inner_strategy: list = []

    def register(self, fn: Callable):
        """Register a strategy."""

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
