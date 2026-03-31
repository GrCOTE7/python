from os import name

import flet as ft
from pymox_kit import cls, end


def main():

    # print("Tips en 2026\n")

    # var: int = 123
    # print(f'{var = }') # permet d'afficher le nom de la variable et sa valeur')
    # print(f'{var = !r}') # affiche la représentation de la variable (utile pour les chaînes de caractères)')
    # print(f'{var = :.2f}') # affiche la variable avec 2 décimales (utile pour les nombres à virgule)')

    # print(f'{var = : >7}') # aligne la variable à droite sur 10')

    # # try / except / else / finally
    # a, b = 1, 0
    # try:
    #     print(f"{a} / {b} = {a / b:.2f}", end=" ")
    # except ZeroDivisionError:
    #     print("Erreur : Pas de division par zéro !")
    # else:
    #     print("(Division réussie)")
    # finally:
    #     print("Bloc finally exécuté")

    # names: list[str] = ["Alice", "Bob", "Charlie"]
    # # for i, name in enumerate(names, start=1):
    # print(
    #     *(f"{i}. {name}" for i, name in enumerate(names, start=1)),
    #     sep="\n",
    #     end=".\n\n",
    # )
    # print("Alice", "Bob", "Charlie", sep=", ", end=".\n")
    # print(*names, sep=", ", end=".\n")
    # print(f"Names: {', '.join(names)}.")

    # first, *_, last = "Pier"
    # print(first, last)
    # first, *_, last = "Pier", "Pol", "Jack"
    # print(first, last)

    # print(*"James", sep="-")

    # a: set[int] = {1, 2, 3}
    # a_ori = a.copy()
    # b: set[int] = {3, 4, 5}
    # print(f"Union : {a | b}")
    # print(f"Intersection : {a & b}")
    # a |= b
    # print(a)
    # a_ori &= b
    # print(a_ori)

    # a: dict[str, int] = {"a": 1, "b": 2}
    # b: dict[str, int] = {"b": 3, "c": 4}
    # a |= b
    # print("Dicts Union", a)

    # Automatic invoc a fct
    # @lambda _: _()
    # def setup() -> int:
    #     print("All set up!")

    # Can return a value
    # @lambda _: _()
    # def setup() -> int:
    #     print("All set up!")
    #     return 10
    # print("Setup returned:", setup)

    # a: list[int] = [1, 2]
    # a.append(a)  # a devient [1, 2, [...]] (une liste qui contient elle-même)
    # print(a)

    # names: list[str] = ["Alice", "Bob", "Charlie"]
    # for name in names[:-1]:
    #     # break
    #     print(name, sep=", ", end=" ")
    # else:
    #     print(f"and {names[-1]}")

    # print([n for n in range(3)])
    # print(list(range(3)))
    # print(*(n for n in range(3)))
    # print(*range(3))
    # print({n for n in [0, 0, 1, 1, 3, 2, 2]})
    # print({n: n**2 for n in range(3)})
    # print({k: v for k, v in [("a", 1), ("b", 2)]})
    # print({v: k for k, v in [("a", 1), ("b", 2)]})

    # point = (2,)
    # print(point)
    # point = 10, 2
    # print(point)
    # x, y = 10, 2
    # print(x, y)

    # # Surcharge d'arguments
    # settings: dict[str, str] = {"sep": ", ", "end": "!\n"}
    # names: list[str] = ["Alice", "Bob", "Charlie"]
    # print(*names, **settings)  # Rouspète mais fonctionne (car print accepte des kwargs)

    # first_three: slice = slice(0, 3, None)  # [0:3]
    # rev: slice = slice(3, None, -1)  # [3::-1]
    # names: list[str] = ["Alice", "Bob", "Charlie", "David", "Eve"]
    # print(names[first_three])  # Affiche les 3 premiers éléments de la liste
    # print(names[rev])  # Affiche les éléments de la liste en ordre inverse

    # a: int = 15
    # print(f"{a = :b}")  # Affiche a en binaire
    # print(f"{a = :x}")  # Affiche a en hexadécimal

    # a: int
    # b: int
    # c: int
    # a, b, c = 15, 10, 5
    # print(f"{a} + {b} + {c} = {a + b + c }")

    # settings: dict[str, float] = {"volume": 1.0, "brightness": 0.5}
    # print(settings["brightness"])  # Affiche la valeur associée à la clé "brightness"
    # print(settings.get("volum"))  # Pas d erreur, retourne None
    # settings["contrast"] = 0.8  # Ajoute une nouvelle clé "
    # print(settings.get("weight", 0.0))  # Default value
    # print(settings)

    # volume: float = 0.7
    # loudness: str = "LOUD" if volume > 0.6 else "silent"
    # print(f"Volume: {volume} ({loudness})")

    # a: int = 10
    # b: int = 20
    # if a < 15 < b > 0:
    #     print("in range!")

    # scores = [
    #     {"name": "Alice", "score": 85},
    #     {"name": "Bob", "score": 92},
    #     {"name": "Charlie", "score": 78},
    # ]
    # # print(max(scores)) # ERROR
    # print(max(scores, key=lambda s: s["score"]))

    # print(n := 10)
    # while user_input := input(">>>"):  # out when None
    #     print(f"You entered: {user_input}")

    def get_len(text: str) -> int:
        return len(text)

    text: str = "Hello, world!"
    length: int = get_len(text)
    print(f"Length of '{text}': {length}")


if __name__ == "__main__":
    # names: list[str] = ["Alice", "Bob", "Charlie"]
    cls()
    main()
    end()
