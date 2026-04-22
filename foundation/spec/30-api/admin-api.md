# Admin API

## GET /api/v1/admin/users

Purpose:
- return the full read-only user list for managers

Success response shape:

```json
{
  "status": "ok",
  "data": [
    {
      "id": "string",
      "email": "manager@example.com",
      "role": "manager",
      "created_at": "2026-01-01T00:00:00Z"
    }
  ]
}
```

Forbidden response shape:

```json
{
  "status": "error",
  "error": {
    "code": "forbidden",
    "message": "Manager role required."
  }
}
```

