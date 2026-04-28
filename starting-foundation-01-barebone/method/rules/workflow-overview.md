---
id: rules.workflow-overview
title: Workflow Overview
type: rule
status: draft
version: 0.1
links:
  parent: method.index
  children:
    - rules.human-llm-codex-roles
    - rules.traceability-policy
    - rules.change-policy
    - rules.review-policy
    - rules.layers-and-flow
  related:
    - rules.repository-model
---

# Workflow Overview

## Purpose

Define the minimum repeatable workflow for developing a project while preserving the chain:

```text
business idea → spec → code → tests → runtime behavior → next change
```

<a id="workflow-loop"></a>
## Workflow Loop

1. Capture the business idea in a short human-readable form.
2. Convert the idea into explicit specifications.
3. Ask Codex to generate or modify code only from the agreed specification context.
4. Review the generated changes against the specification and method rules.
5. Record important decisions and update links between affected documents.
6. Validate the method-wiki before treating the package as clean.

## Links

- Parent: [[method.index]]
- Children: [[rules.human-llm-codex-roles]], [[rules.traceability-policy]], [[rules.change-policy]], [[rules.review-policy]], [[rules.layers-and-flow]]
- Related: [[rules.repository-model]]
