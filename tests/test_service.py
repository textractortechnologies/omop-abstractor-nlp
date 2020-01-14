import pytest
from starlette.testclient import TestClient
from datetime import datetime
from abstractor.service.main import *

client = TestClient(app)


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
        updated_at=datetime.strptime("2019-12-16 13:07:50", "%Y-%m-%d %H:%M:%S"),
    )


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
        updated_at=datetime.strptime("2019-12-16 13:07:50", "%Y-%m-%d %H:%M:%S"),
    )


def test_multiple_suggest():
    pass
    # response=client.post(
    #     "/multiple_suggest",
    #     json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    # )
    # assert response.status_code == 201
    # assert response.json() == {}
