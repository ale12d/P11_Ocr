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


def test_max_place_competition(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': 13}
    )
    assert b"incorrect input" in response.data


def test_past_competition(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Simply Lift', 'competition': 'Fall Classic', 'places': 1}
    )
    assert b"finished competition" in response.data


def test_club_point_sub(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': 1}
    )
    assert b"Points available: 12" in response.data


def test_clubs_points_display(client):
    response = client.get(
        "/showClubsPoints")
    assert b"<title>Points || GUDLFT" in response.data


def test_get_registration_page(client):
    response = client.get("/")
    print(response)
    assert b"Registration Portal" in response.data


def test_logout(client):
    response = client.get("/logout")
    assert b"Redirecting" in response.data
