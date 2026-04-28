---
id: starting-foundation.spec.05-acceptance-criteria
title: Acceptance Criteria
type: spec
status: accepted
version: 0.1
links:
  parent: starting-foundation.spec.index
  children: []
  related:
    - starting-foundation.spec.02-applications
    - starting-foundation.spec.03-database
    - starting-foundation.spec.04-runtime-modes
    - starting-foundation.checks.acceptance-checklist
---

# Acceptance Criteria

The generated code is acceptable only if all checks pass.

## Runtime

- The project starts in development mode.
- The project starts in production mode.
- All five components are present.
- Both frontend applications are reachable from browser.
- Both backend applications expose a database availability endpoint.

## Site

When database is available, site frontend shows:

```text
Site is running. Database is available.
```

When database is unavailable, site frontend shows:

```text
Site is running. Database is unavailable.
```

## Admin

When database is available, admin frontend shows:

```text
Admin placeholder is running. Database is available.
```

When database is unavailable, admin frontend shows:

```text
Admin placeholder is running. Database is unavailable.
```

## Architecture

- site frontend calls only site backend.
- admin frontend calls only admin backend.
- both backends use the same database.
- frontends do not access database directly.

## Tests or check scripts

The generated project must include tests or check scripts that verify:

- site backend database availability response;
- admin backend database availability response;
- site frontend expected text;
- admin frontend expected text.

## Links

- Parent: [[starting-foundation.spec.index]]
- Related: [[starting-foundation.spec.02-applications]], [[starting-foundation.spec.03-database]], [[starting-foundation.spec.04-runtime-modes]], [[starting-foundation.checks.acceptance-checklist]]
