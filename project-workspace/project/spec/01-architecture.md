---
id: starting-foundation.spec.01-architecture
title: Architecture
type: spec
status: draft
version: 0.2
links:
  parent: starting-foundation.spec.index
  children: []
  related:
    - starting-foundation.ideas.000-project-intent
    - starting-foundation.ideas.accepted.001-application-shape
    - starting-foundation.ideas.accepted.002-database
---

# Architecture

## Runtime Components

The system consists of exactly five runtime components:

1. site frontend;
2. site backend;
3. admin frontend;
4. admin backend;
5. shared database.

## Responsibilities

### Site frontend

- provides the public site user interface;
- displays one page;
- displays database availability status for the site application.

### Site backend

- serves the site application's backend responsibility;
- checks whether the shared database is available for the site application.

### Admin frontend

- provides the admin placeholder user interface;
- displays one page;
- displays database availability status for the admin application.

### Admin backend

- serves the admin application's backend responsibility;
- checks whether the shared database is available for the admin application.

### Shared database

- is the single database used by site backend and admin backend;
- only needs to support availability checking in this foundation.

## Communication Paths

The allowed runtime communication paths are:

- site frontend to site backend;
- admin frontend to admin backend;
- site backend to shared database;
- admin backend to shared database.

The shared database availability status shown in a frontend is obtained through that frontend's corresponding backend.

## Separation Rules

The public site and admin are separate applications.

This means:

- site frontend and admin frontend are separate runtime components;
- site backend and admin backend are separate runtime components;
- each frontend shows status for its own application through its own backend;
- both backends use the same shared database.

## Forbidden Responsibility Assignments

The following are not part of this foundation's architecture:

- direct shared database availability checking by the site frontend;
- direct shared database availability checking by the admin frontend;
- replacing the separate site and admin applications with a single frontend;
- replacing the separate site and admin backends with a single backend.
