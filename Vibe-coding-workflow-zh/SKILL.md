---
name: Vibe-coding-workflow-zh
description: 面向非技术用户的代码交付 Skill。覆盖从零开发、基于已有代码开发和 Debug 三种场景，强调先澄清、再计划、后实施，并按任务风险采用分级门禁与文档回填。
compatibility: 适用于支持 Agent Skills 的编程代理环境；需要具备文件读写与脚本执行能力。
metadata:
  author: CCDD2022
  version: "1.2"
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
- 任务涉及多文件改动、已有系统影响分析、缺陷定位修复，或需要沉淀过程文档。

## 不适用场景

- 仅需一次性临时脚本或演示代码，且不要求交付物、验收与文档留痕。
- 明确拒绝需求澄清、计划确认、过程记录或验收标准。
- 任务目标与核心文档体系（`docs/goal.md` / `docs/plan.md` / `docs/rules.md` / `docs/structure.md`）无关。

## 门禁等级（按任务风险选择）

- L1 轻量任务：单文件、小范围、低风险修改。允许先写简版 `plan.md` 再实施；若用户已明确要求直接修改，可在说明计划后直接开工。
- L2 标准任务：多文件需求、常规缺陷修复、需要阅读调用链。必须先形成可执行 `plan.md`，再开始正式改动。
- L3 高风险任务：涉及架构调整、数据库、外部接口、权限、安全、回滚风险。必须先确认目标、计划、风险与回滚方案，再实施变更。

选择规则：

- 无法快速证明“低风险”时，默认按 L2 执行。
- 只允许在 L1 下跳过显式确认；L2/L3 不允许跳过。
- 任何任务只要进入高风险区域，立即从 L1/L2 升级到 L3。

## 总逻辑（全场景通用）

0. 先执行前置脚本 `scripts/ensure_core_docs.py`，在项目根目录创建 `docs/` 并检查核心文档结构是否完整：

  - `docs/goal.md`（总项目目标）
  - `docs/plan.md`（实施计划）
  - `docs/rules.md`（编码规范）
  - `docs/structure.md`（项目架构）

1. 在做任何事之前，先阅读以上 4 个核心文档，并判断哪些文档需要补齐或更新。
2. 选择场景（从零开发 / 基于已有代码开发 / Debug）与门禁等级（L1 / L2 / L3）。
3. 先完成需求澄清、范围判断、计划编写，再进入正式实现；未通过当前门禁，不进入下一步。
4. 如需做探索性工作，只允许进行只读分析、最小复现或不落盘验证；未经允许，不直接提交正式代码改动。
5. 做任何事之后，如发现文档与事实不一致，按“文档更新策略”回填。
6. 输出交付包（结果、证据、风险、后续建议）。

## 文档更新策略

- `docs/goal.md`：仅在任务目标、范围边界、用户对象、完成定义发生变化时更新。
- `docs/plan.md`：在进入 L2/L3、计划发生偏移、修复方案改变、验收方式调整时更新。
- `docs/rules.md`：仅在本次任务沉淀出可复用的新规则、禁用写法或检查项时更新；不要记录一次性细节。
- `docs/structure.md`：仅在模块边界、目录结构、调用关系、关键入口、高风险模块发生变化时更新。

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

- `docs/goal.md` 与当前任务目标一致，且做 / 不做边界清晰。
- `docs/plan.md` 至少包含步骤、影响范围、验证方式、风险或回滚说明。
- `docs/rules.md` 能覆盖本次编码/修复关键规范；若无新增通用规则，可明确写“本次无需更新”。
- `docs/structure.md` 与当前项目结构一致或已更新；若本次不涉及结构变化，可明确标注“无变化”。
- 交付结果可复现，且至少包含 1 条验证证据（命令、截图、日志、测试结果、输入输出样例其一）。
- 输出必须能回答 3 个问题：改了什么、怎么证明、还有什么风险。

## 场景文档

- [references/scenario-01-from-scratch.md](references/scenario-01-from-scratch.md)
- [references/scenario-02-from-existing-code.md](references/scenario-02-from-existing-code.md)
- [references/scenario-03-debug.md](references/scenario-03-debug.md)

## 前置脚本

- [scripts/ensure_core_docs.py](scripts/ensure_core_docs.py)

  - 用途：在项目根目录创建 `docs/`，并检查 `docs/goal.md`、`docs/plan.md`、`docs/rules.md`、`docs/structure.md` 是否存在且包含必需章节。
  - 输入参数：`--project-root`（可选，默认当前目录）、`--check-only`（仅检查，不创建缺失文件）
  - 输出结果：每个文档状态（EXISTS / CREATED / MISSING / INVALID / WARN）

## 快速开始

1. 运行前置脚本，补齐核心文档。
2. 读完 4 个核心文档，并判断当前任务属于 L1 / L2 / L3。
3. 选择场景并执行。
4. 任务完成后按需更新文档并输出交付包。


## 边界与异常处理

- 当用户需求含糊不清时：先澄清，拒绝直接编码。
- 当核心文档缺失时：先补齐文档，再进入场景流程。
- 当 `docs/plan.md` 未确认时：L2/L3 不得开始正式编码；L1 仅允许最小范围实施，并在输出中补齐计划与验证。
- 当修复存在高风险时：必须先给回滚方案，再实施变更。
- 当现有文档结构不完整时：先修正文档结构，再判断是否进入具体场景。

