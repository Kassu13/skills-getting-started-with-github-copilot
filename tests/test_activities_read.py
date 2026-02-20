def test_get_activities_shape(client):
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # Check a known activity exists and has expected keys
    assert "Chess Club" in data
    activity = data["Chess Club"]
    for key in ("description", "schedule", "max_participants", "participants"):
        assert key in activity
