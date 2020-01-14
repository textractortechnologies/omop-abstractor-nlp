from fastapi import FastAPI, Body
from pydantic import BaseModel
import datetime
from typing import List

app = FastAPI()


class AbstractionSchema(BaseModel):
    abstractor_abstraction_schema_id : int
    abstractor_abstraction_schema_uri: str
    abstractor_abstraction_abstractor_suggestions_uri: str
    abstractor_abstraction_id: int
    abstractor_abstraction_source_id: int
    abstractor_subject_id: int
    namespace_type: str
    namespace_id: int
    abstractor_rule_type: str
    updated_at: datetime.datetime


class SuggestRequest(BaseModel):
    source_id: int
    source_type: str
    source_method: str
    abstractor_rules_uri: str
    text: str
    abstractor_abstraction_schemas: List[AbstractionSchema] = []


@app.post("/multiple_suggest")
async def multiple_suggest(
        request: SuggestRequest = Body(...)
):
    return