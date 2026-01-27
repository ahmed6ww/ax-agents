---
title: TDD Strategy (The Quads)
impact: HIGH
impactDescription: Ensures robust and testable code
tags: testing, tdd, strategy
---

## TDD Strategy: The Quads

Do not write generic tests. Identify the layer and apply the specific strategy known as "The Quads".

- **Quad 1 (Unit Tests):** Test pure logic (Services, Utils) in isolation. Mock all dependencies.
- **Quad 2 (Integration Tests):** Test interaction with external systems (DB, APIs). Use Docker containers (Testcontainers).
- **Quad 3 (Component Tests):** Test API endpoints (`TestClient` or `AsyncClient`). Mock external services but use real DB if possible (or in-memory).
- **Quad 4 (E2E Tests):** Test full flows.

Reference: `Read({baseDir}/references/quad_strategy.md)`
