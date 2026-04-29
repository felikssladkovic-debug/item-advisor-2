#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-./project-workspace}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$TARGET_DIR"
cp -R "$SCRIPT_DIR/method" "$TARGET_DIR/"
mkdir -p "$TARGET_DIR/project"

cat <<EOF
Created barebone workspace at: $TARGET_DIR

Next steps:
  cd "$TARGET_DIR"
  python method/tools/generate_graph.py --check
  python method/tools/validate_method_wiki.py

To start code generation, run Codex inside:
  $TARGET_DIR/project

and use:
  $TARGET_DIR/method/prompts/01-bootstrap-project.prompt.md
EOF
