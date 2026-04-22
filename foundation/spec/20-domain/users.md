# Users

Collection: `users`

Application fields:
- `id`
- `email`
- `password_hash`
- `role`
- `created_at`

Constraints:
- `email` is unique
- `id` is unique
- `role` must be `user` or `manager`

API responses never expose `password_hash`.

