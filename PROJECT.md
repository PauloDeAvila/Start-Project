# Project brief — complete for each new project

## Purpose and supported functionality
Document what the project does and the actual user journeys.

## In scope
- Supported capabilities and behaviors.

## Explicitly out of scope
- Excluded features, refactors and architectural changes.

## Stack and environments
- Languages, frameworks, versions, operating systems, environments and external prerequisites.

## Architecture and critical invariants
- API/data contracts, dependency direction, compatibility, state and security constraints.

## Acceptance criteria
- Observable, testable expectations and failure behaviors.

## Mandatory verification matrix
Record actual commands and test coverage for every applicable tier. The agent must run all tiers AND the full existing repository suite after each implementation, not just tests for modified files.

| Layer | Commands / suite | Dependencies / prerequisites | Evidence expected |
| --- | --- | --- | --- |
| Basic functions / unit tests | TBD | TBD | Pass/fail and counts |
| Component and subsystem | TBD | TBD | Pass/fail and counts |
| Integration and contracts | TBD | TBD | Pass/fail and counts |
| Full user-flow / E2E | TBD | TBD | Pass/fail and counts |
| Full repository regression | TBD | TBD | All existing tests run |
| Build, lint, types, other applicable checks | TBD | TBD | Actual exit status |

## Verification policy
An implementation is NOT VERIFIED until the complete applicable matrix passes and objective results are recorded. Missing test infrastructure requires creation or explicit BLOCKED status; do not claim completion when verification cannot run. Do not assert absolute 100% correctness.

## Known risks and unresolved questions
- Keep unknowns explicit until confirmed.

## Bootstrap gate (mandatory before feature work)
- [ ] Stack-specific dependencies and real test commands established
- [ ] CI runs actual automated checks across all applicable levels
- [ ] Missing automated coverage identified and addressed or explicitly blocked
- [ ] GitHub PR/branch protection configured and independently confirmed
- [ ] Required CI checks enforced (not merely present as optional actions)
- [ ] Independent review process configured using PONTO.md

Note: The starter workflow deliberately fails pending project-specific test configuration. This is NOT a runnable product test suite.
