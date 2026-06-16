---
name: orchestrated-delivery
description: Use when the user explicitly wants a documented orchestrated workflow for a complex goal with phased requirements, research, acceptance criteria, execution, review, and delivery. Do not use for simple tasks.
---

# Orchestrated Delivery

Use this skill only after the user explicitly asks for, or approves, a documented multi-phase workflow. The lead agent remains accountable for user alignment, decisions, synthesis, document consistency, and final delivery.

The workflow covers: requirement alignment, researched solution options, acceptance criteria, optional prototype, execution planning, delegated research and advisory work, thread-first review-gated execution, verification, review, and delivery reporting.

## Required Start

1. Read `references/workflow-core.md` before running the workflow.
2. Read `references/shared-hard-rules.md` and `references/artifacts.md` before Phase 1.
3. Confirm the mode: Full, Standard, Lite, Exit, or Split.
4. Determine the workflow language. Default to the language the user is currently using unless explicitly overridden.
5. Establish the workflow document directory before Phase 1. Default to `docs/agent-workflows/<goal-slug>/` unless the user specifies another location.
6. Run the activation, tool-capability, and resume checks in `references/workflow-core.md`.
7. Read the phase reference for the current phase before doing phase work.
8. Read only the template file needed for the artifact or prompt you are drafting. An artifact is a file produced by a workflow phase.
9. Do not create implementation deliverables, threads, or execution work until the active phase gate allows them.

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
- Artifact paths and completion checks: `references/artifacts.md`
- Shared hard rules and workflow terms: `references/shared-hard-rules.md`

## Non-Negotiable Rules

Follow `references/shared-hard-rules.md`. The short version: keep phases separate, require explicit user confirmation at gates, keep Phase 1/3/5 lead-owned, treat delegated output as advisory, use threads for non-trivial review-gated execution unless the lead owns and reviews the work directly, and keep confirmed source-of-truth documents aligned with delivered work.

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

Do not claim completion until `references/artifacts.md` completion checks pass, the delivery report maps the final result to acceptance criteria, required verification has run or residual risk is explicit, review findings have been handled, documents match the delivered state, and the user has a clear acceptance path. When the workflow documents are on disk, run the validator script if available (see `references/artifacts.md` for invocation) and report the result.
