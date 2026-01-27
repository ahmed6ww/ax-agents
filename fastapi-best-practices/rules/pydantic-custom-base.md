---
title: Custom Base Model
impact: MEDIUM
impactDescription: Ensures consistent serialization across the app
tags: pydantic, serialization, standardization
---

## Custom Base Model

Create a custom `BaseModel` that all your application models inherit from. This allows you to enforce global configuration, such as datetime formatting or JSON encoding policies.

**Incorrect (Inconsistent configuration):**

```python
# Model A uses default config
class ModelA(BaseModel):
    created_at: datetime 

# Model B tries to customize but might differ
class ModelB(BaseModel):
    created_at: datetime
    model_config = ConfigDict(json_encoders={datetime: str})
```

**Correct (Global Base Model):**

```python
from pydantic import BaseModel, ConfigDict

def datetime_to_gmt_str(dt: datetime) -> str:
    # Custom formatting logic
    return dt.strftime("%Y-%m-%dT%H:%M:%S%z")

class CustomModel(BaseModel):
    model_config = ConfigDict(
        json_encoders={datetime: datetime_to_gmt_str},
        populate_by_name=True,
    )

class User(CustomModel):
    created_at: datetime # Automatically formatted
```
