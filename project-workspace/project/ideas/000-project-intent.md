---
id: starting-foundation.ideas.000-project-intent
title: Project Intent
type: idea
status: accepted
version: 0.2
links:
  parent: starting-foundation.ideas.index
  children: []
  related:
    - starting-foundation.spec.00-overview
    - starting-foundation.spec.01-architecture
---

# Project Intent

## Intent

Create a minimal deployable foundation for a web product with:

- public site frontend;
- public site backend;
- admin frontend;
- admin backend;
- shared database.

The goal is not to implement business functionality yet.

The goal is to prove that Codex can generate a multi-application system that runs in development and production modes and correctly checks database availability from both backends.

## Success definition

The generated project is successful when:

- the public site opens in a browser;
- the admin placeholder opens in a browser;
- both frontends show whether the shared database is available;
- both backends can check database availability;
- the system can be started in development mode;
- the system can be started in production mode;
- acceptance checks pass.

## Authoritative idea sources

For spec generation, the authoritative idea-layer sources are:

- this file;
- `ideas/accepted/*`;
- `ideas/boundaries/*`.

The following folders are not authoritative for spec generation:

- `ideas/inbox/*`;
- `ideas/archive/*`.
