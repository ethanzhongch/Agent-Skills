import os
import re

def update_toml():
    toml_path = "gradle/libs.versions.toml"
    if not os.path.exists(toml_path):
        print(f"❌ {toml_path} not found")
        return False

    with open(toml_path, "r") as f:
        content = f.read()

    sections = {
        "versions": """# >>> kmp-dependency-init skill start
kotlinx-coroutines = "1.10.1"
kotlinx-serialization = "1.8.0"
kotlinx-datetime = "0.6.1"
ktor = "3.0.3"
koin = "4.0.1"
coil = "3.0.4"
napier = "2.7.1"
# <<< kmp-dependency-init skill end""",
        "libraries": """# >>> kmp-dependency-init skill start
kotlinx-coroutines-core = { module = "org.jetbrains.kotlinx:kotlinx-coroutines-core", version.ref = "kotlinx-coroutines" }
kotlinx-serialization-json = { module = "org.jetbrains.kotlinx:kotlinx-serialization-json", version.ref = "kotlinx-serialization" }
kotlinx-datetime = { module = "org.jetbrains.kotlinx:kotlinx-datetime", version.ref = "kotlinx-datetime" }
ktor-client-core = { module = "io.ktor:ktor-client-core", version.ref = "ktor" }
ktor-client-content-negotiation = { module = "io.ktor:ktor-client-content-negotiation", version.ref = "ktor" }
ktor-serialization-kotlinx-json = { module = "io.ktor:ktor-serialization-kotlinx-json", version.ref = "ktor" }
koin-core = { module = "io.insert-koin:koin-core", version.ref = "koin" }
koin-compose = { module = "io.insert-koin:koin-compose", version.ref = "koin" }
koin-compose-viewmodel = { module = "io.insert-koin:koin-compose-viewmodel", version.ref = "koin" }
coil-compose = { module = "io.coil-kt.coil3:coil-compose", version.ref = "coil" }
coil-network-ktor = { module = "io.coil-kt.coil3:coil-network-ktor3", version.ref = "coil" }
napier = { module = "io.github.aakira:napier", version.ref = "napier" }
# <<< kmp-dependency-init skill end""",
        "plugins": """# >>> kmp-dependency-init skill start
kotlinx-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlin" }
# <<< kmp-dependency-init skill end"""
    }

    # Clean up existing managed blocks
    content = re.sub(r"# >>> kmp-dependency-init skill start.*?# <<< kmp-dependency-init skill end", "", content, flags=re.DOTALL)

    for section, snippet in sections.items():
        pattern = rf"\[{section}\]"
        if re.search(pattern, content):
            content = re.sub(pattern, f"[{section}]\n{snippet}", content)
        else:
            content += f"\n[{section}]\n{snippet}\n"

    with open(toml_path, "w") as f:
        f.write(content)
    print(f"✅ Updated {toml_path}")
    return True

def update_gradle():
    gradle_path = "composeApp/build.gradle.kts"
    if not os.path.exists(gradle_path):
        print(f"❌ {gradle_path} not found")
        return False

    with open(gradle_path, "r") as f:
        content = f.read()

    # 1. Update Plugins
    plugins_block = re.search(r"plugins \{(.*?)\}", content, re.DOTALL)
    if plugins_block:
        plugins_content = plugins_block.group(1)
        if "libs.plugins.kotlinx.serialization" not in plugins_content:
            updated_plugins = f"plugins {{{plugins_content}    alias(libs.plugins.kotlinx.serialization)\n}}"
            content = content.replace(plugins_block.group(0), updated_plugins)

    # 2. Update Dependencies
    deps_block = re.search(r"commonMain\.dependencies \{(.*?)\}", content, re.DOTALL)
    if deps_block:
        deps_content = deps_block.group(1)
        new_deps = ""
        lib_names = [
            "kotlinx.coroutines.core", "kotlinx.serialization.json", "kotlinx.datetime",
            "ktor.client.core", "ktor.client.content-negotiation", "ktor.serialization.kotlinx-json",
            "koin.core", "koin.compose", "koin.compose-viewmodel", "coil.compose", "coil.network-ktor", "napier"
        ]
        
        for lib in lib_names:
            if f"libs.{lib.replace('-', '.')}" not in deps_content:
                new_deps += f"            implementation(libs.{lib.replace('-', '.')})\n"
        
        if new_deps:
            updated_deps = f"commonMain.dependencies {{{deps_content}{new_deps}}}"
            content = content.replace(deps_block.group(0), updated_deps)

    with open(gradle_path, "w") as f:
        f.write(content)
    print(f"✅ Updated {gradle_path}")
    return True

if __name__ == "__main__":
    if update_toml() and update_gradle():
        print("🚀 KMP Dependency Initialized Successfully!")
