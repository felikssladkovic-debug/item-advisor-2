from fastapi import APIRouter, Depends, Request

from app.dependencies import get_current_user, get_user_repository
from app.repositories.users import UserRepository
from app.schemas.auth import AuthState, LoginRequest, LogoutResponse
from app.schemas.common import ApiSuccess
from app.schemas.users import UserOut
from app.services.auth import authenticate_user, build_user_out

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


@router.post("/login", response_model=ApiSuccess[AuthState])
async def login(
    payload: LoginRequest,
    request: Request,
    user_repository: UserRepository = Depends(get_user_repository),
) -> ApiSuccess[AuthState]:
    user = authenticate_user(payload.email, payload.password, user_repository)
    request.session["user_id"] = user["id"]
    user_out = build_user_out(user)
    return ApiSuccess(data=AuthState(authenticated=True, user=user_out))


@router.post("/logout", response_model=ApiSuccess[LogoutResponse])
async def logout(request: Request) -> ApiSuccess[LogoutResponse]:
    request.session.clear()
    return ApiSuccess(data=LogoutResponse(logged_out=True))


@router.get("/me", response_model=ApiSuccess[AuthState])
async def me(current_user: UserOut | None = Depends(get_current_user)) -> ApiSuccess[AuthState]:
    return ApiSuccess(
        data=AuthState(
            authenticated=current_user is not None,
            user=current_user,
        )
    )
