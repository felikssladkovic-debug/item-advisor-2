from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pymongo.database import Database
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.sessions import SessionMiddleware

from app.config import get_settings
from app.db import build_database
from app.repositories.users import UserRepository
from app.routes.admin import router as admin_router
from app.routes.auth import router as auth_router
from app.routes.health import router as health_router
from app.schemas.common import ApiError, ErrorDetail
from app.startup import initialize_data


def create_app(test_database: Database | None = None) -> FastAPI:
    settings = get_settings()
    database = test_database if test_database is not None else build_database(settings)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.db = database
        initialize_data(UserRepository(database), settings)
        yield

    app = FastAPI(title=settings.app_name, lifespan=lifespan)
    app.state.db = database
    app.add_middleware(
        SessionMiddleware,
        secret_key=settings.session_secret,
        session_cookie=settings.session_cookie_name,
        same_site="lax",
        https_only=settings.session_secure,
        max_age=60 * 60 * 24,
    )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
        return JSONResponse(
            status_code=422,
            content=ApiError(
                error=ErrorDetail(
                    code="validation_error",
                    message=str(exc.errors()[0]["msg"]) if exc.errors() else "Invalid request.",
                )
            ).model_dump(),
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(_: Request, exc: StarletteHTTPException) -> JSONResponse:
        code_map = {
            401: "unauthorized",
            403: "forbidden",
            404: "not_found",
        }
        message_map = {
            401: "Authentication required.",
            403: "Manager role required.",
            404: "Resource not found.",
        }
        return JSONResponse(
            status_code=exc.status_code,
            content=ApiError(
                error=ErrorDetail(
                    code=code_map.get(exc.status_code, "http_error"),
                    message=str(exc.detail) if exc.detail else message_map.get(exc.status_code, "Request failed."),
                )
            ).model_dump(),
        )

    app.include_router(health_router)
    app.include_router(auth_router)
    app.include_router(admin_router)
    return app


app = create_app()
