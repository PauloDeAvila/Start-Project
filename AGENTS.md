# Engineering contract for AI agents

Read this file before any task. This project's source of truth is PROJECT.md and its existing implementation, not your assumptions.

## Non-negotiable rules
1. **Respect scope.** Restate the task's goal, affected components, constraints, and acceptance criteria. Do not add unrelated features, refactors, dependencies, or cleanup.
2. **Inspect before editing.** Locate entry points, callers, contracts, dependencies, tests, and error paths. Read the existing implementation instead of guessing.
3. **Avoid speculative abstraction.** Prefer the simplest cohesive solution that fits existing patterns. Do not introduce generic layers, factories, base classes, wrappers, or new architecture without a concrete need and demonstrated benefit.
4. **Protect invariants.** Preserve existing behavior, public APIs, file formats, data contracts, and backwards compatibility unless the task explicitly authorizes changes.
5. **Assess blast radius.** For every change, list what can break, who calls it, and what tests must protect it. Never fix component A by silently breaking component B.
6. **Make narrow edits.** Modify the fewest appropriate modules. Separate behavior changes from refactors. Avoid sweeping rewrites and unrelated formatting diffs.
7. **Test the change.** Add/update focused tests plus regression tests for affected paths. Run available formatters, type checks, tests and build steps relevant to the change. Never claim checks passed if they were not run.
8. **Do not hide failures.** No broad exception swallowing, hardcoded success, disabling tests, weakening assertions, or removing functionality merely to pass validation.
9. **Maintain documentation.** Update context map and architectural decisions only when actual contracts or structure changed; avoid documentation churn.
10. **Escalate risk.** Ask before destructive commands, migrations, security-sensitive changes, changes with unclear compatibility, or large architectural decisions.

## Working sequence
**Understand → Map impact → Plan → Edit minimally → Test → Review diff → Report.**
For small, isolated changes, keep the plan brief. For high-risk changes, request approval before execution.

## Required delivery report
- Scope delivered and files changed.
- Behavioral impact, assumptions and contracts preserved.
- Checks run with actual results; name checks not run and why.
- Remaining risks and recommended follow-ups (without executing extras).

## Project context
Read PROJECT.md first. Consult docs/context-map.md for component ownership, docs/architecture.md for boundaries, and docs/decisions.md for accepted tradeoffs. If they are incomplete, mark unknowns; never invent facts.

## Skills
Use the appropriate workflow under .agents/skills when the task requires it. Skills guide behavior; they do not override this contract.
