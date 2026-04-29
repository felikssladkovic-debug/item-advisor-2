---
id: starting-foundation.spec.01-architecture
title: Architecture
type: spec
status: accepted
version: 0.2
links:
  parent: starting-foundation.spec.index
  children: []
  related:
    - starting-foundation.ideas.000-project-intent
    - starting-foundation.ideas.accepted.001-application-shape
    - starting-foundation.decisions.0001-foundation-scope
    - starting-foundation.spec.02-applications
    - starting-foundation.spec.03-database
---

# Architecture

## Components

### site-frontend

Browser-facing public website.

Calls site-backend.

### site-backend

Backend API for the public website.

Checks database availability.

### admin-frontend

Browser-facing admin placeholder application.

Calls admin-backend.

### admin-backend

Backend API for the admin application.

Checks database availability.

### database

Shared database used by both backends.

## Component communication

```text
site-frontend -> site-backend -> database
admin-frontend -> admin-backend -> database
```

## Restrictions

- site-frontend must not call admin-backend.
- admin-frontend must not call site-backend.
- Frontends must not access the database directly.
- Both backends must use the same database.

## Links

- Parent: [[starting-foundation.spec.index]]
- Related: [[starting-foundation.ideas.000-project-intent]], [[starting-foundation.ideas.accepted.001-application-shape]], [[starting-foundation.decisions.0001-foundation-scope]], [[starting-foundation.spec.02-applications]], [[starting-foundation.spec.03-database]]
