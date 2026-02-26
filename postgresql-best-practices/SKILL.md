---
name: postgresql-best-practices
description: Capture and apply OpenAI's PostgreSQL scaling approach exactly from the OpenAI post "Scaling PostgreSQL to the next level" (January 22, 2026). Use when building, reviewing, or planning PostgreSQL architecture, partitioning/indexing, query optimization, schema migrations, replication, and load balancing with strict source fidelity.
version: 1.0.0
allowed-tools: "Read,Write"
---

# PostgreSQL Best Practices (OpenAI Golden Knowledgebase)

## Canonical Source

- Read `{baseDir}/references/openai-scaling-postgresql.md` first.
- Source URL: `https://openai.com/index/scaling-postgresql/`
- Published: `January 22, 2026`

## Non-Negotiable Rules

1. Preserve all named technologies, numbers, and dates exactly as written in the source.
2. Preserve section order and intent exactly:
   - `Use Postgres for everything`
   - `Partitioning and indexing strategy`
   - `Query optimization`
   - `Schema management`
   - `Replication and load balancing`
   - `Results`
3. Keep technology and project names unchanged: `Citus`, `Citus columnar`, `PgBouncer`, `PgAnalyze`, `Patroni`, `Haste`, `pgroll`, `pgai`.
4. If a detail is not in the source file, explicitly state: `Not stated in the source.`
5. Do not add outside recommendations, interpretations, or alternative patterns that are not present in the source.

## Required Coverage

When summarizing or operationalizing, cover all of the following source facts:

- Scale baseline and growth metrics:
  - Over `4 billion queries` every day
  - Over `2,000` database instances
  - Growth from one Postgres instance in `2022`
  - Over `1 billion` monthly users and over `800 million` weekly users
  - Traffic growth of about `2.5x` in just over a year
- Platform strategy:
  - Keep PostgreSQL as the core datastore
  - Use `Citus` and `Citus columnar` for distributed and analytical/high-throughput use cases
- Partitioning/indexing decisions:
  - Hash partitioning for large event/log tables
  - Time-range partitioning for append-only datasets
  - Composite index strategy
  - Custom index migration tooling to avoid blocking writes
  - Bottlenecks: table bloat, autovacuum inefficiencies, poor index selectivity
  - Spike drivers: full table scans, huge B-tree indexes, write amplification from hot rows
- Query optimization operations:
  - Query fingerprints and execution stats
  - Lock contention and long-running transaction identification
  - Rewriting expensive joins/subqueries
  - Statement-level timeout and retry strategy
  - Query budget alerts and EXPLAIN-based review workflows
  - Reported impact: `43%` DB load reduction, `38%` p95 latency reduction
- Schema management workflows:
  - Expand -> migrate -> contract
  - Async backfills with throttling and checkpointing
  - Canary migrations with progressive rollout
  - Automatic rollback on failing migration health checks
  - Open-sourced tools: `Haste` and `pgroll`
- Replication and load balancing:
  - Region-aware read replicas
  - Replica lag monitoring and query shedding
  - Dedicated analytical replicas
  - Failover orchestration with `Patroni` and custom routing logic
  - Deep integration of `PgBouncer` and `PgAnalyze`
- Results and forward direction:
  - Low latency under exponential growth
  - High migration velocity without sacrificing uptime
  - Operating thousands of instances with lean infrastructure teams
  - Ongoing iteration and open-source contributions including `haste`, `pgroll`, `pgai`

## Output Format

When producing a complete answer, use these exact headings in this order:

1. `Use Postgres for everything`
2. `Partitioning and indexing strategy`
3. `Query optimization`
4. `Schema management`
5. `Replication and load balancing`
6. `Results`

Always include the source URL when attribution is requested.
