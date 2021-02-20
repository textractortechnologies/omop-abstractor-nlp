from typing import List, Tuple, Dict
from abstractor.app.dataclasses import *
from icecream import ic

app = FastAPI()


class Dispatcher:
    # TODO: check out https://docs.python.org/dev/library/functools.html#functools.lru_cache
    schema_cache: Dict[str, Tuple[AbstractionSchemaMetaData, AbstractionSchema]] = {}

    @staticmethod
    def get_abstraction_schema(meta_schema: AbstractionSchemaMetaData) -> AbstractionSchema:
        schema_uri = meta_schema.abstractor_abstraction_schema_uri
        if schema_uri in Dispatcher.schema_cache:
            meta, schema = Dispatcher.schema_cache[schema_uri]
            if meta.updated_at <= meta.updated_at:
                return schema

        resp = requests.get(meta_schema.abstractor_abstraction_schema_uri)
        if resp.ok is True:
            schema = AbstractionSchema(**resp.json())
            Dispatcher.schema_cache[schema_uri] = (meta_schema, schema)
            return schema

        return None

    @staticmethod
    def nlp(request: SuggestRequest, schema: AbstractionSchema) -> List[Suggestion]:
        return []

    @staticmethod
    def submit_suggestion(suggestion: Suggestion, schema_metadata: AbstractionSchemaMetaData) -> None:
        pass


@app.get("/", status_code=201)
def greeting():
    return {"msg": "OMOP Abstractor NLP Service"}


@app.post("/multiple_suggest", status_code=201)
async def multiple_suggest(request: SuggestRequest = Body(...)):
    for schema_metadata in request.abstractor_abstraction_schemas:
        schema = Dispatcher.get_abstraction_schema(schema_metadata)
        ic(schema.predicate)
        if schema is None:
            raise Exception(
                f"failed to get schema: {schema_metadata.abstractor_abstraction_schema_uri}"
            )
        else:
            suggestions = Dispatcher.nlp(request, schema)
            ic(len(suggestions))
            for suggestion in suggestions:
                Dispatcher.submit_suggestion(suggestion, schema_metadata)
                ic(suggestion)


