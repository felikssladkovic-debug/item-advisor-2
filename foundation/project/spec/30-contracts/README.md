# API Contracts

All backend endpoints are prefixed with `/api`.

## POST `/api/auth/login`

- Request body:
  - `email`: string
  - `password`: string
- Success:
  - status `200`
  - sets session cookie
  - response body:
    - `user.id`
    - `user.email`
    - `user.role`
- Failure:
  - status `401` for invalid credentials

## POST `/api/auth/logout`

- Success:
  - status `200`
  - clears session cookie
  - response body:
    - `ok`: boolean

## GET `/api/auth/session`

- Success:
  - status `200`
  - response body:
    - `authenticated`: boolean
    - `user`: object or `null`

## GET `/api/users/me`

- Requires authenticated session.
- Success:
  - status `200`
  - response body:
    - `id`
    - `email`
    - `role`
- Failure:
  - status `401` if not authenticated

## GET `/api/admin/users`

- Requires authenticated `manager` session.
- Success:
  - status `200`
  - response body:
    - `users`: array of user objects with `id`, `email`, `role`, `created_at`
- Failure:
  - status `401` if not authenticated
  - status `403` if authenticated but not a manager

## Error Model

- Error response body:
  - `error.code`: string
  - `error.message`: string
