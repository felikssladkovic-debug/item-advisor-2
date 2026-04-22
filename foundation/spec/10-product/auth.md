# Auth

Auth mechanism:
- email and password login
- session cookie after successful login
- logout clears the session
- `GET /api/v1/auth/me` reports whether the current request is authenticated

Security requirements:
- passwords are hashed
- cookie is HTTP-only
- cookie secure flag is environment-configurable so local HTTP works and production can require HTTPS

