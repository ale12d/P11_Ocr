from server import showSummary, app, purchasePlaces
import pytest

@pytest.fixture()
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client

#fix 1 / tests
def test_crash_unknown_email(client):
    response = client.post(
        "/showSummary", data={"email": "test@test.fr"}
    )
    assert b"email not found" in response.data

def test_login_email(client):
    response = client.post(
        "/showSummary", data={"email": "admin@irontemple.com"}
    )
    assert b"Logout" in response.data

#fix 2 / tests
def test_club_point_allowed(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Iron Temple', 'competition': 'Spring Festival', 'places': 5}
    )
    print(response.data)
    assert b"incorrect input" in response.data