from starlette.testclient import TestClient
from abstractor.app.main import *
import mock_services


def test_abstraction_schema_service():
    client = TestClient(mock_services.app)
    response = client.get(f"/abstractor_abstraction_schemas/{'1234.json'}")
    assert response.ok is True
    schema = AbstractionSchema(**response.json())


def test_suggestion_service():
    client = TestClient(mock_services.app)
    response = client.post(
        f"/abstractor_abstractions/{10578}/abstractor_suggestions.json"
    )
    assert response.ok is True
    ic(response)
