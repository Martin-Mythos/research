import json

from src.data.store import store
from src.routes.api import dispatch


def setup_function():
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
