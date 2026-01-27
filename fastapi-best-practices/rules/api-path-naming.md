---
title: Consistent API Path Naming
impact: LOW
impactDescription: Enables dependency reuse
tags: api, naming, dependencies
---

## Consistent API Path Naming

Use the same path variable names across different routes that refer to the same entity. This allows you to reuse dependencies that validate those entities.

**Incorrect (Inconsistent naming):**

```python
# Router A
@router.get("/users/{user_id}")
async def get_user(user_id: int): ...

# Router B
@router.get("/profiles/{id}")
async def get_profile(id: int): ...
```

**Correct (Consistent naming):**

```python
# Router A
@router.get("/users/{user_id}")
async def get_user(user: User = Depends(valid_user_id)): ...

# Router B
# Can reuse valid_user_id because it expects the same path param name implicitly or explicitly
@router.get("/profiles/{user_id}")
async def get_profile(user: User = Depends(valid_user_id)): ...
```
