---
title: Chain Dependencies
impact: MEDIUM
impactDescription: 
tags: dependencies, composition, dry
---

## Chain Dependencies

Dependencies can depend on other dependencies. Use this to build complex validation chains from smaller, reusable building blocks.

**Correct:**

```python
# 1. Base dependency
async def valid_token(token: str) -> User:
    return decode_token(token)

# 2. Derived dependency (uses valid_token)
async def active_user(user: User = Depends(valid_token)) -> User:
    if not user.is_active:
        raise HTTPException(400, "Inactive")
    return user

# 3. Further derived (uses active_user)
async def admin_user(user: User = Depends(active_user)) -> User:
    if not user.is_admin:
        raise HTTPException(403, "Not admin")
    return user

@router.get("/admin")
async def admin_dashboard(user: User = Depends(admin_user)):
    return {"message": "Hello admin"}
```
