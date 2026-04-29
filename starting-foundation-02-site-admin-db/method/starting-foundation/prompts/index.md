---
id: starting-foundation.prompts.index
title: Starting Foundation / Project Prompts
type: scaffold
status: draft
version: 0.2
links:
  parent: starting-foundation.index
  children:
    - starting-foundation.prompts.01-generate-code-from-spec.prompt
    - starting-foundation.prompts.02-incremental-code-update.prompt
    - starting-foundation.prompts.03-validate-code-against-spec.prompt
    - starting-foundation.prompts.04-run-acceptance-checks.prompt
  related:
    - rules.project-lifecycle
    - rules.ideas-to-spec-mapping
---

# Project Prompts

These prompts are copied into `project-workspace/project/prompts/` by `start.sh`.

They are used after the project workspace is initialized. Code-generation prompts must use only authoritative idea-layer sources: `ideas/000-project-intent.md`, `ideas/accepted/`, and `ideas/boundaries/`.

## Documents

- [[starting-foundation.prompts.01-generate-code-from-spec.prompt]]
- [[starting-foundation.prompts.02-incremental-code-update.prompt]]
- [[starting-foundation.prompts.03-validate-code-against-spec.prompt]]
- [[starting-foundation.prompts.04-run-acceptance-checks.prompt]]
