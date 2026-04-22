# Architecture Decisions

- Backend uses FastAPI for a compact API surface and explicit dependency injection.
- MongoDB is the only database in this version. The `users` collection is the only application collection.
- Authentication uses a signed HTTP-only session cookie. The session stores the authenticated user id.
- Passwords are stored only as hashes.
- The site and admin interfaces are separate Vue 3 + Vite apps so public and privileged surfaces remain clearly separated.
- Nginx serves the built frontend assets and proxies API traffic to the backend.
- Seed users are created during backend startup if the configured seed emails are missing.
- The repository keeps specs close to code; each implemented behavior in this slice is described in `/spec`.

