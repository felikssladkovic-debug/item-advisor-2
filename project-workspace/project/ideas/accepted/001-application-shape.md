---
id: starting-foundation.ideas.accepted.001-application-shape
title: Application Shape
type: accepted-idea
status: accepted
version: 0.2
links:
  parent: starting-foundation.ideas.accepted.index
  children: []
  related:
    - starting-foundation.spec.01-architecture
---

# Application Shape

## Decision

The generated project must consist of five runtime components:

1. site frontend;
2. site backend;
3. admin frontend;
4. admin backend;
5. shared database.

## Rationale

This foundation must prove the future project shape early: public site and admin are separate applications, each with its own backend, while both backends use the same database.

## Spec mapping

This decision must be represented in:

- `spec/01-architecture.md`;
- `spec/04-runtime-modes.md`;
- `spec/05-acceptance-criteria.md`.
