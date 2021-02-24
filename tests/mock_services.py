import os
import json
from pathlib import Path
from icecream import ic
from fastapi import HTTPException, BackgroundTasks, Depends
from abstractor.app.main import app
from abstractor.app.dataclasses import *


dir_path = Path(os.path.dirname(os.path.realpath(__file__)))

json_text = Path(dir_path / "data/schema-1.json").read_text()
schema_1 = AbstractionSchema(**json.loads(json_text))
json_text = Path(dir_path / "data/schema-2.json").read_text()
schema_2 = AbstractionSchema(**json.loads(json_text))


@app.post("/test_multiple_suggest", status_code=201)
def multiple_suggest(background_tasks: BackgroundTasks, request: SuggestRequest):
    return {"msg": f"request accepted"}


@app.get(
    "/abstractor_abstraction_schemas/{schema_id}",
    status_code=201,
    response_model=AbstractionSchema,
)
def get_abstraction_schema(schema_id: str) -> AbstractionSchema:
    if schema_id == "schema-1.json":
        return schema_1
    elif schema_id == "schema-2.json":
        return schema_2
    raise HTTPException(status_code=404, detail=f"schema not found: {schema_id}")


@app.post(
    "/abstractor_abstractions/{abstractor_abstraction_id}/abstractor_suggestions.json",
    status_code=201,
)
def accept_suggestion(abstractor_abstraction_id: int, suggestion: Suggestion):
    ic(abstractor_abstraction_id)
    return {"msg": f"accepted suggestion {suggestion.abstractor_abstraction_source_id}"}
