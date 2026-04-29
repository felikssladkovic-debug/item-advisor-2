---
id: starting-foundation.index
title: Starting Foundation / Site Admin DB
type: scaffold
status: draft
version: 0.2
links:
  parent: method.index
  children:
    - starting-foundation.ideas.index
    - starting-foundation.spec.index
    - starting-foundation.decisions.index
    - starting-foundation.change-requests.index
    - starting-foundation.prompts.index
    - starting-foundation.checks.index
  related:
    - rules.workflow-overview
    - rules.project-lifecycle
    - rules.repository-model
    - prompts.01-bootstrap-project.prompt
---

# Starting Foundation / Site Admin DB

This folder is the pre-created scaffold that `start.sh` copies into `project-workspace/project/`.

It defines a minimal deployable multi-application system:

- site frontend;
- site backend;
- admin frontend;
- admin backend;
- shared database.

It intentionally does not define real business functionality yet.

## Folders

- [[starting-foundation.ideas.index]] — idea layer: project intent, accepted ideas, boundaries, inbox, and archive.
- [[starting-foundation.spec.index]] — initial specifications for the generated system.
- [[starting-foundation.decisions.index]] — decisions that shape the foundation.
- [[starting-foundation.change-requests.index]] — planned deltas after the first generated version exists.
- [[starting-foundation.prompts.index]] — prompts to run inside the generated project workspace.
- [[starting-foundation.checks.index]] — acceptance checks used as deployment gate.

## Rule

LLM-2 may generate implementation code from this scaffold, but must not add behavior that is absent from the spec or explicitly marked as out of scope. Inbox and archive ideas are not source of truth for code generation.
