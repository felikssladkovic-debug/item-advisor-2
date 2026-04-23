import base64
import hashlib
import hmac
import os
import secrets
from typing import Optional


PBKDF2_ITERATIONS = 120_000


def hash_password(password: str, salt: Optional[str] = None) -> str:
    password_salt = salt or secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(password_salt),
        PBKDF2_ITERATIONS,
    )
    return f"{password_salt}${digest.hex()}"


def verify_password(password: str, password_hash: str) -> bool:
    salt, expected_digest = password_hash.split("$", 1)
    actual_hash = hash_password(password, salt)
    return hmac.compare_digest(actual_hash, f"{salt}${expected_digest}")


def generate_session_id() -> str:
    return secrets.token_urlsafe(32)


def sign_session_id(session_id: str, secret: str) -> str:
    encoded_id = base64.urlsafe_b64encode(session_id.encode("utf-8")).decode("ascii")
    signature = hmac.new(
        secret.encode("utf-8"),
        session_id.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    return f"{encoded_id}.{signature}"


def verify_session_cookie(cookie_value: str, secret: str) -> Optional[str]:
    try:
        encoded_id, provided_signature = cookie_value.split(".", 1)
        session_id = base64.urlsafe_b64decode(encoded_id.encode("ascii")).decode("utf-8")
    except Exception:
        return None

    expected_signature = hmac.new(
        secret.encode("utf-8"),
        session_id.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    if not hmac.compare_digest(provided_signature, expected_signature):
        return None

    return session_id
