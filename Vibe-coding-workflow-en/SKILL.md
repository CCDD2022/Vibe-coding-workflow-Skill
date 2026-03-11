---
name: Vibe-coding-workflow-en
description: A code delivery skill for non-technical users. Covers greenfield work, feature development on existing code, and debugging, with progressive gates and document backfill based on task risk.
compatibility: Works in agent environments that support Agent Skills and provide file read/write plus script execution capabilities.
metadata:
  author: CCDD2022
  version: "1.2"
---

# General Code Delivery Skill

## Goal

Help non-technical users produce deliverable code through a standard workflow with traceable steps and verifiable outcomes.

## Supported Scenarios

This skill supports 3 scenarios:

1. Build from scratch
2. Add features on top of existing code
3. Debug and fix problems

## When To Use

- You need to turn business requirements into deliverable code with traceability and acceptance criteria.
- The task should follow a standard workflow with clear inputs, outputs, and gates.
- The task involves multi-file changes, impact analysis on an existing system, debugging, or process documentation.

## When Not To Use

- You only need a throwaway script or demo and do not need documentation, acceptance, or delivery records.
- The requester explicitly refuses requirement clarification, plan confirmation, execution records, or acceptance criteria.
- The task has no relationship to the core document set in `docs/goal.md`, `docs/plan.md`, `docs/rules.md`, and `docs/structure.md`.

## Gate Levels

- L1 Lightweight: single-file, low-risk, small-scope changes. A short `plan.md` is enough, and you may start after stating the plan.
- L2 Standard: multi-file work, typical bug fixes, or tasks that require reading a call chain. A usable `plan.md` is required before formal implementation.
- L3 High Risk: architecture changes, databases, external interfaces, permissions, security, or rollback-sensitive changes. Confirm goals, plan, risks, and rollback before implementation.

Selection rules:

- If you cannot quickly prove the task is low risk, default to L2.
- Only L1 may skip explicit confirmation.
- If the task enters a high-risk area, immediately upgrade it to L3.

## Shared Workflow

0. Run the bootstrap script `scripts/ensure_core_docs.py` first. It creates `docs/` in the project root and checks whether the core document structure is complete:

  - `docs/goal.md`
  - `docs/plan.md`
  - `docs/rules.md`
  - `docs/structure.md`

1. Read all 4 core documents and decide which ones need to be created, repaired, or updated.
2. Choose a scenario and a gate level.
3. Clarify the requirement, define scope, and write the plan before formal implementation.
4. Exploratory work is limited to read-only analysis, minimal reproductions, or non-persistent validation unless formal implementation has been approved.
5. If documents and reality diverge, backfill documents according to the update policy.
6. Deliver the result package with evidence, risks, and next steps.

## Document Update Policy

- `docs/goal.md`: update only when the task goal, scope boundary, target users, or completion definition changes.
- `docs/plan.md`: update when entering L2 or L3, when implementation deviates from the plan, when the fix strategy changes, or when validation changes.
- `docs/rules.md`: update only when the task produces reusable rules, forbidden patterns, or review checks. Do not store one-off details here.
- `docs/structure.md`: update only when module boundaries, directory structure, call flow, key entries, or high-risk modules change.

## Scenario Routing

- No usable codebase yet: use [references/scenario-01-from-scratch.md](references/scenario-01-from-scratch.md)
- Existing code with a new requirement: use [references/scenario-02-from-existing-code.md](references/scenario-02-from-existing-code.md)
- Existing error or abnormal behavior to diagnose and fix: use [references/scenario-03-debug.md](references/scenario-03-debug.md)

## Standard Output Format

1. Goal summary
2. Execution record
3. Evidence of results
4. Risks and limits
5. Document updates
6. Suggested next steps

## Global Quality Gates

- `docs/goal.md` matches the current task goal and clearly defines in-scope and out-of-scope items.
- `docs/plan.md` contains at least steps, impact scope, validation approach, and risks or rollback notes.
- `docs/rules.md` covers the key coding or fixing rules for this task. If no reusable rule was added, explicitly state that no update was needed.
- `docs/structure.md` matches the current project structure or has been updated. If the task did not affect structure, explicitly state that there was no structural change.
- The result is reproducible and includes at least one piece of evidence such as a command, screenshot, log, test result, or sample input/output.
- The final output answers 3 questions: what changed, how it was verified, and what risks remain.

## Scenario Documents

- [references/scenario-01-from-scratch.md](references/scenario-01-from-scratch.md)
- [references/scenario-02-from-existing-code.md](references/scenario-02-from-existing-code.md)
- [references/scenario-03-debug.md](references/scenario-03-debug.md)

## Bootstrap Script

- [scripts/ensure_core_docs.py](scripts/ensure_core_docs.py)

  - Purpose: create `docs/` in the project root and check whether `docs/goal.md`, `docs/plan.md`, `docs/rules.md`, and `docs/structure.md` exist and contain required sections.
  - Parameters: `--project-root` optional, defaults to current directory; `--check-only` validates without creating missing files.
  - Output: status per document using `EXISTS`, `CREATED`, `MISSING`, `INVALID`, and `WARN`.

## Quick Start

1. Run the bootstrap script.
2. Read the 4 core documents and decide whether the task is L1, L2, or L3.
3. Pick the matching scenario and execute it.
4. Backfill documents only where needed, then output the delivery package.

## Boundaries And Exception Handling

- If requirements are unclear, clarify first and do not code immediately.
- If core documents are missing, repair them before entering scenario execution.
- If `docs/plan.md` is not confirmed, L2 and L3 must not start formal coding. L1 may proceed only within a minimal scope and must include plan and validation in the output.
- If the fix is high risk, define a rollback plan before implementation.
- If the current document structure is incomplete, fix the document structure first and then continue with the scenario.