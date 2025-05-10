import lorem, random

from globals import *
from tools import *

cls(f"Test pour {sb}mes tools{eb}")

if __name__ == "__main__":

    def lineWrap(items, w=cliW, prt=0) -> list:
        res = []
        indexLast = 0
        lineSum = 0
        for index, v in enumerate(items):
            cumul = len(str(v)) if type(v) == str else v
            lineSum += cumul
            # 2ar calcul du delta : 1 space / car.
            if lineSum > w - 8:
                res.append(tuple(items[indexLast:index]))
                indexLast = index
                lineSum = cumul
                # 2ar ici faire  str complète directement
        res.append(tuple(items[indexLast:]))  # Ajouter le dernier groupe
        if prt:
            print(f"{res=}")
        return res

    text = lorem.paragraph().split()
    print(text)
    ls()

    res = lineWrap(text, cliW, 1)
    import pprint

    # pprint.pprint(res)
    # pprint.pprint(res, width=5)

    ls()
    # print(repr(res))
    # ls()

    for i, tup in enumerate(res):
        if i == len(res) - 10:  # Vérifie si c'est le dernier élément
            print(*tup, sep="", end="\n")
        else:
            print(*tup, sep=" ", end="\n")

    print("-" * cliW)
    print(str(cliW).center(cliW))
    print("-" * cliW)

    exit()

    # for l in range(1, 8):
    #     gras = "\x1b[1m" if not l % 3 else "\033[0m"
    #     print(f"{sb}{l: >3} {' '*3}→{s[0]: >10}{' '*5}{s[1]: >3}\033[0m")

    # class _Lorem:
    #     def paragraph(self, words=50):
    #         return " ".join(["Lorem ipsum"] * words)  # Exemple : texte factice

    # def paragraph(*args, **kwargs):
    #     return _Lorem().paragraph(*args, **kwargs)

    # print(paragraph(10))  # Générera une phrase Lorem Ipsum de 10 mots
