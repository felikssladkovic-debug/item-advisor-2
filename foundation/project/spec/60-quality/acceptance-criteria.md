# Acceptance Criteria

## AC-01 Login Success

- Given valid seeded credentials
- when the user submits the login form
- then the system creates a session
- and redirects the user to `/site`

## AC-02 Login Failure

- Given invalid credentials
- when the user submits the login form
- then the system shows an authentication error
- and does not create a session

## AC-03 Site Access

- Given an authenticated user
- when the user opens `/site`
- then the site page is displayed

## AC-04 Admin Access

- Given an authenticated manager
- when the manager opens `/admin/users`
- then the user list is displayed

## AC-05 Admin Denial

- Given an authenticated regular user
- when the user opens `/admin/users`
- then access is denied
- and the UI routes the user back to `/site`
