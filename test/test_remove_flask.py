import pytest
from src.flask_server import app
from test.xml_str import xml_as_string
import random
import string


@pytest.fixture
def client():
    app.config['Debug'] = True
    return app.test_client()


def test_remove_basic(client):
    file_name = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    password = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    # Store 'xml'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": file_name, "XML": xml_as_string, "Password": password})
    assert resp.status_code == 200

    # Remove stored 'xml'
    resp = client.get("/remove")
    assert resp.status_code == 200
    resp = client.post("/remove", data={"FileName": file_name, "Password": password})
    assert resp.status_code == 200

    # Ensure removed correctly
    resp = client.get("/extract")
    assert resp.status_code == 200
    resp = client.post("/extract", data={"FileName": file_name, "Password": password})
    assert resp.status_code == 400


def test_remove_not_there(client):
    file_name = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    password = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    # Store 'xml'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": file_name, "XML": xml_as_string, "Password": password})
    assert resp.status_code == 200

    # Delete non-existant xml
    resp = client.get("/remove")
    assert resp.status_code == 200
    resp = client.post("/remove", data={"FileName": "Non-existant", "Password": password})
    assert resp.status_code == 400

def test_remove_same_filename_different_password(client):
    file_name = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    password = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    password2 = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))

    # Store 'xml' with password 'test'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": file_name, "XML": xml_as_string, "Password": password})
    assert resp.status_code == 200

    # Delete file_name using a different password
    resp = client.get("/remove")
    assert resp.status_code == 200
    resp = client.post("/remove", data={"FileName": file_name, "Password": password2})
    assert resp.status_code == 400

    # Check SecondTest with password test2 is gone
    resp = client.get("/extract")
    assert resp.status_code == 200
    resp = client.post("/extract", data={"FileName": file_name, "Password": password2})
    assert resp.status_code == 400

    # Check SecondTest with passwrod test is still in db
    resp = client.get("/extract")
    assert resp.status_code == 200
    resp = client.post("/extract", data={"FileName": file_name, "Password": password})
    assert resp.status_code == 200

def test_remove_matching_filename(client):
    file_name = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    password = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    password2 = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))

    # Store 'xml' with password 'test'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": file_name, "XML": xml_as_string, "Password": password})
    assert resp.status_code == 200

    # Store 'xml' with password 'test2'
    resp = client.get("/store")
    assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": file_name, "XML": xml_as_string, "Password": password2})
    assert resp.status_code == 200

    # Delete file_name using a different password
    resp = client.get("/remove")
    assert resp.status_code == 200
    resp = client.post("/remove", data={"FileName": file_name, "Password": password2})
    assert resp.status_code == 200

    # Check SecondTest under the password 'test' still exists
    resp = client.get("/extract")
    assert resp.status_code == 200
    resp = client.post("/extract", data={"FileName": file_name, "Password": password})
    assert resp.status_code == 200
    