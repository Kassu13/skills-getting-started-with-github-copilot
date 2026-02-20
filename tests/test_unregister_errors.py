from urllib.parse import quote


def test_unregister_unknown_activity(client):
    url = f"/activities/{quote('NoSuchActivity')}/signup"
    resp = client.delete(url, params={"email": "a@b.com"})
    assert resp.status_code == 404


def test_unregister_email_not_signed_up(client):
    activity = "Chess Club"
    email = "not_signed_up@mergington.edu"
    url = f"/activities/{quote(activity)}/signup"
    resp = client.delete(url, params={"email": email})
    assert resp.status_code == 404
