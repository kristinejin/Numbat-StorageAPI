# import pytest
# from src.flask_server import app

# @pytest.fixture
# def client():
# 	return app.test_client()

# def test_home(client):
# 	resp = client.get('/')
# 	print(resp.data)
# 	assert resp.status_code == 200

# def test_store(client):
# 	resp = client.get('/store')
# 	assert resp.status_code == 200
# 	resp = client.post('/store', data={'fnm': 'Test','xmll': 'Pls'})
# 	assert resp.status_code == 200

# def test_remove(client):
# 	resp = client.get('/remove')
# 	print(resp.data)
# 	assert resp.status_code == 200

# def test_search(client):
# 	resp = client.get('/search')
# 	print(resp.data)
# 	assert resp.status_code == 200
