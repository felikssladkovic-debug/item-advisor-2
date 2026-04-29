---
id: starting-foundation.ideas.accepted.004-admin-behavior
title: Admin Behavior
type: accepted-idea
status: accepted
version: 0.2
links:
  parent: starting-foundation.ideas.accepted.index
  children: []
  related:
    - starting-foundation.spec.02-applications
---

# Admin Behavior

## Decision

The admin frontend has one page.

It displays different text depending on whether the admin backend can access the shared database.

## Required texts

When database is available, the admin frontend must show:

```text
Admin placeholder is running. Database is available.
```

When database is unavailable, the admin frontend must show:

```text
Admin placeholder is running. Database is unavailable.
```

## Spec mapping

This decision must be represented in:

- `spec/02-applications.md`;
- `spec/05-acceptance-criteria.md`.
