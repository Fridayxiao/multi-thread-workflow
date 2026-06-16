# Phase 4: Optional Demo Or Prototype

Read this file only when a prototype or demo is requested or would materially reduce risk.

## Goal

Create something observable that lets the user test, inspect, or reason about the proposed direction before full execution.

## Entry

Use this phase when:

- The user asks for a prototype or demo.
- A prototype would reduce material uncertainty about product flow, feasibility, integration, or user acceptance.

## Approach

1. Define what the prototype is meant to validate.
2. Define what it does not validate.
3. Use a thread when the prototype needs independent worktree context, persistent state, long-running iteration, separated tracking, or risk isolation. Otherwise use lead-owned work or a bounded delegate.
4. Make the prototype observable to the user when possible.
5. Collect feedback and update Phase 1, 2, or 3 documents when feedback changes them.

## Artifact

Create `04-prototype-notes.md` when this phase is used. Use `template-documents.md`.

## Output Contract (Required Fields)

`04-prototype-notes.md` must include:

- prototype purpose;
- output produced and how to view or use it;
- what the prototype validates;
- what it does not validate;
- verification performed;
- user feedback, or the user's explicit agreement to continue without prototype feedback;
- impact on requirements, solution, and acceptance criteria.

## Gate

Proceed only when:

- The prototype or demo result is recorded.
- User feedback is handled, or the user explicitly agrees to continue without prototype feedback.
- Impact on requirements, solution, and acceptance criteria is handled.

## Rollback

Return to Phase 1, 2, or 3 when prototype feedback changes requirements, solution, or done criteria.
