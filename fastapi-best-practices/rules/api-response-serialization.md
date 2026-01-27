---
title: Response Serialization Overhead
impact: MEDIUM
impactDescription: Reduces CPu usage and latency
tags: performance, serialization, pydantic
---

## Response Serialization Overhead

Be aware that FastAPI performs double validation/serialization:
1. When you create a Pydantic model instance to return.
2. When FastAPI validates that instance against the `response_model` (implicit).

To avoid this, you can return a dictionary or use `Response` directly if maximum performance is needed, though you lose some automatic validation safety.

**Insight:**

```python
@app.get("/", response_model=User)
async def get_user():
    # 1. User() creates validation
    user = User(name="John") 
    # 2. FastAPI re-validates 'user' against 'User' model
    return user 
```

**Optimization (if needed):**

Return plain dicts if you trust the data source (e.g., direct DB result) and want to skip the first Pydantic instantiation, letting FastAPI handle the final validation.

```python
@app.get("/", response_model=User)
async def get_user():
    # Returns dict, FastAPI validates it ONCE against Check
    return {"name": "John"} 
```
