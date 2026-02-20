def test_root_redirect(client):
    resp = client.get("/", follow_redirects=False)
    assert resp.status_code in (307, 308)
    assert resp.headers.get("location") == "/static/index.html"
