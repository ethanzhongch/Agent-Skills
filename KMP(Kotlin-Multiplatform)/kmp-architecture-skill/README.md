# KMP Architecture Skill

A sophisticated scaffolding tool and set of base classes for KMP projects following MVVM, MVI, and Clean Architecture patterns.

## Features
- **Base Classes**: Provided implementations for `BaseViewModel` (MVVM) and `MviViewModel` (MVI).
- **Feature Generator**: CLI tool to bootstrap new features with correct layer separation.
- **DI Support**: Automatic Koin module generation.
- **Test Templates**: Optional generation of unit test boilerplates.

## Usage
1. Copy base classes from `resources/base` to your project's `base` package.
2. **Initialize `AppLogger`** in your main entry point (e.g., `App.kt`):
   ```kotlin
   @Composable
   fun App() {
       remember { AppLogger.init() }
       // ...
   }
   ```
3. Generate a new feature:
```bash
python3 scripts/generate_feature.py Search --pattern mvi --clean --test --package com.example.app
```

### Generator Flags:
- `name`: Feature name (required).
- `--pattern`: `mvvm` or `mvi` (default: `mvvm`).
- `--clean`: Include Clean Architecture (Use Cases).
- `--test`: Generate unit test templates.
- `--package`: Your project's base package name.
