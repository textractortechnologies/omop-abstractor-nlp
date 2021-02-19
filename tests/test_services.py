import pytest
from starlette.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from unittest.mock import patch
from datetime import datetime as dt
from abstractor.app.main import *
import services


def test_abstraction_schema_service():
    client = TestClient(services.app)
    response = client.get(f"/abstraction_schema/{'1234'}")
    assert response.ok is True
    schema = AbstractionSchema(**response.json())
    print(schema)
