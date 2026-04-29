---
id: starting-foundation.checks.acceptance-checklist
title: Acceptance Checklist
type: checklist
status: accepted
version: 0.1
links:
  parent: starting-foundation.checks.index
  children: []
  related:
    - rules.project-lifecycle
    - starting-foundation.spec.05-acceptance-criteria
---

# Acceptance Checklist

## Development mode

- [ ] Start development mode.
- [ ] Open site frontend.
- [ ] Open admin frontend.
- [ ] Check site backend health/database endpoint.
- [ ] Check admin backend health/database endpoint.
- [ ] Confirm both backends use the same database.

## Production mode

- [ ] Build production artifacts.
- [ ] Start production mode.
- [ ] Open site frontend.
- [ ] Open admin frontend.
- [ ] Check site backend health/database endpoint.
- [ ] Check admin backend health/database endpoint.

## Database available scenario

- [ ] Site shows database available text.
- [ ] Admin shows database available text.

## Database unavailable scenario

- [ ] Stop or disconnect database.
- [ ] Site shows database unavailable text.
- [ ] Admin shows database unavailable text.

## Architecture

- [ ] Site frontend does not call admin backend.
- [ ] Admin frontend does not call site backend.
- [ ] Frontends do not access database directly.

## Gate

- [ ] All acceptance checks passed.
- [ ] Code can be considered deployable.

## Links

- Parent: [[starting-foundation.checks.index]]
- Related: [[rules.project-lifecycle]], [[starting-foundation.spec.05-acceptance-criteria]]
