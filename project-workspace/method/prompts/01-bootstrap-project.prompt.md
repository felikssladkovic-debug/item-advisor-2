---
id: prompts.01-bootstrap-project.prompt
title: Bootstrap Project Prompt
type: prompt
status: draft
version: 0.1
links:
  parent: method.index
  children: []
  related:
    - rules.workflow-overview
    - rules.wiki-linking-rules
---

# Bootstrap Project Prompt

## Purpose

Use this prompt when Codex is launched inside the `project/` folder and should create the first real project files from method context.

## Prompt

```text
You are working inside the project folder.
Before generating code, read the method-wiki in ../method.
Respect the workflow, traceability, naming, and review rules.
Do not assume a stack unless the user explicitly provides it.
When adding or editing Markdown under ../method, preserve YAML front matter, update links, and run the method-wiki validation scripts.
```

## Links

- Parent: [[method.index]]
- Related: [[rules.workflow-overview]], [[rules.wiki-linking-rules]]
