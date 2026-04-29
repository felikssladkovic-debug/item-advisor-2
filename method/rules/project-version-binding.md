---
id: rules.project-version-binding
title: Project Version Binding
type: rule
status: draft
version: 0.1
links:
  parent: method.index
  children: []
  related:
    - rules.traceability-policy
---

# Project Version Binding

## Purpose

Record which method assumptions were used to create or change the project.

## Rule

A project state should be reproducible from:

```text
method version + prompt + project files + recorded decisions
```

The barebone package includes `method.lock.json` as the minimal place for method package metadata.

