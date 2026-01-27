# FastAPI Best Practices

This document provides a comprehensive list of best practices for building production-grade FastAPI applications.

## Table of Contents

- [Async & Concurrency](#async--concurrency)
- [Project Structure](#project-structure)
- [Pydantic Patterns](#pydantic-patterns)
- [Dependency Injection](#dependency-injection)
- [Database & Storage](#database--storage)
- [REST & API Design](#rest--api-design)
- [Testing & Tooling](#testing--tooling)

## Async & Concurrency

### Async vs Sync Routes for I/O

FastAPI can handle both `async` and `sync` routes effectively, but they must be used correctly.
- Use `async def` for routes that perform non-blocking I/O (awaitables).
- Use `def` (sync) for routes that perform blocking I/O; FastAPI will run these in a threadpool.

**Incorrect (Blocking I/O in async route):**

```python
import time

@router.get("/terrible")
async def terrible_ping():
    time.sleep(10) # BLOCKS the whole event loop!
    return {"pong": True}
```

### Offload CPU-Intensive Tasks

Do not perform heavy CPU calculations directly in FastAPI routes. Offload them to a separate process using `multiprocessing` or a task queue like Celery.

### Sync SDKs in Async Routes

If you must use a synchronous library inside an `async def` route, run it in a threadpool using `starlette.concurrency.run_in_threadpool`.

```python
from fastapi.concurrency import run_in_threadpool

@router.get("/")
async def call_simc_lib():
    response = await run_in_threadpool(sync_client.make_request)
    return response
```

## Project Structure

### Structure by Domain

Organize code by domain (functionality area) rather than by file type.

**Correct (Domain-based structure):**

```text
src/
├── auth/
├── posts/
└── main.py
```

## Pydantic Patterns

### Use Built-in Validators

Use Pydantic's built-in validation tools (`Field`, `EmailStr`) instead of custom validators where possible.

### Custom Base Model

Create a custom `BaseModel` that all your application models inherit from to enforce global configuration.

### Decouple BaseSettings

Split `BaseSettings` by domain or module instead of having one monolithic config.

### ValueError to 422

Raising `ValueError` in validators is automatically converted to `422 Unprocessable Entity`.

## Dependency Injection

### Validation via Dependencies

Use FastAPI Dependencies for complex request validation, especially when it involves database checks.

### Chain Dependencies

Chain dependencies to reuse logic and avoid duplication.

### Decouple Dependencies

Decouple huge dependencies into smaller, focused ones. FastAPI caches dependency results per request.

### Async Dependencies

Prefer `async def` for dependencies to avoid threadpool overhead.

## Database & Storage

### Database Naming Conventions

Maintain strict naming conventions: `lower_case_snake`, singular tables, `_at`/`_date` suffixes.

### Explicit Index Naming

Explicitly name DB indexes/constraints in SQLAlchemy metadata to avoid migration conflicts.

### SQL-First Approach

Prefer writing optimized SQL for complex data retrieval over Python-side processing.

### Meaningful Migrations

Migrations must be static, reversible, and use descriptive names.

## REST & API Design

### Consistent API Path Naming

Use the same path variable names across routes (e.g., `{user_id}`) to enable dependency reuse.

### Response Serialization Overhead

Be aware of double validation/serialization overhead when using `response_model`. Return dicts for trustable data if performance is critical.

### Hide Docs in Production

Disable `/docs` in production environments.

### Customize API Docs

Use `tags`, `summary`, and `description` to document your API.

## Testing & Tooling

### Async Test Client

Use `httpx.AsyncClient` for integration tests with `async` routes.

### Use Ruff

Use `ruff` for all linting and formatting.
