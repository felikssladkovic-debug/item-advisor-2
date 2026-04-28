---
id: starting-foundation.prompts.03-validate-code-against-spec.prompt
title: Validate Code Against Spec Prompt
type: prompt
status: accepted
version: 0.1
links:
  parent: starting-foundation.prompts.index
  children: []
  related:
    - rules.project-lifecycle
    - rules.traceability-policy
    - starting-foundation.spec.index
---

# Validate Code Against Spec Prompt

## Prompt

```text
You are working inside the project folder.

Compare generated code against spec.

Report:

1. implemented requirements
2. missing requirements
3. behavior mismatches
4. undocumented endpoints
5. undocumented dependencies
6. undocumented data structures
7. dark code: behavior present in code but absent from spec
8. recommended fixes

Do not modify code automatically.

If useful undocumented behavior is found, propose whether to:

- remove it from code
- promote it into ideas/spec
- postpone decision

Promotion is never automatic. It requires human approval.
```

## Links

- Parent: [[starting-foundation.prompts.index]]
- Related: [[rules.project-lifecycle]], [[rules.traceability-policy]], [[starting-foundation.spec.index]]
