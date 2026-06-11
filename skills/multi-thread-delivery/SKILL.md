---
name: multi-thread-delivery
description: Use when the user explicitly wants a documented multi-thread workflow for a complex goal, including requirement alignment, researched solution options, acceptance criteria, optional prototype, execution planning, worker threads, verification, sub-agent review, and delivery reporting. Do not use for simple tasks unless explicitly requested.
---

# Multi-Thread Delivery

Use this skill only after the user explicitly asks for, or approves, this workflow. That approval is workflow-level authorization to create Codex threads in the phases where this workflow allows them.

## Required Start

1. Read `references/workflow-definition.md` before running the workflow.
2. Read `references/templates.md` when drafting phase documents, thread prompts, worker handoffs, or gate prompts.
3. Confirm the current workflow mode: Full, Standard, Lite, Exit, or Split.
4. Establish the workflow document directory before Phase 1. Default to `docs/agent-workflows/<goal-slug>/` unless the user specifies another location.
5. Do not create files, threads, or implementation work until the active phase gate allows it.

## Non-Negotiable Rules

- The lead agent remains accountable for synthesis, decisions, user alignment, document consistency, and final delivery.
- Do not use threads in Phase 1, Phase 3, or Phase 5.
- Use at least one research/design thread in Phase 2.
- Use worker threads in Phase 6.
- Phase 4 is optional; use a prototype thread only when the user wants a prototype or it materially reduces risk.
- Phase 6 worker threads must use relevant skills and must call the predefined reviewer sub-agent before handoff.
- Source-of-truth documents must stay aligned with the real work. If an upstream document is wrong, return to the affected phase and re-run the needed gate.
- Every phase must actively check and maintain upstream source-of-truth documents, not only produce its own artifact.
- User gates require explicit user confirmation. Do not treat silence or lack of objection as approval.

## Phase Summary

- Phase 0: Activation and workflow-level thread authorization.
- Phase 1: Problem, goal, requirements, constraints, and non-goals. No threads.
- Phase 2: Research and solution design with at least two options. Use research/design threads.
- Phase 3: Acceptance criteria. No threads.
- Phase 4: Optional demo or prototype. Use a prototype thread when needed.
- Phase 5: Execution path plan. No threads.
- Phase 6: Execution, verification, worker-thread review, and integration.
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

Thread and review briefs do not need to be written as separate files by default. Keep brief content in the thread or sub-agent context, and record thread registry, verification, review, and risk summaries in `06-execution-log.md`.

## Thread Brief Rules

Every thread prompt must be self-contained and include the current phase, user goal, source-of-truth context, task scope, non-scope, readable context, writable boundaries, expected output, verification requirements, skill usage requirements, stopping conditions, and handoff format.

Every thread must identify and use the minimal relevant set of available skills. In its handoff, it must report which skills it used, which obvious skills it skipped and why, and whether any skill instruction conflicted with the workflow brief.

## Completion Rule

Do not claim completion until the delivery report maps the final result to acceptance criteria, required verification has run or residual risk is explicit, reviewer sub-agent findings have been handled, documents match the delivered state, and the user has a clear acceptance path.
