---
title: ValueError to 422
impact: LOW
impactDescription: 
tags: pydantic, error-handling
---

## ValueError to 422

When writing custom validators in Pydantic, raising a simple `ValueError` is sufficient. FastAPI (via Pydantic) catches these and automatically converts them into a structured `422 Unprocessable Entity` response with field details.

**Correct:**

```python
@field_validator("password")
def strong_password(cls, v):
    if len(v) < 8:
        raise ValueError("Password too short") # Becomes 422 automatically
    return v
```

Reference: [FastAPI Request Validation](https://fastapi.tiangolo.com/tutorial/handling-errors/#requestvalidationerror-vs-validationerror)
