---
title: Explicit Index Naming
impact: MEDIUM
impactDescription: Prevents migration conflicts and ambiguity
tags: database, sqlalchemy, alembic
---

## Explicit Index Naming

Do not rely on auto-generated names for database constraints and indexes (like `ix_user_email`). They can vary between environments or Alembic versions. Define a strict naming convention in your SQLAlchemy metadata.

**Correct:**

```python
from sqlalchemy import MetaData

naming_convention = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}
metadata = MetaData(naming_convention=naming_convention)
```
