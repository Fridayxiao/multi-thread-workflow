---
name: orchestrated-delivery
description: Use when the user explicitly wants a documented orchestrated workflow for a complex goal, including requirement alignment, researched solution options, acceptance criteria, optional prototype, execution planning, delegated research/advisory work, thread-first review-gated execution, verification, review, and delivery reporting. Do not use for simple tasks unless explicitly requested.
---

# Orchestrated Delivery

Use this skill only after the user explicitly asks for, or approves, a documented multi-phase workflow. The lead agent remains accountable for user alignment, decisions, synthesis, document consistency, and final delivery.

## Required Start

1. Read `references/workflow-core.md` before running the workflow.
2. Confirm the mode: Full, Standard, Lite, Exit, or Split.
3. Determine the workflow language. Default to the language the user is currently using unless explicitly overridden.
4. Establish the workflow document directory before Phase 1. Default to `docs/agent-workflows/<goal-slug>/` unless the user specifies another location.
5. Run the activation, tool-capability, and resume checks in `references/workflow-core.md`.
6. Read the phase reference for the current phase before doing phase work.
7. Read only the template file needed for the artifact or prompt you are drafting.
8. Do not create implementation deliverables, threads, or execution work until the active phase gate allows them.

## Phase References

- Phase 1 requirements alignment: `references/phase-1-requirements.md`
- Phase 2 research and solution design: `references/phase-2-solution.md`
- Phase 3 acceptance criteria: `references/phase-3-acceptance.md`
- Phase 4 optional prototype: `references/phase-4-prototype.md`
- Phase 5 execution paths: `references/phase-5-execution-plan.md`
- Phase 6 execution, verification, and review: `references/phase-6-execution-review.md`
- Phase 7 delivery and user acceptance: `references/phase-7-delivery.md`

## Template References

- Phase documents: `references/template-documents.md`
- Delegate, thread, review, and handoff prompts: `references/template-delegation.md`
- User gates and confirmation records: `references/template-gates.md`

## Non-Negotiable Rules

- User gates require explicit confirmation. Do not treat silence or lack of objection as approval.
- Phase 1, Phase 3, and Phase 5 are lead-owned. Do not use threads in those phases.
- The lead agent must not outsource user alignment, final synthesis, source-of-truth decisions, or acceptance decisions.
- Source-of-truth documents must stay aligned with real work. If an earlier phase document is wrong, return to the affected phase and re-run the needed gate.
- Delegates and threads are advisory or bounded execution units. Their outputs are not verified truth until the lead agent evaluates them.
- Non-trivial review-gated execution lanes must use a thread unless the lead agent owns the work directly and runs review itself. Do not assign review-gated execution to an ordinary subagent, because ordinary subagents cannot call reviewer subagents before handoff.
- Use the workflow language for phase communication, documents, delegate prompts, handoffs, reports, and gate requests unless the user explicitly asks otherwise.

## Required Documents

- `01-problem-goal-requirements.md`
- `02-solution-options.md`
- `03-acceptance-criteria.md`
- `05-execution-paths.md`
- `06-execution-log.md`
- `07-delivery-report.md`

Optional:

- `04-prototype-notes.md`
- `00-workflow-state.md` for complex or resumed workflows

Use compact documents by default. Preserve decisions, evidence, validation, and user confirmations, but omit empty sections and avoid large tables when bullets are clearer.

## Completion Rule

Do not claim completion until the delivery report maps the final result to acceptance criteria, required verification has run or residual risk is explicit, review findings have been handled, documents match the delivered state, and the user has a clear acceptance path.
