from server import showSummary, app
import pytest

@pytest.fixture()
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client


def test_crash_unknown_email(client):
    response = client.post(
        "/showSummary", data={"email": "test@test.fr"}
    )
    assert b"email not found" in response.data

def test_login_email(client):
    response = client.post(
        "/showSummary", data={"email": "admin@irontemple.com"}
    )
    print(response.data)
    assert b"Logout" in response.data