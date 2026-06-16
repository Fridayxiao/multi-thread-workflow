# Shared Hard Rules

Read this file at workflow start and apply it before phase-specific rules.

## Terms Used Here

- A gate is a required check before moving to the next phase. When the gate says user confirmation is required, the confirmation must be explicit.
- Source-of-truth documents are confirmed phase documents that later work must follow unless they are explicitly updated and reconfirmed.
- A delegate is a thread or subagent given a bounded task.
- A reviewer is a specialized subagent asked to check work against the confirmed goal, requirements, solution, acceptance criteria, and execution path.
- A handoff is the delegate's return report to the lead agent.
- Review-gated execution means work that cannot be handed off or integrated until the required reviewer has checked it.
- Residual risk means a known remaining risk after verification, fallback, or review.

## Rules

- Keep phases separate and follow them in order unless the user explicitly chooses Lite, Exit, or Split mode.
- Do not treat silence or lack of objection as approval.
- Phase 1, Phase 3, and Phase 5 are lead-owned. Do not use threads in those phases.
- The lead agent must not outsource user alignment, final synthesis, source-of-truth decisions, or acceptance decisions.
- Use project evidence before making decisions: instructions, docs, code, tests, runtime behavior, and current authoritative sources when facts can go stale.
- Use the workflow language for phase communication, documents, delegate prompts, handoffs, reports, and gate requests unless the user asks otherwise.
- Standard and Full mode require at least one independent research or design delegate in Phase 2. Lite mode may skip it only when speed is more important than independence, and the reason must be recorded.
- Do not create or adopt a persistent goal during Phase 1, Phase 2, or Phase 3. After Phase 3, create or adopt one only with explicit user agreement and only from confirmed source-of-truth documents.
- Delegated output is advisory until the lead agent checks it.
- Non-trivial review-gated execution lanes must use a thread unless the lead agent owns the work directly and runs review itself.
- Do not assign review-gated execution to an ordinary subagent, because ordinary subagents cannot call reviewer subagents before handoff.
- If a needed tool is unavailable, state the fallback before relying on it and record residual risk when the fallback weakens coverage.
- Do not weaken tests, validation, or review requirements just to proceed.
- Do not claim completion until final delivery satisfies the completion checks in `artifacts.md`.
