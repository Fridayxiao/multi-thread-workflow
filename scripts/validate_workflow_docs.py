#!/usr/bin/env python3
"""Validate minimum structure for Orchestrated Delivery workflow documents."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


STANDARD_REQUIRED = [
    "01-problem-goal-requirements.md",
    "02-solution-options.md",
    "03-acceptance-criteria.md",
    "05-execution-paths.md",
    "06-execution-log.md",
    "07-delivery-report.md",
]


CHECKS = {
    "01-problem-goal-requirements.md": [
        ("must-have requirement id", re.compile(r"\bR-\d{3}\b")),
        ("source or owner", re.compile(r"Source/owner|Source or owner", re.I)),
        ("rationale", re.compile(r"\bRationale\b", re.I)),
        ("acceptance hint or validation surface", re.compile(r"Acceptance hint|validation surface", re.I)),
        ("user confirmation", re.compile(r"User Confirmation", re.I)),
    ],
    "02-solution-options.md": [
        ("Option A", re.compile(r"\bOption A\b", re.I)),
        ("Option B", re.compile(r"\bOption B\b", re.I)),
        ("fit to Phase 1 IDs", re.compile(r"Fit to Phase 1 IDs|Fit to R-\*|Fit to .*IDs", re.I)),
        ("freshness checks", re.compile(r"Freshness|Deprecation", re.I)),
        ("user decision", re.compile(r"User Decision", re.I)),
    ],
    "03-acceptance-criteria.md": [
        ("acceptance criterion id", re.compile(r"\bAC-\d{3}\b")),
        ("covers mapping", re.compile(r"\bCovers\b", re.I)),
        ("validation method", re.compile(r"\bValidation\b", re.I)),
        ("user confirmation", re.compile(r"User Confirmation", re.I)),
    ],
    "05-execution-paths.md": [
        ("execution path coverage", re.compile(r"\bCovers\b", re.I)),
        ("verification plan", re.compile(r"\bVerification\b", re.I)),
        ("review plan", re.compile(r"\bReview\b", re.I)),
        ("review-gated field", re.compile(r"Review-gated", re.I)),
        ("user confirmation", re.compile(r"User Confirmation", re.I)),
    ],
    "06-execution-log.md": [
        ("verification evidence", re.compile(r"Verification Evidence", re.I)),
        ("review results", re.compile(r"Review Results", re.I)),
        ("document updates", re.compile(r"Document Updates", re.I)),
        ("open risks or blockers", re.compile(r"Open Risks Or Blockers", re.I)),
    ],
    "07-delivery-report.md": [
        ("acceptance criteria results", re.compile(r"Acceptance Criteria Results", re.I)),
        ("verification performed", re.compile(r"Verification Performed", re.I)),
        ("review summary", re.compile(r"Review Summary", re.I)),
        ("user acceptance steps", re.compile(r"User Acceptance Steps", re.I)),
        ("final user acceptance", re.compile(r"Final User Acceptance", re.I)),
    ],
}


FORBIDDEN_PATTERNS = [
    ("old earlier-document wording", re.compile(r"Upstream Check", re.I)),
    ("unresolved placeholder", re.compile(
        r"\bTODO\b"
        r"|<(?:placeholder|fill-in|fill in|TBD|your-[^>]+|insert-[^>]+|REPLACE[^>]*)>",
        re.I,
    )),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workflow_dir", type=Path, help="Directory containing workflow markdown documents.")
    parser.add_argument(
        "--mode",
        choices=["Full", "Standard", "Lite"],
        default="Standard",
        help="Workflow mode. Lite allows combined documents when explicit.",
    )
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Allow TODO and <placeholder> markers while drafting.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text()


def validate_file(path: Path, errors: list[str], *, allow_placeholders: bool) -> None:
    if not path.exists():
        errors.append(f"missing required artifact: {path.name}")
        return
    text = read_text(path)
    if not text.strip():
        errors.append(f"empty artifact: {path.name}")
        return

    for label, pattern in CHECKS.get(path.name, []):
        if not pattern.search(text):
            errors.append(f"{path.name}: missing {label}")

    for label, pattern in FORBIDDEN_PATTERNS:
        if allow_placeholders and label == "unresolved placeholder":
            continue
        if pattern.search(text):
            errors.append(f"{path.name}: contains {label}")


def has_combined_lite_docs(workflow_dir: Path) -> bool:
    """Check that combined Lite-mode documents contain the required section headers."""
    texts = []
    for path in workflow_dir.glob("*.md"):
        texts.append(read_text(path))
    combined = "\n".join(texts)
    # Match actual section headers from templates, not just keywords.
    required_headers = [
        re.compile(r"#.*Problem.*Goal.*Requirements", re.I),
        re.compile(r"#.*Solution\s+Options|#.*Research.*Solution", re.I),
        re.compile(r"#.*Acceptance\s+Criteria", re.I),
        re.compile(r"#.*Execution\s+(Paths|Log)", re.I),
        re.compile(r"#.*Delivery\s+Report", re.I),
    ]
    return all(header.search(combined) for header in required_headers)


def main() -> int:
    args = parse_args()
    workflow_dir = args.workflow_dir
    errors: list[str] = []

    if not workflow_dir.exists() or not workflow_dir.is_dir():
        print(f"Workflow directory does not exist: {workflow_dir}", file=sys.stderr)
        return 2

    if args.mode == "Lite" and has_combined_lite_docs(workflow_dir):
        print("Workflow docs validation passed for Lite combined documents.")
        return 0

    for filename in STANDARD_REQUIRED:
        validate_file(workflow_dir / filename, errors, allow_placeholders=args.allow_placeholders)

    # Phase 4 prototype validation
    prototype_path = workflow_dir / "04-prototype-notes.md"
    if prototype_path.exists():
        prototype = read_text(prototype_path)
        for label in ["Purpose", "Output", "Validates", "User Feedback", "Impact On Prior Documents"]:
            if label.lower() not in prototype.lower():
                errors.append(f"04-prototype-notes.md: missing {label}")
    elif args.mode == "Full":
        # Full mode expects Phase 4 unless explicitly skipped.
        errors.append(
            "04-prototype-notes.md: missing in Full mode "
            "(expected unless prototype was explicitly skipped)"
        )

    if errors:
        print("Workflow docs validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Workflow docs validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
