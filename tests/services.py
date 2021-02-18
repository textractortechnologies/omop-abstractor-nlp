from urllib.parse import urljoin
import requests
from fastapi import FastAPI
from abstractor.app.dataclasses import *


app = FastAPI()


BASE_URL = 'http://jsonplaceholder.typicode.com'

TODOS_URL = urljoin(BASE_URL, 'todos')


def get_todos() -> requests.models.Response:
    response = requests.get(TODOS_URL)
    if response.ok:
        return response
    else:
        return None


# TODO: create an abstraction schema test service
@app.get("/abstraction_schema/{uri}", status_code=201)
async def get_abstraction_schema(uri: str) -> AbstractionSchema:
    print(uri)
    schema = AbstractionSchema(
        predicate="pred",
        display_name="display_name",
        abstractor_object_type="type",
        preferred_name="preferred_name",
        predicate_variants=[]
    )
    return schema
