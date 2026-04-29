---
id: rules.validation-contract
title: Validation Contract
type: rule
status: stable
version: 1.0
links:
  parent: rules.workflow-overview
  children: []
  related:
    - rules.spec-to-code-mapping
    - rules.ideas-to-spec-mapping
    - rules.foundation-snapshot
---

# Validation Contract

## Purpose

This document defines how validation must be performed in the system.

Validation ensures that:

- spec correctly reflects ideas
- code correctly implements spec
- no information is lost or invented across layers

---

## Validation Flows

There are two mandatory validation directions:

1. spec → ideas
2. code → spec

Both must be performed regularly.

---

# Part 1: Spec → Ideas Validation

## Goal

Ensure that spec is a correct and complete representation of ideas.

---

## Source of Truth

Validation must be based on:

- ideas/accepted/*
- ideas/boundaries/*
- ideas/000-project-intent.md

---

## Checks

### 1. Coverage

For every accepted idea:

- verify it is represented in spec
- verify it is not partially implemented

---

### 2. No Missing Requirements

Detect:

- ideas not reflected in spec
- constraints not reflected in spec

---

### 3. No Distortion

Detect:

- meaning changes
- simplified or altered behavior
- loss of constraints

---

### 4. No Invention

Detect:

- features present in spec but absent in ideas
- entities not defined in ideas
- behaviors not defined in ideas

---

### 5. Consistency

Check:

- no contradictions between spec sections
- consistent naming
- consistent boundaries

---

## Output

The LLM must produce:

1. coverage report:
   idea → spec mapping

2. list of issues:
    - missing
    - distorted
    - invented

3. clarification questions (if needed)

---

## Rules

- do NOT fix automatically
- do NOT modify spec without approval
- propose changes only

---

# Part 2: Code → Spec Validation

## Goal

Ensure that code is a correct implementation of spec.

---

## Source of Truth

Validation must be based on:

- project/spec/*

Code is not authoritative.

---

## Checks

### 1. Coverage

For every spec requirement:

- verify implementation exists

---

### 2. Missing Implementation

Detect:

- endpoints not implemented
- UI not implemented
- database behavior missing

---

### 3. Behavior Mismatch

Detect:

- response shape mismatch
- UI text mismatch
- incorrect logic

---

### 4. Dark Code Detection

Detect any behavior in code that:

- is not described in spec
- cannot be traced to spec

Examples:

- extra endpoints
- hidden logic
- additional data processing
- implicit behavior

---

### 5. Dependency Check

Detect:

- external services not defined in spec
- libraries introducing behavior

---

### 6. Architecture Violations

Detect:

- forbidden calls between components
- incorrect boundaries
- direct DB access from frontend (if forbidden)

---

## Output

The LLM must produce:

1. mapping report:
   spec → code

2. issue list:
    - missing
    - mismatch
    - dark code

3. suggested actions:
    - fix code
    - update spec
    - escalate to ideas

---

## Rules

- do NOT modify code automatically
- do NOT ignore dark code
- do NOT justify behavior not in spec

---

# Issue Resolution

For each issue:

## Option A: Fix code

If spec is correct:

→ update code

## Option B: Fix spec

If spec is incomplete:

→ update spec (after human approval)

## Option C: Escalate to ideas

If behavior is useful but not defined:

→ propose idea
→ move through ideas → spec

---

# Validation Frequency

Validation must be performed:

- after spec generation
- after code generation
- after incremental updates
- before creating a foundation snapshot

---

# Acceptance Gate

A system is considered valid only if:

- spec passes spec → ideas validation
- code passes code → spec validation
- acceptance checks pass

---

# Core Principle

Validation is not optional.

Without validation:

- spec drifts from ideas
- code drifts from spec
- system becomes unreliable

Validation maintains alignment:

ideas ↔ spec ↔ code