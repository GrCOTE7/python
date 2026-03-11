from re import I, L
import sys

# sys.path.append("c:/laragon/www/PYTHON/python/tools/")
# from tools import *
# from tools import cls
from pathlib import Path

from cycler import V

sys.path.append(str(Path(__file__).parent.parent.parent / "tools"))
from tools import *
from tools import cls, pf

if __name__ == "__main__":

    cls("Dial Thomas / PyPRO")
    reaction = [
        "Au début, j'comprenais pas trop...",
        "Après, j'crois qu'j'ai compris la vanne...",
        "Et maintenant, j'ai compris :",
        "Mais j'cherche encore le lien qui permet d'acheter cette tablette !!!",
        "Au final: Ha, ha, ha... Merci ! ;-)",
    ]
    soluceThomas = """print("\\n".join(f"\\033[1;33;40m{idx}\\033[0;37;40m: Ok, ok... {txt}" for idx, txt in enumerate(reaction)))"""
    soluceGrCOTE7 = """print(*map(lambda t: f"\b\033[1;33;40m{t[0]}\033[0;37;40m: Ok, ok... {t[1]}\n", enumerate(reaction),)"""
    print("Recherche de la façon la + compacte...:")
    soluceChatGPT = """print(*(f"\b\033[1;33;40m{idx}\033[0;37;40m: Ok, ok... {txt}\n" for idx, txt in enumerate(reaction)))"""
    pf("len(soluceThomas),len(soluceGrCOTE7), len(soluceChatGPT)", 2)
    print(
        *(
            f"\b\033[1;33;40m{idx}\033[0;37;40m: Ok, ok... {txt}\n"
            for idx, txt in enumerate(reaction)
        )
    )
    print(
        *(
            f"\033[1;33;40m{idx}\033[0;37;40m:Ok, ok...{txt}"
            for idx, txt in enumerate(reaction)
        ),
        sep="\n",
    )

    exit()
