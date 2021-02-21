import time
from typing import List, Tuple, Dict
from fastapi import FastAPI, BackgroundTasks
from icecream import ic
from abstractor.app.dataclasses import *

app = FastAPI()


@app.get("/", status_code=201)
def greeting():
    return {"msg": "OMOP Abstractor NLP Service"}


@app.post("/multiple_suggest", status_code=201)
def multiple_suggest(
    background_tasks: BackgroundTasks, request: SuggestRequest = Body(...)
):
    background_tasks.add_task(EventHandler.handle_request, request)
    return {"msg": f"request accepted"}


class EventHandler:
    """
    EventHandler
    """

    # TODO: check out https://docs.python.org/dev/library/functools.html#functools.lru_cache
    schema_cache: Dict[str, Tuple[AbstractionSchemaMetaData, AbstractionSchema]] = {}

    @staticmethod
    def get_abstraction_schema(
        schema_metadata: AbstractionSchemaMetaData,
    ) -> AbstractionSchema:
        schema_uri = schema_metadata.abstractor_abstraction_schema_uri
        if schema_uri in EventHandler.schema_cache:
            meta, schema = EventHandler.schema_cache[schema_uri]
            if meta.updated_at <= meta.updated_at:
                return schema

        resp = requests.get(schema_metadata.abstractor_abstraction_schema_uri)
        if resp.ok is True:
            schema = AbstractionSchema(**resp.json())
            EventHandler.schema_cache[schema_uri] = (schema_metadata, schema)
            return schema

        return None

    @staticmethod
    def run_nlp(request: SuggestRequest, schema: AbstractionSchema) -> List[Suggestion]:
        return []

    @staticmethod
    def submit_suggestion(
        suggestion: Suggestion, schema_metadata: AbstractionSchemaMetaData
    ) -> None:
        pass

    @staticmethod
    def handle_request(request: SuggestRequest) -> None:
        for schema_metadata in request.abstractor_abstraction_schemas:
            ic(schema_metadata.abstractor_abstraction_schema_id)
            schema = EventHandler.get_abstraction_schema(schema_metadata)
            if schema is None:
                raise Exception(
                    f"schema not found: {schema_metadata.abstractor_abstraction_schema_uri}"
                )
            else:
                suggestions = EventHandler.run_nlp(request, schema)
                ic(len(suggestions))
                for suggestion in suggestions:
                    EventHandler.submit_suggestion(suggestion, schema_metadata)
