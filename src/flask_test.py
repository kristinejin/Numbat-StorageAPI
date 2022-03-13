import pytest
from src.flaskServer import app

@pytest.fixture
def client():
	return app.test_client()

def test_home(client):
	resp = client.get('/')
	print(resp.data)
	assert resp.status_code == 200

def test_store(client):
	resp = client.get('/store')
	print(resp.data)
	assert resp.status_code == 200

def test_extract(client):
	resp = client.get('/extract')
	print(resp.data)
	assert resp.status_code == 200

def test_remove(client):
	resp = client.get('/remove')
	print(resp.data)
	assert resp.status_code == 200