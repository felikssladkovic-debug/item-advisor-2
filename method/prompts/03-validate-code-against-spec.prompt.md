---
id: prompts.03-validate-code-against-spec.prompt
title: Validate Code Against Spec Prompt
type: prompt
status: accepted
version: 0.2
links:
  parent: prompts.index
  children: []
  related:
    - rules.workflow-overview
    - rules.spec-to-code-mapping
---

# Validate Code Against Spec Prompt

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
- generated code

Do NOT treat `ideas/inbox/` or `ideas/archive/` as authoritative input.

Compare generated code against spec.

Also verify that spec traces back to authoritative idea-layer sources according to ../method/rules/ideas-to-spec-mapping.md.

Report:

1. implemented requirements
2. missing requirements
3. behavior mismatches
4. undocumented endpoints
5. undocumented dependencies
6. undocumented data structures
7. dark code: behavior present in code but absent from spec
8. spec statements that do not trace back to accepted ideas or boundaries
9. recommended fixes

Do not modify code automatically.

If useful undocumented behavior is found, propose whether to:

- remove it from code
- promote it into ideas/accepted or ideas/boundaries through human approval
- postpone decision

Promotion is never automatic.
```
