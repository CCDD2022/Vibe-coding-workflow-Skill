---
name: scenario-from-scratch
description: Build a new project from a requirement. Choose a gate level based on risk, define goals and plan first, then implement and deliver.
---

# Scenario 1: Build From Scratch

## Required Input Template

- What needs to be built in one sentence:
- Final deliverable type: program / script / page / API / other
- Explicit non-goals, if any:
- What counts as done, with at least one verifiable rule:

## Execution Flow

1. **Clarify the requirement and scope**

- Ask follow-up questions for ambiguous requirements.
- Decide whether the task is L1, L2, or L3. Default to L2.

1. **Write `goal.md`**

- Define objective, scope, success criteria, and non-goals.
- For L1 tasks, a compact version is acceptable, but deliverable and completion rules must still be explicit.

1. **Write `plan.md`**

- Break the task into milestones, ordered work items, validation points, and risks.
- For L1, the minimum is: what will change, how it will be verified, and what to do if it fails.

1. **Apply the confirmation gate**

- For L2 and L3, iterate with the user until `goal.md` and `plan.md` are confirmed.
- For L1, if the user clearly asked for direct delivery, implementation may start after the plan is stated, but validation and result explanation are still mandatory.

1. **Implement, validate, and backfill documents**

- Follow `plan.md` and update it first if implementation deviates.
- Validate the running result and acceptance checks.
- Update `structure.md` and `rules.md` only when structure or reusable rules actually changed.

## Outputs

- Confirmed `goal.md`
- Confirmed `plan.md`
- Implementation and run instructions
- Validation record for main flow, edge cases, and failure cases
- Updated documents when needed

## Completion Checklist

- [ ] `goal.md` was generated and confirmed
- [ ] `plan.md` was generated, and for L2 or L3 it was confirmed
- [ ] The main flow runs successfully, or a limitation and alternative validation are clearly provided
- [ ] The output matches the promised deliverable
- [ ] All completion rules are satisfied
- [ ] At least one piece of validation evidence is provided