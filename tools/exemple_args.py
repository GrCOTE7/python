import lorem, random
from tools import cls, cliW, ls, sb, eb, pf, exit
from sub_tools import cliWR, caller_info, nf, pf, tbl

if __name__ == "__main__":
    cls()

    # Définition de la fonction
    def exemple(*args, **kwargs):
        print("Arguments positionnels :", f"{type(args).__name__} {args=}")
        print("Arguments nommés :", f"{type(kwargs).__name__} {kwargs=}")

    # Utilisation de la fonction
    exemple(1, 2, 3, name="Alice", age=25)

    exit()
    pass
