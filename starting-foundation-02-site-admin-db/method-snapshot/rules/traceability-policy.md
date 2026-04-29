---
id: rules.traceability-policy
title: Traceability Policy
type: rule
status: draft
version: 0.1
links:
  parent: rules.workflow-overview
  children: []
  related:
    - rules.consistency-policy
    - templates.spec-template
    - templates.decision-log-template
---

# Traceability Policy

## Purpose

Prevent business intent, specification, and code from drifting apart.

<a id="traceability-chain"></a>
## Traceability Chain

Every meaningful change should be traceable across at least these layers:

```text
why → what → how → where → how verified
```

- **why**: business idea, user need, or technical rationale;
- **what**: expected behavior or constraint;
- **how**: implementation approach;
- **where**: files, modules, APIs, or data structures affected;
- **how verified**: manual check, test, lint, or runtime observation.

