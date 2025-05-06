import inspect
from tools import cls, cliWR, sb, eb, tbl, exit

if __name__ == "__main__":
    cls()

    class Car:
        def __init__(self, brand, color):
            self.brand = brand
            self.color = color

        def start(self):
            print(f"La {self.brand} démarre !")

        def __repr__(self):
            """Return a readable representation of the Car object"""
            return f"Car(brand='{self.brand}', color='{self.color}')"

    def get_var_infos(var_name):
        """Retrieve variable type and value from the current global or local scope."""
        for scope in (globals(), locals()):  # Parcourir global et local
            if var_name in scope:
                value = scope[var_name]
                return (
                    var_name,
                    (
                        type(value).__name__
                        if not hasattr(value, "__dict__")
                        else "object"
                    ),
                    value,
                )
        return f"Error: Variable '{var_name}' not found."

    age = 25  # Un entier
    price = 19.99  # Un flottant
    name = "Alice"
    is_active = True
    fruits = ["Pomme", "Banane", "Cerise"]
    coordonnees = (45.678, -3.456)
    person = {"nom": "Alice", "âge": 25}
    numbers = {1, 2, 3, 4, 4, 2}  # Les doublons sont supprimés

    # Création d'un objet
    my_car = Car("Toyota", "bleu")

    # Utilisation des attributs et méthodes
    print(my_car.brand, my_car.color)  # Affiche "rouge"
    my_car.start()  # Affiche "La Toyota démarre !"

    response = None
    headers = ["varName", "varType", "varValue"]
    vars = [
        "age",
        "name",
        "price",
        "is_active",
        "fruits",
        "coordonnees",
        "person",
        "numbers",
        "response",
        "my_car",
    ]

    data = []
    for var in vars:
        data.append(list(get_var_infos(var)))
    print(data)
    print("-" * cliWR)

    import random

    # uniques et ordonnée
    numbers = set(random.sample(range(1, 10), 9))
    print(numbers)
    numbers = tuple(random.sample(range(1, 10), 9))
    print(numbers)
    # Pas uniques
    numbers = tuple(random.choices(range(1, 10), k=9))
    print(numbers)
    print("-" * cliWR)

    def auto_partition(data, L):
        """Découpe la liste 'data' en sous-groupes en fonction de L."""
        partitions = []
        index = 0
        sizes = []

        # Génération dynamique des tailles de groupe en fonction de L
        while sum(sizes) < L:
            next_size = 3 if len(sizes) % 3 == 0 else (1 if len(sizes) % 3 == 1 else 2)
            if sum(sizes) + next_size > L:
                next_size = L - sum(sizes)  # Ajuster pour ne pas dépasser L
            sizes.append(next_size)

        # Découpage des éléments selon les tailles calculées
        for size in sizes:
            partitions.append(tuple(data[index : index + size]))
            index += size

        return partitions


    print()

    exit()
