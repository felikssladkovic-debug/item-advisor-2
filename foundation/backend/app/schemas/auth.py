from pydantic import BaseModel, EmailStr

from app.schemas.users import UserOut


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class AuthState(BaseModel):
    authenticated: bool
    user: UserOut | None


class LogoutResponse(BaseModel):
    logged_out: bool

