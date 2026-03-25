import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "tools"))
from tools.tools import *
# from pymox_kit import *

# Redéfinir print pour utiliser sys.__stdout__ par défaut
_builtin_print = print


def print(*args, **kwargs):
    if "file" not in kwargs:
        kwargs["file"] = sys.__stdout__
    _builtin_print(*args, **kwargs)


if __name__ == "__main__":
    
    cols = CLIWR

    title = "Démo intérêts des fonctions cls(), sl(), ls() et nf()"

    cls(f"{title.capitalize()}")

    ls(CYAN)

    def nombres_espaces(cols):
        total = 0
        i = 0
        while True:
            s = str(i) + " "
            if total + len(s) > cols:
                break
            yield str(i)
            total += len(s)
            i += 1
    # print(" ".join(nombres_espaces(cols)))
    print(*nombres_espaces(cols))

    # sl()
    print('\n'+f"{' 1 façon de centrer': ^{cols}}")
    print(" & 1 autre \x1b[3mfaçon\x1b[0m 😉 !".center(cols+4), end='\b')
    
    sl(FRENCH)
    
    n = 123456.789
    print(f'Format rapide d\'un nombre : nf({n}) → {nf(n)}')
    exit()
