import pytest
from starlette.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from datetime import datetime as dt
from abstractor.app.main import *


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="session")
def abstraction_schema() -> AbstractionSchema:
    return AbstractionSchema(
        abstractor_abstraction_schema_id=1184,
        abstractor_abstraction_schema_uri="https://schemas/1184.json",
        abstractor_abstraction_abstractor_suggestions_uri="https://abstractions/669/abstractor_suggestions.json",
        abstractor_abstraction_id=669,
        abstractor_abstraction_source_id=1374,
        abstractor_subject_id=1355,
        namespace_type="Abstractor::AbstractorNamespace",
        namespace_id=281,
        abstractor_rule_type="value",
        updated_at=dt.strptime("2019-12-16 13:07:50", "%Y-%m-%d %H:%M:%S"),
    )


@pytest.fixture(scope="session")
def suggest_request(abstraction_schema) -> SuggestRequest:
    return SuggestRequest(
        source_id=156,
        source_type="NoteStableIdentifier",
        source_method="note_text",
        abstractor_rules_uri="https://moomin.com/abstractor_rules.json",
        text="Looks like metastatic carcinoma to me.",
        abstractor_abstraction_schemas=[abstraction_schema],
    )


def test_multiple_suggest(client, suggest_request):
    # print(jsonable_encoder(suggest_request))
    response = client.post(
        "/multiple_suggest",
        json=jsonable_encoder(suggest_request),
    )
    assert response.status_code == 201
    assert response.json() is None
