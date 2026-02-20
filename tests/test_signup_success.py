from urllib.parse import quote


def test_signup_adds_participant(client):
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    url = f"/activities/{quote(activity)}/signup"
    resp = client.post(url, params={"email": email})
    assert resp.status_code == 200
    body = resp.json()
    assert "Signed up" in body.get("message", "")

    # Verify via GET that the participant was added
    get_resp = client.get("/activities")
    assert get_resp.status_code == 200
    activities = get_resp.json()
    assert email in activities[activity]["participants"]
