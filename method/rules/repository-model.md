---
id: rules.repository-model
title: Repository Model
type: rule
status: draft
version: 0.1
links:
  parent: method.index
  children: []
  related:
    - rules.workflow-overview
---

# Repository Model

## Purpose

Define the minimal repository model for a barebone starting package.

## Minimal Folders

```text
method/   # method-wiki: rules, templates, prompts, tools
project/  # target project workspace; initially empty in barebone
```

The barebone package must not assume a web app, admin panel, database, backend, frontend, or infrastructure stack.

## Links

- Parent: [[method.index]]
- Related: [[rules.workflow-overview]]
