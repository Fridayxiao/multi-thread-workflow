# Phase 1: Problem, Goal, And Requirements

Read this file when aligning the user goal. Do not use threads in this phase.

## Goal

Define the problem from the user's perspective, the target outcome, current state, desired state, scope, requirements, constraints, assumptions, open questions, non-goals, terms, and risks clearly enough that later phases can trace decisions back to confirmed requirements.

## Approach

1. First synthesize a draft from the conversation and available project context. Do not start with a broad interview when the answer can be inferred.
2. For codebase work, inspect applicable guidance and domain documents before finalizing terms, including `AGENTS.md`, `CONTEXT.md`, `CONTEXT-MAP.md`, relevant `docs/adr/`, nearby code, tests, and docs.
3. Use the project's domain language. If user terms conflict with code or docs, call out the conflict and resolve the canonical term.
4. Test fuzzy requirements with concrete scenarios: primary path, edge cases, permissions, data boundaries, integration boundaries, failure modes, and unacceptable outcomes.
5. Ask only targeted blocking questions. Ask one decision at a time, include a recommended answer, and wait when the answer changes the workflow.
6. Assign stable `R-*` IDs to every must-have requirement. Assign IDs to constraints, assumptions, open questions, risks, non-goals, and terms when later phases need to reference them.
7. For every must-have requirement, record the requirement text, source or owner, rationale, and acceptance hint or validation surface.

## Artifact

Create or update `01-problem-goal-requirements.md`. Use `template-documents.md`.

## Gate

Proceed only when:

- The document states the problem, goal, current state, desired state, scope, requirements, constraints, assumptions, open questions, non-goals, terms, and risks at the needed depth.
- Every must-have requirement has a stable `R-*` ID.
- Every must-have requirement includes source or owner, rationale, and acceptance hint or validation surface.
- Must-have requirements do not depend on unresolved blocking questions.
- The user explicitly confirms the Phase 1 result.

## Rollback

Return to Phase 1 when later work exposes vague, wrong, or unstable requirements.
