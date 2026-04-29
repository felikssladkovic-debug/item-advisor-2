---
id: rules.core-principles-for-workflow
title: Core Principles for Workflow
type: rule
status: stable
version: 1.0
links:
  parent: rules.workflow-overview
  children: []
  related:
    - rules.roles
    - rules.ideas-to-spec-mapping
    - rules.spec-to-code-mapping
    - rules.validation-contract
---

## Core Principles

### 1. Spec is the source of truth

Code is derived and replaceable.

---

### 2. No direct code editing

Humans do not manually modify generated code.

---

### 3. No use of inbox as truth

ideas/inbox is not authoritative.

---

### 4. No invention

LLM must not introduce behavior outside ideas/spec.

---

### 5. Explicitness over assumptions

Everything must be defined explicitly.

---

### 6. Acceptance as gate

No deployment without passing checks.

---

### 7. Traceability

Every behavior in code must be traceable to spec and ideas.

