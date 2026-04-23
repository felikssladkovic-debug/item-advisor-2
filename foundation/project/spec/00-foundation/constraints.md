# Constraints

## Functional Constraints

- The system must not expose admin user data to non-manager users.
- Unauthenticated requests to protected routes must fail.
- The implementation must not add user management actions that are not defined in this spec.

## Technical Constraints

- MongoDB connection settings must come from environment variables.
- Session behavior must use these environment variable names:
  - `ITEMADVISOR_SESSION_SECRET`
  - `ITEMADVISOR_SESSION_COOKIE_NAME`
  - `ITEMADVISOR_SESSION_SECURE`
- Seed account values must use these environment variable names:
  - `ITEMADVISOR_MANAGER_EMAIL`
  - `ITEMADVISOR_MANAGER_PASSWORD`
  - `ITEMADVISOR_USER_EMAIL`
  - `ITEMADVISOR_USER_PASSWORD`
- The generated code must stay within the `project/generated/*` tree.
