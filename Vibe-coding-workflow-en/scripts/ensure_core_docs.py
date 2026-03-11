from __future__ import annotations

import argparse
from pathlib import Path


DOC_TEMPLATES: dict[str, str] = {
    "goal.md": """# Project Goal

## Background
- Business scenario:
- Target users:

## Goal
- 

## Success Criteria
- Functional success criteria:
- Quality success criteria:

## Scope Boundary
- In scope:
- Out of scope:

## Constraints
- Technical constraints:
- Time constraints:
""",
    "plan.md": """# Implementation Plan

## Milestones
1. Milestone 1:
2. Milestone 2:
3. Milestone 3:

## Task Breakdown
- Task 1: goal / input / output / owner
- Task 2: goal / input / output / owner
- Task 3: goal / input / output / owner

## Acceptance Checkpoints
- Checkpoint 1:
- Checkpoint 2:

## Risks And Rollback
- Risks:
- Rollback strategy:
""",
    "rules.md": """# Coding Rules

## Default Rules
- Keep a layered design when applicable, such as interface, service, and data access layers. Do not pile business logic into entry files.
- Keep configuration in a dedicated place such as a config module or config file. Avoid scattered hard-coded values.
- Critical flows must have explicit error handling. Do not fail silently.
- Validate external input before entering business logic.
- Keep functions single-purpose. Split complex functions into smaller ones.
- Confirm scope before changing code, and provide at least minimal reproducible validation after the change.

## Naming
- Use meaningful names. Do not let names like `tmp` or `test1` enter production code.

## Style
- Keep formatting consistent and prefer small, low-coupling functions.

## Error Handling
- Error messages should be actionable and include enough context for diagnosis.

## Logging And Comments
- Log key paths. Comments should explain why, not restate what the code does.

## Security And Privacy
- Never commit secrets, tokens, passwords, or similar sensitive data.

## Testing And Regression
- Cover at least the main flow and one failure branch.

## Anti-Patterns
- Avoid direct cross-layer calls that create uncontrolled coupling.
""",
    "structure.md": """# Project Structure

## Directory Layout
- Root directory:

## Module Breakdown
- 

## Data Flow Or Call Flow
- 

## Dependencies And External Interfaces
- 

## Key Entry Files
- 

## High-Risk Modules
- 
""",
}

REQUIRED_SECTIONS: dict[str, tuple[str, ...]] = {
    "goal.md": (
        "## Background",
        "## Goal",
        "## Success Criteria",
        "## Scope Boundary",
        "## Constraints",
    ),
    "plan.md": (
        "## Milestones",
        "## Task Breakdown",
        "## Acceptance Checkpoints",
        "## Risks And Rollback",
    ),
    "rules.md": (
        "## Default Rules",
        "## Naming",
        "## Style",
        "## Error Handling",
        "## Logging And Comments",
        "## Security And Privacy",
        "## Testing And Regression",
        "## Anti-Patterns",
    ),
    "structure.md": (
        "## Directory Layout",
        "## Module Breakdown",
        "## Data Flow Or Call Flow",
        "## Dependencies And External Interfaces",
        "## Key Entry Files",
        "## High-Risk Modules",
    ),
}

PLACEHOLDER_HINTS: dict[str, tuple[str, ...]] = {
    "goal.md": ("- Business scenario:", "- Target users:", "- Functional success criteria:"),
    "plan.md": ("Milestone 1:", "- Task 1: goal / input / output / owner", "- Risks:"),
    "rules.md": ("## Default Rules",),
    "structure.md": ("- Root directory:", "## Module Breakdown"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check and bootstrap core docs: goal.md, plan.md, rules.md, structure.md"
    )
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root directory, default is current directory",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Only validate document status without creating missing files",
    )
    return parser.parse_args()


def validate_content(name: str, content: str) -> tuple[bool, list[str]]:
    missing_sections = [
        section for section in REQUIRED_SECTIONS[name] if section not in content
    ]
    return (len(missing_sections) == 0, missing_sections)


def collect_warnings(name: str, content: str) -> list[str]:
    warnings: list[str] = []
    if content == DOC_TEMPLATES[name]:
        warnings.append("document is still the default template")

    if "    ##" in content:
        warnings.append("contains indented headings that may render incorrectly")

    hint_hits = sum(1 for hint in PLACEHOLDER_HINTS[name] if hint in content)
    if hint_hits == len(PLACEHOLDER_HINTS[name]):
        warnings.append("placeholder content has not been replaced yet")

    return warnings


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).resolve()
    docs_dir = project_root / "docs"

    print(f"[INFO] ProjectRoot: {project_root}")
    print(f"[INFO] DocsDir: {docs_dir}")

    if not args.check_only:
        project_root.mkdir(parents=True, exist_ok=True)
        docs_dir.mkdir(parents=True, exist_ok=True)

    has_error = False

    if not docs_dir.exists():
        print("[MISSING] docs/")
        return 1

    for name, template in DOC_TEMPLATES.items():
        path = docs_dir / name
        if not path.exists():
            if args.check_only:
                print(f"[MISSING] docs/{name}")
                has_error = True
                continue

            path.write_text(template, encoding="utf-8")
            print(f"[CREATED] docs/{name}")
            content = template
        else:
            print(f"[EXISTS] docs/{name}")
            content = path.read_text(encoding="utf-8")

        is_valid, missing_sections = validate_content(name, content)
        if not is_valid:
            print(
                f"[INVALID] docs/{name} missing sections: {', '.join(missing_sections)}"
            )
            has_error = True

        for warning in collect_warnings(name, content):
            print(f"[WARN] docs/{name} {warning}")

    print("[DONE] Core docs check completed.")
    return 1 if has_error else 0


if __name__ == "__main__":
    raise SystemExit(main())