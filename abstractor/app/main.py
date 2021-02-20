from typing import List, Tuple, Dict
from abstractor.app.dataclasses import *
from icecream import ic

app = FastAPI()


class Dispatcher:
    # TODO: check out https://docs.python.org/dev/library/functools.html#functools.lru_cache
    schema_cache: Dict[str, Tuple[AbstractionSchemaMeta, AbstractionSchema]] = {}

    @staticmethod
    def get_abstraction_schema(meta_schema: AbstractionSchemaMeta) -> AbstractionSchema:
        schema_uri = meta_schema.abstractor_abstraction_schema_uri
        ic(schema_uri)
        if schema_uri in Dispatcher.schema_cache:
            meta, schema = Dispatcher.schema_cache[schema_uri]
            if meta.updated_at <= meta.updated_at:
                return schema

        resp = requests.get(meta_schema.abstractor_abstraction_schema_uri)
        return AbstractionSchema(**resp.json()) if resp.ok is True else None


@app.get("/", status_code=201)
def greeting():
    return {"msg": "OMOP Abstractor NLP Service"}


@app.post("/multiple_suggest", status_code=201)
async def multiple_suggest(request: SuggestRequest = Body(...)):
    for schema_meta in request.abstractor_abstraction_schemas:
        schema_uri = schema_meta.abstractor_abstraction_schema_uri
        ic(schema_uri)
        schema = Dispatcher.get_abstraction_schema(schema_meta)
        if schema is None:
            raise Exception(
                f"failed to get schema: {schema_meta.abstractor_abstraction_schema_uri}"
            )

        # TODO: async event handling

