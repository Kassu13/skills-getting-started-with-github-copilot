from urllib.parse import quote


def test_signup_unknown_activity(client):
    url = f"/activities/{quote('NoSuchActivity')}/signup"
    resp = client.post(url, params={"email": "a@b.com"})
    assert resp.status_code == 404


def test_signup_duplicate(client):
    activity = "Chess Club"
    email = "dup@mergington.edu"
    url = f"/activities/{quote(activity)}/signup"

    # first signup ok
    r1 = client.post(url, params={"email": email})
    assert r1.status_code == 200

    # second signup should fail with 400
    r2 = client.post(url, params={"email": email})
    assert r2.status_code == 400
