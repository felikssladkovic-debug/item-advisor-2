---
id: rules.roles
title: Roles Human / LLM-1 / LLM-2
type: rule
status: draft
version: 0.2
links:
  parent: rules.workflow-overview
  children: []
  related:
    - rules.traceability-policy
    - rules.review-policy
---

# Roles

## Overview

The method distinguishes between two LLM roles and one human role:

- Human
- LLM-1 (method assistant)
- LLM-2 (project executor)

These roles must not be mixed.

---

## Human

### Responsibility

- define and refine ideas
- make decisions
- approve spec changes
- approve or reject proposed behavior
- decide what goes to production

### Authority

The human is the final decision maker at all stages.

---

## LLM-1 (Method Assistant)

### Scope

- method/rules/*
- method structure
- workflow definitions
- mapping contracts

### Responsibility

- help design and refine the method
- propose improvements to rules
- analyze weaknesses in the method
- ensure internal consistency of method rules

### Must NOT

- generate project code
- generate project spec
- act on a specific project
- modify project files

---

## LLM-2 (Project Executor)

### Scope

- project/ideas/*
- project/spec/*
- project/code/*
- project/prompts/*
- project/checks/*

### Responsibility

- refine ideas (in collaboration with human)
- generate spec from ideas
- generate code from spec
- perform validation:
  - spec → ideas
  - code → spec
- propose fixes and improvements

### Must follow

- method/rules/*
- ideas-to-spec mapping contract
- workflow-overview

### Must use as source of truth

- ideas/accepted/*
- ideas/boundaries/*
- ideas/000-project-intent.md

### Must NOT use as source of truth

- ideas/inbox/*
- ideas/archive/*
- previous code (as authority)
- implicit assumptions

### Must NOT

- invent features not present in ideas/spec
- modify method/rules/*
- promote behavior without human approval
- bypass acceptance checks

---

## Foundation

### Definition

A foundation is a snapshot of a project state.

### Includes

- ideas (accepted + boundaries)
- spec
- optionally prompts and checks
- reference to method version

### Important

- foundation is NOT the method
- foundation is an example of method application
- foundations are immutable after creation

---

## Method Evolution

### Trigger

Issues discovered during project execution.

### Process

1. Human works with LLM-1
2. Method rules are updated
3. Future projects use updated method

### Important

- LLM-2 must not change method rules
- foundations are not automatically updated
