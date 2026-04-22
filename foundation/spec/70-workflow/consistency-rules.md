# Consistency Rules

- Specs describe the intended behavior and structure for the current slice.
- Code must match the behavior, route names, roles, and response shapes defined in `/spec`.
- README must explain how specs and implementation relate.
- Avoid placeholder modules, fake services, and speculative abstractions that are not used.
- When implementation introduces a meaningful concrete decision, update the relevant spec file in the same change.
- Keep demo credentials, routes, and role names identical across specs, code, tests, and README.
