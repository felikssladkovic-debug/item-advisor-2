# 01-bootstrap-project.prompt

Ты работаешь в папке `project/`.

Это barebone-проект, созданный из `starting-foundation-01-barebone`. Твоя задача — не сразу писать код, а подготовить проект к первой осмысленной генерации кода с сохранением связности:

`business idea → ideas → spec → code → tests → runtime`.

## Сначала прочитай

- `../README.md`
- `../method/rules/README.md`
- `../method/rules/*.md`
- `ideas/*.md`
- `spec/**/*.md`
- `method.lock.json`

## Сделай

1. Проверь, что структура проекта корректна.
2. Найди пустые/слишком общие места в `ideas/` и `spec/`.
3. Составь список вопросов к человеку, без которых нельзя безопасно выбирать стек и генерировать код.
4. Если данных достаточно, предложи минимальный вертикальный срез.
5. Не создавай backend/frontend/database/auth/infra, если это явно не вытекает из заполненной спецификации.
6. Не добавляй технологические решения только потому, что они типовые.

## Формат ответа

Верни отчет в Markdown:

- `Structure check`
- `Missing product decisions`
- `Spec gaps`
- `Suggested minimal vertical slice`
- `Files I would create next`
- `Questions for human`

## Жесткое правило

Любой предлагаемый файл кода должен иметь ссылку на конкретный spec/decision/acceptance criterion, из которого он следует.
