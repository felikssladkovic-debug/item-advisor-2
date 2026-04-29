#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-./project-workspace}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$TARGET_DIR"
rm -rf "$TARGET_DIR/method"
cp -R "$SCRIPT_DIR/method" "$TARGET_DIR/"
mkdir -p "$TARGET_DIR/project"
cp -R "$SCRIPT_DIR/method/starting-foundation/." "$TARGET_DIR/project/"

cat <<EOF
Created site-admin-db workspace at: $TARGET_DIR

Workspace contains:
  $TARGET_DIR/method   - method-wiki rules, templates, prompts, validation tools
  $TARGET_DIR/project  - initialized project ideas/spec/prompts/checks

Recommended checks:
  cd "$TARGET_DIR"
  python method/tools/generate_graph.py --check
  python method/tools/validate_method_wiki.py

To start code generation, run Codex inside:
  $TARGET_DIR/project

and use:
  prompts/01-generate-code-from-spec.prompt.md
EOF
