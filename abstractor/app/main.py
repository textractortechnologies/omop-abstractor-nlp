from abstractor.app.dataclasses import *
from icecream import ic

app = FastAPI()


class Dispatcher:
    def get_abstraction_schema(self, meta_schema: AbstractionSchemaMeta) -> AbstractionSchema:
        ic(meta_schema.abstractor_abstraction_schema_uri)
        resp = requests.get(meta_schema.abstractor_abstraction_schema_uri)
        return AbstractionSchema(**resp.json()) if resp.ok is True else None


dispatcher = Dispatcher()


@app.get("/", status_code=201)
def greeting():
    return {"msg": "OMOP Abstractor NLP Service"}


@app.post("/multiple_suggest", status_code=201)
async def multiple_suggest(request: SuggestRequest = Body(...)):
    ic()
    for schema_meta in request.abstractor_abstraction_schemas:
        schema_uri = schema_meta.abstractor_abstraction_schema_uri
        ic(schema_uri)
        if schema_uri in schema_meta_cache:
            schema_meta_lookup = schema_meta_cache[schema_uri]
            if schema_meta.updated_at > schema_meta_lookup.updated_at:
                schema = schema_cache[schema_uri]
        else:
            schema = Dispatcher().get_abstraction_schema(schema_meta)
            ic(schema.predicate)
            if schema is None:
                raise Exception(
                    f"schema not found: {schema_meta.abstractor_abstraction_schema_uri}"
                )

        # TODO: async event handling

