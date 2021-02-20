import os
import json
from pathlib import Path
from icecream import ic
from abstractor.app.main import app
from abstractor.app.dataclasses import *


dir_path = Path(os.path.dirname(os.path.realpath(__file__)))


@app.get("/abstractor_abstraction_schemas/{schema_id}", status_code=201)
async def get_abstraction_schema(schema_id: str) -> AbstractionSchema:
    ic(schema_id)
    json_text = Path(dir_path / "data/abstraction_schema.json").read_text()
    json_dict = json.loads(json_text)
    schema = AbstractionSchema(**json_dict)
    return schema