"""Tests for the HTTP API as it behaves today.

Each test follows the same pattern: Arrange (set things up), Act (make a request),
Assert (check what came back).
"""


async def test_root_says_online(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert "online" in response.json()["message"]


async def test_create_returns_short_key_and_secret(client):
    response = await client.post("/create", json={"target_url": "https://example.com/page"})

    assert response.status_code == 200
    body = response.json()
    assert body["target_url"] == "https://example.com/page"
    assert len(body["key"]) == 7
    assert len(body["secret_key"]) >= 12
    assert body["clicks"] == 0
    assert body["is_active"] is True


async def test_create_rejects_something_that_is_not_a_url(client):
    response = await client.post("/create", json={"target_url": "not a url"})
    assert response.status_code == 422


async def test_create_rejects_non_http_schemes(client):
    response = await client.post("/create", json={"target_url": "javascript:alert(1)"})
    assert response.status_code == 422


async def test_two_links_get_different_keys(client):
    first = (await client.post("/create", json={"target_url": "https://a.example"})).json()
    second = (await client.post("/create", json={"target_url": "https://a.example"})).json()
    assert first["key"] != second["key"]
    assert first["secret_key"] != second["secret_key"]


async def test_redirect_sends_you_to_the_target(client, created):
    response = await client.get(f"/{created['key']}")

    assert response.status_code in (301, 302, 307, 308)
    assert response.headers["location"] == "https://example.com/page"


async def test_redirect_counts_clicks(client, created):
    for _ in range(3):
        await client.get(f"/{created['key']}")

    stats = (await client.get(f"/stats/{created['secret_key']}")).json()
    assert stats["clicks"] == 3


async def test_unknown_key_is_404(client):
    response = await client.get("/doesnotexist")
    assert response.status_code == 404


async def test_stats_with_wrong_secret_is_404(client, created):
    response = await client.get("/stats/wrong-secret")
    assert response.status_code == 404


async def test_delete_removes_the_link_for_good(client, created):
    response = await client.delete(f"/admin/{created['secret_key']}")
    assert response.status_code == 204

    assert (await client.get(f"/{created['key']}")).status_code == 404
    assert (await client.get(f"/stats/{created['secret_key']}")).status_code == 404


async def test_deleting_twice_is_404_the_second_time(client, created):
    await client.delete(f"/admin/{created['secret_key']}")
    response = await client.delete(f"/admin/{created['secret_key']}")
    assert response.status_code == 404
