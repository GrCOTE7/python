import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent / "tools"))
from globals import CLIWR
from main_tools import cls, sl, ls
from tools import *
from pf_tools import pf

if __name__ == "__main__":
    cls()
    def aFunction() -> None:
        print("\nAppel de aFunction()... Juste pour...: exit() !\n")
        exit()
    def hello(name: str = None, toPrint=True) -> None | str:
        s = "Hello " + ("World" if name is None else name) + "!"
        return s if not toPrint else print(s)
    print("Début script →\n")

    s = hello("PyPasPro", 0)
    print(s.replace("Pas", "") + "\n" + sl(YELLOW, toPrint=0) + hello(toPrint=0))  # type: ignore

    a = 2
    b = "3"
    c = "a+b → " + str((a + int(b)))
    [pf("a,b, c", i, 1 if i == 1 else 0) for i in range(1, 3)]
    print()

    [ print(f"Couleur n°{c}: " + sl(c, w=CLIWR - len("Couleur n°x: "), toPrint=0)) for c in range(8) ]

    print(f"\n{'← Fin du script': >{CLIWR}}")
    aFunction() #2ar Cas particulier ( Devrait être + avant... ;-) )
    exit()  # @i Jamais atteint ;-) !
