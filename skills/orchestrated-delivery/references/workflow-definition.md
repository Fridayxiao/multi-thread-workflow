# Orchestrated Delivery Workflow Definition

Version: 0.3.1

## Purpose

This workflow is for complex or high-risk user goals. It reduces four delivery risks: misunderstood requirements, outdated or shallow solution design, execution drift, and vague final acceptance.

The lead agent aligns the goal and success criteria with the user, uses subagents for research, design checks, advisory validation, and review, uses Codex threads for review-gated execution lanes, maintains phase documents, synthesizes all delegated outputs, and remains accountable for final delivery.

Threads are not the point of the workflow, but they are the right execution container when the worker must call reviewer subagents before handoff. Ordinary subagents cannot spawn reviewer subagents. Threads also preserve the original thread-based capabilities: independent worktrees, long-running multi-turn work, persistent context, user-visible separated tracks, and risk isolation.

## Applicability

Use this workflow when:

- The user explicitly asks for or approves this workflow.
- The goal is complex, multi-stage, high-risk, or likely to benefit from research, parallel work, prototype validation, independent review, or documented gates.
- The work involves multiple modules, domains, systems, stakeholders, or material tradeoffs.
- Failure would be costly enough to justify documents, gates, delegation, and verification.

Do not use this workflow when:

- The task is a simple answer, explanation, translation, formatting change, or small low-risk edit.
- The user asks for fast direct execution and does not want the workflow.
- The user does not allow delegation, documents, or confirmation gates.
- The goal is too broad for one workflow and should be split first.

## Roles

### User

The user is the source of goals, requirements, constraints, solution choice, acceptance criteria, and final acceptance. The user must explicitly confirm key gates.

### Lead Agent

The lead agent owns the workflow. It clarifies the goal, maintains documents, delegates bounded tasks, decides when thread escalation is justified, synthesizes outputs, resolves conflicts, updates source-of-truth documents, asks for user confirmation, and decides whether to proceed, stop, or roll back.

The lead agent must not outsource user alignment, final synthesis, source-of-truth decisions, or acceptance decisions to delegates.

### Subagent Delegate

A subagent delegate is the default bounded work unit for research, design review, advisory validation, simple bounded work that does not require nested review, documentation, and specialist checks. Use the most specific available role for the task, such as `docs-researcher`, `explorer`, `architect`, `product-designer`, `worker`, `code-reviewer`, `test-engineer`, `security-auditor`, or `docs-maintainer`.

Subagents should receive self-contained briefs and return structured handoffs. Their outputs are advisory until evaluated by the lead agent.

### Thread Delegate

A thread delegate is the default container for non-trivial review-gated execution and an escalation unit for work that needs persistence, an independent worktree, long-running multi-turn work, a user-visible separated track, risk isolation, or a stateful prototype.

Thread delegates must still follow bounded briefs. A review-gated execution thread must obtain reviewer subagent review before handoff unless blocked; if blocked, it must report the blocker instead of pretending review happened.

### Reviewer Subagent

Reviewer subagents are predefined outside this workflow. This workflow controls when to call them, what context to provide, and how to handle output. Their own system prompts control review behavior. Findings are advisory until evaluated by the lead agent or responsible worker.

## Modes

### Full Mode

Use Full Mode for high-risk, high-complexity, multi-stakeholder, or explicitly complete workflows.

Requirements:

- Execute Phase 0 through Phase 7.
- Use independent research/design delegation in Phase 2.
- Use Phase 4 when prototype validation reduces material risk or the user requests it.
- Use thread-first review-gated execution and review in Phase 6.
- Escalate to threads only when thread escalation criteria are met.
- Maintain complete source-of-truth documents.
- Keep explicit user gates.
- Produce a final delivery report.

### Standard Mode

Standard Mode is the default for complex goals.

Requirements:

- Execute Phase 1, Phase 2, Phase 3, Phase 5, Phase 6, and Phase 7.
- Phase 4 is optional.
- Documents may be concise but must exist.
- Use at least one research/design delegate in Phase 2.
- Use thread-first review-gated execution in Phase 6 when work is non-trivial.
- Require appropriate review subagents.
- Do not skip user gates.

### Lite Mode

Use Lite Mode only when the user wants speed and the risk is acceptable.

Requirements:

- Phase 1, Phase 3, and Phase 5 may be concise or combined, but goal, acceptance, and execution path must remain explicit.
- Phase 2 may use one research/design delegate, but should still compare at least two options unless the user explicitly wants one direction.
- Phase 6 still requires verification and review. Review-gated execution must use a thread unless the lead agent performs the work directly and runs review itself.
- Durable documentation is still required. A combined Lite document is acceptable, but it must preserve every phase's required decisions, evidence, validation, and user confirmations.
- Explain the risks of compression.
- Do not use Lite Mode for high-risk work.

### Exit or Split

Exit the workflow when the task is too small, the user will not allow essential gates, or the cost exceeds the benefit.

Split the workflow when the goal contains independent sub-goals with different acceptance criteria, owners, prototypes, or delivery paths. First align the parent goal, child workflows, ordering, shared constraints, dependencies, and the first child workflow to run.

## Language Policy

Default all workflow communication to the language the user is currently using, unless the user explicitly requests another language.

This applies to phase conversations, gate prompts, documents, delegate prompts, worker handoffs, reviewer or specialist context, delivery reports, and user acceptance instructions.

Keep stable technical identifiers unchanged, including file names, code symbols, command names, paths, API names, log excerpts, and quoted source text. Section headings in templates may be translated to the workflow language while keeping the same required meaning.

If the user uses multiple languages, infer the working language from the current request and surrounding context. Ask only when ambiguity would materially affect the deliverable.

## Phase 0: Activation

Goal: decide whether to use the workflow and establish authorization for subagent delegation, review-gated execution threads, and thread escalation.

Delegation: no work delegation yet.

Gate:

- The user explicitly asks for or approves the workflow.
- The user understands the workflow may use subagents, may use threads for review-gated execution or other escalation criteria, produce documents, and wait at key gates.
- The workflow language is determined.
- The workflow document directory is established. Default to `docs/agent-workflows/<goal-slug>/` unless the user specifies another location.
- The lead agent judges the task suitable.

If the task is too small or the user rejects delegation/documents/gates, exit the workflow.

## Phase 1: Problem, Goal, Requirements Alignment

Goal: define the problem from the user's perspective, the target outcome, actors, scenarios, scope, requirements, constraints, assumptions, open questions, non-goals, terms, and risks at enough depth that later phases can trace decisions back to stable requirements.

Delegation: none. This phase is lead-owned because user alignment must remain direct.

Artifact: `01-problem-goal-requirements.md`.

Approach:

- First synthesize a draft from the existing conversation and available project context. Do not start with a broad interview when the answer can be inferred or researched.
- For codebase work, inspect applicable project guidance and domain documents before finalizing terminology, including `AGENTS.md`, `CONTEXT.md`, `CONTEXT-MAP.md`, relevant `docs/adr/`, and nearby code or tests when they clarify current behavior.
- Use the project's existing domain language. If the user's terms conflict with a glossary or code reality, call out the conflict and resolve the canonical term before proceeding.
- Stress-test fuzzy requirements with concrete scenarios, including the primary path, edge cases, permission or data boundaries, integration boundaries, failure modes, and unacceptable outcomes.
- Ask targeted clarification questions only for blocking gaps. Ask one decision at a time, provide a recommended answer, and wait for feedback before moving to the next blocking decision.
- Convert resolved decisions into traceable entries: requirements (`R-*`), constraints (`C-*`), assumptions (`A-*`), open questions (`Q-*`), risks (`K-*`), terms (`T-*`), or non-goals (`N-*`).

Documentation sync:

- If a domain term is resolved and the project uses `CONTEXT.md` or `CONTEXT-MAP.md`, update the appropriate glossary when file edits are allowed. `CONTEXT.md` is only for domain language, not implementation decisions.
- Offer or create an ADR only when the decision is hard to reverse, surprising without context, and the result of a real tradeoff. Do not create ADRs for obvious or easily reversible choices.
- If file edits are not yet allowed, record required glossary or ADR updates in `01-problem-goal-requirements.md` so they are not lost.

Depth requirements:

- The problem statement must be from the user's perspective, not only a technical task summary.
- The current state and desired state must be explicit.
- Core actors, stakeholders, user stories, and scenarios must be identified where applicable.
- Scope must be explicit through in-scope items, out-of-scope items, and non-goals.
- Every core requirement must have an ID, type, priority, source or owner, rationale, and acceptance hint or validation surface.
- Constraints must distinguish hard constraints from preferences.
- Assumptions must include confidence and a validation path.
- Open questions must identify whether they block Phase 2, Phase 3, Phase 5, or Phase 6.
- Must-have requirements may not rely on unresolved blocking questions.

Gate:

- The document or equivalent draft clearly states the user-perspective problem, goal, current state, desired state, scope, requirements, constraints, assumptions, open questions, non-goals, terms, risks, and user confirmation record.
- Core terminology is aligned with project language or unresolved conflicts are explicitly recorded.
- The primary scenarios and important edge cases are covered at the level needed for solution design.
- Every must-have requirement has an ID, priority, rationale, source or owner, and acceptance hint or validation surface.
- No unresolved blocking question prevents Phase 2 research or makes the selected goal unstable.
- The user explicitly confirms it.
- Downstream phases are instructed to reference Phase 1 IDs when comparing options, writing acceptance criteria, planning execution paths, executing work, and reporting delivery.

Rollback:

- If the user disagrees, continue clarifying in Phase 1.
- If the goal splits into independent goals, split the workflow.
- If later phases expose vague or unstable requirements, return to Phase 1 and update the document before continuing.

## Phase 2: Research and Solution Design

Goal: research existing and current solutions, verify relevant APIs or practices, and present at least two viable solution options with tradeoffs.

Delegation: default to research/design subagents. Escalate to a thread only when the research/design work needs persistent context, long-running multi-turn investigation, an independent worktree, or a user-visible separated track.

Typical subagent roles:

- `docs-researcher` for official docs, API signatures, version differences, deprecation risks, and migration paths.
- `explorer` for specific codebase questions.
- `architect` for architecture boundaries, interfaces, migration paths, and scalability tradeoffs.
- `product-designer` for product scope, UX flows, and user-facing acceptance tradeoffs.

Artifact: `02-solution-options.md`.

Research requirements:

- Actively investigate usable or adaptable existing solutions before proposing custom work.
- Verify current status for information that may be stale, including APIs, dependencies, standards, regulations, market facts, and product behavior.
- If no suitable existing solution is found, collect enough task and system context to justify a custom design.
- The lead agent must interact with delegates until their output is strong enough to support at least two options and a defensible recommendation.
- `02-solution-options.md` must record what existing solutions were investigated and why they were adopted or rejected.
- Each option must map its fit, gaps, and tradeoffs to relevant Phase 1 requirement, constraint, assumption, and risk IDs.

Gate:

- At least one independent research/design delegate has completed in Standard and Full modes.
- At least two options are compared.
- Key assumptions, deprecation risks, and freshness risks are checked or explicitly recorded.
- Options are evaluated against Phase 1 IDs, not only a loose goal summary.
- The lead agent recommends a default with rationale.
- The user selects one option or approves a combination.

Rollback:

- If research is insufficient, continue Phase 2.
- If no option satisfies Phase 1, return to Phase 1.
- If the user introduces a new goal, update Phase 1.

## Phase 3: Acceptance Criteria

Goal: define what "done" means before execution begins.

Delegation: lead-owned. Optional advisory subagent checks may be used after the lead drafts criteria, but no thread may be used and no delegate may replace user confirmation.

Typical advisory roles:

- `product-designer` for user-visible acceptance and flow coverage.
- `test-engineer` for testability and validation strategy.

Artifact: `03-acceptance-criteria.md`.

Gate:

- Each core requirement maps to at least one acceptance criterion.
- Each criterion has a validation method or an explicit substitute judgment method.
- Unacceptable outcomes are stated.
- Requirement IDs from Phase 1 are preserved so later execution can trace delivered work to confirmed requirements.
- The user explicitly confirms the criteria.

Rollback:

- If criteria fail to cover requirements, continue Phase 3 or return to Phase 1.
- If criteria conflict with the selected solution, return to Phase 2.

## Phase 4: Demo or Prototype

Goal: create something the user can see, try, review, or reason about before full execution.

Delegation: optional. Default to direct lead work or subagent delegation. Escalate to a thread only when the prototype needs an independent worktree, persistent state, long-running multi-turn iteration, user-visible separated tracking, or risk isolation.

Typical roles:

- `product-designer` for flows, UX sketches, and prototype scope.
- `worker` for bounded implementation prototypes.
- `test-engineer` for prototype validation strategy.

Artifact: `04-prototype-notes.md` is optional. Updates to `01`, `02`, and `03` are required when prototype feedback changes them.

Entry:

- The user requests a prototype, or the lead agent recommends one because it materially reduces risk and the user agrees.

Gate:

- The prototype or demo is observable by the user.
- Feedback is collected.
- The impact on requirements, solution, and acceptance criteria is handled.

Rollback:

- If the prototype changes requirements, return to Phase 1.
- If it changes the solution, return to Phase 2.
- If it changes done criteria, return to Phase 3.

## Phase 5: Execution Path Plan

Goal: plan how to execute before doing the work. Identify serial dependencies, parallel paths, delegate ownership, review-gated thread lanes, other thread escalation candidates, integration strategy, validation strategy, risks, and rollback points.

Delegation: lead-owned. Optional advisory subagent checks may be used, but no thread may be used and no delegate may replace the plan or user confirmation.

Typical advisory roles:

- `architect` for sequencing, boundaries, interfaces, and migration risk.
- `test-engineer` for validation and TDD strategy.
- `security-auditor` for security-sensitive plans.

Artifact: `05-execution-paths.md`.

Gate:

- The execution path is clear.
- Parallel and serial work are separated.
- Each delegate path has a target, role, scope, inputs, outputs, validation method, stopping conditions, ownership boundaries, and review-gated status.
- Each path identifies the Phase 1 requirement IDs and Phase 3 acceptance criteria it covers.
- Thread escalation candidates are justified by explicit criteria.
- Integration and rollback are defined.
- The user explicitly confirms the plan.

Rollback:

- If planning exposes solution problems, return to Phase 2.
- If planning exposes acceptance problems, return to Phase 3.

## Phase 6: Execution, Verification, Review

Goal: execute the plan, verify results, run appropriate review subagents, integrate outputs, and update documents.

Delegation: non-trivial review-gated execution is thread-first. Use `worker` subagents only for simple bounded work that does not need to call reviewer subagents before handoff, or when the lead agent will run review after the subagent returns. Escalate any execution path to a thread when subagent delegation is insufficient because pre-handoff reviewer subagent review, persistence, independent worktree execution, long-running multi-turn work, user-visible separated tracking, or risk isolation is needed.

Artifact: `06-execution-log.md`.

Requirements:

- Each execution delegate follows its brief and ownership boundary.
- Each execution delegate verifies its own scope.
- Each execution delegate reports changed files or artifacts, verification, risks, and suggested document updates.
- Each output is reviewed by the appropriate review subagent role before final integration.
- Each non-trivial review-gated execution lane runs in a thread.
- Each review-gated execution thread must obtain reviewer subagent review before handoff unless blocked; blocked review must be reported as a blocker or residual risk.
- If a simple worker subagent is used for execution, the lead agent must run the appropriate review subagent after handoff before final integration.
- The lead agent checks each handoff, integrates work, resolves conflicts, and performs workflow-level verification.
- Affected source-of-truth documents are updated.

Typical roles:

- `worker` for simple bounded implementation or execution that does not require nested review before handoff.
- `code-reviewer` for code review.
- `test-engineer` for test coverage, failure analysis, and validation strategy.
- `security-auditor` for security-sensitive changes.
- `docs-maintainer` for documentation updates after implementation or review findings.

Gate:

- All delegated execution paths and review-gated thread lanes are complete or explicitly canceled.
- Required verification has run or residual risk is explicit.
- Review subagent findings are handled.
- The execution log includes delegation registry, review-gated thread lanes, verification evidence, review summaries, integration notes, and unresolved risks.
- Delivered work still matches `01`, `02`, `03`, and `05`.

Rollback:

- If execution drifts from requirements, return to Phase 1 or Phase 5.
- If execution exposes solution flaws, return to Phase 2.
- If criteria are incomplete, return to Phase 3.
- If integration fails, return to Phase 5.

## Phase 7: Delivery Report and User Acceptance

Goal: report the final state and give the user a clear acceptance path.

Delegation: usually none. A final specialist or reviewer subagent check may be used when needed, but the lead agent must synthesize it.

Artifact: `07-delivery-report.md`.

Gate:

- The report maps results to acceptance criteria.
- Verification evidence is clear.
- Known limitations and risks are explicit.
- User acceptance steps are clear.
- The user accepts or provides rework feedback.

Rollback:

- Execution issue: return to Phase 6.
- Planning issue: return to Phase 5.
- Solution, requirement, or acceptance issue: return to Phase 1, 2, or 3.
- Enhancement requests after acceptance become a new task or workflow.

## Document System

Required source-of-truth documents:

- `01-problem-goal-requirements.md`
- `02-solution-options.md`
- `03-acceptance-criteria.md`
- `05-execution-paths.md`
- `06-execution-log.md`
- `07-delivery-report.md`

Default directory: `docs/agent-workflows/<goal-slug>/`, where `<goal-slug>` is a short, stable, kebab-case label for the goal. Use another location only when the user specifies one or project conventions clearly require it.

Optional:

- `04-prototype-notes.md`
- `00-workflow-state.md` for complex state tracking

Delegate, thread, and review briefs are not required as separate files. Their content may live in the subagent, thread, or review context. `06-execution-log.md` must preserve enough registry, status, verification, review, and risk information to audit the workflow.

Only the lead agent updates source-of-truth conclusions. Delegates may recommend updates but must not change requirements, solution decisions, or acceptance criteria on their own.

## Document Maintenance Duty

Every phase must maintain upstream documents, not only create its own artifact.

- At the start of each phase, the lead agent checks whether upstream source-of-truth documents are still accurate, complete, and current enough to continue.
- At the end of each phase, the lead agent records whether the phase affected upstream documents.
- If a phase reveals that an upstream document is wrong or incomplete, update the affected document and re-run any required user gate before continuing.
- Delegates must report suggested source-of-truth updates in their handoff instead of changing user-confirmed decisions on their own.
- Phase 6 must explicitly check whether execution changed or invalidated `01`, `02`, `03`, or `05`.
- Before Phase 7 delivery, the lead agent must perform a final consistency check across source-of-truth documents and the actual delivered result.

## Delegation Protocol

Subagents are the default delegation primitive for research, advisory checks, specialist review, and simple bounded work. Threads are mandatory for review-gated execution lanes and are escalation tools elsewhere.

Before delegating, the lead agent must state in the main workflow:

- Why delegation is needed.
- Which delegate type and role will be used.
- The task boundary.
- What the delegate may read or write.
- Expected output.
- How the result will return to the workflow.

Every delegation brief must be self-contained and include:

- Workflow language.
- Current workflow phase.
- User goal and success criteria summary.
- Relevant source-of-truth document summaries or paths.
- Delegate role and type.
- Specific task.
- Scope and non-scope.
- Readable context.
- Writable boundaries, if any.
- Expected output format.
- Verification requirements.
- Whether the task is review-gated.
- Stopping conditions.
- Handoff requirements.

Delegates must stop and report when the brief conflicts with reality, scope needs to expand, upstream documents appear wrong, validation cannot run, dependencies are missing, or the next action would be destructive or high risk.

## Thread Escalation Criteria

Use a thread when one or more criteria is met:

- The execution lane must call reviewer subagents before handoff.
- Independent worktree execution is needed.
- The task requires persistent context across many turns.
- The task is long-running and benefits from an independently trackable lane.
- The user should be able to inspect a separated work track.
- The work involves a stateful prototype or environment.
- Risk isolation is useful.
- A single subagent handoff would be too shallow or unreliable.

When using or escalating to a thread, the lead agent must record the criterion in `06-execution-log.md` or the current phase document.

Threads remain prohibited in Phase 1, Phase 3, and Phase 5.

## Review Subagent Usage

Use the most relevant review subagent role for the risk:

- `code-reviewer` for code quality and plan conformance.
- `test-engineer` for testing strategy, coverage, and validation.
- `security-auditor` for security-sensitive work.
- `architect` for structural design concerns.
- `product-designer` for product and UX acceptance concerns.
- `docs-maintainer` for documentation gaps.

The workflow must provide or require enough review context:

- User goal.
- Requirements.
- Selected solution.
- Acceptance criteria.
- Execution plan scope.
- Actual deliverable or changes.
- Verification already run.
- Known risks.

Review subagents' own system prompts control review behavior. Ordinary subagents cannot spawn review subagents, so review for ordinary subagent outputs is run by the lead agent after handoff. Threads can call review subagents internally and must do so for review-gated execution lanes. The lead agent must treat findings as advisory, then fix, document accepted risk, or roll back to an earlier phase when needed.

## Execution Quality

All execution must trace back to requirements and acceptance criteria.

For code tasks, use TDD by default:

- Bugs: reproduce or write a failing test first.
- Features: define acceptance, unit, or integration tests before implementation where practical.
- Refactors: confirm coverage or add characterization tests when needed.
- Do not weaken tests just to pass.
- Execution delegates run scope-level tests.
- Execution delegates must run relevant verification before handoff.
- If a delegate creates a commit or asks the lead agent to commit its work, relevant tests and checks must run before that commit.
- The lead agent runs appropriate integration-level checks such as tests, lint, typecheck, build, or e2e according to the project.
- The lead agent must run appropriate verification after integrating delegate outputs and before any final commit or delivery.

For non-code tasks, use appropriate validation:

- Research: source citation, cross-checking, freshness checks.
- Writing: audience, structure, tone, and factual accuracy checks.
- Product/design: walkthroughs, user scenarios, edge states.
- Data/analysis: sample validation, calculation review, assumptions, sensitivity checks.
- Strategy/operations: constraints, feasibility, risks, dependencies.
- High-stakes domains: state professional boundaries and prefer authoritative sources.

If verification cannot run, state why, explain impact, and provide alternative checks.

## User Alignment

Explicit user confirmation is required for:

- Phase 0 activation.
- Phase 1 problem, goal, requirements, constraints, and non-goals.
- Phase 2 selected solution.
- Phase 3 acceptance criteria.
- Phase 4 prototype impact, when used.
- Phase 5 execution path.
- Phase 7 final acceptance or rework direction.

Pause and realign during Phase 6 if requirements, solution, acceptance criteria, scope, risk, permissions, budget, or assumptions materially change.

User confirmation must be explicit. Silence or lack of objection is not approval.

## State Management

The lead agent must know and communicate:

- Current phase.
- Current phase goal.
- Confirmed and unconfirmed documents.
- Blockers.
- Active and completed delegates.
- Rollbacks.
- Next gate.

For complex workflows, create `00-workflow-state.md`. Otherwise keep state in phase documents and `06-execution-log.md`.

Record rollbacks with the trigger, affected documents, target phase, gates to re-run, and which prior work remains valid.

## Hard Rules

- Do not delegate before the user activates the workflow.
- Use threads for review-gated execution lanes; do not use threads elsewhere unless a thread escalation criterion is met.
- Do not use threads in Phase 1, Phase 3, or Phase 5.
- Do not assign review-gated execution to an ordinary subagent, because ordinary subagents cannot call reviewer subagents before handoff.
- Do not let delegates replace user confirmation.
- Do not let delegates change source-of-truth decisions on their own.
- Do not continue from a source-of-truth document known to be wrong.
- Do not claim completion before acceptance criteria, verification, review findings, document consistency, and delivery reporting are handled.
