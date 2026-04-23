from typing import Literal, Optional

from pydantic import BaseModel, EmailStr


Role = Literal["manager", "user"]


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    role: Role


class LoginResponse(BaseModel):
    user: UserResponse


class UserListItem(UserResponse):
    created_at: str


class SessionResponse(BaseModel):
    authenticated: bool
    user: Optional[UserResponse]


class UserListResponse(BaseModel):
    users: list[UserListItem]


class OkResponse(BaseModel):
    ok: bool


class ErrorPayload(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    error: ErrorPayload
