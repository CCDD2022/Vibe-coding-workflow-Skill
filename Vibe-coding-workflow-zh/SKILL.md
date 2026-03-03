---
name: Vibe-coding-workflow-zh
description: 面向非技术用户的代码交付 Skill。覆盖从零开发、基于已有代码开发和 Debug 三种场景，强制先文档化再编码，并要求事后回填核心文档。
compatibility: 适用于支持 Agent Skills 的编程代理环境；需要具备文件读写与脚本执行能力。
metadata:
  author: CCDD2022
  version: "1.1"
---

# 通用编码交付 Skill（可执行版）

## 目标

让不懂代码的用户，也能通过标准流程产出可交付代码，并保证过程可追溯、结果可验证。

## 支持场景

支持 3 个场景：

1. 从零开始写代码
2. 基于已有代码写代码
3. 出错 Debug

## 激活条件（何时使用）

- 需要将业务需求转化为可交付代码，并要求过程可追溯、结果可验收。
- 任务需要按标准流程推进，且每个阶段必须具备明确输入、输出与门禁条件。
- 期望在开发或修复完成后，同步沉淀规范与经验（更新 `rules.md`）。

## 不适用场景

- 仅需一次性临时脚本或演示代码，且不要求交付物、验收与文档留痕。
- 明确拒绝需求澄清、计划确认、过程记录或验收标准。
- 任务目标与核心文档体系（`goal.md` / `plan.md` / `rules.md` / `structure.md`）无关。

## 总逻辑（全场景通用）

0. 先执行前置脚本 `scripts/ensure_core_docs.py`，确保核心文档存在：

   - `goal.md`（总项目目标）
   - `plan.md`（实施计划）
   - `rules.md`（编码规范）
   - `structure.md`（项目架构）

1. 在做任何事之前，先阅读以上 4 个核心文档。
2. 选择场景（从零开发 / 基于已有代码开发 / Debug）。
3. 严格按场景流程执行；未通过当前门禁，不进入下一步。
4. 做任何事之后，如发现文档与事实不一致，立即更新文档。
5. 输出交付包（结果、证据、风险、后续建议）。

## 场景路由

- 没有可用代码基础：使用 [references/scenario-01-from-scratch.md](references/scenario-01-from-scratch.md)
- 已有代码，需要新增需求：使用 [references/scenario-02-from-existing-code.md](references/scenario-02-from-existing-code.md)
- 已有报错/异常，需要排查修复：使用 [references/scenario-03-debug.md](references/scenario-03-debug.md)

## 统一输出格式（每次任务都要给）

1. 目标摘要（本次要达成什么）
2. 执行记录（做了哪些步骤）
3. 结果证据（如何证明完成）
4. 风险与限制（当前不能解决什么）
5. 文档更新（更新了哪些核心文档）
6. 下一步建议（下一轮怎么做）

## 全局质量门禁

- `goal.md` 与当前任务目标一致。
- `plan.md` 有可执行步骤与验收点。
- `rules.md` 能覆盖本次编码/修复关键规范。
- `structure.md` 与当前项目结构一致或已更新。
- 交付结果可复现，且有验证证据。

## 场景文档

- [references/scenario-01-from-scratch.md](references/scenario-01-from-scratch.md)
- [references/scenario-02-from-existing-code.md](references/scenario-02-from-existing-code.md)
- [references/scenario-03-debug.md](references/scenario-03-debug.md)

## 前置脚本

- [scripts/ensure_core_docs.py](scripts/ensure_core_docs.py)

  - 用途：检查并补齐 `goal.md`、`plan.md`、`rules.md`、`structure.md`
  - 输入参数：`--project-root`（可选，默认当前目录）
  - 输出结果：每个文档状态（EXISTS / CREATED）

## 快速开始

1. 运行前置脚本，补齐核心文档。
2. 读完 4 个核心文档。
3. 选择场景并执行。
4. 任务完成后更新文档并输出交付包。


## 边界与异常处理

- 当用户需求含糊不清时：先澄清，拒绝直接编码。
- 当核心文档缺失时：先补齐文档，再进入场景流程。
- 当 `plan.md` 未确认时：不得开始编码或改动代码。
- 当修复存在高风险时：必须先给回滚方案，再实施变更。

