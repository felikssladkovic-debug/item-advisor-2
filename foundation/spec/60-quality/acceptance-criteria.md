# Acceptance Criteria

- Opening `/` shows whether the visitor is authenticated.
- Logging in with valid credentials authenticates the session and shows user details.
- Invalid login returns an unauthorized response.
- Logging out clears the session and returns the unauthenticated state on the site.
- Opening `/admin/users` as a manager shows the read-only users list.
- Opening `/admin/users` as a non-manager returns a forbidden response and the admin UI shows that clearly.
- `GET /health` returns application and database health.
- The repository includes runnable deployment files, tests, specs, and README instructions.

