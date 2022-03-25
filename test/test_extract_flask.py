import pytest
import random
import string
from src.flask_server import app
import requests
from test.xml_str import xml_as_string

@pytest.fixture
def client():
    return app.test_client()

def test_extract_basic(client):
    file_name = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    password = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    # Store 'xml'
    # resp = client.get("/store")
    # assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": file_name, "XML": xml_as_string, "Password": password})
    assert resp.status_code == 200

    # Extract stored 'xml'
    # resp = client.get("/extract")
    resp = client.post("/extract", data={"FileName": file_name, "Password": password})
    assert xml_as_string == resp.get_data(as_text=True)
    assert resp.status_code == 200


def test_extract_not_there(client):
    file_name = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    password = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    
    # resp = client.get("/store")
    # assert resp.status_code == 200
    resp = client.post("/store", data={"FileName": file_name, "XML": xml_as_string, "Password": password})
    assert resp.status_code == 200

    # Extract stored 'xml'
    # resp = client.get("/extract")
    # print(resp.data)
    # assert resp.status_code == 200
    resp = client.post("/extract", data={"FileName": file_name + 'i', "Password": password + 'i'})
    assert resp.status_code == 400


