import pytest
from src.flaskServer import app
from test.xml_str_for_search import generate_random_date, generate_random_name, generate_unique_xml


@pytest.fixture
def client():
    return app.test_client()


'''
def test_home(client):
    resp = client.get('/')
    print(resp.data)
    assert resp.status_code == 200


def test_store(client):
    resp = client.get('/store')
    assert resp.status_code == 200
    resp = client.post('/store', data={'fnm': 'Test', 'xmll': 'Pls'})
    assert resp.status_code == 200



def test_extract(client):
    resp = client.get('/extract')
    print(resp.data)
    assert resp.status_code == 200


def test_remove(client):
    resp = client.get('/remove')
    print(resp.data)
    assert resp.status_code == 200
'''


def test_search_success(client):
    date = generate_random_date()
    sender_name = generate_random_name(20)
    xml = generate_unique_xml(date, sender_name)
    file_name = generate_random_name(5)
    # stores the invoice
    resp = client.get('/store')
    assert resp.status_code == 200
    resp = client.post('/store', data={'fnm': file_name, 'xmll': xml})
    assert resp.status_code == 200

    # search request
    resp = client.get('/search')
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post('/search', data={'sfn': sender_name, 'ssd': date})
    assert resp.status_code == 200


def test_search_fail(client):
    date = generate_random_date()
    sender_name = generate_random_name(20)
    xml = generate_unique_xml(date, sender_name)
    file_name = generate_random_name(5)
    # stores the invoice
    resp = client.get('/store')
    assert resp.status_code == 200
    resp = client.post('/store', data={'fnm': file_name, 'xmll': xml})
    assert resp.status_code == 200

    # search request
    resp = client.get('/search')
    print(resp.data)
    assert resp.status_code == 200
    resp = client.post('/search', data={'sfn': 'kkk', 'ssd': '1930-03-03'})
    assert resp.status_code == 200
    # TODO -> should be:
    # assert resp.status_code == 400
