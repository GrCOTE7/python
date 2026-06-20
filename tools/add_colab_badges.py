import json
from pathlib import Path
import flet as ft

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


def sayHi():
    print ('hi')

# Parcours récursif du repo
# for nb_file in Path(".").rglob("*.ipynb"):
#     # add_badge_to_notebook(nb_file)
#     sayHi()
    
sayHi()
