def test_clubs_points_display(client):
    response = client.get(
        "/showClubsPoints")
    print(response.data)
    assert b"<title>Points || GUDLFT" in response.data