# Starter governance audit — 2026-10-31

## Status: BLOCKED / NOT VERIFIED FOR PRODUCTION
This is an evidence-based record, not an unconditional certification.

## Verified from GitHub
- GitHub Actions recognized and ran the Validation Gate workflow: run 41254815589.
- "Starter Unit Tests" job succeeded in that run; this establishes a successful execution for the then-existing tests.
- "Project Verification" job failed. The project matrix deliberately contains unconfigured test tiers: ci/checks.json.
- A subsequent commit 0fca3892c99022991a4cfe178f79c93a961ab352 added tests for command success, failure, missing executable, result evidence, and fail-closed configuration. Refer to Actions for the outcome of this newer run; do not assume it passed.
- No verified active ruleset or branch protection: the connected GitHub API returned HTTP 403 on GET /branches/main/protection.

## Implemented controls
- Agent engineering contract (AGENTS.md), scope guard, dependency impact analysis and full regression rules.
- Read-only reviewer protocol (PONTO.md) with detailed report template.
- Project bootstrap and independent-review agent skills.
- Python verification runner, six named test tiers, JSON result evidence, and GitHub Actions job.
- Branch protection setup and verification guide (docs/branch-protection.md).

## Known gaps
1. This is a stack-agnostic template, not an application. Configure real project tests per tier before feature work.
2. The verification runner cannot prove full functional coverage just by running commands. A project's test design, coverage and independent review remain essential.
3. Branch rulesets must be configured in GitHub and enforcement validated via a failing PR and a passing PR.
4. The current GitHub integration lacks sufficient permission to inspect/configure branch protection (HTTP 403). Do not claim protection exists.
5. A separate autonomous review agent is not running as a service. The skill defines the process for an independent read-only reviewer when supported.

## Required acceptance evidence for a new project
- Actual checks specified in ci/checks.json; execution results attached.
- Successful unit, component, integration, E2E and full regression checks as applicable, with exclusions justified.
- A reviewed change-impact report identifying relevant direct and indirect references.
- GitHub ruleset active for main, requiring PR and passing Project Verification status.
- Evidence that a failing PR cannot be merged.

## Conclusion
The starter's *framework* has been established, but production readiness is intentionally denied pending project-specific setup and enforced repository protections. Test results must be assessed per commit and cannot be inferred from file presence.
