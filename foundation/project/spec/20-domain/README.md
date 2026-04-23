# Domain Model

## Entities

### User

- Fields:
  - `id`: string
  - `email`: string
  - `password_hash`: string
  - `role`: `manager | user`
  - `created_at`: ISO datetime string
- Rules:
  - `email` is unique.
  - `role` must be either `manager` or `user`.

### Session

- Fields:
  - `id`: string
  - `user_id`: string
  - `created_at`: ISO datetime string
- Rules:
  - Every session belongs to exactly one user.

## Roles

- `manager`
  - can access authenticated site page
  - can list users on admin users page
- `user`
  - can access authenticated site page
  - cannot list users on admin users page
