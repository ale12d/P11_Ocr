def test_get_registration_page(client):
    response = client.get("/")
    print(response)
    assert b"Registration Portal" in response.data

def test_login_email(client):
    response = client.post(
        "/showSummary", data={"email": "admin@irontemple.com"}
    )
    assert b"Logout" in response.data

def test_club_point_allowed(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Iron Temple', 'competition': 'Spring Festival', 'places': 5}
    )
    assert b"incorrect input" in response.data

def test_purchase_places(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Iron Temple', 'competition': 'Spring Festival', 'places': 2}
    )
    assert b"Points available: 2" in response.data

def test_logout(client):
    response = client.get("/logout")
    print(response)
    assert b"Redirecting" in response.data
