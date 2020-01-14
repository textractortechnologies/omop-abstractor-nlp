from starlette.testclient import TestClient

from abstractor.service.main import app

client = TestClient(app)


def test_post():
    response = client.get("/")
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
