import pytest
from src.flaskServer import app


@pytest.fixture
def client():
    return app.test_client()


def test_extract_basic(client):
    # Store 'xml'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"fnm": "Test", "xmll": "Pls"})
    assert resp.status_code == 200

    # Extract stored 'xml'
    resp = client.get("/extract")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/extract", data={"efn": "Test"})
    assert resp.status_code == 200


def test_extract_not_there(client):
    # Store 'xml'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"fnm": "Test", "xmll": "Pls"})
    assert resp.status_code == 200

    # Extract stored 'xml'
    resp = client.get("/extract")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/extract", data={"efn": "No-name"})
    assert resp.status_code == 200
    # assert resp.status_code == 400

