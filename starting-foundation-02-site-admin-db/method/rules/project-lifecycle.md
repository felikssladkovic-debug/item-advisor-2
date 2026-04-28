---
id: rules.project-lifecycle
title: Project Lifecycle
type: rule
status: draft
version: 0.1
links:
  parent: rules.workflow-overview
  children: []
  related:
    - rules.layers-and-flow
    - rules.human-llm-codex-roles
    - rules.traceability-policy
    - rules.change-policy
    - rules.review-policy
---

# Project Lifecycle

## Purpose

Define the repeatable lifecycle for developing a project through ideas, specifications, prompts, generated code, checks, and runtime validation.

## Core layers

Project development is organized around three primary layers:

```text
ideas -> spec -> code
```

The primary flow is:

```text
ideas -> spec -> code
```

Reverse validation flows are:

```text
code -> spec
spec -> ideas
```

The spec is treated as **code in English**. Generated source code is a derived artifact.

## Human and LLM responsibilities

Humans own:

- ideas;
- approvals;
- product and architecture decisions;
- acceptance of spec changes;
- acceptance of discovered behavior promotion;
- production deployment decision.

LLM/Codex owns:

- drafting spec from ideas;
- generating code from spec;
- proposing controlled code deltas;
- validating code against spec;
- proposing fixes;
- proposing promotion of discovered behavior.

Humans should not manually edit generated application code.

## Lifecycle operations

### A. Initialize project

Create a project workspace from a selected starting foundation.

### B. Generate code from spec

Generate or regenerate application code from the current spec.

This operation may be:

- clean generation;
- regeneration after removing existing code;
- regeneration after major spec changes.

The source of truth is always spec, not code.

### C. Incremental code update

Apply a controlled code delta based on a spec delta.

This operation is used when:

- existing code already exists;
- spec changed locally;
- full regeneration is unnecessary or risky.

The LLM must:

- read the relevant spec;
- read the existing code;
- change only what is required;
- preserve unrelated behavior;
- update tests/checks when required;
- report what was changed.

### D. Add idea

A human adds a new idea, decision, constraint, or product intention.

Ideas should follow the existing ideas format used in the project.

### E. Refine idea into spec

LLM converts an approved idea into a draft spec change.

The LLM may ask clarifying questions.

The human must review and approve the proposed spec changes before they become authoritative.

### F. Validate spec against ideas

Check that the spec correctly reflects the ideas layer.

This process may detect:

- missing requirements;
- distorted meaning;
- premature technical decisions;
- behavior not justified by ideas.

### G. Validate code against spec

Check generated code against the spec.

This includes dark code detection.

The validation must detect:

- missing implementation;
- behavior mismatch;
- undocumented endpoints;
- undocumented data structures;
- undocumented dependencies;
- extra behavior not described in spec;
- hardcoded behavior not justified by spec.

### H. Propose promotion of discovered behavior

If useful behavior is discovered in code but is not present in spec, the LLM may propose promotion.

Promotion is never automatic.

The human must decide:

- remove it from code;
- keep it by adding it to ideas/spec;
- postpone the decision.

### I. Run acceptance checks

Code is not deployable until acceptance checks pass.

Acceptance checks must verify:

- runtime startup;
- expected endpoints;
- expected UI behavior;
- database behavior;
- development mode;
- production mode.

### J. Update method and propagate changes to foundations

When method rules change, existing starting foundations may become outdated.

Any method update must include a propagation decision:

- update all foundations;
- update only new foundations;
- add compatibility note;
- add migration note.

## Links

- Parent: [[rules.workflow-overview]]
- Related: [[rules.layers-and-flow]], [[rules.human-llm-codex-roles]], [[rules.traceability-policy]], [[rules.change-policy]], [[rules.review-policy]]
