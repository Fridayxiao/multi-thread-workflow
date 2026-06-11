# Multi-Thread Delivery Workflow Definition

Version: 0.1

## Purpose

This workflow is for complex or high-risk user goals. It reduces four common delivery risks: misunderstood requirements, outdated or shallow solution design, execution drift, and vague final acceptance.

The lead agent must align the goal and success criteria with the user, use controlled threads for research, design, prototypes, and execution, maintain phase documents, synthesize thread results, and remain accountable for the final delivery. Threads are bounded work units. Sub-agents are used for independent review, specialist checks, and second opinions.

## Applicability

Use this workflow when:

- The user explicitly asks for or approves this workflow.
- The goal is complex, multi-stage, high-risk, or likely to benefit from research, parallel work, prototype validation, or independent review.
- The work involves multiple modules, domains, systems, stakeholders, or material tradeoffs.
- Failure would be costly enough to justify documents, gates, and verification.

Do not use this workflow when:

- The task is a simple answer, explanation, translation, formatting change, or small low-risk edit.
- The user asks for fast direct execution and does not want the workflow.
- The user does not allow threads, phase documents, or confirmation gates.
- The goal is too broad for one workflow and should be split first.

## Roles

### User

The user is the source of goals, requirements, constraints, solution choice, acceptance criteria, and final acceptance. The user must explicitly confirm key gates.

### Lead Agent

The lead agent owns the workflow. It clarifies the goal, maintains documents, creates threads, provides self-contained briefs, synthesizes outputs, resolves conflicts, updates source-of-truth documents, asks for user confirmation, and decides whether to proceed, stop, or roll back.

The lead agent must not outsource user alignment, final synthesis, or acceptance decisions to threads or sub-agents.

### Worker Thread

A worker thread is a bounded work unit for research, design, prototype, implementation, or execution. It must follow its brief, stay in scope, use relevant skills, verify its own work, call the predefined reviewer sub-agent before handoff in Phase 6, and report risks or upstream document problems.

### Reviewer Sub-Agent

The reviewer sub-agent is predefined outside this workflow. This workflow only controls when to call it, what context to provide, and how to handle its output. Its own system prompt controls review behavior. Its findings are advisory until evaluated by the worker thread or lead agent.

### Specialist Sub-Agent

A specialist sub-agent may be used for security, performance, UX, database, compliance, fact-checking, or other focused checks. Its output is advisory and must be synthesized by the lead agent.

## Modes

### Full Mode

Use Full Mode for high-risk, high-complexity, multi-stakeholder, or explicitly complete workflows.

Requirements:

- Execute Phase 0 through Phase 7.
- Use threads in Phase 2 and Phase 6.
- Use Phase 4 when prototype validation reduces material risk or the user requests it.
- Maintain complete source-of-truth documents.
- Keep explicit user gates.
- Require reviewer sub-agent review inside each Phase 6 worker thread.
- Produce a final delivery report.

### Standard Mode

Standard Mode is the default for complex goals.

Requirements:

- Execute Phase 1, Phase 2, Phase 3, Phase 5, Phase 6, and Phase 7.
- Phase 4 is optional.
- Documents may be concise but must exist.
- Use at least one research/design thread in Phase 2.
- Use at least one worker thread in Phase 6.
- Require worker-thread review.
- Do not skip user gates.

### Lite Mode

Use Lite Mode only when the user wants speed and the risk is acceptable.

Requirements:

- Phase 1, Phase 3, and Phase 5 may be concise or combined, but goal, acceptance, and execution path must remain explicit.
- Phase 2 may use one research thread, but should still compare at least two options unless the user explicitly wants one direction.
- Phase 6 still requires verification and review.
- Durable documentation is still required. A combined Lite document is acceptable, but it must preserve every phase's required decisions, evidence, validation, and user confirmations.
- Explain the risks of compression.
- Do not use Lite Mode for high-risk work.

### Exit or Split

Exit the workflow when the task is too small, the user will not allow essential gates, or the cost exceeds the benefit.

Split the workflow when the goal contains independent sub-goals with different acceptance criteria, owners, prototypes, or delivery paths. First align the parent goal, child workflows, ordering, shared constraints, dependencies, and the first child workflow to run.

## Phase 0: Activation

Goal: decide whether to use the workflow and establish workflow-level thread authorization.

Threads: not allowed.

Gate:

- The user explicitly asks for or approves the workflow.
- The user understands the workflow may create threads, produce documents, and wait at key gates.
- The workflow document directory is established. Default to `docs/agent-workflows/<goal-slug>/` unless the user specifies another location.
- The lead agent judges the task suitable.

If the task is too small or the user rejects threads/documents/gates, exit the workflow.

## Phase 1: Problem, Goal, Requirements Alignment

Goal: define the problem, target outcome, requirements, constraints, non-goals, unknowns, and risks.

Threads: not allowed.

Artifact: `01-problem-goal-requirements.md`.

Gate:

- The document or equivalent draft clearly states the problem, goal, requirements, constraints, non-goals, unknowns, and user confirmation record.
- The user explicitly confirms it.
- Unknowns are recorded and do not block research.

Rollback:

- If the user disagrees, continue clarifying in Phase 1.
- If the goal splits into independent goals, split the workflow.

## Phase 2: Research and Solution Design

Goal: research existing and current solutions, verify relevant APIs or practices, and present at least two viable solution options with tradeoffs.

Threads: at least one research/design thread is required.

Artifact: `02-solution-options.md`.

Research requirements:

- Actively investigate usable or adaptable existing solutions before proposing custom work.
- Verify current status for information that may be stale, including APIs, dependencies, standards, regulations, market facts, and product behavior.
- If no suitable existing solution is found, collect enough task and system context to justify a custom design.
- The lead agent must interact with research/design threads until their output is strong enough to support at least two options and a defensible recommendation.
- `02-solution-options.md` must record what existing solutions were investigated and why they were adopted or rejected.

Gate:

- At least one research/design thread has completed.
- At least two options are compared.
- Key assumptions, deprecation risks, and freshness risks are checked or explicitly recorded.
- The lead agent recommends a default with rationale.
- The user selects one option or approves a combination.

Rollback:

- If research is insufficient, continue Phase 2.
- If no option satisfies Phase 1, return to Phase 1.
- If the user introduces a new goal, update Phase 1.

## Phase 3: Acceptance Criteria

Goal: define what "done" means before execution begins.

Threads: not allowed.

Artifact: `03-acceptance-criteria.md`.

Gate:

- Each core requirement maps to at least one acceptance criterion.
- Each criterion has a validation method or an explicit substitute judgment method.
- Unacceptable outcomes are stated.
- The user explicitly confirms the criteria.

Rollback:

- If criteria fail to cover requirements, continue Phase 3 or return to Phase 1.
- If criteria conflict with the selected solution, return to Phase 2.

## Phase 4: Demo or Prototype

Goal: create something the user can see, try, review, or reason about before full execution.

Threads: use a prototype thread when Phase 4 is active.

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

Goal: plan how to execute before doing the work. Identify serial dependencies, parallel paths, worker thread boundaries, integration strategy, validation strategy, risks, and rollback points.

Threads: not allowed.

Artifact: `05-execution-paths.md`.

Gate:

- The execution path is clear.
- Parallel and serial work are separated.
- Each worker thread has a target, scope, inputs, outputs, validation method, and stopping conditions.
- Integration and rollback are defined.
- The user explicitly confirms the plan.

Rollback:

- If planning exposes solution problems, return to Phase 2.
- If planning exposes acceptance problems, return to Phase 3.

## Phase 6: Execution, Verification, Review

Goal: execute the plan, verify results, run worker-thread reviewer sub-agent review, integrate outputs, and update documents.

Threads: worker threads are required.

Artifact: `06-execution-log.md`.

Requirements:

- Each worker thread follows its brief and uses relevant skills.
- Each worker thread verifies its own scope.
- Each worker thread calls the predefined reviewer sub-agent before handoff.
- Each worker thread handles reviewer findings by fixing, documenting accepted risk, or reporting an upstream problem.
- The lead agent checks each handoff, integrates work, resolves conflicts, and performs final workflow-level verification.
- Affected source-of-truth documents are updated.

Gate:

- All worker threads are complete or explicitly canceled.
- Required verification has run or residual risk is explicit.
- Reviewer sub-agent findings are handled.
- The execution log includes thread registry, verification evidence, review summaries, integration notes, and unresolved risks.
- Delivered work still matches `01`, `02`, `03`, and `05`.

Rollback:

- If execution drifts from requirements, return to Phase 1 or Phase 5.
- If execution exposes solution flaws, return to Phase 2.
- If criteria are incomplete, return to Phase 3.
- If integration fails, return to Phase 5.

## Phase 7: Delivery Report and User Acceptance

Goal: report the final state and give the user a clear acceptance path.

Threads: usually not allowed. A final specialist or reviewer sub-agent check may be used when needed, but the lead agent must synthesize it.

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

Thread and review briefs are not required as separate files. Their content may live in the thread or sub-agent context. `06-execution-log.md` must preserve enough registry, status, verification, review, and risk information to audit the workflow.

Only the lead agent updates source-of-truth conclusions. Worker threads may recommend updates but must not change requirements, solution decisions, or acceptance criteria on their own.

## Document Maintenance Duty

Every phase must maintain upstream documents, not only create its own artifact.

- At the start of each phase, the lead agent checks whether upstream source-of-truth documents are still accurate, complete, and current enough to continue.
- At the end of each phase, the lead agent records whether the phase affected upstream documents.
- If a phase reveals that an upstream document is wrong or incomplete, update the affected document and re-run any required user gate before continuing.
- Worker threads must report suggested source-of-truth updates in their handoff instead of changing user-confirmed decisions on their own.
- Phase 6 must explicitly check whether execution changed or invalidated `01`, `02`, `03`, or `05`.
- Before Phase 7 delivery, the lead agent must perform a final consistency check across source-of-truth documents and the actual delivered result.

## Thread Protocol

Threads are allowed only in Phase 2, Phase 4, and Phase 6.

Before creating a thread, the lead agent must state in the main workflow:

- Why the thread is needed.
- The thread's task boundary.
- What it may read or write.
- Expected output.
- How the result will return to the workflow.

Every thread brief must be self-contained and include:

- Current workflow phase.
- User goal and success criteria summary.
- Relevant source-of-truth document summaries or paths.
- Specific task.
- Scope and non-scope.
- Readable context.
- Writable boundaries.
- Expected output format.
- Verification requirements.
- Skill usage requirements.
- Stopping conditions.
- Handoff requirements.

Worker threads must stop and report when the brief conflicts with reality, scope needs to expand, upstream documents appear wrong, validation cannot run, dependencies are missing, or the next action would be destructive or high risk.

## Skill Usage in Threads

Each thread must identify and use the minimal relevant set of available skills.

The lead agent should name any known relevant skills in the brief. The thread must read selected `SKILL.md` files and follow their gate, validation, and output requirements. If a seemingly relevant skill is skipped, the thread must explain why in its handoff.

If skill instructions conflict with the workflow brief, the thread must stop when the conflict changes scope, safety, phase gates, or user commitments.

## Reviewer Sub-Agent Usage

In Phase 6, every worker thread must call the predefined reviewer sub-agent before handoff.

The workflow must provide or require enough review context:

- User goal.
- Requirements.
- Selected solution.
- Acceptance criteria.
- Execution plan scope.
- Actual deliverable or changes.
- Verification already run.
- Known risks.

The reviewer sub-agent's own system prompt controls review behavior. The workflow does not redefine it. Worker threads and the lead agent must treat findings as advisory, then fix, document accepted risk, or roll back to an earlier phase when needed.

## Execution Quality

All execution must trace back to requirements and acceptance criteria.

For code tasks, use TDD by default:

- Bugs: reproduce or write a failing test first.
- Features: define acceptance, unit, or integration tests before implementation where practical.
- Refactors: confirm coverage or add characterization tests when needed.
- Do not weaken tests just to pass.
- Worker threads run scope-level tests.
- Worker threads must run relevant verification before handoff.
- If a worker thread creates a commit or asks the lead agent to commit its work, relevant tests and checks must run before that commit.
- The lead agent runs appropriate integration-level checks such as tests, lint, typecheck, build, or e2e according to the project.
- The lead agent must run appropriate verification after integrating worker outputs and before any final commit or delivery.

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
- Active and completed threads.
- Rollbacks.
- Next gate.

For complex workflows, create `00-workflow-state.md`. Otherwise keep state in phase documents and `06-execution-log.md`.

Record rollbacks with the trigger, affected documents, target phase, gates to re-run, and which prior work remains valid.

## Hard Rules

- Do not use threads before the user activates the workflow.
- Do not use threads in Phase 1, Phase 3, or Phase 5.
- Do not let threads or sub-agents replace user confirmation.
- Do not let worker threads change source-of-truth decisions on their own.
- Do not continue from a source-of-truth document known to be wrong.
- Do not claim completion before acceptance criteria, verification, review findings, document consistency, and delivery reporting are handled.
