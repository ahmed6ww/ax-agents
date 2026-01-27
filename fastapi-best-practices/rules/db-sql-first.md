---
title: SQL-First Approach
impact: HIGH
impactDescription: Improved performance for complex queries
tags: database, sql, performance
---

## SQL-First Approach

For complex data retrieval, joins, and aggregations, prefer writing optimized SQL (or robust SQLAlchemy queries) over fetching raw data and processing it in Python. The database is much faster at filtering and aggregating than Pydantic or Python loops.

**Incorrect (Python-side processing):**

```python
posts = await db.all(Post)
for post in posts:
    post.author = await db.get(User, post.author_id) # N+1 problem
```

**Correct (SQL-side join):**

```python
# Fetch everything in one query
query = select(Post, User).join(User, Post.author_id == User.id)
results = await db.execute(query)
```
