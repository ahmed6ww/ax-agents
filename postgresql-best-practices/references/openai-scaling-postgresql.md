# Scaling PostgreSQL to the next level

Source URL: https://openai.com/index/scaling-postgresql/
Published: January 22, 2026

At OpenAI, the Postgres database is one of the backbones for serving our products. We run over 4 billion queries every day and host over 2,000 database instances.

We started from one Postgres instance when we launched ChatGPT in 2022 and now have over 1 billion users monthly and over 800 million users weekly.

To support this growth, we've had to scale our PostgreSQL cluster and evolve our architecture quickly while maintaining strict reliability standards. Our traffic has grown about 2.5x in just over a year.

This post outlines some of the technical decisions we made and lessons learned while scaling PostgreSQL from a single machine to thousands of database instances.

## Use Postgres for everything

At OpenAI's scale, migrating your data stack from PostgreSQL to another datastore can be very costly and complex in terms of development effort. We considered splitting workload to another datastore but ultimately chose to continue scaling PostgreSQL itself due to:

- Existing reliability and operational familiarity
- The flexibility of PostgreSQL's rich ecosystem (indexes, extensions, replication, etc.)
- Reduced migration risk under rapid growth

As our workload diversified, we started to use Citus and Citus columnar to distribute and manage analytical and high-throughput use cases in PostgreSQL.

We ensured the stack remained simple enough for our teams to own and maintain.

## Partitioning and indexing strategy

As we scaled PostgreSQL for workloads of every shape and size, table bloat, autovacuum inefficiencies, and poor index selectivity became key bottlenecks.

We observed major latency spikes due to:

- Full table scans
- Huge B-tree indexes
- Write amplification from hot rows

To mitigate this, we implemented:

- Hash partitioning for large event and log tables
- Time-range partitioning for append-only datasets
- Composite index strategy to preserve read performance
- Custom index migration tooling to avoid blocking writes

Partitioning was especially useful for reducing vacuum pressure and improving cache locality.

Index tuning became a continuous process due to dynamic query patterns and changing access paths.

## Query optimization

At our scale, ORM-generated SQL and poorly tuned joins were no longer acceptable.

We built tooling to profile and optimize high-impact queries by:

- Tracking query fingerprints and execution stats
- Identifying lock contention and long-running transactions
- Rewriting expensive joins and subqueries
- Applying statement-level timeout and retry strategy

We also introduced query budget alerts and EXPLAIN-based review workflows for service teams.

This gave us visibility into query behavior before it became a production incident.

Graph showing reduced database impact from optimization:
- 43% reduction in DB load
- 38% reduction in p95 query latency

## Schema management

Frequent product iteration meant frequent schema changes.

We needed safe migrations without downtime, even for tables with billions of rows.

To achieve this, we designed migration workflows that include:

- Backward-compatible rollouts (expand -> migrate -> contract)
- Async backfills with throttling and checkpointing
- Canary migrations and progressive rollout
- Automatic rollback when migration health checks fail

We open-sourced Haste and pgroll, two tools that helped us manage safe schema changes at scale.

## Replication and load balancing

As read traffic exploded, we moved from simple primary-replica setups to more sophisticated replication topologies.

Our architecture now includes:

- Region-aware read replicas for low-latency access
- Replica lag monitoring and query shedding
- Dedicated replicas for analytical workloads
- Failover orchestration using Patroni and custom routing logic

We also integrated PgBouncer and PgAnalyze deeply into our platform tooling for connection pooling and query observability.

## Results

By continuously investing in PostgreSQL scalability, we've been able to:

- Maintain low query latency under exponential user growth
- Keep migration velocity high without sacrificing uptime
- Operate thousands of Postgres instances with lean infrastructure teams

PostgreSQL has proven to be both flexible and resilient enough for OpenAI's multi-product, global-scale environment.

As we continue to grow, we'll keep iterating on internal tooling and architecture, and we're excited to contribute back to the Postgres community through open source efforts like haste, pgroll, and pgai.
