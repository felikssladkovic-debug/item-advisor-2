# Implementation Rules

- Implement only behavior that exists in the current specs.
- Prefer direct, readable structures over abstract frameworks for future features.
- Keep backend layers separated by responsibility: config, routes, services, repositories, schemas.
- Keep the site and admin frontends separate because they are separate delivery surfaces.
- Add tests only for real implemented behavior.
- If a choice affects runtime behavior, document it in the related spec file.

