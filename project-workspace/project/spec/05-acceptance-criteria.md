---
id: starting-foundation.spec.05-acceptance-criteria
title: Acceptance Criteria
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
    - starting-foundation.ideas.accepted.003-site-behavior
    - starting-foundation.ideas.accepted.004-admin-behavior
    - starting-foundation.ideas.boundaries.001-out-of-scope
---

# Acceptance Criteria

## Runtime Startup

The system passes runtime startup acceptance when:

- the system can be started in development mode;
- the system can be started in production mode.

## Component Presence

The system passes component-shape acceptance when the running system contains:

1. site frontend;
2. site backend;
3. admin frontend;
4. admin backend;
5. shared database.

## Public Site Acceptance

The system passes public site acceptance when:

- the public site opens in a browser;
- the public site shows exactly `Site is running. Database is available.` when the site backend can access the shared database;
- the public site shows exactly `Site is running. Database is unavailable.` when the site backend cannot access the shared database.

## Admin Acceptance

The system passes admin acceptance when:

- the admin placeholder opens in a browser;
- the admin frontend shows exactly `Admin placeholder is running. Database is available.` when the admin backend can access the shared database;
- the admin frontend shows exactly `Admin placeholder is running. Database is unavailable.` when the admin backend cannot access the shared database.

## Backend Database Acceptance

The system passes backend database acceptance when:

- site backend can check shared database availability;
- admin backend can check shared database availability.

## Anti-Scope Acceptance

The foundation remains within accepted scope when it does not implement:

- authentication;
- authorization;
- CRUD;
- user management;
- roles and permissions;
- admin business functionality;
- public catalog;
- item cards;
- search;
- production business data model;
- business migrations;
- external APIs.
