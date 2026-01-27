---
title: Code Maintenance
impact: LOW
impactDescription: Keeps codebase clean and performant
tags: maintenance, refactoring, dead-code
---

## Code Maintenance

Regularly sanitize the codebase to remove technical debt.

### Dead Code Elimination
Analyze the AST to find unused endpoints or "Zombie Code" (commented out blocks). Delete them immediately; do not just comment them out.

### Pydantic V2 Standards
Ensure all models follow Pydantic V2 syntax:
- Use `model_config = ConfigDict(...)` instead of `class Config:`.
- Use `@field_validator` instead of `@validator`.
- Use `Field(..., description="...")` for documentation.

### Automated Sanitation
Run automated scripts (like Ruff) to handle imports and whitespace.
