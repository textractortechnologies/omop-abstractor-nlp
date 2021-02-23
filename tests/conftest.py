import os
import pytest
import yaml
import json
from pathlib import Path
from starlette.testclient import TestClient
from abstractor.app.dataclasses import *
from abstractor.app.main import app


dir_path = Path(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture(scope="session")
def config():
    config_file = dir_path / "config.yml"
    with open(config_file) as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
        return conf


@pytest.fixture(scope="module")
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="session")
def schema_0() -> AbstractionSchema:
    json_text = Path(dir_path / "data/schema-0.json").read_text()
    json_dict = json.loads(json_text)
    schema = AbstractionSchema(**json_dict)
    return schema


@pytest.fixture(scope="session")
def schema_1() -> AbstractionSchema:
    json_text = Path(dir_path / "data/schema-1.json").read_text()
    json_dict = json.loads(json_text)
    schema = AbstractionSchema(**json_dict)
    return schema


@pytest.fixture(scope="session")
def schema_2() -> AbstractionSchema:
    json_text = Path(dir_path / "data/schema-2.json").read_text()
    json_dict = json.loads(json_text)
    schema = AbstractionSchema(**json_dict)
    return schema


@pytest.fixture(scope="session")
def request_1() -> SuggestRequest:
    json_text = Path(dir_path / "data/request-1.json").read_text()
    json_dict = json.loads(json_text)
    request = SuggestRequest(**json_dict)
    return request


@pytest.fixture(scope="session")
def suggestion_1() -> SuggestRequest:
    json_text = Path(dir_path / "data/suggestion-1.json").read_text()
    json_dict = json.loads(json_text)
    suggestion = Suggestion(**json_dict)
    return suggestion


@pytest.fixture(scope="session")
def suggestion_2() -> SuggestRequest:
    json_text = Path(dir_path / "data/suggestion-2.json").read_text()
    json_dict = json.loads(json_text)
    suggestion = Suggestion(**json_dict)
    return suggestion
