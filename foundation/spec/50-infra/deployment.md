# Deployment

Runtime services:
- MongoDB
- FastAPI backend
- Nginx frontend and reverse proxy

Nginx responsibilities:
- serve the site app at `/`
- serve the admin app under `/admin/`
- proxy `/api/` to the backend
- proxy `/health` to the backend

The repository includes Dockerfiles and `docker-compose.yml` for a local production-like stack.

