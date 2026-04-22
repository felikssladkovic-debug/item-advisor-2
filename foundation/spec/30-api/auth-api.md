# Auth API

## POST /api/v1/auth/login

Request body:
- `email`
- `password`

Success response:

```json
{
  "status": "ok",
  "data": {
    "authenticated": true,
    "user": {
      "id": "string",
      "email": "manager@example.com",
      "role": "manager",
      "created_at": "2026-01-01T00:00:00Z"
    }
  }
}
```

Failure response:

```json
{
  "status": "error",
  "error": {
    "code": "unauthorized",
    "message": "Invalid email or password."
  }
}
```

## POST /api/v1/auth/logout

Success response:

```json
{
  "status": "ok",
  "data": {
    "logged_out": true
  }
}
```

## GET /api/v1/auth/me

Authenticated response returns `authenticated: true` and a user object.

Unauthenticated response:

```json
{
  "status": "ok",
  "data": {
    "authenticated": false,
    "user": null
  }
}
```

