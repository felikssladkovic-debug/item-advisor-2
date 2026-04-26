#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$ROOT_DIR/project"
FOUNDATION_DIR="$ROOT_DIR/method/starting-foundation"

mkdir -p "$PROJECT_DIR"

if [ -d "$PROJECT_DIR/ideas" ] || [ -d "$PROJECT_DIR/spec" ]; then
  echo "ERROR: project/ideas or project/spec already exists."
  echo "This script is intentionally non-destructive. Move or delete existing folders first."
  exit 1
fi

cp -R "$FOUNDATION_DIR/ideas" "$PROJECT_DIR/ideas"
cp -R "$FOUNDATION_DIR/spec" "$PROJECT_DIR/spec"
cp "$ROOT_DIR/method.lock.json" "$PROJECT_DIR/method.lock.json"

cat > "$PROJECT_DIR/README.md" <<'EOF'
# project

Рабочая папка проекта.

Сначала заполни `ideas/` и `spec/`. Код появляется только после того, как решение можно проследить от бизнес-идеи к спецификации.
EOF

echo "OK: starting foundation copied into project/."
echo "Next: cd project"
echo "Then run Codex with: ../method/prompts/01-bootstrap-project.prompt.md"
