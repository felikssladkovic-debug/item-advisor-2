---
id: starting-foundation.ideas.accepted.003-site-behavior
title: Site Behavior
type: accepted-idea
status: accepted
version: 0.2
links:
  parent: starting-foundation.ideas.accepted.index
  children: []
  related:
    - starting-foundation.spec.02-applications
---

# Site Behavior

## Decision

The public site has one page.

It displays different text depending on whether the site backend can access the shared database.

## Required texts

When database is available, the public site must show:

```text
Site is running. Database is available.
```

When database is unavailable, the public site must show:

```text
Site is running. Database is unavailable.
```

## Spec mapping

This decision must be represented in:

- `spec/02-applications.md`;
- `spec/05-acceptance-criteria.md`.
