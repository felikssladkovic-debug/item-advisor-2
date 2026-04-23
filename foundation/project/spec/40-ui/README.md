# UI Specification

## Screens

### Login

- Shows:
  - application title
  - email field
  - password field
  - submit button
  - inline error message on failed login
- Behavior:
  - successful login navigates to `/site`

### Site Page

- Route: `/site`
- Access: authenticated users only
- Shows:
  - current user email
  - current user role
  - navigation links
  - logout action
- Navigation:
  - managers see a link to `/admin/users`
  - regular users do not see the admin link

### Admin Users Page

- Route: `/admin/users`
- Access: `manager` only
- Shows:
  - page title
  - user table
  - columns: email, role, created at
  - link back to site page

## UI States

- Unauthenticated access to protected routes redirects to `/login`.
- Unauthorized access to `/admin/users` redirects to `/site`.
- Loading states are allowed but not required to be elaborate.
