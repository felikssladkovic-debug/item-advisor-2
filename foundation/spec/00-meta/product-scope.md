# Product Scope

This foundation version implements one public page, one manager-only admin page, session auth, role checks, MongoDB persistence, deployment setup, and tests.

In scope:
- `/`
- `/admin/users`
- login by email and password
- logout
- `GET /api/v1/auth/me`
- `GET /api/v1/admin/users`
- `GET /health`
- seeded manager and user accounts

Out of scope:
- registration
- password reset
- profile editing
- admin mutations
- all ItemAdvisor business-domain features beyond users and access control

