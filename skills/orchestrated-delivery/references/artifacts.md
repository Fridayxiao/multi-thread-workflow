# Workflow Artifacts

Read this file when choosing document paths, resuming a workflow, checking phase output, or preparing final delivery.

An artifact is a file produced by a workflow phase. An output contract is the required information that must appear in an artifact before the phase can be considered complete.

## Default Directory

Use `docs/agent-workflows/<goal-slug>/` unless the user provides another location. Here, `<goal-slug>` means a short filesystem-safe name for the goal.

For Lite mode, documents may be combined only when the combined file still contains the required information for the phases used.

## Required Artifacts

- `01-problem-goal-requirements.md`: confirmed problem, goal, scope, requirements, constraints, assumptions, questions, risks, non-goals, and terms.
- `02-solution-options.md`: research summary, reusable solutions checked, at least two options when required, freshness checks, recommendation, and user decision.
- `03-acceptance-criteria.md`: done criteria mapped to requirements, validation methods, and unacceptable outcomes.
- `05-execution-paths.md`: serial and parallel execution paths, ownership, scope, outputs, verification, review, integration, and rollback.
- `06-execution-log.md`: completed work, delegation, verification evidence, review results, integration notes, document updates, and open risks.
- `07-delivery-report.md`: delivered work mapped to acceptance criteria, verification, review summary, limitations, risks, and user acceptance steps.

## Optional Artifacts

- `04-prototype-notes.md`: required only when Phase 4 is used.
- `00-workflow-state.md`: use for long, paused, resumed, split, or high-risk workflows.

## Source-Of-Truth Rules

Source-of-truth documents are confirmed phase documents that later work must follow unless they are explicitly updated and reconfirmed.

- Treat `01`, `02`, `03`, and `05` as source-of-truth after user confirmation.
- Keep source-of-truth documents aligned with actual work.
- At the start and end of each phase, check whether earlier source-of-truth documents still match reality.
- If an earlier source-of-truth document is wrong, return to the affected phase, update it, and re-run the needed confirmation.
- Delegates may suggest document updates, but the lead agent decides and applies source-of-truth changes.

## Completion Checks

Before Phase 7 completion, confirm that:

- every required artifact for the selected mode exists or is intentionally combined in Lite mode;
- each artifact satisfies the required output fields in its phase reference;
- user confirmations are recorded for Phase 1, Phase 2, Phase 3, Phase 5, and Phase 7;
- Phase 4 confirmation is recorded when Phase 4 is used;
- `06-execution-log.md` records verification and review outcomes;
- `07-delivery-report.md` maps delivered work to acceptance criteria and gives user acceptance steps.

When available, run the workflow document validator before final delivery. The script is located at `scripts/validate_workflow_docs.py` relative to the plugin root (the directory containing `skills/` and `scripts/`). Locate the plugin root from the skill path, then run:

```bash
uv run python <plugin-root>/scripts/validate_workflow_docs.py <workflow-document-directory> --mode <Full|Standard|Lite>
```

If `uv` is not available, use `python3` directly:

```bash
python3 <plugin-root>/scripts/validate_workflow_docs.py <workflow-document-directory> --mode <Full|Standard|Lite>
```

