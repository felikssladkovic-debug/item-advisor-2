---
id: rules.foundation-snapshot
title: Foundation Snapshot
type: rule
status: stable
version: 1.0
links:
  parent: rules.workflow-overview
  children: []
  related:
    - rules.validation-contract
    - rules.spec-to-code-mapping
    - rules.ideas-to-spec-mapping
---

# Foundation Snapshot Contract

## Purpose

This document defines how to create a foundation snapshot.

A foundation is a reproducible project state that can be reused as a starting point.

---

## Definition

A foundation is a snapshot of:

- ideas (accepted + boundaries)
- spec
- project-level prompts and checks (optional)
- method version (or method snapshot)

It does NOT include:

- code
- experimental ideas
- temporary artifacts

---

## Preconditions

A foundation may be created only if:

### 1. Ideas are stable

- all relevant ideas are in ideas/accepted/
- ideas/inbox/ is empty or contains only future ideas
- ideas are internally consistent

---

### 2. Spec is complete

- spec fully covers all accepted ideas
- no gaps remain
- no contradictions exist

---

### 3. Code is validated

- code was generated from spec
- code passed code → spec validation
- no unresolved dark code

---

### 4. Acceptance checks passed

- all checks in checks/acceptance-checklist.md passed
- dev mode works
- prod mode works

---

foundation-NN-<description>

## Contents

A foundation must include:

```text
method/starting-foundation/
  ideas/
    accepted/
    boundaries/
    000-project-intent.md

  spec/

  prompts/        (optional but recommended)
  checks/         (optional but recommended)