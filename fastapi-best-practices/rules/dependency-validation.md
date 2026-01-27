---
title: Validation via Dependencies
impact: HIGH
impactDescription: Removes duplicated validation logic from endpoints
tags: dependencies, validation, dry
---

## Validation via Dependencies

Use FastAPI Dependencies for complex request validation, especially when it involves database checks (e.g., verifying a user exists, or an item belongs to a user). Do not repeat this logic inside every endpoint.

**Incorrect (Duplicated validation):**

```python
@router.get("/items/{item_id}")
async def get_item(item_id: int):
    item = await db.get(item_id)
    if not item:
        raise HTTPException(404)
    return item

@router.put("/items/{item_id}")
async def update_item(item_id: int):
    item = await db.get(item_id) # Repeated logic
    if not item:
        raise HTTPException(404)
    # update logic...
```

**Correct (Validation dependency):**

```python
async def valid_item_id(item_id: int) -> Item:
    item = await db.get(item_id)
    if not item:
        raise HTTPException(404)
    return item

@router.get("/items/{item_id}")
async def get_item(item: Item = Depends(valid_item_id)):
    return item

@router.put("/items/{item_id}")
async def update_item(item: Item = Depends(valid_item_id)):
    # Item is already validated and injected
    return update_logic(item)
```
