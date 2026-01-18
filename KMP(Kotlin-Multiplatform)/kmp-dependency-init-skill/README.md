# KMP Dependency Init Skill

Quickly adds a set of essential, industry-standard KMP dependencies to your project.

## Dependencies Included:
- **Networking**: Ktor
- **DI**: Koin
- **Concurrency**: Kotlinx Coroutines
- **Serialization**: Kotlinx Serialization
- **Date/Time**: Kotlinx Datetime
- **Image Loading**: Coil
- **Logging**: Napier

## Usage
Run the initialization script from the project root:
```bash
python3 scripts/init_dependencies.py
```
This script modifies `gradle/libs.versions.toml` and `composeApp/build.gradle.kts` using managed blocks.
