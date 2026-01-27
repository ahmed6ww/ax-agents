---
title: Async vs Sync Rotes for I/O
impact: CRITICAL
impactDescription: Prevents event loop blocking
tags: async, performance, multithreading
---

## Async vs Sync Routes for I/O

FastAPI can handle both `async` and `sync` routes effectively, but they must be used correctly.
- Use `async def` for routes that perform non-blocking I/O (awaitables).
- Use `def` (sync) for routes that perform blocking I/O; FastAPI will run these in a threadpool.
- NEVER perform blocking operations inside an `async def` route without awaiting; this blocks the entire event loop.

**Incorrect (Blocking I/O in async route):**

```python
import time

@router.get("/terrible")
async def terrible_ping():
    time.sleep(10) # BLOCKS the whole event loop!
    return {"pong": True}
```

**Correct (Non-blocking I/O):**

```python
import asyncio

@router.get("/perfect")
async def perfect_ping():
    await asyncio.sleep(10) # Non-blocking yield
    return {"pong": True}
```

**Correct (Blocking I/O in sync route):**

```python
import time

@router.get("/good")
def good_ping():
    time.sleep(10) # Run in a separate thread
    return {"pong": True}
```

Reference: [FastAPI Async/Await](https://fastapi.tiangolo.com/async/#path-operation-functions)
