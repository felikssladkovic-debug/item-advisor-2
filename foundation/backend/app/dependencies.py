from fastapi import Depends, HTTPException, Request, status
from pymongo.database import Database

from app.repositories.users import UserRepository
from app.schemas.users import UserOut
from app.services.auth import build_user_out, get_current_user_from_session


async def get_database(request: Request) -> Database:
    return request.app.state.db


async def get_user_repository(database: Database = Depends(get_database)) -> UserRepository:
    return UserRepository(database)


async def get_current_user(
    request: Request,
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserOut | None:
    user = get_current_user_from_session(request, user_repository)
    if user is None:
        return None
    return build_user_out(user)


async def require_authenticated_user(
    current_user: UserOut | None = Depends(get_current_user),
) -> UserOut:
    if current_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required.",
        )
    return current_user


async def require_manager(
    current_user: UserOut = Depends(require_authenticated_user),
) -> UserOut:
    if current_user.role != "manager":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Manager role required.",
        )
    return current_user
