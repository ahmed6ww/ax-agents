---
title: Async Test Client
impact: MEDIUM
impactDescription: 
tags: testing, async, httpx
---

## Async Test Client

If your application uses `async` routes and database calls, your tests must use an asynchronous client (like `httpx.AsyncClient`) to correctly interact with the event loop and avoid `RuntimeError`.

**Incorrect (Sync Client with Async App):**

```python
from fastapi.testclient import TestClient

def test_root():
    client = TestClient(app)
    response = client.get("/") # Might fail if app assumes running loop
```

**Correct (Async Client):**

```python
import pytest
from httpx import AsyncClient, ASGITransport

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url="http://test"
    ) as client:
        response = await client.get("/")
```
