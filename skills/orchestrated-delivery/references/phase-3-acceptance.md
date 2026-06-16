# Phase 3: Acceptance Criteria

Read this file before execution planning. Do not use threads in this phase.

## Goal

Define what done means before implementation or delivery begins.

## Approach

1. Map each must-have requirement to at least one acceptance criterion.
2. Include user-visible behavior, quality expectations, verification method, and unacceptable outcomes.
3. Keep criteria testable where possible. If a criterion cannot be tested directly, state the substitute judgment method.
4. Optionally ask an advisory subagent to check testability or product coverage after the lead drafts criteria.

## Artifact

Create or update `03-acceptance-criteria.md`. Use `template-documents.md`.

## Output Contract (Required Fields)

`03-acceptance-criteria.md` must include:

- `AC-*` criteria that cover every must-have `R-*` requirement;
- validation method for each criterion, or an explicit substitute judgment method when direct testing is not possible;
- unacceptable outcomes -- may be stated per-criterion or as a document-level summary, but must appear at least once at the document level;
- validation plan covering tests, inspection, demo, user review, or other evidence as appropriate;
- explicit user confirmation.

## Gate

Proceed only when:

- Core requirements are covered.
- Each criterion has a validation method or explicit substitute judgment method.
- Unacceptable outcomes are stated.
- The user explicitly confirms the criteria.

## Rollback

Return to Phase 1 if requirements are incomplete. Return to Phase 2 if criteria conflict with the selected solution.
