# starting-foundation-02-site-admin-db

Starting package for projects developed with a method-wiki approach.

This package assumes a minimal deployable multi-application system:

- site frontend
- site backend
- admin frontend
- admin backend
- shared database

The package does not implement business functionality yet. It prepares `ideas`, `spec`, prompts, and checks so Codex can generate the application code from the spec.

## Usage

```bash
./start.sh
```

This creates `project-workspace/` and copies `method/starting-foundation/*` into `project-workspace/project/`.

Then run Codex inside:

```bash
cd project-workspace/project
```

Use:

```text
prompts/01-generate-code-from-spec.prompt.md
```


## Ideas layer

The initialized project uses this idea-layer structure:

```text
ideas/
  000-project-intent.md
  accepted/    # approved idea-layer decisions, source of truth for spec
  boundaries/  # explicit non-goals and constraints
  inbox/       # raw ideas under discussion, not authoritative
  archive/     # processed inbox ideas, not authoritative
```

Spec generation must use only `000-project-intent.md`, `accepted/`, and `boundaries/`.

## Method-wiki checks

```bash
python method/tools/generate_graph.py --check
python method/tools/validate_method_wiki.py
```
