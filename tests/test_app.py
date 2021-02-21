import pytest
from unittest.mock import patch, call
from starlette.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from abstractor.app.main import EventHandler
from mock_services import *
import abstractor


dir_path = Path(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture(scope="module")
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="module")
def schema_0() -> AbstractionSchema:
    json_text = Path(dir_path / "data/schema-0.json").read_text()
    json_dict = json.loads(json_text)
    schema = AbstractionSchema(**json_dict)
    return schema


@pytest.fixture(scope="module")
def schema_1() -> AbstractionSchema:
    json_text = Path(dir_path / "data/schema-1.json").read_text()
    json_dict = json.loads(json_text)
    schema = AbstractionSchema(**json_dict)
    return schema


@pytest.fixture(scope="module")
def schema_2() -> AbstractionSchema:
    json_text = Path(dir_path / "data/schema-2.json").read_text()
    json_dict = json.loads(json_text)
    schema = AbstractionSchema(**json_dict)
    return schema


@pytest.fixture(scope="module")
def request_1() -> SuggestRequest:
    json_text = Path(dir_path / "data/request-1.json").read_text()
    json_dict = json.loads(json_text)
    request = SuggestRequest(**json_dict)
    return request


@pytest.fixture(scope="module")
def suggestion_1() -> SuggestRequest:
    json_text = Path(dir_path / "data/suggestion-1.json").read_text()
    json_dict = json.loads(json_text)
    suggestion = Suggestion(**json_dict)
    return suggestion


@pytest.fixture(scope="module")
def suggestion_2() -> SuggestRequest:
    json_text = Path(dir_path / "data/suggestion-2.json").read_text()
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


@patch.object(
    abstractor.app.main.EventHandler, "submit_suggestion", name="mock_submit_suggestion"
)
@patch.object(abstractor.app.main.EventHandler, "run_nlp", name="mock_run_nlp")
@patch.object(
    abstractor.app.main.EventHandler,
    "get_abstraction_schema",
    name="mock_get_abstraction_schema",
)
def test_multiple_suggest(
    mock_get,
    mock_nlp,
    mock_suggest,
    client,
    request_1,
    schema_1,
    schema_2,
    suggestion_1,
    suggestion_2,
):

    mock_get.side_effect = [schema_1, schema_2]
    mock_nlp.side_effect = [[suggestion_1], [suggestion_2]]
    mock_suggest.return_value = None

    response = client.post(
        "/multiple_suggest",
        json=jsonable_encoder(request_1),
    )

    assert response.status_code == 201
    assert response.json() == {"msg": "request accepted"}

    mock_get.assert_called()
    expected = [
        call.get_abstraction_schema(request_1.abstractor_abstraction_schemas[0]),
        call.get_abstraction_schema(request_1.abstractor_abstraction_schemas[1]),
    ]
    assert mock_get.mock_calls == expected

    mock_nlp.assert_called()
    expected = [call.run_nlp(request_1, schema_1), call.run_nlp(request_1, schema_2)]
    assert mock_nlp.mock_calls == expected

    mock_suggest.assert_called()
    expected = [
        call.submit_suggestion(
            suggestion_1, request_1.abstractor_abstraction_schemas[0]
        ),
        call.submit_suggestion(
            suggestion_2, request_1.abstractor_abstraction_schemas[1]
        ),
    ]
    assert mock_suggest.mock_calls == expected
