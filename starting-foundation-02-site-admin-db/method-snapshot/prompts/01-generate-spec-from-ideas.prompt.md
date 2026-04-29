---
id: prompts.01-generate-spec-from-ideas.prompt
title: Generate Code From Spec Prompt
type: prompt
status: accepted
version: 0.2
links:
  parent: prompts.index
  children: []
  related:
    - rules.workflow-overview
    - rules.ideas-to-spec-mapping
---

# Generate Spec From Ideas

## Role

You are LLM-2 (project executor).

You are working inside a project that follows a strict method.

You must follow all rules in:

- method/rules/roles.md
- method/rules/ideas-to-spec-mapping.md
- method/rules/validation-contract.md
- method/rules/workflow-overview.md

---

## Objective

Generate or update the project specification (spec/) based on accepted ideas.

---

## Sources of Truth

You MUST use ONLY:

- ideas/accepted/*
- ideas/boundaries/*
- ideas/000-project-intent.md

You MUST NOT use:

- ideas/inbox/*
- ideas/archive/*
- project/code/*
- assumptions
- conventions not explicitly stated

---

## Task

1. Read all accepted ideas
2. Read all boundaries
3. Read project intent
4. Generate or update spec files

---

## Output Structure

You must produce:

1. Updated or new files in:

spec/

Typical files:

- spec/00-overview.md
- spec/01-architecture.md
- spec/02-applications.md
- spec/03-database.md
- spec/04-runtime-modes.md
- spec/05-acceptance-criteria.md
- spec/06-non-goals.md

2. Mapping report:

For each accepted idea:

ideas/accepted/XXX-*.md → spec sections

3. Gap report:

- missing decisions
- unclear requirements
- ambiguities

---

## Rules

### 1. Coverage

Every accepted idea must be represented in spec.

No accepted idea may be ignored.

---

### 2. No Invention

You MUST NOT introduce:

- new features
- new entities
- new behavior
- new assumptions

If something is missing:

→ report a gap  
→ do NOT invent

---

### 3. Boundaries Enforcement

Everything in:

ideas/boundaries/*

must be reflected in:

spec/06-non-goals.md

---

### 4. Explicitness

Avoid vague language such as:

- "standard behavior"
- "should work normally"
- "as usual"

Everything must be explicitly defined:

- components
- interactions
- behavior
- outputs

---

### 5. Consistency

Ensure:

- no contradictions
- consistent naming
- clear boundaries between components

---

### 6. Structure

Follow mapping rules:

- architecture → spec/01-architecture.md
- behavior → spec/02-applications.md
- data → spec/03-database.md
- runtime → spec/04-runtime-modes.md
- constraints → spec/06-non-goals.md

---

### 7. No Auto-Fix

If ideas are incomplete:

- list gaps
- ask questions (if needed)

Do NOT modify ideas automatically.

---

## Validation (Mandatory)

After generating spec, perform validation:

### spec → ideas

Check:

- coverage
- no distortion
- no invention

Produce:

- validation report

---

## Output Format

Return:

1. Spec files (full content)
2. Mapping report (ideas → spec)
3. Gap report
4. Validation report

---

## Important Constraints

- spec is the only source of truth for code generation
- do not optimize, improve, or extend ideas
- do not add "best practices" unless explicitly required
- do not assume missing details

---

## Goal

Produce a spec that is:

- complete (covers all ideas)
- exact (no invention)
- explicit (no ambiguity)
- consistent
- ready for code generation