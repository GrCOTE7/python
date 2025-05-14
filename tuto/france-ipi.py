import sys

# sys.path.append("c:/laragon/www/PYTHON/python/tools/")
# from tools import *
# from tools import cls
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *

# Réf.: https://www.france-ioi.org/

if __name__ == "__main__":

    cls("France-IOI")

    print("Tout droit tu grimperas,")
    print("La clé tu trouveras,")
    print("Habile tu seras,")
    print("Quand tu les porteras,")
    print("Et avec le chef tu reviendras !")

    exit()
