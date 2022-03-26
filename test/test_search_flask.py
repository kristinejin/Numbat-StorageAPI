import pytest
from src.flask_server import app
from test.xml_str_for_search import generate_random_date, generate_random_name, generate_unique_xml
import json
PASSWORD = 'searchtest'


@pytest.fixture
def client():
    return app.test_client()


def test_search_success_both_keys(client):
    date = generate_random_date()
    sender_name = generate_random_name(20)
    xml = generate_unique_xml(date, sender_name)
    file_name = generate_random_name(5)
    # stores the invoice
    resp = client.post(
        '/store', data={'FileName': file_name, 'XML': xml, 'Password': PASSWORD})
    assert resp.status_code == 200

    # search request
    resp = client.get('/search')
    assert resp.status_code == 200
    resp = client.post(
        '/search', data={'sender_name': sender_name, 'issue_date': date, 'Password': PASSWORD})
    assert resp.status_code == 200
    assert {'file_names': [file_name]} == json.loads(resp.get_data())


def test_search_success_sender_name_only(client):
    date = generate_random_date()
    sender_name = generate_random_name(20)
    xml = generate_unique_xml(date, sender_name)
    file_name = generate_random_name(5)
    # stores the invoice
    resp = client.post(
        '/store', data={'FileName': file_name, 'XML': xml, 'Password': PASSWORD})
    assert resp.status_code == 200

    # search request
    resp = client.get('/search')
    assert resp.status_code == 200
    resp = client.post(
        '/search', data={'sender_name': sender_name, 'Password': PASSWORD})
    assert resp.status_code == 200
    assert {'file_names': [file_name]} == json.loads(resp.get_data())


def test_search_success_issue_date_only(client):
    date = generate_random_date()
    sender_name = generate_random_name(20)
    xml = generate_unique_xml(date, sender_name)
    file_name = generate_random_name(5)
    # stores the invoice
    resp = client.get('/store')
    assert resp.status_code == 200
    resp = client.post(
        '/store', data={'FileName': file_name, 'XML': xml, 'Password': PASSWORD})
    assert resp.status_code == 200

    # search request
    resp = client.get('/search')
    assert resp.status_code == 200
    resp = client.post(
        '/search', data={'issue_date': date, 'Password': PASSWORD})
    assert resp.status_code == 200
    assert {'file_names': [file_name]} == json.loads(resp.get_data())


def test_search_fail(client):
    date = generate_random_date()
    sender_name = generate_random_name(20)
    xml = generate_unique_xml(date, sender_name)
    file_name = generate_random_name(5)
    # stores the invoice
    resp = client.get('/store')
    assert resp.status_code == 200
    resp = client.post(
        '/store', data={'FileName': file_name, 'XML': xml, 'Password': PASSWORD})
    assert resp.status_code == 200

    # search request
    resp = client.get('/search')
    assert resp.status_code == 200
    resp = client.post(
        '/search', data={'sender_name': 'kkk', 'issue_date': '1930-03-03', 'Password': PASSWORD})
    assert resp.status_code == 400
