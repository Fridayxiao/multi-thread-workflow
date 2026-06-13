# Phase 5: Execution Paths

Read this file before implementation. Do not use threads in this phase.

## Goal

Plan how to execute the selected solution by identifying serial dependencies, parallel paths, ownership boundaries, verification, review, integration, risks, and rollback points.

## Approach

1. Summarize the selected solution and acceptance criteria.
2. Separate serial work from parallel work.
3. For each path, define goal, scope, non-scope, readable context, writable boundaries, expected output, verification, review need, and stop conditions.
4. Identify which paths should use a thread, ordinary subagent, reviewer, or lead-owned work.
5. Define integration order and rollback points.
6. Optionally ask advisory reviewers for plan quality, test strategy, security risk, or architecture risk.

## Artifact

Create or update `05-execution-paths.md`. Use `template-documents.md`.

## Gate

Proceed only when:

- Each execution path maps to requirements and acceptance criteria.
- Parallel and serial work are clear.
- Verification and review are planned.
- Integration and rollback are defined.
- The user explicitly confirms the execution path.

## Rollback

Return to Phase 2 when planning exposes solution flaws. Return to Phase 3 when acceptance criteria are incomplete.
