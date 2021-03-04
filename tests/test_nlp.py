from unittest.mock import patch, call
from icecream import ic
from fastapi.encoders import jsonable_encoder
from abstractor.app.dataclasses import *
import datetime
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
        call(
            Suggestion(
                abstractor_abstraction_source_id=0,
                source_id=2049,
                source_type="NoteStableIdentifier",
                source_method="note_text",
                value="TODO",
                unknown=None,
                not_applicable=None,
                negated=False,
                suggestion_sources=[
                    SuggestionSource(
                        match_value="glioblastoma",
                        sentence_match_value="The patient has a diagnosis of glioblastoma.",
                        section_name="SPECIMEN",
                        section_name_begin=1,
                        section_name_end=25,
                    )
                ],
            ),
            AbstractionSchemaMetaData(
                abstractor_abstraction_schema_id=1,
                abstractor_abstraction_schema_uri="http://localhost:8000/abstractor_abstraction_schemas/schema-1.json",
                abstractor_abstraction_abstractor_suggestions_uri="http://localhost:8000/abstractor_abstractions/10577/abstractor_suggestions.json",
                abstractor_abstraction_id=10577,
                abstractor_abstraction_source_id=5403,
                abstractor_subject_id=5403,
                namespace_type="Abstractor::AbstractorNamespace",
                namespace_id=488,
                abstractor_rule_type="value",
                abstractor_object_type="list",
                updated_at=datetime.datetime(
                    2020, 10, 6, 20, 56, 40, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
        call(
            Suggestion(
                abstractor_abstraction_source_id=0,
                source_id=2049,
                source_type="NoteStableIdentifier",
                source_method="note_text",
                value="TODO",
                unknown=None,
                not_applicable=None,
                negated=False,
                suggestion_sources=[
                    SuggestionSource(
                        match_value="gbm",
                        sentence_match_value="GBM does not have a good prognosis.",
                        section_name="SPECIMEN",
                        section_name_begin=1,
                        section_name_end=25,
                    )
                ],
            ),
            AbstractionSchemaMetaData(
                abstractor_abstraction_schema_id=1,
                abstractor_abstraction_schema_uri="http://localhost:8000/abstractor_abstraction_schemas/schema-1.json",
                abstractor_abstraction_abstractor_suggestions_uri="http://localhost:8000/abstractor_abstractions/10577/abstractor_suggestions.json",
                abstractor_abstraction_id=10577,
                abstractor_abstraction_source_id=5403,
                abstractor_subject_id=5403,
                namespace_type="Abstractor::AbstractorNamespace",
                namespace_id=488,
                abstractor_rule_type="value",
                abstractor_object_type="list",
                updated_at=datetime.datetime(
                    2020, 10, 6, 20, 56, 40, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
        call(
            Suggestion(
                abstractor_abstraction_source_id=0,
                source_id=2049,
                source_type="NoteStableIdentifier",
                source_method="note_text",
                value="TODO",
                unknown=None,
                not_applicable=None,
                negated=False,
                suggestion_sources=[
                    SuggestionSource(
                        match_value="glioblastoma",
                        sentence_match_value="The patient has a diagnosis of glioblastoma.",
                        section_name="SPECIMEN",
                        section_name_begin=1,
                        section_name_end=25,
                    )
                ],
            ),
            AbstractionSchemaMetaData(
                abstractor_abstraction_schema_id=2,
                abstractor_abstraction_schema_uri="http://localhost:8000/abstractor_abstraction_schemas/schema-2.json",
                abstractor_abstraction_abstractor_suggestions_uri="http://localhost:8000/abstractor_abstractions/10578/abstractor_suggestions.json",
                abstractor_abstraction_id=10578,
                abstractor_abstraction_source_id=5404,
                abstractor_subject_id=5404,
                namespace_type="Abstractor::AbstractorNamespace",
                namespace_id=488,
                abstractor_rule_type="value",
                abstractor_object_type="list",
                updated_at=datetime.datetime(
                    2020, 10, 6, 20, 56, 42, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
        call(
            Suggestion(
                abstractor_abstraction_source_id=0,
                source_id=2049,
                source_type="NoteStableIdentifier",
                source_method="note_text",
                value="TODO",
                unknown=None,
                not_applicable=None,
                negated=False,
                suggestion_sources=[
                    SuggestionSource(
                        match_value="gbm",
                        sentence_match_value="GBM does not have a good prognosis.",
                        section_name="SPECIMEN",
                        section_name_begin=1,
                        section_name_end=25,
                    )
                ],
            ),
            AbstractionSchemaMetaData(
                abstractor_abstraction_schema_id=2,
                abstractor_abstraction_schema_uri="http://localhost:8000/abstractor_abstraction_schemas/schema-2.json",
                abstractor_abstraction_abstractor_suggestions_uri="http://localhost:8000/abstractor_abstractions/10578/abstractor_suggestions.json",
                abstractor_abstraction_id=10578,
                abstractor_abstraction_source_id=5404,
                abstractor_subject_id=5404,
                namespace_type="Abstractor::AbstractorNamespace",
                namespace_id=488,
                abstractor_rule_type="value",
                abstractor_object_type="list",
                updated_at=datetime.datetime(
                    2020, 10, 6, 20, 56, 42, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
    ]
    assert mock_suggest.mock_calls == expected
