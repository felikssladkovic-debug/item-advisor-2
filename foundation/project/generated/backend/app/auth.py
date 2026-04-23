from datetime import datetime, timezone
from typing import Any, Optional

from bson import ObjectId
from fastapi import HTTPException, Request, Response, status

from .config import settings
from .database import sessions_collection, users_collection
from .schemas import UserResponse
from .security import generate_session_id, sign_session_id, verify_password, verify_session_cookie


def serialize_user(user: dict[str, Any]) -> UserResponse:
    return UserResponse(id=str(user["_id"]), email=user["email"], role=user["role"])


def load_current_user(request: Request) -> Optional[dict[str, Any]]:
    cookie_value = request.cookies.get(settings.itemadvisor_session_cookie_name)
    if not cookie_value:
        return None

    session_id = verify_session_cookie(cookie_value, settings.itemadvisor_session_secret)
    if not session_id:
        return None

    session = sessions_collection.find_one({"id": session_id})
    if not session:
        return None

    user = users_collection.find_one({"_id": ObjectId(session["user_id"])})
    return user


def require_user(request: Request) -> dict[str, Any]:
    user = load_current_user(request)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": {"code": "not_authenticated", "message": "Authentication required."}},
        )
    return user


def require_manager(request: Request) -> dict[str, Any]:
    user = require_user(request)
    if user["role"] != "manager":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"error": {"code": "not_authorized", "message": "Manager role required."}},
        )
    return user


def authenticate_user(email: str, password: str) -> Optional[dict[str, Any]]:
    user = users_collection.find_one({"email": email})
    if not user:
        return None
    if not verify_password(password, user["password_hash"]):
        return None
    return user


def start_session(response: Response, user_id: str) -> None:
    session_id = generate_session_id()
    sessions_collection.insert_one(
        {
            "id": session_id,
            "user_id": user_id,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    cookie_value = sign_session_id(session_id, settings.itemadvisor_session_secret)
    response.set_cookie(
        key=settings.itemadvisor_session_cookie_name,
        value=cookie_value,
        httponly=True,
        secure=settings.itemadvisor_session_secure,
        samesite="lax",
        path="/",
    )


def end_session(request: Request, response: Response) -> None:
    cookie_value = request.cookies.get(settings.itemadvisor_session_cookie_name)
    if cookie_value:
        session_id = verify_session_cookie(cookie_value, settings.itemadvisor_session_secret)
        if session_id:
            sessions_collection.delete_one({"id": session_id})
    response.delete_cookie(settings.itemadvisor_session_cookie_name, path="/")
