# Contributing Agents to AX Registry

Thank you for your interest in contributing an agent to AX! 🎉

## How to Submit an Agent

### 1. Fork this repository

### 2. Create your agent YAML file

Create a new file in `agents/` directory following this schema:

```yaml
name: "your-agent-name"
version: "1.0.0"
description: "Brief description of what your agent does"
author: "your-github-username"

identity:
  model: "claude-3-5-sonnet-latest"  # or "opus", "haiku"
  icon: "🤖"  # Single emoji representing your agent
  system_prompt: |
    Your agent's system prompt goes here.
    This defines the agent's personality and expertise.

skills:
  - name: "skill-name"
    content: |
      # Skill Title
      
      Knowledge and context for this skill.
      Use markdown formatting.

mcp:  # Optional - MCP tool integrations
  - name: "tool-name"
    command: "command"
    args: ["arg1", "arg2"]
    env:
      ENV_VAR: "value"
    setup_url: "https://example.com/api-key" # Optional - Link to get API key
```

### 3. Update registry.json

Add your agent to the `registry.json` file:

```json
{
  "name": "your-agent-name",
  "version": "1.0.0",
  "description": "Brief description",
  "author": "your-github-username"
}
```

### 4. Submit a Pull Request

- Use a descriptive PR title: `Add agent: your-agent-name`
- Describe what your agent does in the PR description
- Ensure your YAML is valid

## Guidelines

### Naming
- Use lowercase with hyphens: `my-agent-name`
- Be descriptive but concise

### System Prompts
- Be specific about the agent's expertise
- Include clear guidelines and patterns
- Use markdown formatting

### Skills
- Break down knowledge into logical sections
- Include code examples where helpful
- Keep content focused and actionable

### Quality Checks
- [ ] Valid YAML syntax
- [ ] All required fields present
- [ ] System prompt is detailed and useful
- [ ] Description accurately reflects capabilities

## Questions?

Open an issue if you have questions about contributing!
