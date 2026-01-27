---
title: Database Naming Conventions
impact: MEDIUM
impactDescription: 
tags: database, naming, standards
---

## Database Naming Conventions

Maintain strict naming conventions for database objects to ensure consistency.

- **Tables:** `lower_case_snake`, singular (e.g., `user`, `post_like`).
- **Pivot Tables:** `table1_table2` (e.g., `user_role`).
- **Columns:** `lower_case_snake`.
- **Date/Time:** Suffix with `_at` for timestamps (e.g., `created_at`), `_date` for dates (e.g., `birth_date`).
- **Foreign Keys:** `related_table_id` (e.g., `creator_id`, `post_id`).

**Examples:**

- Table: `payment_account`
- Column: `is_active`
- Column: `published_at`
