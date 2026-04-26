# tools

Минимальные проверки для barebone-пакета.

```bash
python3 method/tools/spec_lint.py project
python3 method/tools/link_check.py project
python3 method/tools/orphan_check.py project
python3 method/tools/traceability_check.py project
```

Эти скрипты намеренно простые. Они не заменяют review, но помогают поймать грубые ошибки структуры.
