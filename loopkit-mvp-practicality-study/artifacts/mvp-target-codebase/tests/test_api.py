import json
import os

from src.data.store import store
from src.routes.api import dispatch
from src.services.auth import authenticate_token, issue_token


def setup_function():
    os.environ["LOOPKIT_MVP_SECRET"] = "test-only-secret-that-is-at-least-32-bytes"
    store.reset()


def register_and_login(username="alice"):
    dispatch("POST", "/users", json.dumps({"username": username, "password": "secret"}))
    status, payload = dispatch("POST", "/login", json.dumps({"username": username, "password": "secret"}))
    assert status == 200
    return {"Authorization": f"Bearer {payload['token']}"}


def test_unauthorized_task_access_is_rejected():
    status, payload = dispatch("GET", "/tasks")
    assert status == 401
    assert payload["error"] == "unauthorized"


def test_user_can_create_and_list_own_tasks():
    headers = register_and_login()
    status, task = dispatch("POST", "/tasks", json.dumps({"title": "ship report"}), headers)
    assert status == 201
    status, payload = dispatch("GET", "/tasks", headers=headers)
    assert status == 200
    assert payload["items"] == [task]


def test_cross_user_task_access_is_hidden():
    alice = register_and_login("alice")
    bob = register_and_login("bob")
    _, task = dispatch("POST", "/tasks", json.dumps({"title": "private"}), alice)
    status, _ = dispatch("GET", f"/tasks/{task['id']}", headers=bob)
    assert status == 404
    status, _ = dispatch("PATCH", f"/tasks/{task['id']}", json.dumps({"completed": True}), bob)
    assert status == 404


def test_tampered_token_is_rejected():
    headers = register_and_login()
    headers["Authorization"] += "tampered"
    status, payload = dispatch("GET", "/tasks", headers=headers)
    assert status == 401
    assert payload == {"error": "unauthorized"}


def test_password_is_salted_and_not_stored_as_plain_sha256():
    dispatch("POST", "/users", json.dumps({"username": "alice", "password": "secret"}))
    first = store.find_user_by_username("alice").password_hash
    store.reset()
    dispatch("POST", "/users", json.dumps({"username": "alice", "password": "secret"}))
    second = store.find_user_by_username("alice").password_hash
    assert first.startswith("pbkdf2_sha256$")
    assert first != second


def test_expired_token_is_rejected():
    dispatch("POST", "/users", json.dumps({"username": "alice", "password": "secret"}))
    user = store.find_user_by_username("alice")
    assert authenticate_token(issue_token(user, ttl_seconds=-1)) is None
