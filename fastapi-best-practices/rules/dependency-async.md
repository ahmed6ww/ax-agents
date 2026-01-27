---
title: Async Dependencies
impact: MEDIUM
impactDescription: Avoids overhead of threadpool for dependencies
tags: dependencies, async, performance
---

## Async Dependencies

Just like routes, dependencies can be `async` or `sync`. Prefer `async def` for dependencies, especially if they don't perform blocking I/O or if they perform I/O that can be awaited. `sync` dependencies run in a threadpool, adding overhead.

**Incorrect (Sync dependency for simple logic):**

```python
def get_query_param(q: str | None = None):
    # Runs in threadpool! Unnecessary overhead.
    return q
```

**Correct:**

```python
async def get_query_param(q: str | None = None):
    # Runs directly in event loop. Fast.
    return q
```
