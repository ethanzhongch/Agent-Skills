# Agent-Skills

English | [中文版](./README_CN.md)

A curated collection of AI Agent Skills powered by the **[Agent Skills Standard](https://agentskills.io)**. These skills enable AI agents (like Antigravity, Claude Code, Cursor, and Codex) to perform complex engineering tasks with precision.

---

## 🏗 KMP (Kotlin Multiplatform) Evolution Suite

The **KMP Evolution Suite** is a set of specialized skills designed to bootstrap and maintain high-quality Kotlin Multiplatform projects.

### Core Skills:

*   **[kmp-dependency-init-skill](./KMP(Kotlin-Multiplatform)/kmp-dependency-init-skill)**: Automates the injection of essential KMP dependencies (Koin, Ktor, Coroutines, etc.).
*   **[kmp-architecture-skill](./KMP(Kotlin-Multiplatform)/kmp-architecture-skill)**: A scaffolding engine that generates MVI/MVVM feature modules with Clean Architecture support.
*   **[kmp-quality-standards-skill](./KMP(Kotlin-Multiplatform)/kmp-quality-standards-skill)**: Enforces strict coding standards, including unified logging and async safety.

---

## 🤖 Multi-Tool Integration Guide

This repository follows the official Agent Skills specification, making it compatible with the following tools:

### [Antigravity](https://antigravity.google/docs/skills)
- **Global**: Copy skill folders to `~/.antigravity/skills/`
- **Project**: Copy skill folders to `.antigravity/skills/` in your project root.
- **Activation**: The agent automatically discovers skills and uses them when instructions match your request.

### [Claude Code](https://code.claude.com/docs/en/skills)
- **Global**: Copy skill folders to `~/.claude/skills/`
- **Project**: Copy skill folders to `.claude/skills/` in your project root.
- **Activation**: Claude will identify and load the skills from these directories during startup.

### [Cursor](https://cursor.com/docs/cn/context/skills)
- **Global**: Copy skill folders to `~/.cursor/skills/`
- **Project**: Copy skill folders to `.cursor/skills/` in your project root.
- **Activation**: Cursor's Chat and Composer agents will utilize the `SKILL.md` instructions when relevant to your task.

### [Codex](https://developers.openai.com/codex/skills/)
- **Global**: Copy skill folders to `~/.codex/skills/`
- **Project**: Copy skill folders to `.codex/skills/` in your project root.
- **Activation**: Codex automatically loads skills at startup. Use the `/skills` command in Codex to manage them.

---

## 🛠 Manual Installation

To install a specific skill, simply clone this repo and copy the desired skill folder to your agent's skill directory:

```bash
# Example for installing kmp-architecture-skill to Claude Code globally
mkdir -p ~/.claude/skills/
cp -r ./KMP(Kotlin-Multiplatform)/kmp-architecture-skill ~/.claude/skills/
```

---
*Created and maintained by [Ethan](https://github.com/ethanzhongch).*
