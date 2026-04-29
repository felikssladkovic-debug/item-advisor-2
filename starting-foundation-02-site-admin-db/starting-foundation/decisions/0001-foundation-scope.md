---
id: starting-foundation.decisions.0001-foundation-scope
title: Foundation Scope: Site, Admin, Shared Database
type: decision
status: accepted
version: 0.1
links:
  parent: starting-foundation.decisions.index
  children: []
  related:
    - starting-foundation.ideas.accepted.001-application-shape
    - starting-foundation.spec.01-architecture
---

# Foundation Scope: Site, Admin, Shared Database

## Context

The barebone foundation proves the method-wiki workflow but does not assume any application shape.

The next foundation should prove the minimal deployable shape of a real web project.

## Decision

Create a foundation with:

- site frontend;
- site backend;
- admin frontend;
- admin backend;
- shared database.

The foundation must remain minimal and must not implement business functionality.

## Consequences

Codex must generate a multi-component project instead of a single application.

Acceptance checks must verify both frontend/backend pairs and shared database availability.

## Links

- Parent: [[starting-foundation.decisions.index]]
- Related: [[starting-foundation.ideas.accepted.001-application-shape]], [[starting-foundation.spec.01-architecture]]
