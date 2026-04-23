# Scope

## In Scope

- Email and password login.
- Session-based authentication using an HTTP cookie.
- Two roles:
  - `manager`
  - `user`
- A site page visible to authenticated users.
- An admin users page visible only to `manager`.
- Initial seed users loaded from environment variables.
- User list read capability for the admin users page.

## Out of Scope

- Self-sign-up.
- Password reset.
- Email verification.
- Profile editing.
- User creation, update, or deletion from the UI.
- Audit log.
- Multi-tenant behavior.
- Fine-grained permissions beyond role checks.
- Any page other than login, site, and admin users.
