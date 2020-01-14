import os
import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def dir_path() -> Path:
    return Path(os.path.dirname(os.path.realpath(__file__)))
