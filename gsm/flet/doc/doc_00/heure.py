import sys
from pathlib import Path
import flet as ft
from datetime import datetime


tools_path = Path(__file__).parent.parent.parent.parent.parent.parent / "tools"
sys.path.append(str(tools_path))

from tools import *
import time

def main(page: ft.Page):

    t = ft.Text()
    page.add(t)

    page.controls.append(ft.Text("Hello, Guy!", size=25, color="green", weight="bold"))
    page.update()

    while True:
        now = datetime.now()
        t.value = f"{now.hour: >2}:{now.minute:0>2}:{now.second:0>2}"

        # Effacer la ligne précédente avant d'afficher la nouvelle
        sys.stdout.write(
            "\033[1A\033[K"
        )  # \033[1A = remonter d'une ligne, \033[K = effacer la ligne
        sys.stdout.write(f"\r{t.value}")
        sys.stdout.flush()  # Assurer un affichage immédiat

        time.sleep(1)
        page.update()

    # for i in range(0,20000001, 100):
    #     t.value = f"Step {nf(i,0): >11}"
    #     page.update()
    #     # time.sleep(.1)

    # exit()

ft.app(main)
