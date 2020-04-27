import metadsl
import pandas as pd

from toki import datatypes as dtypes
from toki.backend import Backend, BackendTranslator


class TokiExampleTranslator(BackendTranslator):
    rules = metadsl.RulesRepeatFold()

    def translate(self, expr):
        result = metadsl.execute(expr)
        return result

    @rules.append
    @metadsl.rule
    def _add_int32(x: int, y: int):
        return (
            dtypes.int32(x) + dtypes.int32(y),
            lambda: dtypes.int32(x + y),
        )


class TokiExample(Backend):
    translator: BackendTranslator = TokiExampleTranslator

    def connect(self) -> None:
        ...

    def compile(self, expr) -> str:
        return self.translator(expr)

    def execute(self, expr) -> pd.DataFrame:
        request_str = self.compile(expr)
        print(request_str)
        return pd.DataFrame()
