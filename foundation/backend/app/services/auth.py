from fastapi import HTTPException, Request, status

from app.repositories.users import UserRepository
from app.schemas.users import UserOut
from app.security import verify_password


def build_user_out(user_document: dict) -> UserOut:
    return UserOut(
        id=user_document["id"],
        email=user_document["email"],
        role=user_document["role"],
        created_at=user_document["created_at"],
    )


def authenticate_user(
    email: str,
    password: str,
    user_repository: UserRepository,
) -> dict:
    user = user_repository.get_by_email(email)
    if user is None or not verify_password(password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )
    return user


def get_current_user_from_session(
    request: Request,
    user_repository: UserRepository,
) -> dict | None:
    user_id = request.session.get("user_id")
    if not user_id:
        return None
    return user_repository.get_by_id(user_id)

