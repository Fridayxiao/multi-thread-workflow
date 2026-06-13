---
name: orchestrated-delivery
description: Use when the user explicitly wants a documented orchestrated workflow for a complex goal, including requirement alignment, researched solution options, acceptance criteria, optional prototype, execution planning, subagent-led research/advisory work, thread-first review-gated execution, verification, review, and delivery reporting. Do not use for simple tasks unless explicitly requested.
---

# Orchestrated Delivery

Use this skill only after the user explicitly asks for, or approves, this workflow. That approval is workflow-level authorization to use subagents for research/advisory/review work and Codex threads for review-gated execution lanes or other thread escalation criteria.

## Required Start

1. Read `references/workflow-definition.md` before running the workflow.
2. Read `references/templates.md` when drafting phase documents, delegate prompts, thread prompts, handoffs, review context, or gate prompts.
3. Confirm the current workflow mode: Full, Standard, Lite, Exit, or Split.
4. Determine the workflow language. Default to the language the user is currently using unless the user explicitly requests another language.
5. Establish the workflow document directory before Phase 1. Default to `docs/agent-workflows/<goal-slug>/` unless the user specifies another location.
6. Do not create implementation deliverables, threads, or execution work until the active phase gate allows them. Phase documents may be drafted or updated during their own phase after workflow activation, subject to the user's file-edit permissions.

## Non-Negotiable Rules

- The lead agent remains accountable for user alignment, synthesis, decisions, document consistency, and final delivery.
- Subagents are the default delegation primitive for research, design checks, advisory validation, and review.
- Threads are escalation tools for persistence, independent worktrees, long-running multi-turn execution, user-visible separated tracks, or risk isolation.
- Threads are mandatory for non-trivial execution lanes that must obtain review subagent feedback before handoff, because ordinary subagents cannot spawn reviewer subagents.
- Do not use threads in Phase 1, Phase 3, or Phase 5.
- Phase 1 is lead-owned and must not be delegated.
- Phase 2 requires at least one independent research/design delegate in Standard and Full modes.
- Phase 6 requires thread-first execution for non-trivial review-gated work unless the lead agent can safely complete the work directly and run review itself.
- Review must be performed by appropriate review subagent roles. Review-gated execution threads must obtain reviewer subagent review before handoff unless blocked, and blockers must be reported.
- Source-of-truth documents must stay aligned with the real work. If an upstream document is wrong, return to the affected phase and re-run the needed gate.
- Every phase must actively check and maintain upstream source-of-truth documents, not only produce its own artifact.
- Use the workflow language for phase communication, documents, delegate prompts, handoffs, reports, and gate requests unless the user explicitly asks otherwise.
- User gates require explicit user confirmation. Do not treat silence or lack of objection as approval.

## Phase Summary

- Phase 0: Activation and delegation/thread escalation authorization.
- Phase 1: User-perspective problem, current and desired state, actors, scenarios, scope, traceable requirements, constraints, assumptions, terms, risks, and non-goals. Lead-owned; no delegation.
- Phase 2: Research and solution design with at least two options. Default to research/design subagents; escalate to threads only when justified.
- Phase 3: Acceptance criteria. Lead-owned; optional advisory subagent check; no threads.
- Phase 4: Optional demo or prototype. Default to lead work or subagent delegation; escalate to a thread when persistence or an independent worktree is useful.
- Phase 5: Execution path plan. Lead-owned; optional advisory subagent check; no threads.
- Phase 6: Execution, verification, review, and integration. Use thread-first lanes for non-trivial review-gated execution; use subagents for review, advisory checks, and simple bounded work that does not need nested review.
- Phase 7: Delivery report and user acceptance.

## Required Documents

Create and maintain these source-of-truth documents for Standard and Full workflows:

- `01-problem-goal-requirements.md`
- `02-solution-options.md`
- `03-acceptance-criteria.md`
- `05-execution-paths.md`
- `06-execution-log.md`
- `07-delivery-report.md`

Optional documents:

- `04-prototype-notes.md`
- `00-workflow-state.md` for especially complex workflows

Default location: `docs/agent-workflows/<goal-slug>/`, unless the user specifies another location. In Lite Mode, documents may be combined, but every phase's required decisions, evidence, validation, and user confirmations must still be preserved in durable documentation.

Delegate, thread, and review briefs do not need to be written as separate files by default. Keep brief content in the delegate, thread, or subagent context, and record delegation registry, thread lanes, verification, review, and risk summaries in `06-execution-log.md`.

## Delegation Brief Rules

Every delegate prompt must be self-contained and include the workflow language, current phase, user goal, source-of-truth context, task scope, non-scope, readable context, writable boundaries if any, expected output, verification requirements, stopping conditions, and handoff format.

For subagents, choose the most specific available role that fits the task. For threads, state why the lane needs thread execution, including whether it is review-gated and must call reviewer subagents before handoff.

## Completion Rule

Do not claim completion until the delivery report maps the final result to acceptance criteria, required verification has run or residual risk is explicit, review findings have been handled, documents match the delivered state, and the user has a clear acceptance path.
