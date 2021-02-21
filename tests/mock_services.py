import os
import json
from pathlib import Path
from icecream import ic
from abstractor.app.main import app
from abstractor.app.dataclasses import *


dir_path = Path(os.path.dirname(os.path.realpath(__file__)))


@app.get("/abstractor_abstraction_schemas/{schema_id}", status_code=201)
async def get_abstraction_schema(schema_id: str) -> AbstractionSchema:
    json_text = Path(dir_path / "data/schema-0.json").read_text()
    json_dict = json.loads(json_text)
    schema = AbstractionSchema(**json_dict)
    ic(schema.predicate)
    return schema


@app.post(
    "/abstractor_abstractions/{abstractor_abstraction_id}/abstractor_suggestions.json",
    status_code=201,
)
async def get_abstraction_schema(abstractor_abstraction_id: int):
    ic(abstractor_abstraction_id)
