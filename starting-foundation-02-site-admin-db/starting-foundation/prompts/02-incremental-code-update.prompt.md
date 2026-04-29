---
id: starting-foundation.prompts.02-incremental-code-update.prompt
title: Incremental Code Update Prompt
type: prompt
status: accepted
version: 0.2
links:
  parent: starting-foundation.prompts.index
  children: []
  related:
    - rules.project-lifecycle
    - rules.ideas-to-spec-mapping
    - starting-foundation.spec.index
---

# Incremental Code Update Prompt

## Prompt

```text
You are working inside an existing generated project.

Read:

- ../method/rules/
- ideas/000-project-intent.md
- ideas/accepted/
- ideas/boundaries/
- spec/
- checks/
- existing code

Do NOT use these folders as source of truth for implementation:

- ideas/inbox/
- ideas/archive/

Apply only the changes required by the current spec delta.

Do not rewrite unrelated parts.

Do not add features not present in spec.

Do not implement behavior listed in boundaries or non-goals.

If the spec delta appears to require an idea-layer decision that is missing from `ideas/accepted/` or `ideas/boundaries/`, stop and report the gap.

After changes, report:

- authoritative idea files used
- spec files used
- code files changed
- tests/checks changed
- acceptance checks to run
- any risks or assumptions
```

## Links

- Parent: [[starting-foundation.prompts.index]]
- Related: [[rules.project-lifecycle]], [[rules.ideas-to-spec-mapping]], [[starting-foundation.spec.index]]
