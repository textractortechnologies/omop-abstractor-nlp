import pytest
import json
from starlette.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from unittest.mock import patch
from datetime import datetime as dt
from pathlib import Path
from abstractor.app.main import *


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="module")
def abstraction_schema(dir_path) -> AbstractionSchema:
    json_text = Path(dir_path / "data/abstraction_schema.json").read_text()
    json_dict = json.loads(json_text)
    schema = AbstractionSchema(**json_dict)
    return schema


@pytest.fixture(scope="session")
def suggest_request(dir_path) -> SuggestRequest:
    json_text = Path(dir_path / "data/suggest_request.json").read_text()
    json_dict = json.loads(json_text)
    request = SuggestRequest(**json_dict)
    return request


@pytest.fixture(scope="session")
def suggestion(dir_path) -> SuggestRequest:
    json_text = Path(dir_path / "data/suggestion.json").read_text()
    json_dict = json.loads(json_text)
    suggestion = Suggestion(**json_dict)
    return suggestion


@patch('services.requests.get')
def test_multiple_suggest(mock_get, client, suggest_request, suggestion):
    mock_get.return_value.ok = True

    response = client.post(
        "/multiple_suggest",
        json=jsonable_encoder(suggest_request),
    )
    assert response.status_code == 201
    assert response.json() is None

