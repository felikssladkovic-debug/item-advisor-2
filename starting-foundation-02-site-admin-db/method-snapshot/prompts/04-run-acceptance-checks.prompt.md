---
id: prompts.04-run-acceptance-checks.prompt
title: Run Acceptance Checks Prompt
type: prompt
status: accepted
version: 0.1
links:
  parent: prompts.index
  children: []
  related:
    - rules.workflow-mappings
---

# Run Acceptance Checks Prompt

## Prompt

```text
You are working inside the project folder.

Run or create the required acceptance checks for the generated project.

Use checks/acceptance-checklist.md as the deployment gate.

Verify at minimum:

- development mode startup
- production mode startup
- site frontend expected text when database is available
- admin frontend expected text when database is available
- site backend database availability response
- admin backend database availability response
- database unavailable behavior
- frontend/backend communication restrictions

Report:

- commands executed
- passed checks
- failed checks
- fixes required before production deployment

Code is not deployable until acceptance checks pass.
```
