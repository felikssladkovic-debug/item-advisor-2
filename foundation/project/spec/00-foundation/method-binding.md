# Method Binding

## Boundaries

- This specification is the source of truth for the first generated implementation.
- Implementation is limited to the capabilities explicitly described in this spec.
- `/method/*` is read-only and is treated as process guidance, not executable product behavior.

## Generation Scope

- The implementation generated from this spec must create:
  - `project/generated/backend`
  - `project/generated/frontend`
  - `project/generated/infra`
- The generated system is the first minimal slice only.
- The minimal slice includes:
  - authentication
  - authorization via roles
  - a site page for authenticated users
  - an admin users page for managers

## Consistency Rules

- Product terms must be used consistently across ideas, spec, and code.
- API names, route names, role names, and environment variable names must match this spec exactly.
- No generated feature may exceed the scope defined in `scope.md`, `feature-map.md`, `30-contracts/README.md`, and `40-ui/README.md`.
