# Routing

External routes:
- `/` -> site app
- `/admin/users` -> admin app
- `/api/v1/auth/*` -> backend auth API
- `/api/v1/admin/users` -> backend admin API
- `/health` -> backend health endpoint

Nginx serves both frontend builds and forwards backend routes to FastAPI.

