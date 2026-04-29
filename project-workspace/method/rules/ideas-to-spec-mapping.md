---
id: rules.ideas-to-spec-mapping
title: Ideas to Spec Mapping Contract
type: rule
status: draft
version: 0.1
links:
  parent: method.index
  children: []
  related:
    - rules.workflow-overview
    - rules.traceability-policy
    - rules.consistency-policy
---

# Ideas to Spec Mapping Contract

## Purpose

This rule defines how the `spec` layer must be derived from the `ideas` layer.

The purpose is to make `ideas -> spec` a controlled translation step, not a free-form rewriting step.

## Authoritative sources

The spec must be derived only from:

- `ideas/000-project-intent.md`;
- `ideas/accepted/*`;
- `ideas/boundaries/*`.

The following must not be used as source of truth for spec generation:

- `ideas/inbox/*`;
- `ideas/archive/*`;
- previous generated code;
- implicit assumptions;
- generic framework defaults unless explicitly required for runtime viability.

## Coverage requirement

Every accepted idea must be represented in spec.

For each file in `ideas/accepted/`, identify:

- functional statements;
- architectural decisions;
- constraints;
- explicitly required texts, endpoints, data, or runtime behavior.

Each such statement must be mapped to one or more spec files.

## Boundaries requirement

Every boundary must be represented in spec.

For each file in `ideas/boundaries/`, identify what must not be implemented or what must be constrained.

These exclusions must be represented in:

- `spec/06-non-goals.md`; and
- acceptance checks when the exclusion is testable.

## No invention rule

The spec must not introduce:

- new business features not present in accepted ideas;
- new business entities not present in accepted ideas;
- new user roles not present in accepted ideas;
- new behavior not present in accepted ideas;
- new product scope not present in accepted ideas.

If something is missing, ambiguous, or underspecified, report a gap instead of inventing a solution.

## Mapping rules

### Application shape -> architecture

Accepted decisions about system components must be mapped to:

- `spec/01-architecture.md`.

This includes:

- runtime components;
- boundaries;
- responsibilities;
- allowed communication paths;
- forbidden communication paths.

### Behavior -> applications

Accepted decisions about UI or API behavior must be mapped to:

- `spec/02-applications.md`.

This includes:

- frontend behavior;
- backend endpoints;
- response formats;
- user-visible text when explicitly defined.

### Data -> database

Accepted decisions about data storage must be mapped to:

- `spec/03-database.md`.

This includes:

- shared vs isolated database decisions;
- connectivity requirements;
- schema requirements if explicitly defined;
- absence of business schema when explicitly scoped out.

### Runtime -> runtime modes

Accepted decisions about startup, deployment, and operating modes must be mapped to:

- `spec/04-runtime-modes.md`.

### Acceptance -> acceptance criteria

Accepted decisions and boundaries that define observable behavior must be mapped to:

- `spec/05-acceptance-criteria.md`;
- `checks/acceptance-checklist.md` when applicable.

### Boundaries -> non-goals

Boundaries and out-of-scope statements must be mapped to:

- `spec/06-non-goals.md`.

## Explicitness rule

The spec must not rely on implicit interpretation.

All of the following must be explicit:

- which component calls which component;
- which component owns which responsibility;
- what happens in each supported scenario;
- what is shown to the user;
- what is forbidden.

Avoid vague phrases such as:

- `standard behavior`;
- `normal setup`;
- `as usual`;
- `basic admin`;
- `simple CRUD`.

Replace them with explicit definitions.

## Consistency check

After generating or updating spec:

- ensure there are no contradictions between spec files;
- ensure naming is consistent across ideas and spec;
- ensure no accepted idea is missing from spec;
- ensure no spec behavior lacks an accepted idea or boundary source.

If conflicts are found, report them and do not resolve silently.

## Gap detection

If ideas are incomplete, the LLM must report:

- missing decisions;
- ambiguous areas;
- assumptions that would be needed to continue;
- proposed clarification questions.

The LLM must not fill these gaps automatically.

## Required output when performing ideas -> spec

When the LLM performs an `ideas -> spec` step, it must provide a mapping summary:

```text
ideas/accepted/001-... -> spec/...
ideas/accepted/002-... -> spec/...
ideas/boundaries/001-... -> spec/...
```

It must also report:

- missing mappings;
- unclear ideas;
- potential conflicts;
- any spec statements that do not trace back to accepted ideas or boundaries.

