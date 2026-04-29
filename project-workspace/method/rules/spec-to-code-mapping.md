---
id: rules.spec-to-code-mapping
title: Spec to Code Mapping
type: rule
status: stable
version: 1.0
links:
  parent: rules.workflow-overview
  children: []
  related:
    - rules.validation-contract
    - rules.ideas-to-spec-mapping
    - rules.roles
---

# Spec → Code Mapping Contract

## Purpose

This document defines how code must be generated from spec.

The goal is:

- eliminate dark code
- ensure full traceability
- prevent uncontrolled behavior
- make code reproducible from spec

---

## Source of Truth

Code must be generated ONLY from:

- project/spec/*

Code must NOT be based on:

- ideas/*
- previous code (as authority)
- assumptions
- conventions not explicitly defined in spec

---

## Coverage Requirement

Every requirement in spec must be implemented in code.

For each spec file:

- identify all behaviors
- identify all components
- identify all interactions

Each must have a corresponding implementation in code.

---

## No Invention Rule

Code must NOT introduce:

- new features not present in spec
- new endpoints not defined in spec
- new data structures not defined in spec
- new external dependencies not defined in spec

If something is missing in spec:

- report a gap
- do NOT implement it

---

## Mapping Rules

### Architecture → Structure

spec/01-architecture.md defines:

- services / applications
- boundaries
- communication paths

Code must reflect:

- separate services (if specified)
- correct communication paths
- no forbidden calls

---

### Applications → Endpoints and UI

spec/02-applications.md defines:

- frontend behavior
- backend endpoints
- responses

Code must implement:

- endpoints exactly as described
- response shape exactly as described
- UI behavior exactly as described

---

### Database → Persistence

spec/03-database.md defines:

- storage requirements
- shared vs isolated database

Code must:

- connect to the database
- respect shared/isolated constraints
- not introduce extra schema unless required

---

### Runtime → Execution

spec/04-runtime-modes.md defines:

- dev mode
- prod mode

Code must include:

- commands or scripts to run both modes
- correct startup of all components

---

### Acceptance Criteria → Tests / Checks

spec/05-acceptance-criteria.md defines:

- expected behavior

Code must include:

- tests or scripts that verify these criteria
- or instructions how to verify them

---

### Non-goals → Exclusions

spec/06-non-goals.md defines:

- what must NOT be implemented

Code must NOT contain any of these.

---

## Explicitness Rule

Code must not rely on implicit behavior.

Avoid:

- hidden defaults
- magic values
- implicit configuration

Everything required for correct behavior must be:

- visible
- explainable from spec

---

## Traceability Requirement

Every part of code must be traceable to spec.

The LLM must be able to explain:

- which spec requirement produced this code
- which file and section it came from

---

## Gap Detection

If spec is incomplete:

- list missing parts
- ask clarification questions
- do NOT guess

---

## Consistency Check

After code generation:

- verify alignment with spec
- detect:
    - missing implementation
    - mismatches
    - extra behavior (dark code)

---

## Output Requirements

When generating code, the LLM must provide:

1. list of spec files used
2. mapping summary:

   spec section → code files

3. report:

    - missing parts
    - assumptions (if any)
    - risks

---

## Dark Code Definition

Dark code is any behavior in code that:

- is not described in spec
- cannot be traced to spec
- is not required for infrastructure

Examples:

- extra endpoints
- hidden logic
- undocumented data transformations

---

## Allowed Infrastructure Code

The following is allowed even if not explicitly described in spec:

- framework boilerplate
- startup scripts
- minimal configuration

But:

- must not introduce behavior
- must not change system logic

---

## Enforcement

Code that violates this contract must be:

- rejected
  or
- corrected before acceptance

Code is not considered valid unless:

- it matches spec
- it passes acceptance checks