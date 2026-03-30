import importlib.util
import sys


def compute():
    print("compute() appelée")

    import time  # lazy import

    print("time importé !")

    return time.time()


print("Avant l'appel à compute()")
result = compute()
print("Résultat :", result)


def lazy_import_module(module_name: str):
    spec = importlib.util.find_spec(module_name)
    if spec is None or spec.loader is None:
        raise ModuleNotFoundError(f"Module introuvable: {module_name}")

    loader = importlib.util.LazyLoader(spec.loader)
    spec.loader = loader

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    loader.exec_module(module)
    return module

# Déclaration d’un module lazy
json = lazy_import_module("json")

print(">>> Le module json n'est PAS encore importé")

# Toujours pas importé ici
print("Type de json :", type(json))

# Le module est importé SEULEMENT maintenant
print(">>> Appel à json.dumps → import réel")
print(json.dumps({"a": 1}))
