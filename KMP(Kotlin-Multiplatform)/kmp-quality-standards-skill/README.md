# KMP Quality Standards Skill

Enforces high-quality coding standards and best practices for Kotlin Multiplatform development.

## Standards Enforced:
- **SOLID Principles**: Mandatory dependency inversion and single responsibility.
- **Dependency Injection**: Enforces Koin module usage per feature.
- **Error Handling**: Standardized `Resource<T>` wrapping for all domain flows.
- **Async Safety**: Explicit Dispatcher management and injection.
- **Logging**: Strict `Napier` usage (forbids `println`).
- **Resource Management**: Prohibits hardcoded strings.

## How to use with agents
Link this skill to your agent to ensure all generated code complies with these industrial-grade standards.
