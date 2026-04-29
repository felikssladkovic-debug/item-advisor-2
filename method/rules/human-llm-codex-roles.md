---
id: rules.human-llm-codex-roles
title: Human / LLM / Codex Roles
type: rule
status: draft
version: 0.2
links:
  parent: rules.workflow-overview
  children: []
  related:
    - rules.project-lifecycle
    - rules.traceability-policy
    - rules.review-policy
---

# Human / LLM / Codex Roles

## Purpose

Clarify who is responsible for which part of the work.

<a id="human-role"></a>
## Human Role

The human owns goals, priorities, acceptance criteria, product decisions, architecture decisions, and final approval.

The human may edit ideas, specs, decisions, prompts, and checks.

The human should not manually edit generated application code. Application code is a derived artifact produced from spec.

<a id="llm-role"></a>
## LLM Role

The LLM helps transform rough intent into structured method artifacts: specs, prompts, checklists, review notes, and explanations.

The LLM may propose spec changes and promotion of useful discovered behavior, but these changes require human approval.

<a id="codex-role"></a>
## Codex Role

Codex operates inside the project folder and changes code/files according to the current prompt and method context.

Codex must not silently invent a different architecture when a spec already defines one.

Codex must not add behavior that is not described in the spec or explicitly requested by the current prompt.

## Links

- Parent: [[rules.workflow-overview]]
- Related: [[rules.project-lifecycle]], [[rules.traceability-policy]], [[rules.review-policy]]
