# starting-foundation-01-barebone

Barebone-пакет для разработки проекта по методике связности:

**business idea → ideas → spec → code → tests → runtime → sync back to spec**.

Эта версия намеренно не знает, какой именно продукт будет построен. Здесь нет предположений про сайт, админку, базу данных, backend, frontend, auth или инфраструктуру. Пакет задает только минимальную структуру, правила и стартовые файлы для любого проекта.

## Что внутри

- `method/starting-foundation/` — стартовый набор файлов, который копируется в `project/`.
- `method/rules/` — правила работы с идеями, спецификацией, кодом и изменениями.
- `method/templates/` — шаблоны для будущего расширения spec/ideas.
- `method/prompts/01-bootstrap-project.prompt.md` — первый промпт для Codex после копирования стартовых файлов.
- `method/tools/` — минимальные локальные проверки структуры и ссылок.
- `project/` — рабочая папка будущего проекта. До запуска `start.sh` почти пустая.

## Как стартовать

```bash
chmod +x start.sh
./start.sh
cd project
```

После этого запусти Codex именно из папки `project/` и передай ему промпт:

```text
../method/prompts/01-bootstrap-project.prompt.md
```

## Важное ограничение barebone-версии

Codex не должен сразу генерировать произвольный backend/frontend/infra. Сначала он должен заполнить и согласовать файлы `ideas/` и `spec/`, затем предложить минимальный план генерации кода.
