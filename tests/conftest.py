import pytest
from pathlib import Path
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture(scope="session")
def morph_file_path() -> Path:
    return Path(dir_path) / "../data/ICD-O-3_CSV-metadata/Morphenglish.txt"


@pytest.fixture(scope="session")
def topo_file_path() -> Path:
    return Path(dir_path) / "../data/ICD-O-3_CSV-metadata/Topoenglish.txt"
