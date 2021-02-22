import time
from typing import List, Tuple, Dict
from fastapi import FastAPI, BackgroundTasks, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from icecream import ic
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
        """
        get_abstraction_schema
        :param schema_metadata:
        :return:
        """
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
        """
        run_nlp
        :param request:
        :param schema:
        :return:
        """
        return []

    @staticmethod
    def submit_suggestion(
        suggestion: Suggestion, schema_metadata: AbstractionSchemaMetaData
    ) -> bool:
        """
        submit_suggestion
        :param suggestion:
        :param schema_metadata:
        :return:
        """
        suggest_uri = schema_metadata.abstractor_abstraction_abstractor_suggestions_uri
        resp = requests.post(suggest_uri, data=jsonable_encoder(suggestion))
        return resp.ok is True

    @staticmethod
    def handle_request(request: SuggestRequest) -> None:
        """
        handle_request
        :param request:
        :return:
        """
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
