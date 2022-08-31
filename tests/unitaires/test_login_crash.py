def test_crash_unknown_email(client):
    response = client.post(
        "/showSummary", data={"email": "test@test.fr"}
    )
    assert b"email not found" in response.data
