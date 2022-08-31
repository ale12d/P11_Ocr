def test_max_place_competition(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': 13}
    )
    assert b"incorrect input" in response.data