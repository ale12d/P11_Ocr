def test_past_competition(client):
    response = client.post(
        "/purchasePlaces", data={'club': 'Simply Lift', 'competition': 'Fall Classic', 'places': 1}
    )
    assert b"finished competition" in response.data
