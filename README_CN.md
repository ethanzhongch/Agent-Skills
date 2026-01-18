# Agent-Skills

[English](./README.md) | 中文版

由 **[Agent Skills Standard](https://agentskills.io)** 驱动的 AI Agent 技能精选集。这些技能赋予 AI Agent（如 Antigravity, Claude Code, Cursor, 和 Codex）执行复杂工程任务的精准能力。

---

## 🏗 KMP (Kotlin Multiplatform) 进化套件

**KMP Evolution Suite** 是一套专门为初始化和维护高质量 Kotlin Multiplatform 项目设计的专业技能集。它专注于架构完整性、依赖管理和生产级编码标准。

### 核心技能：

*   **[kmp-dependency-init-skill](./KMP(Kotlin-Multiplatform)/kmp-dependency-init-skill)**: 自动将核心 KMP 依赖（Koin, Ktor, Coroutines 等）注入到 `libs.versions.toml` 和 `build.gradle.kts` 中。
*   **[kmp-architecture-skill](./KMP(Kotlin-Multiplatform)/kmp-architecture-skill)**: 架构脚手架引擎，支持生成带有 Clean Architecture 的 MVI/MVVM 功能模块及标准基类。
*   **[kmp-quality-standards-skill](./KMP(Kotlin-Multiplatform)/kmp-quality-standards-skill)**: 强制执行严格的编码标准，包括通过 `AppLogger` 实现的统一日志规范、依赖倒置和异步安全。

---

## 🤖 多工具集成指南

本仓库遵循官方 Agent Skills 规范，兼容以下主流 AI 开发工具：

### [Antigravity](https://antigravity.google/docs/skills)
- **全局安装**: 将技能文件夹复制到 `~/.antigravity/skills/`
- **项目安装**: 将技能文件夹复制到项目根目录下的 `.antigravity/skills/`
- **激活**: Agent 会自动发现技能，并在指令与说明匹配时自动调用。

### [Claude Code](https://code.claude.com/docs/en/skills)
- **全局安装**: 将技能文件夹复制到 `~/.claude/skills/`
- **项目安装**: 将技能文件夹复制到项目根目录下的 `.claude/skills/`
- **激活**: Claude 在启动时会自动识别并加载这些目录下的技能。

### [Cursor](https://cursor.com/docs/cn/context/skills)
- **全局安装**: 将技能文件夹复制到 `~/.cursor/skills/`
- **项目安装**: 将技能文件夹复制到项目根目录下的 `.cursor/skills/`
- **激活**: Cursor 的 Chat 和 Composer 机器人会在任务相关时利用 `SKILL.md` 中的指令。

### [Codex](https://developers.openai.com/codex/skills/)
- **全局安装**: 将技能文件夹复制到 `~/.codex/skills/`
- **项目安装**: 将技能文件夹复制到项目根目录下的 `.codex/skills/`
- **激活**: Codex 启动时自动加载。使用 `/skills` 命令可以查看和管理。

---

## 🛠 手动安装示例

要安装特定技能，只需克隆本仓库并将对应文件夹复制到 Agent 的技能目录中：

```bash
# 以全局安装 kmp-architecture-skill 到 Claude Code 为例
mkdir -p ~/.claude/skills/
cp -r ./KMP(Kotlin-Multiplatform)/kmp-architecture-skill ~/.claude/skills/
```

---
*由 [Ethan](https://github.com/ethanzhongch) 创建并维护。*
