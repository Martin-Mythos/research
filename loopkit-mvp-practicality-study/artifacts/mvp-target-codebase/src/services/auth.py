from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import json
import os
import secrets
import time
from typing import Optional

from src.data.store import User, store

PBKDF2_ITERATIONS = 200_000


def _secret() -> bytes:
    value = os.environ.get("LOOPKIT_MVP_SECRET", "")
    if len(value) < 32:
        raise RuntimeError("LOOPKIT_MVP_SECRET must contain at least 32 characters")
    return value.encode()

def _b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")

def _unb64(data: str) -> bytes:
    return base64.urlsafe_b64decode(data + "=" * (-len(data) % 4))

def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, PBKDF2_ITERATIONS)
    return f"pbkdf2_sha256${PBKDF2_ITERATIONS}${_b64(salt)}${_b64(digest)}"

def verify_password(password: str, password_hash: str) -> bool:
    try:
        algorithm, iterations, salt, expected = password_hash.split("$", 3)
        if algorithm != "pbkdf2_sha256":
            return False
        digest = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), _unb64(salt), int(iterations)
        )
        return hmac.compare_digest(_b64(digest), expected)
    except (ValueError, binascii.Error):
        return False

def issue_token(user: User, ttl_seconds: int = 3600) -> str:
    header = _b64(json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":")).encode())
    payload = {"sub": user.id, "exp": int(time.time()) + ttl_seconds}
    body = _b64(json.dumps(payload, separators=(",", ":")).encode())
    signing_input = f"{header}.{body}"
    sig = _b64(hmac.new(_secret(), signing_input.encode(), hashlib.sha256).digest())
    return f"{signing_input}.{sig}"

def authenticate_token(token: str) -> Optional[User]:
    try:
        header, body, sig = token.split(".", 2)
        token_header = json.loads(_unb64(header))
        if token_header != {"alg": "HS256", "typ": "JWT"}:
            return None
        signing_input = f"{header}.{body}"
        expected = _b64(hmac.new(_secret(), signing_input.encode(), hashlib.sha256).digest())
        if not hmac.compare_digest(sig, expected):
            return None
        payload = json.loads(_unb64(body))
        if int(payload["exp"]) < int(time.time()):
            return None
        return store.get_user(int(payload["sub"]))
    except (ValueError, KeyError, TypeError, json.JSONDecodeError, binascii.Error):
        return None
