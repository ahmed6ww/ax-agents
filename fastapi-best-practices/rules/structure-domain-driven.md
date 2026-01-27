---
title: Structure by Domain
impact: HIGH
impactDescription: Improved scalability and maintainability for large projects
tags: structure, architecture, scalability
---

## Structure by Domain

Organize code by domain (functionality area) rather than by file type (e.g., controllers, models). This keeps related logic together and makes the codebase more navigable as it grows.

**Incorrect (Layer-based structure):**

```text
src/
├── routers/
│   ├── auth.py
│   └── posts.py
├── schemas/
│   ├── auth.py
│   └── posts.py
├── services/
│   ├── auth.py
│   └── posts.py
```

**Correct (Domain-based structure):**

```text
src/
├── auth/
│   ├── router.py
│   ├── schemas.py
│   ├── service.py
│   └── dependencies.py
├── posts/
│   ├── router.py
│   ├── schemas.py
│   ├── service.py
│   └── dependencies.py
└── main.py
```

Reference: [Netflix Dispatch](https://github.com/Netflix/dispatch)
