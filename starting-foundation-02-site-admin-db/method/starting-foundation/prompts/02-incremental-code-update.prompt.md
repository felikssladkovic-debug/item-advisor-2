---
id: starting-foundation.prompts.02-incremental-code-update.prompt
title: Incremental Code Update Prompt
type: prompt
status: accepted
version: 0.1
links:
  parent: starting-foundation.prompts.index
  children: []
  related:
    - rules.project-lifecycle
    - rules.change-policy
---

# Incremental Code Update Prompt

## Prompt

```text
You are working inside the project folder.

Read:

- ../method/rules/
- current ideas/
- current decisions/
- current spec/
- existing generated code
- checks/

Apply only the changes required by the spec delta.

Do not rewrite unrelated parts.

Do not add features not present in spec.

Preserve existing behavior unless the spec explicitly changes it.

Update tests or check scripts when required.

After changes, report:

- spec files used
- code files changed
- tests/checks changed
- acceptance checks to run
- risks or assumptions
```

## Links

- Parent: [[starting-foundation.prompts.index]]
- Related: [[rules.project-lifecycle]], [[rules.change-policy]]
