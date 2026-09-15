import os

import pytest


@pytest.fixture(autouse=True)
def _example_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("EXAMPLE_API_KEY", os.environ.get("EXAMPLE_API_KEY", "test-key"))
