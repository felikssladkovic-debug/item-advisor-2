# Site

Route: `/`

Behavior:
- On load, the page calls `GET /api/v1/auth/me`.
- If the user is not authenticated, the page shows a login form.
- If the user is authenticated, the page shows user id, email, and role.
- The authenticated state includes a logout button.

This version has no other public pages.

