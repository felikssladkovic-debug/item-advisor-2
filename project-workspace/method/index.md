---
id: method.index
title: Method Index
type: index
status: draft
version: 0.3
links:
  parent: 
  children:
    - rules.workflow-overview
    - rules.ideas-to-spec-mapping
    - rules.wiki-linking-rules
    - rules.naming-rules
    - rules.project-version-binding
    - templates.business-idea-template
    - templates.spec-template
    - templates.decision-log-template
    - templates.change-request-template
    - prompts.01-bootstrap-project.prompt
  related:
    - method.graph
---

# Method Index

This folder is a small **method-wiki**. It describes how to keep business intent, specifications, implementation, checks, runtime behavior, and project evolution connected.

## Core Rules

- [[rules.workflow-overview]] — the end-to-end workflow for changing a project through text, specs, checks, and code.
- [[rules.ideas-to-spec-mapping]] — contract for deriving spec from accepted ideas and boundaries.
- [[rules.roles]] — division of responsibility between human, LLM-1, and LLM-2.
- [[rules.traceability-policy]] — how business idea, spec, code, tests, and decisions stay linked.
- [[rules.wiki-linking-rules]] — rules for metadata, links, graph generation, and orphan prevention.
- [[rules.naming-rules]] — naming conventions for files, ids, and documents.
- [[rules.project-version-binding]] — how project state and method state are bound together.
- [[rules.change-policy]] — how changes are proposed and applied.
- [[rules.review-policy]] — how changes are reviewed before they become part of the project.
- [[rules.consistency-policy]] — what consistency means in this method.

## Templates

- [[templates.business-idea-template]] — business intent template.
- [[templates.spec-template]] — specification template.
- [[templates.decision-log-template]] — decision log template.
- [[templates.change-request-template]] — change request template.

## Prompts

- [[prompts.01-bootstrap-project.prompt]] — initial prompt for LLM-2.

## Generated Map

- [[method.graph]] — generated graph of method-wiki links.
