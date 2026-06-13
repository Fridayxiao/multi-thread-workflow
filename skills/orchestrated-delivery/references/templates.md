# Orchestrated Delivery Templates

Use these as adaptable skeletons. Keep required content, but adjust format to the task. For Lite Mode, sections may be compressed as long as the required decisions remain explicit and durable.

Default workflow document directory: `docs/agent-workflows/<goal-slug>/`, unless the user specifies another location.

Default workflow language: the language the user is currently using, unless the user explicitly requests another language. Translate section headings and template labels to the workflow language when drafting real documents. Keep file names, paths, commands, code symbols, API names, and quoted source text unchanged when needed for precision.

## `01-problem-goal-requirements.md`

```markdown
# Problem, Goal, and Requirements

## Original Request

## Workflow Language

## Context Sources Reviewed
- Conversation:
- Project guidance:
- Domain glossary:
- ADRs or prior decisions:
- Code, tests, docs, logs, or external sources:

## User-Perspective Problem Statement

## Current State

## Desired State

## Primary Goal

## Success Definition

## Actors and Stakeholders

## User Stories and Scenarios
Cover the primary path, important edge cases, failure modes, permission boundaries, data boundaries, integration boundaries, and scenarios that would split the goal into separate workflows.

1. As a <actor>, I want <capability>, so that <benefit>.
2. Edge case:
3. Failure or boundary scenario:

## In Scope

## Out of Scope and Non-Goals

| ID | Item | Rationale |
| --- | --- | --- |
| N-001 |  |  |

## Requirements

| ID | Type | Priority | Requirement | Rationale | Source/Owner | Acceptance Hint / Validation Surface |
| --- | --- | --- | --- | --- | --- | --- |
| R-001 | Functional / Quality / Operational / UX / Security / Data / Documentation | Must / Should / Could |  |  |  |  |

## Constraints

| ID | Constraint | Hard/Soft | Source | Impact |
| --- | --- | --- | --- | --- |
| C-001 |  |  |  |  |

## Assumptions

| ID | Assumption | Confidence | Validation Path | Blocking? |
| --- | --- | --- | --- | --- |
| A-001 |  | High / Medium / Low |  | Yes / No |

## Open Questions

| ID | Question | Recommended Default | Owner | Blocking? | Needed Before Phase |
| --- | --- | --- | --- | --- | --- |
| Q-001 |  |  |  | Yes / No | 2 / 3 / 5 / 6 |

## Domain Terms

| ID | Term | Canonical Meaning | Avoid / Ambiguous Terms | Source |
| --- | --- | --- | --- | --- |
| T-001 |  |  |  |  |

## Known Decisions

| ID | Decision | Why It Is Already Decided | Revisit Trigger |
| --- | --- | --- | --- |
| D-001 |  |  |  |

## Risks and Failure Modes

| ID | Risk / Failure Mode | Impact | Mitigation or Follow-Up |
| --- | --- | --- | --- |
| K-001 |  |  |  |

## Grill Notes
- Fuzzy terms challenged:
- Scenarios used to stress-test requirements:
- Conflicts with glossary, docs, code, or prior decisions:
- User decisions made during clarification:

## Documentation Sync
- CONTEXT.md updates needed:
- ADRs needed:
- Deferred documentation updates:

## Downstream Traceability Rules
- Phase 2 solution options must cite relevant `R-*`, `C-*`, `A-*`, and `K-*` IDs.
- Phase 3 acceptance criteria must map to `R-*` IDs.
- Phase 5 execution paths must cite the `R-*` and acceptance criteria they cover.
- Phase 6 execution and review must report work against the same IDs.

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
- Fit to Phase 1 IDs:

## Option B
- Description:
- Benefits:
- Costs:
- Risks:
- Fit to Phase 1 IDs:

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
| Requirement ID | Acceptance criterion | Validation method |
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
| Path | Requirement / AC IDs | Delegate type | Role | Review-gated | Goal | Scope | Inputs | Outputs | Validation | Stop conditions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Delegation Plan

## Review-Gated Thread Lanes
| Path | Review required before handoff | Reviewer roles | Why thread is required |
| --- | --- | --- | --- |

## Other Thread Escalation Candidates
| Path | Escalation criterion | Why subagent is insufficient |
| --- | --- | --- |

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

## Delegation Registry
| Delegate | Type | Role | Requirement / AC IDs | Review-gated | Purpose | Scope | Source docs | Status | Verification | Review | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Review-Gated Thread Lanes
| Thread | Purpose | Reviewer roles | Verification | Review result | Handoff status |
| --- | --- | --- | --- | --- | --- |

## Other Thread Escalations
| Thread | Escalation criterion | Reason | Status | Result |
| --- | --- | --- | --- | --- |

## Work Completed

## Verification Evidence

## Pre-Handoff Verification

## Pre-Commit / Pre-Delivery Verification

## Review Subagent Summaries

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

## Research or Design Delegate Prompt

```text
You are a bounded research/design delegate in the Orchestrated Delivery workflow.

Workflow language:
<user's current language unless explicitly overridden>

Current phase: Phase 2, Research and Solution Design.

Delegate type and role:
<subagent role, or thread with escalation criterion>

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

Expected output:
- Write the handoff in the workflow language
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

## Prototype Delegate Prompt

```text
You are a bounded prototype delegate in the Orchestrated Delivery workflow.

Workflow language:
<user's current language unless explicitly overridden>

Current phase: Phase 4, Demo or Prototype.

Delegate type and role:
<subagent role, lead-owned task, or thread with escalation criterion>

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

Expected output:
- Write the handoff in the workflow language
- Prototype/demo artifact
- How to view or run it
- What it validates
- What it does not validate
- Verification performed
- Risks and assumptions
- Suggested updates to requirements, solution, or acceptance criteria

Stop and report if the prototype would require scope expansion or contradicts confirmed documents.
```

## Execution Delegate Prompt

```text
You are a bounded execution delegate in the Orchestrated Delivery workflow.

Workflow language:
<user's current language unless explicitly overridden>

Current phase: Phase 6, Execution, Verification, Review.

Delegate type and role:
<execution thread, worker subagent for simple non-review-gated work, or lead-owned task>

Review-gated:
<yes/no. If yes, this must be an execution thread unless the lead agent owns the work directly>

User goal:
<goal summary>

Source-of-truth context:
- Requirements: <summary or path>
- Selected solution: <summary or path>
- Acceptance criteria: <summary or path>
- Execution plan: <summary or path>
- Requirement and acceptance IDs covered by this task: <IDs>

Your task:
<specific execution path>

Scope:
<allowed work>

Non-scope:
<excluded work>

Ownership / writable boundaries:
<files, modules, or artifacts owned by this delegate>

Verification requirements:
<tests, checks, walkthroughs, fact checks, or other validation>

Review requirement:
Your output must be reviewed by the appropriate review subagent before final integration. If this is a review-gated execution thread, obtain reviewer subagent review before handoff unless blocked. If this is a simple worker subagent task, provide enough context for the lead agent to run review after handoff.

Expected handoff:
- Write the handoff in the workflow language
- Completed work
- Files or artifacts changed
- Verification performed and results
- Pre-commit verification performed, if a commit was created or requested
- Review subagent summary, if review happened inside this delegate
- Findings fixed
- Findings accepted as risk, with rationale
- Open risks or blockers
- Suggested source-of-truth document updates
- Integration notes for the lead agent

Stop and report if you need to change requirements, solution, acceptance criteria, scope, writable boundaries, or destructive operations.
```

## Thread Escalation Checklist

Use a thread when at least one applies:

- The execution lane must call reviewer subagents before handoff.
- Independent worktree execution is needed.
- Persistent context across many turns is needed.
- Long-running multi-turn work should be tracked separately.
- The user should be able to inspect a separated work track.
- The work involves a stateful prototype or environment.
- Risk isolation is useful.
- A single subagent handoff would be too shallow or unreliable.

Record the selected criterion in the phase document or `06-execution-log.md`.

## Worker Handoff Checklist

```text
Completed work:

Changed files or artifacts:

Verification:

Pre-commit verification, if applicable:

Review subagent summary:

Review findings fixed:

Accepted risks:

Open risks or blockers:

Suggested document updates:

Integration notes:
```

## Review Subagent Context Checklist

Provide the review subagent:

- Workflow language.
- User goal.
- Requirements.
- Selected solution.
- Acceptance criteria.
- Execution plan scope.
- Actual deliverable, diff, or artifact summary.
- Verification already run.
- Known risks.
- Review scope and non-scope.

Use the review subagent's own system prompt for review behavior and output expectations.

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
