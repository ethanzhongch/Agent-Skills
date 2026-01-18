---
name: kmp-quality-standards
description: >
  Coding standards and best practices for Kotlin Multiplatform (KMP) development.
  Enforces SOLID principles, Dependency Injection (Koin), and Resource Management (Compose Resources).
---

# KMP Quality Standards

## Intent
Ensure all code generated or modified by agents adheres to high-quality software engineering standards.

## Error Handling (Consolidated)
- **Standardized Wrapping**: Use `Resource<T>` (Loading, Success, Error) for all Domain-Presentation data flows.
- **Fail-Safe Repositories**: Data layers should catch exceptions and return `Resource.Error` instead of throwing.

## Testing Standards (Optional)
- **UseCase Verification**: When using the `--test` flag, generate unit tests in `src/commonTest` following the `MockRepository` pattern.

## Async Safety (Coroutine Dispatchers)
- **Explicit Dispatchers**: Repositories and UseCases should never depend on `Dispatchers.Main`. 
- **Injection**: Prefer injecting a `CoroutineDispatcher` via Koin to facilitate testing.

## Standardized Logging (AppLogger Wrapper)
- **Zero Third-Party Direct Usage**: Never use `Napier` or `Kermit` directly in ViewModels or Repositories.
- **Mandatory Wrapper**: All logging must go through the project's `AppLogger` abstraction.
- **Mandatory Initialization**: `AppLogger.init()` MUST be called exactly once in the application's entry point (e.g., `App.kt` or platform-specific `Main`) before any logging occurs.
- **Level Usage Guidelines**:
    - `AppLogger.v`: (Verbose) Use for high-frequency logs like scroll offsets or low-level network trace.
    - `AppLogger.d`: (Debug) Use for development tracing (e.g., "Navigating to home").
    - `AppLogger.i`: (Info) Use for significant business milestones (e.g., "User logged in", "Payment successful").
    - `AppLogger.w`: (Warning) Use for unexpected but recoverable conditions (e.g., "Network timeout, retrying").
    - `AppLogger.e`: (Error) Use for non-recoverable failures (e.g., "Database corruption", "API unauthorized").

## Decision Rules for Agents
- If you find a hardcoded string, extract it to `commonMain/composeResources/values/strings.xml`.
- If you find a direct repository instantiation in a ViewModel, refactor to use DI.
- Every new feature generation must include a `di` module and respect the `Resource` error handling pattern.
