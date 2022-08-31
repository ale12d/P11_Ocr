def test_club_point_sub(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': 1}
    )
    assert b"Points available: 12" in response.data