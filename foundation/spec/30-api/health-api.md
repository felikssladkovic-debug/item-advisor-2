# Health API

## GET /health

Response:

```json
{
  "status": "ok",
  "data": {
    "status": "ok",
    "database": "ok"
  }
}
```

The endpoint verifies MongoDB connectivity with a ping command.

