def test_get_registration_page(client):
    response = client.get("/")
    print(response)
    assert b"Registration Portal" in response.data

def test_login_email(client):
    response = client.post(
        "/showSummary", data={"email": "admin@irontemple.com"}
    )
    assert b"Logout" in response.data

def test_clubs_points_display(client):
    response = client.get(
        "/showClubsPoints")
    print(response.data)
    assert b"<title>Points || GUDLFT" in response.data

def test_logout(client):
    response = client.get("/logout")
    print(response)
    assert b"Redirecting" in response.data
