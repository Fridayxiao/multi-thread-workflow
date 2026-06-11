# Multi-Thread Delivery Templates

Use these as adaptable skeletons. Keep required content, but adjust format to the task. For Lite Mode, sections may be compressed as long as the required decisions remain explicit and durable.

Default workflow document directory: `docs/agent-workflows/<goal-slug>/`, unless the user specifies another location.

## `01-problem-goal-requirements.md`

```markdown
# Problem, Goal, and Requirements

## Original Request

## Problem Definition

## Goal

## Success Criteria Summary

## Requirements

## Non-Functional Requirements

## Constraints

## Non-Goals

## Unknowns and Assumptions

## Risks

## Upstream Document Check
- Reviewed:
- Updates needed:
- User reconfirmation needed:

## User Confirmation
- Status:
- Date/turn:
- Confirmation:
```

## `02-solution-options.md`

```markdown
# Solution Options

## Research Summary

## Existing or Reusable Solutions Investigated

## Context Collected for Custom Design

## Current Context and Evidence

## Option A
- Description:
- Benefits:
- Costs:
- Risks:
- Fit to requirements:

## Option B
- Description:
- Benefits:
- Costs:
- Risks:
- Fit to requirements:

## Other Options Considered

## Freshness and Deprecation Checks

## Recommendation

## User Decision
- Selected option:
- Rationale:
- Date/turn:

## Upstream Document Check
- Reviewed:
- Updates needed:
- User reconfirmation needed:
```

## `03-acceptance-criteria.md`

```markdown
# Acceptance Criteria

## User-Visible Criteria

## Quality Criteria

## Requirement Traceability
| Requirement | Acceptance criterion | Validation method |
| --- | --- | --- |

## Unacceptable Outcomes

## Validation Plan

## Upstream Document Check
- Reviewed:
- Updates needed:
- User reconfirmation needed:

## User Confirmation
- Status:
- Date/turn:
- Confirmation:
```

## `04-prototype-notes.md`

```markdown
# Prototype Notes

## Prototype Purpose

## Prototype Output

## How to View or Use

## What It Validates

## What It Does Not Validate

## User Feedback

## Impact on Requirements

## Impact on Solution

## Impact on Acceptance Criteria

## Follow-Up Decisions

## Upstream Document Check
- Reviewed:
- Updates needed:
- User reconfirmation needed:
```

## `05-execution-paths.md`

```markdown
# Execution Paths

## Selected Solution Summary

## Execution Strategy

## Serial Dependencies

## Parallel Paths
| Path | Goal | Scope | Inputs | Outputs | Validation | Stop conditions |
| --- | --- | --- | --- | --- | --- | --- |

## Worker Thread Plan

## Integration Strategy

## Verification Strategy

## Risks and Rollback Points

## Upstream Document Check
- Reviewed:
- Updates needed:
- User reconfirmation needed:

## User Confirmation
- Status:
- Date/turn:
- Confirmation:
```

## `06-execution-log.md`

```markdown
# Execution Log

## Current Phase State

## Thread Registry
| Thread | Purpose | Scope | Source docs | Status | Verification | Review | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Work Completed

## Verification Evidence

## Pre-Handoff Verification

## Pre-Commit / Pre-Delivery Verification

## Reviewer Sub-Agent Summaries

## Integration Notes

## Document Updates

## Open Risks and Accepted Risks

## Blockers

## Upstream Document Check
- Reviewed:
- Updates needed:
- User reconfirmation needed:
```

## `07-delivery-report.md`

```markdown
# Delivery Report

## Summary

## Delivered Work

## Acceptance Criteria Results
| Criterion | Result | Evidence |
| --- | --- | --- |

## Verification Performed

## Important Decisions and Tradeoffs

## Known Limitations and Risks

## User Acceptance Steps

## Follow-Up Recommendations

## Final Document Consistency Check

## Final User Acceptance
- Status:
- Date/turn:
- Notes:
```

## Research or Design Thread Prompt

```text
You are a bounded research/design worker thread in the Multi-Thread Delivery workflow.

Current phase: Phase 2, Research and Solution Design.

User goal:
<goal summary>

Confirmed requirements and constraints:
<summary or paths>

Your task:
<specific research/design task>

Scope:
<what to investigate>

Non-scope:
<what not to decide or change>

Context to read:
<files, docs, URLs, logs, code areas>

Skill requirement:
Before acting, identify relevant available skills for this task. Use the minimal set that applies. Read and follow each selected SKILL.md. In your handoff, report which skills you used, which relevant skills you skipped and why, and whether any skill instruction conflicted with this workflow brief.

Expected output:
- Investigation scope
- Existing or reusable solutions investigated
- Context collected for custom design if no suitable existing solution exists
- Evidence and citations or code references
- At least two options when applicable
- Benefits, costs, risks, and freshness/deprecation checks
- Recommendation with rationale
- Unknowns and questions for the lead agent

Do not change requirements, acceptance criteria, or user-facing decisions. If the brief conflicts with reality, stop and report the conflict.
```

## Prototype Thread Prompt

```text
You are a bounded prototype worker thread in the Multi-Thread Delivery workflow.

Current phase: Phase 4, Demo or Prototype.

User goal and selected solution:
<summary>

Acceptance criteria relevant to the prototype:
<summary>

Your task:
<prototype task>

Scope:
<what to build or demonstrate>

Non-scope:
<what not to build>

Writable boundaries:
<files or artifacts allowed>

Skill requirement:
Before acting, identify relevant available skills for this task. Use the minimal set that applies. Read and follow each selected SKILL.md. In your handoff, report which skills you used, which relevant skills you skipped and why, and whether any skill instruction conflicted with this workflow brief.

Expected output:
- Prototype/demo artifact
- How to view or run it
- What it validates
- What it does not validate
- Verification performed
- Risks and assumptions
- Suggested updates to requirements, solution, or acceptance criteria

Stop and report if the prototype would require scope expansion or contradicts confirmed documents.
```

## Execution Worker Thread Prompt

```text
You are a bounded execution worker thread in the Multi-Thread Delivery workflow.

Current phase: Phase 6, Execution, Verification, Review.

User goal:
<goal summary>

Source-of-truth context:
- Requirements: <summary or path>
- Selected solution: <summary or path>
- Acceptance criteria: <summary or path>
- Execution plan: <summary or path>

Your task:
<specific execution path>

Scope:
<allowed work>

Non-scope:
<excluded work>

Writable boundaries:
<files or artifacts allowed>

Verification requirements:
<tests, checks, walkthroughs, fact checks, or other validation>

Skill requirement:
Before acting, identify relevant available skills for this task. Use the minimal set that applies. Read and follow each selected SKILL.md. In your handoff, report which skills you used, which relevant skills you skipped and why, and whether any skill instruction conflicted with this workflow brief.

Reviewer requirement:
Before handoff, call the predefined reviewer sub-agent with the goal, requirements, selected solution, acceptance criteria, execution plan scope, actual deliverable or diff, verification already run, and known risks. Handle the findings before returning to the lead agent.

Expected handoff:
- Completed work
- Files or artifacts changed
- Verification performed and results
- Pre-commit verification performed, if a commit was created or requested
- Skills used and skipped
- Reviewer sub-agent summary
- Findings fixed
- Findings accepted as risk, with rationale
- Open risks or blockers
- Suggested source-of-truth document updates
- Integration notes for the lead agent

Stop and report if you need to change requirements, solution, acceptance criteria, scope, writable boundaries, or destructive operations.
```

## Worker Handoff Checklist

```text
Completed work:

Changed files or artifacts:

Verification:

Skills used:

Relevant skills skipped:

Reviewer sub-agent summary:

Review findings fixed:

Accepted risks:

Open risks or blockers:

Suggested document updates:

Integration notes:
```

## Reviewer Sub-Agent Context Checklist

Provide the predefined reviewer sub-agent:

- User goal.
- Requirements.
- Selected solution.
- Acceptance criteria.
- Execution plan scope.
- Actual deliverable, diff, or artifact summary.
- Verification already run.
- Known risks.
- Review scope and non-scope.

Use the reviewer sub-agent's own system prompt for review behavior and output expectations.

## User Gate Prompt Pattern

```text
Current phase: <phase>.

Decision needed:
<what the user is confirming>

Summary:
<phase conclusion>

Key tradeoffs or risks:
<bullets>

Recommended default:
<recommendation, if any>

Please explicitly confirm, reject, or request changes before I proceed.
```
