import sys, os
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

tools_path = Path(__file__).parent.parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import dg, fg, lg, cls, exit, pf

cls("Jeu/")

# * Pour créer un jeu en python (10 parties - Graven) https://www.youtube.com/watch?v=Ti_Engsqbic
# Réf.: https://pyga.me/docs/

if __name__ == "__main__":
    pass
