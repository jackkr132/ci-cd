import pytest
import app

@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    test_client = app.app.test_client()
    return test_client


def test_get(client):
    response = client.get('/')
    check = response.data.decode('utf-8') == "HELLO WORLD"
    assert check


def test_post(client):
    response = client.post("/")
    assert response.status_code == 405
