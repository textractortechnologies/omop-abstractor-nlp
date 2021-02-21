import pytest
from starlette.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from unittest.mock import patch, MagicMock, create_autospec
from datetime import datetime as dt
from abstractor.app.main import *
import mock_services


def test_abstraction_schema_service():
    client = TestClient(mock_services.app)
    response = client.get(f"/abstractor_abstraction_schemas/{'1234.json'}")
    assert response.ok is True
    schema = AbstractionSchema(**response.json())
    ic(schema)
