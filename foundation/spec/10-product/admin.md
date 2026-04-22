# Admin

Route: `/admin/users`

Behavior:
- The page requests `GET /api/v1/admin/users`.
- Only users with role `manager` can access the data successfully.
- The page is read-only.
- If the current session is not allowed, the page shows a clear error message.

This version has no admin create, edit, delete, or pagination features.

