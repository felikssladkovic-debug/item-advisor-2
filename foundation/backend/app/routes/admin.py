from fastapi import APIRouter, Depends

from app.dependencies import get_user_repository, require_manager
from app.repositories.users import UserRepository
from app.schemas.common import ApiSuccess
from app.schemas.users import UserListItem, UserOut

router = APIRouter(prefix="/api/v1/admin", tags=["admin"])


@router.get("/users", response_model=ApiSuccess[list[UserListItem]])
async def list_users(
    _: UserOut = Depends(require_manager),
    user_repository: UserRepository = Depends(get_user_repository),
) -> ApiSuccess[list[UserListItem]]:
    users = [UserListItem(**user) for user in user_repository.list_users()]
    return ApiSuccess(data=users)
