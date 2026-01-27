---
title: Hide Docs in Production
impact: LOW
impactDescription: Security through obscurity
tags: security, docs, openapi
---

## Hide Docs in Production

Do not expose `/docs` and `/redoc` in production environments unless your API is public.

**Correct:**

```python
from fastapi import FastAPI
import os

env = os.getenv("ENVIRONMENT", "production")
openapi_url = "/openapi.json" if env != "production" else None

app = FastAPI(openapi_url=openapi_url)
```
