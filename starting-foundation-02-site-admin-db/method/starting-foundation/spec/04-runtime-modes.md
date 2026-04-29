---
id: starting-foundation.spec.04-runtime-modes
title: Runtime Modes
type: spec
status: accepted
version: 0.2
links:
  parent: starting-foundation.spec.index
  children: []
  related:
    - starting-foundation.spec.05-acceptance-criteria
---

# Runtime Modes

The generated project must support development mode and production mode.

## Development mode

Development mode should be convenient for local/server development.

It must start:

- database;
- site backend;
- site frontend;
- admin backend;
- admin frontend.

## Production mode

Production mode should run the same logical system with production-oriented build/start commands.

It must start:

- database;
- site backend;
- site frontend;
- admin backend;
- admin frontend.

## Required startup documentation

The generated project must document exact commands for:

- starting development mode;
- stopping development mode;
- starting production mode;
- stopping production mode;
- checking logs.

## Links

- Parent: [[starting-foundation.spec.index]]
- Related: [[starting-foundation.spec.05-acceptance-criteria]]
