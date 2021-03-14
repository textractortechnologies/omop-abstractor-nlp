from fastapi import BackgroundTasks, FastAPI
from abstractor.app.events import *
from abstractor.app.dataclasses import *


app = FastAPI()


@app.get("/", status_code=200)
def greeting():
    """greeting
    :return:

    Parameters
    ----------

    Returns
    -------

    """
    return {"msg": "OMOP Abstractor NLP Service"}


@app.post("/multiple_suggest", status_code=200)
def multiple_suggest(background_tasks: BackgroundTasks, request: SuggestRequest):
    """multiple_suggest

    Parameters
    ----------
    background_tasks :
        param request:
    background_tasks: BackgroundTasks :

    request: SuggestRequest :


    Returns
    -------

    """
    background_tasks.add_task(EventHandler.handle_request, request)
    return {"msg": f"request accepted"}


@app.get(
    "/abstractor_abstraction_schemas/{schema_id}",
    status_code=200,
    response_model=AbstractionSchema,
)
def get_abstraction_schema_stub(schema_id: str) -> AbstractionSchema:
    """

    Parameters
    ----------
    schema_id: str :


    Returns
    -------

    """
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
    status_code=200,
)
def accept_suggestion_stub(abstractor_abstraction_id: int, suggestion: Suggestion):
    """

    Parameters
    ----------
    abstractor_abstraction_id: int :

    suggestion: Suggestion :


    Returns
    -------

    """
    return {"msg": f"accepted suggestion {suggestion.abstractor_abstraction_source_id}"}
