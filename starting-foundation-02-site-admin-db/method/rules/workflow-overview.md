---
id: rules.workflow-overview
title: Workflow Overview
type: rule
status: draft
version: 0.2
links:
  parent: method.index
  children:
    - rules.project-lifecycle
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
ideas → spec → code → tests/checks → runtime behavior → next change
```

<a id="workflow-loop"></a>
## Workflow Loop

1. Capture the business idea in a short human-readable form.
2. Convert the idea into explicit specifications.
3. Ask Codex to generate or modify code only from the agreed specification context.
4. Review the generated changes against the specification and method rules.
5. Run acceptance checks before treating code as deployable.
6. Record important decisions and update links between affected documents.
7. Validate the method-wiki before treating the package as clean.

## Lifecycle

The detailed lifecycle operations are defined in [[rules.project-lifecycle]].

## Links

- Parent: [[method.index]]
- Children: [[rules.project-lifecycle]], [[rules.human-llm-codex-roles]], [[rules.traceability-policy]], [[rules.change-policy]], [[rules.review-policy]], [[rules.layers-and-flow]]
- Related: [[rules.repository-model]]
