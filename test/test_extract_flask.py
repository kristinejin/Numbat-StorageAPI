import pytest
import random
import string
from src.flask_server import app


@pytest.fixture
def client():
    return app.test_client()


def test_extract_basic(client):
    file_name = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    # Store 'xml'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"fnm": file_name, "xmll": "Pls"})
    assert resp.status_code == 200

    # Extract stored 'xml'
    resp = client.get("/extract")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/extract", data={"efn": file_name})
    assert resp.status_code == 200


def test_extract_not_there(client):
    file_name = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    # Store 'xml'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"fnm": file_name, "xmll": "Pls"})
    assert resp.status_code == 200

    # Extract stored 'xml'
    resp = client.get("/extract")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/extract", data={"efn": file_name + 'i'})
    assert resp.status_code == 200
    # assert resp.status_code == 400
