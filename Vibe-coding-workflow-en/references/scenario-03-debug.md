---
name: scenario-debug-fix
description: A debugging workflow for development or production issues. Follow a six-step method for locating, validating, and fixing the problem, and update rules only when the fix yields reusable guidance.
---

# Scenario 3: Debug And Fix

## Required Input Template

- Symptom or error message:
- Rough trigger conditions, or state that it is intermittent:
- Expected behavior:
- Other known clues, if any:

> Note: it is normal for the user not to know technical details. Missing details should be filled in during investigation.

## Execution Flow

1. **Read `goal.md` and `structure.md` to narrow down the problem area**

- Identify the business goal, key modules, and likely impact area.
- Make minimal assumptions for missing information and mark them as pending validation.
- Decide the risk level. Production incidents, data consistency issues, and security issues should be treated as L3.

1. **Gather evidence from code and narrow the exact scope**

- Read the relevant files and call chains.
- Collect logs, stack traces, sample inputs, and other evidence.
- Record the impact boundary as modules, functions, and data paths.
- If the user cannot provide logs or environment details, build a minimal reproduction and fill in the missing context.
- If reproduction fails, at least record that reproduction failed and explain how the scope was still narrowed.

1. **Propose candidate root causes and validate them**

- List root cause hypotheses and verify them one by one.
- Keep only conclusions supported by evidence.

1. **Write the fix plan into `plan.md`**

- Document change points, risks, validation approach, and rollback idea.
- For L2, L3, or behavior-changing fixes, confirm the plan with the user first.

1. **Implement and verify the fix**

- Apply the fix under `rules.md`.
- Validate both the failing case and the key regression cases.

1. **Update `rules.md` when the lesson is reusable**

- Update `rules.md` only when the fix yields reusable rules, forbidden patterns, or review checks.
- Otherwise, explicitly state that no new reusable rule was added.

## Outputs

- Bug localization record with rough area and exact scope
- Root cause validation record with hypotheses and evidence
- Fix plan written into `plan.md`
- Post-fix validation results for the failing case and regressions
- Updated `rules.md` when applicable

## Completion Checklist

- [ ] The rough problem area was identified from `goal.md` and `structure.md`
- [ ] An evidence chain was built and the exact scope was narrowed down
- [ ] The root cause conclusion is evidence-based
- [ ] The fix plan was written into `plan.md`
- [ ] The problem was fixed and verified
- [ ] `rules.md` was updated, or it was explicitly stated that no reusable rule was needed