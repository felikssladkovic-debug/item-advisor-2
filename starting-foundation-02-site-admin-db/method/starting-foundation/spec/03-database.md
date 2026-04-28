---
id: starting-foundation.spec.03-database
title: Database
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

# Database

The system must include one shared database.

Both backends must be configured to connect to the same database.

The database does not need business collections or tables yet.

The minimum requirement is that both backends can check database connectivity.

The generated project may create a minimal technical collection/table for health checks if needed.

No business schema is required.

## Links

- Parent: [[starting-foundation.spec.index]]
- Related: [[starting-foundation.ideas.01-accepted-decisions]], [[starting-foundation.spec.01-architecture]], [[starting-foundation.spec.05-acceptance-criteria]]
