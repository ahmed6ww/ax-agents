---
title: Database Connection Pooling
impact: HIGH
impactDescription: Prevents connection exhaustion and latency
tags: database, performance, sqlalchemy
---

## Database Connection Pooling

Ensure connection pooling is enabled in SQLAlchemy (or your ORM) to manage database connections efficiently.

- **Use QueuePool:** Default in SQLAlchemy for many engines.
- **Recommended Settings:**
  - `pool_size`: 10–20 (adjust based on load)
  - `max_overflow`: 10–20
  - `pool_recycle`: ~1800s (to prevent stale connections)

**Correct:**

```python
engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=10,
    pool_recycle=1800
)
```
