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
    assert b"incorrect input" in response.data

#fix 3 / tests
def test_max_place_competition(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': 13}
    )
    assert b"incorrect input" in response.data

#fix 4 / tests
def test_past_competition(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Simply Lift', 'competition': 'Fall Classic', 'places': 1}
    )
    assert b"finished competition" in response.data

#fix 5 / tests
def test_club_point_sub(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': 1}
    )
    assert b"Points available: 12" in response.data