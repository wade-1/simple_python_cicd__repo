import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, Jenkins Pipeline!" in response.data

def test_add(client):
    response = client.get('/add/2/3')
    assert b"Result: 5" in response.data