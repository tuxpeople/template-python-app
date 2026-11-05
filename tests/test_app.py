import pytest

import app as application


@pytest.fixture
def client():
    application.app.config["TESTING"] = True
    return application.app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>" in response.data


def test_healthz(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_debug_is_off(client):
    # The Werkzeug debugger allows code execution from the browser
    assert application.app.debug is False
    response = client.get("/does-not-exist")
    assert response.status_code == 404
    assert b"Werkzeug Debugger" not in response.data
