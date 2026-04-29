---
id: starting-foundation.ideas.accepted.002-database
title: Shared Database
type: accepted-idea
status: accepted
version: 0.2
links:
  parent: starting-foundation.ideas.accepted.index
  children: []
  related:
    - starting-foundation.spec.03-database
---

# Shared Database

## Decision

The database is shared by site backend and admin backend.

## Scope

The database does not need business collections, business tables, or production business schema in this foundation.

The minimum requirement is database availability checking from both backends.

## Spec mapping

This decision must be represented in:

- `spec/01-architecture.md`;
- `spec/03-database.md`;
- `spec/05-acceptance-criteria.md`.
