---
id: rules.workflow-overview
title: Workflow Overview
type: rule
status: stable
version: 1.0
links:
  parent: method.index
  children:
    - rules.roles
    - rules.ideas-to-spec-mapping
    - rules.spec-to-code-mapping
    - rules.validation-contract
    - rules.foundation-snapshot
  related:
    - rules.core-principles-for-workflow
---

# Workflow Overview

## Purpose

This document defines how a project evolves using the method.

It describes:

- the sequence of steps
- inputs and outputs of each step
- validation points
- transition rules between layers

Role definitions are described in [[rules.roles]].

---

## System Model

### Layers

ideas → spec → code

### Reverse validation flows

- spec → ideas
- code → spec

---

## High-Level Workflow

### Summary

1. Initialize project
2. Add ideas
3. Accept ideas
4. Generate spec (for ideas)
5. Validate spec against ideas
6. Generate code
7. Run acceptance checks
8. Validate code against spec
9. Resolve issues
10. Create foundation snapshot

---

## Detailed Steps

### Step 1. Initialize project

- Select a starting foundation
- Run start.sh - this will create folder project (which is the project-workspace)

```bash
./start.sh
```

Result: project workspace is created. It includes:
- project/ideas
- project/spec
- project/prompts
- project/checks

---

### Step 2. Add ideas

Human creates new ideas in:

ideas/inbox/

Example:

ideas/inbox/007-roles.md

These ideas may be:
- incomplete
- ambiguous
- exploratory

LLM-2 may:
- ask clarifying questions
- propose refinements
- suggest structure

Important:

ideas/inbox is NOT a source of truth.

---

### Step 3. Accept ideas

After discussion, the human makes decisions.

Move or rewrite ideas into:

ideas/accepted/

If the idea defines constraints or exclusions:

ideas/boundaries/

Move original drafts to:

ideas/archive/

Important:

Only the following are authoritative:

ideas/accepted/*
ideas/boundaries/*
ideas/000-project-intent.md

---

### Step 4. Generate spec (for ideas)

LLM-2 generates spec from accepted ideas.

Must follow:
[[rules.ideas-to-spec-mapping]]

Rules:
- follow method/rules/ideas-to-spec-mapping.md
- use only accepted and boundaries
- do not use ideas/inbox
- do not invent behavior

It is supposed:
- The LLM may ask clarifying questions.
- The human must review and approve the proposed spec changes before they become authoritative.

Output:
- spec files
- mapping report: ideas → spec

If gaps exist:
- report them
- do not fill automatically

---

### Step 5. Validate spec against ideas

Perform validation:

spec → ideas

Must follow:

[[rules.validation-contract]] (Part 1)

Check:
- all accepted ideas are covered
- no distorted meaning
- no contradictions
- no invented features

If issues found:
- refine ideas
- update spec

Output:
- coverage report
- issue list
- clarification questions (if needed)

Important:

Do NOT modify spec automatically.

---

### Step 6. Generate code

LLM-2 generates code from spec.

Must follow:

[[rules.spec-to-code-mapping]]

Rules:
- spec is the only source of truth
- do not invent features
- implement all defined behavior

Output:
- application code
- run scripts (dev/prod)
- tests or check scripts

---

### Step 7. Run acceptance checks

Execute:

checks/acceptance-checklist.md

Verify:
- system starts (dev mode)
- system starts (prod mode)
- frontends are reachable
- backends respond correctly
- database behavior matches spec
- architecture constraints are respected

Important:
- Code is NOT deployable unless all checks pass.

---

### Step 8. Validate code against spec

Perform validation:

code → spec

Must follow:

[[rules.validation-contract]] (Part 2)

Check:
- missing implementations
- behavior mismatches
- architecture violations
- undocumented dependencies
- undocumented endpoints
- undocumented data structures
- dark code

Output:
- mapping report: spec → code
- issue list
- suggested actions

---

### Step 9. Resolve issues

For each issue:
- Option A: fix code
- Option B: fix spec
- Option C: escalate to ideas

If useful behavior exists in code but not in spec:

- propose promotion
- human decides:
    - remove
    - promote to ideas/spec
    - postpone

Important:
- No automatic promotion is allowed.

---

### Step 10. Create foundation snapshot

When project reaches stable state:
- ideas are accepted and consistent
- spec is complete
- code passes acceptance checks

Create foundation according to:

[[rules.foundation-snapshot]]

Important:
- foundation is a snapshot, not the method.
- foundation is a snapshot of ideas + spec
- foundation is reproducible starting point
- foundation is immutable

---

## Method Evolution

If problems are discovered:

1. Human discusses with LLM-1
2. Update method/rules
3. Future projects use updated method

Existing foundations:
- are NOT automatically updated
- may require migration if reused

---

## Core Principles
Core principles, project workflow is designed with, see: [[rules.core-principles-for-workflow]]
