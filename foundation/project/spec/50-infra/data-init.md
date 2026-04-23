# Data Initialization

## Seed Rules

- On backend startup, ensure the manager seed user exists.
- On backend startup, ensure the regular user seed user exists.
- If a seed user already exists by email, do not create a duplicate.
- Seeded users must receive roles:
  - manager seed -> `manager`
  - regular user seed -> `user`
