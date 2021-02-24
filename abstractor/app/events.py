import pluggy
import abstractor
from typing import Tuple
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from icecream import ic
from abstractor.app.dataclasses import *
from abstractor.nlp import hookspecs


def get_plugin_manager():
    pm = pluggy.PluginManager(abstractor.PROJECT_NAME)
    pm.add_hookspecs(hookspecs)
    pm.load_setuptools_entrypoints(abstractor.PROJECT_NAME)
    return pm


plugin_manager = get_plugin_manager()


class EventHandler:
    """
    EventHandler class
    Note: Gathering the event handing functions here makes it easier to test and mock
    this functionality
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

        # first check to see if schema is cached, and if so compare update times
        if schema_uri in EventHandler.schema_cache:
            m, s = EventHandler.schema_cache[schema_uri]
            if schema_metadata.updated_at <= m.updated_at:
                return s

        # fetch a new schema if we don't have a valid cached schema
        resp = requests.get(schema_uri)
        if resp.ok is True:
            s = AbstractionSchema(**resp.json())
            EventHandler.schema_cache[schema_uri] = (schema_metadata, s)
            return s

        # if we've gotten here, there's been an issue getting the schema
        raise HTTPException(status_code=404, detail=f"schema not found: {schema_uri}")

    @staticmethod
    def run_nlp(request: SuggestRequest, schema: AbstractionSchema) -> List[Suggestion]:
        """
        run_nlp
        :param request:
        :param schema:
        :return:
        """
        suggestions = plugin_manager.hook.extract_suggestions(
            text=request.text, schema=schema, sections=request.abstractor_sections
        )
        return suggestions[0]

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
            schema = EventHandler.get_abstraction_schema(schema_metadata)
            if schema is None:
                raise Exception(
                    f"schema not found: {schema_metadata.abstractor_abstraction_schema_uri}"
                )
            else:
                suggestions = EventHandler.run_nlp(request, schema)
                assert type(suggestions) == list
                for suggestion in suggestions:
                    EventHandler.submit_suggestion(suggestion, schema_metadata)
