def test_club_point_allowed(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Iron Temple', 'competition': 'Spring Festival', 'places': 5}
    )
    assert b"incorrect input" in response.data