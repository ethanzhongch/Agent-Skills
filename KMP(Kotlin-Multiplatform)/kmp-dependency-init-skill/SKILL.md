---
name: kmp-dependency-init
description: >
  Initialize common industry-standard dependencies for a Kotlin Multiplatform (KMP) project.
  Automates the setup of Ktor, Koin, Coroutines, Serialization, and more by updating
  libs.versions.toml and build.gradle.kts with best-practice configurations.
---

# KMP Dependency Initialization

## Intent
Provide a repeatable way to bootstrap a KMP project with essential libraries:
1) **Networking**: Ktor
2) **Dependency Injection**: Koin
3) **Concurrency**: Coroutines
4) **Data Handling**: Serialization, DateTime
5) **UI Utilities**: Coil (Multiplatform), Lifecycle
6) **Logging**: Napier

## Inputs
- **Target path (optional)**: Project root directory. Default: current working directory.
- **Behavior flags (optional)**:
  - `--all`: Install all common libraries (default).
  - `--minimal`: Install only Coroutines and Serialization.

## Workflow
1) **Detect project root** and verify presence of `libs.versions.toml` and `build.gradle.kts`.
2) **Inject Managed Blocks** into `libs.versions.toml`:
   - `[versions]` section
   - `[libraries]` section
   - `[plugins]` section
3) **Update `composeApp/build.gradle.kts`**:
   - Apply `kotlinx-serialization` plugin.
   - Inject dependency calls into `commonMain`.
4) **Validation**: Ensure the project still syncs and builds.

## Managed Markers
The skill uses the following markers to ensure idempotency:
- `# >>> kmp-dependency-init skill start`
- `# <<< kmp-dependency-init skill end`

## How to Run
```bash
bash scripts/init_dependencies.sh
```
