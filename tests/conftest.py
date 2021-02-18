import os
import pytest
import yaml
from pathlib import Path


@pytest.fixture(scope="session")
def dir_path() -> Path:
    return Path(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture(scope="session")
def config(base_path: Path):
    config_path = base_path / "config.yml"
    with open(base_path / "config.yml") as conf_file:
        conf = yaml.load(conf_file, Loader=yaml.FullLoader)
        return conf
