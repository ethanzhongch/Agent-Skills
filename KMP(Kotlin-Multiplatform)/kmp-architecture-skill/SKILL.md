---
name: kmp-architecture
description: >
  Guide and implement architectural patterns (MVVM, MVI, Clean Architecture) for KMP.
  Includes base classes, decision matrices, and code generation scripts.
---

# KMP Architecture Guide

## Intent
Standardize architecture across KMP projects to ensure maintainability and testability.

## Decision Matrix

| Metric | MVVM | MVI |
| :--- | :--- | :--- |
| **Simple States** | Recommended | Overkill |
| **Predictability** | High | Very High |
| **Boilerplate** | Low | Medium |
| **Scaling** | Good | Excellent |

## Usage
Use provided base classes from `resources/base/` or generate a new feature using `scripts/generate_feature.py`.

### Patterns
1. **Repository Pattern**: Common for most apps.
2. **Clean Architecture**: Use for complex business logic (Domain layer + UseCases).

## Directory Structure
```
feature/
├── data/           # Repository implementations, Data Sources
├── domain/         # Use Cases, Repository Interfaces, Models
└── presentation/   # ViewModels, UI States (and Intents for MVI)
```
