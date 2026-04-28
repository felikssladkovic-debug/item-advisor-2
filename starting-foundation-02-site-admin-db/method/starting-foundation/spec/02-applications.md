---
id: starting-foundation.spec.02-applications
title: Applications
type: spec
status: accepted
version: 0.1
links:
  parent: starting-foundation.spec.index
  children: []
  related:
    - starting-foundation.ideas.01-accepted-decisions
    - starting-foundation.spec.01-architecture
    - starting-foundation.spec.05-acceptance-criteria
---

# Applications

## Site frontend

The site frontend must render one page.

It must call the site backend health/database endpoint.

If database is available, show:

```text
Site is running. Database is available.
```

If database is unavailable, show:

```text
Site is running. Database is unavailable.
```

## Site backend

The site backend must expose an endpoint that returns database availability.

Expected logical response:

```json
{
  "service": "site-backend",
  "databaseAvailable": true
}
```

`databaseAvailable` may be `true` or `false`.

## Admin frontend

The admin frontend must render one page.

It must call the admin backend health/database endpoint.

If database is available, show:

```text
Admin placeholder is running. Database is available.
```

If database is unavailable, show:

```text
Admin placeholder is running. Database is unavailable.
```

## Admin backend

The admin backend must expose an endpoint that returns database availability.

Expected logical response:

```json
{
  "service": "admin-backend",
  "databaseAvailable": true
}
```

`databaseAvailable` may be `true` or `false`.

## Links

- Parent: [[starting-foundation.spec.index]]
- Related: [[starting-foundation.ideas.01-accepted-decisions]], [[starting-foundation.spec.01-architecture]], [[starting-foundation.spec.05-acceptance-criteria]]
