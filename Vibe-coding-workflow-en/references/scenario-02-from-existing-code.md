---
name: scenario-from-existing-code
description: Add a requirement on top of an existing codebase. Check structure first, create a plan from the goal, choose a gate level, then read the relevant code and implement.
---

# Scenario 2: Work On Existing Code

## Required Input Template

- New requirement:
- Protected areas that must not change, if any:
- Acceptance criteria:
- Where to change, if already known:

## Execution Flow

1. **Read `structure.md` and verify the real code structure**

- Open the relevant files directly when structure is unclear.
- If `structure.md` differs significantly from reality:
  - inspect the full project structure;
  - update `structure.md` first, then continue.
- Decide whether the task is L1, L2, or L3. If it affects cross-module behavior, public interfaces, or data structures, upgrade to L3.

1. **Read `goal.md` and write `plan.md` from the requirement**

- Break the requirement into actionable work items, impacted modules, and validation rules.
- If the user did not specify where to change, propose candidate change points before implementation.
- `plan.md` must include impacted files, reason for change, validation method, and regression scope.

1. **Iterate on `plan.md` until the gate is satisfied**

- For L2 and L3, do not start formal implementation without user agreement.
- For L1, implementation may start after stating the minimal change plan, but the scope must not expand silently.

1. **Locate and read the relevant code in detail**

- Read the target modules, call chains, key data structures, and boundary conditions.
- If the reading result conflicts with the original plan, update `plan.md` first.

1. **Implement the change**

- Develop strictly against the approved or stated `plan.md`.
- Backfill `plan.md`, `structure.md`, and other core documents when needed.
- Do not update `rules.md` unless the task produced a reusable rule.

## Outputs

- Updated `structure.md` if needed
- Confirmed `plan.md`
- Change list with modules, files, and impact scope
- Validation record for the new requirement and regressions
- Document backfill record

## Completion Checklist

- [ ] `structure.md` matches the real project structure, or it was updated
- [ ] `plan.md` was generated, and for L2 or L3 it was confirmed
- [ ] The new requirement works
- [ ] Existing behavior was not broken
- [ ] The change is traceable
- [ ] Impact scope and regression scope are explicitly recorded