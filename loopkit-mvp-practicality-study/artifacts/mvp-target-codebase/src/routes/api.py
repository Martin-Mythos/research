from __future__ import annotations

import json
from http import HTTPStatus
from typing import Dict, Tuple

from src.data.store import store
from src.services.auth import authenticate_token, hash_password, issue_token, verify_password
from src.services.tasks import create_task, serialize_task

Response = Tuple[int, Dict[str, object]]

def _current_user(headers: Dict[str, str]):
    auth = headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return None
    return authenticate_token(auth.removeprefix("Bearer "))

def _require_user(headers: Dict[str, str]):
    user = _current_user(headers)
    if user is None:
        return None, (HTTPStatus.UNAUTHORIZED, {"error": "unauthorized"})
    return user, None

def dispatch(method: str, path: str, body: str = "{}", headers: Dict[str, str] | None = None) -> Response:
    headers = headers or {}
    data = json.loads(body or "{}")
    parts = [p for p in path.strip("/").split("/") if p]

    if method == "POST" and parts == ["users"]:
        user = store.create_user(data["username"], hash_password(data["password"]))
        return HTTPStatus.CREATED, {"id": user.id, "username": user.username}

    if method == "POST" and parts == ["login"]:
        user = store.find_user_by_username(data.get("username", ""))
        if user is None or not verify_password(data.get("password", ""), user.password_hash):
            return HTTPStatus.UNAUTHORIZED, {"error": "invalid credentials"}
        return HTTPStatus.OK, {"token": issue_token(user)}

    user, error = _require_user(headers)
    if error:
        return error

    if method == "POST" and parts == ["tasks"]:
        return HTTPStatus.CREATED, create_task(user.id, data.get("title", ""))
    if method == "GET" and parts == ["tasks"]:
        return HTTPStatus.OK, {"items": [serialize_task(t) for t in store.list_tasks(user.id)]}
    if len(parts) == 2 and parts[0] == "tasks":
        task_id = int(parts[1])
        if method == "GET":
            task = store.get_task(task_id, user.id)
            return (HTTPStatus.OK, serialize_task(task)) if task else (HTTPStatus.NOT_FOUND, {"error": "not found"})
        if method == "PATCH":
            task = store.update_task(task_id, user.id, bool(data.get("completed")))
            return (HTTPStatus.OK, serialize_task(task)) if task else (HTTPStatus.NOT_FOUND, {"error": "not found"})
    return HTTPStatus.NOT_FOUND, {"error": "not found"}
