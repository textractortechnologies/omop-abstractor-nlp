from abstractor.app.dataclasses import *

app = FastAPI()


@app.get("/", status_code=201)
def greeting():
    return {"msg": "OMOP Abstractor NLP Service"}


@app.post("/multiple_suggest", status_code=201)
async def multiple_suggest(request: SuggestRequest = Body(...)):
    for schema_meta in request.abstractor_abstraction_schemas:
        schema_uri = schema_meta.abstractor_abstraction_schema_uri
        if schema_uri in schema_meta_cache:
            schema_meta_lookup = schema_meta_cache[
                schema_meta.abstractor_abstraction_schema_uri
            ]
            if schema_meta.updated_at > schema_meta_lookup.updated_at:
                schema = schema_cache[schema_uri]
        else:
            resp = requests.get(schema_meta.abstractor_abstraction_schema_uri)
            if resp.ok is True:
                print(resp.json())

        # TODO: async event handling


def get_abstraction_schema(uri: str) -> AbstractionSchema:
    resp = requests.get(uri)
    if resp.ok is True:
        print(resp.json())
