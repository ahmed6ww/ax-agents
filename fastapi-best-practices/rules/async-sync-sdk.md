---
title: Sync SDKs in Async Routes
impact: HIGH
impactDescription: Prevents event loop blocking when using legacy libraries
tags: async, dependencies, starlette
---

## Sync SDKs in Async Routes

If you must use a synchronous library (one that doesn't support `await`) inside an `async def` route, you must run it in a threadpool to avoid blocking the event loop. Use `starlette.concurrency.run_in_threadpool`.

**Incorrect (Blocking call in async route):**

```python
@router.get("/")
async def call_sync_lib():
    # Blocks the loop!
    client = SyncAPIClient()
    response = client.make_request() 
    return response
```

**Correct (Run in threadpool):**

```python
from fastapi.concurrency import run_in_threadpool

@router.get("/")
async def call_sync_lib():
    client = SyncAPIClient()
    # Runs in a separate thread, non-blocking for the loop
    response = await run_in_threadpool(client.make_request)
    return response
```

Reference: [FastAPI Tips](https://github.com/Kludex/fastapi-tips)
