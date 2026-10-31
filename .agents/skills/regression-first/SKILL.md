---
name: regression-first
description: Fix bugs and evolve behavior with reproduction, focused tests, regression checks, and honest verification reporting.
---
# Regression-first workflow

1. Reproduce or characterize the observed problem with evidence; do not guess.
2. Add a failing regression test when feasible, or document a deterministic manual reproduction.
3. Make the smallest correction that addresses the root cause.
4. Execute focused tests and checks for affected consumers, then broader validation when practical.
5. Compare pre/post behavior and review the patch for newly introduced edge cases.
6. Do not disable tests, loosen assertions, or swallow errors to obtain green checks.
7. Report exact commands and outcomes; explicitly mark anything unverified.
