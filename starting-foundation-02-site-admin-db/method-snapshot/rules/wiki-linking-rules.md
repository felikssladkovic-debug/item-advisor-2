---
id: rules.wiki-linking-rules
title: Wiki Linking Rules
type: rule
status: draft
version: 0.1
links:
  parent: method.index
  children: []
  related:
    - method.graph
---

# Wiki Linking Rules

## Purpose

Make `/method` behave as a small method-wiki, not as a pile of unrelated Markdown files.

## Required Metadata

Every Markdown file under `/method`, except generated files when explicitly documented, must start with YAML front matter:

```yaml
---
id: rules.example
title: Example
type: rule
status: draft
version: 0.1
links:
  parent: method.index
  children: []
  related: []
---
```

## ID Rule

The `id` must match the relative path inside `/method` without `.md`, with `/` replaced by `.`.

Example:

```text
method/rules/workflow-overview.md
→ rules.workflow-overview
```

## Link Rule

Every document except `method.index` must have at least one incoming link and must be reachable from `method.index` through `links.children`, `links.parent`, or `links.related`.

## Graph Rule

`method/graph.md` is generated from YAML front matter by `method/tools/generate_graph.py`.
