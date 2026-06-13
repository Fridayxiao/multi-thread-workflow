# Phase 6: Execution, Verification, And Review

Read this file during implementation and integration.

## Goal

Execute the confirmed plan, verify results, review changes against prior decisions, integrate outputs, and update source-of-truth documents.

## Approach

1. Follow `05-execution-paths.md`.
2. Use TDD for code tasks where practical:
   - bugs: reproduce or write a failing test first;
   - features: define acceptance, unit, or integration tests before implementation where practical;
   - refactors: confirm coverage or add characterization tests when needed.
3. Do not weaken tests just to pass.
4. Run relevant verification before handoff, before commit when committing, and after integration.
5. Use appropriate reviewers: `code-reviewer`, `test-engineer`, `security-auditor`, `architect`, `product-designer`, or `docs-maintainer`.
6. Use a thread for non-trivial review-gated execution unless the lead agent owns the work directly and runs review itself.
7. Do not assign review-gated execution to an ordinary subagent, because ordinary subagents cannot call reviewer subagents before handoff.
8. If a planned thread or reviewer is unavailable, state the fallback, continue only when safe, and record residual risk in `06-execution-log.md`.
9. Pause and realign with the user if implementation changes scope, risk, requirements, selected solution, acceptance criteria, or permissions.

## Artifact

Create or update `06-execution-log.md`. Use `template-documents.md`.

## Gate

Proceed to delivery only when:

- Execution paths are complete or explicitly canceled.
- Verification has run or residual risk is explicit.
- Non-trivial review-gated execution used a thread, or the lead agent owned the work directly and ran review.
- Review findings are fixed or accepted as risk with rationale.
- Documents `01`, `02`, `03`, and `05` still match the delivered state.

## Rollback

Return to Phase 1 for requirement drift, Phase 2 for solution flaws, Phase 3 for incomplete criteria, or Phase 5 for integration-plan failure.
