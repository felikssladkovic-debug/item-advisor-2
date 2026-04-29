---
id: prompts.01-generate-spec-from-ideas.prompt
title: Generate Code From Spec Prompt
type: prompt
status: accepted
version: 0.2
links:
  parent: prompts.index
  children: []
  related:
    - rules.workflow-overview
    - rules.ideas-to-spec-mapping
---

# Generate Code From Spec Prompt

## Prompt

```text
You are working inside the project folder.

Read the method rules:

- ../method/rules/

Read authoritative idea-layer sources:

- ideas/000-project-intent.md
- ideas/accepted/
- ideas/boundaries/

Do NOT use these folders as source of truth for implementation:

- ideas/inbox/
- ideas/archive/

Read implementation specifications and checks:

- spec/
- checks/

Before generating code, validate that spec fully covers the authoritative idea-layer sources according to ../method/rules/ideas-to-spec-mapping.md.

If spec does not cover accepted ideas or boundaries, stop and report missing mappings instead of generating code.

Generate the application code strictly according to spec.

Do not invent business features.

Do not implement functionality listed in non-goals, boundaries, or out-of-scope documents.

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
- idea-to-spec coverage summary
- any assumptions
- any acceptance criteria not yet satisfied
```
