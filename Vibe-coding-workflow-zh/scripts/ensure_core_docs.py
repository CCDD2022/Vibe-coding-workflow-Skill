from __future__ import annotations

import argparse
from pathlib import Path


DOC_TEMPLATES: dict[str, str] = {
    "goal.md": """# 项目总目标（Goal）

## 项目背景
- 业务场景：
- 目标用户：

## 总目标
- 

## 成功标准
- 功能成功标准：
- 质量成功标准：

## 范围边界（做 / 不做）
- 做：
- 不做：

## 约束条件
- 技术约束：
- 时间约束：
""",
    "plan.md": """# 实施计划（Plan）

## 里程碑
1. 里程碑 1：
2. 里程碑 2：
3. 里程碑 3：

## 任务拆解
- 任务 1：目标 / 输入 / 输出 / 负责人
- 任务 2：目标 / 输入 / 输出 / 负责人
- 任务 3：目标 / 输入 / 输出 / 负责人

## 验收节点
- 验收点 1：
- 验收点 2：

## 风险与回滚
- 风险：
- 回滚策略：
""",
    "rules.md": """# 编码规范（Rules）

## 默认规则（创建即生效）
- 程序设计要分层（如：接口层 / 业务层 / 数据访问层），避免把业务逻辑堆在入口文件。
- 配置信息要放在统一位置（如 `config` 模块或配置文件），禁止在代码中散落硬编码。
- 关键流程必须有明确错误处理，禁止静默吞错。
- 对外输入必须先校验（参数、文件、请求体），再进入业务逻辑。
- 函数保持单一职责，复杂函数应拆分为小函数。
- 变更前先确认范围，变更后必须有最小可复现验证。

## 命名规范
- 使用有语义的命名，禁止 `tmp`、`test1` 等无意义命名进入正式代码。

## 代码风格
- 保持一致的格式化风格；优先小函数、低耦合。

## 错误处理
- 错误信息应可定位（包含上下文），并返回明确失败状态。

## 日志与注释
- 日志记录关键路径；注释写“为什么”，不重复“做了什么”。

## 安全与隐私
- 禁止提交密钥、令牌、密码等敏感信息。

## 测试与回归要求
- 至少覆盖主流程与一个失败分支。

## 禁止事项（反模式）
- 禁止跨层直接调用导致耦合失控。
""",
    "structure.md": """# 项目架构（Structure）

## 目录结构
- 根目录：

## 模块划分
- 

## 数据流/调用关系
- 

## 依赖与外部接口
- 

## 关键入口文件
- 

## 高风险模块
- 
""",
}

REQUIRED_SECTIONS: dict[str, tuple[str, ...]] = {
    "goal.md": (
        "## 项目背景",
        "## 总目标",
        "## 成功标准",
        "## 范围边界（做 / 不做）",
        "## 约束条件",
    ),
    "plan.md": (
        "## 里程碑",
        "## 任务拆解",
        "## 验收节点",
        "## 风险与回滚",
    ),
    "rules.md": (
        "## 默认规则（创建即生效）",
        "## 命名规范",
        "## 代码风格",
        "## 错误处理",
        "## 日志与注释",
        "## 安全与隐私",
        "## 测试与回归要求",
        "## 禁止事项（反模式）",
    ),
    "structure.md": (
        "## 目录结构",
        "## 模块划分",
        "## 数据流/调用关系",
        "## 依赖与外部接口",
        "## 关键入口文件",
        "## 高风险模块",
    ),
}

PLACEHOLDER_HINTS: dict[str, tuple[str, ...]] = {
    "goal.md": ("- 业务场景：", "- 目标用户：", "- 功能成功标准："),
    "plan.md": ("里程碑 1：", "- 任务 1：目标 / 输入 / 输出 / 负责人", "- 风险："),
    "rules.md": ("## 默认规则（创建即生效）",),
    "structure.md": ("- 根目录：", "## 模块划分"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="检查并补齐核心文档：goal.md、plan.md、rules.md、structure.md"
    )
    parser.add_argument(
        "--project-root",
        default=".",
        help="项目根目录（默认：当前目录）",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="仅检查文档状态，不创建缺失文件",
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
        warnings.append("文档仍为默认模板，尚未填入任务信息")

    if "    ##" in content:
        warnings.append("存在缩进标题，Markdown 渲染可能异常")

    hint_hits = sum(1 for hint in PLACEHOLDER_HINTS[name] if hint in content)
    if hint_hits == len(PLACEHOLDER_HINTS[name]):
        warnings.append("关键占位内容尚未替换")

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
