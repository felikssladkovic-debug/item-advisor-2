# Test Scenarios

## API Scenarios

- Login succeeds for manager seed credentials.
- Login succeeds for regular user seed credentials.
- Login fails for incorrect password.
- Session endpoint returns authenticated user after login.
- Admin users endpoint returns `403` for regular user.
- Admin users endpoint returns user list for manager.

## UI Scenarios

- Login form submits and navigates to site page.
- Site page hides admin link for regular user.
- Site page shows admin link for manager.
- Admin users page renders the returned user list.
