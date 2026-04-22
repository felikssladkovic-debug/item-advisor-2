# Data Init

On backend startup:
- ensure indexes for `users.id` and `users.email`
- ensure the configured manager seed user exists
- ensure the configured regular seed user exists

Default seed credentials:
- manager: `manager@example.com` / `manager123`
- user: `user@example.com` / `user123`

Seeding is additive for this version. Existing users with the same seed email are not overwritten.

