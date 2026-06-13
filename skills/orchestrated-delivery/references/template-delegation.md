# Delegation Brief Templates

Read this file before sending work to a thread, subagent, or reviewer.

A brief is the task message sent to another agent. It must be self-contained because that agent may not share the lead agent's context.

A handoff is the delegate's return report to the lead agent.

## Common Brief Fields

Include:

- Workflow language.
- Current phase.
- User goal.
- Confirmed source-of-truth context or paths.
- Task.
- Scope and non-scope.
- Context to read.
- Writable boundaries, if any.
- Expected output.
- Verification requirements.
- Stopping conditions.
- Handoff format.

## Research Or Design Brief

```text
Workflow language:

Current phase: Phase 2, Research and Solution Design.

User goal:

Confirmed requirements and constraints:

Your task:

Scope:

Non-scope:

Context to read:

Expected output:
- Investigation scope
- Existing or reusable solutions checked
- Evidence with citations or code references
- At least two options when applicable
- Benefits, costs, risks, and freshness checks
- Recommendation with rationale
- Unknowns or questions

Do not change requirements, acceptance criteria, or user-facing decisions. Stop and report if the brief conflicts with reality.
```

## Prototype Brief

```text
Workflow language:

Current phase: Phase 4, Demo or Prototype.

User goal and selected solution:

Acceptance criteria relevant to the prototype:

Your task:

Scope:

Non-scope:

Writable boundaries:

Expected output:
- Prototype or demo artifact
- How to view or run it
- What it validates
- What it does not validate
- Verification performed
- Risks and assumptions
- Suggested updates to requirements, solution, or acceptance criteria

Stop and report if the prototype would require scope expansion or contradicts confirmed documents.
```

## Execution Brief

```text
Workflow language:

Current phase: Phase 6, Execution, Verification, Review.

User goal:

Source-of-truth context:
- Requirements:
- Selected solution:
- Acceptance criteria:
- Execution path:

Your task:

Scope:

Non-scope:

Writable boundaries:

Verification requirements:

Review-gated: yes/no

If review-gated: explain why this is a thread or lead-owned task, not an ordinary subagent task.

Reviewer role:

Review timing: before handoff / after handoff / lead-owned review

Review requirements:

Expected handoff:
- Completed work
- Files or artifacts changed
- Verification performed and results
- Review summary, if review happened inside this delegate
- Findings fixed
- Accepted risks with rationale
- Open risks or blockers
- Suggested document updates
- Integration notes

Stop and report if you need to change requirements, solution, acceptance criteria, scope, writable boundaries, or destructive operations.
```

## Review Brief

```text
Workflow language:

Review role:

Review goal:

User goal:

Confirmed requirements:

Selected solution:

Acceptance criteria:

Execution plan scope:

Deliverable, diff, or artifact to review:

Verification already run:

Known risks:

Review scope:

Non-scope:

Expected output:
- Findings ordered by severity
- File or artifact references where applicable
- Missing tests or verification gaps
- Questions or assumptions
- Recommendation: pass, pass with risks, or block
```

## Handoff Checklist

```text
Completed work:

Changed files or artifacts:

Verification:

Review summary:

Findings fixed:

Accepted risks:

Open risks or blockers:

Suggested document updates:

Integration notes:
```
