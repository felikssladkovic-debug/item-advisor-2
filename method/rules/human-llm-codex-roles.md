---
id: rules.human-llm-codex-roles
title: Human / LLM / Codex Roles
type: rule
status: draft
version: 0.1
links:
  parent: rules.workflow-overview
  children: []
  related:
    - rules.traceability-policy
    - rules.review-policy
---

# Human / LLM / Codex Roles

## Purpose

Clarify who is responsible for which part of the work.

<a id="human-role"></a>
## Human Role

The human owns goals, priorities, acceptance criteria, and final approval. The human does not need to write all implementation details, but must keep the product direction explicit.

<a id="llm-role"></a>
## LLM Role

The LLM helps transform rough intent into structured method artifacts: specs, prompts, checklists, review notes, and explanations. The LLM should preserve traceability rather than produce isolated text.

<a id="codex-role"></a>
## Codex Role

Codex operates inside the project folder and changes code/files according to the current prompt and method context. Codex should not silently invent a different architecture when a spec already defines one.

## Links

- Parent: [[rules.workflow-overview]]
- Related: [[rules.traceability-policy]], [[rules.review-policy]]
