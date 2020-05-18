import metadsl
import metadsl_rewrite
import pandas as pd

from toki import datatypes as dtypes
from toki.backend import Backend
from toki.types import Expr

#  TokiExampleTranslator(BackendTranslator):
register = metadsl_rewrite.register['toki-example']
compiler = metadsl_rewrite.register['toki-example-compile']


def translate(expr: Expr):
    result = metadsl.execute(expr)
    return result


@register
@metadsl_rewrite.rule
def _add_int32(x: int, y: int):
    return (
        dtypes.int32(x) + dtypes.int32(y),
        lambda: dtypes.int32(x + y),
    )


@metadsl.expression
def _compile(expr: Expr) -> str:
    ...


class TokiExample(Backend):
    # translator: BackendTranslator = TokiExampleTranslator

    def connect(self) -> None:
        ...

    def compile(self, expr) -> str:
        return translate(expr)

    def execute(self, expr) -> pd.DataFrame:
        request_str = self.compile(expr)
        print(request_str)
        return pd.DataFrame()
