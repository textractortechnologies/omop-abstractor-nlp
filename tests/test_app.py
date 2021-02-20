import os
import json
import pytest

from pathlib import Path
from unittest.mock import patch, create_autospec
from starlette.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from icecream import ic
from abstractor.app.main import *
from abstractor.app.dataclasses import *
from mock_services import *
import abstractor


dir_path = Path(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture(scope="module")
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="module")
def abstraction_schema() -> AbstractionSchema:
    json_text = Path(dir_path / "data/abstraction_schema.json").read_text()
    json_dict = json.loads(json_text)
    schema = AbstractionSchema(**json_dict)
    return schema


@pytest.fixture(scope="module")
def suggest_request() -> SuggestRequest:
    json_text = Path(dir_path / "data/suggest_request.json").read_text()
    json_dict = json.loads(json_text)
    request = SuggestRequest(**json_dict)
    return request


@pytest.fixture(scope="module")
def suggestion() -> SuggestRequest:
    json_text = Path(dir_path / "data/suggestion.json").read_text()
    json_dict = json.loads(json_text)
    suggestion = Suggestion(**json_dict)
    return suggestion


def test_smoke(client):
    response = client.get(f"/")
    assert response.ok is True
    assert response.json() == {"msg": "OMOP Abstractor NLP Service"}


def test_abstraction_schema_service(client):
    response = client.get(f"/abstractor_abstraction_schemas/{'1234.json'}")
    assert response.ok is True
    schema = AbstractionSchema(**response.json())
    assert schema is not None


def mock_get_abstraction_schema(uri: str) -> AbstractionSchema:
    json_text = Path(dir_path / "data/abstraction_schema.json").read_text()
    json_dict = json.loads(json_text)
    schema = AbstractionSchema(**json_dict)
    return schema


@patch("abstractor.app.main.Dispatcher")
def test_multiple_suggest(mock_dispatch, client, abstraction_schema, suggest_request):

    # mock_get.return_value = mock_get_abstraction_schema("1234")
    # mock_get = mock_get_abstraction_schema
    # dispatcher = create_autospec(abstractor.app.main.dispatcher, spec_set=True)
    # dispatcher.get_abstraction_schema = lambda x: abstraction_schema

    mock_dispatch.get_abstraction_schema = mock_get_abstraction_schema

    response = client.post(
        "/multiple_suggest",
        json=jsonable_encoder(suggest_request),
    )
    assert response.status_code == 201
    assert response.json() is None
