import json
from pathlib import Path
import flet as ft

from main_tools import *

# Script pour ajouter un badge "Open in Colab" à tous les notebooks d'un repo GitHub
# et l'import du chrono (class Top)


GITHUB_USER = "GrCOTE7"
REPO = "deep_learning_course"
BRANCH = "main"  # ou "main" selon ton repo

def add_badge_to_notebook(nb_path: Path):
    with nb_path.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    # Badge Colab
    badge = f"""
<a href="https://colab.research.google.com/github/{GITHUB_USER}/{REPO}/blob/{BRANCH}/{nb_path.as_posix()}" target="_parent">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
"""

# https://colab.research.google.com/github/GrCOTE7/deep_learning_course/blob/gc7/01-01%20Introduction%20au%20Deep%20Learning.ipynb

    first_cell = nb["cells"][0]

    # Si la première cellule contient déjà un badge → on ne double pas
    if first_cell["cell_type"] == "markdown" and "colab-badge" in "".join(
        first_cell["source"]
    ):
        print(f"Badge déjà présent : {nb_path}")
        return

    # Sinon on insère une nouvelle cellule Markdown au début
    nb["cells"].insert(0, {"cell_type": "markdown", "metadata": {}, "source": [badge]})

    with nb_path.open("w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)

    print(f"Badge ajouté : {nb_path}")


def files_list():
    
    # folder = Path(r"D:\Py\tutos\kevindegila\2_DeepLearning_160")  # 19 fichiers
    folder = Path(r"D:\Py\tutos\machinelearnia") # 3 fichiers
    files = []

    for nb_file in folder.glob("*.ipynb"):
        files.append(nb_file)

    return files


def add_badge_and_timer(nb_path: Path):
    with nb_path.open("r", encoding="utf-8") as f:
        nb = json.load(f)

    # Badge Colab (cellule 1)
    badge = f"""
<a href="https://colab.research.google.com/github/{GITHUB_USER}/{REPO}/blob/{BRANCH}/{nb_path.as_posix()}" target="_parent">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
"""

    # Code chrono start (cellule 2)
    chrono_start = [
        "from top import Top\n",
        "t = Top()\n",
        "t.start()\n",
    ]

    # stop chrono (cellule finale)
    chrono_stop = [
        "t.stop()\n"
    ]

    # 1) Cellule Markdown du badge
    badge_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [badge]
    }

    # 2) Cellule Code du chrono (start)
    chrono_start_cell = {
        "cell_type": "code",
        "metadata": {},
        "source": chrono_start,
        "outputs": [],
        "execution_count": None
    }

    # 3) Cellule Code du chrono (stop)
    chrono_stop_cell = {
        "cell_type": "code",
        "metadata": {},
        "source": chrono_stop,
        "outputs": [],
        "execution_count": None
    }

    # On insère au début (mais on NE SAUVEGARDE PAS)
    nb["cells"].insert(0, chrono_start_cell)
    nb["cells"].insert(0, badge_cell)

    # On ajoute la cellule finale
    nb["cells"].append(chrono_stop_cell)

    print(f"Modifications préparées (non sauvegardées) pour : {nb_path}")

    # On sauvegarde
    # with nb_path.open("w", encoding="utf-8") as f:
    #     json.dump(nb, f, indent=2, ensure_ascii=False)

    # print(f"Modifié : {nb_path}")
    print(nb['cells'])


def main():

    files=files_list()
        
    # print(len(files))
    
    # for f in files:
    #     print(f)
    f0 = files[len(files)-1]
    # print(f0)
    add_badge_to_notebook(f0)
    # add_badge_and_timer(f0) # À la fin

# Parcours récursif du repo
# for nb_file in Path(".").rglob("*.ipynb"):
#     # add_badge_to_notebook(nb_file)
#     sayHi()

if __name__ == "__main__":

    cls()
    
    print()
    main()
    exit()