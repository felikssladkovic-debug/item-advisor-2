---
id: starting-foundation.spec.03-database
title: Database
type: spec
status: draft
version: 0.2
links:
  parent: starting-foundation.spec.index
  children: []
  related:
    - starting-foundation.ideas.accepted.002-database
---

# Database

## Shared Database

The database is shared by:

- site backend;
- admin backend.

## Required Database Behavior

The minimum required database behavior in this foundation is:

- site backend can check whether the shared database is available;
- admin backend can check whether the shared database is available.

## Excluded Database Scope

This foundation does not require:

- business collections;
- business tables;
- production business schema.
