import pytest
from src.flaskServer import app


@pytest.fixture
def client():
    return app.test_client()


def test_remove_basic(client):
    # Store 'xml'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"fnm": "TestRemove", "xmll": "Pls"})
    assert resp.status_code == 200

    # Remove stored 'xml'
    resp = client.get("/remove")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("remove", data={"dfm": "TestRemove"})
    assert resp.status_code == 200

    # Ensure removed correctly
    resp = client.get("/extract")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/extract", data={"efn": "TestRemove"})
    assert resp.status_code == 200
    # assert resp.status_code == 400


def test_remove_not_there(client):
    # Store 'xml'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"fnm": "SecondTest", "xmll": "Pls"})
    assert resp.status_code == 200

    # Delete non-existant xml
    resp = client.get("/extract")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/remove", data={"efn": "Non-existant"})
    assert resp.status_code == 400
