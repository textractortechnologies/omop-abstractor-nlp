import pluggy
import requests
import textabstractor
from typing import Tuple, Dict, List
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from textabstractor.nlp import hookspecs
from textabstractor.app.dataclasses import (
    AbstractionSchema,
    AbstractionSchemaMetaData,
    Suggestion,
    SuggestRequest,
)


def get_plugin_manager():
    """ """
    pm = pluggy.PluginManager(textabstractor.__project_name__)
    pm.add_hookspecs(hookspecs)
    pm.load_setuptools_entrypoints(textabstractor.__project_name__)
    return pm


plugin_manager = get_plugin_manager()


class EventHandler:
    """EventHandler class
    Note: Gathering the event handing functions here makes it easier to test and mock
    this functionality

    Parameters
    ----------

    Returns
    -------

    """

    schema_cache: Dict[str, Tuple[AbstractionSchemaMetaData, AbstractionSchema]] = {}

    @staticmethod
    def get_abstraction_schema(
        schema_metadata: AbstractionSchemaMetaData,
    ) -> AbstractionSchema:
        """get_abstraction_schema

        Parameters
        ----------
        schema_metadata :
            return:
        schema_metadata: AbstractionSchemaMetaData :


        Returns
        -------

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
    def run_nlp(
        request: SuggestRequest, schema: AbstractionSchema, schema_idx: int
    ) -> List[Suggestion]:
        """run_nlp

        Parameters
        ----------
        request :
            param schema:
        request: SuggestRequest :

        schema: AbstractionSchema :

        schema_idx: int :


        Returns
        -------

        """
        suggestion_source_dicts = plugin_manager.hook.extract_suggestions(
            request=request, schema=schema, schema_idx=schema_idx
        )
        suggestions = []
        for suggestion_source_dict in suggestion_source_dicts:
            for k, v in suggestion_source_dict.items():
                suggestion = Suggestion(
                    abstractor_abstraction_source_id=request.abstractor_abstraction_schemas[
                        schema_idx
                    ].abstractor_abstraction_source_id,
                    source_id=request.source_id,
                    source_type=request.source_type,
                    source_method=request.source_method,
                    value=k,
                    suggestion_sources=v,
                )
                suggestions.append(suggestion)
        return suggestions

    @staticmethod
    def submit_suggestion(
        suggestion: Suggestion, schema_metadata: AbstractionSchemaMetaData
    ) -> bool:
        """submit_suggestion

        Parameters
        ----------
        suggestion :
            param schema_metadata:
        suggestion: Suggestion :

        schema_metadata: AbstractionSchemaMetaData :


        Returns
        -------

        """
        suggest_uri = schema_metadata.abstractor_abstraction_abstractor_suggestions_uri
        resp = requests.post(suggest_uri, json=jsonable_encoder(suggestion))
        return resp.ok is True

    @staticmethod
    def handle_request(request: SuggestRequest) -> None:
        """handle_request

        Parameters
        ----------
        request :
            return:
        request: SuggestRequest :


        Returns
        -------

        """
        for idx, schema_metadata in enumerate(request.abstractor_abstraction_schemas):
            schema = EventHandler.get_abstraction_schema(schema_metadata)
            suggestions = EventHandler.run_nlp(request, schema, idx)
            assert type(suggestions) == list
            for e in suggestions:
                assert isinstance(e, Suggestion)
            for suggestion in suggestions:
                EventHandler.submit_suggestion(suggestion, schema_metadata)
