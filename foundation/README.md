# ItemAdvisor Foundation

ItemAdvisor Foundation is the first production-like vertical slice of a new project. It is intentionally small: one public page, one admin page, session auth, role checks, MongoDB persistence, deployment wiring, tests, and repository-local English specs.

The purpose of this repository is to validate a development method:
- specs are written in English and stored in `/spec`
- the implementation stays constrained to those specs
- infrastructure starts deploy-ready instead of being deferred
- the slice is end-to-end real, not a mock skeleton

## Scope of this version

Included:
- public site at `/`
- admin page at `/admin/users`
- login, logout, current-user endpoint
- roles: `user`, `manager`
- MongoDB-backed users collection
- automatic seed users
- FastAPI backend
- Vue 3 + Vite site app
- Vue 3 + Vite admin app
- Docker, Compose, and Nginx setup
- backend and frontend tests

Excluded by design:
- registration
- password reset
- profile editing
- admin CRUD
- item catalog and all other business features

## Repository structure

```text
backend/             FastAPI API, auth, MongoDB integration, backend tests
frontend/site/       Vue public site app
frontend/admin/      Vue admin app
infra/nginx/         Reverse proxy config and production image
spec/                English implementation specs
docker-compose.yml   Local production-like stack
```

## Specs and implementation discipline

The repository is spec-first, but not spec-only.

- `/spec` defines the intended behavior, route structure, data model, and workflow rules.
- Code implements only the requested scope.
- If an implementation choice matters for behavior or structure, it is documented in the relevant spec file.
- The foundation version avoids speculative abstractions that are not used by the current slice.

Start with:
- [spec/00-meta/product-scope.md](/home/ubuntu/projects/item-advisor-2/foundation/spec/00-meta/product-scope.md)
- [spec/00-meta/architecture-decisions.md](/home/ubuntu/projects/item-advisor-2/foundation/spec/00-meta/architecture-decisions.md)
- [spec/70-workflow/consistency-rules.md](/home/ubuntu/projects/item-advisor-2/foundation/spec/70-workflow/consistency-rules.md)

## Demo credentials

These users are seeded automatically on backend startup:

- Manager: `manager@example.com` / `manager123`
- User: `user@example.com` / `user123`

These defaults are defined in `.env.example` and documented in the specs.

## Local development

### Option 1: Docker Compose

1. Copy `.env.example` to `.env`.
2. Run:

```bash
docker compose up --build
```

3. Open:
- Site: `http://localhost/`
- Admin: `http://localhost/admin/users`
- Health: `http://localhost/health`

### Option 2: Run services directly

Backend:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Site frontend:

```bash
cd frontend/site
npm install
npm run dev
```

Admin frontend:

```bash
cd frontend/admin
npm install
npm run dev
```

For direct frontend development, Vite proxies API requests to `http://localhost:8000`.

## Tests

Backend:

```bash
cd backend
pip install -r requirements.txt
pytest
```

Frontend site:

```bash
cd frontend/site
npm install
npm run test
```

Frontend admin:

```bash
cd frontend/admin
npm install
npm run test
```

## Deployment approach

The production-like stack is:
- `nginx` serves the built site and admin assets
- `nginx` proxies `/api/` and `/health` to the FastAPI backend
- `backend` connects to MongoDB
- `backend` seeds the initial users if they are missing

Relevant files:
- [docker-compose.yml](/home/ubuntu/projects/item-advisor-2/foundation/docker-compose.yml)
- [infra/nginx/nginx.conf](/home/ubuntu/projects/item-advisor-2/foundation/infra/nginx/nginx.conf)
- [infra/nginx/Dockerfile](/home/ubuntu/projects/item-advisor-2/foundation/infra/nginx/Dockerfile)
- [spec/50-infra/deployment.md](/home/ubuntu/projects/item-advisor-2/foundation/spec/50-infra/deployment.md)

## Key architectural choices

- FastAPI is split into config, repositories, services, routes, and schemas to keep the vertical slice readable.
- MongoDB documents store an explicit `id` field for API-facing stability, while MongoDB still maintains its native `_id`.
- Session auth uses a signed, HTTP-only cookie via Starlette session middleware.
- Passwords are stored as hashes with `pwdlib`.
- The site and admin UIs are separate Vue apps so public and privileged surfaces remain explicit from the start.

