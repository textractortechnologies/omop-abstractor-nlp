from fastapi import BackgroundTasks
from abstractor.app.events import *


app = FastAPI()


@app.get("/", status_code=201)
def greeting():
    """
    greeting
    :return:
    """
    return {"msg": "OMOP Abstractor NLP Service"}


@app.post("/multiple_suggest", status_code=201)
def multiple_suggest(background_tasks: BackgroundTasks, request: SuggestRequest):
    """
    multiple_suggest
    :param background_tasks:
    :param request:
    :return:
    """
    background_tasks.add_task(EventHandler.handle_request, request)
    return {"msg": f"request accepted"}
