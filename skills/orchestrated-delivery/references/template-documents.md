# Document Templates

Read this file when drafting or updating phase documents.

## Compact Writing Rules

- Omit empty sections.
- Use bullets for short lists and tables only when comparison or traceability is clearer.
- Give every must-have requirement a stable `R-*` ID. Add IDs to constraints, assumptions, risks, and terms when later phases need traceability.
- Record user confirmations with date or turn context.
- Add an "Earlier Document Check" note when a phase confirms prior documents are still valid or need changes.

## `01-problem-goal-requirements.md`

```markdown
# Problem, Goal, And Requirements

## Original Request

## Context Reviewed

## User-Perspective Problem

## Current State

## Desired State

## Goal

## Scope
- In:
- Out:
- Non-goals:

## Requirements
- R-001 (Must): <requirement>
  - Source/owner:
  - Rationale:
  - Acceptance hint / validation surface:

## Constraints
- C-001:

## Assumptions And Open Questions
- A-001:
- Q-001:

## Risks
- K-001:

## Terms
- T-001:

## Earlier Document Check
- Reviewed:
- Updates needed:

## User Confirmation
- Status:
- Date/turn:
- Confirmation:
```

## `02-solution-options.md`

```markdown
# Solution Options

## Research Summary

## Existing Or Reusable Solutions Checked

## Option A
- Description:
- Benefits:
- Costs:
- Risks:
- Fit to Phase 1 IDs (`R-*`, `C-*`, `A-*`, `K-*`):

## Option B
- Description:
- Benefits:
- Costs:
- Risks:
- Fit to Phase 1 IDs (`R-*`, `C-*`, `A-*`, `K-*`):

## Other Options Considered

## Freshness And Deprecation Checks

## Recommendation

## User Decision
- Selected option:
- Date/turn:
- Rationale:

## Earlier Document Check
```

## `03-acceptance-criteria.md`

```markdown
# Acceptance Criteria

## Criteria
- AC-001:
  - Covers:
  - Validation:

## Unacceptable Outcomes

## Validation Plan

## User Confirmation
- Status:
- Date/turn:
- Confirmation:

## Earlier Document Check
```

## `04-prototype-notes.md`

```markdown
# Prototype Notes

## Purpose

## Output

## How To View Or Use

## Validates

## Does Not Validate

## User Feedback

## Impact On Prior Documents

## Earlier Document Check
```

## `05-execution-paths.md`

```markdown
# Execution Paths

## Selected Solution

## Execution Strategy

## Serial Work

## Parallel Paths
- Path:
  - Covers:
  - Owner:
  - Scope:
  - Output:
  - Verification:
  - Review:
  - Review-gated: yes/no
  - If review-gated: thread or lead-owned task, with reason
  - Stop conditions:

## Integration And Rollback

## User Confirmation
- Status:
- Date/turn:
- Confirmation:

## Earlier Document Check
```

## `06-execution-log.md`

```markdown
# Execution Log

## Current State

## Work Completed

## Delegation And Threads

## Verification Evidence

## Review Results

## Integration Notes

## Document Updates

## Open Risks Or Blockers

## Earlier Document Check
```

## `07-delivery-report.md`

```markdown
# Delivery Report

## Summary

## Delivered Work

## Acceptance Criteria Results
- AC-001:
  - Result:
  - Evidence:

## Verification Performed

## Review Summary

## Known Limitations And Risks

## User Acceptance Steps

## Final Document Consistency Check

## Final User Acceptance
- Status:
- Date/turn:
- Notes:
```
