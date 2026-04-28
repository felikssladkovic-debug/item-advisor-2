---
id: starting-foundation.prompts.01-generate-code-from-spec.prompt
title: Generate Code From Spec Prompt
type: prompt
status: accepted
version: 0.1
links:
  parent: starting-foundation.prompts.index
  children: []
  related:
    - rules.project-lifecycle
    - starting-foundation.spec.index
    - starting-foundation.checks.acceptance-checklist
---

# Generate Code From Spec Prompt

## Prompt

```text
You are working inside the project folder.

Read all files in:

- ../method/rules/
- ideas/
- decisions/
- spec/
- checks/

Generate the application code strictly according to spec.

Do not invent business features.

Do not implement functionality listed in non-goals or out-of-scope documents.

The result must include:

- site frontend
- site backend
- admin frontend
- admin backend
- shared database
- development startup command
- production startup command
- tests or check scripts
- README with exact run instructions

The generated system must satisfy all acceptance criteria.

Do not ask the human to manually write code.

After generation, report:

- generated structure
- startup commands
- test/check commands
- any assumptions
- any acceptance criteria not yet satisfied
```

## Links

- Parent: [[starting-foundation.prompts.index]]
- Related: [[rules.project-lifecycle]], [[starting-foundation.spec.index]], [[starting-foundation.checks.acceptance-checklist]]
