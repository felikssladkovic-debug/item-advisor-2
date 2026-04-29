---
id: starting-foundation.spec.00-overview
title: Overview
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
    - starting-foundation.ideas.accepted.005-admin-scope
    - starting-foundation.ideas.boundaries.001-out-of-scope
---

# Overview

## Purpose

This foundation defines a minimal deployable web product shape with:

- public site frontend;
- public site backend;
- admin frontend;
- admin backend;
- shared database.

The foundation does not implement business functionality.

## Goal

The goal of this foundation is to prove that:

- a multi-application system can be generated in this project shape;
- the system runs in development mode;
- the system runs in production mode;
- both backends can check shared database availability;
- both frontends show whether the shared database is available through their respective backends.

## Scope Summary

The scope of this foundation is limited to:

- one public site page;
- one admin placeholder page;
- shared database availability checking from both backends;
- runtime support for development mode and production mode;
- acceptance criteria for the behaviors above.
