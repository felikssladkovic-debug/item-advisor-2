---
id: starting-foundation.ideas.01-accepted-decisions
title: Accepted Decisions
type: idea
status: accepted
version: 0.1
links:
  parent: starting-foundation.ideas.index
  children: []
  related:
    - starting-foundation.decisions.0001-foundation-scope
    - starting-foundation.spec.01-architecture
    - starting-foundation.spec.02-applications
    - starting-foundation.spec.03-database
---

# Accepted Decisions

## Application shape

The project consists of five runtime components:

1. site frontend;
2. site backend;
3. admin frontend;
4. admin backend;
5. shared database.

## Database

The database is shared by site backend and admin backend.

## Site behavior

The public site has one page.

It displays different text depending on whether the site backend can access the database.

## Admin behavior

The admin frontend has one page.

It displays different text depending on whether the admin backend can access the database.

## Admin scope

The admin application is only a placeholder.

It is not a functional admin panel yet.

## Links

- Parent: [[starting-foundation.ideas.index]]
- Related: [[starting-foundation.decisions.0001-foundation-scope]], [[starting-foundation.spec.01-architecture]], [[starting-foundation.spec.02-applications]], [[starting-foundation.spec.03-database]]
