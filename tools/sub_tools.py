from tabulate import tabulate

from globals import *
from main_tools import *


def chrono(function):
    """Décorateur: Calcule le temps en secondes que met une fonction à s'executer.\n
    Placer @ chrono dans la ligne précédent le def de la fonction."""

    def wrapper(*args, **kwargs):
        """Décore la fonction avec un calcul du temps."""
        # retourne le temps en secondes depuis le 01/01/1970.
        # (Le temps "epoch").
        start = time()

        result = function(*args, **kwargs)

        end = time()
        # Différence entre 2 temps "epochs", celui qui est gardé dans "start", et celui qui sera gardé dans "end". ;)
        time_spent = end - start

        print(f"{str(args[0]) + ': ' if args else ''}{time_spent:.2f}\"")
        print(f"{str(args[0]) + ': ' if args else ''}{time_spent:.2f}\"")

        return result

    wrapper.__doc__ = function.__doc__
    return wrapper


if __name__ == "__main__":

    cls("sub TOOLS()")

    if 0:
        a = 777
        b = 888
        c = "111"
        d = (1, 2, 3, 4, "555")
        pf("a, b, c")
        ls()
        pf("a, b, c, d")
        exit()
        pf("a, b, c, d, a, c")
        pf("a, b, c, d, a, c, b, d, b, c, a")
        ls()
        exit()

        import json

        print(json.dumps(d, indent=4))

        vars = (a, b, c, d, b, c, d, b, c, a)
        pf("vars")
        # print("vars", vars)

    def vv(v):
        return f"<{type(v).__name__}> {v}"

        values = [vv(a) for a in vars]

    # print(values)

    # lengths = sum([len(str(v)) for v in values]) + 2 * len(vars)
    # print(lengths)
    # exit()
    # # Example usage:
    # text = "<list> [<int> 777, <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 888, <str> 111, <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 777]"

    # formatted_text = format_string(text, 44)
    # print(text + "\n\n\n" + formatted_text)
