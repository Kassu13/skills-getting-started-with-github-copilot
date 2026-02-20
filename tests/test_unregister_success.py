from urllib.parse import quote


def test_unregister_removes_participant(client):
    # michael@mergington.edu exists in initial Chess Club participants
    activity = "Chess Club"
    email = "michael@mergington.edu"

    url = f"/activities/{quote(activity)}/signup"
    resp = client.delete(url, params={"email": email})
    assert resp.status_code == 200
    body = resp.json()
    assert "Removed" in body.get("message", "")

    # Verify via GET that the participant was removed
    get_resp = client.get("/activities")
    activities = get_resp.json()
    assert email not in activities[activity]["participants"]
