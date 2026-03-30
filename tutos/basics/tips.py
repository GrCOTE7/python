import flet as ft
from pymox_kit import cls, end


















def main():

    print("Tips en 2026\n")

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

    names: list[str] = ["Alice", "Bob", "Charlie"]
    # for i, name in enumerate(names, start=1):
    print(*(f"{i}. {name}" for i, name in enumerate(names, start=1)), sep='\n', end='.\n\n')
    print(*names, sep=', ', end='.\n')
    





if __name__ == "__main__":
    cls()
    main()
    end()
















