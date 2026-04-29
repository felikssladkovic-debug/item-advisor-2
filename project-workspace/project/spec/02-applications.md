---
id: starting-foundation.spec.02-applications
title: Applications
type: spec
status: draft
version: 0.2
links:
  parent: starting-foundation.spec.index
  children: []
  related:
    - starting-foundation.ideas.000-project-intent
    - starting-foundation.ideas.accepted.003-site-behavior
    - starting-foundation.ideas.accepted.004-admin-behavior
    - starting-foundation.ideas.accepted.005-admin-scope
---

# Applications

## Public Site

The public site frontend has one page.

The page displays different text depending on whether the site backend can access the shared database.

When the shared database is available to the site backend, the page must show exactly:

```text
Site is running. Database is available.
```

When the shared database is unavailable to the site backend, the page must show exactly:

```text
Site is running. Database is unavailable.
```

## Admin Application

The admin frontend has one page.

The admin application is only a placeholder in this foundation.

The page displays different text depending on whether the admin backend can access the shared database.

When the shared database is available to the admin backend, the page must show exactly:

```text
Admin placeholder is running. Database is available.
```

When the shared database is unavailable to the admin backend, the page must show exactly:

```text
Admin placeholder is running. Database is unavailable.
```

## Admin Placeholder Constraint

The admin application is a separate web application, but it is not a functional admin panel in this foundation.
