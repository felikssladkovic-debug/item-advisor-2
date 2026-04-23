from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .auth import (
    authenticate_user,
    end_session,
    load_current_user,
    require_manager,
    require_user,
    serialize_user,
    start_session,
)
from .config import settings
from .database import ensure_indexes, ensure_seed_users, users_collection
from .schemas import ErrorResponse, LoginRequest, LoginResponse, OkResponse, SessionResponse, UserListResponse, UserResponse


@asynccontextmanager
async def lifespan(_: FastAPI):
    ensure_indexes()
    ensure_seed_users()
    yield


app = FastAPI(title=settings.itemadvisor_app_name, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(_: Request, exc: HTTPException):
    if isinstance(exc.detail, dict) and "error" in exc.detail:
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail,
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": {"code": "http_error", "message": str(exc.detail)}},
    )


@app.get("/api/health")
def health_check() -> dict[str, bool]:
    return {"ok": True}


@app.post("/api/auth/login", response_model=LoginResponse, responses={401: {"model": ErrorResponse}})
def login(payload: LoginRequest, response: Response):
    user = authenticate_user(payload.email, payload.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail={"error": {"code": "invalid_credentials", "message": "Invalid email or password."}},
        )

    start_session(response, str(user["_id"]))
    return LoginResponse(user=serialize_user(user))


@app.post("/api/auth/logout", response_model=OkResponse)
def logout(request: Request, response: Response):
    end_session(request, response)
    return OkResponse(ok=True)


@app.get("/api/auth/session", response_model=SessionResponse)
def session_status(request: Request):
    user = load_current_user(request)
    if not user:
        return SessionResponse(authenticated=False, user=None)
    return SessionResponse(authenticated=True, user=serialize_user(user))


@app.get("/api/users/me", response_model=UserResponse, responses={401: {"model": ErrorResponse}})
def current_user(request: Request):
    user = require_user(request)
    return serialize_user(user)


@app.get(
    "/api/admin/users",
    response_model=UserListResponse,
    responses={401: {"model": ErrorResponse}, 403: {"model": ErrorResponse}},
)
def list_users(request: Request):
    require_manager(request)
    users = []
    for user in users_collection.find({}, sort=[("email", 1)]):
        users.append(
            {
                "id": str(user["_id"]),
                "email": user["email"],
                "role": user["role"],
                "created_at": user["created_at"],
            }
        )
    return UserListResponse(users=users)
