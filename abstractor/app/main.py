from fastapi import BackgroundTasks
from abstractor.app.events import *
from abstractor.app.dataclasses import *


app = FastAPI()


@app.get("/", status_code=201)
def greeting():
    """
    greeting
    :return:
    """
    return {"msg": "OMOP Abstractor NLP Service"}


@app.post("/multiple_suggest", status_code=201)
def multiple_suggest(background_tasks: BackgroundTasks, request: SuggestRequest):
    """
    multiple_suggest
    :param background_tasks:
    :param request:
    :return:
    """
    ic(request.source_id)
    background_tasks.add_task(EventHandler.handle_request, request)
    return {"msg": f"request accepted"}


@app.get(
    "/abstractor_abstraction_schemas/{schema_id}",
    status_code=201,
    response_model=AbstractionSchema,
)
def get_abstraction_schema_stub(schema_id: str) -> AbstractionSchema:
    ic(schema_id)
    return AbstractionSchema(
        predicate="foo",
        display_name="bar",
        abstractor_object_type="baz",
        preferred_name="bip",
        predicate_variants=[],
        object_values=[],
    )


@app.post(
    "/abstractor_abstractions/{abstractor_abstraction_id}/abstractor_suggestions.json",
    status_code=201,
)
def accept_suggestion_stub(abstractor_abstraction_id: int, suggestion: Suggestion):
    ic(abstractor_abstraction_id)
    return {"msg": f"accepted suggestion {suggestion.abstractor_abstraction_source_id}"}
