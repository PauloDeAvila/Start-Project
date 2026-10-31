# Start Project

A reusable, language-agnostic foundation for software projects developed with AI coding agents, especially Codex.

## Purpose

Start a new project with clear operating rules, reusable task-specific skills, explicit architectural decisions and lightweight context mapping. This is a *template*, not a code generator or a complete application.

## Getting started

1. Use GitHub's **Use this template** after enabling the template setting, or copy the repository into a new project.
2. Update `PROJECT.md` with the actual product, constraints, stack and acceptance criteria.
3. Start Codex **from the project root**, so it discovers `AGENTS.md` and `.agents/skills/`.
4. Ask the agent to map the repository before major changes, then plan and implement a small vertical slice.
5. Keep `docs/architecture.md`, `docs/context-map.md`, and `docs/decisions.md` current as the project evolves.

## Repository layout

- `AGENTS.md` — short, persistent coding-agent operating rules.
- `PROJECT.md` — project-specific brief to fill in when starting a new project.
- `.agents/skills/` — reusable workflows with `SKILL.md` metadata and instructions.
- `docs/` — lightweight architecture, context map and decision log.
- `.github/pull_request_template.md` — review and verification checklist.

## Working agreement

Read before editing; separate observed facts from guesses; change the smallest coherent unit; run relevant checks; report changes and remaining risks. Never claim a test ran unless it actually ran.

## Usage note

Skills are instructions, not executable tooling. MCP connections, compilers, test runners, external accounts and credentials are deliberately not installed or embedded here. Configure them per project and per machine.
