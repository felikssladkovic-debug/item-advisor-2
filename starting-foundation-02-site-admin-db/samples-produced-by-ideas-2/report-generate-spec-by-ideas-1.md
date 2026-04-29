

Updated the spec under spec/00-overview.md, spec/01-architecture.md, spec/02-applications.md, spec/03-database.md,
spec/04-runtime-modes.md, spec/05-acceptance-criteria.md, spec/06-non-goals.md, and spec/index.md. Those files now
contain the full generated spec content.

Mapping Report

- ideas/000-project-intent.md -> spec/00-overview.md, spec/01-architecture.md, spec/02-applications.md, spec/04-
  runtime-modes.md, spec/05-acceptance-criteria.md
- ideas/accepted/001-application-shape.md -> spec/00-overview.md, spec/01-architecture.md, spec/04-runtime-modes.md,
  spec/05-acceptance-criteria.md
- ideas/accepted/002-database.md -> spec/00-overview.md, spec/01-architecture.md, spec/03-database.md, spec/05-
  acceptance-criteria.md
- ideas/accepted/003-site-behavior.md -> spec/00-overview.md, spec/02-applications.md, spec/05-acceptance-criteria.md
- ideas/accepted/004-admin-behavior.md -> spec/00-overview.md, spec/02-applications.md, spec/05-acceptance-criteria.md
- ideas/accepted/005-admin-scope.md -> spec/00-overview.md, spec/02-applications.md, spec/06-non-goals.md
- ideas/boundaries/001-out-of-scope.md -> spec/00-overview.md, spec/05-acceptance-criteria.md, spec/06-non-goals.md

Gap Report

- Backend API contract is unspecified: no endpoint paths, methods, payloads, or response format are defined in the
  accepted ideas.
- Frontend delivery details are unspecified: no route paths, page URLs, or rendering mechanism are defined beyond “one
  page” per frontend.
- Database implementation details are unspecified: no database type, connection mechanism, schema object, or health-
  check query/operation is defined.
- Runtime execution details are unspecified: no startup commands, port assignments, process model, or production
  packaging/deployment shape is defined.
- Acceptance execution details are unspecified: accepted ideas define outcomes, but not the concrete checklist steps
  or tooling used to verify them.

Validation Report

- Coverage: all accepted ideas and the boundary file are represented in spec.
- Missing: none detected relative to the accepted idea set and boundary file.
- Distortion: none detected.
- Invention: no business features, entities, roles, or behaviors were added beyond the accepted ideas and direct
  boundary constraints.

I did not run tests or acceptance checks.