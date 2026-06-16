# Orchestrated Delivery Core

Read this file at workflow start. Also read `shared-hard-rules.md` and `artifacts.md` before Phase 1. Read phase and template files only when needed.

## Purpose

Use this workflow for complex or high-risk goals where ordinary direct execution is likely to fail through misunderstood requirements, shallow research, execution drift, weak review, or unclear final acceptance.

The lead agent owns the workflow. It aligns with the user, writes and maintains source-of-truth documents, delegates bounded work when useful, checks outputs, keeps decisions consistent, and reports delivery.

## Modes

- Full: use all phases, including prototype when it reduces material risk or the user requests it.
- Standard: default for complex goals. Use Phases 1, 2, 3, 5, 6, and 7. Phase 4 is optional.
- Lite: use only when the user wants speed and risk is acceptable. Keep durable records, but documents may be combined and shorter.
- Exit: stop using this workflow when the task is too small or the user rejects documents, delegation, or explicit confirmations.
- Split: use when one request contains independent goals with different acceptance criteria or delivery paths.

## Start Checklist

1. Confirm the user explicitly wants or approves this workflow.
2. Confirm the workflow language. Use the user's current language unless they ask otherwise.
3. Establish the document directory. Default to `docs/agent-workflows/<goal-slug>/`.
4. Check available tools before relying on them: thread creation, subagents, reviewer roles, browser, shell, network, and file-write permissions.
5. If a needed tool is unavailable, choose a fallback before proceeding: lead-owned work, available subagent, user approval request, or recorded residual risk.
6. Check whether the document directory already exists and follow the resume protocol below.
7. Use `artifacts.md` for document path, required artifact, and completion rules.
8. Announce the current phase, next artifact, and next user confirmation point.

A gate is the check that must pass before moving to the next phase, including required user confirmation when listed.

## Goal Setup

Some runtimes support persistent goal tracking (e.g., Codex goals) -- a runtime objective that keeps long work from stopping before the required outcome is reached. If the runtime does not support persistent goals, skip this section.

Do not create or adopt a persistent goal during Phase 1, Phase 2, or Phase 3, because the problem, solution, and acceptance criteria are still being corrected.

Goal setup is allowed only when all of these are true:

1. Phase 3 has been explicitly confirmed by the user.
2. The user explicitly agrees to create or adopt a persistent goal.
3. The goal text is based on confirmed source-of-truth documents, not only the original request.
4. If Phase 4 is used and may change requirements, solution, or acceptance criteria, Phase 4 has passed its gate first.

Shape the objective like:

`Run the Orchestrated Delivery workflow for the confirmed <goal>; do not stop until required phase artifacts exist, required gates are recorded, execution is verified and reviewed, and the final delivery report gives user acceptance steps.`

Do not mark the goal complete until the completion checks in `artifacts.md` pass. If goal tools are unavailable after the user asks for goal setup, record that limitation and continue without creating a goal.

## Resume Protocol

If the workflow directory already exists:

1. Read `00-workflow-state.md` if present.
2. If no state file exists, read the latest available phase document and `06-execution-log.md` if present.
3. Decide whether to continue, restart, or split:
   - Continue when the existing documents still match the user's goal.
   - Restart when the prior documents are stale or conflict with the current goal.
   - Split when the current goal contains independent tracks.
4. Tell the user what you found and ask for confirmation when the decision changes scope, discards prior decisions, or resumes from a risky point.

## Phase Map

| Phase | Purpose | Reference | Artifact | User confirmation |
| --- | --- | --- | --- | --- |
| 1 | Align problem, goal, scope, requirements, constraints, risks, and non-goals | `phase-1-requirements.md` | `01-problem-goal-requirements.md` | Required |
| 2 | Research current solutions and compare at least two options | `phase-2-solution.md` | `02-solution-options.md` | Required |
| 3 | Define what done means | `phase-3-acceptance.md` | `03-acceptance-criteria.md` | Required |
| 4 | Build an optional demo or prototype | `phase-4-prototype.md` | `04-prototype-notes.md` | Required when used |
| 5 | Plan execution paths, parallel work, verification, and rollback | `phase-5-execution-plan.md` | `05-execution-paths.md` | Required |
| 6 | Execute, verify, review, integrate, and update documents | `phase-6-execution-review.md` | `06-execution-log.md` | Pause if scope or risk changes |
| 7 | Report delivery and guide user acceptance | `phase-7-delivery.md` | `07-delivery-report.md` | Required |

In Lite or low-risk Standard mode, the user may confirm several phase results in one response, such as requirements, selected solution, acceptance criteria, and execution path. This reduces stops but does not remove explicit confirmation. Record exactly what the user confirmed.

## Document Rules

Use `artifacts.md` for artifact paths, required documents, source-of-truth rules, and completion checks.

Keep documents compact by default. Omit empty sections. Use bullets for small lists. Use tables only when comparison, traceability, or auditability is clearer.

## Context Management

This skill has many reference files. Do not load all of them at once. Follow the loading order in SKILL.md: read `workflow-core.md`, `shared-hard-rules.md`, and `artifacts.md` at start, then read only the current phase reference and the needed template section when drafting.

If context is constrained, prioritize: (1) `shared-hard-rules.md`, (2) the current phase reference, (3) `artifacts.md`. Template files can be re-read when drafting. Phase references for completed phases can be dropped from context.

## Delegation And Review

Terms: a delegate is a thread or subagent given a bounded task. A reviewer is a specialized subagent asked to check work against confirmed documents. Review-gated execution means work that cannot be handed off or integrated until the required reviewer has checked it.

The rules for delegation ownership, review-gated execution, and advisory treatment of delegated output are in `shared-hard-rules.md`. The operational guidance below supplements those rules:

- Use the most specific available delegate or reviewer role.
- Before delegating, provide a self-contained task brief with context, scope, non-scope, expected output, verification, and stopping conditions.
- Record delegation, review, verification, risks, and integration notes in `06-execution-log.md`.
- If thread or reviewer tools are unavailable, state the fallback and record residual risk.

## Completion Rule

Do not claim completion until the completion checks in `artifacts.md` pass.
