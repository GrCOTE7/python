import inspect
from tools import *

# from sub_tools import pf

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
    numbers1 = set(random.sample(range(1, 10), 9))
    print(numbers1)
    numbers2 = tuple(random.sample(range(1, 10), 9))
    print(numbers2)
    # Pas uniques
    numbers3 = tuple(random.choices(range(1, 10), k=9))
    print(numbers3)
    print("-" * cliWR)

    
    ls()

    # print(auto_partition(range(1, 10), 9))

    # pf(
    #     "age,name,price,is_active,fruits,coordonnees,person,numbers,numbers1,numbers2,numbers3,response,my_car"
    # )

    exit()
