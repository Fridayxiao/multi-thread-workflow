# Orchestrated Delivery Core

Read this file at workflow start. Read phase and template files only when needed.

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
7. Announce the current phase, next artifact, and next user confirmation point.

A gate is the check that must pass before moving to the next phase, including required user confirmation when listed.

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

- Keep documents compact by default. Omit empty sections.
- Use bullets for small lists. Use tables only when comparison, traceability, or auditability is clearer.
- Store phase documents in the workflow document directory.
- Treat `01`, `02`, `03`, and `05` as source-of-truth documents once confirmed. Source-of-truth documents are the confirmed phase documents that later work must follow unless they are explicitly updated and reconfirmed.
- At the start and end of each phase, check whether earlier documents remain accurate. Earlier documents means documents from prior phases, especially `01`, `02`, `03`, and `05`.
- If a confirmed earlier document is wrong, update it and re-run the affected user confirmation before continuing.
- Delegates may suggest document updates, but the lead agent decides and applies source-of-truth changes.

## Delegation And Review

Here, a delegate means a thread or subagent given a bounded task. A reviewer means a specialized subagent asked to check work against the confirmed goal, requirements, solution, acceptance criteria, and execution path. Review-gated execution means work that cannot be handed off or integrated until the required reviewer has checked it.

- Do not delegate Phase 1, Phase 3, or Phase 5 ownership.
- Use the most specific available delegate or reviewer role.
- Standard and Full mode require at least one independent research or design delegate in Phase 2.
- Non-trivial review-gated execution lanes must use a thread unless the lead agent owns the work directly and runs review itself.
- Do not assign review-gated execution to an ordinary subagent, because ordinary subagents cannot call reviewer subagents before handoff.
- Before delegating, provide a self-contained task brief with context, scope, non-scope, expected output, verification, and stopping conditions.
- Treat delegated output as advisory until the lead agent checks it.
- Record delegation, review, verification, risks, and integration notes in `06-execution-log.md`.
- If thread or reviewer tools are unavailable, state the fallback and record residual risk. Residual risk means a known remaining risk after verification, fallback, or review.

## Completion Rule

Do not claim completion until:

- `07-delivery-report.md` maps delivered work to acceptance criteria.
- Required verification has run, or residual risk is explicit.
- Review findings have been fixed or consciously accepted as risk.
- Source-of-truth documents match the delivered state.
- The user has clear acceptance steps.
