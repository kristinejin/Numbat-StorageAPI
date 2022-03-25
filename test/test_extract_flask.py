import pytest
import random
import string
from src.flask_server import app
import requests
from test.xml_str import xml_as_string

URL = "http://127.0.0.1:5000"

def test_extract_basic():
    file_name = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    password = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    # Store 'xml'
    # resp = client.get("/store")
    # assert resp.status_code == 200
    resp = requests.post(URL + "/store", json={"FileName": file_name, "XML": xml_as_string, "Password": password})
    assert resp.status_code == 200

    # Extract stored 'xml'
    # resp = client.get("/extract")
    # print(resp.data)
    # assert resp.status_code == 200
    resp = requests.post(URL + "/extract", json={"FileName": file_name, "Password": password})
    assert resp.json()["XML"][0] == xml_as_string
    # assert resp.content() == "pls"
    assert resp.status_code == 200


def test_extract_not_there():
    file_name = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    password = (''.join(random.choice(string.ascii_lowercase)
                 for i in range(10)))
    
    # resp = client.get("/store")
    # assert resp.status_code == 200
    resp = requests.post(URL + "/store", json={"FileName": file_name, "XML": xml_as_string, "Password": password})
    assert resp.status_code == 200

    # Extract stored 'xml'
    # resp = client.get("/extract")
    # print(resp.data)
    # assert resp.status_code == 200
    resp = requests.post(URL + "/extract", json={"FileName": file_name + 'i', "Password": password + 'i'})
    assert resp.status_code == 400


