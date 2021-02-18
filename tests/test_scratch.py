import pytest
from starlette.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from unittest.mock import patch
from datetime import datetime as dt
from abstractor.app.main import *
import services

from services import get_todos


@patch('services.requests.get')
def test_getting_todos(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert response is not None
    assert response.ok is True


def test_abstraction_schema_service():
    client = TestClient(services.app)
    response = client.get(
        f"/abstraction_schema/{'1234'}"
    )
    assert response.ok is True
    schema = AbstractionSchema(**response.json())
    print(schema)