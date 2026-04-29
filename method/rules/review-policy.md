---
id: rules.review-policy
title: Review Policy
type: rule
status: draft
version: 0.1
links:
  parent: rules.workflow-overview
  children: []
  related:
    - rules.roles
    - rules.traceability-policy
---

# Review Policy

## Purpose

Define what should be checked after LLM-2 changes.

## Minimum Review

Check that:

1. the result matches the requested intent;
2. generated files do not introduce a hidden architecture;
3. changed documents keep YAML front matter;
4. method-wiki links and graph remain valid;
5. tests or manual checks are described.

