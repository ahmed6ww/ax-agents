---
title: Customize API Docs
impact: LOW
impactDescription: 
tags: docs, openapi, dx
---

## Customize API Docs

Help consumers of your API by providing detailed metadata in your routes. Use `tags`, `summary`, `description`, and `responses`.

**Correct:**

```python
@router.post(
    "/items",
    tags=["Items"],
    summary="Create a new item",
    description="Creates an item with the given name and price.",
    status_code=201,
    responses={
        201: {"description": "Item created successfully"},
        400: {"description": "Invalid input data"},
    }
)
async def create_item(item: ItemCreate):
    pass
```
