# starting-foundation-01-barebone

Barebone starting package for projects developed with a method-wiki approach.

The package intentionally does not assume a website, admin panel, database, backend, frontend, or infrastructure stack.

## Structure

```text
method/   # method-wiki: rules, templates, prompts, graph, validation tools
project/  # target workspace; initially empty
start.sh  # copies the starting workspace to a target folder
```

## Method-wiki checks

```bash
python method/tools/generate_graph.py
python method/tools/validate_method_wiki.py
```

Every Markdown document in `method/` has YAML front matter, a path-derived id, and links to related method documents.
