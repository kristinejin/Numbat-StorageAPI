import pytest
from src.flask_server import app
from test.xml_str_for_search import generate_random_date, generate_random_name, generate_unique_xml

PASSWORD = 'password'
PASSWORD_ALTER = "password2"


@pytest.fixture
def client():
    return app.test_client()


def test_store_success(client):
    date = generate_random_date()
    sender_name = generate_random_name(20)
    xml = generate_unique_xml(date, sender_name)
    file_name = generate_random_name(5)
    # stores the invoice
    resp = client.post(
        '/store', data={'FileName': file_name, 'XML': xml, 'Password': PASSWORD})
    assert resp.status_code == 200


def test_store_duplicated_fname_only(client):
    date = generate_random_date()
    sender_name = generate_random_name(20)
    xml = generate_unique_xml(date, sender_name)
    file_name = generate_random_name(5)
    # stores the invoice
    resp = client.post(
        '/store', data={'FileName': file_name, 'XML': xml, 'Password': PASSWORD})
    assert resp.status_code == 200

    resp = client.post(
        '/store', data={'FileName': file_name, 'XML': xml, 'Password': PASSWORD_ALTER})
    assert resp.status_code == 200


def test_store_duplicated_fname_and_password(client):
    date = generate_random_date()
    sender_name = generate_random_name(20)
    xml = generate_unique_xml(date, sender_name)
    file_name = generate_random_name(5)
    # stores the invoice
    resp = client.post(
        '/store', data={'FileName': file_name, 'XML': xml, 'Password': PASSWORD})
    assert resp.status_code == 200

    resp = client.post(
        '/store', data={'FileName': file_name, 'XML': xml, 'Password': PASSWORD})
    assert resp.status_code == 400


def test_store_invalid_xml(client):
    date = generate_random_date()
    sender_name = generate_random_name(20)
    xml = 'invalid xml'
    file_name = generate_random_name(5)
    # stores the invoice
    resp = client.post(
        '/store', data={'FileName': file_name, 'XML': xml, 'Password': PASSWORD})
    assert resp.status_code == 400
