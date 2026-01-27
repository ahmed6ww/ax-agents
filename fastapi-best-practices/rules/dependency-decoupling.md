---
title: Decouple Dependencies
impact: MEDIUM
impactDescription: 
tags: dependencies, performance, caching
---

## Decouple Dependencies

FastAPI caches dependency return values within the scope of a single request. If a dependency is used multiple times in a dependency tree, it is executed only once. Use this to decoupled huge dependencies into smaller, focused ones without fear of performance penalty.

**Example:**

```python
async def get_db():
    # ... connection logic
    pass

async def get_current_user(db = Depends(get_db)):
    pass

async def get_current_active_user(user = Depends(get_current_user)):
    pass

@router.get("/")
async def endpoint(
    user = Depends(get_current_user), 
    active_user = Depends(get_current_active_user)
):
    # get_db is called ONCE
    # get_current_user is called ONCE (result shared with get_current_active_user)
    pass
```
