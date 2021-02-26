from unittest.mock import patch, call
from icecream import ic
from fastapi.encoders import jsonable_encoder
import abstractor
import nlp_impl


@patch.object(
    abstractor.app.events.EventHandler,
    "submit_suggestion",
    name="mock_submit_suggestion",
)
@patch.object(
    abstractor.app.events.EventHandler,
    "get_abstraction_schema",
    name="mock_get_abstraction_schema",
)
def test_nlp_plugin(
    mock_get,
    mock_suggest,
    client,
    request_1,
    schema_1,
    schema_2,
    suggestion_1,
    suggestion_2,
):
    # block any currently resistered plugins
    for n in abstractor.app.events.plugin_manager.list_name_plugin():
        abstractor.app.events.plugin_manager.set_blocked(n[0])

    # register the test plugin
    abstractor.app.events.plugin_manager.register(nlp_impl)

    mock_get.side_effect = [schema_1, schema_2]
    mock_suggest.return_value = None

    response = client.post(
        "/multiple_suggest",
        json=jsonable_encoder(request_1),
    )
    assert response.status_code == 200
    assert response.json() == {"msg": "request accepted"}

    expected = [
        call.submit_suggestion(
            suggestion_1, request_1.abstractor_abstraction_schemas[0]
        ),
        call.submit_suggestion(
            suggestion_2, request_1.abstractor_abstraction_schemas[0]
        ),
        call.submit_suggestion(
            suggestion_1, request_1.abstractor_abstraction_schemas[1]
        ),
        call.submit_suggestion(
            suggestion_2, request_1.abstractor_abstraction_schemas[1]
        ),
    ]
    assert mock_suggest.mock_calls == expected
