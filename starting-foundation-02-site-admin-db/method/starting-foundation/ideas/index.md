---
id: starting-foundation.ideas.index
title: Starting Foundation / Ideas
type: index
status: accepted
version: 0.2
links:
  parent: starting-foundation.index
  children:
    - starting-foundation.ideas.000-project-intent
    - starting-foundation.ideas.accepted.index
    - starting-foundation.ideas.boundaries.index
    - starting-foundation.ideas.inbox.README
    - starting-foundation.ideas.archive.README
  related:
    - templates.business-idea-template
    - rules.traceability-policy
    - rules.ideas-to-spec-mapping
---

# Ideas

This folder contains the idea layer for the site/admin/database foundation.

## Structure

- `000-project-intent.md` — top-level project intent.
- `accepted/` — approved idea-layer decisions and source of truth for spec generation.
- `boundaries/` — explicit non-goals, constraints, and exclusions.
- `inbox/` — raw ideas under discussion.
- `archive/` — processed idea history.

## Authoritative sources for spec generation

The authoritative idea-layer sources are:

- [[starting-foundation.ideas.000-project-intent]]
- [[starting-foundation.ideas.accepted.index]]
- [[starting-foundation.ideas.boundaries.index]]

The following are not authoritative for spec generation:

- [[starting-foundation.ideas.inbox.README]]
- [[starting-foundation.ideas.archive.README]]

## Lifecycle of a new idea

1. Create a new file in `ideas/inbox/`.
2. Discuss and refine it with LLM and human review.
3. If accepted, create or update a file in `ideas/accepted/` or `ideas/boundaries/`.
4. Move the original inbox file to `ideas/archive/`.
5. Update spec only from authoritative idea-layer sources.

## Links

- Parent: [[starting-foundation.index]]
- Related: [[templates.business-idea-template]], [[rules.traceability-policy]], [[rules.ideas-to-spec-mapping]]
