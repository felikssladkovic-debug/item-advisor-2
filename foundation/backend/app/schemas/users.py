from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr


Role = Literal["user", "manager"]


class UserOut(BaseModel):
    id: str
    email: EmailStr
    role: Role
    created_at: datetime


class UserListItem(BaseModel):
    id: str
    email: EmailStr
    role: Role
    created_at: datetime

