# Roles

Supported roles:
- `user`
- `manager`

Permissions:
- `user` can authenticate and read their own auth state
- `manager` can do everything a `user` can do and can read `/api/v1/admin/users`

No other roles or RBAC layers exist in this version.

