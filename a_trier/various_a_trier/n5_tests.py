from pyparsing import C
from tabulate import tabulate
import sys

sys.path.append("c:/laragon/www/PYTHON/python/tools/")
from globals import *
from main_tools import *
from width_tests import auto_partition

if __name__ == "__main__":

    cls("Les 5 nombres - Tests")
    from itertools import combinations, permutations, product

    def apply_operations(numbers, operations, nb):
        """Applique les opérations sur la liste de nombres et calcule le résultat."""
        expression = str(numbers[0])
        result = numbers[0]

        for i in range(4):  # Il y a 4 opérations entre 5 nombres
            op = operations[i]
            num = numbers[i + 1]
            if op == "+":
                result += num
            elif op == "-":
                result -= num
            elif op == "*":
                result *= num
            elif op == "/" and num != 0:
                result /= num
            expression += f" {op} {num}"

        return result, expression

    def find_expression(target, numbers):
        """Teste toutes les permutations et combinaisons d'opérations pour atteindre le target."""
        operators = ["+", "-", "*", "/"]
        nb = 0

        for nums in permutations(numbers):  # Toutes les permutations des nombres
            for ops in product(
                operators, repeat=4
            ):  # Toutes les combinaisons possibles de 4 opérateurs
                nb += 1
                result, expression = apply_operations(nums, ops, nb)
                if result == target:
                    # print(f"{nf(nb, 0): >5}")
                    results.append((expression, f"{nf(nb, 0): >5}"))
        return results
        # return "Aucune solution trouvée."

    #
    # Données
    ns = [2, 3, 6, 8, 9]
    target = 26
    results = []

    # Recherche de solution
    solutions = find_expression(target, ns)

    if solutions:
        print("15 premières solution(s) trouvée(s) :")
        tbl(solutions[:15], indexes=1, colalign=("right", "center", "right"))
    else:
        print("Aucune solution trouvée.")
    exit()
    solutions = [1, 2, 3]
    # for index, (expr, s) in enumerate(solutions):
    #     print(f"# {index: >3} - {nf(s,0): >7} : {expr}")
    # solutions = solutions[10:16]
    exit()
    ls()

    # res = list(enumerate(combinations("ABCD", 2)))
    headers = ["#", "Combinaison"]

    res = enumerate(list(combinations("ABCD", 2)))
    tbl(res, headers=headers)

    sl(french)
    res = list(enumerate(["".join(pair) for pair in combinations("ABCD", 2)]))
    tbl(res, headers=headers)
    sl(french)

    tbl(
        [[r] for r in ["".join(pair) for pair in (combinations("ABCD", 2))]],
        headers=headers,
        indexes=1,
    ),

    ls()

    arr = [21, 12, 31]
    print(arr)
    print(*arr)
    print(", ".join(map(str, arr)))
    print(*enumerate(arr))
    for i, v in enumerate(arr):
        print(f"Index: {i}, Valeur: {v}")

    exit()
