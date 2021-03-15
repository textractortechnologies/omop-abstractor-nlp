from unittest.mock import patch, call
from fastapi.encoders import jsonable_encoder
from tests.app.mock_services import *
import textabstractor


def test_smoke(client):
    response = client.get(f"/")
    assert response.ok is True
    assert response.json() == {"msg": "OMOP Abstractor NLP Service"}


def test_abstraction_schema_service(client):
    response = client.get(f"/abstractor_abstraction_schemas/{'schema-1.json'}")
    assert response.ok is True
    schema = AbstractionSchema(**response.json())
    assert schema is not None


def test_suggestion_service(client, suggestion_1, suggestion_2):
    response = client.post(
        f"/abstractor_abstractions/{suggestion_1.abstractor_abstraction_source_id}/abstractor_suggestions.json",
        json=jsonable_encoder(suggestion_1),
    )
    assert response.ok is True
    assert response.json() == {
        "msg": f"accepted suggestion {suggestion_2.abstractor_abstraction_source_id}"
    }

    response = client.post(
        f"/abstractor_abstractions/{suggestion_2.abstractor_abstraction_source_id}/abstractor_suggestions.json",
        json=jsonable_encoder(suggestion_2),
    )
    assert response.ok is True
    assert response.json() == {
        "msg": f"accepted suggestion {suggestion_2.abstractor_abstraction_source_id}"
    }


def test_test_multiple_suggest(client, request_1):
    response = client.post(
        "/test_multiple_suggest",
        json=jsonable_encoder(request_1),
    )
    assert response.ok is True
    assert response.json() == {"msg": "request accepted"}

    response = client.post(
        f"/test_multiple_suggest",
        json=jsonable_encoder(request_1),
    )
    assert response.ok is True
    assert response.json() == {"msg": "request accepted"}


@patch.object(
    textabstractor.app.events.EventHandler,
    "submit_suggestion",
    name="mock_submit_suggestion",
)
@patch.object(textabstractor.app.events.EventHandler, "run_nlp", name="mock_run_nlp")
@patch.object(
    textabstractor.app.events.EventHandler,
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
    assert response.status_code == 200
    assert response.json() == {"msg": "request accepted"}

    mock_get.assert_called()
    expected = [
        call.get_abstraction_schema(request_1.abstractor_abstraction_schemas[0]),
        call.get_abstraction_schema(request_1.abstractor_abstraction_schemas[1]),
    ]
    assert mock_get.mock_calls == expected

    mock_nlp.assert_called()
    expected = [
        call.run_nlp(request_1, schema_1, 0),
        call.run_nlp(request_1, schema_2, 1),
    ]
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
