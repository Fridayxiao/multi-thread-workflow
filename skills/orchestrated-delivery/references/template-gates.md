# User Confirmation Templates

Read this file when asking the user to confirm phase results.

User confirmation must be explicit. Do not treat silence, "looks okay" without a clear decision, or lack of objection as approval.

## Single Phase Confirmation

```text
Current phase: <phase>.

Please confirm before I proceed:
<specific decision or artifact being confirmed>

Summary:
<short summary>

Important tradeoffs or risks:
- <risk or tradeoff>

Recommended default:
<recommendation, if useful>

Please explicitly confirm, reject, or request changes.
```

## One Response Confirming Multiple Phase Results

Use this only in Lite mode or low-risk Standard mode when the user wants fewer interruptions. This means the user confirms several already-written results at once; it does not skip confirmation.

```text
Please confirm these results before I proceed:

1. Requirements:
<summary>

2. Selected solution:
<summary>

3. Acceptance criteria:
<summary>

4. Execution path:
<summary>

Known risks:
- <risk>

Please explicitly confirm all, or list the items that need changes.
```

Record the exact items confirmed in the relevant phase documents.

## Reconfirmation After Change

```text
The workflow needs reconfirmation because <what changed>.

Previously confirmed:
<old decision>

Updated proposal:
<new decision>

Impact:
- <impact>

Please explicitly confirm the updated version or request changes.
```
