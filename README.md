# 🌍 AX Agent Registry

The official global repository for [AX (Agent Package Manager)](https://github.com/ahmed6ww/ax). 

This registry serves as the central hub where developers from around the world share, discover, and improve specialized AI agent configurations. By contributing to this registry, you are helping to build a universal library of expert "identities" that can run anywhere (Claude Code, Cursor, etc.).

## 🎯 Purpose

- **Democratize Expert Knowledge**: Share specialized prompts and skillsets (e.g., "Senior Rust Engineer", "QA Specialist") so anyone can spin up an expert agent in seconds.
- **Write Once, Run Anywhere**: Define an agent's behavior once in a universal format, and let AX compile it for any supported environment.
- **Community Driven**: A collaborative space to iterate on what makes a "good" agent.

## 📦 Available Agents

These agents are built on the **Agent Skill Standard**, offering rich, multi-file knowledge bases and deterministic scripts.

| Agent | Version | Description |
|-------|---------|-------------|
| 🧹 [code-cleaner](code-cleaner/) | 1.0.0 | Refactor code to remove technical debt, eliminate dead code, and enforce SOLID principles without altering runtime behavior. |
| 🏛️ [enterprise-code-architect](enterprise-code-architect/) | 2.0.0 | Expert guidance on system design, repository strategy (Monorepo vs Polyrepo), and architectural patterns (Hexagonal, Clean, Onion). |
| 🐍 [fastapi-code-cleaner](fastapi-code-cleaner/) | 1.0.0 | Refactor and sanitize FastAPI codebases by removing dead code, enforcing Pydantic V2 standards, and running deterministic linters. |
| 🚀 [fastapi-code-optimizer](fastapi-code-optimizer/) | - | Expert Python Backend Engineer specializing in high-performance FastAPI applications. |
| 🏗️ [fastapi-code-structure](fastapi-code-structure/) | 2.0.0 | Enforce enterprise-grade project structure (Dispatch style), dependency injection patterns, and async concurrency rules. |
| 🧪 [fastapi-tdd](fastapi-tdd/) | 1.0.0 | Expert guide for Test-Driven Development in FastAPI, focusing on the "Quads" strategy and async testing patterns. |
| ⚛️ [nextjs-code-structure](nextjs-code-structure/) | 1.0.0 | Architect scalable Next.js applications using Feature-Sliced Design and Server Component patterns. |
| 🐘 [postgresql-best-practices](postgresql-best-practices/) | 1.0.0 | OpenAI source-faithful PostgreSQL scaling playbook based on "Scaling PostgreSQL to the next level" (Jan 22, 2026). |

## 🤝 How to Contribute

We welcome contributions from developers across the globe! Whether you've crafted the perfect Python debugging assistant or a deeply knowledgeable Kubernetes operator, we want your agent.

### Quick Start Guide

1.  **Fork & Clone**
    Fork this repository and clone it to your local machine.

2.  **Create Your Agent**
    Create a new directory for your agent (e.g., `my-special-agent/`).
    Inside, create a `SKILL.md` file with the following frontmatter:
    
    ```markdown
    ---
    name: my-special-agent
    description: Brief description of what your agent does.
    version: 1.0.0
    allowed-tools: "Read,Write" 
    ---
    
    # Detailed Instructions
    
    Your agent's main prompt and instructions go here...
    ```

3.  **Add Resources (Optional)**
    You can add `scripts/` or `references/` folders inside your agent directory to provide specialized tools or knowledge base files.

4.  **Submit a PR**
    Open a Pull Request with your new agent directory. Once approved, it will be instantly available to all AX users.

For detailed schema documentation and strict guidelines, please read [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT
