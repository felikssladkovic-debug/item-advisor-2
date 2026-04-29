# method-wiki-eng-prog

This method define evolution process for any applicable project by method-wiki-eng-prog (which implements paradigm of programming in english).

## Structure

```text
method/   # method-wiki: rules, templates, prompts, graph, validation tools
starting-foundation-<nn>-<name>/  # versions of project evolution stable states (i.e. ideas with reflected spec)
```

## Method-wiki checks

```bash
python method/tools/generate_graph.py
python method/tools/validate_method_wiki.py
```

Every Markdown document in `method/` has YAML front matter, a path-derived id, and links to related method documents.

## How to start new project
Choose foundation close to your project intention (see starting-foundation-<nn>-<name> folders), and run its start.sh


