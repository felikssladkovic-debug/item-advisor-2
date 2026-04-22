from typing import Generic, TypeVar

from pydantic import BaseModel


DataT = TypeVar("DataT")


class ErrorDetail(BaseModel):
    code: str
    message: str


class ApiSuccess(BaseModel, Generic[DataT]):
    status: str = "ok"
    data: DataT


class ApiError(BaseModel):
    status: str = "error"
    error: ErrorDetail

