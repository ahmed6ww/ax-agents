---
title: Use Built-in Validators
impact: HIGH
impactDescription: Reduces custom code and improves security
tags: pydantic, validation, security
---

## Use Built-in Validators

Pydantic offers powerful built-in validation tools. Use them instead of writing custom validators or manual checks.
- Use `Field` constraints (`min_length`, `max_length`, `pattern`, `ge`, `le`).
- Use types like `EmailStr`, `AnyUrl`, `UUID4`, `PastDate`.
- Use `Enums` for fixed sets of values.

**Incorrect (Manual validation):**

```python
class User(BaseModel):
    username: str
    email: str

    @validator("username")
    def validate_username(cls, v):
        if not re.match("^[a-z0-9]+$", v):
            raise ValueError("Invalid username")
        return v
```

**Correct (Declarative validation):**

```python
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    username: str = Field(pattern="^[a-z0-9]+$")
    email: EmailStr
```

Reference: [Pydantic Fields](https://docs.pydantic.dev/latest/concepts/fields/)
