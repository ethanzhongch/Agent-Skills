import os
import sys
import argparse

def generate_feature(name, pattern, clean, include_test, package):
    pkg_path = package.replace('.', '/')
    base_path = f"composeApp/src/commonMain/kotlin/{pkg_path}/features/{name.lower()}"
    test_path = f"composeApp/src/commonTest/kotlin/{pkg_path}/features/{name.lower()}"
    
    os.makedirs(os.path.join(base_path, "presentation"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "domain"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "domain", "usecase") if clean else base_path, exist_ok=True)
    os.makedirs(os.path.join(base_path, "data"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "di"), exist_ok=True)

    package_name = f"{package}.features.{name.lower()}"
    
    # 1. DI Layer (Koin)
    with open(os.path.join(base_path, "di", f"{name}Module.kt"), "w") as f:
        f.write(f"package {package_name}.di\n\n")
        f.write(f"import org.koin.dsl.module\n")
        f.write(f"import org.koin.core.module.dsl.factoryOf\n")
        f.write(f"import org.koin.core.module.dsl.viewModelOf\n")
        f.write(f"import kotlinx.coroutines.Dispatchers\n")
        f.write(f"import {package_name}.presentation.{name}ViewModel\n")
        f.write(f"import {package_name}.domain.{name}Repository\n")
        f.write(f"import {package_name}.data.{name}RepositoryImpl\n")
        if clean:
            f.write(f"import {package_name}.domain.usecase.Get{name}UseCase\n")
        
        f.write(f"\nval {name.lower()}Module = module {{\n")
        f.write(f"    single {{ Dispatchers.Default }}\n")
        f.write(f"    single<{name}Repository> {{ {name}RepositoryImpl(get()) }}\n")
        if clean:
            f.write(f"    factoryOf(::Get{name}UseCase)\n")
            f.write(f"    viewModelOf(::{name}ViewModel)\n")
        else:
            f.write(f"    viewModelOf(::{name}ViewModel)\n")
        f.write(f"}}\n")

    # 2. Presentation Layer
    if pattern == "mvi":
        with open(os.path.join(base_path, "presentation", f"{name}Contract.kt"), "w") as f:
            f.write(f"package {package_name}.presentation\n\n")
            f.write(f"import {package}.base.Resource\n\n")
            f.write(f"data class {name}State(\n")
            f.write(f"    val data: Resource<Any> = Resource.Loading\n")
            f.write(f")\n\n")
            f.write(f"sealed class {name}Intent {{\n")
            f.write(f"    object LoadData : {name}Intent()\n")
            f.write(f"}}\n\n")
            f.write(f"sealed class {name}Effect {{\n")
            f.write(f"    data class ShowError(val message: String) : {name}Effect()\n")
            f.write(f"}}\n")
        
        with open(os.path.join(base_path, "presentation", f"{name}ViewModel.kt"), "w") as f:
            f.write(f"package {package_name}.presentation\n\n")
            f.write(f"import {package}.base.MviViewModel\n")
            f.write(f"import {package}.base.Resource\n")
            f.write(f"import {package}.base.AppLogger\n")
            if clean:
                f.write(f"import {package_name}.domain.usecase.Get{name}UseCase\n")
            
            f.write(f"\nclass {name}ViewModel(\n")
            if clean:
                f.write(f"    private val get{name}UseCase: Get{name}UseCase\n")
            else:
                f.write(f"    private val repository: {name}Repository\n")
            f.write(f") : MviViewModel<{name}State, {name}Intent, {name}Effect>({name}State()) {{\n\n")
            f.write(f"    override fun onIntent(intent: {name}Intent) {{\n")
            f.write(f"        when (intent) {{\n")
            f.write(f"            is {name}Intent.LoadData -> loadData()\n")
            f.write(f"        }}\n")
            f.write(f"    }}\n\n")
            f.write(f"    private fun loadData() {{\n")
            f.write(f"        AppLogger.d(\"Loading {name} data\")\n")
            f.write(f"    }}\n")
            f.write(f"}}\n")
    else: # MVVM
        with open(os.path.join(base_path, "presentation", f"{name}State.kt"), "w") as f:
            f.write(f"package {package_name}.presentation\n\n")
            f.write(f"import {package}.base.Resource\n\n")
            f.write(f"data class {name}State(\n")
            f.write(f"    val result: Resource<Any> = Resource.Loading\n")
            f.write(f")\n")
            
        with open(os.path.join(base_path, "presentation", f"{name}ViewModel.kt"), "w") as f:
            f.write(f"package {package_name}.presentation\n\n")
            f.write(f"import {package}.base.BaseViewModel\n")
            f.write(f"import {package}.base.Resource\n")
            f.write(f"import {package}.base.AppLogger\n")
            if clean:
                f.write(f"import {package_name}.domain.usecase.Get{name}UseCase\n")
            
            f.write(f"\nclass {name}ViewModel(\n")
            if clean:
                f.write(f"    private val get{name}UseCase: Get{name}UseCase\n")
            f.write(f") : BaseViewModel<{name}State>({name}State()) {{\n\n")
            f.write(f"    fun loadData() {{\n")
            f.write(f"        AppLogger.d(\"Executing LoadData for {name}\")\n")
            f.write(f"        updateState {{ copy(result = Resource.Loading) }}\n")
            f.write(f"    }}\n")
            f.write(f"}}\n")

    # 3. Domain & Data Layer
    with open(os.path.join(base_path, "domain", f"{name}Repository.kt"), "w") as f:
        f.write(f"package {package_name}.domain\n\n")
        f.write(f"import {package}.base.Resource\n\n")
        f.write(f"interface {name}Repository {{\n")
        f.write(f"    suspend fun get{name}Data(): Resource<Any>\n")
        f.write(f"}}\n")

    with open(os.path.join(base_path, "data", f"{name}RepositoryImpl.kt"), "w") as f:
        f.write(f"package {package_name}.data\n\n")
        f.write(f"import {package_name}.domain.{name}Repository\n")
        f.write(f"import {package}.base.Resource\n")
        f.write(f"import kotlinx.coroutines.CoroutineDispatcher\n")
        f.write(f"import kotlinx.coroutines.withContext\n")
        f.write(f"import {package}.base.AppLogger\n\n")
        f.write(f"class {name}RepositoryImpl(\n")
        f.write(f"    private val dispatcher: CoroutineDispatcher\n")
        f.write(f") : {name}Repository {{\n")
        f.write(f"    override suspend fun get{name}Data(): Resource<Any> = withContext(dispatcher) {{\n")
        f.write(f"        try {{\n")
        f.write(f"            Resource.Success(Unit)\n")
        f.write(f"        }} catch (e: Exception) {{\n")
        f.write(f"            AppLogger.e(\"Failed to load {name} data\", e)\n")
        f.write(f"            Resource.Error(e.message ?: \"Unknown error\")\n")
        f.write(f"        }}\n")
        f.write(f"    }}\n")
        f.write(f"}}\n")

    if clean:
        usecase_name = f"Get{name}UseCase"
        with open(os.path.join(base_path, "domain", "usecase", f"{usecase_name}.kt"), "w") as f:
            f.write(f"package {package_name}.domain.usecase\n\n")
            f.write(f"import {package_name}.domain.{name}Repository\n")
            f.write(f"import {package}.base.Resource\n\n")
            f.write(f"class {usecase_name}(private val repository: {name}Repository) {{\n")
            f.write(f"    suspend operator fun invoke(): Resource<Any> = repository.get{name}Data()\n")
            f.write(f"}}\n")

    if include_test:
        os.makedirs(os.path.join(test_path, "domain", "usecase"), exist_ok=True)
        test_class_name = f"Get{name}UseCaseTest"
        with open(os.path.join(test_path, "domain", "usecase", f"{test_class_name}.kt"), "w") as f:
            f.write(f"package {package_name}.domain.usecase\n\n")
            f.write(f"import kotlin.test.Test\n")
            f.write(f"import kotlin.test.assertTrue\n\n")
            f.write(f"class {test_class_name} {{\n")
            f.write(f"    @Test\n")
            f.write(f"    fun `test usecase execution`() {{\n")
            f.write(f"        assertTrue(true)\n")
            f.write(f"    }}\n")
            f.write(f"}}\n")

    print(f"✅ SOLID KMP Feature '{name}' generated.")
    if include_test:
        print(f"🧪 Test templates generated at {test_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate KMP Feature')
    parser.add_argument('name', help='Feature name')
    parser.add_argument('--pattern', choices=['mvvm', 'mvi'], default='mvvm', help='Architecture pattern')
    parser.add_argument('--clean', action='store_true', help='Include Clean Architecture')
    parser.add_argument('--test', action='store_true', help='Generate unit test templates')
    parser.add_argument('--package', default='com.lite.skill', help='Base package name')
    
    args = parser.parse_args()
    generate_feature(args.name, args.pattern, args.clean, args.test, args.package)
