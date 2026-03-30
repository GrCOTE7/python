# import flet as ft
# from pymox_kit import cls, end


def lists_sample() -> None:
    # Listes en compréhension
    # C’est une syntaxe spéciale pour construire des listes de manière concise et expressive.
    #
    #  - On peut filtrer les éléments avec une condition (if).
    #  - On peut faire des transformations sur les éléments (expression).
    #  - C’est souvent plus lisible que les boucles for classiques pour créer des listes.
    #
    # Donc ici, “comprehension” veut dire : “on utilise la syntaxe de compréhension pour construire des listes facilement”.

    squares = [x**2 for x in range(10) if x % 2 == 0]
    print("Squares of even numbers from 0 to 9:", squares, end="\n" * 2)

    lists = [[1, 2], [3, 4], [5]]
    flat = [x for L in lists for x in L]
    print("Flat list:", flat)
    print("New way (v3.15):", [*L for L in lists], end="\n" * 2)  # only Py 3.15

    sets = [{1, 2}, {3, 4}, {5}]
    print("Flat set 1:", {num for subset in sets for num in subset})
    print("Flat set 2:", [*subset for subset in sets], end="\n" * 2)  # only Py 3.15

    dicts = [{"a": 1}, {"b": 2}, {"a": 3}]
    print("Flat dict 1:", {k: v for d in dicts for k, v in d.items()})
    print("Flat dict 2:", {**d for d in dicts}, end="\n" * 2)  # only Py 3.15

    # Aussi avec generator


def main() -> None:

    print("Liste avec comprehension avec Py 315")
    lists_sample()


if __name__ == "__main__":

    # cls()
    main()
    # end()
