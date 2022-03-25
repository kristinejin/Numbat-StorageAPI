import pytest
from src.flask_server import app


@pytest.fixture
def client():
    return app.test_client()


def test_remove_basic(client):
    # Store 'xml'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": "TestRemove", "XML": "Pls", "Password": "test"})
    assert resp.status_code == 200

    # Remove stored 'xml'
    resp = client.get("/remove")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/remove", data={"FileName": "TestRemove", "Password": "test"})
    assert resp.status_code == 200

    # Ensure removed correctly
    resp = client.get("/extract")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/extract", data={"FileName": "TestRemove", "Password": "test"})
    assert resp.status_code == 400


def test_remove_not_there(client):
    # Store 'xml'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": "SecondTest", "XML": "Pls", "Password": "test"})
    assert resp.status_code == 200

    # Delete non-existant xml
    resp = client.get("/remove")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/remove", data={"FileName": "Non-existant", "Password": "test"})
    assert resp.status_code == 400

def test_remove_same_filename_different_password(client):
    # Store 'xml' with password 'test'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": "SecondTest", "XML": "Pls", "Password": "test"})
    assert resp.status_code == 200

    # Delete "SecondTest" using a different password
    resp = client.get("/remove")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/remove", data={"FileName": "SecondTest", "Password": "test2"})
    assert resp.status_code == 400

    # Check SecondTest with password test2 is gone
    resp = client.get("/extract")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/extract", data={"FileName": "SecondTest", "Password": "test2"})
    assert resp.status_code == 400

    # Check SecondTest with passwrod test is still in db
    resp = client.get("/extract")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/extract", data={"FileName": "SecondTest", "Password": "test2"})
    assert resp.status_code == 200

def test_remove_matching_filename(client):
    # Store 'xml' with password 'test'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": "SecondTest", "XML": "Pls", "Password": "test"})
    assert resp.status_code == 200

    # Store 'xml' with password 'test2'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": "SecondTest", "XML": "Pls", "Password": "test2"})
    assert resp.status_code == 200

    # Delete "SecondTest" using a different password
    resp = client.get("/remove")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/remove", data={"FileName": "SecondTest", "Password": "test2"})
    assert resp.status_code == 200

    # Check SecondTest under the password 'test' still exists
    resp = client.get("/extract")
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post("/extract", data={"FileName": "TestRemove", "Password": "test"})
    assert resp.status_code == 200
    