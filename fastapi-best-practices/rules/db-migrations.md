---
title: Meaningful Migrations
impact: HIGH
impactDescription: 
tags: database, migrations, alembic
---

## Meaningful Migrations

- **Static & Reversible:** Migrations must typically be reversible (provide a `downgrade`).
- **Descriptive Names:** Use the `slug` field in Alembic to describe the change (e.g., `add_users_table`).
- **File Template:** Configure `alembic.ini` to prefix files with dates for ordering.

```ini
file_template = %%(year)d-%%(month).2d-%%(day).2d_%%(slug)s
```
