"""Test the Flask API endpoints."""


def test_request_example(client):
    response = client.get('/schema')
    assert b"default sample checklist" in response.data


def test_post_submit(client):
    response = client.post("/submit", json={
        "name": "John Doe",
        "age": 42
    })
    assert b"success" in response.data
