---
title: Decouple BaseSettings
impact: MEDIUM
impactDescription: Improves modularity and prevents monolithic config
tags: pydantic, configuration, modularity
---

## Decouple BaseSettings

Do not use a single giant `Config` class for the entire application. Split `BaseSettings` by domain or module. This makes modules more independent and reusable.

**Incorrect (Monolithic Config):**

```python
class Settings(BaseSettings):
    DB_URL: str
    AWS_KEY: str
    STRIPE_KEY: str
    AUTH_SECRET: str
    # ... 50 other vars
```

**Correct (Modular Dependencies):**

```python
# src/auth/config.py
class AuthConfig(BaseSettings):
    JWT_SECRET: str
    JWT_EXP: int = 5

# src/aws/config.py
class AWSConfig(BaseSettings):
    AWS_ACCESS_KEY: str
    AWS_REGION: str
```
