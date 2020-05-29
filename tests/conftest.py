import pytest

from .backend_example import TokiExample


@pytest.fixture
def con():
    return TokiExample()
